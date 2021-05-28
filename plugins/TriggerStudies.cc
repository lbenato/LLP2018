// -*- C++ -*-
//
// Package:    Analyzer/LLP
// Class:      TriggerStudies
// 
/**\class TriggerStudies TriggerStudies.cc Analyzer/LLP/plugins/TriggerStudies.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Lisa Benato
//         Created:  Tue, 24 Jul 2018 11:12:19 GMT
//
//


#include "TriggerStudies.h"

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
//TriggerStudies::TriggerStudies(const edm::ParameterSet& iConfig, edm::ConsumesCollector&& CColl):
TriggerStudies::TriggerStudies(const edm::ParameterSet& iConfig):
    GenPSet(iConfig.getParameter<edm::ParameterSet>("genSet")),
    PileupPSet(iConfig.getParameter<edm::ParameterSet>("pileupSet")),
    TriggerPSet(iConfig.getParameter<edm::ParameterSet>("triggerSet")),
    JetPSet(iConfig.getParameter<edm::ParameterSet>("jetSet")),
    //VBFJetPSet(iConfig.getParameter<edm::ParameterSet>("vbfJetSet")),
    CHSFatJetPSet(iConfig.getParameter<edm::ParameterSet>("chsFatJetSet")),
    ElectronPSet(iConfig.getParameter<edm::ParameterSet>("electronSet")),
    MuonPSet(iConfig.getParameter<edm::ParameterSet>("muonSet")),
    TauPSet(iConfig.getParameter<edm::ParameterSet>("tauSet")),
    PhotonPSet(iConfig.getParameter<edm::ParameterSet>("photonSet")),
    VertexPSet(iConfig.getParameter<edm::ParameterSet>("vertexSet")),
    PFCandidatePSet(iConfig.getParameter<edm::ParameterSet>("pfCandidateSet")),
    MinGenBpt(iConfig.getParameter<double>("minGenBpt")),
    MaxGenBeta(iConfig.getParameter<double>("maxGenBeta")),
    InvmassVBF(iConfig.getParameter<double>("invmassVBF")),
    DetaVBF(iConfig.getParameter<double>("detaVBF")),
    WriteNGenBquarks(iConfig.getParameter<int>("writeNGenBquarks")),
    WriteNGenLongLiveds(iConfig.getParameter<int>("writeNGenLongLiveds")),
    WriteNMatchedJets(iConfig.getParameter<int>("writeNMatchedJets")),
    WriteNLeptons(iConfig.getParameter<int>("writeNLeptons")),
    WriteOnlyTriggerEvents(iConfig.getParameter<bool>("writeOnlyTriggerEvents")),
    WriteOnlyL1FilterEvents(iConfig.getParameter<bool>("writeOnlyL1FilterEvents")),
    WriteOnlyisVBFEvents(iConfig.getParameter<bool>("writeOnlyisVBFEvents")),
    WriteFatJets(iConfig.getParameter<bool>("writeFatJets")),
    WriteJetPFCandidates(iConfig.getParameter<bool>("writeJetPFCandidates")),
    WriteAllPFCandidates(iConfig.getParameter<bool>("writeAllPFCandidates")),
    WriteLostTracks(iConfig.getParameter<bool>("writeLostTracks")),
    WriteVertices(iConfig.getParameter<bool>("writeVertices")),
    PerformPreFiringStudies(iConfig.getParameter<bool>("performPreFiringStudies")),
    isVerbose(iConfig.getParameter<bool> ("verbose")),
    isVerboseTrigger(iConfig.getParameter<bool> ("verboseTrigger")),
    isSignal(iConfig.getParameter<bool> ("signal"))
    
{
    //Initalize objects
    theJetAnalyzer      = new JetAnalyzer(JetPSet, consumesCollector());
    //theVBFJetAnalyzer      = new JetAnalyzer(VBFJetPSet, consumesCollector());
    if (WriteFatJets) theCHSFatJetAnalyzer   = new JetAnalyzer(CHSFatJetPSet, consumesCollector());
    theGenAnalyzer         = new GenAnalyzer(GenPSet, consumesCollector());
    thePileupAnalyzer      = new PileupAnalyzer(PileupPSet, consumesCollector());
    theTriggerAnalyzer     = new TriggerAnalyzer(TriggerPSet, consumesCollector());
    theElectronAnalyzer    = new ElectronAnalyzer(ElectronPSet, consumesCollector());
    theMuonAnalyzer        = new MuonAnalyzer(MuonPSet, consumesCollector());
    theTauAnalyzer         = new TauAnalyzer(TauPSet, consumesCollector());
    thePhotonAnalyzer      = new PhotonAnalyzer(PhotonPSet, consumesCollector());
    theVertexAnalyzer      = new VertexAnalyzer(VertexPSet, consumesCollector());
    thePFCandidateAnalyzer = new PFCandidateAnalyzer(PFCandidatePSet, consumesCollector());

    std::vector<std::string> TriggerList(TriggerPSet.getParameter<std::vector<std::string> >("paths"));
    for(unsigned int i = 0; i < TriggerList.size(); i++) TriggerMap[ TriggerList[i] ] = false;
    for(unsigned int i = 0; i < TriggerList.size(); i++) PrescalesTriggerMap[ TriggerList[i] ] = -1;
    std::vector<std::string> MetFiltersList(TriggerPSet.getParameter<std::vector<std::string> >("metpaths"));
    for(unsigned int i = 0; i < MetFiltersList.size(); i++) MetFiltersMap[ MetFiltersList[i] ] = false;
    std::vector<std::string> L1FiltersList(TriggerPSet.getParameter<std::vector<std::string> >("l1filters"));
    for(unsigned int i = 0; i < L1FiltersList.size(); i++) L1FiltersMap[ L1FiltersList[i] ] = false;

    //L1 bits information, thanks to scouting dijet team
    //https://github.com/CMSDIJET/DijetScoutingRootTreeMaker/blob/master/plugins/DijetScoutingTreeProducer.cc
    l1GtUtils_ = new l1t::L1TGlobalUtil(iConfig,consumesCollector());
    algToken_ = consumes<BXVector<GlobalAlgBlk>>(iConfig.getParameter<edm::InputTag>("AlgInputTag"));
    l1Seeds_ = iConfig.getParameter<std::vector<std::string> >("l1Seeds");
    //fill a map of l1 seeds
    for(unsigned int i = 0; i < l1Seeds_.size(); i++) L1BitsMap[ l1Seeds_[i] ] = false;


    if(isVerbose) std::cout << "CONSTRUCTOR" << std::endl;
    //if(isVerbose) std::cout << "ONLY EVENTS WITH 4 GEN B QUARKS IN ACCEPTANCE" << std::endl;

    //now do what ever initialization is needed
    usesResource("TFileService");

    if(isVerbose) std::cout << "---------- STARTING ----------" << std::endl;

}


TriggerStudies::~TriggerStudies()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
    if(isVerbose) std::cout << "---------- ENDING  ----------" << std::endl;

    delete theJetAnalyzer;
    //delete theVBFJetAnalyzer;
    if (WriteFatJets)    delete theCHSFatJetAnalyzer;
    delete theGenAnalyzer;
    delete thePileupAnalyzer;
    delete theTriggerAnalyzer;
    delete theElectronAnalyzer;
    delete theMuonAnalyzer;
    delete theTauAnalyzer;
    delete thePhotonAnalyzer;
    delete theVertexAnalyzer;
    delete thePFCandidateAnalyzer;
}


//
// member functions
//

// ------------ method called for each event  ------------
void
TriggerStudies::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  //if(isVerbose) std::cout << "STARTING ANALYZE METHOD!" << std::endl;

    using namespace edm;
    using namespace reco;
    using namespace std;

    // Initialize types
    ObjectsFormat::ResetMEtType(MEt);
    ObjectsFormat::ResetCandidateType(VBF);
    ObjectsFormat::ResetCandidateType(TriggerVBF);
    //ObjectsFormat::ResetCandidateType(Z);
    //ObjectsFormat::ResetCandidateType(W);

    isMC = false;
    isVBF = isTriggerVBF = false;
    isZtoMM = isZtoEE = isWtoMN = isWtoEN = isTtoEM = false;
    EventNumber = LumiNumber = RunNumber = nPV = 0;
    AtLeastOneTrigger = AtLeastOneL1Filter = false;
    number_of_PV = number_of_SV = 0;//27 Sep: remember to properly initialize everything
    nJets = nLooseJets = nTightJets = nVBFPairJets = nTriggerObjectsTripleJet50 = nTriggerObjectsTripleJet50WithDuplicates = 0;
    nTriggerObjects = nTriggerVBFPairJets = 0;
    nTriggerObjectsDoubleJet90 = nTriggerObjectsQuadJet45 = nTriggerObjectsDoubleJetC112MaxDeta1p6 = nTriggerObjectsDoubleJetC112 = nTriggerObjectsSixJet30 = nTriggerObjectsQuadPFJetMqq240 = nTriggerObjectsQuadPFJetMqq500 = 0;
    //    nSelectedDisplacedJet = nSelectedVBFJets = 0;
    nCHSFatJets = nLooseCHSFatJets = nTightCHSFatJets = nGenBquarks = nGenLL = nPV = nSV = 0;
    nMatchedJets = 0;
    nDisplaced = 0;
    nCaloTagJets = nLooseCaloTagJets = 0;
    nElectrons = nMuons = nTaus = nPhotons = 999;//We want to veto them for QCD control regions! Best offset is a large number!
    nTightElectrons = nTightMuons = 0;//This time we want a W, Z control region. Let's count them from zero
    number_of_b_matched_to_Jets = 0;
    EventWeight = PUWeight = PUWeightDown = PUWeightUp = LeptonWeight = ZewkWeight = WewkWeight = 1.;
    HT = 0.;
    MinJetMetDPhi = 10.;
    Prefired = false;
    //bit_L1_TripleJet_84_68_48_VBF = bit_L1_TripleJet_88_72_56_VBF = bit_L1_TripleJet_92_76_64_VBF = bit_L1_HTT300 = false;


    muon1_pt = -1.;
    muon1_eta = -9.;
    muon1_phi = -9.;
    met_pt_nomu = -1.;

    //Event info
    isMC = !iEvent.isRealData();
    EventNumber = iEvent.id().event();
    LumiNumber = iEvent.luminosityBlock();
    RunNumber = iEvent.id().run();


    //theTriggerAnalyzer->Debug(iEvent);

    // Trigger and MET filters
    //if(isVerbose) std::cout << "Trigger and met filters" << std::endl;
    theTriggerAnalyzer->FillTriggerMap(iEvent, TriggerMap, PrescalesTriggerMap, isVerboseTrigger);

    // 2020_12_18 comment, because this trigger isn't studied!
    // std::string VBF_DisplacedJet40_VTightID_Hadronic_string;
    // VBF_DisplacedJet40_VTightID_Hadronic_string = "VBF_DisplacedJet40_VTightID_Hadronic_v";
    // std::vector<pat::TriggerObjectStandAlone> VBF_DisplacedJet40_VTightID_Hadronic_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,VBF_DisplacedJet40_VTightID_Hadronic_string);

    // nTriggerObjects = VBF_DisplacedJet40_VTightID_Hadronic_Vec.size();

    // std::vector<pat::TriggerObjectStandAlone> PotentialTriggerVBFPairJets;
    // std::vector<pat::TriggerObjectStandAlone> PotentialTriggerDisplacedJets;


    //Do it for IsoMu24
    std::string IsoMu24_string;
    IsoMu24_string = "HLT_IsoMu24_v";
    std::vector<pat::TriggerObjectStandAlone> IsoMu24_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,IsoMu24_string);

    std::string DoubleJet90_string = "HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v";
    std::vector<pat::TriggerObjectStandAlone> DoubleJet90_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,DoubleJet90_string);
    nTriggerObjectsDoubleJet90 = DoubleJet90_Vec.size();

    std::string QuadJet45_string = "HLT_QuadJet45_TripleBTagCSV_p087_v";
    std::vector<pat::TriggerObjectStandAlone> QuadJet45_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,QuadJet45_string);
    nTriggerObjectsQuadJet45 = QuadJet45_Vec.size();

    std::string DoubleJetC112MaxDeta1p6_string = "HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v";
    std::vector<pat::TriggerObjectStandAlone> DoubleJetC112MaxDeta1p6_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,DoubleJetC112MaxDeta1p6_string);
    nTriggerObjectsDoubleJetC112MaxDeta1p6 = DoubleJetC112MaxDeta1p6_Vec.size();

    std::string DoubleJetC112_string = "HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v";
    std::vector<pat::TriggerObjectStandAlone> DoubleJetC112_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,DoubleJetC112_string);
    nTriggerObjectsDoubleJetC112 = DoubleJetC112_Vec.size();
    
    std::string SixJet30_string = "HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v";
    std::vector<pat::TriggerObjectStandAlone> SixJet30_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,SixJet30_string);
    nTriggerObjectsSixJet30 = SixJet30_Vec.size();

    std::string QuadPFJetMqq240_string = "HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v";
    std::vector<pat::TriggerObjectStandAlone> QuadPFJetMqq240_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,QuadPFJetMqq240_string);
    nTriggerObjectsQuadPFJetMqq240 = QuadPFJetMqq240_Vec.size();

    std::string QuadPFJetMqq500_string = "HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v";
    std::vector<pat::TriggerObjectStandAlone> QuadPFJetMqq500_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,QuadPFJetMqq500_string);
    nTriggerObjectsQuadPFJetMqq500 = QuadPFJetMqq500_Vec.size();

    //Remove duplicates from VBF_DisplacedJet40_VTightID_Hadronic_Vec

    //31 Jan: THIS MUST NOT BE DONE, OTHERWISE WE REMOVE THINGS FIRING THE NEEDED FILTERS!

    /*
    for(unsigned int r = 0; r<VBF_DisplacedJet40_VTightID_Hadronic_Vec.size(); r++)
      {
        for(unsigned int s = 0; s<VBF_DisplacedJet40_VTightID_Hadronic_Vec.size(); s++)
          {
            if(r!=s && VBF_DisplacedJet40_VTightID_Hadronic_Vec[s].pt()==VBF_DisplacedJet40_VTightID_Hadronic_Vec[r].pt()) VBF_DisplacedJet40_VTightID_Hadronic_Vec.erase(VBF_DisplacedJet40_VTightID_Hadronic_Vec.begin()+s);
          }//duplicates removed
      }
    */



    // 2020_12_18 comment, because this trigger isn't studied!
    // std::string VBF_DisplacedJet40_VVTightID_Hadronic_string;
    // VBF_DisplacedJet40_VVTightID_Hadronic_string = "VBF_DisplacedJet40_VVTightID_Hadronic_v";
    // std::vector<pat::TriggerObjectStandAlone> VBF_DisplacedJet40_VVTightID_Hadronic_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,VBF_DisplacedJet40_VVTightID_Hadronic_string);
    theTriggerAnalyzer->FillMetFiltersMap(iEvent, MetFiltersMap);
    BadPFMuonFlag = theTriggerAnalyzer->GetBadPFMuonFlag(iEvent);
    BadChCandFlag = theTriggerAnalyzer->GetBadChCandFlag(iEvent);
    //    theTriggerAnalyzer->FillL1FiltersMap(iEvent, L1FiltersMap, TriggerObjectsVector);
    theTriggerAnalyzer->FillL1FiltersMap(iEvent, L1FiltersMap);

    // 27 Sep 2018: saving only events that fired at least one trigger, to reduce output size
    for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++)
      {
	if(it->second)
	  {
	    ////std::cout << "Trigger fired!!! " << it->first << std::endl;
	    AtLeastOneTrigger = true;
	  }
	//if(AtLeastOneTrigger) break;// no need to go through everything; once one trigger is fired, event can be saved
      }

    ////if(!AtLeastOneTrigger && WriteOnlyTriggerEvents) std::cout << "This event can be rejected" << std::endl;
    if(!AtLeastOneTrigger && WriteOnlyTriggerEvents) return;




    // 10 Dec 2018: saving only events that fired at least one L1 seed
    for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++)
      {
	//	std::cout << "filter " << it->first << " is " << it->second << std::endl;
    	if(it->second)
    	  {
    	    AtLeastOneL1Filter = true;
    	  }
      }

    if(!AtLeastOneL1Filter && WriteOnlyL1FilterEvents) return;

    //Pre-firing
    if(PerformPreFiringStudies)
      {
	Prefired = theTriggerAnalyzer->EvaluatePrefiring(iEvent);
      }


    //L1 bits information, thanks to scouting dijet team
    //https://github.com/CMSDIJET/DijetScoutingRootTreeMaker/blob/master/plugins/DijetScoutingTreeProducer.cc

    l1GtUtils_->retrieveL1(iEvent,iSetup,algToken_);

    for( unsigned int iseed = 0; iseed < l1Seeds_.size(); iseed++ ) {
      L1BitsMap[l1Seeds_[iseed]] = false;
      bool l1htbit = 0;
      l1GtUtils_->getFinalDecisionByName(l1Seeds_[iseed], l1htbit);
      //if(isVerbose) std::cout<<l1Seeds_[iseed]<< " " << l1htbit << std::endl;
      if (l1htbit)
	{
	  L1BitsMap[l1Seeds_[iseed]] = true;
	}
     

    }





    //theTriggerAnalyzer->Debug(iEvent);

    //std::cout << std::endl;
    //std::cout << std::endl;
    //std::cout << std::endl;




    //if(EventNumber==40628 or EventNumber==8841 or EventNumber==9952 or EventNumber==12405) std::cout << " WARNINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG " << std::endl;


    //if(isVerbose) std::cout << " ------------------------------- " << std::endl;
    //if(isVerbose) std::cout << " ---trigger objects ---" << std::endl;



    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int r = 0; r<VBF_DisplacedJet40_VTightID_Hadronic_Vec.size(); r++)
    //   {

    // 	//std::cout << std::endl;
    // 	//std::cout << "Object n. " << r << std::endl;
    // 	//std::cout << "pt, eta, phi " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).pt() << " " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).eta() << " " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).phi() << std::endl;
    // 	//std::cout << "Collection: " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).collection() << std::endl;
    // 	//std::cout << "TypeID: ";
    // 	//for (unsigned h = 0; h < VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds().size(); ++h) std::cout << "; " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds()[h] ;
    // 	//std::cout << std::endl;
    // 	//std::cout << "Filters: ";
    // 	//for (unsigned h = 0; h < VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels().size(); ++h) std::cout << "; " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[h];
    // 	//std::cout << std::endl;

    // 	//std::cout << " ++++++ GUESS ++++++ " << std::endl;
    // 	for (unsigned h = 0; h < VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds().size(); ++h)
    // 	  {
    // 	    if( (VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds()[h])==85 or (VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds()[h])==86)
    // 	      {
    // 		for (unsigned l = 0; l < VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels().size(); ++l)
    // 		  {
    // 		    if(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltVBFFilterDisplacedJets" or VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltVBFFilterDisplacedJetsTight" ) 
    // 		      {
    // 			PotentialTriggerVBFPairJets.push_back(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r));
    // 			//std::cout<< "VBF!!!!!!!!! jet n. " << r << std::endl;
    // 			//std::cout << "pT: " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).pt() << std::endl;
    // 		      }
    // 		    // //else if(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltCentralHadronCaloJetpt40VTightID" or VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltL4PromptHadronJetsFullTracksHLTCaloJetTagFilterVTightID")
    // 		    else if(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltCentralHadronCaloJetpt40VTightID")
    // 		      {
    // 			PotentialTriggerDisplacedJets.push_back(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r));
    // 			//std::cout<< "DISPLACED!!!!!!!!! jet n. " << r << std::endl;
    // 			//std::cout << "pT: " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).pt() << std::endl;
    // 		      }

    // 		    else if(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltTripleJet50")
    // 		      {
    // 			//!!!!!!!!!!!!!!!!
    // 			//std::cout << "Object matched to hltTripleJet50 and VBF_DisplacedJet40_VTightID_Hadronic path!" << std::endl;
    // 			/////std::cout<< "DISPLACED!!!!!!!!! jet n. " << r << std::endl;
    // 			//std::cout << "pT: " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).pt() << std::endl;
    // 			//std::cout << "eta: " << VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).eta() << std::endl;
    // 		      }

    // 		  }		
    // 	      }

    // 	  }


      
    //   }

    //std::cout << " ++++++ END OF GUESS ++++++ " << std::endl;
    //if(isVerbose) std::cout << " ------------------------------- " << std::endl;







    // EWK corrections
    /*
    //std::cout << "EWK corrections" << std::endl;

    std::vector<reco::GenParticle> GenZBosons = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,23,22);
    std::vector<reco::GenParticle> GenWBosons = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,24,22);
    
    reco::Candidate* theGenZ = theGenAnalyzer->FindGenParticle(GenZBosons, 23);
    reco::Candidate* theGenW = theGenAnalyzer->FindGenParticle(GenWBosons, 24);
    
    if(theGenZ) {
      ZewkWeight = theGenAnalyzer->GetZewkWeight(theGenZ->pt());
    }
    if(theGenW) {
      WewkWeight = theGenAnalyzer->GetWewkWeight(theGenW->pt());
    }
    

    EventWeight *= ZewkWeight * WewkWeight;

    */

    // Pu weight and number of vertices
    //if(isVerbose) std::cout << "Pile-up" << std::endl;
    PUWeight     = thePileupAnalyzer->GetPUWeight(iEvent);//calculates pileup weights
    nPV = thePileupAnalyzer->GetPV(iEvent);//calculates number of vertices

    EventWeight *= PUWeight;
    // Missing Energy
    //if(isVerbose) std::cout << "MET" << std::endl;
    pat::MET MET = theJetAnalyzer->FillMetVector(iEvent);
    //pat::MET Neutrino(MET);
    // HT
    //if(isVerbose) std::cout << "HT" << std::endl;
    HT = theJetAnalyzer->CalculateHT(iEvent,iSetup,3,15,3.,true);

    // Electrons
    //if(isVerbose) std::cout << "Electrons" << std::endl;
    std::vector<pat::Electron> ElecVect = theElectronAnalyzer->FillElectronVector(iEvent);
    //std::vector<pat::Electron> TightElecVect;

    //for(unsigned int a = 0; a<ElecVect.size(); a++)
    //{
    //	if(ElecVect.at(a).hasUserInt("isTight") && ElecVect.at(a).userInt("isTight")>0)
    //	  {
    //	    TightElecVect.push_back(ElecVect.at(a));
    //	    nTightElectrons++;
    //	  }
    //}
    nElectrons = ElecVect.size();

    // Muons
    //if(isVerbose) std::cout << "Muons" << std::endl;
    std::vector<pat::Muon> MuonVect = theMuonAnalyzer->FillMuonVector(iEvent);
    Muons.clear();
    std::vector<pat::Muon> TightMuonVect;
    for(unsigned int a = 0; a<MuonVect.size(); a++)
      {
    	if(MuonVect.at(a).hasUserInt("isTight") && MuonVect.at(a).userInt("isTight")>0 && MuonVect.at(a).hasUserFloat("pfIso04") && MuonVect.at(a).userFloat("pfIso04")<0.15)//tight iso for muons
    	  {
    	    TightMuonVect.push_back(MuonVect.at(a));
    	    nTightMuons++;
    	  }
      }

    nMuons = MuonVect.size();

    //std::cout << "number of tight muons: " << nTightMuons << std::endl;

    //1 muon requirement; input muons already matched with IsoMu24 trigger
    //skip events with not exactly 1 muon matched to trigger!
    //    if(nTightMuons!=1 && !isSignal) return;
    if (nMuons==0 && !isSignal) return;

    if(nTightMuons==1)
      {
	muon1_pt = TightMuonVect.at(0).pt();
	muon1_eta = TightMuonVect.at(0).eta();
	muon1_phi = TightMuonVect.at(0).phi();
      }

    //Initialize met no mu
    float met_pt_nomu_x(0.), met_pt_nomu_y(0.);
    
    met_pt_nomu_x = MET.px();//before summing up muons
    met_pt_nomu_y = MET.py();//before summing up muons

    //Add up muon px,py
    if(nTightMuons==1)
      {
	met_pt_nomu_x += TightMuonVect.at(0).px();
	met_pt_nomu_y += TightMuonVect.at(0).py();
      }
    //Calculate met pt no mu
    met_pt_nomu = sqrt( pow(met_pt_nomu_x,2) + pow(met_pt_nomu_y,2) );


    //if(isVerbose) if(TriggerMap.find("HLT_IsoMu24_v") != TriggerMap.end() && TriggerMap["HLT_IsoMu24_v"]) std::cout << "IsoMu24 fired! " << std::endl; 
    //if(isVerbose) std::cout << "Size of IsoMu24_Vec: " << IsoMu24_Vec.size() << std::endl;
    float deltaR_muon(1000.), curr_deltaR_muon(1000.);
    for(unsigned int a = 0; a<IsoMu24_Vec.size(); a++)
      {
    	//if(isVerbose) std::cout << " object n. " << a << std::endl;
    	//if(isVerbose) std::cout << " filter Ids: " << std::endl;
    	//if(isVerbose) std::cout << " pt: " << IsoMu24_Vec.at(a).pt() << std::endl;
    	//if(isVerbose) std::cout << " eta: " << IsoMu24_Vec.at(a).eta() << std::endl;
    	//if(isVerbose) std::cout << "dR with tight muon: " << fabs(reco::deltaR(IsoMu24_Vec.at(a).eta(),IsoMu24_Vec.at(a).phi(),muon1_eta,muon1_phi)) << std::endl;
    	curr_deltaR_muon = fabs(reco::deltaR(IsoMu24_Vec.at(a).eta(),IsoMu24_Vec.at(a).phi(),muon1_eta,muon1_phi));
    	if(curr_deltaR_muon<0.5 and curr_deltaR_muon<deltaR_muon) deltaR_muon=curr_deltaR_muon;
      }
    //if(isVerbose) std::cout << "Size of tight muon vec: " << TightMuonVect.size() << std::endl;
    //if(isVerbose) std::cout << " pt: " << muon1_pt << std::endl;
    //if(isVerbose) std::cout << " eta: " << muon1_eta << std::endl;
    // if(deltaR_muon==1000. && !isSignal)
    //   {
    // 	//if(isVerbose) std::cout << " REJECTED!!! " << std::endl;
    // 	return;
    //   }
    //Reject events where tight muon and isomu24 trigger objects are not matched
    //std::cout << "NOW I should have passed AAAALLL the selections! " << std::endl;

    
    // Taus
    // if(isVerbose) std::cout << "Taus" << std::endl;
    std::vector<pat::Tau> TauVect = theTauAnalyzer->FillTauVector(iEvent);
    theTauAnalyzer->CleanTausFromMuons(TauVect, MuonVect, 0.4);
    theTauAnalyzer->CleanTausFromElectrons(TauVect, ElecVect, 0.4);
    nTaus = TauVect.size();

    // Photons
    // if(isVerbose) std::cout << "Photons" << std::endl;
    std::vector<pat::Photon> PhotonVect = thePhotonAnalyzer->FillPhotonVector(iEvent);
    nPhotons = PhotonVect.size();


    // Jets
    std::vector<pat::Jet> JetsVect = theJetAnalyzer->FillJetVector(iEvent,iSetup);//theVBFJetAnalyzer->FillJetVector(iEvent);
    theJetAnalyzer->CleanJetsFromMuons(JetsVect, MuonVect, 0.4);
    nJets = JetsVect.size();


    // Debug hltTripleJet50
    // std::string all_trigger_string;
    // all_trigger_string = "HLT";
    // std::vector<pat::TriggerObjectStandAlone> AllTriggerVec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,all_trigger_string);
    // std::vector<pat::TriggerObjectStandAlone> TripleJet50TriggerVec;
    // std::vector<pat::TriggerObjectStandAlone> TripleJet50TriggerWithDuplicatesVec;

    // for(unsigned int r = 0; r<AllTriggerVec.size(); r++)
    //   {

    // 	for (unsigned h = 0; h < AllTriggerVec.at(r).filterIds().size(); ++h)
    // 	  {
    // 	    //if( (AllTriggerVec.at(r).filterIds()[h])==85 or (AllTriggerVec.at(r).filterIds()[h])==86)
    // 	      //remove condition of being jets?
    // 	      //{
    // 		for (unsigned l = 0; l < AllTriggerVec.at(r).filterLabels().size(); ++l)
    // 		  {
    // 		    if(AllTriggerVec.at(r).filterLabels()[l]=="hltTripleJet50")
    // 		      {
    // 			//std::cout << "Object matched to hltTripleJet50!" << std::endl;
    // 			//std::cout << "pT: " << AllTriggerVec.at(r).pt() << std::endl;
    // 			//std::cout << "eta: " << AllTriggerVec.at(r).eta() << std::endl;
    // 			TripleJet50TriggerWithDuplicatesVec.push_back(AllTriggerVec.at(r));
    // 			TripleJet50TriggerVec.push_back(AllTriggerVec.at(r));
    // 		      }

    // 		  }		
    // 	      //}

    // 	  }

    //   }


    /*
    //Remove duplicates from TripleJet50TriggerVec
    //std::cout << "TripleJet50TriggerVec size before removal: " << TripleJet50TriggerVec.size() << std::endl;
    for(unsigned int r = 0; r<TripleJet50TriggerVec.size(); r++)
      {
	//std::cout << "TripleJet50TriggerVec[r=" << r << "].pt = " << TripleJet50TriggerVec.at(r).pt() << std::endl;
        for(unsigned int s = 0; s<TripleJet50TriggerVec.size(); s++)
          {
	    //std::cout << "TripleJet50TriggerVec[s=" << s << "].pt = " << TripleJet50TriggerVec.at(s).pt() << std::endl;
            if(r!=s && TripleJet50TriggerVec.at(s).pt()==TripleJet50TriggerVec.at(r).pt()) 
	      {
		//std::cout << "duplicate!" << std::endl;
		TripleJet50TriggerVec.erase(TripleJet50TriggerVec.begin()+s);
	      }
          }//duplicates removed
      }



    //Remove duplicates from TripleJet50TriggerVec, secon time
    //std::cout << "TripleJet50TriggerVec size before removal, 2nd time: " << TripleJet50TriggerVec.size() << std::endl;
    for(unsigned int r = 0; r<TripleJet50TriggerVec.size(); r++)
      {
	//std::cout << "TripleJet50TriggerVec[r=" << r << "].pt = " << TripleJet50TriggerVec.at(r).pt() << std::endl;
        for(unsigned int s = 0; s<TripleJet50TriggerVec.size(); s++)
          {
	    //std::cout << "TripleJet50TriggerVec[s=" << s << "].pt = " << TripleJet50TriggerVec.at(s).pt() << std::endl;
            if(r!=s && TripleJet50TriggerVec.at(s).pt()==TripleJet50TriggerVec.at(r).pt()) 
	      {
		//std::cout << "duplicate!" << std::endl;
		TripleJet50TriggerVec.erase(TripleJet50TriggerVec.begin()+s);
	      }
          }//duplicates removed
      }

    //std::cout << "TripleJet50TriggerVec size after removal, 2nd time: " << TripleJet50TriggerVec.size() << std::endl;
    */


    // 2020_12_18 comment, because this trigger isn't studied!
    // nTriggerObjectsTripleJet50WithDuplicates = TripleJet50TriggerVec.size();

    // auto comp = [] ( const pat::TriggerObjectStandAlone& lhs, const pat::TriggerObjectStandAlone& rhs ) {return lhs.pt() ==rhs.pt();};
    // auto last = std::unique(TripleJet50TriggerVec.begin(), TripleJet50TriggerVec.end(),comp);
    // TripleJet50TriggerVec.erase(last, TripleJet50TriggerVec.end());

    // nTriggerObjectsTripleJet50 = TripleJet50TriggerVec.size();


    // float delta_R_TripleJet50 = 1000.;
    // float current_delta_R_TripleJet50 = 1000.;
    // int ch_TripleJet50 = -1;

    // for(unsigned int t1 = 0; t1<TripleJet50TriggerVec.size(); t1++)
    //   {

    // 	for(unsigned int s = 0; s<JetsVect.size(); s++)
    // 	  {
    // 	    current_delta_R_TripleJet50 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),TripleJet50TriggerVec.at(t1).eta(),TripleJet50TriggerVec.at(t1).phi()));
    // 	    if(current_delta_R_TripleJet50<0.6 and current_delta_R_TripleJet50<delta_R_TripleJet50) 
    // 	      {
    // 		delta_R_TripleJet50=current_delta_R_TripleJet50;
    // 		ch_TripleJet50 = s;
    // 	      }
    // 	  }


    // 	if(ch_TripleJet50>=0) JetsVect.at(ch_TripleJet50).addUserInt("TriggerMatched_TripleJet50",1);

    //   }


    for(unsigned int s = 0; s<JetsVect.size(); s++){
      float current_delta_R_DoubleJet90 = 1000.;
      for(unsigned int t1 = 0; t1 < DoubleJet90_Vec.size(); t1++){
	current_delta_R_DoubleJet90 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),DoubleJet90_Vec.at(t1).eta(),DoubleJet90_Vec.at(t1).phi()));
	if (current_delta_R_DoubleJet90<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_DoubleJet90",1);
	  break;
	}
      }
      float current_delta_R_QuadJet45 = 1000.;
      for(unsigned int t1 = 0; t1 < QuadJet45_Vec.size(); t1++){
	current_delta_R_QuadJet45 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),QuadJet45_Vec.at(t1).eta(),QuadJet45_Vec.at(t1).phi()));
	if (current_delta_R_QuadJet45<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_QuadJet45",1);
	  break;
	}
      }
      float current_delta_R_DoubleJetC112MaxDeta1p6 = 1000.;
      for(unsigned int t1 = 0; t1 < DoubleJetC112MaxDeta1p6_Vec.size(); t1++){
	current_delta_R_DoubleJetC112MaxDeta1p6 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),DoubleJetC112MaxDeta1p6_Vec.at(t1).eta(),DoubleJetC112MaxDeta1p6_Vec.at(t1).phi()));
	if (current_delta_R_DoubleJetC112MaxDeta1p6<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_DoubleJetC112MaxDeta1p6",1);
	  break;
	}
      }
      float current_delta_R_DoubleJetC112 = 1000.;
      for(unsigned int t1 = 0; t1 < DoubleJetC112_Vec.size(); t1++){
	current_delta_R_DoubleJetC112 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),DoubleJetC112_Vec.at(t1).eta(),DoubleJetC112_Vec.at(t1).phi()));
	if (current_delta_R_DoubleJetC112<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_DoubleJetC112",1);
	  break;
	}
      }
      float current_delta_R_SixJet30 = 1000.;
      for(unsigned int t1 = 0; t1 < SixJet30_Vec.size(); t1++){
	current_delta_R_SixJet30 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),SixJet30_Vec.at(t1).eta(),SixJet30_Vec.at(t1).phi()));
	if (current_delta_R_SixJet30<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_SixJet30",1);
	  break;
	}
      }
      float current_delta_R_QuadPFJetMqq240 = 1000.;
      for(unsigned int t1 = 0; t1 < QuadPFJetMqq240_Vec.size(); t1++){
	current_delta_R_QuadPFJetMqq240 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),QuadPFJetMqq240_Vec.at(t1).eta(),QuadPFJetMqq240_Vec.at(t1).phi()));
	if (current_delta_R_QuadPFJetMqq240<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_QuadPFJetMqq240",1);
	  break;
	}
      }
      float current_delta_R_QuadPFJetMqq500 = 1000.;
      for(unsigned int t1 = 0; t1 < QuadPFJetMqq500_Vec.size(); t1++){
	current_delta_R_QuadPFJetMqq500 = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),QuadPFJetMqq500_Vec.at(t1).eta(),QuadPFJetMqq500_Vec.at(t1).phi()));
	if (current_delta_R_QuadPFJetMqq500<0.5){
	  JetsVect.at(s).addUserInt("TriggerMatched_QuadPFJetMqq500",1);
	  break;
	}
      }


    }//end loop over jets


    /*
    if(nTriggerObjectsTripleJet50<3)
      {
	std::cout << "Less than 2 trigger objects matched to hltTripleJet50!" << std::endl;
	for(unsigned int i=0; i<TripleJet50TriggerWithDuplicatesVec.size(); i++)
	  {
	    std::cout << "TripleJet50TriggerWithDuplicates  [" << i << "]\tpt: " << TripleJet50TriggerWithDuplicatesVec[i].pt() << "\teta: " << TripleJet50TriggerWithDuplicatesVec[i].eta() << "\tphi: " << TripleJet50TriggerWithDuplicatesVec[i].phi() << "\tmass: " << TripleJet50TriggerWithDuplicatesVec[i].mass() << std::endl; 
	  }
      }
    */

    //std::cout << "!!!!!!!!!!LLLLLL!!!" << std::endl;
    //std::cout << "number of CHS AK4 jets:  " << JetsVect.size() << std::endl;
    //for(unsigned int i = 0; i < JetsVect.size(); i++) std::cout << "  CHS AK4 jet  [" << i << "]\tpt: " << JetsVect[i].pt() << "\teta: " << JetsVect[i].eta() << "\tphi: " << JetsVect[i].phi() << "\tmass: " << JetsVect[i].mass() << std::endl;
    //std::cout << " --- Event n. " << iEvent.id().event() << ", lumi " << iEvent.luminosityBlock() << ", run " << iEvent.id().run() << std::endl;

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // VBF tagging
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------


    // Jets
    for(unsigned int j = 0; j < JetsVect.size(); j++){

      int nTrackConstituents = 0;
      //per jet tag: number of pf candidates; number of tracks
      std::vector<edm::Ptr<reco::Candidate>> JetConstituentVect = JetsVect[j].getJetConstituents();
      //std::cout << "jet " << j << " has " << JetConstituentVect.size()<< " constituents" << std::endl;
      JetsVect.at(j).addUserInt("nConstituents",JetConstituentVect.size());
      for(unsigned int k = 0; k < JetConstituentVect.size(); k++){

	if(JetConstituentVect[k]->charge()!=0) 
	  {
	    nTrackConstituents++;
	  }	
      }
      JetsVect.at(j).addUserInt("nTrackConstituents",nTrackConstituents);
    }


    //if(isVerbose) std::cout << "Filled JetsVect" << std::endl;
    



    //if(isVerbose) std::cout << "VBF tagging" << std::endl;


    pat::CompositeCandidate theVBF;
    //pat::CompositeCandidate theVBFJECUp;
    //pat::CompositeCandidate theVBFJECDown;
    //pat::CompositeCandidate theVBFJERUp;
    //pat::CompositeCandidate theVBFJERDown;
    std::vector<pat::Jet> VBFPairJetsVect;

    pat::CompositeCandidate theTriggerVBF;
    std::vector<pat::TriggerObjectStandAlone> TriggerVBFPairJetsVect;



    float delta_eta_reco (0.), curr_delta_eta_reco(0.) ;
    int j1(-1), j2(-1);
    float curr_mjj(0.);
    pat::CompositeCandidate current_VBF;

    if(JetsVect.size()>=2) {
      //if(isVerbose) std::cout << "Loop over jets to determine VBF pair" << std::endl;
      for(unsigned int a = 0; a<JetsVect.size(); a++) {
        //find the VBF pair                                                                                                                                                             
        for(unsigned int b = 1; b<JetsVect.size(); b++) {
	  if(b!=a and JetsVect.at(a).pt()>=20 and JetsVect.at(b).pt()>=20 and JetsVect.at(a).userInt("isLoose")>0 and JetsVect.at(b).userInt("isLoose")>0 and (JetsVect.at(a).eta()*JetsVect.at(b).eta())<0)//if looser thresholds applied; we will use that for JER-JEC effects

	    {

	      //calculate delta eta
	      curr_delta_eta_reco = abs(JetsVect[a].eta() - JetsVect[b].eta());
	      current_VBF.clearDaughters();
	      current_VBF.addDaughter(JetsVect[a]);
	      current_VBF.addDaughter(JetsVect[b]);
	      addP4.set(current_VBF);
	      curr_mjj = current_VBF.mass();
	      if(curr_delta_eta_reco>delta_eta_reco and curr_delta_eta_reco>DetaVBF and curr_mjj>InvmassVBF)//Work in progress
		{
		  delta_eta_reco = curr_delta_eta_reco;
		  j1=std::min(a,b);
		  j2=std::max(a,b);
		}



	    }


	  //old loop, no pre-conditions on mjj and deta
	  //  {
	  //  //calculate delta eta
          //  curr_delta_eta_reco = abs(JetsVect[a].eta() - JetsVect[b].eta());
	  //  if(curr_delta_eta_reco>delta_eta_reco)
	  //    {
	  //      delta_eta_reco = curr_delta_eta_reco;
	  //      j1=std::min(a,b);
	  //      j2=std::max(a,b);
	  //    }
	  //  }



        }
      }

      //if(isVerbose) std::cout << "VBF pair decided, filling theVBF candidate" << std::endl;
      //if(isVerbose) std::cout << "Size of JetsVect: " << JetsVect.size() << std::endl;
      //if(isVerbose) std::cout << "Chosen indices: " << j1 << "\t" << j2 << std::endl;

      if(j1>=0 && j2>=0)//otherwise, if indices are -1, theVBF seg faults
	{
	  theVBF.addDaughter(JetsVect.at(j1));
	  theVBF.addDaughter(JetsVect.at(j2));
	  addP4.set(theVBF);
	  //if(isVerbose) std::cout << "VBF pair decided, added daughters to theVBF; proceed with VBF pair jet vector" << std::endl;
	  //if(theVBF.mass()>400 and fabs(theVBF.daughter(0)->eta() - theVBF.daughter(1)->eta())>3)
	  //{
	  VBFPairJetsVect.push_back(JetsVect.at(j1));
	  VBFPairJetsVect.push_back(JetsVect.at(j2));
	  //}
	}
    }

    nVBFPairJets = VBFPairJetsVect.size();
    //if(isVerbose) std::cout << "Set boolean isVBF" << std::endl;

    if(theVBF.pt()>0 && theVBF.mass()>InvmassVBF && abs(theVBF.daughter(1)->eta() - theVBF.daughter(0)->eta())>DetaVBF) {isVBF = true;}

    ////Skip the event if VBF conditions not fulfilled
    ////!!! Removed, let's keep it as a flag. We need non-VBF events for control regions in data.

    // 27 Sep 2018: restored, to reduce output size
    if(WriteOnlyisVBFEvents)//set in cfg file
      {
	if(!isVBF) return;
      }

    // 2020_12_18 comment, because this trigger isn't studied!
    // //Find VBF pair in trigger standalone objects

    // float delta_eta_reco_HLT (0.), curr_delta_eta_reco_HLT(0.) ;
    // float curr_mjj_HLT (0.);
    // pat::CompositeCandidate current_VBF_HLT;
    // int j1_HLT(-1), j2_HLT(-1);

    // if(PotentialTriggerVBFPairJets.size()>=2) {
    //   //if(isVerbose) std::cout << "Loop over trigger standalone objects to determine VBF pair" << std::endl;
    //   for(unsigned int a = 0; a<PotentialTriggerVBFPairJets.size(); a++) {
    //     //find the VBF pair                                                                                                                                                             
    //     for(unsigned int b = 1; b<PotentialTriggerVBFPairJets.size(); b++) {


    // 	  //here: loop over the filters and consider only trigger objects firing the proper filter
    // 	  //not needed anymore

    // 	  //for (unsigned l = 0; l < PotentialTriggerVBFPairJets.at(a).filterLabels().size(); ++l)
    // 	  //{//TOBECLOSED

    // 	  //for (unsigned m = 0; m < PotentialTriggerVBFPairJets.at(b).filterLabels().size(); ++m)
    // 	  //{//TOBECLOSED

    // 	  //if(PotentialTriggerVBFPairJets.at(a).filterLabels()[l]=="hltVBFFilterDisplacedJets" and PotentialTriggerVBFPairJets.at(b).filterLabels()[m]=="hltVBFFilterDisplacedJets" and b!=a and PotentialTriggerVBFPairJets.at(a).pt()>=20 and PotentialTriggerVBFPairJets.at(b).pt()>=20 and (PotentialTriggerVBFPairJets.at(a).eta()*PotentialTriggerVBFPairJets.at(b).eta())<0)//CHECK!!!!!!!!!!!


    // 		  if(b!=a and PotentialTriggerVBFPairJets.at(a).pt()>=20 and PotentialTriggerVBFPairJets.at(b).pt()>=20 and (PotentialTriggerVBFPairJets.at(a).eta()*PotentialTriggerVBFPairJets.at(b).eta())<0)//CHECK!!!!!!!!!!!

    // 		    {
    // 		      //calculate delta eta
    // 		      curr_delta_eta_reco_HLT = abs(PotentialTriggerVBFPairJets[a].eta() - PotentialTriggerVBFPairJets[b].eta());
    // 		      current_VBF_HLT.clearDaughters();
    // 		      current_VBF_HLT.addDaughter(PotentialTriggerVBFPairJets[a]);
    // 		      current_VBF_HLT.addDaughter(PotentialTriggerVBFPairJets[b]);
    // 		      addP4.set(current_VBF_HLT);
    // 		      curr_mjj_HLT = current_VBF_HLT.mass();
    // 		      ////if(EventNumber==40628 or EventNumber==8841 or EventNumber==9952 or EventNumber==12405)
    // 		      ////{
    // 		      ////std::cout << "Event number: " << EventNumber << std::endl;
    // 		      ////std::cout << "Trigger pair: " << a << " , " << b <<std::endl;
    // 		      ////std::cout << "n of trigger objects: " << PotentialTriggerVBFPairJets.size() << std::endl;
    // 		      ////std::cout << "eta: " << PotentialTriggerVBFPairJets[a].eta() << " , " << PotentialTriggerVBFPairJets[b].eta() <<std::endl;
    // 		      ////std::cout << "Collection: " << PotentialTriggerVBFPairJets.at(a).collection() << PotentialTriggerVBFPairJets.at(b).collection() << std::endl;
    // 		      ////std::cout << "TypeID: ";
    // 		      ////for (unsigned h = 0; h < PotentialTriggerVBFPairJets[a].filterIds().size(); ++h) std::cout << " " << PotentialTriggerVBFPairJets[a].filterIds()[h] ;
    // 		      ////std::cout << std::endl;
    // 		      ////for (unsigned h = 0; h < PotentialTriggerVBFPairJets[b].filterIds().size(); ++h) std::cout << " " << PotentialTriggerVBFPairJets[b].filterIds()[h] ;
    // 		      ////std::cout << std::endl;
    // 		      ////std::cout << "dEta: " << curr_delta_eta_reco_HLT << std::endl;
    // 		      ////std::cout << "mjj: " << curr_mjj_HLT << std::endl;
    // 		      ////}
    // 		      if(curr_delta_eta_reco_HLT>delta_eta_reco_HLT and curr_delta_eta_reco_HLT>DetaVBF and curr_mjj_HLT>InvmassVBF)//Work in progress
    // 			{
    // 			  delta_eta_reco_HLT = curr_delta_eta_reco_HLT;
    // 			  j1_HLT=std::min(a,b);
    // 			  j2_HLT=std::max(a,b);
    // 			}
    // 		    }

    // 	  //}

    // 	  //}

    //     }
    //   }

    //   //if(isVerbose) std::cout << "Chosen indices of HLT VBF Pair: " << j1_HLT << "\t" << j2_HLT << std::endl;

    //   if(j1_HLT>=0 && j2_HLT>=0)//otherwise, if indices are -1, theVBF seg faults

    // 	//CHECK HERE VBF TRIGGER CONDITIONS
    // 	{

    // 	  //if(isVerbose) std::cout << "=========================================================" << std::endl;
    // 	  //if(isVerbose) std::cout << "=========================================================" << std::endl;
    // 	  //if(isVerbose) std::cout << "VBF Trigger pair: " <<std::endl;
    // 	  //if(isVerbose) std::cout << "A: pt, eta, phi " << PotentialTriggerVBFPairJets.at(j1_HLT).pt() << " " << PotentialTriggerVBFPairJets.at(j1_HLT).eta() << " " << PotentialTriggerVBFPairJets.at(j1_HLT).phi() << std::endl;
    // 	  //if(isVerbose) std::cout << "B: pt, eta, phi " << PotentialTriggerVBFPairJets.at(j2_HLT).pt() << " " << PotentialTriggerVBFPairJets.at(j2_HLT).eta() << " " << PotentialTriggerVBFPairJets.at(j2_HLT).phi() << std::endl;
    // 	  //if(isVerbose) std::cout << "Collection: a: " << PotentialTriggerVBFPairJets.at(j1_HLT).collection() << " , b: "<< PotentialTriggerVBFPairJets.at(j2_HLT).collection() << std::endl;
    // 	  //if(isVerbose) std::cout << "TypeID: ";
    // 	  //if(isVerbose) {for (unsigned h = 0; h < PotentialTriggerVBFPairJets[j1_HLT].filterIds().size(); ++h) std::cout << " " << PotentialTriggerVBFPairJets[j1_HLT].filterIds()[h] ;}
    // 	  //if(isVerbose) std::cout << std::endl;
    // 	  //if(isVerbose) {for (unsigned h = 0; h < PotentialTriggerVBFPairJets[j2_HLT].filterIds().size(); ++h) std::cout << " " << PotentialTriggerVBFPairJets[j2_HLT].filterIds()[h] ;}
    // 	  //if(isVerbose) std::cout << std::endl;
    // 	  //if(isVerbose) std::cout << "Filters: ";
    // 	  //if(isVerbose) {for (unsigned h = 0; h < PotentialTriggerVBFPairJets[j1_HLT].filterLabels().size(); ++h) std::cout << " " << PotentialTriggerVBFPairJets[j1_HLT].filterLabels()[h];}
    // 	  //if(isVerbose) std::cout << std::endl;
    // 	  //if(isVerbose) {for (unsigned h = 0; h < PotentialTriggerVBFPairJets[j2_HLT].filterLabels().size(); ++h) std::cout << " " << PotentialTriggerVBFPairJets[j2_HLT].filterLabels()[h];}
    // 	  //if(isVerbose) std::cout << std::endl;

    // 	  theTriggerVBF.addDaughter(PotentialTriggerVBFPairJets.at(j1_HLT));
    // 	  theTriggerVBF.addDaughter(PotentialTriggerVBFPairJets.at(j2_HLT));
    // 	  addP4.set(theTriggerVBF);
    // 	  //if(isVerbose) std::cout << "HLT VBF pair decided; proceed with HLT VBF pair jet vector" << std::endl;
    // 	  //if(theTriggerVBF.mass()>400 and fabs(theTriggerVBF.daughter(0)->eta() - theTriggerVBF.daughter(1)->eta())>3)
    // 	  //{
    // 	  TriggerVBFPairJetsVect.push_back(PotentialTriggerVBFPairJets.at(j1_HLT));
    // 	  TriggerVBFPairJetsVect.push_back(PotentialTriggerVBFPairJets.at(j2_HLT));
    // 	  //}
    // 	  //if(isVerbose) std::cout<< "d eta: " << abs(theTriggerVBF.daughter(1)->eta() - theTriggerVBF.daughter(0)->eta()) << std::endl;
    // 	  //if(isVerbose) std::cout<< "mjj: " << theTriggerVBF.mass() << std::endl;
    // 	}
    // }

    // if(theTriggerVBF.pt()>0 && theTriggerVBF.mass()>InvmassVBF && abs(theTriggerVBF.daughter(1)->eta() - theTriggerVBF.daughter(0)->eta())>DetaVBF) {isTriggerVBF = true;}

    // nTriggerVBFPairJets = TriggerVBFPairJetsVect.size();



    // float delta_R_VBF = 1000.;
    // float current_delta_R_VBF = 1000.;
    // int ch_VBF = -1;
    // std::vector<pat::Jet> SelectedVBFJetsVect;



    // for(unsigned int t1 = 0; t1<TriggerVBFPairJetsVect.size(); t1++)
    //   {

    // 	for(unsigned int s = 0; s<JetsVect.size(); s++)
    // 	  {
    // 	    current_delta_R_VBF = fabs(reco::deltaR(JetsVect.at(s).eta(),JetsVect.at(s).phi(),TriggerVBFPairJetsVect.at(t1).eta(),TriggerVBFPairJetsVect.at(t1).phi()));
    // 	    if(current_delta_R_VBF<0.6 and current_delta_R_VBF<delta_R_VBF) 
    // 	      {
    // 		delta_R_VBF=current_delta_R_VBF;
    // 		ch_VBF = s;
    // 	      }
    // 	  }


    // 	if(ch_VBF>=0) SelectedVBFJetsVect.push_back(JetsVect.at(ch_VBF));

    //   }


    // nSelectedVBFJets = SelectedVBFJetsVect.size();
    //std::cout << "Size of SelectedVBFJetsVect: " << nSelectedVBFJets << std::endl; 


    ////for(unsigned int k = 0; k<SelectedVBFJetsVect.size(); k++)
    ///{
    ///	if(!SelectedVBFJetsVect.at(k).hasUserInt("TriggerMatched_VBFJet")) SelectedVBFJetsVect.at(k).addUserInt("TriggerMatched_VBFJet",1);
    ///}





















    //this is obsolete.... check!



    //Match VBF jets with trigger objects

    //if(isVerbose) std::cout << "Matching VBF jets with trigger objects " << std::endl;

    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int s = 0; s<VBFPairJetsVect.size(); s++)
    //   {

    // 	//VBF_DisplacedJet40_VTightID_Hadronic
    // 	float delta_R_trigVBFJets_t1 = 1000.;
    // 	float current_delta_R_trigVBFJets_t1 = 1000.;
    // 	for(unsigned int t1 = 0; t1<PotentialTriggerVBFPairJets.size(); t1++)
    // 	  {
    // 	    current_delta_R_trigVBFJets_t1 = fabs(reco::deltaR(VBFPairJetsVect.at(s).eta(),VBFPairJetsVect.at(s).phi(),PotentialTriggerVBFPairJets.at(t1).eta(),PotentialTriggerVBFPairJets.at(t1).phi()));
    // 	    if(current_delta_R_trigVBFJets_t1<0.5 and current_delta_R_trigVBFJets_t1<delta_R_trigVBFJets_t1) 
    // 	      {
    // 		delta_R_trigVBFJets_t1=current_delta_R_trigVBFJets_t1;
    // 		////if(!VBFPairJetsVect.at(s).hasUserInt("TriggerMatched_VBFJet")) VBFPairJetsVect.at(s).addUserInt("TriggerMatched_VBFJet",1);
    // 	      }
    // 	  }

    // 	//VBF_DisplacedJet40_VVTightID_Hadronic
    // 	float delta_R_trigVBFJets_t2 = 1000.;
    // 	float current_delta_R_trigVBFJets_t2 = 1000.;
    // 	// for(unsigned int t2 = 0; t2<VBF_DisplacedJet40_VVTightID_Hadronic_Vec.size(); t2++)
    // 	//   {
    // 	//     current_delta_R_trigVBFJets_t2 = fabs(reco::deltaR(VBFPairJetsVect.at(s).eta(),VBFPairJetsVect.at(s).phi(),VBF_DisplacedJet40_VVTightID_Hadronic_Vec.at(t2).eta(),VBF_DisplacedJet40_VVTightID_Hadronic_Vec.at(t2).phi()));
    // 	//     if(current_delta_R_trigVBFJets_t2<0.5 and current_delta_R_trigVBFJets_t2<delta_R_trigVBFJets_t2) 
    // 	//       {
    // 	// 	delta_R_trigVBFJets_t2=current_delta_R_trigVBFJets_t2;
    // 	// 	if(!VBFPairJetsVect.at(s).hasUserInt("VBF_DisplacedJet40_VVTightID_Hadronic_match")) VBFPairJetsVect.at(s).addUserInt("VBF_DisplacedJet40_VVTightID_Hadronic_match",1);
    // 	//       }
    // 	//   }


    //   }


    //if(isVerbose) std::cout << "AK4 CHS counting ID" << std::endl;

    //Counts how many loose-tight ID jets are found in the event
    for(unsigned int a = 0; a<JetsVect.size(); a++) {
        if(JetsVect[a].hasUserInt("isLoose") && JetsVect[a].userInt("isLoose")>0) nLooseJets++;
        if(JetsVect[a].hasUserInt("isTight") && JetsVect[a].userInt("isTight")>0) nTightJets++;
	//2 Nov 2018: first calo-lifetime tentative tagging
	if(JetsVect[a].chargedHadronEnergyFraction()<0.2 && JetsVect[a].chargedMultiplicity()<10 && JetsVect[a].neutralEmEnergyFraction()<0.15 && JetsVect[a].neutralHadronEnergyFraction()>0.8 && JetsVect[a].photonEnergyFraction()<0.1) 
	  {
	    nLooseCaloTagJets++;
	    if(JetsVect[a].chargedHadronEnergyFraction()<0.08 && JetsVect[a].chargedMultiplicity()<8 && JetsVect[a].neutralEmEnergyFraction()<0.08 && JetsVect[a].neutralHadronEnergyFraction()>0.9 && JetsVect[a].photonEnergyFraction()<0.08 && (JetsVect[a].chargedEmEnergy() + JetsVect[a].neutralEmEnergy())<10) 
	      {
		nCaloTagJets++;
		JetsVect[a].addUserInt("isCaloTag",1);
	      }
	  }
    }


    //Clear the vector of structures at every event, because we are not using a fixed number of jets and not using the Reset/List function //#### Johannes
    Jets.clear();
    TriggerObjects.clear();
    //    TriggerObjectsAll.clear();
    TriggerObjects_DoubleJet90.clear();
    TriggerObjects_QuadJet45.clear();
    TriggerObjects_DoubleJetC112MaxDeta1p6.clear();
    TriggerObjects_DoubleJetC112.clear();
    TriggerObjects_SixJet30.clear();
    TriggerObjects_QuadPFJetMqq240.clear();
    TriggerObjects_QuadPFJetMqq500.clear();
    DisplacedJets.clear();
    VBFPairJets.clear();
    //TriggerVBFPairJets.clear();
    //TriggerDisplacedJets.clear();
    //SelectedDisplacedJet.clear();
    //SelectedVBFJets.clear();


    //Clear VBF vector, not needed anymore
    //JetsVect.clear();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 CHS Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //Fill a vector of AK4 CHS Jets, with kinematical cuts defined in the config file (pT, eta, eventually JetID or b-tagging)
    //if(isVerbose) std::cout << "AK4 CHS" << std::endl;

    //if(isVerbose) std::cout << "Fill displaced jets" << std::endl;
    // 2020_12_18 comment, because this isn't studied!
    // std::vector<pat::Jet> DisplacedJetsVect;//here: require centrality, eta<2

    // //std::cout<< "size of jet vect: " << JetsVect.size() << std::endl;

    // for(unsigned int s = 0; s<JetsVect.size(); s++)
    //   {
    // 	if( abs(JetsVect.at(s).eta()) <2.4) //Prev version(v4): eta<2; Now: eta<2.4
    // 	  {
    // 	  //if(fabs(JetsVect.at(s).eta())>2) DisplacedJetsVect.erase(DisplacedJetsVect.begin()+s);
    // 	    DisplacedJetsVect.push_back(JetsVect.at(s));
    // 	  }
    //   }
    //if(isVerbose) std::cout<< "size of displaced jet vect: " << DisplacedJetsVect.size() << std::endl;



    //Remove Trigger Jets marked as VBF
    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int s = 0; s<TriggerVBFPairJetsVect.size(); s++)
    //   {

    // 	for(unsigned int r = 0; r<PotentialTriggerDisplacedJets.size(); r++)
    // 	  {
    // 	    if(TriggerVBFPairJetsVect.at(s).pt()==PotentialTriggerDisplacedJets.at(r).pt() && isTriggerVBF) //if jets are don't tagged as VBF jets, don't remove them
    // 	      {
    // 		PotentialTriggerDisplacedJets.erase(PotentialTriggerDisplacedJets.begin()+r);
    // 	      }
    // 	  }//VBF jet pair removed
    //   }

    //if(isVerbose) std::cout<< "Removed: " << std::endl;


    //VBF OFFLINE might be wrongly assigned. First of all, get the jet matched to the trigger object that is not the trigger VBF pair
    //Matching: DisplacedJetsVect and PotentialTriggerDisplacedJets. Save the match as SelectedDisplacedJet
    // 2020_12_18 comment, because this trigger isn't studied!
    // float delta_R = 1000.;
    // float current_delta_R = 1000.;
    // int ch = -1;
    // std::vector<pat::Jet> SelectedDisplacedJetVect;

    // for(unsigned int s = 0; s<DisplacedJetsVect.size(); s++)
    //   {

    // 	if(DisplacedJetsVect.at(s).neutralHadronEnergyFraction()>0.9) nDisplaced++;

    // 	////if(isVerbose) std::cout << " - - - - - - - - - - - - - - - - - " << std::endl;
    // 	////if(isVerbose) std::cout << "Jet n. " << s << std::endl;
    // 	////if(isVerbose) std::cout << "pt " << DisplacedJetsVect.at(s).pt() << "; eta " << DisplacedJetsVect.at(s).eta() << "; phi " << DisplacedJetsVect.at(s).phi() << std::endl;

    // 	for(unsigned int t1 = 0; t1<PotentialTriggerDisplacedJets.size(); t1++)
    // 	  {

    // 	    ////if(s==DisplacedJetsVect.size()-1)
    // 	    ////{
    // 	    ////std::cout << " * * * * * * * * * * * * * * * * * " << std::endl;
    // 	    ////std::cout << "Trig obj n. " << t1 << std::endl;
    // 	    ////std::cout << "pt " << PotentialTriggerDisplacedJets.at(t1).pt() << "; eta " << PotentialTriggerDisplacedJets.at(t1).eta() << "; phi " << PotentialTriggerDisplacedJets.at(t1).phi() << std::endl;
    // 	    ////std::cout << "; isJet " << PotentialTriggerDisplacedJets.at(t1).isJet() << "; pdgId " << PotentialTriggerDisplacedJets.at(t1).pdgId() << std::endl;
    // 	    ////std::cout << "filter ids " << PotentialTriggerDisplacedJets.at(t1).filterIds() << "; filter labels " << PotentialTriggerDisplacedJets.at(t1).filterLabels() << "; isJet " << PotentialTriggerDisplacedJets.at(t1).isJet() << "; pdgId " << PotentialTriggerDisplacedJets.at(t1).pdgId() << std::endl;
    // 	    ////std::cout << " * * * * * * * * * * * * * * * * * " << std::endl;
    // 	    ////}

    // 	    current_delta_R = fabs(reco::deltaR(DisplacedJetsVect.at(s).eta(),DisplacedJetsVect.at(s).phi(),PotentialTriggerDisplacedJets.at(t1).eta(),PotentialTriggerDisplacedJets.at(t1).phi()));
    // 	    ////if(isVerbose) std::cout << "Matching jet n." << s << " and trigger obj n." << t1 << std::endl;
    // 	    ////if(isVerbose) std::cout << "Trig obj n. " << t1 << std::endl;
    // 	    ////if(isVerbose) std::cout << "pt " << PotentialTriggerDisplacedJets.at(t1).pt() << "; eta " << PotentialTriggerDisplacedJets.at(t1).eta() << "; phi " << PotentialTriggerDisplacedJets.at(t1).phi() << std::endl;
    // 	    ////if(isVerbose) std::cout << "Their dR: " << current_delta_R << std::endl;
    // 	    if(current_delta_R<0.6 and current_delta_R<delta_R) 
    // 	      {
    // 		////if(isVerbose) std::cout << "Smaller than 0.6!!!!!!!!!!!!!!" << std::endl;
    // 		////if(isVerbose) std::cout << "Delta pt: " << fabs(PotentialTriggerDisplacedJets.at(t1).pt() - DisplacedJetsVect.at(s).pt()) << std::endl;

    // 		//if(isVerbose) std::cout << "* * * ** * * ** *** * ** * * " << std::endl;
    // 		//if(isVerbose) std::cout << "Trigger object selected as displaced jet: " <<std::endl;
    // 		//if(isVerbose) std::cout << "pt, eta, phi " << PotentialTriggerDisplacedJets.at(t1).pt() << " " << PotentialTriggerDisplacedJets.at(t1).eta() << " " << PotentialTriggerDisplacedJets.at(t1).phi() << std::endl;
    // 		//if(isVerbose) std::cout << "Collection: " << PotentialTriggerDisplacedJets.at(t1).collection() << std::endl;
    // 		//if(isVerbose) std::cout << "TypeID: ";
    // 		//if(isVerbose) {for (unsigned h = 0; h < PotentialTriggerDisplacedJets.at(t1).filterIds().size(); ++h) std::cout << " " << PotentialTriggerDisplacedJets.at(t1).filterIds()[h] ;}
    // 		//if(isVerbose) std::cout << std::endl;
    // 		//if(isVerbose) std::cout << "Filters: ";
    // 		//if(isVerbose)  {for (unsigned h = 0; h < PotentialTriggerDisplacedJets.at(t1).filterLabels().size(); ++h) std::cout << " " << PotentialTriggerDisplacedJets.at(t1).filterLabels()[h];}
    // 		//if(isVerbose) std::cout << std::endl;
    // 		delta_R=current_delta_R;
    // 		ch = s;
    // 	      }
    // 	  }


    //   }

    //if(isVerbose) std::cout << "Chosen matched jet is " << ch << std::endl;
    // 2020_12_18 comment, because this trigger isn't studied!
    // if(ch>=0)
    //   {
    // 	//if(!DisplacedJetsVect.at(ch).hasUserInt("VBF_DisplacedJet40_VTightID_Hadronic_match"))
    // 	/////////DisplacedJetsVect.at(ch).addUserInt("TriggerMatched_DisplacedJet",1);
    // 	SelectedDisplacedJetVect.push_back(DisplacedJetsVect.at(ch));
    //   }

    // nSelectedDisplacedJet = SelectedDisplacedJetVect.size();

    //REMOVE VBF JETS FROM SIGNAL COLLECTION ONLY!!!
    
    //Remove jets tagged as VBF from the list of potential signal    
    //if(isVerbose) std::cout << "Remove VBF pair from displaced jets" << std::endl;

    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int s = 0; s<VBFPairJetsVect.size(); s++)
    //   {
    // 	//std::cout << "VBF pair jet index: " << s << std::endl;
    // 	for(unsigned int r = 0; r<DisplacedJetsVect.size(); r++)
    // 	  {
    // 	    //std::cout << "displ jet index: " << r << std::endl;
    // 	    if(VBFPairJetsVect.at(s).pt()==DisplacedJetsVect.at(r).pt() && isVBF) //if jets are don't tagged as VBF jets, don't remove them
    // 	      {
    // 		//std::cout << "same jet: jet n." << r  << " , VBF pair n." << s << std::endl;
    // 		DisplacedJetsVect.erase(DisplacedJetsVect.begin()+r);
    // 		//std::cout << "jet n." << r  << " removed!!! " << std::endl;
    // 		//std::cout << "size of displaced jet vect now: " << DisplacedJetsVect.size() << std::endl;
    // 		//std::cout << "But r is still: " << r << std::endl;
    // 	      }
    // 	    //std::cout << "size of displaced jet vect: " << DisplacedJetsVect.size() << std::endl;
    // 	  }//VBF jet pair removed
    //   }
    
    
    
    //if(isVerbose) std::cout << "Match Jets with trigger objects" << std::endl;

    
    //Assign flags to jets matched to trigger objects
    //VBF jets trigger matched: SelectedVBFJetsVect
    //Displaced jets trigger matched: SelectedDisplacedJet
    //To be checked: JetsVect, VBFPairJetsVect, DisplacedJetsVect

    //.at(k).addUserInt("TriggerMatched_VBFJet",1);
    //.at(k).addUserInt("TriggerMatched_DisplacedJet",1);

    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int s = 0; s<VBFPairJetsVect.size(); s++)
    //   {

    // 	//VBF Trigger
    // 	for(unsigned int a = 0; a<SelectedVBFJetsVect.size(); a++)
    // 	  {
    // 	    if(SelectedVBFJetsVect.at(a).pt()==VBFPairJetsVect.at(s).pt())
    // 	      {
    // 		if(!VBFPairJetsVect.at(s).hasUserInt("TriggerMatched_VBFJet")) VBFPairJetsVect.at(s).addUserInt("TriggerMatched_VBFJet",1);
    // 	      }
    //       }

    // 	//Displaced Trigger
    // 	for(unsigned int b = 0; b<SelectedDisplacedJetVect.size(); b++)
    // 	  {
    // 	    if(SelectedDisplacedJetVect.at(b).pt()==VBFPairJetsVect.at(s).pt())
    // 	      {
    // 		if(!VBFPairJetsVect.at(s).hasUserInt("TriggerMatched_DisplacedJet")) VBFPairJetsVect.at(s).addUserInt("TriggerMatched_DisplacedJet",1);
    // 	      }
    //       }

    //   }

    
    // for(unsigned int s = 0; s<DisplacedJetsVect.size(); s++)
    //   {

    // 	//VBF Trigger
    // 	for(unsigned int a = 0; a<SelectedVBFJetsVect.size(); a++)
    // 	  {
    // 	    if(SelectedVBFJetsVect.at(a).pt()==DisplacedJetsVect.at(s).pt())
    // 	      {
    // 		if(!DisplacedJetsVect.at(s).hasUserInt("TriggerMatched_VBFJet")) DisplacedJetsVect.at(s).addUserInt("TriggerMatched_VBFJet",1);
    // 	      }
    //       }

    // 	//Displaced Trigger
    // 	for(unsigned int b = 0; b<SelectedDisplacedJetVect.size(); b++)
    // 	  {
    // 	    if(SelectedDisplacedJetVect.at(b).pt()==DisplacedJetsVect.at(s).pt())
    // 	      {
    // 		if(!DisplacedJetsVect.at(s).hasUserInt("TriggerMatched_DisplacedJet")) DisplacedJetsVect.at(s).addUserInt("TriggerMatched_DisplacedJet",1);
    // 	      }
    //       }

    //   }
    

    

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // PFCandidates
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //std::vector<pat::PackedCandidate> PFCandidateVect;
    //std::vector<int> PFCandidateJetIndex;
    //std::vector<int> PFCandidateVtxIndex;

    //PFCandidateVect = thePFCandidateAnalyzer->FillPFCandidateVector(iEvent);
    // Initialize PFCandidate variables: Set indices to -1 (not matched)
    //for(unsigned int i = 0; i < PFCandidateVect.size(); i++){
    //PFCandidateJetIndex.push_back(-1);
    //PFCandidateVtxIndex.push_back(-1);
    //}


    //Matching
    //unsigned int nPFCandidatesMatchedToJet = 0;//new
    //for(unsigned int i = 0; i < PFCandidateVect.size(); i++){

    //int nMatchedJets = 0; // TODO: Remove if no warnings are observed during a large production.

      
      //if (nMatchedJets > 1) std::cout << "WARNING: More than 1 JetContituent has been matched to PFCandidate " << i << std::endl;
        
      //}


    if(isVerbose) {
      //Write a summary, in verbose mode
      std::cout << " --- Event n. " << iEvent.id().event() << ", lumi " << iEvent.luminosityBlock() << ", run " << iEvent.id().run() << std::endl;
      std::cout << "number of CHS AK4 jets:  " << JetsVect.size() << std::endl;
      for(unsigned int i = 0; i < JetsVect.size(); i++) std::cout << "  CHS AK4 jet  [" << i << "]\tpt: " << JetsVect[i].pt() << "\teta: " << JetsVect[i].eta() << "\tphi: " << JetsVect[i].phi() << "\tmass: " << JetsVect[i].mass() << std::endl;

      //      std::cout << "number of trigger objects matched to hltTripleJet50:  " << TripleJet50TriggerVec.size() << std::endl;
      //      for(unsigned int i = 0; i < TripleJet50TriggerVec.size(); i++) std::cout << "  Trigger object  [" << i << "]\tpt: " << TripleJet50TriggerVec[i].pt() << "\teta: " << TripleJet50TriggerVec[i].eta() << "\tphi: " << TripleJet50TriggerVec[i].phi() << "\tmass: " << TripleJet50TriggerVec[i].mass() << std::endl;
      std::cout << "VBF jets pair:  " << VBFPairJetsVect.size() << std::endl;
      if(isVBF) std::cout << "VBF conditions satisfied" << std::endl;
      for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) std::cout << "  VBF jet  [" << i << "]\tpt: " << VBFPairJetsVect[i].pt() << "\teta: " << VBFPairJetsVect[i].eta() << "\tphi: " << VBFPairJetsVect[i].phi() << "\tmass: " << VBFPairJetsVect[i].mass() << std::endl;
      // std::cout << "number of displaced AK4 jets:  " << DisplacedJetsVect.size() << std::endl;
      // for(unsigned int i = 0; i < DisplacedJetsVect.size(); i++) std::cout << "  displaced CHS AK4 jet  [" << i << "]\tpt: " << DisplacedJetsVect[i].pt() << "\teta: " << DisplacedJetsVect[i].eta() << "\tphi: " << DisplacedJetsVect[i].phi() << "\tmass: " << DisplacedJetsVect[i].mass() << std::endl;

    }


    //Vectors of structures
    //Here it doesn't know JetsVect size, hence we cannot store a dynamic amount of things. Trying to do it inside Analyze method
    for(unsigned int i = 0; i < JetsVect.size(); i++) Jets.push_back( JetType() );
    for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) VBFPairJets.push_back( JetType() );
    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int i = 0; i < DisplacedJetsVect.size(); i++) DisplacedJets.push_back( JetType() );
    // for(unsigned int i = 0; i < TripleJet50TriggerVec.size(); i++) TriggerObjects.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < MuonVect.size(); i++) Muons.push_back( LeptonType() );
    //    for(unsigned int i = 0; i < TriggerObjectsVector.size(); i++) TriggerObjectsAll.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < DoubleJet90_Vec.size(); i++) TriggerObjects_DoubleJet90.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < QuadJet45_Vec.size(); i++) TriggerObjects_QuadJet45.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < DoubleJetC112MaxDeta1p6_Vec.size(); i++) TriggerObjects_DoubleJetC112MaxDeta1p6.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < DoubleJetC112_Vec.size(); i++) TriggerObjects_DoubleJetC112.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < SixJet30_Vec.size(); i++) TriggerObjects_SixJet30.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < QuadPFJetMqq240_Vec.size(); i++) TriggerObjects_QuadPFJetMqq240.push_back( TriggerObjectType() );
    for(unsigned int i = 0; i < QuadPFJetMqq500_Vec.size(); i++) TriggerObjects_QuadPFJetMqq500.push_back( TriggerObjectType() );
    ////if (WriteFatJets) for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) CHSFatJets.push_back( FatJetType() );
    //for(unsigned int i = 0; i < TriggerVBFPairJetsVect.size(); i++) TriggerVBFPairJets.push_back( TriggerObjectType() );
    //for(unsigned int i = 0; i < PotentialTriggerDisplacedJets.size(); i++) TriggerDisplacedJets.push_back( TriggerObjectType() );
    //for(unsigned int i = 0; i < SelectedDisplacedJetVect.size(); i++) SelectedDisplacedJet.push_back( JetType() );
    //for(unsigned int i = 0; i < SelectedVBFJetsVect.size(); i++) SelectedVBFJets.push_back( JetType() );


    // ---------- Fill objects ----------

    //if(isVerbose) std::cout << " - Filling objects" << std::endl;

    std::vector<float> nullFloat;
    std::vector<int> nullInt;


    for(unsigned int i = 0; i < JetsVect.size(); i++) {
      nullFloat.push_back(-100.);
      nullInt.push_back(-1);
    }

    for(unsigned int i = 0; i < JetsVect.size(); i++){
      ObjectsFormat::FillJetType(Jets[i], &JetsVect[i], isMC);//, nullInt[i]);//Remove Jets.size(), testing
      //      if(isVerbose) {
	//std::cout << " j[" << i << "] n const: " << Jets[i].nConstituents << std::endl; 
	//std::cout << " j[" << i << "] n Track const: " << Jets[i].nTrackConstituents << std::endl; 
	//std::cout << " j[" << i << "] n selected track: " << Jets[i].nSelectedTracks << std::endl; 
	//std::cout << " j[" << i << "] matched to trigger: " << Jets[i].VBF_DisplacedJet40_VTightID_Hadronic_match << std::endl; 
      //      }
    }


    ObjectsFormat::FillMEtType(MEt, &MET, isMC);


    nullFloat.clear();
    nullInt.clear();
    for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) {
      nullFloat.push_back(-100.);
      nullInt.push_back(-1);
    }

    for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++){
      ObjectsFormat::FillJetType(VBFPairJets[i], &VBFPairJetsVect[i], isMC);//, nullInt[i]);
    }

    // 2020_12_18 comment, because this trigger isn't studied!
    // nullFloat.clear();
    // nullInt.clear();
    // for(unsigned int i = 0; i < DisplacedJetsVect.size(); i++) {
    //   nullFloat.push_back(-100.);
    //   nullInt.push_back(-1);
    // }
    // for(unsigned int i = 0; i < DisplacedJetsVect.size(); i++){
    //   ObjectsFormat::FillJetType(DisplacedJets[i], &DisplacedJetsVect[i], isMC);//, nullInt[i]);
    // }

    //nullFloat.clear();
    //nullInt.clear();
    //for(unsigned int i = 0; i < SelectedDisplacedJetVect.size(); i++) {
    //nullFloat.push_back(-100.);
    //nullInt.push_back(-1);
    //}

    //for(unsigned int i = 0; i < SelectedDisplacedJetVect.size(); i++){
    //ObjectsFormat::FillJetType(SelectedDisplacedJet[i], &SelectedDisplacedJetVect[i], isMC, nullFloat[i], nullFloat[i], nullFloat[i], nullInt[i]);
    //}


    //nullFloat.clear();
    //nullInt.clear();
    //for(unsigned int i = 0; i < SelectedVBFJetsVect.size(); i++) {
    //nullFloat.push_back(-100.);
    //nullInt.push_back(-1);
    //}

    //for(unsigned int i = 0; i < SelectedVBFJetsVect.size(); i++){
    //ObjectsFormat::FillJetType(SelectedVBFJets[i], &SelectedVBFJetsVect[i], isMC, nullFloat[i], nullFloat[i], nullFloat[i], nullInt[i]);
    //}


    ObjectsFormat::FillCandidateType(VBF, &theVBF, isMC);
    ObjectsFormat::FillCandidateType(TriggerVBF, &theTriggerVBF, isMC);
    // for(unsigned int i = 0; i < TriggerObjectsVector.size(); i++){
    //   ObjectsFormat::FillTriggerObjectType(TriggerObjectsAll[i], &TriggerObjectsVector[i]);
    // }
    for(unsigned int i = 0; i < DoubleJet90_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_DoubleJet90[i], &DoubleJet90_Vec[i]);
    }
    for(unsigned int i = 0; i < QuadJet45_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_QuadJet45[i], &QuadJet45_Vec[i]);
    }
    for(unsigned int i = 0; i < DoubleJetC112MaxDeta1p6_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_DoubleJetC112MaxDeta1p6[i], &DoubleJetC112MaxDeta1p6_Vec[i]);
    }
    for(unsigned int i = 0; i < DoubleJetC112_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_DoubleJetC112[i], &DoubleJetC112_Vec[i]);
    }
    for(unsigned int i = 0; i < SixJet30_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_SixJet30[i], &SixJet30_Vec[i]);
    }
    for(unsigned int i = 0; i < QuadPFJetMqq240_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_QuadPFJetMqq240[i], &QuadPFJetMqq240_Vec[i]);
    }
    for(unsigned int i = 0; i < QuadPFJetMqq500_Vec.size(); i++){
      ObjectsFormat::FillTriggerObjectType(TriggerObjects_QuadPFJetMqq500[i], &QuadPFJetMqq500_Vec[i]);
    }


    // 2020_12_18 comment, because this trigger isn't studied!
    // for(unsigned int i = 0; i < TripleJet50TriggerVec.size(); i++){
    //   ObjectsFormat::FillTriggerObjectType(TriggerObjects[i], &TripleJet50TriggerVec[i]);
    //   //std:: cout << "Trigger object n. " << i << std::endl;
    //   //std:: cout << "pt " << TriggerObjects[i].pt << std::endl;
    //   //std:: cout << "pt " << TripleJet50TriggerVec.at(i).pt() << std::endl;
    //   //std:: cout << "eta " << TripleJet50TriggerVec.at(i).eta() << std::endl;
    //   //std:: cout << "phi " << TripleJet50TriggerVec.at(i).phi() << std::endl;
    // }

    for(unsigned int i = 0; i < Muons.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &MuonVect[i], isMC);
    //for(unsigned int i = 0; i < TriggerVBFPairJetsVect.size(); i++){
    //ObjectsFormat::FillTriggerObjectType(TriggerVBFPairJets[i], &TriggerVBFPairJetsVect[i]);
    //}

    //for(unsigned int i = 0; i < PotentialTriggerDisplacedJets.size(); i++){
    //ObjectsFormat::FillTriggerObjectType(TriggerDisplacedJets[i], &PotentialTriggerDisplacedJets[i]);
    //}

    tree -> Fill();
    //if(isVerbose) std::cout << " - Tree filled, next event" << std::endl;

}


