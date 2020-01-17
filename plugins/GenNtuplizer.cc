// -*- C++ -*-
//
// Package:    Analyzer/GenNtuplizer
// Class:      GenNtuplizer
// 
/**\class GenNtuplizer GenNtuplizer.cc Analyzer/LLP2018/plugins/GenNtuplizer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Lisa Benato
//         Created:  Fri, 1 Nov 2019 09:48:39 GMT
//
//


// system include files
#include <memory>
#include <iostream>//compute time
#include <chrono>//compute time
#include <ctime>//compute time

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

//Trigger
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

//Reco Jet classes
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

//Pat classes
//#include "DataFormats/PatCandidates/interface/MET.h"
//#include "DataFormats/PatCandidates/interface/Jet.h"
//#include "DataFormats/JetReco/interface/CaloJet.h"
//#include "DataFormats/JetReco/interface/CaloJetCollection.h"
//#include "DataFormats/PatCandidates/interface/Muon.h"
//#include "DataFormats/PatCandidates/interface/Electron.h"
//#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TTree.h"
#include <string>

//#include "JetAnalyzer.h"
//#include "RecoJetAnalyzer.h"
//#include "CaloJetAnalyzer.h"
#include "GenAnalyzer.h"
//#include "PileupAnalyzer.h"
//#include "RecoTriggerAnalyzer.h"
#include "TriggerAnalyzer.h"
//#include "PFCandidateAnalyzer.h"
//#include "VertexAnalyzer.h"
//#include "ElectronAnalyzer.h"
//#include "RecoElectronAnalyzer.h"
//#include "MuonAnalyzer.h"
//#include "TauAnalyzer.h"
//#include "PhotonAnalyzer.h"
//#include "RecoPhotonAnalyzer.h"
//#include "RecoObjects.h"
//#include "RecoObjectsFormat.h"
#include "Objects.h"
#include "ObjectsFormat.h"
//#include "DTAnalyzer.h"
//#include "CSCAnalyzer.h"
//#include "StandAloneMuonsAnalyzer.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class GenNtuplizer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit GenNtuplizer(const edm::ParameterSet&);
      ~GenNtuplizer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

    // ----------member data ---------------------------
    edm::ParameterSet GenPSet;
    //edm::ParameterSet PileupPSet;
    edm::ParameterSet TriggerPSet;

    GenAnalyzer* theGenAnalyzer;
    //PileupAnalyzer* thePileupAnalyzer;
    TriggerAnalyzer* theTriggerAnalyzer;

    double MinGenBpt, MaxGenBeta, MinGenBradius2D, MaxGenBradius2D, MinGenBetaAcc, MaxGenBetaAcc;
    //bool WriteGenVBFquarks, 
    bool WriteGenHiggs, WriteGenBquarks, WriteGenLLPs;

    //std::vector<GenPType> GenVBFquarks;
    std::vector<GenPType> GenBquarks;
    std::vector<GenPType> GenLLPs;
    GenPType GenHiggs;

    std::map<std::string, bool> TriggerMap;
    std::map<std::string, int> PrescalesTriggerMap;
    std::map<std::string, bool> MetFiltersMap;

    bool isVerbose, isVerboseTrigger;
    bool isMC;
    long int EventNumber, LumiNumber, RunNumber;//, nPV, nSV;
    float EventWeight;
    float GenEventWeight;
    //float PUWeight, PUWeightUp, PUWeightDown;
    
    float m_pi, gen_b_radius, gen_b_radius_2D;
    //MET filters
    bool BadPFMuonFlag, BadChCandFlag;
    //Pre-firing
    long int nGenBquarks, nGenLL;
    //Initialize tree                                                                                                                     
    edm::Service<TFileService> fs;
    TTree* tree;


};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
GenNtuplizer::GenNtuplizer(const edm::ParameterSet& iConfig):
    GenPSet(iConfig.getParameter<edm::ParameterSet>("genSet")),
    //PileupPSet(iConfig.getParameter<edm::ParameterSet>("pileupSet")),
    TriggerPSet(iConfig.getParameter<edm::ParameterSet>("triggerSet")),
    MinGenBpt(iConfig.getParameter<double>("minGenBpt")),
    MaxGenBeta(iConfig.getParameter<double>("maxGenBeta")),
    MinGenBradius2D(iConfig.getParameter<double>("minGenBradius2D")),
    MaxGenBradius2D(iConfig.getParameter<double>("maxGenBradius2D")),
    MinGenBetaAcc(iConfig.getParameter<double>("minGenBetaAcc")),
    MaxGenBetaAcc(iConfig.getParameter<double>("maxGenBetaAcc")),
    //WriteGenVBFquarks(iConfig.getParameter<bool>("writeGenVBFquarks")),
    WriteGenHiggs(iConfig.getParameter<bool>("writeGenHiggs")),
    WriteGenBquarks(iConfig.getParameter<bool>("writeGenBquarks")),
    WriteGenLLPs(iConfig.getParameter<bool>("writeGenLLPs")),
    isVerbose(iConfig.getParameter<bool> ("verbose"))

{

    theGenAnalyzer          = new GenAnalyzer(GenPSet, consumesCollector());
    //thePileupAnalyzer       = new PileupAnalyzer(PileupPSet, consumesCollector());
    theTriggerAnalyzer      = new TriggerAnalyzer(TriggerPSet, consumesCollector());

    std::vector<std::string> TriggerList(TriggerPSet.getParameter<std::vector<std::string> >("paths"));
    for(unsigned int i = 0; i < TriggerList.size(); i++) TriggerMap[ TriggerList[i] ] = false;
    for(unsigned int i = 0; i < TriggerList.size(); i++) PrescalesTriggerMap[ TriggerList[i] ] = -1;
    std::vector<std::string> MetFiltersList(TriggerPSet.getParameter<std::vector<std::string> >("metpaths"));
    for(unsigned int i = 0; i < MetFiltersList.size(); i++) MetFiltersMap[ MetFiltersList[i] ] = false;

    //now do what ever initialization is needed

    usesResource("TFileService");

    if(isVerbose) std::cout << "---------- STARTING ----------" << std::endl;


}


GenNtuplizer::~GenNtuplizer()
{
 
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    if(isVerbose) std::cout << "---------- ENDING  ----------" << std::endl;

    delete theGenAnalyzer;
    //delete thePileupAnalyzer;
    delete theTriggerAnalyzer;
}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    auto start = std::chrono::system_clock::now();//time!
    using namespace edm;
    using namespace reco;
    using namespace std;

    // Initialize types
    ObjectsFormat::ResetGenPType(GenHiggs);

    isMC = false;
    isVerboseTrigger = false;
    EventNumber = LumiNumber = RunNumber = 0;
    //nPV = 0;
    GenEventWeight = EventWeight = 1.;
    //PUWeight = PUWeightDown = PUWeightUp = 1.;
    nGenBquarks = nGenLL = 0;
    m_pi = 0.;
    gen_b_radius = -1.;
    gen_b_radius_2D = -1.;

    //Event info                                                                
    isMC = !iEvent.isRealData();
    EventNumber = iEvent.id().event();
    LumiNumber = iEvent.luminosityBlock();
    RunNumber = iEvent.id().run();

    //GenEventWeight
    GenEventWeight = theGenAnalyzer->GenEventWeight(iEvent);
    EventWeight *= GenEventWeight;


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Gen particles
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    
    //GenVBFquarks.clear();
    GenLLPs.clear();
    GenBquarks.clear();

    //std::vector<reco::GenParticle> GenVBFVect = theGenAnalyzer->FillVBFGenVector(iEvent);
    std::vector<reco::GenParticle> GenHiggsVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,25,22);
    std::vector<reco::GenParticle> GenLongLivedVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,9000006,22);
    std::vector<reco::GenParticle> GenBquarksVect;

    nGenLL = GenLongLivedVect.size();
    int nGenBinAcceptance = 0;
    float gen_b_radius_2D = -1.;

    if(nGenLL>0)
      {
	//GenBquarksVect = theGenAnalyzer->FillGenVectorByIdStatusAndMotherAndKinAndRadius2D(iEvent,5,23,9000006,float(MinGenBpt),float(MaxGenBeta),float(MinGenBradius2D),float(MaxGenBradius2D));
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdStatusAndMotherAndKin(iEvent,5,23,9000006,float(MinGenBpt),float(MaxGenBeta));
      }
    else
      {
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdAndStatusAndKin(iEvent,5,23,float(MinGenBpt),float(MaxGenBeta));
      }

    nGenBquarks = GenBquarksVect.size();

    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
      {
	gen_b_radius_2D = GenBquarksVect.at(b).mother()? sqrt(pow(GenBquarksVect.at(b).vx() - GenBquarksVect.at(b).mother()->vx(),2) + pow(GenBquarksVect.at(b).vy() - GenBquarksVect.at(b).mother()->vy(),2)) : -1.;
	if(gen_b_radius_2D > MinGenBradius2D && gen_b_radius_2D < MaxGenBradius2D && fabs(GenBquarksVect.at(b).eta())>MinGenBetaAcc && fabs(GenBquarksVect.at(b).eta())<MaxGenBetaAcc) nGenBinAcceptance++;
      }

    //if(nGenBinAcceptance<1) return;//!Remove!!!
    if(isVerbose) std::cout << "Gen b quarks in acceptance: " << nGenBinAcceptance << std::endl;


    //for(unsigned int i = 0; i < GenVBFVect.size(); i++) GenVBFquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) GenLLPs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenBquarksVect.size(); i++) GenBquarks.push_back( GenPType() );
    
    if(nGenBquarks>0) gen_b_radius = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2) + pow(GenBquarksVect.at(0).vz() - GenBquarksVect.at(0).mother()->vz(),2)) : -1.;
    if(nGenBquarks>0) gen_b_radius_2D = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2)) : -1.;
    if(nGenLL>0) m_pi = GenLongLivedVect.at(0).mass();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Pu weight and number of vertices
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(isVerbose) std::cout << "Pile-up" << std::endl;
    //PUWeight     = thePileupAnalyzer->GetPUWeight(iEvent);//calculates pileup weights
    //PUWeightUp   = thePileupAnalyzer->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
    //PUWeightDown = thePileupAnalyzer->GetPUWeightDown(iEvent);//syst uncertainties due to pileup
    //nPV = thePileupAnalyzer->GetPV(iEvent);//calculates number of vertices
    
    //EventWeight *= PUWeight;

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Trigger and MET filters
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //if(isVerbose) std::cout << "Trigger and met filters" << std::endl;
    theTriggerAnalyzer->FillTriggerMap(iEvent, TriggerMap, PrescalesTriggerMap, isVerboseTrigger);
    theTriggerAnalyzer->FillMetFiltersMap(iEvent, MetFiltersMap);
    BadPFMuonFlag = theTriggerAnalyzer->GetBadPFMuonFlag(iEvent);
    BadChCandFlag = theTriggerAnalyzer->GetBadChCandFlag(iEvent);
    //theTriggerAnalyzer->FillL1FiltersMap(iEvent, L1FiltersMap);

    //-----------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Fill objects
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    auto end = std::chrono::system_clock::now();//time!
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    if(isVerbose)
      {
	std::cout << "**************************************************" << std::endl;
	std::cout << "finished Analyze method computations at " << std::ctime(&end_time)
		  << "elapsed time: " << elapsed_seconds.count() << "s\n";
	std::cout << "**************************************************" << std::endl;
      }

    if(isVerbose) std::cout << " - Filling objects" << std::endl;
    
    //if (WriteGenVBFquarks) for(unsigned int i = 0; i < GenVBFVect.size(); i++) ObjectsFormat::FillGenPType(GenVBFquarks[i], &GenVBFVect[i]);
    if (WriteGenHiggs) for(unsigned int i = 0; i < GenHiggsVect.size(); i++) ObjectsFormat::FillGenPType(GenHiggs, &GenHiggsVect[i]);
    if (WriteGenLLPs) for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) ObjectsFormat::FillGenPType(GenLLPs[i], &GenLongLivedVect[i]);
    if (WriteGenBquarks) for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillGenPType(GenBquarks[i], &GenBquarksVect[i]);


    if(isVerbose) {
      //Write a summary, in verbose mode
      std::cout << " --- Event n. " << iEvent.id().event() << ", lumi " << iEvent.luminosityBlock() << ", run " << iEvent.id().run() << std::endl;

      std::cout << "number of Gen B quarks:  " << GenBquarksVect.size() << std::endl;
      for(unsigned int i = 0; i < GenBquarksVect.size(); i++) {std::cout << "  Gen B quark  [" << i << "]\tpt: " << GenBquarksVect[i].pt() << "\teta: " << GenBquarksVect[i].eta() << "\tphi: " << GenBquarksVect[i].phi() << "\tradius (in cm): " << ( GenBquarksVect[i].mother() ? sqrt(pow(GenBquarksVect[i].vx() - GenBquarksVect[i].mother()->vx(),2) + pow(GenBquarksVect[i].vy() - GenBquarksVect[i].mother()->vy(),2) + pow(GenBquarksVect[i].vz() - GenBquarksVect[i].mother()->vz(),2)) : -1000. ) << "\tradius 2D (in cm): " << ( GenBquarksVect[i].mother() ? sqrt(pow(GenBquarksVect[i].vx() - GenBquarksVect[i].mother()->vx(),2) + pow(GenBquarksVect[i].vy() - GenBquarksVect[i].mother()->vy(),2)) : -1000. ) << std::endl;}

    }



    //Fill tree
    tree -> Fill();
    if(isVerbose) std::cout << "TREE FILLED!!!!!!!!!!!! Go to next event...--->" << std::endl;

#ifdef THIS_IS_AN_EVENT_EXAMPLE
    Handle<ExampleData> pIn;
    iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
    ESHandle<SetupData> pSetup;
    iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
GenNtuplizer::beginJob()
{
  //Tree branches                                                                                                                       
  //tree = fs->make<TTree>("tree", "tree");
  //

   tree = fs->make<TTree>("tree", "tree");
   tree -> Branch("isMC" , &isMC, "isMC/O");
   tree -> Branch("EventNumber" , &EventNumber , "EventNumber/L");
   tree -> Branch("LumiNumber" , &LumiNumber , "LumiNumber/L");
   tree -> Branch("RunNumber" , &RunNumber , "RunNumber/L");
   tree -> Branch("EventWeight", &EventWeight, "EventWeight/F");
   tree -> Branch("GenEventWeight", &GenEventWeight, "GenEventWeight/F");
   //tree -> Branch("PUWeight", &PUWeight, "PUWeight/F");
   //tree -> Branch("PUWeightUp", &PUWeightUp, "PUWeightUp/F");
   //tree -> Branch("PUWeightDown", &PUWeightDown, "PUWeightDown/F");
   tree -> Branch("nGenBquarks" , &nGenBquarks , "nGenBquarks/L");
   tree -> Branch("nGenLL" , &nGenLL , "nGenLL/L");
   tree -> Branch("gen_b_radius" , &gen_b_radius , "gen_b_radius/F");
   tree -> Branch("gen_b_radius_2D" , &gen_b_radius_2D , "gen_b_radius_2D/F");
   tree -> Branch("m_pi" , &m_pi , "m_pi/F");
   tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
   tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
   // Set trigger branches
   for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   for(auto it = MetFiltersMap.begin(); it != MetFiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   //for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());

   tree -> Branch("GenHiggs", &GenHiggs.pt, ObjectsFormat::ListGenPType().c_str());
   tree -> Branch("GenLLPs", &GenLLPs);
   tree -> Branch("GenBquarks", &GenBquarks);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenNtuplizer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenNtuplizer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenNtuplizer);
