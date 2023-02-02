// -*- C++ -*-
//
// Package:    Analyzer/GenNtuplizerCalo
// Class:      GenNtuplizerCalo
// 
/**\class GenNtuplizerCalo GenNtuplizerCalo.cc Analyzer/LLP2018/plugins/GenNtuplizerCalo.cc

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
//#include "FWCore/Common/interface/TriggerNames.h"
//#include "DataFormats/Common/interface/TriggerResults.h"
//#include "DataFormats/HLTReco/interface/TriggerObject.h"
//#include "DataFormats/HLTReco/interface/TriggerEvent.h"
//#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
//#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
//#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

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

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"

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
//#include "TriggerAnalyzer.h"
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

class GenNtuplizerCalo : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit GenNtuplizerCalo(const edm::ParameterSet&);
      ~GenNtuplizerCalo();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

    // ----------member data ---------------------------
    edm::ParameterSet GenPSet;
    //edm::ParameterSet PileupPSet;
    //edm::ParameterSet TriggerPSet;

    edm::EDGetTokenT<GenEventInfoProduct> genEventInfoToken;
    edm::EDGetTokenT<GenLumiInfoHeader> genLumiInfoToken;
    std::string     Model;

    GenAnalyzer* theGenAnalyzer;
    //PileupAnalyzer* thePileupAnalyzer;
    //TriggerAnalyzer* theTriggerAnalyzer;

    int idLLP1, idLLP2;
    int idHiggs1, idHiggs2, idMotherB1, idMotherB2, statusLLP, statusHiggs;
    double MinGenBpt, MaxGenBeta, MinGenBradius2D, MaxGenBradius2D, MinGenBetaAcc, MaxGenBetaAcc;
    //bool WriteGenVBFquarks, 
    bool WriteGenHiggs, WriteGenBquarks, WriteGenLLPs;

    //std::vector<GenPType> GenVBFquarks;
    std::vector<GenPType> GenBquarks;
    std::vector<GenPType> GenLLPs;
    std::vector<GenPType> GenHiggs;
    std::vector<GenPType> GenGravitinos;

    //std::map<std::string, bool> TriggerMap;
    //std::map<std::string, int> PrescalesTriggerMap;
    //std::map<std::string, bool> MetFiltersMap;

    bool isSignal;
    bool isVerbose;//, isVerboseTrigger;
    bool isMC;
    long int EventNumber, LumiNumber, RunNumber;//, nPV, nSV;
    float EventWeight;
    float GenEventWeight;
    //float PUWeight, PUWeightUp, PUWeightDown;
    
    float m_pi;//, gen_b_radius, gen_b_radius_2D;
    int m_chi;
    int ctau;
    bool is_central;

    //MET filters
    //bool BadPFMuonFlag, BadChCandFlag;
    //Pre-firing
    long int nGenBquarks, nGenLL;
    int nLLPInCalo;
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
GenNtuplizerCalo::GenNtuplizerCalo(const edm::ParameterSet& iConfig):
    GenPSet(iConfig.getParameter<edm::ParameterSet>("genSet")),
    //PileupPSet(iConfig.getParameter<edm::ParameterSet>("pileupSet")),
    //TriggerPSet(iConfig.getParameter<edm::ParameterSet>("triggerSet")),
    idLLP1(iConfig.getParameter<int>("idLLP1")),
    idLLP2(iConfig.getParameter<int>("idLLP2")),
    idHiggs1(iConfig.getParameter<int>("idHiggs1")),
    idHiggs2(iConfig.getParameter<int>("idHiggs2")),
    idMotherB1(iConfig.getParameter<int>("idMotherB1")),
    idMotherB2(iConfig.getParameter<int>("idMotherB2")),
    statusLLP(iConfig.getParameter<int>("statusLLP")),
    statusHiggs(iConfig.getParameter<int>("statusHiggs")),
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
    isSignal(iConfig.getParameter<bool> ("signal")),
    isVerbose(iConfig.getParameter<bool> ("verbose"))

{

    theGenAnalyzer          = new GenAnalyzer(GenPSet, consumesCollector());
    //thePileupAnalyzer       = new PileupAnalyzer(PileupPSet, consumesCollector());
    //theTriggerAnalyzer      = new TriggerAnalyzer(TriggerPSet, consumesCollector());

    //std::vector<std::string> TriggerList(TriggerPSet.getParameter<std::vector<std::string> >("paths"));
    //for(unsigned int i = 0; i < TriggerList.size(); i++) TriggerMap[ TriggerList[i] ] = false;
    //for(unsigned int i = 0; i < TriggerList.size(); i++) PrescalesTriggerMap[ TriggerList[i] ] = -1;
    //std::vector<std::string> MetFiltersList(TriggerPSet.getParameter<std::vector<std::string> >("metpaths"));
    //for(unsigned int i = 0; i < MetFiltersList.size(); i++) MetFiltersMap[ MetFiltersList[i] ] = false;

    //GenLumiInfo
    edm::InputTag genLumiInfo = edm::InputTag(std::string("generator"));
    genLumiInfoToken          = consumes <GenLumiInfoHeader,edm::InLumi> (genLumiInfo);

    edm::InputTag genInfoProduct = edm::InputTag(std::string("generator"));
    genEventInfoToken         = consumes <GenEventInfoProduct> (genInfoProduct);


    //now do what ever initialization is needed

    usesResource("TFileService");


    if(isVerbose) std::cout << "---------- STARTING ----------" << std::endl;


}


GenNtuplizerCalo::~GenNtuplizerCalo()
{
 
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    if(isVerbose) std::cout << "---------- ENDING  ----------" << std::endl;

    delete theGenAnalyzer;
    //delete thePileupAnalyzer;
    //delete theTriggerAnalyzer;
}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenNtuplizerCalo::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    auto start = std::chrono::system_clock::now();//time!
    using namespace edm;
    using namespace reco;
    using namespace std;

    // Initialize types
    //ObjectsFormat::ResetGenPType(GenHiggs);

    isMC = false;
    //isVerboseTrigger = false;
    EventNumber = LumiNumber = RunNumber = 0;
    //nPV = 0;
    GenEventWeight = EventWeight = 1.;
    //PUWeight = PUWeightDown = PUWeightUp = 1.;
    nGenBquarks = nGenLL = 0;
    m_pi = 0.;
    nLLPInCalo = 0;
    m_chi = 0;
    ctau = -1;
    is_central = false;

    //gen_b_radius = -1.;
    //gen_b_radius_2D = -1.;

    //Event info                                                                
    isMC = !iEvent.isRealData();
    EventNumber = iEvent.id().event();
    LumiNumber = iEvent.luminosityBlock();
    RunNumber = iEvent.id().run();
    //std::cout<< " = = = = = = = " << std::endl;
    //std::cout<< "Event number: " << EventNumber << " Lumi number" << "\t"<< LumiNumber <<std::endl;

    //GenLumiInfo
    if(isSignal and idLLP1==1000023)
      {
	edm::Handle<GenLumiInfoHeader> GenHeader;
        iEvent.getLuminosityBlock().getByToken(genLumiInfoToken,GenHeader);
	Model = GenHeader->configDescription();

	std::stringstream parser(Model);
	std::string item;
        getline(parser, item, '_');
        if(getline(parser, item, '_'))
          {
            if(getline(parser, item, '_'))
              {
                if(getline(parser, item, '_'))
                  {
                    m_chi = atoi(item.c_str());
                    if(getline(parser, item, '_'))
                      {
                        ctau = atoi(item.c_str());
                      }
                  }
              }
          }

        if(ctau>-1 and m_chi>0) is_central = true;

      }

    if(isSignal and idLLP1==9000006)
      {
	edm::Handle<GenLumiInfoHeader> GenHeader;
        iEvent.getLuminosityBlock().getByToken(genLumiInfoToken,GenHeader);
	Model = GenHeader->configDescription();

	//std::cout << Model << std::endl;

	std::stringstream parser(Model);
	std::string item;
	std::string pre;
        getline(parser, item, '_');
        if(getline(parser, item, '_'))
          {
            if(getline(parser, item, '_'))
              {
                if(getline(parser, item, '_'))
                  {
		    m_chi = atoi( item.substr(item.find("-") + 1).c_str());
                    if(getline(parser, item, '_'))
                      {
			ctau = atoi(item.substr(item.find("-") + 1).c_str());
                      }
                  }
              }
          }

        if(ctau>-1 and m_chi>0) is_central = true;

      }


    //std::cout << "m_chi " << m_chi << std::endl;
    //std::cout << "ctau " << ctau << std::endl;
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
    GenHiggs.clear();
    GenBquarks.clear();
    GenGravitinos.clear();

    std::vector<reco::GenParticle> GenLongLivedVect = theGenAnalyzer->FillGenVectorByTwoIdsAndStatus(iEvent,idLLP1,idLLP2,statusLLP);
    nGenLL = GenLongLivedVect.size();
    //std::cout << "nGenLL: " << nGenLL << std::endl;

    //std::vector<reco::GenParticle> GenVBFVect = theGenAnalyzer->FillVBFGenVector(iEvent);
    std::vector<reco::GenParticle> GenHiggsVect;
    //std::cout << "debug idHiggs1/2: \t" << idHiggs1 << "\t" << idHiggs2 <<std::endl; 
    if(idHiggs1==idHiggs2)
      {
	GenHiggsVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idHiggs1,statusHiggs);
      }
    else
      {
	//First kind of Higgs
	GenHiggsVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idHiggs1,statusHiggs);
	//std::cout << "size of GenHiggsVect \t" << GenHiggsVect.size() << std::endl;
	//Second kind of Higgs
	std::vector<reco::GenParticle> GenHiggsVect2 = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idHiggs2,statusHiggs);
	//std::cout << "size of GenHiggsVect2 \t" << GenHiggsVect2.size() << std::endl;

	//If they don't have size 1 and 1, skip
	if(GenHiggsVect.size()!=1 and GenHiggsVect2.size()!=1 and nGenLL==2) return;

	//Concatenate and clear
	GenHiggsVect.insert(std::end(GenHiggsVect), std::begin(GenHiggsVect2), std::end(GenHiggsVect2));
	//std::cout << "size of GenHiggsVect inserted \t" << GenHiggsVect.size() << std::endl;
	GenHiggsVect2.clear();
      }

    std::vector<reco::GenParticle> GenGravitinosVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,1000022,1);
    std::vector<reco::GenParticle> GenBquarksVect;

    int nGenBinAcceptance = 0;
    float gen_b_radius_2D = -1.;
    
    float ecal_radius = 129.0;
    float max_calo_radius = 184.;
    float max_calo_z = 376.;
    float min_displacement_radius = 30;

    //Check if there are two Higgs bosons in the event --> don't need it actually!
    //if(nGenLL>0 and GenHiggsVect.size()!=2) return;
    if(nGenLL!=2) return;

    //std::cout << "\n" << std::endl;
    //std::cout << "GenHiggs IDs: \t"<< GenHiggsVect.at(0).pdgId() << "\t" << GenHiggsVect.at(1).pdgId() << std::endl;

    if(nGenLL>0)
      {
	//Can have two mothers! new function needed!!
	//Need to change all the methods using idMotherB!!
	//Will have to do it also in AOD
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdStatusAndTwoMothersAndKin(iEvent,5,23,idMotherB1,idMotherB2,float(MinGenBpt),float(MaxGenBeta));
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


    //calculate calo corrections
    std::vector<float> corrEtaDaughterLLP;
    std::vector<float> corrPhiDaughterLLP;
    std::vector<float> corrEtaGrandDaughterLLP;
    std::vector<float> corrPhiGrandDaughterLLP;
    std::vector<bool>  LLPInCalo;
    std::vector<bool>  DaughterOfLLPInCalo;
    std::vector<bool>  GrandDaughterOfLLPInCalo;

    std::vector<float> LLPRadius_Dau;
    std::vector<float> LLPX_Dau;
    std::vector<float> LLPY_Dau;
    std::vector<float> LLPZ_Dau;
    std::vector<float> LLPRadius_GrandDau;
    std::vector<float> LLPX_GrandDau;
    std::vector<float> LLPY_GrandDau;
    std::vector<float> LLPZ_GrandDau;

    
    std::vector<float> checkPtDaughterLLP;
    std::vector<float> checkPtGrandDaughterLLP;
    std::vector<float> checkEtaDaughterLLP;
    std::vector<float> checkEtaGrandDaughterLLP;
    std::vector<float> checkPhiDaughterLLP;
    std::vector<float> checkPhiGrandDaughterLLP;
    /*
    if(idMotherB==idLLP1 || idMotherB==idLLP2)
    {
        //initialize vectors       
        std::cout<< "bs from LL, need only daughter" << std::endl;
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) corrEtaDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) corrPhiDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) checkPtDaughterLLP.push_back(-1.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) checkEtaDaughterLLP.push_back(-9.);
    }
    else if(idMotherB==idHiggs)
     {
        //initialize vectors       
        std::cout<< "bs from Higgs, need grand daughter" << std::endl;
        for(unsigned int a=0; a<GenHiggsVect.size(); a++) corrEtaDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenHiggsVect.size(); a++) corrPhiDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenHiggsVect.size(); a++) checkPtDaughterLLP.push_back(-1.);
        for(unsigned int a=0; a<GenHiggsVect.size(); a++) checkEtaDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) corrEtaGrandDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) corrPhiGrandDaughterLLP.push_back(-9.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) checkPtGrandDaughterLLP.push_back(-1.);
        for(unsigned int a=0; a<GenBquarksVect.size(); a++) checkEtaGrandDaughterLLP.push_back(-9.);
    }   
    */
    
    //corr_eta_daughter vector
    //corr_phi_daughter vector
    //corr_eta_grand_daughter vector
    //corr_phi_grand_daughter vector
    
    //use idmotherb to determine wether one needs dau or grand dau corrections (heavy higgs: dau; susy: grand dau)
    std::vector<const reco::Candidate*> LLPs;

     
    //must conver reco::GenParticles into const reco::Candidate*, otherwise daughter method does not work
    //for(unsigned int l=0; l<GenLongLivedVect.size(); l++)
    //{
    //    LLPs.push_back(&(GenLongLivedVect)[l]);
    //} 
    
    //for(unsigned int l = 0; l < LLPs.size(); l++)
    //{
    //  if(LLPs.size()>1 && LLPs[l]->numberOfDaughters()>1)
    //  {
    //    std::cout << "Has these daughters: " << LLPs[l]->numberOfDaughters() << std::endl;
    //    std::cout << "pt dau 0 " << LLPs[l]->daughter(0)->pt() << std::endl;
    //  }
    //}   
    
    for(unsigned int l=0; l<GenLongLivedVect.size(); l++)
    {
         if(GenLongLivedVect.size()>1 && GenLongLivedVect.at(l).numberOfDaughters()>1)
         {
         //must conver reco::GenParticles into const reco::Candidate*, otherwise daughter method does not work
         const reco::Candidate *candLLP = &(GenLongLivedVect)[l];
         
         //float beta        = candLLP->energy()>0 ? sqrt(pow(candLLP->px(),2) + pow(candLLP->py(),2) + pow(candLLP->pz(),2))/candLLP->energy() : -1.;
         //std::cout << "Has these daughters: " << candLLP->numberOfDaughters() << std::endl;
         //const reco::Candidate * dau = candLLP->daughter(0);
         //std::cout << dau->pt() << std::endl;
         //float travelTime  = (candLLP->numberOfDaughters()>1 && beta>0) ? sqrt( pow(candLLP->daughter(0)->vx()-candLLP->vx(),2)+ pow(candLLP->daughter(0)->vy()-candLLP->vy(),2) + pow(candLLP->daughter(0)->vz()-candLLP->vz(),2) )/30*beta : -1.;
         float travelRadius = candLLP->numberOfDaughters()>1 ? sqrt( pow(candLLP->daughter(0)->vx(),2)+ pow(candLLP->daughter(0)->vy(),2) ) : -1000.;
	 float travelX      = candLLP->numberOfDaughters()>1 ? candLLP->daughter(0)->vx() : -10000.;
         float travelY      = candLLP->numberOfDaughters()>1 ? candLLP->daughter(0)->vy() : -10000.;
         float travelZ      = candLLP->numberOfDaughters()>1 ? candLLP->daughter(0)->vz() : -10000.;
         
	 bool isLLPInCaloAcceptance = travelRadius > min_displacement_radius && travelRadius < max_calo_radius && fabs(travelZ) < max_calo_z;
         
         if (isLLPInCaloAcceptance)
         {
             nLLPInCalo++;
             LLPInCalo.push_back(true);
         }
         else
         {
             LLPInCalo.push_back(false);
         }

	 
         //std::cout << " - - - - - - - - - - - - - - " << std::endl;
         //std::cout << "LLP n. " << l << std::endl;
         //std::cout << "in calo acceptance " << isLLPInCaloAcceptance << std::endl;
         //std::cout << "travelRadius " << travelRadius << std::endl;
         //std::cout << "travelZ " << travelZ << std::endl;
         
         for (unsigned int i = 0; i < candLLP->numberOfDaughters(); i++ )
         {
	   if(abs(candLLP->daughter(i)->pdgId())==idHiggs1 || abs(candLLP->daughter(i)->pdgId())==idHiggs2 || abs(candLLP->daughter(i)->pdgId())==5)//consider only higgs and b quarks
             //if(abs(candLLP->daughter(i)->pdgId())==5)//consider only higgs and b quarks
             {
               float decayVertex_x  = candLLP->daughter(i)->vx();//per daughter of llp
               float decayVertex_y  = candLLP->daughter(i)->vy();
               float decayVertex_z  = candLLP->daughter(i)->vz();            
               TLorentzVector tmp;
               tmp.SetPxPyPzE(candLLP->daughter(i)->px(), candLLP->daughter(i)->py(), candLLP->daughter(i)->pz(), candLLP->daughter(i)->energy());
               float gLLP_daughter_travel_time = (1./30.)*fabs(ecal_radius-travelRadius)/(tmp.Pt()/tmp.E());//per daughter of llp
               float x_ecal = decayVertex_x + 30. * (tmp.Px()/tmp.E())*gLLP_daughter_travel_time;
               float y_ecal = decayVertex_y + 30. * (tmp.Py()/tmp.E())*gLLP_daughter_travel_time;
               float z_ecal = decayVertex_z + 30. * (tmp.Pz()/tmp.E())*gLLP_daughter_travel_time;
             
               float phi = atan((y_ecal-decayVertex_y)/(x_ecal-decayVertex_x));
               if  (x_ecal < 0.0){
                  phi = TMath::Pi() + phi;
               }
               phi = reco::deltaPhi(phi,0.0);
               float theta = atan(sqrt(pow(x_ecal-decayVertex_x,2)+pow(y_ecal-decayVertex_y,2))/abs(z_ecal-decayVertex_z));
               float eta = -1.0*TMath::Sign(1.0, z_ecal-decayVertex_z)*log(tan(theta/2));
               corrEtaDaughterLLP.push_back(eta);
               corrPhiDaughterLLP.push_back(phi);
               checkPtDaughterLLP.push_back(candLLP->daughter(i)->pt());
               checkEtaDaughterLLP.push_back(candLLP->daughter(i)->eta());
               checkPhiDaughterLLP.push_back(candLLP->daughter(i)->phi());
               if (isLLPInCaloAcceptance)
               {
                  DaughterOfLLPInCalo.push_back(true);
               }
               else
               {
                  DaughterOfLLPInCalo.push_back(false);
               }

	       LLPRadius_Dau.push_back(travelRadius);
               LLPX_Dau.push_back(travelX);
               LLPY_Dau.push_back(travelY);
               LLPZ_Dau.push_back(travelZ);
               
               //std::cout << "\n" << std::endl;
               //std::cout << "LLP n. " << l << "; daughter n. " << i << std::endl;
               //std::cout << "decayVertex_x " << decayVertex_x << std::endl;
               //std::cout << "gLLP_daughter_travel_time " << gLLP_daughter_travel_time << std::endl;
               //std::cout << "x_ecal " << x_ecal << std::endl;
               //std::cout << "y_ecal " << y_ecal << std::endl;
               //std::cout << "z_ecal " << z_ecal << std::endl;
               //std::cout << "phi " << candLLP->daughter(i)->phi() << std::endl;
               //std::cout << "corr phi " << phi << std::endl;
               //std::cout << "eta " << candLLP->daughter(i)->eta() << std::endl;
               //std::cout << "corr theta " << theta << std::endl;
               //std::cout << "corr eta " << eta << std::endl;
               
               //std::cout << "status and id dau: " << candLLP->daughter(i)->pdgId() << "\t" << candLLP->daughter(i)->status() << std::endl;
            
             
               //granddaughters: only bs
               //if(idMotherB==idHiggs && candLLP->daughter(i)->numberOfDaughters()>1)
             
               
               const reco::Candidate *tmpDauParticle = candLLP->daughter(i);
               for (unsigned int g = 0; g < tmpDauParticle->numberOfDaughters(); g++ )
		 {
		   if(abs(candLLP->daughter(i)->daughter(g)->pdgId())==5 && (idMotherB1==25 || idMotherB1==23))
		     {
		       TLorentzVector tmpdau;
		       tmpdau.SetPxPyPzE(tmpDauParticle->daughter(g)->px(), tmpDauParticle->daughter(g)->py(), tmpDauParticle->daughter(g)->pz(), tmpDauParticle->daughter(g)->energy());
		       float gLLP_granddaughter_travel_time = (1./30.)*fabs(ecal_radius-travelRadius)/(tmpdau.Pt()/tmpdau.E());
		       float x_ecal = decayVertex_x + 30. * (tmpdau.Px()/tmpdau.E())*gLLP_granddaughter_travel_time;
		       float y_ecal = decayVertex_y + 30. * (tmpdau.Py()/tmpdau.E())*gLLP_granddaughter_travel_time;
		       float z_ecal = decayVertex_z + 30. * (tmpdau.Pz()/tmpdau.E())*gLLP_granddaughter_travel_time;
		       float phi = atan((y_ecal-decayVertex_y)/(x_ecal-decayVertex_x));
		       if  (x_ecal < 0.0) {
			 phi = TMath::Pi() + phi;
		       }
		       phi = deltaPhi(phi,0.0);
		       float theta = atan(sqrt(pow(x_ecal-decayVertex_x,2)+pow(y_ecal-decayVertex_y,2))/abs(z_ecal-decayVertex_z));
		       float eta = -1.0*TMath::Sign(1.0, z_ecal-decayVertex_z)*log(tan(theta/2));
		       corrEtaGrandDaughterLLP.push_back(eta);
		       corrPhiGrandDaughterLLP.push_back(phi);
		       checkPtGrandDaughterLLP.push_back(tmpDauParticle->daughter(g)->pt());
		       checkEtaGrandDaughterLLP.push_back(tmpDauParticle->daughter(g)->eta());
		       checkPhiGrandDaughterLLP.push_back(tmpDauParticle->daughter(g)->phi());
		       if (isLLPInCaloAcceptance)
			 {
			   GrandDaughterOfLLPInCalo.push_back(true);
			 }
		       else
			 {
			   GrandDaughterOfLLPInCalo.push_back(false);
			 }
		       LLPRadius_GrandDau.push_back(travelRadius);
		       LLPX_GrandDau.push_back(travelX);
		       LLPY_GrandDau.push_back(travelY);
		       LLPZ_GrandDau.push_back(travelZ);
		       //std::cout << "\n" << std::endl;
		       //std::cout << "LLP n. " << l << "; daughter n. " << i << "; grand daughter n. " << g << std::endl;
		       //std::cout << "decayVertex_x " << decayVertex_x << std::endl;
		       //std::cout << "gLLP_granddaughter_travel_time " << gLLP_granddaughter_travel_time << std::endl;
		       //std::cout << "x_ecal " << x_ecal << std::endl;
		       //std::cout << "y_ecal " << y_ecal << std::endl;
		       //std::cout << "z_ecal " << z_ecal << std::endl;
		       //std::cout << "phi " << tmpDauParticle->daughter(g)->phi() << std::endl;
		       //std::cout << "corr phi " << phi << std::endl;
		       //std::cout << "corr theta " << theta << std::endl;
		       //std::cout << "eta " << tmpDauParticle->daughter(g)->eta() << std::endl;
		       //std::cout << "corr eta " << eta << std::endl;
		       //std::cout << "status and id grand dau: " << tmpDauParticle->daughter(g)->pdgId() << "\t" << tmpDauParticle->daughter(g)->status() << std::endl;
		     }
		 }//granddau loop
             }//if
         
         }//dau loop
         
         }//ask to have 2 daughters and size>1
    }//loop on LLPs

    /*
    std::cout << "check pt higgs: " << std::endl;
    for(unsigned int a=0;a<GenHiggsVect.size();a++) std::cout << GenHiggsVect.at(a).pt() << std::endl;
    std::cout << "check pt bquarks: " << std::endl;
    for(unsigned int a=0;a<GenBquarksVect.size();a++) std::cout << GenBquarksVect.at(a).pt() << std::endl;
    std::cout << "checkPtDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<checkPtDaughterLLP.size();a++) std::cout << checkPtDaughterLLP.at(a) << std::endl;
    std::cout << "checkPtGrandDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<checkPtGrandDaughterLLP.size();a++) std::cout << checkPtGrandDaughterLLP.at(a) << std::endl;
    std::cout << "check eta higgs: " << std::endl;
    for(unsigned int a=0;a<GenHiggsVect.size();a++) std::cout << GenHiggsVect.at(a).eta() << std::endl;
    std::cout << "check eta bquarks: " << std::endl;
    for(unsigned int a=0;a<GenBquarksVect.size();a++) std::cout << GenBquarksVect.at(a).eta() << std::endl;
    std::cout << "checkEtaDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<checkEtaDaughterLLP.size();a++) std::cout << checkEtaDaughterLLP.at(a) << std::endl;
    std::cout << "corrEtaDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<corrEtaDaughterLLP.size();a++) std::cout << corrEtaDaughterLLP.at(a) << std::endl;
    std::cout << "checkEtaGrandDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<checkEtaGrandDaughterLLP.size();a++) std::cout << checkEtaGrandDaughterLLP.at(a) << std::endl; 
    std::cout << "corrEtaGrandDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<corrEtaGrandDaughterLLP.size();a++) std::cout << corrEtaGrandDaughterLLP.at(a) << std::endl;   
    std::cout << "check phi higgs: " << std::endl;
    for(unsigned int a=0;a<GenHiggsVect.size();a++) std::cout << GenHiggsVect.at(a).phi() << std::endl;
    std::cout << "check phi bquarks: " << std::endl;
    for(unsigned int a=0;a<GenBquarksVect.size();a++) std::cout << GenBquarksVect.at(a).phi() << std::endl;
    std::cout << "checkPhiDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<checkPhiDaughterLLP.size();a++) std::cout << checkPhiDaughterLLP.at(a) << std::endl;
    std::cout << "corrPhiDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<corrPhiDaughterLLP.size();a++) std::cout << corrPhiDaughterLLP.at(a) << std::endl;
    std::cout << "checkPhiGrandDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<checkPhiGrandDaughterLLP.size();a++) std::cout << checkPhiGrandDaughterLLP.at(a) << std::endl; 
    std::cout << "corrPhiGrandDaughterLLP: " << std::endl;
    for(unsigned int a=0;a<corrPhiGrandDaughterLLP.size();a++) std::cout << corrPhiGrandDaughterLLP.at(a) << std::endl;
    */

    //if(nGenBinAcceptance<1) return;//!Remove!!!
    if(isVerbose) std::cout << "Gen b quarks in acceptance: " << nGenBinAcceptance << std::endl;


    //for(unsigned int i = 0; i < GenVBFVect.size(); i++) GenVBFquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) GenLLPs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenHiggsVect.size(); i++)     GenHiggs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenBquarksVect.size(); i++)   GenBquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenGravitinosVect.size(); i++) GenGravitinos.push_back( GenPType() );
    
    if (WriteGenLLPs)  
      {
	//Old implementation
	//for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenLLPs[i], &GenLongLivedVect[i], LLPInCalo[i], -9., -9., -1., -1., -1., -1.);

	//From AODNtuplizer 08.12.2021
	for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenLLPs[i], &GenLongLivedVect[i], LLPInCalo[i], -9., -9., -1000.,-10000.,-10000.,-10000.);

      }
    if (WriteGenHiggs) 
      {
	//Old implementation:
	//for(unsigned int i = 0; i < GenHiggsVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenHiggs[i], &GenHiggsVect[i], idMotherB==25 ? DaughterOfLLPInCalo[i] : false, idMotherB==25 ? corrEtaDaughterLLP[i] : -9., idMotherB==25 ? corrPhiDaughterLLP[i] : -9., -1., -1., -1., -1.);

	//From AODNtuplizer 08.12.2021
	for(unsigned int i = 0; i < GenHiggsVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenHiggs[i], &GenHiggsVect[i], (idMotherB1==25 || idMotherB1==23) ? DaughterOfLLPInCalo[i] : false, (idMotherB1==25 || idMotherB1==23) ? corrEtaDaughterLLP[i] : -9., (idMotherB1==25 || idMotherB1==23) ? corrPhiDaughterLLP[i] : -9., (idMotherB1==25 || idMotherB1==23) ? LLPRadius_Dau[i] : -1000., (idMotherB1==25 || idMotherB1==23) ? LLPX_Dau[i] : -10000., (idMotherB1==25 || idMotherB1==23) ? LLPY_Dau[i] : -10000., (idMotherB1==25 || idMotherB1==23) ? LLPZ_Dau[i] : -10000.);

	//Write also gravitinos
        //check if it segfaults!
	for(unsigned int i = 0; i < GenGravitinosVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenGravitinos[i], &GenGravitinosVect[i], (idMotherB1==25 || idMotherB1==23) ? DaughterOfLLPInCalo[i]: false, (idMotherB1==25 || idMotherB1==23) ? corrEtaDaughterLLP[i] : -9., (idMotherB1==25 || idMotherB1==23) ? corrPhiDaughterLLP[i] : -9., (idMotherB1==25 || idMotherB1==23) ? LLPRadius_Dau[i] : -1000., (idMotherB1==25 || idMotherB1==23) ? LLPX_Dau[i] : -10000., (idMotherB1==25 || idMotherB1==23) ? LLPY_Dau[i] : -10000., (idMotherB1==25 || idMotherB1==23) ? LLPZ_Dau[i] : -10000.);
      }

    //Old implementation
    //if (WriteGenBquarks) for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenBquarks[i], &GenBquarksVect[i], (idMotherB1==25 || idMotherB1==23) ? GrandDaughterOfLLPInCalo[i] : DaughterOfLLPInCalo[i], (idMotherB1==25 || idMotherB1==23) ? corrEtaGrandDaughterLLP[i] : corrEtaDaughterLLP[i], (idMotherB1==25 || idMotherB1==23) ? corrPhiGrandDaughterLLP[i] : corrPhiDaughterLLP[i], -1., -1., -1., -1.);

    if(WriteGenBquarks && (LLPZ_GrandDau.size()==GenBquarksVect.size() || LLPZ_Dau.size()==GenBquarksVect.size()) ) for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenBquarks[i], &GenBquarksVect[i], (idMotherB1==25 || idMotherB1==23) && GrandDaughterOfLLPInCalo.size()==GenBquarksVect.size() ? GrandDaughterOfLLPInCalo[i] : DaughterOfLLPInCalo[i], (idMotherB1==25 || idMotherB1==23) && corrEtaGrandDaughterLLP.size()==GenBquarksVect.size() ? corrEtaGrandDaughterLLP[i] : corrEtaDaughterLLP[i], (idMotherB1==25 || idMotherB1==23) && corrPhiGrandDaughterLLP.size()==GenBquarksVect.size()? corrPhiGrandDaughterLLP[i] : corrPhiDaughterLLP[i], (idMotherB1==25 || idMotherB1==23) && LLPRadius_GrandDau.size()==GenBquarksVect.size() ? LLPRadius_GrandDau[i] : LLPRadius_Dau[i], (idMotherB1==25 || idMotherB1==23) && LLPX_GrandDau.size()==GenBquarksVect.size() ? LLPX_GrandDau[i] : LLPX_Dau[i], (idMotherB1==25 || idMotherB1==23) && LLPY_GrandDau.size()==GenBquarksVect.size() ? LLPY_GrandDau[i] : LLPY_Dau[i], (idMotherB1==25 || idMotherB1==23) && LLPZ_GrandDau.size()==GenBquarksVect.size() ? LLPZ_GrandDau[i] : LLPZ_Dau[i]);

    
    //for(unsigned int i = 0; i < GenLLPs.size(); i++)
    //{
    //std::cout << "LLP n. " << i << " from struct" << std::endl;
    //std::cout << "travelRadius " << GenLLPs[i].travelRadius << std::endl;
    // GenLLPs[i].travelRadius = -1.;
    //std::cout << " force it to change " << GenLLPs[i].travelRadius << std::endl;
    //}
    
    
    //if(nGenBquarks>0) gen_b_radius = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2) + pow(GenBquarksVect.at(0).vz() - GenBquarksVect.at(0).mother()->vz(),2)) : -1.;
    //if(nGenBquarks>0) gen_b_radius_2D = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2)) : -1.;
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
    //theTriggerAnalyzer->FillTriggerMap(iEvent, TriggerMap, PrescalesTriggerMap, isVerboseTrigger);
    //theTriggerAnalyzer->FillMetFiltersMap(iEvent, MetFiltersMap);
    //BadPFMuonFlag = theTriggerAnalyzer->GetBadPFMuonFlag(iEvent);
    //BadChCandFlag = theTriggerAnalyzer->GetBadChCandFlag(iEvent);
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
GenNtuplizerCalo::beginJob()
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
   tree -> Branch("nLLPInCalo" , &nLLPInCalo , "nLLPInCalo/I");
   //tree -> Branch("gen_b_radius" , &gen_b_radius , "gen_b_radius/F");
   //tree -> Branch("gen_b_radius_2D" , &gen_b_radius_2D , "gen_b_radius_2D/F");
   tree -> Branch("m_pi" , &m_pi , "m_pi/F");
   tree -> Branch("is_central" , &is_central , "is_central/O");
   tree -> Branch("m_chi" , &m_chi , "m_chi/I");
   tree -> Branch("ctau" , &ctau , "ctau/I");
   //tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
   //tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
   // Set trigger branches
   //for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   //for(auto it = MetFiltersMap.begin(); it != MetFiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   //for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());

   tree -> Branch("GenHiggs", &GenHiggs);//, ObjectsFormat::ListGenPType().c_str());
   tree -> Branch("GenLLPs", &GenLLPs);
   tree -> Branch("GenBquarks", &GenBquarks);
   tree -> Branch("GenGravitinos", &GenGravitinos);
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenNtuplizerCalo::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenNtuplizerCalo::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenNtuplizerCalo);