// ------------ method called once each job just before starting event loop  ------------
void
TriggerStudies::beginJob()
{

    std::cout << "BEGIN JOB!" << std::endl;

    //Tree branches
    tree = fs->make<TTree>("tree", "tree");
    tree -> Branch("isMC" , &isMC, "isMC/O");
    tree -> Branch("EventNumber" , &EventNumber , "EventNumber/L");
    tree -> Branch("LumiNumber" , &LumiNumber , "LumiNumber/L");
    tree -> Branch("RunNumber" , &RunNumber , "RunNumber/L");
    tree -> Branch("EventWeight", &EventWeight, "EventWeight/F");
    tree -> Branch("AtLeastOneTrigger" , &AtLeastOneTrigger , "AtLeastOneTrigger/O");
    tree -> Branch("AtLeastOneL1Filter" , &AtLeastOneL1Filter , "AtLeastOneL1Filter/O");
    tree -> Branch("Prefired" , &Prefired , "Prefired/O");
    tree -> Branch("nPV" , &nPV , "nPV/L");
    tree -> Branch("nSV" , &nSV , "nSV/L");
    tree -> Branch("PUWeight", &PUWeight, "PUWeight/F");
    //tree -> Branch("ZewkWeight", &ZewkWeight, "ZewkWeight/F");
    //tree -> Branch("WewkWeight", &WewkWeight, "WewkWeight/F");
    tree -> Branch("nJets" , &nJets , "nJets/L");
    //    tree -> Branch("nTriggerObjectsTripleJet50" , &nTriggerObjectsTripleJet50 , "nTriggerObjectsTripleJet50/L");
    //    tree -> Branch("nTriggerObjectsTripleJet50WithDuplicates" , &nTriggerObjectsTripleJet50WithDuplicates , "nTriggerObjectsTripleJet50WithDuplicates/L");
    tree -> Branch("nTriggerObjectsDoubleJet90" , &nTriggerObjectsDoubleJet90 , "nTriggerObjectsDoubleJet90/L");
    tree -> Branch("nTriggerObjectsQuadJet45" , &nTriggerObjectsQuadJet45 , "nTriggerObjectsQuadJet45/L");
    tree -> Branch("nTriggerObjectsDoubleJetC112MaxDeta1p6" , &nTriggerObjectsDoubleJetC112MaxDeta1p6 , "nTriggerObjectsDoubleJetC112MaxDeta1p6/L");
    tree -> Branch("nTriggerObjectsDoubleJetC112" , &nTriggerObjectsDoubleJetC112 , "nTriggerObjectsDoubleJetC112/L");
    tree -> Branch("nTriggerObjectsSixJet30" , &nTriggerObjectsSixJet30 , "nTriggerObjectsSixJet30/L");
    tree -> Branch("nTriggerObjectsQuadPFJetMqq240" , &nTriggerObjectsQuadPFJetMqq240 , "nTriggerObjectsQuadPFJetMqq240/L");
    tree -> Branch("nTriggerObjectsQuadPFJetMqq500" , &nTriggerObjectsQuadPFJetMqq500 , "nTriggerObjectsQuadPFJetMqq500/L");
    tree -> Branch("nLooseJets" , &nLooseJets , "nLooseJets/L");
    tree -> Branch("nTightJets" , &nTightJets , "nTightJets/L");
    tree -> Branch("nLooseCaloTagJets" , &nLooseCaloTagJets , "nLooseCaloTagJets/L");
    tree -> Branch("nCaloTagJets" , &nCaloTagJets , "nCaloTagJets/L");
    tree -> Branch("nElectrons", &nElectrons, "nElectrons/I");
    tree -> Branch("nMuons", &nMuons, "nMuons/I");
    tree -> Branch("nTightMuons", &nTightMuons, "nTightMuons/I");
    tree -> Branch("nTaus", &nTaus, "nTaus/I");
    tree -> Branch("nPhotons", &nPhotons, "nPhotons/I");
    tree -> Branch("nTriggerObjects" , &nTriggerObjects , "nTriggerObjects/L");
    // tree -> Branch("nSelectedDisplacedJet" , &nSelectedDisplacedJet , "nSelectedDisplacedJet/L");
    // tree -> Branch("nSelectedVBFJets" , &nSelectedVBFJets , "nSelectedVBFJets/L");
    tree -> Branch("nDisplaced" , &nDisplaced , "nDisplaced/L");
    tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
    tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
    tree -> Branch("isVBF" , &isVBF, "isVBF/O");
    tree -> Branch("isTriggerVBF" , &isTriggerVBF, "isTriggerVBF/O");
    tree -> Branch("HT" , &HT , "HT/F");
    //tree->Branch("MinJetMetDPhi", &MinJetMetDPhi, "MinJetMetDPhi/F");
    tree->Branch("MEt_pt", &MEt.pt, "MEt_pt/F");
    tree->Branch("MEt_phi", &MEt.phi, "MEt_phi/F");
    tree->Branch("met_pt_nomu", &met_pt_nomu, "met_pt_nomu/F");
    tree->Branch("Muon1_pt", &muon1_pt, "Muon1_pt/F");
    tree->Branch("Muon1_eta", &muon1_eta, "Muon1_eta/F");
    tree->Branch("Muon1_phi", &muon1_phi, "Muon1_phi/F");
    // Set trigger branches
    for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
    if(isVerboseTrigger)//save PS values in ntuple
        { 
  	    for(auto it = PrescalesTriggerMap.begin(); it != PrescalesTriggerMap.end(); it++) {
	        tree->Branch( ("PS_" + it->first).c_str(), &(it->second), ("PS_" + it->first+"/I").c_str());
	    }
        }
    for(auto it = MetFiltersMap.begin(); it != MetFiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
    for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
    for(auto it = L1BitsMap.begin(); it != L1BitsMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());

    //tree->Branch("MEt", &MEt.pt, ObjectsFormat::ListMEtType().c_str());


    tree -> Branch("VBFPair", &VBF.pt, ObjectsFormat::ListCandidateType().c_str());
    tree -> Branch("TriggerVBFPair", &TriggerVBF.pt, ObjectsFormat::ListCandidateType().c_str());
    tree -> Branch("Jets", &Jets);
    tree -> Branch("VBFPairJets", &VBFPairJets);
    // tree -> Branch("DisplacedJets", &DisplacedJets);
    // tree -> Branch("TripleJet50TriggerObjects", &TriggerObjects);
    //    tree -> Branch("TriggerObjectsAll", &TriggerObjectsAll);
    tree -> Branch("TriggerObjects_DoubleJet90", &TriggerObjects_DoubleJet90);
    tree -> Branch("TriggerObjects_QuadJet45", &TriggerObjects_QuadJet45);
    tree -> Branch("TriggerObjects_DoubleJetC112MaxDeta1p6", &TriggerObjects_DoubleJetC112MaxDeta1p6);
    tree -> Branch("TriggerObjects_DoubleJetC112", &TriggerObjects_DoubleJetC112);
    tree -> Branch("TriggerObjects_SixJet30", &TriggerObjects_SixJet30);
    tree -> Branch("TriggerObjects_QuadPFJetMqq240", &TriggerObjects_QuadPFJetMqq240);
    tree -> Branch("TriggerObjects_QuadPFJetMqq500", &TriggerObjects_QuadPFJetMqq500);
    tree -> Branch("Muons", &Muons);
    //tree -> Branch("TriggerVBFPairJets", &TriggerVBFPairJets);
    //tree -> Branch("TriggerDisplacedJets", &TriggerDisplacedJets);
    //tree -> Branch("SelectedDisplacedJet", &SelectedDisplacedJet);
    //tree -> Branch("SelectedVBFJets", &SelectedVBFJets);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerStudies::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerStudies::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(TriggerStudies);

