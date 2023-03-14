
//
// Package:    Analyzer/LLP
// Class:      Ntuplizer
//
/**\class Ntuplizer Ntuplizer.cc Analyzer/LLP/plugins/Ntuplizer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Lisa Benato
//         Created:  Tue, 24 Jul 2018 11:12:19 GMT
//
//


#include "Ntuplizer.h"

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
//Ntuplizer::Ntuplizer(const edm::ParameterSet& iConfig, edm::ConsumesCollector&& CColl):
Ntuplizer::Ntuplizer(const edm::ParameterSet& iConfig):
    GenPSet(iConfig.getParameter<edm::ParameterSet>("genSet")),
    PileupPSet(iConfig.getParameter<edm::ParameterSet>("pileupSet")),
    TriggerPSet(iConfig.getParameter<edm::ParameterSet>("triggerSet")),
    AllJetPSet(iConfig.getParameter<edm::ParameterSet>("allJetSet")),
    CHSJetPSet(iConfig.getParameter<edm::ParameterSet>("chsJetSet")),
    VBFJetPSet(iConfig.getParameter<edm::ParameterSet>("vbfJetSet")),
    CHSFatJetPSet(iConfig.getParameter<edm::ParameterSet>("chsFatJetSet")),
    //CaloJetPSet(iConfig.getParameter<edm::ParameterSet>("caloJetSet")),
    ElectronPSet(iConfig.getParameter<edm::ParameterSet>("electronSet")),
    MuonPSet(iConfig.getParameter<edm::ParameterSet>("muonSet")),
    TauPSet(iConfig.getParameter<edm::ParameterSet>("tauSet")),
    PhotonPSet(iConfig.getParameter<edm::ParameterSet>("photonSet")),
    VertexPSet(iConfig.getParameter<edm::ParameterSet>("vertexSet")),
    PFCandidatePSet(iConfig.getParameter<edm::ParameterSet>("pfCandidateSet")),
    ROIPSet(iConfig.getParameter<edm::ParameterSet>("roiSet")),
    V0PSet(iConfig.getParameter<edm::ParameterSet>("v0Set")), 
    //JetTagToken(CColl.consumes<reco::JetTagCollection>(iConfig.getParameter<edm::InputTag>("jetTagToken"))),//here????
    idLLP(iConfig.getParameter<int>("idLLP")),
    idHiggs(iConfig.getParameter<int>("idHiggs")),
    idMotherB(iConfig.getParameter<int>("idMotherB")),
    statusLLP(iConfig.getParameter<int>("statusLLP")),
    statusHiggs(iConfig.getParameter<int>("statusHiggs")),
    MinGenBpt(iConfig.getParameter<double>("minGenBpt")),
    MaxGenBeta(iConfig.getParameter<double>("maxGenBeta")),
    MinHT(iConfig.getParameter<double>("minHT")),
    InvmassVBF(iConfig.getParameter<double>("invmassVBF")),
    DetaVBF(iConfig.getParameter<double>("detaVBF")),
    //WriteNJets(iConfig.getParameter<int>("writeNJets")),//unused, we have vectors now
    //WriteNFatJets(iConfig.getParameter<int>("writeNFatJets")),//unused, we have vectors now
    //WriteNGenBquarks(iConfig.getParameter<int>("writeNGenBquarks")),
    //WriteNGenLongLiveds(iConfig.getParameter<int>("writeNGenLongLiveds")),
    WriteGenVBFquarks(iConfig.getParameter<bool>("writeGenVBFquarks")),
    WriteGenHiggs(iConfig.getParameter<bool>("writeGenHiggs")),
    WriteGenLLPs(iConfig.getParameter<bool>("writeGenLLPs")),
    WriteGenBquarks(iConfig.getParameter<bool>("writeGenBquarks")),
    WriteGenMuons(iConfig.getParameter<bool>("writeGenMuons")),
    WriteNMatchedJets(iConfig.getParameter<int>("writeNMatchedJets")),
    WriteNLeptons(iConfig.getParameter<int>("writeNLeptons")),
    WriteOnlyTriggerEvents(iConfig.getParameter<bool>("writeOnlyTriggerEvents")),
    WriteOnlyL1FilterEvents(iConfig.getParameter<bool>("writeOnlyL1FilterEvents")),
    WriteOnlyisVBFEvents(iConfig.getParameter<bool>("writeOnlyisVBFEvents")),
    WriteFatJets(iConfig.getParameter<bool>("writeFatJets")),
    WriteAllJets(iConfig.getParameter<bool>("writeAllJets")),
    WriteAK4JetPFCandidates(iConfig.getParameter<bool>("writeAK4JetPFCandidates")),
    WriteAK8JetPFCandidates(iConfig.getParameter<bool>("writeAK8JetPFCandidates")),
    WriteAllJetPFCandidates(iConfig.getParameter<bool>("writeAllJetPFCandidates")),
    WriteAllPFCandidates(iConfig.getParameter<bool>("writeAllPFCandidates")),
    WriteLostTracks(iConfig.getParameter<bool>("writeLostTracks")),
    WriteVertices(iConfig.getParameter<bool>("writeVertices")),
    WriteBtagInfos(iConfig.getParameter<bool>("writeBtagInfos")),
    WriteROITaggerScore(iConfig.getParameter<bool>("writeROITaggerScore")),
    WriteROITaggerInputs(iConfig.getParameter<bool>("writeROITaggerInputs")),
    WriteKShorts(iConfig.getParameter<bool>("writeKShorts")),
    WriteLambdas(iConfig.getParameter<bool>("writeLambdas")), 
    CalculateNsubjettiness(iConfig.getParameter<bool>("calculateNsubjettiness")),
    PerformPreFiringStudies(iConfig.getParameter<bool>("performPreFiringStudies")),
    PerformVBF(iConfig.getParameter<bool>("performVBF")),
    PerformggH(iConfig.getParameter<bool>("performggH")),
    isVerbose(iConfig.getParameter<bool> ("verbose")),
    isVerboseTrigger(iConfig.getParameter<bool> ("verboseTrigger")),
    isSignal(iConfig.getParameter<bool> ("signal")),
    isCalo(iConfig.getParameter<bool> ("iscalo")),
    isTracking(iConfig.getParameter<bool> ("istracking")),
    isShort(iConfig.getParameter<bool> ("isshort")),
    isControl(iConfig.getParameter<bool> ("iscontrol")),
    isCentralProd(iConfig.getParameter<bool> ("iscentralprod")),
    is2016(iConfig.getParameter<bool> ("isera2016")),
    is2017(iConfig.getParameter<bool> ("isera2017")),
    is2018(iConfig.getParameter<bool> ("isera2018"))


{
    // Check writePFCandidate flags
    int PFCandidateFlags = 0;
    if (WriteAK4JetPFCandidates) PFCandidateFlags++;
    if (WriteAK8JetPFCandidates) PFCandidateFlags++;
    if (WriteAllJetPFCandidates) PFCandidateFlags++;
    if (WriteAllPFCandidates)    PFCandidateFlags++;
    if (PFCandidateFlags > 1)   throw cms::Exception("Configuration") << "More than one writePFCandidates flag selected. Please choose one option only!";

    //Initalize objects
    AllJetAnalyzer         = new JetAnalyzer(AllJetPSet, consumesCollector());
    theCHSJetAnalyzer      = new JetAnalyzer(CHSJetPSet, consumesCollector());
    theVBFJetAnalyzer      = new JetAnalyzer(VBFJetPSet, consumesCollector());
    theCHSFatJetAnalyzer   = new JetAnalyzer(CHSFatJetPSet, consumesCollector());
    //theCaloJetAnalyzer     = new CaloJetAnalyzer(CaloJetPSet, consumesCollector());
    theGenAnalyzer         = new GenAnalyzer(GenPSet, consumesCollector());
    thePileupAnalyzer      = new PileupAnalyzer(PileupPSet, consumesCollector());
    theTriggerAnalyzer     = new TriggerAnalyzer(TriggerPSet, consumesCollector());
    theElectronAnalyzer    = new ElectronAnalyzer(ElectronPSet, consumesCollector());
    theMuonAnalyzer        = new MuonAnalyzer(MuonPSet, consumesCollector());
    theTauAnalyzer         = new TauAnalyzer(TauPSet, consumesCollector());
    thePhotonAnalyzer      = new PhotonAnalyzer(PhotonPSet, consumesCollector());
    theVertexAnalyzer      = new VertexAnalyzer(VertexPSet, consumesCollector());
    thePFCandidateAnalyzer = new PFCandidateAnalyzer(PFCandidatePSet, consumesCollector());
    theROIAnalyzer         = new ROIAnalyzer(ROIPSet, consumesCollector());
    theV0Analyzer          = new V0Analyzer(V0PSet, consumesCollector());

    std::vector<std::string> TriggerList(TriggerPSet.getParameter<std::vector<std::string> >("paths"));
    for(unsigned int i = 0; i < TriggerList.size(); i++) TriggerMap[ TriggerList[i] ] = false;
    for(unsigned int i = 0; i < TriggerList.size(); i++) PrescalesTriggerMap[ TriggerList[i] ] = -1;
    std::vector<std::string> MetFiltersList(TriggerPSet.getParameter<std::vector<std::string> >("metpaths"));
    for(unsigned int i = 0; i < MetFiltersList.size(); i++) MetFiltersMap[ MetFiltersList[i] ] = false;
    //std::vector<std::string> L1FiltersList(TriggerPSet.getParameter<std::vector<std::string> >("l1filters"));//commented
    //for(unsigned int i = 0; i < L1FiltersList.size(); i++) L1FiltersMap[ L1FiltersList[i] ] = false;//commented

    if (isTracking && is2018) {
      // Initialize additional PileupAnalyzers for B-parking triggers
      PileupPSet = iConfig.getParameter<edm::ParameterSet>("pileupSet_HLT_Mu7_IP4");
      thePileupAnalyzer_HLT_Mu7_IP4   = new PileupAnalyzer(PileupPSet, consumesCollector());

      PileupPSet = iConfig.getParameter<edm::ParameterSet>("pileupSet_HLT_Mu9_IP6");
      thePileupAnalyzer_HLT_Mu9_IP6    = new PileupAnalyzer(PileupPSet, consumesCollector());

      PileupPSet = iConfig.getParameter<edm::ParameterSet>("pileupSet_HLT_Mu9_IP6_v6");
      thePileupAnalyzer_HLT_Mu9_IP6_v6 = new PileupAnalyzer(PileupPSet, consumesCollector());

      PileupPSet = iConfig.getParameter<edm::ParameterSet>("pileupSet_HLT_Mu12_IP6");
      thePileupAnalyzer_HLT_Mu12_IP6  = new PileupAnalyzer(PileupPSet, consumesCollector());

      // Set back to usual value
      PileupPSet = iConfig.getParameter<edm::ParameterSet>("pileupSet");
    }

    //Imperial College Tagger
    edm::InputTag JetTagWP0p01 = edm::InputTag("pfXTags:0p01:ntuple");
    JetTagWP0p01Token= consumes<reco::JetTagCollection>(JetTagWP0p01);

    edm::InputTag JetTagWP0p1 = edm::InputTag("pfXTags:0p1:ntuple");
    JetTagWP0p1Token= consumes<reco::JetTagCollection>(JetTagWP0p1);

    edm::InputTag JetTagWP1 = edm::InputTag("pfXTags:1:ntuple");
    JetTagWP1Token= consumes<reco::JetTagCollection>(JetTagWP1);

    edm::InputTag JetTagWP10 = edm::InputTag("pfXTags:10:ntuple");
    JetTagWP10Token= consumes<reco::JetTagCollection>(JetTagWP10);

    edm::InputTag JetTagWP100 = edm::InputTag("pfXTags:100:ntuple");
    JetTagWP100Token= consumes<reco::JetTagCollection>(JetTagWP100);

    edm::InputTag JetTagWP1000 = edm::InputTag("pfXTags:1000:ntuple");
    JetTagWP1000Token= consumes<reco::JetTagCollection>(JetTagWP1000);

    //split up signal samples
    edm::InputTag genLumi = edm::InputTag(std::string("generator"));
    genLumiHeaderToken_             = consumes <GenLumiInfoHeader,edm::InLumi> (genLumi);

    if(isVerbose) std::cout << "CONSTRUCTOR" << std::endl;
    //if(isVerbose) std::cout << "ONLY EVENTS WITH 4 GEN B QUARKS IN ACCEPTANCE" << std::endl;

    //now do what ever initialization is needed
    usesResource("TFileService");

    if(isVerbose) std::cout << "---------- STARTING ----------" << std::endl;

}


Ntuplizer::~Ntuplizer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
    if(isVerbose) std::cout << "---------- ENDING  ----------" << std::endl;

    delete AllJetAnalyzer;
    delete theCHSJetAnalyzer;
    delete theVBFJetAnalyzer;
    delete theCHSFatJetAnalyzer;
    //delete theCaloJetAnalyzer;
    delete theGenAnalyzer;
    delete thePileupAnalyzer;
    delete theTriggerAnalyzer;
    delete theElectronAnalyzer;
    delete theMuonAnalyzer;
    delete theTauAnalyzer;
    delete thePhotonAnalyzer;
    delete theVertexAnalyzer;
    delete thePFCandidateAnalyzer;
    delete theROIAnalyzer;
    delete theV0Analyzer;

}


//
// member functions
//

// ------------ method called for each event  ------------
void
Ntuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    //if(isVerbose) std::cout << "STARTING ANALYZE METHOD!" << std::endl;
    auto start = std::chrono::system_clock::now();//time!
    using namespace edm;
    //using namespace reco; // WARNING: Can't be used together with ROI variables! (Not needed anyways)
    using namespace std;

    // Initialize types
    ObjectsFormat::ResetMEtType(MEt);
    ////for(int i = 0; i < WriteNJets; i++) ObjectsFormat::ResetJetType(CHSJets[i]);
    ////    for(int i = 0; i < WriteNFatJets; i++) ObjectsFormat::ResetFatJetType(CHSFatJets[i]);
    //for(int i = 0; i < WriteNMatchedJets; i++) ObjectsFormat::ResetJetType(MatchedCHSJets[i]);
    ////for(int i = 0; i < WriteNMatchedJets; i++) ObjectsFormat::ResetCaloJetType(MatchedCaloJets[i]);
    ////for(int i = 0; i < WriteNGenBquarks; i++) ObjectsFormat::ResetGenPType(GenBquarks[i]);
    ////for(int i = 0; i < WriteNGenLongLiveds; i++) ObjectsFormat::ResetGenPType(GenLongLiveds[i]);
    //////for(int i = 0; i < WriteNLeptons; i++) ObjectsFormat::ResetLeptonType(Leptons[i]);
    ////for(int i = 0; i < WriteNLeptons; i++) ObjectsFormat::ResetLeptonType(Muons[i]);
    ////for(int i = 0; i < WriteNLeptons; i++) ObjectsFormat::ResetLeptonType(Electrons[i]);
    ////ObjectsFormat::ResetGenPType(GenHiggs);
    ObjectsFormat::ResetCandidateType(VBF);
    if (isControl){
      ObjectsFormat::ResetCandidateType(Z);
      ObjectsFormat::ResetCandidateType(W);
    }

    isMC = false;
    isVBF = isTriggerVBF = false;
    isggH = false;
    isTightMM = isTightEE = isTightE = isTightM = isTightEM = isLooseEM = false;
    isOppositeSignTightMM = isOppositeSignTightEE = false;
    isZtoMM = isZtoEE = isWtoMN = isWtoEN = isTtoEM = false;
    EventNumber = LumiNumber = RunNumber = nPV = 0;
    model_="NotSignal";
    AtLeastOneTrigger = AtLeastOneL1Filter = false;
    isIsoMu24_OR_IsoTkMu24 = isMu50_OR_TkMu50 = false;
    number_of_PV = number_of_SV = 0;//27 Sep: remember to properly initialize everything
    MeanNumInteractions = 0;
    nCHSJets = nLooseCHSJets = nTightCHSJets = 0;
    nVBFGenMatchedJets = 0;
    nAllBarrelJets = nAllJets = 0;
    nCHSFatJets = nLooseCHSFatJets = nTightCHSFatJets = nGenLL = nGenBquarks = nGenMuons = nPV = nSV = nROIs = 0;
    nMatchedCHSJets = nMatchedFatJets = 0;
    //nCaloJets = nMatchedCaloJets = nMatchedCaloJetsWithGenJets = 0;
    //nCaloTagJets = nLooseCaloTagJets = 0;
    nElectrons = nMuons = nTaus = nPhotons = 999;//We want to veto them for QCD control regions! Best offset is a large number!
    nTightElectrons = nTightMuons = 0;//This time we want a W, Z control region. Let's count them from zero
    nLooseElectrons = nLooseMuons = nTriggerMuons = 0;
    number_of_b_matched_to_CHSJets = 0;
    number_of_b_matched_to_FatJets = 0;
    number_of_VBFGen_matched_to_AllJets = 0;
    //number_of_b_matched_to_CaloJets = number_of_b_matched_to_CaloJetsWithGenJets = 0;
    GenEventWeight = EventWeight = PUWeight = PUWeightDown = PUWeightUp = LeptonWeight = ZewkWeight = WewkWeight = 1.;
    PUWeight_HLT_Mu7_IP4 = PUWeightUp_HLT_Mu7_IP4 = PUWeightDown_HLT_Mu7_IP4 = 1.;
    PUWeight_HLT_Mu9_IP6 = PUWeightUp_HLT_Mu9_IP6 = PUWeightDown_HLT_Mu9_IP6 = 1.;
    PUWeight_HLT_Mu12_IP6 = PUWeightUp_HLT_Mu12_IP6 = PUWeightDown_HLT_Mu12_IP6 = 1.;
    LeptonWeightUp = LeptonWeightDown = 1.;
    EventWeight_leptonSF = EventWeight_leptonSFUp = EventWeight_leptonSFDown = 1.;
    bTagWeight_central = bTagWeight_jesup = bTagWeight_jesdown = bTagWeight_lfup = bTagWeight_lfdown = bTagWeight_hfup = bTagWeight_hfdown = bTagWeight_hfstats1up = bTagWeight_hfstats1down = bTagWeight_hfstats2up = bTagWeight_hfstats2down = bTagWeight_lfstats1up = bTagWeight_lfstats1down = bTagWeight_lfstats2up = bTagWeight_lfstats2down = bTagWeight_cferr1up = bTagWeight_cferr1down = bTagWeight_cferr2up = bTagWeight_cferr2down = 1.0;
    HT = 0.;
    MinJetMetDPhi = MinJetMetDPhiAllJets = ggHJetMetDPhi = 10.;
    m_pi = 0.;
    gen_b_radius = -1.;
    Prefired = false;
    HDiCHS = HTriCHS = HQuadCHS = HDiCHSMatched = HTriCHSMatched = HQuadCHSMatched = 0;
    nPFCandidates = nPFCandidatesTrack = nPFCandidatesHighPurityTrack = nPFCandidatesFullTrackInfo = nPFCandidatesFullTrackInfo_pt = nPFCandidatesFullTrackInfo_hasTrackDetails = 0;
    //HDiCalo = HTriCalo = HQuadCalo = HDiCaloMatched = HTriCaloMatched = HQuadCaloMatched = 0;
    LeadingROI = SubleadingROI_dPhi2p0 = LeadingLLP = -1;
    LeadingROIScore = SubleadingROIScore_dPhi2p0 = -1.0;

    //Event info
    isMC = !iEvent.isRealData();
    EventNumber = iEvent.id().event();
    LumiNumber = iEvent.luminosityBlock();
    RunNumber = iEvent.id().run();

    //GenEventWeight
    GenEventWeight = theGenAnalyzer->GenEventWeight(iEvent);
    EventWeight *= GenEventWeight;

    //split up signal samples
    if(isCentralProd){
      edm::Handle<GenLumiInfoHeader> gen_header;
      iEvent.getLuminosityBlock().getByToken(genLumiHeaderToken_,gen_header);
      model_ = gen_header->configDescription();
    }

    if(PerformVBF and PerformggH) throw cms::Exception("Configuration") << "VBF and ggH selections can't be performed together! Please choose one option only!";

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Trigger and MET filters
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    // Trigger and MET filters
    if(isVerbose) std::cout << "Trigger and met filters" << std::endl;
    theTriggerAnalyzer->FillTriggerMap(iEvent, TriggerMap, PrescalesTriggerMap, isVerboseTrigger);
    theTriggerAnalyzer->FillMetFiltersMap(iEvent, MetFiltersMap);
    BadPFMuonFlag = theTriggerAnalyzer->GetBadPFMuonFlag(iEvent);
    BadChCandFlag = theTriggerAnalyzer->GetBadChCandFlag(iEvent);
    ECALCalibFlag = theTriggerAnalyzer->GetECALCalibFlag(iEvent);

    //theTriggerAnalyzer->FillL1FiltersMap(iEvent, L1FiltersMap);//commented; filters are treated differently in 2016 w.r.t. 2017/2018

    // 27 Sep 2018: saving only events that fired at least one trigger, to reduce output size
    for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++)
      {
	if(it->second)
	  {
	    ////std::cout << "Trigger fired!!! " << it->first << std::endl;
	    AtLeastOneTrigger = true;
	  }
	//if(AtLeastOneTrigger) break;// no need to go through everything; once one trigger is fired, event can be saved
	if (it->first == "HLT_IsoMu24_v" || it->first == "HLT_IsoTkMu24_v"){
	  isIsoMu24_OR_IsoTkMu24 = true;
	}
	if (it->first == "HLT_Mu50_v" || it->first == "HLT_TkMu50_v"){
	  isMu50_OR_TkMu50 = true;
	}
      }

    ////if(!AtLeastOneTrigger && WriteOnlyTriggerEvents) std::cout << "This event can be rejected" << std::endl;
    if(!AtLeastOneTrigger && WriteOnlyTriggerEvents) return;

    // 10 Dec 2018: saving only events that fired at least one L1 seed
    // 11 Feb 2020: commented, filters treated differently in 2016 w.r.t. 2017-2018
    //for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++)
    //{
    //if(it->second)
    //{
    //AtLeastOneL1Filter = true;
    //}
    //}

    if(!AtLeastOneL1Filter && WriteOnlyL1FilterEvents) return;

    //Trigger-dependent standalone objects
    //They will be used for trigger matching
    //std::string VBF_DisplacedJet40_VTightID_Hadronic_string;
    //VBF_DisplacedJet40_VTightID_Hadronic_string = "VBF_DisplacedJet40_VTightID_Hadronic_v";
    //std::vector<pat::TriggerObjectStandAlone> VBF_DisplacedJet40_VTightID_Hadronic_Vec  = theTriggerAnalyzer->FillTriggerObjectVector(iEvent,VBF_DisplacedJet40_VTightID_Hadronic_string);
    //std::vector<pat::TriggerObjectStandAlone> PotentialTriggerVBFPairJets;
    //std::vector<pat::TriggerObjectStandAlone> PotentialTriggerDisplacedJets;
    //Match trigger standalone objects to the filter they fired;
    //this allows to distinguish objects that fired VBF part from Displaced part
    //for(unsigned int r = 0; r<VBF_DisplacedJet40_VTightID_Hadronic_Vec.size(); r++)
    //{
    //for (unsigned h = 0; h < VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds().size(); ++h)
    ////loop over filter Ids
      //{
    //if( (VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds()[h])==85 or (VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterIds()[h])==86)
    // //objects with filterIds 85 or 86 are jets or b-jets; see our LongLived twiki
    //{
    //for (unsigned l = 0; l < VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels().size(); ++l)
    ////loop over filter labels
    //{
    //if(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltVBFFilterDisplacedJets" or VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltVBFFilterDisplacedJetsTight" )
    ////objects that fired VBF filter are potential VBF jet pair candidates
      ////still need to check VBF conditions over mjj and dEta
    //{
    //PotentialTriggerVBFPairJets.push_back(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r));
    //}
    //else if(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r).filterLabels()[l]=="hltCentralHadronCaloJetpt40VTightID")
    ////objects that fired displaced filter are potential displaced jet candidates
    //{
    //PotentialTriggerDisplacedJets.push_back(VBF_DisplacedJet40_VTightID_Hadronic_Vec.at(r));
    //}
    //}
    //}
    //}
    //}


    //Pre-firing
    if(PerformPreFiringStudies)
      {
	Prefired = theTriggerAnalyzer->EvaluatePrefiring(iEvent);
      }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Gen particles
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "Gen Particles" << std::endl;

    GenVBFquarks.clear();
    GenHiggs.clear();
    GenLLPs.clear();
    GenBquarks.clear();
    GenMuons.clear();

    std::vector<reco::GenParticle> GenVBFVect = theGenAnalyzer->FillVBFGenVector(iEvent);
    std::vector<reco::GenParticle> GenHiggsVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idHiggs,statusHiggs);
    std::vector<reco::GenParticle> GenLongLivedVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idLLP,statusLLP);
    std::vector<reco::GenParticle> GenBquarksVect;

    if(nGenLL>0)
      {
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdStatusAndMotherAndKin(iEvent,5,23,idMotherB,float(MinGenBpt),float(MaxGenBeta));
      }
    else
      {
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdAndStatusAndKin(iEvent,5,23,float(MinGenBpt),float(MaxGenBeta));
      }

    std::vector<reco::GenParticle> GenMuonsVect = theGenAnalyzer->FillGenVectorByIdAndAncestor(iEvent,13,idLLP);

    nGenLL = GenLongLivedVect.size();
    nGenBquarks = GenBquarksVect.size();
    nGenMuons = GenMuonsVect.size();

    for(unsigned int i = 0; i < GenVBFVect.size(); i++) GenVBFquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenHiggsVect.size(); i++) GenHiggs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) GenLLPs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenBquarksVect.size(); i++) GenBquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenMuonsVect.size(); i++) GenMuons.push_back( GenPType() );

    if(nGenBquarks>0) gen_b_radius = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2) + pow(GenBquarksVect.at(0).vz() - GenBquarksVect.at(0).mother()->vz(),2)) : -1.;
    if(nGenLL>0) m_pi = GenLongLivedVect.at(0).mass();

    ///////////////////////
    //// This is used to skip signal events with less than 4 b quarks in acceptance; can be used for signal-only studies
    ///////////////////////
    //if(nGenBquarks<4)
    //{
	//GenBquarksVect.clear();
	//GenLongLivedVect.clear();
	//return; //First step: only full reconstruction!
    //}

    // EWK corrections
    if(isVerbose) std::cout << "EWK corrections" << std::endl;

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

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Pu weight and number of vertices
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "Pile-up" << std::endl;
    PUWeight     = thePileupAnalyzer->GetPUWeight(iEvent);//calculates pileup weights
    PUWeightUp   = thePileupAnalyzer->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
    PUWeightDown = thePileupAnalyzer->GetPUWeightDown(iEvent);//syst uncertainties due to pileup

    nPV = thePileupAnalyzer->GetPV(iEvent);//calculates number of vertices
    MeanNumInteractions = thePileupAnalyzer->GetMeanNumInteractions(iEvent);

    EventWeight *= PUWeight;

    // Additional PU weights for B-parking triggers
    if (isTracking && is2018) {
      // PUWeight_HLT_Mu7_IP4      = thePileupAnalyzer_HLT_Mu7_IP4->GetPUWeight(iEvent);//calculates pileup weights
      // PUWeightUp_HLT_Mu7_IP4    = thePileupAnalyzer_HLT_Mu7_IP4->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
      // PUWeightDown_HLT_Mu7_IP4  = thePileupAnalyzer_HLT_Mu7_IP4->GetPUWeightDown(iEvent);//syst uncertainties due to pileup

      PUWeight_HLT_Mu9_IP6        = thePileupAnalyzer_HLT_Mu9_IP6->GetPUWeight(iEvent);//calculates pileup weights
      PUWeightUp_HLT_Mu9_IP6      = thePileupAnalyzer_HLT_Mu9_IP6->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
      PUWeightDown_HLT_Mu9_IP6    = thePileupAnalyzer_HLT_Mu9_IP6->GetPUWeightDown(iEvent);//syst uncertainties due to pileup

      PUWeight_HLT_Mu9_IP6_v6     = thePileupAnalyzer_HLT_Mu9_IP6_v6->GetPUWeight(iEvent);//calculates pileup weights
      PUWeightUp_HLT_Mu9_IP6_v6   = thePileupAnalyzer_HLT_Mu9_IP6_v6->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
      PUWeightDown_HLT_Mu9_IP6_v6 = thePileupAnalyzer_HLT_Mu9_IP6_v6->GetPUWeightDown(iEvent);//syst uncertainties due to pileup

      // PUWeight_HLT_Mu12_IP6     = thePileupAnalyzer_HLT_Mu12_IP6->GetPUWeight(iEvent);//calculates pileup weights
      // PUWeightUp_HLT_Mu12_IP6   = thePileupAnalyzer_HLT_Mu12_IP6->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
      // PUWeightDown_HLT_Mu12_IP6 = thePileupAnalyzer_HLT_Mu12_IP6->GetPUWeightDown(iEvent);//syst uncertainties due to pileup
    }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Missing Energy
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "MET" << std::endl;
    pat::MET MET = theCHSJetAnalyzer->FillMetVector(iEvent);
    pat::MET Neutrino(MET);

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // HT
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "HT" << std::endl;
    HT = theCHSJetAnalyzer->CalculateHT(iEvent,iSetup,3,15,3.);

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Electrons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "Electrons" << std::endl;
    std::vector<pat::Electron> ElecVect = theElectronAnalyzer->FillElectronVector(iEvent);
    std::vector<pat::Electron> TightElecVect;
    std::vector<pat::Electron> LooseElecVect;
    Electrons.clear();
    if (isTracking) LooseElectrons.clear();

    for(unsigned int a = 0; a<ElecVect.size(); a++) {
      if(ElecVect.at(a).pt() > 15.0 && ElecVect.at(a).hasUserInt("isTight") && ElecVect.at(a).userInt("isTight")>0) {
        TightElecVect.push_back(ElecVect.at(a));
        nTightElectrons++;
  	  }
      else if(ElecVect.at(a).hasUserInt("isLoose") && ElecVect.at(a).userInt("isLoose")>0) {
        LooseElecVect.push_back(ElecVect.at(a));
        nLooseElectrons++;
  	  }
    }
    nElectrons = ElecVect.size();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Muons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "Muons" << std::endl;
    std::vector<pat::Muon> MuonVect = theMuonAnalyzer->FillMuonVector(iEvent);
    std::vector<pat::Muon> TightMuonVect;
    std::vector<pat::Muon> LooseMuonVect; // Only used for tracking lifetimes
    std::vector<pat::Muon> TriggerMuonVect; // Only used for tracking lifetimes
    Muons.clear(); // Tight muons for short lifetimes, trigger muons for tracking
    if (isTracking) {
      TightMuons.clear();
      LooseMuons.clear();
    }

    if (isTracking) { // Tracking lifetimes
      for(unsigned int a = 0; a<MuonVect.size(); a++) {

        // All muons: Gen-matching to muons from LLP decay
        if(MuonVect.at(a).genLepton() != nullptr) {
          for (unsigned int thisGenMu = 0; thisGenMu < GenMuonsVect.size(); thisGenMu++) {
            if ( (*MuonVect.at(a).genLepton()).pt() == GenMuonsVect.at(thisGenMu).pt() ) {
              MuonVect.at(a).addUserInt("isGenMatched",1);
              MuonVect.at(a).addUserInt("MatchedGenMuonIndex",thisGenMu);
            }
          }
        }

        // Trigger muons: All requirements as in muonPSet (For v6: loose ID, no isolation, pT > 0.1 GeV, |eta| < 2.4)
        if (MuonVect.at(a).hasUserInt("triggered_HLT_Mu9_IP6") && MuonVect.at(a).userInt("triggered_HLT_Mu9_IP6")>0) {
            TriggerMuonVect.push_back(MuonVect.at(a));
            nTriggerMuons++;
        }

        else {
          // Tight (and did not fire trigger path)
          if(MuonVect.at(a).pt() > 15.0 &&
             MuonVect.at(a).hasUserInt("isTight") && MuonVect.at(a).userInt("isTight") > 0 &&
             MuonVect.at(a).hasUserFloat("pfIso04") && MuonVect.at(a).userFloat("pfIso04") < 0.15 ) { //tight iso for muons
            TightMuonVect.push_back(MuonVect.at(a));
            nTightMuons++;
          }

          // Loose (and did not fire trigger path)
          else if (MuonVect.at(a).pt() > 10.0 &&
                   MuonVect.at(a).hasUserInt("isLoose") && MuonVect.at(a).userInt("isLoose") > 0 &&
                   MuonVect.at(a).hasUserFloat("pfIso04") && MuonVect.at(a).userFloat("pfIso04") < 0.25 ) {
            LooseMuonVect.push_back(MuonVect.at(a));
            nLooseMuons++;
          }
        }
      } // End of loop over muons
    } // Tracking

    else { // Short and calo lifetimes
      for(unsigned int a = 0; a<MuonVect.size(); a++) {
        if(MuonVect.at(a).hasUserInt("isTight") && MuonVect.at(a).userInt("isTight")>0 && MuonVect.at(a).hasUserFloat("pfIso04") && MuonVect.at(a).userFloat("pfIso04")<0.15) { //tight iso for muons
          TightMuonVect.push_back(MuonVect.at(a));
          nTightMuons++;
        }
      }
    }

    nMuons = MuonVect.size();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Taus
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "Taus" << std::endl;
    std::vector<pat::Tau> TauVect = theTauAnalyzer->FillTauVector(iEvent);
    theTauAnalyzer->CleanTausFromMuons(TauVect, MuonVect, 0.4);
    theTauAnalyzer->CleanTausFromElectrons(TauVect, ElecVect, 0.4);
    nTaus = TauVect.size();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Photons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if(isVerbose) std::cout << "Photons" << std::endl;
    std::vector<pat::Photon> PhotonVect = thePhotonAnalyzer->FillPhotonVector(iEvent);
    nPhotons = PhotonVect.size();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Preselections
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(EventNumber!=44169) return;
    if(HT<MinHT) return;//Avoid events with low HT//WAIT!!
    if(isCalo && MET.pt()<120) return;//Avoid events with very low MET for calo analysis
    if(isCalo && nMuons>0) return;//Veto leptons and photons!
    if(isCalo && nTaus>0) return;//Veto leptons and photons!
    if(isCalo && nElectrons>0) return;//Veto leptons and photons!
    if(isCalo && nPhotons>0) return;//Veto leptons and photons!

    if(isShort && !isControl){
      if (nMuons>0) return;//Veto leptons and photons!
      if( nTaus>0) return;//Veto leptons and photons!
      if(nElectrons>0) return;//Veto leptons and photons!
      if(nPhotons>0) return;//Veto leptons and photons!
    }
    if(isShort && isControl){
      //if(nTightMuons!=1 || nTightElectrons!=1) return; //Control region for short lifetimes
      if(nTightMuons<1 && nTightElectrons<1) return; //Control region for short lifetimes
      //      if(nTaus<1) return;//Veto taus!
      //      if(nPhotons<1) return;//Veto photons!
    }

    if(isTracking) {
      if (isControl) {
        // if (nTightMuons < 1 && nTightElectrons < 1) return;
        if (nTightMuons < 1 && nTightElectrons < 1 && !(nLooseMuons == 1 && nLooseElectrons == 1)) return;
      }
      else {
        if (nTightMuons > 0) return; // Potentially tighten preselection to nTightMuons + nLooseMuons > 0
        if (nTightElectrons > 0) return;
      }
    }


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Z and W candidates, control region
    // Please do not remove!
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "Count leptons for Z and W" << std::endl;
    pat::CompositeCandidate theZ;
    pat::CompositeCandidate theW;

    if ( (isShort || isTracking) && isControl) {
      float LeptonWeightUnc;
      // float LeptonWeightUp = 1.; // Defined in Ntuplizer.h and default value set above
      // float LeptonWeightDown = 1.; // Defined in Ntuplizer.h and default value set above

      //// ---------- Z TO LEPTONS ----------
      if(TightMuonVect.size()>=2 || TightElecVect.size()>=2) {
        if(TightMuonVect.size()>=2 && TightElecVect.size()>=2) {
        	if(TightMuonVect.at(0).pt() > TightElecVect.at(0).pt()) isTightMM=true;
        	else isTightEE=true;
        }
        else if(TightMuonVect.size()>=2) isTightMM=true;
        else if(TightElecVect.size()>=2) isTightEE=true;
      }

      ////    ---------- W TO LEPTON and NEUTRINO ----------
      else if(TightMuonVect.size()==1 || TightElecVect.size()==1) {
        if(TightMuonVect.size()==1 && TightElecVect.size()==1) isTightEM = true;
        else if(TightElecVect.size()==1) isTightE=true;
        else if(TightMuonVect.size()==1) isTightM=true;
      }

      else if(LooseMuonVect.size()==1 && LooseElecVect.size()==1) isLooseEM = true;

      if(isTightMM) {
        if(isVerbose) std::cout << "Do the Z->mu mu" << std::endl;
        int m1(-1), m2(-1);
        for(unsigned int i = 0; i < TightMuonVect.size(); i++) {
        	for(unsigned int j = i+1; j < TightMuonVect.size(); j++) {
        	  if(TightMuonVect[i].charge() == TightMuonVect[j].charge())
        	    {
        	      // isZtoMM = false;
        	      continue;
        	    }
        	  float Zmass = (TightMuonVect[i].p4() + TightMuonVect[j].p4()).mass();
            // Not needed: Find muon pair with invariant mass inside Z mass window
        	  // if(Zmass > 50. && Zmass < 130.)
        	  //   {
        	  //     m1 = i;
        	  //     m2 = j;
            //     isOppositeSignTightMM = isZtoMM = true;
        	  //   }

            // Instead: Reject events where any electron pair has invariant mass inside Z mass window
            if (TMath::Abs(Zmass - 91.1876) < 20.) return;
        	}
        }

        // For CR events (outside Z window), take leading two muons
        if (!isZtoMM) {
          m1 = 0;
          m2 = 1;
          if (TightMuonVect.at(m1).charge() != TightMuonVect.at(m2).charge()) isOppositeSignTightMM = true;
        }

        // Build candidate
        if(m1 >= 0 && m2 >= 0) {
          theZ.addDaughter(TightMuonVect.at(m1).charge() < 0 ? TightMuonVect.at(m1) : TightMuonVect.at(m2));
          theZ.addDaughter(TightMuonVect.at(m1).charge() < 0 ? TightMuonVect.at(m2) : TightMuonVect.at(m1));
          addP4.set(theZ);
          isZtoMM = true;

        	//SF
        	if(isMC && !is2016) {
        	  LeptonWeightUnc = 0.;
            LeptonWeightUp = 1.;
            LeptonWeightDown = 1.;
        	  /// FIXED -> APPLYING THE SF FOR IsoMu24 NOT ANYLONGER HADRCODED <- FIXED ///
            if (isIsoMu24_OR_IsoTkMu24) {
              if (TightMuonVect.at(m1).pt() > TightMuonVect.at(m2).pt() ) {
                LeptonWeight     *= theMuonAnalyzer->GetMuonTriggerSFIsoMu24(TightMuonVect.at(m1));
                LeptonWeightUnc  += pow(theMuonAnalyzer->GetMuonTriggerSFErrorIsoMu24(MuonVect.at(m1)),2);
              }
              else {
                LeptonWeight     *= theMuonAnalyzer->GetMuonTriggerSFIsoMu24(TightMuonVect.at(m2));
                LeptonWeightUnc  += pow(theMuonAnalyzer->GetMuonTriggerSFErrorIsoMu24(MuonVect.at(m2)),2);
              }
            }// IsoMu24 trigger
            if (isMu50_OR_TkMu50) {
              if (TightMuonVect.at(m1).pt() > TightMuonVect.at(m2).pt() ) {
                LeptonWeight     *= theMuonAnalyzer->GetMuonTriggerSFMu50(TightMuonVect.at(m1));
                LeptonWeightUnc  += pow(theMuonAnalyzer->GetMuonTriggerSFErrorMu50(MuonVect.at(m1)),2);
              }
              else {
                LeptonWeight     *= theMuonAnalyzer->GetMuonTriggerSFMu50(TightMuonVect.at(m2));
                LeptonWeightUnc  += pow(theMuonAnalyzer->GetMuonTriggerSFErrorMu50(MuonVect.at(m2)),2);
              }
            }// IsoMu50 trigger

            // //removed obsolete things for now
            // LeptonWeight *= theMuonAnalyzer->GetMuonTrkSF(TightMuonVect.at(m1));
            // LeptonWeight *= theMuonAnalyzer->GetMuonTrkSF(TightMuonVect.at(m2));
        	  // //LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonTrkSFError(MuonVect.at(m1))      ,2);
        	  // //LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonTrkSFError(MuonVect.at(m2))      ,2);

        	  LeptonWeight *= theMuonAnalyzer->GetMuonIdSF(TightMuonVect.at(m1), 3);
         	  LeptonWeight *= theMuonAnalyzer->GetMuonIdSF(TightMuonVect.at(m2), 3);
         	  LeptonWeight *= theMuonAnalyzer->GetMuonIsoSF(TightMuonVect.at(m1), 3);
         	  LeptonWeight *= theMuonAnalyzer->GetMuonIsoSF(TightMuonVect.at(m2), 3);

        	  LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIdSFError(TightMuonVect.at(m1), 3)    ,2);
         	  LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIdSFError(TightMuonVect.at(m2), 3)    ,2);
         	  LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIsoSFError(TightMuonVect.at(m1), 3)   ,2);
         	  LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIsoSFError(TightMuonVect.at(m2), 3)   ,2);

        	  LeptonWeightUp   = LeptonWeight+sqrt(LeptonWeightUnc);
    	      LeptonWeightDown = LeptonWeight-sqrt(LeptonWeightUnc);
        	}
        }
      } // isTightMM

      else if(isTightEE) {
        if(isVerbose) std::cout << "Do the Z->e e" << std::endl;
        int e1(-1), e2(-1);
        for(unsigned int i = 0; i < TightElecVect.size(); i++) {
          for(unsigned int j = i+1; j < TightElecVect.size(); j++) {
            if(TightElecVect[i].charge() == TightElecVect[j].charge()) {
              // isZtoEE = false;
      	      continue;
      	    }
            float Zmass = (TightElecVect[i].p4() + TightElecVect[j].p4()).mass();
            // Not needed: Find electron pair with invariant mass inside Z mass window
            // if(Zmass > 50. && Zmass < 130.) {
            //   e1 = i;
            //   e2 = j;
            //   isOppositeSignTightEE = isZtoEE = true;
            // }

            // Instead: Reject events where any electron pair has invariant mass inside Z mass window
            if (TMath::Abs(Zmass - 91.1876) < 20.) return;
          }
        }

        // For CR events (outside Z window), take leading two electrons
        if (!isZtoEE) {
          e1 = 0;
          e2 = 1;
          if (TightElecVect.at(e1).charge() != TightElecVect.at(e2).charge()) isOppositeSignTightEE = true;
        }

        // Build candidate
        if(e1 >= 0 && e2 >= 0) {
        	theZ.addDaughter(TightElecVect.at(e1).charge() < 0 ? TightElecVect.at(e1) : TightElecVect.at(e2));
        	theZ.addDaughter(TightElecVect.at(e1).charge() < 0 ? TightElecVect.at(e2) : TightElecVect.at(e1));
        	addP4.set(theZ);
        	isZtoEE = true;

        	// SF
        	if(isMC && !is2016) {
            LeptonWeightUnc = 0.;
            LeptonWeightUp = 1.;
            LeptonWeightDown = 1.;
        	  /// FIXME -> APPLYING THE SF FOR Ele27Tight HADRCODED <- FIXME ///
        	  // if (TightElecVect.at(e1).pt() > TightElecVect.at(e2).pt() ){
        	  //   LeptonWeight     *= theElectronAnalyzer->GetElectronTriggerSFEle27Tight(TightElecVect.at(e1));
        	  //   //LeptonWeightUnc  += pow(theElectronAnalyzer->GetElectronTriggerSFErrorEle27Tight(ElecVect.at(e1)),2);
        	  // }
        	  // else{
        	  //   LeptonWeight     *= theElectronAnalyzer->GetElectronTriggerSFEle27Tight(TightElecVect.at(e2));
        	  //   //LeptonWeightUnc  += pow(theElectronAnalyzer->GetElectronTriggerSFErrorEle27Tight(ElecVect.at(e2)),2);
        	  // }
        	  LeptonWeight    *= theElectronAnalyzer->GetElectronRecoEffSF(TightElecVect.at(e1));
         	  LeptonWeight    *= theElectronAnalyzer->GetElectronRecoEffSF(TightElecVect.at(e2));
         	  LeptonWeight    *= theElectronAnalyzer->GetElectronIdSF(TightElecVect.at(e1), 3);
         	  LeptonWeight    *= theElectronAnalyzer->GetElectronIdSF(TightElecVect.at(e2), 3);

        	  LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronRecoEffSFError(TightElecVect.at(e1))   ,2);
         	  LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronRecoEffSFError(TightElecVect.at(e2))   ,2);
         	  LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronIdSFError(TightElecVect.at(e1), 3)     ,2);
         	  LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronIdSFError(TightElecVect.at(e2), 3)     ,2);

        	  LeptonWeightUp   = LeptonWeight+sqrt(LeptonWeightUnc);
            LeptonWeightDown = LeptonWeight-sqrt(LeptonWeightUnc);
        	}
        }
      } // isTightEE

      else if(isTightM) {
        if(isVerbose) std::cout << "Do the W->mu nu" << std::endl;

        //// W kinematic reconstruction
        // float pz = Utilities::RecoverNeutrinoPz(&TightMuonVect.at(0).p4(), &MET.p4());
        // Neutrino.setP4(reco::Particle::LorentzVector(MET.px(), MET.py(), pz, sqrt(MET.pt()*MET.pt() + pz*pz) ));
        theW.addDaughter(TightMuonVect.at(0));
        theW.addDaughter(MET);
        addP4.set(theW);
        isWtoMN = true;

        // Debugging:
        // std::cout << "E  = " << MET.energy() << " + " << TightMuonVect.at(0).energy() << " = " << theW.energy()  << std::endl;
        // std::cout << "px = " << MET.px()     << " + " << TightMuonVect.at(0).px()     << " = " << theW.px()      << std::endl;
        // std::cout << "py = " << MET.py()     << " + " << TightMuonVect.at(0).py()     << " = " << theW.py()      << std::endl;
        // std::cout << "pz = " << MET.pz()     << " + " << TightMuonVect.at(0).pz()     << " = " << theW.pz()      << std::endl;
        // std::cout << "m  = " << theW.mass()       << std::endl;
        // std::cout << "mT = " << theW.mt()         << " =? " << TMath::Sqrt(theW.mass()*theW.mass() + theW.pt()*theW.pt()) << std::endl;
        // std::cout << "mT'= " << TMath::Sqrt(2.*Neutrino.pt()*TightMuonVect.at(0).pt()*(1.-TMath::Cos(reco::deltaPhi(Neutrino.phi(),TightMuonVect.at(0).phi())))) << std::endl;

        double mt = TMath::Sqrt(2. * MET.pt() * TightMuonVect.at(0).pt() * (1.-TMath::Cos(reco::deltaPhi(MET,TightMuonVect.at(0)))) );

        if (mt < 100. && isControl){
          // isWtoMN = true;
          return;
        }

        theW.addUserInt("isW", true);
        theW.addUserFloat("mt", mt);

        // SF
        if(isMC && !is2016) {
          // if(isVerbose) std::cout << "Muon ID SF" << std::endl;

          LeptonWeightUnc = 0.;
          LeptonWeightUp = 1.;
          LeptonWeightDown = 1.;
          // LeptonWeight    *= theMuonAnalyzer->GetMuonTriggerSFIsoMu24(TightMuonVect.at(0));
          // LeptonWeight    *= theMuonAnalyzer->GetMuonTrkSF(TightMuonVect.at(0));
          LeptonWeight    *= theMuonAnalyzer->GetMuonIdSF(TightMuonVect.at(0), 3);
          // if(isVerbose) std::cout << "Muon Iso SF" << std::endl;
          LeptonWeight    *= theMuonAnalyzer->GetMuonIsoSF(TightMuonVect.at(0), 3);

          // if(isVerbose) std::cout << "Muon SF Errors" << std::endl;
          // LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonTriggerSFErrorMu50(TightMuonVect.at(0)),2);
          // LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonTrkSFError(TightMuonVect.at(0))        ,2);
          LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIdSFError(TightMuonVect.at(0), 3)      ,2);
          LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIsoSFError(TightMuonVect.at(0), 3)     ,2);

          LeptonWeightUp   = LeptonWeight+sqrt(LeptonWeightUnc);
          LeptonWeightDown = LeptonWeight-sqrt(LeptonWeightUnc);
        }
      }

      else if(isTightE) {
        if(isVerbose) std::cout << "Do the W->e nu" << std::endl;

        // W kinematic reconstruction
        // float pz = Utilities::RecoverNeutrinoPz(&TightElecVect.at(0).p4(), &MET.p4());
        // Neutrino.setP4(reco::Particle::LorentzVector(MET.px(), MET.py(), pz, sqrt(MET.pt()*MET.pt() + pz*pz) ));
        theW.addDaughter(TightElecVect.at(0));
        theW.addDaughter(MET);
        addP4.set(theW);
        isWtoEN = true;

        double mt = TMath::Sqrt(2. * MET.pt() * TightElecVect.at(0).pt() * (1.-TMath::Cos(reco::deltaPhi(MET,TightElecVect.at(0)))) );

        if (mt < 100. && isControl){
          // isWtoEN = true;
          return;
        }

        theW.addUserInt("isW", true);
        theW.addUserFloat("mt", mt);

        if(isMC && !is2016) {
          // if(isVerbose) std::cout << "Electron SF" << std::endl;

          LeptonWeightUnc = 0.;
          LeptonWeightUp = 1.;
          LeptonWeightDown = 1.;
          // LeptonWeight    *= theElectronAnalyzer->GetElectronTriggerSFEle27Tight(TightElecVect.at(0));
          LeptonWeight    *= theElectronAnalyzer->GetElectronRecoEffSF(TightElecVect.at(0));
          LeptonWeight    *= theElectronAnalyzer->GetElectronIdSF(TightElecVect.at(0), 3);

          // if(isVerbose) std::cout << "Electron SF Error" << std::endl;
          LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronRecoEffSFError(TightElecVect.at(0))   ,2);
          LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronIdSFError(TightElecVect.at(0), 3)     ,2);

          LeptonWeightUp   = LeptonWeight+sqrt(LeptonWeightUnc);
          LeptonWeightDown = LeptonWeight-sqrt(LeptonWeightUnc);
        }
      }

      else if(isTightEM) {
        // Top event if opposite-sign EM pair. Not attempting to reconstruct candidate
        if(TightElecVect.at(0).charge() != TightMuonVect.at(0).charge()) isTtoEM = true;
        //std::cout << "isTtoEM, muon 1 pt: " << TightMuonVect.at(0).pt() << std::endl;

    	  if(isMC && !is2016) {

          LeptonWeightUnc = 0.;
          LeptonWeightUp = 1.;
          LeptonWeightDown = 1.;

    	    //Trigger is non trivial; we need non-isolated triggers!
    	    //if (TightElecVect.at(e).pt() > TightMuonVect.at(m).pt() ){
    	    //LeptonWeight     *= theElectronAnalyzer->GetElectronTriggerSFEle27Tight(TightElecVect.at(e1));
    	    //  //LeptonWeightUnc  += pow(theElectronAnalyzer->GetElectronTriggerSFErrorEle27Tight(ElecVect.at(e1)),2);
    	    //}
    	    //else{
    	    //  LeptonWeight     *= theElectronAnalyzer->GetElectronTriggerSFEle27Tight(TightElecVect.at(e2));
    	    //  //LeptonWeightUnc  += pow(theElectronAnalyzer->GetElectronTriggerSFErrorEle27Tight(ElecVect.at(e2)),2);
    	    //  }
          LeptonWeight    *= theMuonAnalyzer->GetMuonIdSF(TightMuonVect.at(0), 3);
          LeptonWeight    *= theMuonAnalyzer->GetMuonIsoSF(TightMuonVect.at(0), 3);
    	    LeptonWeight    *= theElectronAnalyzer->GetElectronRecoEffSF(TightElecVect.at(0));
    	    LeptonWeight    *= theElectronAnalyzer->GetElectronIdSF(TightElecVect.at(0), 3);

          LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIdSFError(TightMuonVect.at(0), 3)      ,2);
          LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIsoSFError(TightMuonVect.at(0), 3)     ,2);
          LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronRecoEffSFError(TightElecVect.at(0))   ,2);
          LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronIdSFError(TightElecVect.at(0), 3)     ,2);

          LeptonWeightUp   = LeptonWeight+sqrt(LeptonWeightUnc);
          LeptonWeightDown = LeptonWeight-sqrt(LeptonWeightUnc);
      	}
      }

      else if(isLooseEM) {
        // Top event if opposite-sign EM pair. Not attempting to reconstruct candidate
        if(LooseElecVect.at(0).charge() != LooseMuonVect.at(0).charge()) isTtoEM = true;

    	  if(isMC && !is2016) {
          LeptonWeightUnc = 0.;
          LeptonWeightUp = 1.;
          LeptonWeightDown = 1.;

          LeptonWeight    *= theMuonAnalyzer->GetMuonIdSF(LooseMuonVect.at(0), 1); // Loose ID
          LeptonWeight    *= theMuonAnalyzer->GetMuonIsoSF(LooseMuonVect.at(0), 1); // Loose iso
    	    LeptonWeight    *= theElectronAnalyzer->GetElectronRecoEffSF(LooseElecVect.at(0));
    	    LeptonWeight    *= theElectronAnalyzer->GetElectronIdSF(LooseElecVect.at(0), 1); // Loose ID

          LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIdSFError(LooseMuonVect.at(0), 1)      ,2); // Loose ID
          LeptonWeightUnc += pow(theMuonAnalyzer->GetMuonIsoSFError(LooseMuonVect.at(0), 1)     ,2); // Loose iso
          LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronRecoEffSFError(LooseElecVect.at(0))   ,2);
          LeptonWeightUnc += pow(theElectronAnalyzer->GetElectronIdSFError(LooseElecVect.at(0), 1)     ,2); // Loose ID

          LeptonWeightUp   = LeptonWeight+sqrt(LeptonWeightUnc);
          LeptonWeightDown = LeptonWeight-sqrt(LeptonWeightUnc);
      	}
      }

      // Used for short lifetimes?
      EventWeight_leptonSF = EventWeight * LeptonWeight;
      EventWeight_leptonSFUp = EventWeight * LeptonWeightUp;
      EventWeight_leptonSFDown = EventWeight * LeptonWeightDown;

      // For tracking lifetimes, include in EventWeight to be consistent with all other weights
      if (isTracking) EventWeight *= LeptonWeight;

    } // isControl

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // All Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //Used to understand VBF jets features;

    std::vector<pat::Jet> AllJetsVect = AllJetAnalyzer->FillJetVector(iEvent,iSetup);//
    nAllJets = AllJetsVect.size();

    std::vector<pat::Jet> VBFGenMatchedJetsVect;

    int VBF_matching_index_AllJets;//local variable
    float VBF_delta_R_AllJets;//local variable
    float VBF_current_delta_R_AllJets;//local variable
    for(unsigned int b = 0; b<GenVBFVect.size(); b++)
      {
	VBF_delta_R_AllJets = 1000.;
	VBF_current_delta_R_AllJets = 1000.;
	VBF_matching_index_AllJets = -1;
	for(unsigned int a = 0; a<AllJetsVect.size(); a++)
	  {
	    VBF_current_delta_R_AllJets = fabs(reco::deltaR(AllJetsVect[a].eta(),AllJetsVect[a].phi(),GenVBFVect[b].eta(),GenVBFVect[b].phi()));
	    //if(VBF_current_delta_R_AllJets<0.4 && VBF_current_delta_R_AllJets<delta_R_AllJets && AllJetsVect[a].genParton() && (fabs(AllJetsVect[a].hadronFlavour())==5 || fabs(AllJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(AllJetsVect[a].genParton()) )==idMotherB)//removed gen parton 5
	    if(VBF_current_delta_R_AllJets<0.4 && VBF_current_delta_R_AllJets<VBF_delta_R_AllJets)
	      //this implements all the reasonable possibilities!
	      {
	      VBF_delta_R_AllJets = min(VBF_delta_R_AllJets,VBF_current_delta_R_AllJets);
	      VBF_matching_index_AllJets = a;
	      VBFGenMatchedJetsVect.push_back(AllJetsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }
	if(VBF_matching_index_AllJets>=0){
	  number_of_VBFGen_matched_to_AllJets++;
	}
      }


    //Remove duplicates from Matched AllJets Vector
    auto comp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    auto last = std::unique(VBFGenMatchedJetsVect.begin(), VBFGenMatchedJetsVect.end(),comp);
    VBFGenMatchedJetsVect.erase(last, VBFGenMatchedJetsVect.end());
    nVBFGenMatchedJets = VBFGenMatchedJetsVect.size();
    //nMatchedAllJets = VBFGenMatchedJetsVect.size();

    // add VBF Gen matching infos into original jet
    for(unsigned int r = 0; r<AllJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<VBFGenMatchedJetsVect.size(); s++)
	  {

	    if(VBFGenMatchedJetsVect[s].pt()==AllJetsVect[r].pt())
	      {
		AllJetsVect[r].addUserInt("isVBFGenMatched",1);
	      }

	  }
      }



    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // VBF tagging
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "VBF tagging" << std::endl;

    std::vector<pat::Jet> VBFJetsVect = theVBFJetAnalyzer->FillJetVector(iEvent,iSetup);

    pat::CompositeCandidate theVBF;
    //pat::CompositeCandidate theVBFJECUp;
    //pat::CompositeCandidate theVBFJECDown;
    //pat::CompositeCandidate theVBFJERUp;
    //pat::CompositeCandidate theVBFJERDown;
    std::vector<pat::Jet> VBFPairJetsVect;

    float delta_eta_reco (0.), curr_delta_eta_reco(0.) ;
    int j1(-1), j2(-1);
    float curr_mjj(0.);
    pat::CompositeCandidate current_VBF;

    if(VBFJetsVect.size()>=2) {
      for(unsigned int a = 0; a<VBFJetsVect.size(); a++) {
        //find the VBF pair
        for(unsigned int b = 1; b<VBFJetsVect.size(); b++) {
	  //if(b!=a and VBFJetsVect.at(a).pt()>=30 and VBFJetsVect.at(b).pt()>=30 and VBFJetsVect.at(a).userInt("isLoose")>0 and VBFJetsVect.at(b).userInt("isLoose")>0 and (VBFJetsVect.at(a).eta()*VBFJetsVect.at(b).eta())<0)//if looser thresholds applied; we will use that for JER-JEC effects
	  if(b!=a and (VBFJetsVect.at(a).eta()*VBFJetsVect.at(b).eta())<0)//currently we are fine with what is defined in vbfJetSet
            {
	      //calculate delta eta
              curr_delta_eta_reco = abs(VBFJetsVect.at(a).eta() - VBFJetsVect.at(b).eta());
	      current_VBF.clearDaughters();
	      current_VBF.addDaughter(VBFJetsVect.at(a));
	      current_VBF.addDaughter(VBFJetsVect.at(b));
	      addP4.set(current_VBF);
	      curr_mjj = current_VBF.mass();
              if(curr_delta_eta_reco>delta_eta_reco and curr_delta_eta_reco>DetaVBF and curr_mjj>InvmassVBF)
                {
                  delta_eta_reco = curr_delta_eta_reco;
                  j1=std::min(a,b);
                  j2=std::max(a,b);
                }
            }
        }
      }

      if(j1>=0 && j2>=0)//otherwise, if indices are -1, theVBF seg faults
	{
	  theVBF.addDaughter(VBFJetsVect.at(j1));
	  theVBF.addDaughter(VBFJetsVect.at(j2));
	  addP4.set(theVBF);
	  VBFPairJetsVect.push_back(VBFJetsVect.at(j1));
	  VBFPairJetsVect.push_back(VBFJetsVect.at(j2));
	}
    }

    if(theVBF.pt()>0 && theVBF.mass()>InvmassVBF && abs(theVBF.daughter(1)->eta() - theVBF.daughter(0)->eta())>DetaVBF) {isVBF = true;}

    ////Skip the event if VBF conditions not fulfilled
    ////!!! Removed, let's keep it as a flag. We need non-VBF events for control regions in data.

    // 27 Sep 2018: restored, to reduce output size
    if(WriteOnlyisVBFEvents)//set in cfg file
      {
	if(!isVBF) return;
      }


    //This trigger not used anymore
    ////Find the VBF pair among trigger standalone objects
    //pat::CompositeCandidate theTriggerVBF;
    //std::vector<pat::TriggerObjectStandAlone> TriggerVBFPairJetsVect;
    //float delta_eta_reco_HLT (0.), curr_delta_eta_reco_HLT(0.) ;
    //float curr_mjj_HLT (0.);
    //pat::CompositeCandidate current_VBF_HLT;
    //int j1_HLT(-1), j2_HLT(-1);
    //if(PotentialTriggerVBFPairJets.size()>=2) {
    //for(unsigned int a = 0; a<PotentialTriggerVBFPairJets.size(); a++)
    //{
    //for(unsigned int b = 1; b<PotentialTriggerVBFPairJets.size(); b++)
    //{
    //if(b!=a and PotentialTriggerVBFPairJets.at(a).pt()>=20 and PotentialTriggerVBFPairJets.at(b).pt()>=20 and (PotentialTriggerVBFPairJets.at(a).eta()*PotentialTriggerVBFPairJets.at(b).eta())<0)//20 GeV threshold is trigger dependent!!!
	//{
    //curr_delta_eta_reco_HLT = abs(PotentialTriggerVBFPairJets.at(a).eta() - PotentialTriggerVBFPairJets.at(b).eta());
    //current_VBF_HLT.clearDaughters();
    //current_VBF_HLT.addDaughter(PotentialTriggerVBFPairJets.at(a));
    //current_VBF_HLT.addDaughter(PotentialTriggerVBFPairJets.at(b));
    //addP4.set(current_VBF_HLT);
    //curr_mjj_HLT = current_VBF_HLT.mass();
    //if(curr_delta_eta_reco_HLT>delta_eta_reco_HLT and curr_delta_eta_reco_HLT>DetaVBF and curr_mjj_HLT>InvmassVBF)
    //{
    //delta_eta_reco_HLT = curr_delta_eta_reco_HLT;
    //j1_HLT=std::min(a,b);
    //j2_HLT=std::max(a,b);
    //}
    //}
    //}
    //}
    //if(j1_HLT>=0 && j2_HLT>=0)
    //{
    //theTriggerVBF.addDaughter(PotentialTriggerVBFPairJets.at(j1_HLT));
    //  theTriggerVBF.addDaughter(PotentialTriggerVBFPairJets.at(j2_HLT));
    //	  addP4.set(theTriggerVBF);
    //	  TriggerVBFPairJetsVect.push_back(PotentialTriggerVBFPairJets.at(j1_HLT));
    //	  TriggerVBFPairJetsVect.push_back(PotentialTriggerVBFPairJets.at(j2_HLT));
    //	}
    //}
    //if(theTriggerVBF.pt()>0 && theTriggerVBF.mass()>InvmassVBF && abs(theTriggerVBF.daughter(1)->eta() - theTriggerVBF.daughter(0)->eta())>DetaVBF) {isTriggerVBF = true;}

    //    //Find VBF jets that are matched to VBF trigger objects

    //float delta_R_VBF = 1000.;
    //float current_delta_R_VBF = 1000.;
    //int ch_VBF = -1;
    //std::vector<pat::Jet> SelectedVBFJetsVect;

    //for(unsigned int t1 = 0; t1<TriggerVBFPairJetsVect.size(); t1++)
    //{
    //	for(unsigned int s = 0; s<VBFJetsVect.size(); s++)
    //	  {
    //	    current_delta_R_VBF = fabs(reco::deltaR(VBFJetsVect.at(s).eta(),VBFJetsVect.at(s).phi(),TriggerVBFPairJetsVect.at(t1).eta(),TriggerVBFPairJetsVect.at(t1).phi()));
    //	    if(current_delta_R_VBF<0.6 and current_delta_R_VBF<delta_R_VBF)
    //	      {
    //		delta_R_VBF=current_delta_R_VBF;
    //		ch_VBF = s;
    //	      }
    //	  }

    //	if(ch_VBF>=0) SelectedVBFJetsVect.push_back(VBFJetsVect.at(ch_VBF));

    //}

    ////SelectedVBFJetsVect are then the jets matched to trigger objects firing the VBF filter

    // add VBF Gen matching infos into original jet
    for(unsigned int r = 0; r<VBFPairJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<VBFGenMatchedJetsVect.size(); s++)
	  {

	    if(VBFGenMatchedJetsVect[s].pt()==VBFPairJetsVect[r].pt())
	      {
		VBFPairJetsVect[r].addUserInt("isVBFGenMatched",1);
	      }

	  }
      }

    //Clear VBF vector, not needed anymore
    VBFJetsVect.clear();



    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 CHS Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //Fill a vector of AK4 CHS Jets, with kinematical cuts defined in the config file (pT, eta, eventually JetID or b-tagging)
    if(isVerbose) std::cout << "AK4 CHS" << std::endl;

    std::vector<pat::Jet> CHSJetsVect = theCHSJetAnalyzer->FillJetVector(iEvent,iSetup);
    //std::vector<pat::Jet> AllBarrelJetsVect = theCHSJetAnalyzer->FillJetVector(iEvent);//without VBF removal

    //Clear the vector of structures at every event, because we are not using a fixed number of jets and not using the Reset/List function //#### Johannes
    if (WriteAllJets) AllJets.clear();
    //AllBarrelJets.clear();
    CHSJets.clear();
    VBFPairJets.clear();
    ggHJet.clear();
    if(WriteFatJets) CHSFatJets.clear();
    //CaloJets.clear();


    //Counts how many loose-tight ID jets are found in the event
    for(unsigned int a = 0; a<CHSJetsVect.size(); a++) {
        if(CHSJetsVect[a].hasUserInt("isLoose") && CHSJetsVect[a].userInt("isLoose")>0) nLooseCHSJets++;
        if(CHSJetsVect[a].hasUserInt("isTight") && CHSJetsVect[a].userInt("isTight")>0) nTightCHSJets++;
	//2 Nov 2018: first calo-lifetime tentative tagging
	if(CHSJetsVect[a].chargedHadronEnergyFraction()<0.2 && CHSJetsVect[a].chargedMultiplicity()<10 && CHSJetsVect[a].neutralEmEnergyFraction()<0.15 && CHSJetsVect[a].neutralHadronEnergyFraction()>0.8 && CHSJetsVect[a].photonEnergyFraction()<0.1)
	  {
	    nLooseCaloTagJets++;
	    if(CHSJetsVect[a].chargedHadronEnergyFraction()<0.08 && CHSJetsVect[a].chargedMultiplicity()<8 && CHSJetsVect[a].neutralEmEnergyFraction()<0.08 && CHSJetsVect[a].neutralHadronEnergyFraction()>0.9 && CHSJetsVect[a].photonEnergyFraction()<0.08 && (CHSJetsVect[a].chargedEmEnergy() + CHSJetsVect[a].neutralEmEnergy())<10)
	      {
		nCaloTagJets++;
		CHSJetsVect[a].addUserInt("isCaloTag",1);
	      }
	  }
    }



    ////Find jets that are matched to Displaced trigger objects
    ////First, remove trigger standalone objects marked as VBF trigger pair
    //for(unsigned int s = 0; s<TriggerVBFPairJetsVect.size(); s++)
    //{
    //	for(unsigned int r = 0; r<PotentialTriggerDisplacedJets.size(); r++)
    //	  {
    //	    if(TriggerVBFPairJetsVect.at(s).pt()==PotentialTriggerDisplacedJets.at(r).pt() && isTriggerVBF)//if not tagged as VBF trigger pair, don't remove them
    //	      {
    //		PotentialTriggerDisplacedJets.erase(PotentialTriggerDisplacedJets.begin()+r);
    //	      }
    //	  }
    //  }


    ////Second, loop over potential signal jets (left after removing the VBF pair)
    //float delta_R = 1000.;
    //float current_delta_R = 1000.;
    //int ch = -1;
    //std::vector<pat::Jet> SelectedDisplacedJetVect;

    //for(unsigned int s = 0; s<CHSJetsVect.size(); s++)
    //{
    //	for(unsigned int t1 = 0; t1<PotentialTriggerDisplacedJets.size(); t1++)
    //	  {
    //	    current_delta_R = fabs(reco::deltaR(CHSJetsVect.at(s).eta(),CHSJetsVect.at(s).phi(),PotentialTriggerDisplacedJets.at(t1).eta(),PotentialTriggerDisplacedJets.at(t1).phi()));
    //	    if(current_delta_R<0.6 and current_delta_R<delta_R)
    //	      {
    //		delta_R=current_delta_R;
    //		ch = s;
    //	      }
    //
    //	  }
    //}

    //if(ch>=0)
    //{
    //	SelectedDisplacedJetVect.push_back(CHSJetsVect.at(ch));
    //}

    ////Final match to trigger object
    ////First VBF jets
    //for(unsigned int s = 0; s<VBFPairJetsVect.size(); s++)
    //{
    //	//VBF Trigger
    //	for(unsigned int a = 0; a<SelectedVBFJetsVect.size(); a++)
    //	  {
    //	    if(SelectedVBFJetsVect.at(a).pt()==VBFPairJetsVect.at(s).pt())
    //	      {
    //		if(!VBFPairJetsVect.at(s).hasUserInt("TriggerMatched_VBFJet")) VBFPairJetsVect.at(s).addUserInt("TriggerMatched_VBFJet",1);
    //	      }
    //	  }
    //
    //	//Displaced Trigger
    //	for(unsigned int b = 0; b<SelectedDisplacedJetVect.size(); b++)
    ///	  {
    //	    if(SelectedDisplacedJetVect.at(b).pt()==VBFPairJetsVect.at(s).pt())
    //	      {
    //		if(!VBFPairJetsVect.at(s).hasUserInt("TriggerMatched_DisplacedJet")) VBFPairJetsVect.at(s).addUserInt("TriggerMatched_DisplacedJet",1);
    //	      }
    //	  }
    //}

    //Then signal jets
    //for(unsigned int s = 0; s<CHSJetsVect.size(); s++)
    //      {
    //	//VBF Trigger
    //	for(unsigned int a = 0; a<SelectedVBFJetsVect.size(); a++)
    //	  {
    //	    if(SelectedVBFJetsVect.at(a).pt()==CHSJetsVect.at(s).pt())
    //	      {
    //		if(!CHSJetsVect.at(s).hasUserInt("TriggerMatched_VBFJet")) CHSJetsVect.at(s).addUserInt("TriggerMatched_VBFJet",1);
    //	      }
    //	  }
    ///
    //	//Displaced Trigger
    //	for(unsigned int b = 0; b<SelectedDisplacedJetVect.size(); b++)
    //	  {
    //	    if(SelectedDisplacedJetVect.at(b).pt()==CHSJetsVect.at(s).pt())
    //	      {
    //		if(!CHSJetsVect.at(s).hasUserInt("TriggerMatched_DisplacedJet")) CHSJetsVect.at(s).addUserInt("TriggerMatched_DisplacedJet",1);
    //	      }
    //	  }
    //}



    //One way to implement jet-gen b-quark matching is performed here
    if(isVerbose) std::cout << "AK4 CHS matching to b quarks" << std::endl;
    std::vector<pat::Jet> MatchedCHSJetsVect;

    //Matching the b quarks to AK4CHS jets
    //Starting point: b-quark
    int matching_index_CHSJets;//local variable
    float delta_R_CHSJets;//local variable
    float current_delta_R_CHSJets;//local variable
    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
      {
	delta_R_CHSJets = 1000.;
	current_delta_R_CHSJets = 1000.;
	matching_index_CHSJets = -1;
	for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
	  {
	    current_delta_R_CHSJets = fabs(reco::deltaR(CHSJetsVect[a].eta(),CHSJetsVect[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
	    if(current_delta_R_CHSJets<0.4 && current_delta_R_CHSJets<delta_R_CHSJets && CHSJetsVect[a].genParton() && (fabs(CHSJetsVect[a].hadronFlavour())==5 || fabs(CHSJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[a].genParton()) )==idMotherB)
	      //this implements all the reasonable possibilities!
	      {
	      delta_R_CHSJets = min(delta_R_CHSJets,current_delta_R_CHSJets);
	      matching_index_CHSJets = a;
	      CHSJetsVect[a].addUserInt("original_jet_index",a+1);
	      MatchedCHSJetsVect.push_back(CHSJetsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }
	if(matching_index_CHSJets>=0){
	  number_of_b_matched_to_CHSJets++;
	}
      }


    //Remove duplicates from Matched CHSJets Vector
    for(unsigned int r = 0; r<MatchedCHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedCHSJetsVect.size(); s++)
	  {
	    if(r!=s && MatchedCHSJetsVect[s].pt()==MatchedCHSJetsVect[r].pt()) MatchedCHSJetsVect.erase(MatchedCHSJetsVect.begin()+s);
	  }//duplicates removed
      }
    nMatchedCHSJets = MatchedCHSJetsVect.size();

    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedCHSJetsVect.size(); s++)
	  {

	    if(MatchedCHSJetsVect[s].pt()==CHSJetsVect[r].pt())
	      {
		//let's add flags helping to find matched jets corresponding to original Jets vector
		CHSJetsVect[r].addUserInt("isGenMatched",1);
		//CHSJetsVect[r].addUserInt("isMatchedToMatchedCHSJet",s+1);//obsolete
	      }

	  }
	//add number of b's matched to jet
	current_delta_R_CHSJets = 1000.;
	int number_bs_matched_to_CHSJet = 0;
	for (unsigned int b = 0; b<GenBquarksVect.size(); b++){
	  current_delta_R_CHSJets = fabs(reco::deltaR(CHSJetsVect[r].eta(),CHSJetsVect[r].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
	  if(current_delta_R_CHSJets<0.4 && CHSJetsVect[r].genParton() && (fabs(CHSJetsVect[r].hadronFlavour())==5 || fabs(CHSJetsVect[r].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[r].genParton()) )==idMotherB)
	    //this implements all the reasonable possibilities!
	    {
	      number_bs_matched_to_CHSJet += 1;
	    }
	}
	CHSJetsVect[r].addUserInt("nMatchedGenBquarks",number_bs_matched_to_CHSJet);
      }


    // add VBF Gen matching infos into original jet
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<VBFGenMatchedJetsVect.size(); s++)
	  {

	    if(VBFGenMatchedJetsVect[s].pt()==CHSJetsVect[r].pt())
	      {
		CHSJetsVect[r].addUserInt("isVBFGenMatched",1);
	      }

	  }
      }


    // add b-matching infos into original jet
    if (WriteAllJets){
    for(unsigned int r = 0; r<AllJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedCHSJetsVect.size(); s++)
	  {

	    if(MatchedCHSJetsVect[s].pt()==AllJetsVect[r].pt())
	      {
		//let's add flags helping to find matched jets corresponding to original Jets vector
		AllJetsVect[r].addUserInt("isGenMatched",1);
		//CHSJetsVect[r].addUserInt("isMatchedToMatchedCHSJet",s+1);//obsolete
	      }

	  }
      }
    }

    //std::cout << "CHSJetsVect size: " << nCHSJets << std::endl;
    //std::cout << "AllBarrelJetsVect size: " << nAllBarrelJets << std::endl;


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Gluon fusion tagging
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    std::vector<pat::Jet> ggHJetVect;
    int ggH_matching_index_CHSJets;
    ggH_matching_index_CHSJets = -1;

    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
        if(CHSJetsVect.at(r).pt()>=30 and CHSJetsVect.at(r).userInt("isTight")>0 and ggH_matching_index_CHSJets<0)//as soon as it finds a gluon-like jet, exit
          {
            ggH_matching_index_CHSJets = r;
          }
      }

    if(ggH_matching_index_CHSJets>=0)
      {
        ggHJetVect.push_back(CHSJetsVect.at(ggH_matching_index_CHSJets));
        isggH = true;
      }


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Remove jets tagged as VBF or gluon fusion from the list of potential signal
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(PerformVBF)
      {
        for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
          {
            for(unsigned int s = 0; s<VBFPairJetsVect.size(); s++)
              {
                if(VBFPairJetsVect[s].pt()==CHSJetsVect[r].pt() && isVBF) //if jets aren't tagged as VBF jets, don't remove them
                  {
                    CHSJetsVect.erase(CHSJetsVect.begin()+r);
                  }
              }//VBF jets removed
          }

      }

    else if(PerformggH)
      {

        for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
          {
            for(unsigned int s = 0; s<ggHJetVect.size(); s++)
              {
                if(ggHJetVect[s].pt()==CHSJetsVect[r].pt() && isggH) //if jets aren't tagged as ggH jets, don't remove them

                  {
                    CHSJetsVect.erase(CHSJetsVect.begin()+r);
                  }
              }//ggH jet removed
          }
      }

    nCHSJets = CHSJetsVect.size();


    //QCD killer cut
    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) if(fabs(reco::deltaPhi(CHSJetsVect[i].phi(), MET.phi())) < MinJetMetDPhi) MinJetMetDPhi = fabs(reco::deltaPhi(CHSJetsVect[i].phi(), MET.phi()));

    //QCD killer with ggH jet
    for(unsigned int i = 0; i < ggHJetVect.size(); i++) if(fabs(reco::deltaPhi(ggHJetVect[i].phi(), MET.phi())) < ggHJetMetDPhi) ggHJetMetDPhi = fabs(reco::deltaPhi(ggHJetVect[i].phi(), MET.phi()));

    if (WriteAllJets) for(unsigned int i = 0; i < AllJetsVect.size(); i++) if(fabs(reco::deltaPhi(AllJetsVect[i].phi(), MET.phi())) < MinJetMetDPhiAllJets) MinJetMetDPhiAllJets = fabs(reco::deltaPhi(AllJetsVect[i].phi(), MET.phi()));


    //Try to build Higgs candidate
    pat::CompositeCandidate theHDiCHS;
    pat::CompositeCandidate theHTriCHS;
    pat::CompositeCandidate theHQuadCHS;
    pat::CompositeCandidate theHDiCHSMatched;
    pat::CompositeCandidate theHTriCHSMatched;
    pat::CompositeCandidate theHQuadCHSMatched;

    if(nCHSJets>=2)
    {
       theHDiCHS.addDaughter(CHSJetsVect.at(0));
       theHDiCHS.addDaughter(CHSJetsVect.at(1));
       addP4.set(theHDiCHS);
       //std::cout << "Mass of dijet: " << theHDiCHS.mass() << std::endl;
       if(nCHSJets>=3)
       {
           theHTriCHS.addDaughter(CHSJetsVect.at(0));
           theHTriCHS.addDaughter(CHSJetsVect.at(1));
           theHTriCHS.addDaughter(CHSJetsVect.at(2));
           addP4.set(theHTriCHS);
           //std::cout << "Mass of trijet: " << theHTriCHS.mass() << std::endl;
           if(nCHSJets>=4)
           {
               theHQuadCHS.addDaughter(CHSJetsVect.at(0));
               theHQuadCHS.addDaughter(CHSJetsVect.at(1));
               theHQuadCHS.addDaughter(CHSJetsVect.at(2));
               theHQuadCHS.addDaughter(CHSJetsVect.at(3));
               addP4.set(theHQuadCHS);
               //std::cout << "Mass of quadjet: " << theHQuadCHS.mass() << std::endl;
           }
       }
    }

    //std::cout << "nMatchedCHSJets: " << nMatchedCHSJets << std::endl;
    //std::cout << "number of b-quarks matched: " << number_of_b_matched_to_CHSJets << std::endl;

    if(nMatchedCHSJets==2)
    {
       theHDiCHSMatched.addDaughter(MatchedCHSJetsVect.at(0));
       theHDiCHSMatched.addDaughter(MatchedCHSJetsVect.at(1));
       addP4.set(theHDiCHSMatched);
       //std::cout << "Mass of Matched dijet: " << theHDiCHSMatched.mass() << std::endl;
    }

    else if(nMatchedCHSJets==3)
    {
       theHTriCHSMatched.addDaughter(MatchedCHSJetsVect.at(0));
       theHTriCHSMatched.addDaughter(MatchedCHSJetsVect.at(1));
       theHTriCHSMatched.addDaughter(MatchedCHSJetsVect.at(2));
       addP4.set(theHTriCHSMatched);
       //std::cout << "Mass of Matched trijet: " << theHTriCHSMatched.mass() << std::endl;
    }

    else if(nMatchedCHSJets==4)
    {
       theHQuadCHSMatched.addDaughter(MatchedCHSJetsVect.at(0));
       theHQuadCHSMatched.addDaughter(MatchedCHSJetsVect.at(1));
       theHQuadCHSMatched.addDaughter(MatchedCHSJetsVect.at(2));
       theHQuadCHSMatched.addDaughter(MatchedCHSJetsVect.at(3));
       addP4.set(theHQuadCHSMatched);
       //std::cout << "Mass of Matched quadjet: " << theHQuadCHSMatched.mass() << std::endl;
    }

    else {if(isVerbose) std::cout<< "No matched jets!" << std::endl;}


    // For all the other jets
    // VBFPairJets
    // add b-matching infos into original jet
    for(unsigned int r = 0; r<VBFPairJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedCHSJetsVect.size(); s++)
	  {

	    if(MatchedCHSJetsVect[s].pt()==VBFPairJetsVect[r].pt())
	      {
		//let's add flags helping to find matched jets corresponding to original Jets vector
		VBFPairJetsVect[r].addUserInt("isGenMatched",1);
		//CHSJetsVect[r].addUserInt("isMatchedToMatchedCHSJet",s+1);//obsolete
	      }

	  }
      }
    // AllBarrelJets
    // add b-matching infos into original jet
    //for(unsigned int r = 0; r<AllBarrelJetsVect.size(); r++)
    //{
    //for(unsigned int s = 0; s<MatchedCHSJetsVect.size(); s++)
    //  {

    //	    if(MatchedCHSJetsVect[s].pt()==AllBarrelJetsVect[r].pt())
    //	      {
    //		//let's add flags helping to find matched jets corresponding to original Jets vector
    //		AllBarrelJetsVect[r].addUserInt("isGenMatched",1);
    //		//CHSJetsVect[r].addUserInt("isMatchedToMatchedCHSJet",s+1);//obsolete
    //	      }

    //	  }
    // }
    // add VBF Gen matching infos into original jet
    //for(unsigned int r = 0; r<AllBarrelJetsVect.size(); r++)
    //{
    //	for(unsigned int s = 0; s<VBFGenMatchedJetsVect.size(); s++)
    //	  {
    //
    //	    if(VBFGenMatchedJetsVect[s].pt()==AllBarrelJetsVect[r].pt())
    //	      {
    //		AllBarrelJetsVect[r].addUserInt("isVBFGenMatched",1);
    //	      }
    //
    //	  }
    //}


    // calculates n-subjettiness for each jet, including calculated out of neutral and charged constituents
    if(CalculateNsubjettiness) {
      for(unsigned int j = 0; j < CHSJetsVect.size(); j++){
        float tau1_neutral, tau2_neutral, tau1_charged, tau2_charged;
        std::vector<fastjet::PseudoJet> currentAxes;
        calcNsubjettiness(CHSJetsVect[j], tau1_neutral, tau1_charged ,tau2_neutral, tau2_charged, currentAxes);
        CHSJetsVect[j].addUserFloat("tau1", CHSJetsVect[j].userFloat("NjettinessAK4CHS:tau1"));
        CHSJetsVect[j].addUserFloat("tau2", CHSJetsVect[j].userFloat("NjettinessAK4CHS:tau2"));
        CHSJetsVect[j].addUserFloat("tau3", CHSJetsVect[j].userFloat("NjettinessAK4CHS:tau3"));
        CHSJetsVect[j].addUserFloat("tau1_neutral", tau1_neutral);
        CHSJetsVect[j].addUserFloat("tau2_neutral", tau2_neutral);
        CHSJetsVect[j].addUserFloat("tau1_charged", tau1_charged);
        CHSJetsVect[j].addUserFloat("tau2_charged", tau2_charged);
      }
    }
    // stores number of subjets found by SoftDrop algorithm; with relaxed pT cut, for QCD and signal found 2 subjets
    // for (unsigned int l = 0; l < SoftDropSubJetVect.size(); l++){
    //   float dRjets = reco::deltaR(SoftDropSubJetVect[l].eta(),SoftDropSubJetVect[l].phi(),CHSJetsVect[j].eta(),CHSJetsVect[j].phi());
    //   if (dRjets < 0.01) {
    //     auto wSubjets = SoftDropSubJetVect[l].subjets("SoftDrop");
    //     CHSJetsVect[j].addUserFloat("nSubJets", wSubjets.size());
    //   }
    // }

    //TODO: Move this calculation to the PFCandidate section
    if (!isShort){
    for(unsigned int j = 0; j < CHSJetsVect.size(); j++){
      int nTrackConstituents = 0;
      //per jet tag: number of jet constituents and number of tracks
      std::vector<edm::Ptr<reco::Candidate>> JetConstituentVect = CHSJetsVect[j].getJetConstituents();
      CHSJetsVect.at(j).addUserInt("nConstituents",JetConstituentVect.size());
      for(unsigned int k = 0; k < JetConstituentVect.size(); k++){

        if(JetConstituentVect[k]->charge()!=0){
          nTrackConstituents++;
        }
      }
      CHSJetsVect.at(j).addUserInt("nTrackConstituents",nTrackConstituents);
    }
    }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 CHS Jets: Imperial College Tagger
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //First attempt to read Imperial Tagger
    edm::Handle<reco::JetTagCollection> pfXTagWP0p01Handle;
    iEvent.getByToken(JetTagWP0p01Token, pfXTagWP0p01Handle);
    const reco::JetTagCollection & pfXWP0p01Tags = *(pfXTagWP0p01Handle.product());

    edm::Handle<reco::JetTagCollection> pfXTagWP0p1Handle;
    iEvent.getByToken(JetTagWP0p1Token, pfXTagWP0p1Handle);
    const reco::JetTagCollection & pfXWP0p1Tags = *(pfXTagWP0p1Handle.product());

    edm::Handle<reco::JetTagCollection> pfXTagWP1Handle;
    iEvent.getByToken(JetTagWP1Token, pfXTagWP1Handle);
    const reco::JetTagCollection & pfXWP1Tags = *(pfXTagWP1Handle.product());

    edm::Handle<reco::JetTagCollection> pfXTagWP10Handle;
    iEvent.getByToken(JetTagWP10Token, pfXTagWP10Handle);
    const reco::JetTagCollection & pfXWP10Tags = *(pfXTagWP10Handle.product());

    edm::Handle<reco::JetTagCollection> pfXTagWP100Handle;
    iEvent.getByToken(JetTagWP100Token, pfXTagWP100Handle);
    const reco::JetTagCollection & pfXWP100Tags = *(pfXTagWP100Handle.product());

    edm::Handle<reco::JetTagCollection> pfXTagWP1000Handle;
    iEvent.getByToken(JetTagWP1000Token, pfXTagWP1000Handle);
    const reco::JetTagCollection & pfXWP1000Tags = *(pfXTagWP1000Handle.product());

    //Addd per-jet user float including Imperial Tagger
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<pfXWP0p01Tags.size(); s++)
	  {
	    //if(pfXWP0p01Tags[s].first->eta()==CHSJetsVect[r].eta())
            if( reco::deltaR(pfXWP0p01Tags[s].first->eta(),pfXWP0p01Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
	      {
                //std::cout << "CHS Jets n. " << r << " and pfXWP0p01 n. " << s << "are matching!" << std::endl;
		CHSJetsVect[r].addUserFloat("pfXWP0p01",pfXWP0p01Tags[s].second);
	      }
	  }

	for(unsigned int s = 0; s<pfXWP0p1Tags.size(); s++)
          {
            //if(pfXWP0p1Tags[s].first->eta()==CHSJetsVect[r].eta())
            if( reco::deltaR(pfXWP0p1Tags[s].first->eta(),pfXWP0p1Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
              {
                //std::cout << "CHS Jets n. " << r << " and pfXWP0p1 n. " << s << "are matching!" << std::endl;
                CHSJetsVect[r].addUserFloat("pfXWP0p1",pfXWP0p1Tags[s].second);
              }
          }

	for(unsigned int s = 0; s<pfXWP1Tags.size(); s++)
	  {
	    //if(pfXWP1Tags[s].first->eta()==CHSJetsVect[r].eta())
            if( reco::deltaR(pfXWP1Tags[s].first->eta(),pfXWP1Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
	      {
                //std::cout << "CHS Jets n. " << r << " and pfXWP1 n. " << s << "are matching!" << std::endl;
		CHSJetsVect[r].addUserFloat("pfXWP1",pfXWP1Tags[s].second);
	      }
	  }


	for(unsigned int s = 0; s<pfXWP10Tags.size(); s++)
	  {
            if( reco::deltaR(pfXWP10Tags[s].first->eta(),pfXWP10Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
	      {
		CHSJetsVect[r].addUserFloat("pfXWP10",pfXWP10Tags[s].second);
	      }
	  }

	for(unsigned int s = 0; s<pfXWP100Tags.size(); s++)
	  {
            if( reco::deltaR(pfXWP100Tags[s].first->eta(),pfXWP100Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
	      {
		CHSJetsVect[r].addUserFloat("pfXWP100",pfXWP100Tags[s].second);
	      }
	  }



	for(unsigned int s = 0; s<pfXWP1000Tags.size(); s++)
	  {
	    //if(pfXWP1000Tags[s].first->eta()==CHSJetsVect[r].eta())
            if( reco::deltaR(pfXWP1000Tags[s].first->eta(),pfXWP1000Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
	      {
                if(isVerbose) std::cout << "CHS Jets n. " << r << " and pfXWP1000 n. " << s << " are matching; dR: " << reco::deltaR(pfXWP1000Tags[s].first->eta(),pfXWP1000Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) << std::endl;
		CHSJetsVect[r].addUserFloat("pfXWP1000",pfXWP1000Tags[s].second);
	      }
	  }
      }


    //# Loop over jets and study b tag info.
    //for (unsigned int i = 0; i != pfXWP0p01Tags.size(); ++i) {
    //    if(pfXWP0p01Tags[i].first->pt()>1 && abs(pfXWP0p01Tags[i].first->eta())<2.4) std::cout << "  pfX WP0p01 tag jet  [" << i << "]\tpt: " << pfXWP0p01Tags[i].first->pt() << "\teta: " << pfXWP0p01Tags[i].first->eta() << "\tphi: " << pfXWP0p01Tags[i].first->phi() << "\tpfXTags: " << pfXWP0p01Tags[i].second << std::endl;
    //}

    //for (unsigned int i = 0; i != pfXWP1Tags.size(); ++i) {
    //    if(pfXWP1Tags[i].first->pt()>1 && abs(pfXWP1Tags[i].first->eta())<2.4) std::cout << "  pfX WP1 tag jet  [" << i << "]\tpt: " << pfXWP1Tags[i].first->pt() << "\teta: " << pfXWP1Tags[i].first->eta() << "\tphi: " << pfXWP1Tags[i].first->phi() << "\tpfXTags: " << pfXWP1Tags[i].second << std::endl;
    //}

    if(isVerbose) {
      for (unsigned int i = 0; i != pfXWP1000Tags.size(); ++i) {
          if(pfXWP1000Tags[i].first->pt()>1 && abs(pfXWP1000Tags[i].first->eta())<2.4) std::cout << "  pfX WP1000 tag jet  [" << i << "]\tpt: " << pfXWP1000Tags[i].first->pt() << "\teta: " << pfXWP1000Tags[i].first->eta() << "\tphi: " << pfXWP1000Tags[i].first->phi() << "\tpfXTags: " << pfXWP1000Tags[i].second << std::endl;
      }
    }

    //If you have a Jet, rather than a JetTag, and wish to know if it is b-tagged, there are several ways of doing so. One which always works is to perform angular matching between the Jet and the JetTag::jet(). (The match should be perfect if your JetCollection was used to produce the JetTagCollection).


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // B-tagging discriminant shape calibration for AK4 CHS jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    if (isShort){
      std::map<std::string, float> btagWeights = theCHSJetAnalyzer->CalculateBtagReshapeSF(CHSJetsVect);
      bTagWeight_central = btagWeights["weight_central"];
      bTagWeight_jesup = btagWeights["weight_jesup"];
      bTagWeight_jesdown = btagWeights["weight_jesdown"];
      bTagWeight_lfup = btagWeights["weight_lfup"];
      bTagWeight_lfdown = btagWeights["weight_lfdown"];
      bTagWeight_hfup = btagWeights["weight_hfup"];
      bTagWeight_hfdown = btagWeights["weight_hfdown"];
      bTagWeight_hfstats1up = btagWeights["weight_hfstats1up"];
      bTagWeight_hfstats1down = btagWeights["weight_hfstats1down"];
      bTagWeight_hfstats2up = btagWeights["weight_hfstats2up"];
      bTagWeight_hfstats2down = btagWeights["weight_hfstats2down"];
      bTagWeight_lfstats1up = btagWeights["weight_lfstats1up"];
      bTagWeight_lfstats1down = btagWeights["weight_lfstats1down"];
      bTagWeight_lfstats2up = btagWeights["weight_lfstats2up"];
      bTagWeight_lfstats2down = btagWeights["weight_lfstats2down"];
      bTagWeight_cferr1up = btagWeights["weight_cferr1up"];
      bTagWeight_cferr1down = btagWeights["weight_cferr1down"];
      bTagWeight_cferr2up = btagWeights["weight_cferr2up"];
      bTagWeight_cferr2down = btagWeights["weight_cferr2down"];

    }



    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 CALO Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    /*

    std::vector<reco::CaloJet> CaloJetsVect = theCaloJetAnalyzer->FillJetVector(iEvent);
    nCaloJets = CaloJetsVect.size();

    //std::cout << "n of b-quarks with at least one corresponding CHS jets: " << number_of_b_matched_to_CHSJets << std::endl;
    //std::cout << "n of properly matched CHS jets: " << nMatchedCHSJets << std::endl;
    //std::cout << "n of calo jets in acceptance: " << nCaloJets << std::endl;

    //Remove calo jets overlapped with VBF pair
    //We must perform a DR matching, since pT might be different
    //int matching_index_CaloJets_asVBF;//local variable
    float delta_R_CaloJets_asVBF;//local variable
    float current_delta_R_CaloJets_asVBF;//local variable

    for(unsigned int r = 0; r<CaloJetsVect.size(); r++)
      {
	delta_R_CaloJets_asVBF = 1000.;
	current_delta_R_CaloJets_asVBF = 1000.;
	for(unsigned int s = 0; s<VBFPairJetsVect.size(); s++)
	  {
            current_delta_R_CaloJets_asVBF = fabs(reco::deltaR(CaloJetsVect[r].eta(),CaloJetsVect[r].phi(),VBFPairJetsVect[s].eta(),VBFPairJetsVect[s].phi()));
            if(current_delta_R_CaloJets_asVBF<0.4 && current_delta_R_CaloJets_asVBF<delta_R_CaloJets_asVBF && isVBF)
	      //this implements all the reasonable possibilities!
	      {
	      delta_R_CaloJets_asVBF = min(delta_R_CaloJets_asVBF,current_delta_R_CaloJets_asVBF);
              if(isVerbose) std::cout << "This calo jet removed because overlaps VBF pair: pt " << CaloJetsVect[r].pt() << " ; eta: " << CaloJetsVect[r].eta() << " ; phi: " << CaloJetsVect[r].phi() << std::endl;
              CaloJetsVect.erase(CaloJetsVect.begin()+r);
	      }

	  }//VBF jet pair removed
      }

    nCaloJets = CaloJetsVect.size();
    std::vector<bool> caloGenMatched;
    for(unsigned int i = 0; i < CaloJetsVect.size(); i++) caloGenMatched.push_back(false);

    std::vector<reco::CaloJet> MatchedCaloJetsVect;


    //Matching the b quarks to AK4 calo jets
    //Starting point: b-quark
    int matching_index_CaloJets;//local variable
    float delta_R_CaloJets;//local variable
    float current_delta_R_CaloJets;//local variable

    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
      {
	delta_R_CaloJets = 1000.;
	current_delta_R_CaloJets = 1000.;
	matching_index_CaloJets = -1;
	for(unsigned int a = 0; a<CaloJetsVect.size(); a++)
	  {
	    current_delta_R_CaloJets = fabs(reco::deltaR(CaloJetsVect[a].eta(),CaloJetsVect[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
	    if(current_delta_R_CaloJets<0.4 && current_delta_R_CaloJets<delta_R_CaloJets)
	      //this implements all the reasonable possibilities!
	      {
	      delta_R_CaloJets = min(delta_R_CaloJets,current_delta_R_CaloJets);
	      matching_index_CaloJets = a;
              caloGenMatched[a] = true;
	      //JetsVect[a].addUserInt("original_jet_index",a+1);
	      MatchedCaloJetsVect.push_back(CaloJetsVect[a]);//avoid duplicates!
	      }
	  }
	if(matching_index_CaloJets>=0){
	  number_of_b_matched_to_CaloJets++;
	}
      }


    //Remove duplicates from Matched Jets Vector
    for(unsigned int r = 0; r<MatchedCaloJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedCaloJetsVect.size(); s++)
	  {
	    if(r!=s && MatchedCaloJetsVect[s].pt()==MatchedCaloJetsVect[r].pt()) MatchedCaloJetsVect.erase(MatchedCaloJetsVect.begin()+s);
	  }//duplicates removed
      }
    nMatchedCaloJets = MatchedCaloJetsVect.size();



    //Try to build Higgs candidate
    pat::CompositeCandidate theHDiCalo;
    pat::CompositeCandidate theHTriCalo;
    pat::CompositeCandidate theHQuadCalo;
    pat::CompositeCandidate theHDiCaloMatched;
    pat::CompositeCandidate theHTriCaloMatched;
    pat::CompositeCandidate theHQuadCaloMatched;

    if(nCaloJets>=2)
    {
       theHDiCalo.addDaughter(CaloJetsVect.at(0));
       theHDiCalo.addDaughter(CaloJetsVect.at(1));
       addP4.set(theHDiCalo);
       //std::cout << "Mass of dijet: " << theHDiCalo.mass() << std::endl;
       if(nCaloJets>=3)
       {
           theHTriCalo.addDaughter(CaloJetsVect.at(0));
           theHTriCalo.addDaughter(CaloJetsVect.at(1));
           theHTriCalo.addDaughter(CaloJetsVect.at(2));
           addP4.set(theHTriCalo);
           //std::cout << "Mass of trijet: " << theHTriCalo.mass() << std::endl;
           if(nCaloJets>=4)
           {
               theHQuadCalo.addDaughter(CaloJetsVect.at(0));
               theHQuadCalo.addDaughter(CaloJetsVect.at(1));
               theHQuadCalo.addDaughter(CaloJetsVect.at(2));
               theHQuadCalo.addDaughter(CaloJetsVect.at(3));
               addP4.set(theHQuadCalo);
               //std::cout << "Mass of quadjet: " << theHQuadCalo.mass() << std::endl;
           }
       }
    }

    //std::cout << "nMatchedCaloJets: " << nMatchedCaloJets << std::endl;
    //std::cout << "number of b-quarks matched: " << number_of_b_matched_to_CaloJets << std::endl;

    if(nMatchedCaloJets==2)
    {
       theHDiCaloMatched.addDaughter(MatchedCaloJetsVect.at(0));
       theHDiCaloMatched.addDaughter(MatchedCaloJetsVect.at(1));
       addP4.set(theHDiCaloMatched);
       //std::cout << "Mass of Matched dijet: " << theHDiCaloMatched.mass() << std::endl;
    }

    else if(nMatchedCaloJets==3)
    {
       theHTriCaloMatched.addDaughter(MatchedCaloJetsVect.at(0));
       theHTriCaloMatched.addDaughter(MatchedCaloJetsVect.at(1));
       theHTriCaloMatched.addDaughter(MatchedCaloJetsVect.at(2));
       addP4.set(theHTriCaloMatched);
       //std::cout << "Mass of Matched trijet: " << theHTriCaloMatched.mass() << std::endl;
    }

    else if(nMatchedCaloJets==4)
    {
       theHQuadCaloMatched.addDaughter(MatchedCaloJetsVect.at(0));
       theHQuadCaloMatched.addDaughter(MatchedCaloJetsVect.at(1));
       theHQuadCaloMatched.addDaughter(MatchedCaloJetsVect.at(2));
       theHQuadCaloMatched.addDaughter(MatchedCaloJetsVect.at(3));
       addP4.set(theHQuadCaloMatched);
       //std::cout << "Mass of Matched quadjet: " << theHQuadCaloMatched.mass() << std::endl;
    }

    else {if(isVerbose) std::cout<< "No matched jets!" << std::endl;}

    */

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK8 CHS Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    std::string SoftdropPuppiMassString(CHSFatJetPSet.getParameter<std::string>("softdropPuppiMassString"));
    //This string varies, depending on jet reclustering. To be used by JetAnalyzer and FillObjectsFormat
    if(isVerbose) std::cout << SoftdropPuppiMassString << std::endl;

    //Just another example of filling a vector of AK8 Jets
    if(isVerbose) std::cout << "AK8 CHS" << std::endl;

    //Old way
    // std::vector<pat::Jet> CHSFatJetsVect = theCHSFatJetAnalyzer->FillJetVector(iEvent);
    //if(!WriteFatJets)//not needed anymore?
    //{
    //CHSFatJetsVect.clear();//empty vector
    //}

    //New way, save energy
    std::vector<pat::Jet> CHSFatJetsVect;
    if(WriteFatJets)
      //if(WriteNFatJets>0)
      {
	CHSFatJetsVect = theCHSFatJetAnalyzer->FillJetVector(iEvent,iSetup);

      	std::vector<pat::Jet> MatchedCHSAK8JetsVect;

	//Matching the b quarks to AK8 jets
	//Starting point: b-quark
	int matching_index_CHSAK8Jets;//local variable
	float delta_R_CHSAK8Jets;//local variable
	float current_delta_R_CHSAK8Jets;//local variable
	for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
	  {
	    delta_R_CHSAK8Jets = 1000.;
	    current_delta_R_CHSAK8Jets = 1000.;
	    matching_index_CHSAK8Jets = -1;
	    for(unsigned int a = 0; a<CHSFatJetsVect.size(); a++)
	      {
		current_delta_R_CHSAK8Jets = fabs(reco::deltaR(CHSFatJetsVect[a].eta(),CHSFatJetsVect[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
		//		std::cout << "gen info " << CHSFatJetsVect[a].genParton() << "  " << fabs(CHSFatJetsVect[a].hadronFlavour()) << "  " << fabs(CHSFatJetsVect[a].partonFlavour()) << "  " << abs( Utilities::FindMotherId(CHSFatJetsVect[a].genParton()) ) << std::endl;
		if(current_delta_R_CHSAK8Jets<0.8 && current_delta_R_CHSAK8Jets<delta_R_CHSAK8Jets && CHSFatJetsVect[a].genParton() && (fabs(CHSFatJetsVect[a].hadronFlavour())==5 || fabs(CHSFatJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSFatJetsVect[a].genParton()) )==idMotherB)
		  //this implements all the reasonable possibilities, is also working for AK8 jets!
		  {
		    delta_R_CHSAK8Jets = min(delta_R_CHSAK8Jets,current_delta_R_CHSAK8Jets);
		    matching_index_CHSAK8Jets = a;
		    CHSFatJetsVect[a].addUserInt("original_jet_index",a+1);
		    MatchedCHSAK8JetsVect.push_back(CHSFatJetsVect[a]);//duplicates possible, must be removed afterwards!
		  }
	      } //loop over AK8 jets
	    if(matching_index_CHSAK8Jets>=0){
	      number_of_b_matched_to_FatJets++;
	    }
	  }//loop over gen b-quarks


	//Remove duplicates from Matched CHSJets Vector
	for(unsigned int r = 0; r<MatchedCHSAK8JetsVect.size(); r++)
	  {
	    for(unsigned int s = 0; s<MatchedCHSAK8JetsVect.size(); s++)
	      {
		if(r!=s && MatchedCHSAK8JetsVect[s].pt()==MatchedCHSAK8JetsVect[r].pt()) MatchedCHSAK8JetsVect.erase(MatchedCHSAK8JetsVect.begin()+s);
	      }//duplicates removed
	  }
	nMatchedFatJets = MatchedCHSAK8JetsVect.size();

	// add b-matching infos into original jet
	for(unsigned int r = 0; r<CHSFatJetsVect.size(); r++)
	  {
	    for(unsigned int s = 0; s<MatchedCHSAK8JetsVect.size(); s++)
	      {

		if(MatchedCHSAK8JetsVect[s].pt()==CHSFatJetsVect[r].pt())
		  {
		    //let's add flags helping to find matched jets corresponding to original Jets vector
		    CHSFatJetsVect[r].addUserInt("isGenMatched",1);
		  }

	      }//loop MatchedCHSAK8Jets

	    //add number of b's matched to jet
	    current_delta_R_CHSJets = 1000.;
	    int number_bs_matched_to_FatJet = 0;
	    for (unsigned int b = 0; b<GenBquarksVect.size(); b++){
	      current_delta_R_CHSJets = fabs(reco::deltaR(CHSFatJetsVect[r].eta(),CHSFatJetsVect[r].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
	      if(current_delta_R_CHSJets<0.8 && CHSFatJetsVect[r].genParton() && (fabs(CHSFatJetsVect[r].hadronFlavour())==5 || fabs(CHSFatJetsVect[r].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSFatJetsVect[r].genParton()) )==idMotherB)
		//this implements all the reasonable possibilities!
		{
		  number_bs_matched_to_FatJet += 1;
		}
	    }//loop genaerator b quarks
	    CHSFatJetsVect[r].addUserInt("nMatchedGenBquarks",number_bs_matched_to_FatJet);
	  }//loop AK8 jets

      //Remove jets tagged as VBF from the list of potential signal
      if (isVBF){
        theCHSFatJetAnalyzer->CleanFatJetsFromAK4(CHSFatJetsVect, VBFPairJetsVect, 1.2);
      }
     }//loop WriteFatJets

    nCHSFatJets = CHSFatJetsVect.size();

    // TODO: Move this calculation to the PFCandidate section
    if (!isShort){
    for(unsigned int j = 0; j < CHSFatJetsVect.size(); j++){
      int nTrackConstituents = 0;
      //per jet tag: number of jet constituents and number of tracks
      std::vector<edm::Ptr<reco::Candidate>> JetConstituentVect = CHSFatJetsVect[j].getJetConstituents();
      CHSFatJetsVect.at(j).addUserInt("nConstituents",JetConstituentVect.size());
      for(unsigned int k = 0; k < JetConstituentVect.size(); k++){

        if(JetConstituentVect[k]->charge()!=0){
          nTrackConstituents++;
        }
      }
      CHSFatJetsVect.at(j).addUserInt("nTrackConstituents",nTrackConstituents);
    }
    }

    if(isVerbose) {
      //Write a summary, in verbose mode
      std::cout << " --- Event n. " << iEvent.id().event() << ", lumi " << iEvent.luminosityBlock() << ", run " << iEvent.id().run() << std::endl;

      //wait//std::cout << "number of All AK4 jets:  " << AllJetsVect.size() << std::endl;
      //wait//if (WriteAllJets) for(unsigned int i = 0; i < AllJetsVect.size(); i++) std::cout << "  All CHS AK4 jet  [" << i << "]\tpt: " << AllJetsVect[i].pt() << "\teta: " << AllJetsVect[i].eta() << "\tphi: " << AllJetsVect[i].phi() << "\tmass: " << AllJetsVect[i].mass() << std::endl;

      std::cout << "number of CHS AK4 jets:  " << CHSJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < CHSJetsVect.size(); i++) std::cout << "  CHS AK4 jet  [" << i << "]\tpt: " << CHSJetsVect[i].pt() << "\teta: " << CHSJetsVect[i].eta() << "\tphi: " << CHSJetsVect[i].phi() << "\tmass: " << CHSJetsVect[i].mass() << std::endl;
      //wait//std::cout << "VBF jets pair:  " << VBFPairJetsVect.size() << std::endl;
      //wait//if(isVBF) std::cout << "VBF conditions satisfied" << std::endl;
      //wait//or(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) std::cout << "  VBF jet  [" << i << "]\tpt: " << VBFPairJetsVect[i].pt() << "\teta: " << VBFPairJetsVect[i].eta() << "\tphi: " << VBFPairJetsVect[i].phi() << "\tmass: " << VBFPairJetsVect[i].mass() << std::endl;

      std::cout << "Missing ET:  " << std::endl;
      std::cout << "  pt: " << MET.pt() << "\tphi: " << MET.phi() << std::endl;

      std::cout << "number of Gen B quarks:  " << GenBquarksVect.size() << std::endl;
      for(unsigned int i = 0; i < GenBquarksVect.size(); i++) std::cout << "  Gen B quark  [" << i << "]\tpt: " << GenBquarksVect[i].pt() << "\teta: " << GenBquarksVect[i].eta() << "\tphi: " << GenBquarksVect[i].phi() << "\tmass: " << GenBquarksVect[i].mass() << std::endl;
      std::cout << "number of CHS AK4 jets matched to b quarks:  " << MatchedCHSJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < MatchedCHSJetsVect.size(); i++) std::cout << "  Matched CHS AK4 jet  [" << i << "]\tpt: " << MatchedCHSJetsVect[i].pt() << "\teta: " << MatchedCHSJetsVect[i].eta() << "\tphi: " << MatchedCHSJetsVect[i].phi() << "\tmass: " << MatchedCHSJetsVect[i].mass() << std::endl;

      //wait//std::cout << "number of Gen VBF quarks/gluons:  " << GenVBFVect.size() << std::endl;
      //wait//for(unsigned int i = 0; i < GenVBFVect.size(); i++) std::cout << "  Gen VBF parton  [" << i << "]\tpt: " << GenVBFVect[i].pt() << "\teta: " << GenVBFVect[i].eta() << "\tphi: " << GenVBFVect[i].phi() << "\tmass: " << GenVBFVect[i].mass() << "\tpdgid: " << GenVBFVect[i].pdgId() << std::endl;
      //wait//std::cout << "number of CHS AK4 jets matched to VBF partons:  " << VBFGenMatchedJetsVect.size() << std::endl;
      //wait//for(unsigned int i = 0; i < VBFGenMatchedJetsVect.size(); i++) std::cout << "  Matched CHS AK4 jet  [" << i << "]\tpt: " << VBFGenMatchedJetsVect[i].pt() << "\teta: " << VBFGenMatchedJetsVect[i].eta() << "\tphi: " << VBFGenMatchedJetsVect[i].phi() << "\tmass: " << VBFGenMatchedJetsVect[i].mass() << std::endl;
      //if(isSignal) std::cout << "number of Calo AK4 jets:  " << CaloJetsVect.size() << std::endl;
      //if(isSignal) for(unsigned int i = 0; i < CaloJetsVect.size(); i++) std::cout << "  Calo AK4 jet  [" << i << "]\tpt: " << CaloJetsVect[i].pt() << "\teta: " << CaloJetsVect[i].eta() << "\tphi: " << CaloJetsVect[i].phi() << "\tmass: " << CaloJetsVect[i].mass() << std::endl;
      //if(isSignal) std::cout << "number of Matched Calo AK4 jets:  " << MatchedCaloJetsVect.size() << std::endl;
      //if(isSignal) for(unsigned int i = 0; i < MatchedCaloJetsVect.size(); i++) std::cout << "  Calo AK4 jet  [" << i << "]\tpt: " << MatchedCaloJetsVect[i].pt() << "\teta: " << MatchedCaloJetsVect[i].eta() << "\tphi: " << MatchedCaloJetsVect[i].phi() << "\tmass: " << MatchedCaloJetsVect[i].mass() << std::endl;
      //wait//std::cout << "number of CHS AK8 jets:  " << CHSFatJetsVect.size() << std::endl;
      //wait//for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) std::cout << "  AK8 jet  [" << i << "]\tpt: " << CHSFatJetsVect[i].pt() << "\teta: " << CHSFatJetsVect[i].eta() << "\tphi: " << CHSFatJetsVect[i].phi() << "\tmass: " << CHSFatJetsVect[i].mass() << std::endl;
    }



    //Vectors of structures
    //Here it doesn't know CHSJetsVect size, hence we cannot store a dynamic amount of things. Trying to do it inside Analyze method
    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) CHSJets.push_back( JetType() );
    //for(unsigned int i = 0; i < CaloJetsVect.size(); i++) CaloJets.push_back( CaloJetType() );
    //for(unsigned int i = 0; i < AllBarrelJetsVect.size(); i++) AllBarrelJets.push_back( JetType() );
    if (WriteAllJets) for(unsigned int i = 0; i < AllJetsVect.size(); i++) AllJets.push_back( JetType() );
    for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) VBFPairJets.push_back( JetType() );
    if (WriteFatJets) for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) CHSFatJets.push_back( FatJetType() );
    for(unsigned int i = 0; i < ggHJetVect.size(); i++) ggHJet.push_back( JetType() );
    if (isShort && isControl) {
      for(unsigned int i = 0; i < TightMuonVect.size(); i++) Muons.push_back( LeptonType() );
      for(unsigned int i = 0; i < TightElecVect.size(); i++) Electrons.push_back( LeptonType() );
    }
    if (isTracking) {
      // for(unsigned int i = 0; i < MuonVect.size(); i++) Muons.push_back( LeptonType() );
      for(unsigned int i = 0; i < TightMuonVect.size(); i++) TightMuons.push_back( LeptonType() );
      for(unsigned int i = 0; i < LooseMuonVect.size(); i++) LooseMuons.push_back( LeptonType() );
      for(unsigned int i = 0; i < TriggerMuonVect.size(); i++) Muons.push_back( LeptonType() );
      for(unsigned int i = 0; i < TightElecVect.size(); i++) Electrons.push_back( LeptonType() );
      for(unsigned int i = 0; i < LooseElecVect.size(); i++) LooseElectrons.push_back( LeptonType() );

    }
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Vertices
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "Vertices" << std::endl;
    PrimVertices.clear();
    SecVertices.clear();

    std::vector<reco::Vertex> PVertexVect;
    std::vector<reco::VertexCompositePtrCandidate> SVertexVect;

    PVertexVect = theVertexAnalyzer->FillPvVector(iEvent);
    SVertexVect = theVertexAnalyzer->FillSvVector(iEvent);

    for(unsigned int i = 0; i < PVertexVect.size(); i++) PrimVertices.push_back( VertexType() );
    for(unsigned int i = 0; i < SVertexVect.size(); i++) SecVertices.push_back( VertexType() );

    number_of_PV = PVertexVect.size();
    number_of_SV = SVertexVect.size();
    nSV = number_of_SV;


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // PFCandidates
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "PF candidates" << std::endl;
    PFCandidates.clear();

    // PFCandidate variables
    std::vector<pat::PackedCandidate> PFCandidateVect;
    std::vector<int> PFCandidateAK4JetIndex;
    std::vector<int> PFCandidateAK8JetIndex;
    std::vector<int> PFCandidateVtxIndex;

    BTagVertices.clear();

    std::vector<reco::CandSecondaryVertexTagInfo *> bTagInfoVect;
    std::vector<reco::CandIPTagInfo *> bTagIPInfoVect;
    std::vector<int> indexSVJet;

    PFCandidateVect = thePFCandidateAnalyzer->FillPFCandidateVector(iEvent);

    if (!isShort ||  WriteBtagInfos){
    // Initialize PFCandidate variables: Set indices to -1 (not matched)
    for(unsigned int i = 0; i < PFCandidateVect.size(); i++){
      PFCandidateAK4JetIndex.push_back(-1);
      PFCandidateAK8JetIndex.push_back(-1);
      PFCandidateVtxIndex.push_back(-1);

      nPFCandidates++;
      if(PFCandidateVect.at(i).charge()!=0) nPFCandidatesTrack++;
      if(PFCandidateVect.at(i).trackHighPurity()) nPFCandidatesHighPurityTrack++;
      if(PFCandidateVect.at(i).charge()!=0 && PFCandidateVect.at(i).pt() > 0.95) nPFCandidatesFullTrackInfo_pt++;//old
      if(PFCandidateVect.at(i).charge()!=0 && PFCandidateVect.at(i).pt() > 0.95 && PFCandidateVect.at(i).hasTrackDetails()) nPFCandidatesFullTrackInfo++;
      if(PFCandidateVect.at(i).charge()!=0 && PFCandidateVect.at(i).hasTrackDetails()) nPFCandidatesFullTrackInfo_hasTrackDetails++;
    }

    // PFCandidate matching to AK4 jets, AK8 jets and PV's
    unsigned int nPFCandidatesMatchedToAK4Jet = 0;
    unsigned int nPFCandidatesMatchedToAK8Jet = 0;
    unsigned int nPFCandidatesMatchedToAnyJet = 0;

    for(unsigned int i = 0; i < PFCandidateVect.size(); i++){

      int nMatchedAK4Jets = 0; // TODO: Remove if no warnings are observed during a large production.
      int nMatchedAK8Jets = 0;
      int nMatchedPVs = 0;

      // AK4 Jets
      for(unsigned int j = 0; j < CHSJetsVect.size(); j++){

	std::vector<edm::Ptr<reco::Candidate>> JetConstituentVect = CHSJetsVect[j].getJetConstituents();
	for(unsigned int k = 0; k < JetConstituentVect.size(); k++){

	  if (PFCandidateVect[i].p4() == JetConstituentVect[k]->p4()){
	    PFCandidateAK4JetIndex[i]=j;
	    nMatchedAK4Jets++;
	    nPFCandidatesMatchedToAK4Jet++;
            nPFCandidatesMatchedToAnyJet++;
	  }

	}

      }

      if (nMatchedAK4Jets > 1) edm::LogWarning("PFCandidate-Jet Matching") << "More than 1 AK4 jet contituent has been matched to PFCandidate";

      // AK8 Jets
      for(unsigned int j = 0; j < CHSFatJetsVect.size(); j++){

        std::vector<edm::Ptr<reco::Candidate>> JetConstituentVect = CHSFatJetsVect[j].getJetConstituents();
        for(unsigned int k = 0; k < JetConstituentVect.size(); k++){

          if (PFCandidateVect[i].p4() == JetConstituentVect[k]->p4()){
            PFCandidateAK8JetIndex[i]=j;
            nMatchedAK8Jets++;
            nPFCandidatesMatchedToAK8Jet++;
            nPFCandidatesMatchedToAnyJet++;
          }

        }

      }

      if (nMatchedAK8Jets > 1) edm::LogWarning("PFCandidate-Jet Matching") << "More than 1 AK8 jet contituent has been matched to PFCandidate";

      // PVs
      for(unsigned int j = 0; j < PVertexVect.size(); j++){

	if (PFCandidateVect[i].vertexRef()->position() == PVertexVect[j].position()){//was this expection?
	  PFCandidateVtxIndex[i]=j;
	  nMatchedPVs++;
	}
      }

      if (nMatchedPVs > 1) edm::LogWarning("PFCandidate-PV") << "WARNING: More than 1 PV has been matched to PFCandidate " << i << std::endl;

    }

    if(WriteAK4JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK8Jet; i++) PFCandidates.push_back( PFCandidateType() );
    if(WriteAK8JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK4Jet; i++) PFCandidates.push_back( PFCandidateType() );
    if(WriteAllJetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAnyJet; i++) PFCandidates.push_back( PFCandidateType() );
    if(WriteAllPFCandidates)    for(unsigned int i = 0; i < PFCandidateVect.size();       i++) PFCandidates.push_back( PFCandidateType() );


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // EXO-16-003 variables and and n(Pixel)Hits //TODO: Move to separate analyzer!
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    // AK4 jets
    for (unsigned int j = 0; j < CHSJetsVect.size(); j++){
      int jj = j;

      // Initialize jet variables from PFCandidates:
      float sumPtJet = 0.;
      std::vector<float> sumPtPV;
      std::vector<float> sigIP2D;
      std::vector<float> theta2D;
      std::vector<float> POCA_theta2D;
      std::vector<float> nPixelHits;
      std::vector<float> nHits;

      float alphaMax = -100.;
      float sigIP2DMedian = -100000.;
      float theta2DMedian = -100.;
      float POCA_theta2DMedian = -100.;
      float nPixelHitsMedian = -1.;
      float nHitsMedian = -1.;

      int nTracks0PixelHits = 0;
      int nTracks1PixelHit = 0;
      int nTracks2PixelHits = 0;
      int nTracks3PixelHits = 0;
      int nTracks4PixelHits = 0;
      int nTracks5PixelHits = 0;
      int nTracksAtLeast6PixelHits = 0;
      int nTracksValidHitInBPix1 = 0;
      int nTracks0LostInnerHits = 0;
      int nTracks1LostInnerHit = 0;
      int nTracksAtLeast2LostInnerHits = 0;

      // Initialize vertex variable
      for(unsigned int i = 0; i < PVertexVect.size(); i++) sumPtPV.push_back(0.);

      for (unsigned int i = 0; i < PFCandidateVect.size(); i++){
	if (jj == PFCandidateAK4JetIndex[i]){
	  if (PFCandidateVect[i].charge()){
	    sumPtJet += PFCandidateVect[i].pt();
	    sumPtPV[PFCandidateVtxIndex[i]] += PFCandidateVect[i].pt();
	    //sigIP2D.push_back(PFCandidateVect[i].dxy()/PFCandidateVect[i].dxyError()); //dxyError stored only for pT>0.95 (see below)
	    if (CHSJetsVect[j].hasTagInfo("pfSecondaryVertex")) {
	      reco::CandSecondaryVertexTagInfo const *svTagInfo = CHSJetsVect[j].tagInfoCandSecondaryVertex("pfSecondaryVertex");
	      if (svTagInfo->nVertices() > 0) {
		const GlobalVector &dir = svTagInfo->flightDirection(0);
		theta2D.push_back( std::acos( ( dir.x()*PFCandidateVect[i].px() + dir.y()*PFCandidateVect[i].py() ) /
					      ( std::sqrt(dir.x()*dir.x()+dir.y()*dir.y()) * PFCandidateVect[i].pt() ) ) );
	      }
	    }

            float px = PFCandidateVect[i].pt()*TMath::Cos(PFCandidateVect[i].phiAtVtx());
            float py = PFCandidateVect[i].pt()*TMath::Sin(PFCandidateVect[i].phiAtVtx());
            float vR = std::sqrt(PFCandidateVect[i].vx()*PFCandidateVect[i].vx() + PFCandidateVect[i].vy()*PFCandidateVect[i].vy());
            POCA_theta2D.push_back(std::acos((PFCandidateVect[i].vx()*px + PFCandidateVect[i].vy()*py) / (vR*PFCandidateVect[i].pt())));

	    // Full tracking info stored only for pT>0.95 GeV
	    // https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#Embedded_track_information
	    //if(PFCandidateVect[i].pt()>0.95) {//old, causing exceptions!
	    if(PFCandidateVect[i].pt()>0.95 && PFCandidateVect[i].hasTrackDetails()) {//this looks more conservative
	    //if(PFCandidateVect[i].hasTrackDetails()) {

              sigIP2D.push_back(PFCandidateVect[i].dxy()/PFCandidateVect[i].dxyError());

              nPixelHits.push_back(PFCandidateVect[i].numberOfPixelHits());
              nHits.push_back(PFCandidateVect[i].numberOfHits());

              if (PFCandidateVect[i].numberOfPixelHits() == 0) nTracks0PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 1) nTracks1PixelHit++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 2) nTracks2PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 3) nTracks3PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 4) nTracks4PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 5) nTracks5PixelHits++;
              else nTracksAtLeast6PixelHits++;

              if (PFCandidateVect[i].lostInnerHits() == -1) nTracksValidHitInBPix1++;
              else if (PFCandidateVect[i].lostInnerHits() == 0) nTracks0LostInnerHits++;
              else if (PFCandidateVect[i].lostInnerHits() == 1) nTracks1LostInnerHit++;
              else if (PFCandidateVect[i].lostInnerHits() == 2) nTracksAtLeast2LostInnerHits++;

            } // pT selection
	  } // charge
	} // jet index
      } // loop over PFCandidates

      // TODO: Implement a median function to use for all vectors below:

      if (sumPtPV.size() > 0) {
	std::sort(sumPtPV.begin(), sumPtPV.end());
	alphaMax = sumPtPV[sumPtPV.size()-1]/sumPtJet;
      }
      if (sigIP2D.size() > 0) {
	std::sort(sigIP2D.begin(), sigIP2D.end());
	if (sigIP2D.size() % 2 ==0) sigIP2DMedian = ((sigIP2D[sigIP2D.size()/2 -1] + sigIP2D[sigIP2D.size()/2]) /2);
	else sigIP2DMedian = sigIP2D[sigIP2D.size()/2];
      }
      if (theta2D.size() > 0) {
	std::sort(theta2D.begin(), theta2D.end());
	if (theta2D.size() % 2 ==0) theta2DMedian = ((theta2D[theta2D.size()/2 -1] + theta2D[theta2D.size()/2]) /2);
	else theta2DMedian = theta2D[theta2D.size()/2];
      }
      if (POCA_theta2D.size() > 0) {
        std::sort(POCA_theta2D.begin(), POCA_theta2D.end());
        if (POCA_theta2D.size() % 2 ==0) POCA_theta2DMedian = ((POCA_theta2D[POCA_theta2D.size()/2 -1] + POCA_theta2D[POCA_theta2D.size()/2]) /2);
        else POCA_theta2DMedian = POCA_theta2D[POCA_theta2D.size()/2];
      }
      if (nPixelHits.size() > 0) {
        std::sort(nPixelHits.begin(), nPixelHits.end());
        if (nPixelHits.size() % 2 ==0) nPixelHitsMedian = ((nPixelHits[nPixelHits.size()/2 -1] + nPixelHits[nPixelHits.size()/2]) /2);
        else nPixelHitsMedian = nPixelHits[nPixelHits.size()/2];
      }
      if (nHits.size() > 0) {
        std::sort(nHits.begin(), nHits.end());
        if (nHits.size() % 2 ==0) nHitsMedian = ((nHits[nHits.size()/2 -1] + nHits[nHits.size()/2]) /2);
        else nHitsMedian = nHits[nHits.size()/2];
      }

      if (CHSJetsVect[j].hasTagInfo("pfSecondaryVertex")) {
	reco::CandSecondaryVertexTagInfo const *svTagInfo = CHSJetsVect[j].tagInfoCandSecondaryVertex("pfSecondaryVertex");
	bTagInfoVect.push_back(svTagInfo->clone());
	reco::CandIPTagInfo const *ipTagInfo = CHSJetsVect[j].tagInfoCandIP("pfImpactParameter");
        bTagIPInfoVect.push_back(ipTagInfo->clone());
	indexSVJet.push_back(j);
      }

      CHSJetsVect[j].addUserFloat("alphaMaxOld", alphaMax);
      CHSJetsVect[j].addUserFloat("sigIP2DMedianOld", sigIP2DMedian);
      CHSJetsVect[j].addUserFloat("theta2DMedianOld", theta2DMedian);
      CHSJetsVect[j].addUserFloat("POCA_theta2DMedianOld", POCA_theta2DMedian);
      CHSJetsVect[j].addUserFloat("nPixelHitsMedianOld", nPixelHitsMedian);
      CHSJetsVect[j].addUserFloat("nHitsMedianOld", nHitsMedian);

      CHSJetsVect[j].addUserInt("nTracks0PixelHits", nTracks0PixelHits);
      CHSJetsVect[j].addUserInt("nTracks1PixelHit", nTracks1PixelHit);
      CHSJetsVect[j].addUserInt("nTracks2PixelHits", nTracks2PixelHits);
      CHSJetsVect[j].addUserInt("nTracks3PixelHits", nTracks3PixelHits);
      CHSJetsVect[j].addUserInt("nTracks4PixelHits", nTracks4PixelHits);
      CHSJetsVect[j].addUserInt("nTracks5PixelHits", nTracks5PixelHits);
      CHSJetsVect[j].addUserInt("nTracksAtLeast6PixelHits", nTracksAtLeast6PixelHits);
      CHSJetsVect[j].addUserInt("nTracksValidHitInBPix1", nTracksValidHitInBPix1);
      CHSJetsVect[j].addUserInt("nTracks0LostInnerHits", nTracks0LostInnerHits);
      CHSJetsVect[j].addUserInt("nTracks1LostInnerHit", nTracks1LostInnerHit);
      CHSJetsVect[j].addUserInt("nTracksAtLeast2LostInnerHits", nTracksAtLeast2LostInnerHits);

    }//end of EXO-16-003 variables for AK4 Jets

    // AK8 jets
    for (unsigned int j = 0; j < CHSFatJetsVect.size(); j++){
      int jj = j;

      // Initialize jet variables from PFCandidates:
      float sumPtJet = 0.;
      std::vector<float> sumPtPV;
      std::vector<float> sigIP2D;
      std::vector<float> theta2D;
      std::vector<float> POCA_theta2D;
      std::vector<float> nPixelHits;
      std::vector<float> nHits;

      float alphaMax = -100.;
      float sigIP2DMedian = -10000.;
      float theta2DMedian = -100.;
      float POCA_theta2DMedian = -100.;
      float nPixelHitsMedian = -1.;
      float nHitsMedian = -1.;

      int nTracks0PixelHits = 0;
      int nTracks1PixelHit = 0;
      int nTracks2PixelHits = 0;
      int nTracks3PixelHits = 0;
      int nTracks4PixelHits = 0;
      int nTracks5PixelHits = 0;
      int nTracksAtLeast6PixelHits = 0;
      int nTracksValidHitInBPix1 = 0;
      int nTracks0LostInnerHits = 0;
      int nTracks1LostInnerHit = 0;
      int nTracksAtLeast2LostInnerHits = 0;

      // Initialize vertex variable
      for(unsigned int i = 0; i < PVertexVect.size(); i++) sumPtPV.push_back(0.);

      for (unsigned int i = 0; i < PFCandidateVect.size(); i++){
        if (jj == PFCandidateAK8JetIndex[i]){
          if (PFCandidateVect[i].charge()){
            sumPtJet += PFCandidateVect[i].pt();
            sumPtPV[PFCandidateVtxIndex[i]] += PFCandidateVect[i].pt();
            //sigIP2D.push_back(PFCandidateVect[i].dxy()/PFCandidateVect[i].dxyError()); //dxyError stored only for pT>0.95 (see below)
            if (CHSFatJetsVect[j].hasTagInfo("pfSecondaryVertex")) {
              reco::CandSecondaryVertexTagInfo const *svTagInfo = CHSJetsVect[j].tagInfoCandSecondaryVertex("pfSecondaryVertex");
              if (svTagInfo->nVertices() > 0) {
                const GlobalVector &dir = svTagInfo->flightDirection(0);
                theta2D.push_back( std::acos( ( dir.x()*PFCandidateVect[i].px() + dir.y()*PFCandidateVect[i].py() ) /
                                              ( std::sqrt(dir.x()*dir.x()+dir.y()*dir.y()) * PFCandidateVect[i].pt() ) ) );
              }
            }

            float px = PFCandidateVect[i].pt()*TMath::Cos(PFCandidateVect[i].phiAtVtx());
            float py = PFCandidateVect[i].pt()*TMath::Sin(PFCandidateVect[i].phiAtVtx());
            float vR = std::sqrt(PFCandidateVect[i].vx()*PFCandidateVect[i].vx() + PFCandidateVect[i].vy()*PFCandidateVect[i].vy());
            POCA_theta2D.push_back(std::acos((PFCandidateVect[i].vx()*px + PFCandidateVect[i].vy()*py) / (vR*PFCandidateVect[i].pt())));

            // Full tracking info stored only for pT>0.95 GeV
            // https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#Embedded_track_information
            //if(PFCandidateVect[i].pt()>0.95) {//old, throwing exceptions
	    if(PFCandidateVect[i].pt()>0.95 && PFCandidateVect[i].hasTrackDetails()) {//this looks more conservative
	    //if(PFCandidateVect[i].hasTrackDetails()) {

              sigIP2D.push_back(PFCandidateVect[i].dxy()/PFCandidateVect[i].dxyError());

              nPixelHits.push_back(PFCandidateVect[i].numberOfPixelHits());
              nHits.push_back(PFCandidateVect[i].numberOfHits());

              if (PFCandidateVect[i].numberOfPixelHits() == 0) nTracks0PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 1) nTracks1PixelHit++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 2) nTracks2PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 3) nTracks3PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 4) nTracks4PixelHits++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 5) nTracks5PixelHits++;
              else nTracksAtLeast6PixelHits++;

              if (PFCandidateVect[i].lostInnerHits() == -1) nTracksValidHitInBPix1++;
              else if (PFCandidateVect[i].lostInnerHits() == 0) nTracks0LostInnerHits++;
              else if (PFCandidateVect[i].lostInnerHits() == 1) nTracks1LostInnerHit++;
              else if (PFCandidateVect[i].lostInnerHits() == 2) nTracksAtLeast2LostInnerHits++;

            } // pT selection
          } // charge
        } // jet index
      } // loop over PFCandidates

      // TODO: Implement a median function to use for all vectors below:

      if (sumPtPV.size() > 0) {
  std::sort(sumPtPV.begin(), sumPtPV.end());
  alphaMax = sumPtPV[sumPtPV.size()-1]/sumPtJet;
      }
      if (sigIP2D.size() > 0) {
  std::sort(sigIP2D.begin(), sigIP2D.end());
  if (sigIP2D.size() % 2 ==0) sigIP2DMedian = ((sigIP2D[sigIP2D.size()/2 -1] + sigIP2D[sigIP2D.size()/2]) /2);
  else sigIP2DMedian = sigIP2D[sigIP2D.size()/2];
      }
      if (theta2D.size() > 0) {
  std::sort(theta2D.begin(), theta2D.end());
  if (theta2D.size() % 2 ==0) theta2DMedian = ((theta2D[theta2D.size()/2 -1] + theta2D[theta2D.size()/2]) /2);
  else theta2DMedian = theta2D[theta2D.size()/2];
      }
      if (POCA_theta2D.size() > 0) {
        std::sort(POCA_theta2D.begin(), POCA_theta2D.end());
        if (POCA_theta2D.size() % 2 ==0) POCA_theta2DMedian = ((POCA_theta2D[POCA_theta2D.size()/2 -1] + POCA_theta2D[POCA_theta2D.size()/2]) /2);
        else POCA_theta2DMedian = POCA_theta2D[POCA_theta2D.size()/2];
      }
      if (nPixelHits.size() > 0) {
        std::sort(nPixelHits.begin(), nPixelHits.end());
        if (nPixelHits.size() % 2 ==0) nPixelHitsMedian = ((nPixelHits[nPixelHits.size()/2 -1] + nPixelHits[nPixelHits.size()/2]) /2);
        else nPixelHitsMedian = nPixelHits[nPixelHits.size()/2];
      }
      if (nHits.size() > 0) {
        std::sort(nHits.begin(), nHits.end());
        if (nHits.size() % 2 ==0) nHitsMedian = ((nHits[nHits.size()/2 -1] + nHits[nHits.size()/2]) /2);
        else nHitsMedian = nHits[nHits.size()/2];
      }

      // TODO: Is this needed for AK8?
      //if (CHSJetsVect[j].hasTagInfo("pfSecondaryVertex")) {
      //reco::CandSecondaryVertexTagInfo const *svTagInfo = CHSJetsVect[j].tagInfoCandSecondaryVertex("pfSecondaryVertex");
      //bTagInfoVect.push_back(svTagInfo->clone());
      //reco::CandIPTagInfo const *ipTagInfo = CHSJetsVect[j].tagInfoCandIP("pfImpactParameter");
      //bTagIPInfoVect.push_back(ipTagInfo->clone());
      //indexSVJet.push_back(j);


      CHSFatJetsVect[j].addUserFloat("alphaMaxOld", alphaMax);
      CHSFatJetsVect[j].addUserFloat("sigIP2DMedianOld", sigIP2DMedian);
      CHSFatJetsVect[j].addUserFloat("theta2DMedianOld", theta2DMedian);
      CHSFatJetsVect[j].addUserFloat("POCA_theta2DMedianOld", POCA_theta2DMedian);
      CHSFatJetsVect[j].addUserFloat("nPixelHitsMedianOld", nPixelHitsMedian);
      CHSFatJetsVect[j].addUserFloat("nHitsMedianOld", nHitsMedian);

      CHSFatJetsVect[j].addUserInt("nTracks0PixelHits", nTracks0PixelHits);
      CHSFatJetsVect[j].addUserInt("nTracks1PixelHit", nTracks1PixelHit);
      CHSFatJetsVect[j].addUserInt("nTracks2PixelHits", nTracks2PixelHits);
      CHSFatJetsVect[j].addUserInt("nTracks3PixelHits", nTracks3PixelHits);
      CHSFatJetsVect[j].addUserInt("nTracks4PixelHits", nTracks4PixelHits);
      CHSFatJetsVect[j].addUserInt("nTracks5PixelHits", nTracks5PixelHits);
      CHSFatJetsVect[j].addUserInt("nTracksAtLeast6PixelHits", nTracksAtLeast6PixelHits);
      CHSFatJetsVect[j].addUserInt("nTracksValidHitInBPix1", nTracksValidHitInBPix1);
      CHSFatJetsVect[j].addUserInt("nTracks0LostInnerHits", nTracks0LostInnerHits);
      CHSFatJetsVect[j].addUserInt("nTracks1LostInnerHit", nTracks1LostInnerHit);
      CHSFatJetsVect[j].addUserInt("nTracksAtLeast2LostInnerHits", nTracksAtLeast2LostInnerHits);

    }//end of EXO-16-003 variables for AK8 jets

    //Store vertex information for b-taging variables
    if(WriteBtagInfos){
      for (unsigned int i = 0; i < bTagInfoVect.size(); i++) BTagVertices.push_back(VertexType());
    }
    }//end of PFCandidates procedure, not needed for short lifetimes



    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // LostTracks (highPurity tracks not associated to any PFCandidate)
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "Lost tracks" << std::endl;

    LostTracks.clear();

    std::vector<pat::PackedCandidate> LostTrackVect;
    std::vector<int> LostTrackVtxIndex;

    if(WriteLostTracks)

      {
	LostTrackVect = thePFCandidateAnalyzer->FillLostTrackVector(iEvent);
	for(unsigned int i = 0; i < LostTrackVect.size(); i++) LostTracks.push_back( PFCandidateType() );

	// Matching
	for(unsigned int i = 0; i < LostTrackVect.size(); i++) LostTrackVtxIndex.push_back(-1); // Initialize indexes to -1 (not matched)

	for(unsigned int i = 0; i < LostTrackVect.size(); i++){

	  int nMatched = 0; // TODO: Remove if no warnings are observed during a large production.

	  // PVs
	  for(unsigned int j = 0; j < PVertexVect.size(); j++){

	    if (LostTrackVect[i].vertexRef()->position() == PVertexVect[j].position()){
	      LostTrackVtxIndex[i]=j;
	      nMatched++;
	    }
	  }

	  if (nMatched > 1) std::cout << "WARNING: More than 1 PV has been matched to LostTrack " << i << std::endl;

	}

      }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // ROI Tagger
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "ROI's" << std::endl;

    // TODO: Add this somewhere
    // vector<Float_t> ROIScores;
    // vector<Float_t> ROIDeltaR;
    // vector<Float_t> ROIDeltaPhi;
    // vector<Float_t> ROITrackClusterMultiplicity;
    // vector<Float_t> ROIAnnulusTrackMultiplicity;
    // vector<Float_t> ROIDistanceToLeadingLLP;
    // vector<Float_t> ROIDistanceToSubleadingLLP;

    // vector<Float_t> ROIAbsDeltaPhi; // Directly in ObjectsFormat
    // vector<Float_t> ROIDistanceToNearestLLP; // Directly in ObjectsFormat
    // vector<Bool_t> ROIMatchedToLeadingLLP; // Directly in ObjectsFormat
    // vector<Bool_t> ROIMatchedToSubleadingLLP; // Directly in ObjectsFormat

    if (isTracking && (WriteROITaggerScore || WriteROITaggerInputs)) {
      // Set tagger inputs in ROI analyzer
      theROIAnalyzer->SetAllTaggerInputVectors(iEvent);

      // Get ROIs
      RegionsOfInterest.clear();
      RegionsOfInterest = theROIAnalyzer->GetROIVector();
      nROIs = RegionsOfInterest.size();

      if(isVerbose) std::cout << "...inputs" << std::endl;

      // Get lower-level input objects for ntuple if needed
      if (WriteROITaggerInputs) {
        VerticesROI.clear();
        LostTracksROI.clear();
        PFCandidatesROI.clear();
        TrackClusters.clear();

        VerticesROI = theROIAnalyzer->GetVertexVector();
        LostTracksROI =  theROIAnalyzer->GetLostTrackVector();
        PFCandidatesROI = theROIAnalyzer->GetPFCandidateVector();
        TrackClusters = theROIAnalyzer->GetTrackClusterVector();
      }

      if(isVerbose) std::cout << "...outputs" << std::endl;

      // Get tagger score (now background instead of signal score)
      if (WriteROITaggerScore) {
        ROIs.clear();

        // if (!WriteROITaggerInputs) RegionsOfInterest.clear();
        ROIScores.clear();
        ROIDeltaR.clear();
        ROIDeltaPhi.clear();
        ROITrackClusterMultiplicity.clear();
        ROIAnnulusTrackMultiplicity.clear();
        ROIDistanceToLeadingLLP.clear();
        ROIDistanceToSubleadingLLP.clear();

        // theROIAnalyzer->SetTaggerScores(iEvent); //Done in SetAnalysisInfo (below)
        // theROIAnalyzer->SetOverlapRemovalInfo(); //Done in SetAnalysisInfo (below)

        if(isVerbose) std::cout << "...signal matching" << std::endl;

        // GenLLP positions
        math::XYZPoint leadingLLPPosition, subleadingLLPPosition;

        if (isSignal){

          if (GenLongLivedVect.at(0).pt() > GenLongLivedVect.at(1).pt()) {
            LeadingLLP = 0;
            leadingLLPPosition.SetXYZ(GenBquarksVect.at(0).vx(), GenBquarksVect.at(0).vy(), GenBquarksVect.at(0).vz());
            subleadingLLPPosition.SetXYZ(GenBquarksVect.at(2).vx(), GenBquarksVect.at(2).vy(), GenBquarksVect.at(2).vz());
          }

          else {
            LeadingLLP = 1;
            leadingLLPPosition.SetXYZ(GenBquarksVect.at(2).vx(), GenBquarksVect.at(2).vy(), GenBquarksVect.at(2).vz());
            subleadingLLPPosition.SetXYZ(GenBquarksVect.at(0).vx(), GenBquarksVect.at(0).vy(), GenBquarksVect.at(0).vz());
          }

          // theROIAnalyzer->SetGenMatchingInfo(isSignal, leadingLLPPosition, subleadingLLPPosition); //Done in SetAnalysisInfo (below)

        }

        if(isVerbose) std::cout << "...tagger score and analysis variables" << std::endl;

        theROIAnalyzer->SetAnalysisInfo(iEvent, isSignal, leadingLLPPosition, subleadingLLPPosition);

        // Get objects
        // if (!WriteROITaggerInputs) RegionsOfInterest = theROIAnalyzer->GetROIVector();
        ROIScores = theROIAnalyzer->GetTaggerScores();
        ROIDeltaR = theROIAnalyzer->GetDeltaRVector();
        ROIDeltaPhi = theROIAnalyzer->GetDeltaPhiVector();
        ROITrackClusterMultiplicity = theROIAnalyzer->GetTrackClusterMultiplicityVector();
        ROIAnnulusTrackMultiplicity = theROIAnalyzer->GetAnnulusTrackMultiplicityVector();
        ROIDistanceToLeadingLLP = theROIAnalyzer->GetDistanceToLeadingLLPVector();
        ROIDistanceToSubleadingLLP = theROIAnalyzer->GetDistanceToSubleadingLLPVector();

        LeadingROI = theROIAnalyzer->GetLeadingROIIndex();
        if (LeadingROI > -1) LeadingROIScore = TMath::Log10(ROIScores.at(LeadingROI));

        if(isVerbose) std::cout << "nROIs                = " << nROIs << std::endl;
        if(isVerbose) std::cout << "Leading ROI          = " << LeadingROI << std::endl;
        if(isVerbose) std::cout << "Leading ROI score    = " << LeadingROIScore << std::endl;

        SubleadingROI_dPhi2p0 = theROIAnalyzer->GetSubleadingROIIndex();
        (SubleadingROI_dPhi2p0 != -1) ? SubleadingROIScore_dPhi2p0 = TMath::Log10(ROIScores.at(SubleadingROI_dPhi2p0)) : 1.0;

        if(isVerbose) std::cout << "Subleading ROI       = " << SubleadingROI_dPhi2p0 << std::endl;
        if(isVerbose) std::cout << "Subleading ROI score = " << SubleadingROI_dPhi2p0 << std::endl;

        // Find most displaced jet
        MaxDisplacedJet = -1;
        float MaxDisplacement = 0;

        float thisJetPhi;
        float thisJetAbsDeltaPhiToLeadingROI;
        float thisJetAbsDeltaPhiToSubleadingROI;

        // Match jets to (sub)leading ROI
        for(uint thisJet = 0; thisJet < CHSJetsVect.size(); thisJet++) {
          thisJetPhi = CHSJetsVect.at(thisJet).phi();
          thisJetAbsDeltaPhiToLeadingROI = theROIAnalyzer->GetAbsDeltaPhiToLeadingROI(thisJetPhi);
          thisJetAbsDeltaPhiToSubleadingROI = theROIAnalyzer->GetAbsDeltaPhiToSubleadingROI(thisJetPhi);

          // Not needed (keep for future reference)
          // if ( thisJetDeltaPhiToLeadingROI < LeadingROI_dPhiNearestJet ) {
          //   LeadingROI_dPhiNearestJet = thisJetDeltaPhiToLeadingROI;
          //   LeadingROI_NearestJet = thisJet;
          // }

          // if ( thisJetDeltaPhiToSubleadingROI < SubleadingROI_dPhi2p0_dPhiNearestJet ) {
          //   SubleadingROI_dPhi2p0_dPhiNearestJet = thisJetDeltaPhiToSubleadingROI;
          //   SubleadingROI_dPhi2p0_NearestJet = thisJet;
          // }

          CHSJetsVect.at(thisJet).addUserFloat("absDeltaPhiToLeadingROI",thisJetAbsDeltaPhiToLeadingROI);
          CHSJetsVect.at(thisJet).addUserFloat("absDeltaPhiToSubleadingROI",thisJetAbsDeltaPhiToSubleadingROI);

          // For jets with valid 2D IP sig (i.e. with at least one PF candidate with track details)
          if ( CHSJetsVect.at(thisJet).hasUserFloat("sigIP2DMedianOld") && CHSJetsVect.at(thisJet).userFloat("sigIP2DMedianOld") != -10000 ) {
            // Find jet with the maximum |2D IP sig|
            if ( TMath::Abs(CHSJetsVect.at(thisJet).userFloat("sigIP2DMedianOld")) > MaxDisplacement) {
              MaxDisplacedJet = thisJet;
              MaxDisplacement =  TMath::Abs(CHSJetsVect.at(thisJet).userFloat("sigIP2DMedianOld"));
            }
          }
        }

        // // Displaced jet matching to leading ROI and non-overlapping subleading ROI
        // if (MaxDisplacedJet > -1) {
        //   if (nROIs > 0) {
        //     MaxDisplacedJet_dPhiLeadingROI = TMath::Abs(reco::deltaPhi(Jets->at(MaxDisplacedJet).phi, leadingROIPosition.phi()));
        //     if ( MaxDisplacedJet_dPhiLeadingROI < 0.4 ) MaxDisplacedJet_MatchedLeadingROI = 1;
        //   }
        //   if (SubleadingROI_dPhi2p0 != -1) {
        //     MaxDisplacedJet_dPhiSubleadingROI_dPhi2p0 = TMath::Abs(reco::deltaPhi(Jets->at(MaxDisplacedJet).phi, subleadingROIPosition.phi()));
        //     if ( MaxDisplacedJet_dPhiSubleadingROI_dPhi2p0 < 0.4 ) MaxDisplacedJet_MatchedSubleadingROI_dPhi2p0 = 1;
        //   }
        //   if ( MaxDisplacedJet_dPhiLeadingROI < MaxDisplacedJet_dPhiSubleadingROI_dPhi2p0 ) {
        //     MaxDisplacedJet_dPhiNearestTaggedROI = MaxDisplacedJet_dPhiLeadingROI;
        //     MaxDisplacedJet_dPhiUnmatchedTaggedROI = MaxDisplacedJet_dPhiSubleadingROI_dPhi2p0;
        //   }
        //   else {
        //     MaxDisplacedJet_dPhiNearestTaggedROI = MaxDisplacedJet_dPhiSubleadingROI_dPhi2p0;
        //     MaxDisplacedJet_dPhiUnmatchedTaggedROI = MaxDisplacedJet_dPhiLeadingROI;
        //   }
        //   MaxDisplacedJet_MatchedTaggedROI = MaxDisplacedJet_MatchedLeadingROI || MaxDisplacedJet_MatchedSubleadingROI_dPhi2p0;
        // }

        if (isVerbose) std::cout << "Vector sizes: " << RegionsOfInterest.size() << ", "
                                                     << ROIScores.size() << ", "
                                                     << ROIDeltaR.size() << ", " //FIXME!
                                                     << ROIDeltaPhi.size() << ", "//FIXME!
                                                     << ROITrackClusterMultiplicity.size() << ", "
                                                     << ROIAnnulusTrackMultiplicity.size() << ", "
                                                     << ROIDistanceToLeadingLLP.size() << ", "//FIXME!
                                                     << ROIDistanceToSubleadingLLP.size() << std::endl;//FIXME!

        for(unsigned int i = 0; i < RegionsOfInterest.size(); i++) ROIs.push_back( ROIType() );

      }
    }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // V0 candidates
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    if(isVerbose) std::cout << "V0 candidates" << std::endl;

    //------------------------------------------------------------------------------------------
    // KShorts
    //------------------------------------------------------------------------------------------

    KShorts.clear();

    std::vector<reco::VertexCompositePtrCandidate> KShortVect;

    KShortVect = theV0Analyzer->FillKShortVector(iEvent);

    // KShort properties
    KShortNMatchedROIs.clear();
    KShortLeadingMatchedROI.clear();
    KShortNearestMatchedROI.clear();
    KShortLeadingMatchedROIScore.clear();
    KShortNearestMatchedROIScore.clear();
    // KShortDistanceToNearestMatchedROI.clear();
    // KShortDistanceToLeadingMatchedROI.clear();
    KShortNearestMuon.clear();
    KShortDistanceToNearestMuon.clear();
    KShortNearestJet.clear();
    KShortAbsDeltaPhiToNearestJet.clear();
    KShortAbsDeltaPhiToMET.clear();

    if (WriteKShorts) {
        for (unsigned int thisKShort = 0; thisKShort < KShortVect.size(); thisKShort++) {
            math::XYZPoint thisKShortPosition(KShortVect.at(thisKShort).vx(), KShortVect.at(thisKShort).vy(), KShortVect.at(thisKShort).vz());

            // Compute 3D distance (R) to ROIs and add to matched if R < 1cm
            std::vector<int> thisKShortMatchedROIs;
            std::vector<float> thisKShortDistanceToMatchedROIs;

            for (unsigned int thisROI = 0; thisROI < RegionsOfInterest.size(); thisROI++) {
                math::XYZPoint thisROIPosition(RegionsOfInterest.at(thisROI).vx(), RegionsOfInterest.at(thisROI).vy(), RegionsOfInterest.at(thisROI).vz());

                math::XYZVector thisKShortVectorToThisROI = thisROIPosition - thisKShortPosition;

                float thisKShortDistanceToThisROI = thisKShortVectorToThisROI.R();

                if (thisKShortDistanceToThisROI < 1.0) {
                    thisKShortMatchedROIs.push_back(thisROI);
                    thisKShortDistanceToMatchedROIs.push_back(thisKShortDistanceToThisROI);
                }
            }

            // Matched ROIs: Find the leading (highest score) and the nearest (shortest 3D distance)
            int thisKShortNMatchedROIs = thisKShortMatchedROIs.size();

            if (thisKShortNMatchedROIs > 1) std::cout << "More than 1 ROI matched to KShort!!!" << std::endl;

            int thisKShortLeadingMatchedROI = -1;
            int thisKShortNearestMatchedROI = -1;
            float thisKShortLeadingMatchedROIScore = -1.;
            // float thisKShortNearestMatchedROIScore = -1.;
            // float thisKShortDistanceToLeadingMatchedROI = 99;
            float thisKShortDistanceToNearestMatchedROI = 99.;

            for (int thisMatchedROI = 0; thisMatchedROI < thisKShortNMatchedROIs; thisMatchedROI++) {
                if (ROIScores[thisKShortMatchedROIs[thisMatchedROI]] > thisKShortLeadingMatchedROIScore) {
                    thisKShortLeadingMatchedROI = thisKShortMatchedROIs[thisMatchedROI];
                    thisKShortLeadingMatchedROIScore = ROIScores[thisKShortMatchedROIs[thisMatchedROI]];
                }

                if (thisKShortDistanceToMatchedROIs[thisMatchedROI] < thisKShortDistanceToNearestMatchedROI) {
                    thisKShortNearestMatchedROI = thisKShortMatchedROIs[thisMatchedROI];
                    thisKShortDistanceToNearestMatchedROI = thisKShortDistanceToMatchedROIs[thisMatchedROI];
                }
            }

            KShortNMatchedROIs.push_back(thisKShortNMatchedROIs);

            KShortLeadingMatchedROI.push_back(thisKShortLeadingMatchedROI);
            KShortNearestMatchedROI.push_back(thisKShortNearestMatchedROI);

            KShortLeadingMatchedROIScore.push_back(thisKShortLeadingMatchedROIScore);
            KShortNearestMatchedROIScore.push_back(ROIScores[thisKShortNearestMatchedROI]);

            // Distance to nearest muon
            int thisKShortNearestMuon = -1;
            float thisKShortDistanceToNearestMuon = 99.;

            for(unsigned int thisTriggerMuon = 0; thisTriggerMuon < TriggerMuonVect.size(); thisTriggerMuon++) {
                // Get best track from muon
                reco::TrackRef thisMuonTrack = TriggerMuonVect[thisTriggerMuon].muonBestTrack();

                // Consider uniform 3.8T magnetic field
                const UniformMagneticField * const magneticField = new UniformMagneticField(3.8);

                // Get transient track
                reco::TransientTrack thisMuonTransientTrack(thisMuonTrack, magneticField);

                // Get muon trajectory's closest approach
                const auto &thisMuonPOCAToThisKaon = thisMuonTransientTrack.trajectoryStateClosestToPoint(GlobalPoint(thisKShortPosition.x(), thisKShortPosition.y(), thisKShortPosition.z()));

                // Get distance of closest approach
                math::XYZPoint thisMuonPosition(thisMuonPOCAToThisKaon.position().x(), thisMuonPOCAToThisKaon.position().y(), thisMuonPOCAToThisKaon.position().z());

                math::XYZVector thisKShortVectorToThisMuon = thisMuonPosition - thisKShortPosition;

                float thisKShortDistanceToThisMuon = thisKShortVectorToThisMuon.R();

                if (thisKShortDistanceToThisMuon < thisKShortDistanceToNearestMuon) {
                    thisKShortNearestMuon = thisTriggerMuon;
                    thisKShortDistanceToNearestMuon = thisKShortDistanceToThisMuon;
                }

            }

            KShortNearestMuon.push_back(thisKShortNearestMuon);
            KShortDistanceToNearestMuon.push_back(thisKShortDistanceToNearestMuon);

            // DeltaPhi to nearest jet
            int thisKShortNearestJet = -1;
            float thisKShortAbsDeltaPhiToNearestJet = 99.;

            for(unsigned int thisJet = 0; thisJet < CHSJetsVect.size(); thisJet++) {
                float thisKShortAbsDeltaPhiToThisJet = fabs(reco::deltaPhi(thisKShortPosition.phi(), CHSJetsVect[thisJet].phi()));
                if ( thisKShortAbsDeltaPhiToThisJet < thisKShortAbsDeltaPhiToNearestJet) {
                    thisKShortNearestJet = thisJet;
                    thisKShortAbsDeltaPhiToNearestJet = thisKShortAbsDeltaPhiToThisJet;
                }
            }

            KShortNearestJet.push_back(thisKShortNearestJet);
            KShortAbsDeltaPhiToNearestJet.push_back(thisKShortAbsDeltaPhiToNearestJet);

            // DeltaPhi to MET
            float thisKShortAbsDeltaPhiToMET = fabs(reco::deltaPhi(thisKShortPosition.phi(), MET.phi()));
            KShortAbsDeltaPhiToMET.push_back(thisKShortAbsDeltaPhiToMET);
        }
    }

    for(unsigned int i = 0; i < KShortVect.size(); i++) KShorts.push_back( V0Type() );

    nKShorts = KShorts.size();


    //------------------------------------------------------------------------------------------
    // Lambdas
    //------------------------------------------------------------------------------------------

    Lambdas.clear();

    std::vector<reco::VertexCompositePtrCandidate> LambdaVect;

    LambdaVect = theV0Analyzer->FillLambdaVector(iEvent);


    // Lambda properties
    LambdaNMatchedROIs.clear();
    LambdaLeadingMatchedROI.clear();
    LambdaNearestMatchedROI.clear();
    LambdaLeadingMatchedROIScore.clear();
    LambdaNearestMatchedROIScore.clear();
    // LambdaDistanceToNearestMatchedROI.clear();
    // LambdaDistanceToLeadingMatchedROI.clear();
    LambdaNearestMuon.clear();
    LambdaDistanceToNearestMuon.clear();
    LambdaNearestJet.clear();
    LambdaAbsDeltaPhiToNearestJet.clear();
    LambdaAbsDeltaPhiToMET.clear();

    if (WriteLambdas) {
        for (unsigned int thisLambda = 0; thisLambda < LambdaVect.size(); thisLambda++) {
            math::XYZPoint thisLambdaPosition(LambdaVect.at(thisLambda).vx(), LambdaVect.at(thisLambda).vy(), LambdaVect.at(thisLambda).vz());

            // Compute 3D distance (R) to ROIs and add to matched if R < 1cm
            std::vector<int> thisLambdaMatchedROIs;
            std::vector<float> thisLambdaDistanceToMatchedROIs;

            for (unsigned int thisROI = 0; thisROI < RegionsOfInterest.size(); thisROI++) {
                math::XYZPoint thisROIPosition(RegionsOfInterest.at(thisROI).vx(), RegionsOfInterest.at(thisROI).vy(), RegionsOfInterest.at(thisROI).vz());

                math::XYZVector thisLambdaVectorToThisROI = thisROIPosition - thisLambdaPosition;

                float thisLambdaDistanceToThisROI = thisLambdaVectorToThisROI.R();

                if (thisLambdaDistanceToThisROI < 1.0) {
                    thisLambdaMatchedROIs.push_back(thisROI);
                    thisLambdaDistanceToMatchedROIs.push_back(thisLambdaDistanceToThisROI);
                }
            }

            // Matched ROIs: Find the leading (highest score) and the nearest (shortest 3D distance)
            int thisLambdaNMatchedROIs = thisLambdaMatchedROIs.size();

            if (thisLambdaNMatchedROIs > 1) std::cout << "More than 1 ROI matched to Lambda!!!" << std::endl;

            int thisLambdaLeadingMatchedROI = -1;
            int thisLambdaNearestMatchedROI = -1;
            float thisLambdaLeadingMatchedROIScore = -1.;
            // float thisLambdaNearestMatchedROIScore = -1.;
            // float thisLambdaDistanceToLeadingMatchedROI = 99;
            float thisLambdaDistanceToNearestMatchedROI = 99.;

            for (int thisMatchedROI = 0; thisMatchedROI < thisLambdaNMatchedROIs; thisMatchedROI++) {
                if (ROIScores[thisLambdaMatchedROIs[thisMatchedROI]] > thisLambdaLeadingMatchedROIScore) {
                    thisLambdaLeadingMatchedROI = thisLambdaMatchedROIs[thisMatchedROI];
                    thisLambdaLeadingMatchedROIScore = ROIScores[thisLambdaMatchedROIs[thisMatchedROI]];
                }

                if (thisLambdaDistanceToMatchedROIs[thisMatchedROI] < thisLambdaDistanceToNearestMatchedROI) {
                    thisLambdaNearestMatchedROI = thisLambdaMatchedROIs[thisMatchedROI];
                    thisLambdaDistanceToNearestMatchedROI = thisLambdaDistanceToMatchedROIs[thisMatchedROI];
                }
            }

            LambdaNMatchedROIs.push_back(thisLambdaNMatchedROIs);

            LambdaLeadingMatchedROI.push_back(thisLambdaLeadingMatchedROI);
            LambdaNearestMatchedROI.push_back(thisLambdaNearestMatchedROI);

            LambdaLeadingMatchedROIScore.push_back(thisLambdaLeadingMatchedROIScore);
            LambdaNearestMatchedROIScore.push_back(ROIScores[thisLambdaNearestMatchedROI]);

            // Distance to nearest muon
            int thisLambdaNearestMuon = -1;
            float thisLambdaDistanceToNearestMuon = 99.;

            for(unsigned int thisTriggerMuon = 0; thisTriggerMuon < TriggerMuonVect.size(); thisTriggerMuon++) {
                // Get best track from muon
                reco::TrackRef thisMuonTrack = TriggerMuonVect[thisTriggerMuon].muonBestTrack();

                // Consider uniform 3.8T magnetic field
                const UniformMagneticField * const magneticField = new UniformMagneticField(3.8);

                // Get transient track
                reco::TransientTrack thisMuonTransientTrack(thisMuonTrack, magneticField);

                // Get muon trajectory's closest approach
                const auto &thisMuonPOCAToThisKaon = thisMuonTransientTrack.trajectoryStateClosestToPoint(GlobalPoint(thisLambdaPosition.x(), thisLambdaPosition.y(), thisLambdaPosition.z()));

                // Get distance of closest approach
                math::XYZPoint thisMuonPosition(thisMuonPOCAToThisKaon.position().x(), thisMuonPOCAToThisKaon.position().y(), thisMuonPOCAToThisKaon.position().z());

                math::XYZVector thisLambdaVectorToThisMuon = thisMuonPosition - thisLambdaPosition;

                float thisLambdaDistanceToThisMuon = thisLambdaVectorToThisMuon.R();

                if (thisLambdaDistanceToThisMuon < thisLambdaDistanceToNearestMuon) {
                    thisLambdaNearestMuon = thisTriggerMuon;
                    thisLambdaDistanceToNearestMuon = thisLambdaDistanceToThisMuon;
                }

            }

            LambdaNearestMuon.push_back(thisLambdaNearestMuon);
            LambdaDistanceToNearestMuon.push_back(thisLambdaDistanceToNearestMuon);

            // DeltaPhi to nearest jet
            int thisLambdaNearestJet = -1;
            float thisLambdaAbsDeltaPhiToNearestJet = 99.;

            for(unsigned int thisJet = 0; thisJet < CHSJetsVect.size(); thisJet++) {
                float thisLambdaAbsDeltaPhiToThisJet = fabs(reco::deltaPhi(thisLambdaPosition.phi(), CHSJetsVect[thisJet].phi()));
                if ( thisLambdaAbsDeltaPhiToThisJet < thisLambdaAbsDeltaPhiToNearestJet) {
                    thisLambdaNearestJet = thisJet;
                    thisLambdaAbsDeltaPhiToNearestJet = thisLambdaAbsDeltaPhiToThisJet;
                }
            }

            LambdaNearestJet.push_back(thisLambdaNearestJet);
            LambdaAbsDeltaPhiToNearestJet.push_back(thisLambdaAbsDeltaPhiToNearestJet);

            // DeltaPhi to MET
            float thisLambdaAbsDeltaPhiToMET = fabs(reco::deltaPhi(thisLambdaPosition.phi(), MET.phi()));
            LambdaAbsDeltaPhiToMET.push_back(thisLambdaAbsDeltaPhiToMET);
        }
    }

    for(unsigned int i = 0; i < LambdaVect.size(); i++) Lambdas.push_back( V0Type() );

    nLambdas = Lambdas.size();

    // ---------- Fill objects ----------
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

    ObjectsFormat::FillMEtType(MEt, &MET, isMC);
    for(unsigned int i = 0; i < CHSJetsVect.size(); i++){
      ObjectsFormat::FillJetType(CHSJets[i], &CHSJetsVect[i], isMC);//Remove CHSJets.size(), testing
    }

    for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++){
      ObjectsFormat::FillJetType(VBFPairJets[i], &VBFPairJetsVect[i], isMC);//nullFloat[i], nullFloat[i], nullFloat[i]);
    }

    for(unsigned int i = 0; i < ggHJetVect.size(); i++) ObjectsFormat::FillJetType(ggHJet[i], &ggHJetVect[i], isMC);

    //for(unsigned int i = 0; i < AllBarrelJetsVect.size(); i++){
    //ObjectsFormat::FillJetType(AllBarrelJets[i], &AllBarrelJetsVect[i], isMC, 0., 0., 0.);
    //}

    if (WriteAllJets) for(unsigned int i = 0; i < AllJetsVect.size(); i++){
      ObjectsFormat::FillJetType(AllJets[i], &AllJetsVect[i], isMC);
    }


    //if (isSignal) for(unsigned int i = 0; i < CaloJetsVect.size(); i++){ ObjectsFormat::FillCaloJetType(CaloJets[i], &CaloJetsVect[i], isMC, caloGenMatched[i]);}

    if (WriteFatJets) for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) ObjectsFormat::FillFatJetType(CHSFatJets[i], &CHSFatJetsVect[i], SoftdropPuppiMassString, isMC);//Remove CHSFatJets.size(), testin
    //if (WriteNFatJets>0) for(unsigned int i = 0; i < CHSFatJetsVect.size() && i < CHSFatJets.size(); i++) ObjectsFormat::FillFatJetType(CHSFatJets[i], &CHSFatJetsVect[i], SoftdropPuppiMassString, isMC);//Remove CHSFatJets.size(), testing
    for(unsigned int i = 0; i < MatchedCHSJets.size() && i < MatchedCHSJetsVect.size(); i++) ObjectsFormat::FillJetType(MatchedCHSJets[i], &MatchedCHSJetsVect[i], isMC);// List/Reset JetType functions missing several attributes. Please check before using!
    //for(unsigned int i = 0; i < MatchedCaloJets.size() && i < MatchedCaloJetsVect.size(); i++) ObjectsFormat::FillCaloJetType(MatchedCaloJets[i], &MatchedCaloJetsVect[i], isMC, true);
    if (WriteGenVBFquarks) for(unsigned int i = 0; i < GenVBFVect.size(); i++) ObjectsFormat::FillGenPType(GenVBFquarks[i], &GenVBFVect[i]);
    if (WriteGenHiggs) for(unsigned int i = 0; i < GenHiggsVect.size(); i++) ObjectsFormat::FillGenPType(GenHiggs[i], &GenHiggsVect[i]);
    if (WriteGenLLPs) for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) ObjectsFormat::FillGenPType(GenLLPs[i], &GenLongLivedVect[i]);
    if (WriteGenBquarks) for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillGenPType(GenBquarks[i], &GenBquarksVect[i]);
    if (WriteGenMuons) for(unsigned int i = 0; i < GenMuonsVect.size(); i++) ObjectsFormat::FillGenPType(GenMuons[i], &GenMuonsVect[i]);
    if (isShort && isControl){
      for(unsigned int i = 0; i < Muons.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &TightMuonVect[i], isMC);
      for(unsigned int i = 0; i < Electrons.size(); i++) ObjectsFormat::FillElectronType(Electrons[i], &TightElecVect[i], isMC);
    }
    if (isTracking) {
      // for(unsigned int i = 0; i < Muons.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &MuonVect[i], isMC);
      for(unsigned int i = 0; i < TightMuons.size(); i++) ObjectsFormat::FillMuonType(TightMuons[i], &TightMuonVect[i], isMC);
      for(unsigned int i = 0; i < LooseMuons.size(); i++) ObjectsFormat::FillMuonType(LooseMuons[i], &LooseMuonVect[i], isMC);
      for(unsigned int i = 0; i < Muons.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &TriggerMuonVect[i], isMC);
      for(unsigned int i = 0; i < Electrons.size(); i++) ObjectsFormat::FillElectronType(Electrons[i], &TightElecVect[i], isMC);
      for(unsigned int i = 0; i < LooseElectrons.size(); i++) ObjectsFormat::FillElectronType(LooseElectrons[i], &LooseElecVect[i], isMC);

    }
    // else{
    //   if(isZtoMM || isWtoMN) for(unsigned int i = 0; i < Muons.size() && i < TightMuonVect.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &TightMuonVect[i], isMC);
    //   else if(isZtoEE || isWtoEN) for(unsigned int i = 0; i < Electrons.size() && i < TightElecVect.size(); i++) ObjectsFormat::FillElectronType(Electrons[i], &TightElecVect[i], isMC);
    //   else if(isTtoEM)
    //   {
    //     for(unsigned int i = 0; i < Electrons.size() && i < TightElecVect.size(); i++) ObjectsFormat::FillElectronType(Electrons[i], &TightElecVect[i], isMC);
    //     for(unsigned int i = 0; i < Muons.size() && i < TightMuonVect.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &TightMuonVect[i], isMC);
    //   }
    // }
    ObjectsFormat::FillCandidateType(VBF, &theVBF, isMC);
    if (isControl) {
      if (isTracking) {
        if (isZtoMM || isZtoEE) ObjectsFormat::FillCandidateType(Z, &theZ, isMC);
        if (isWtoMN || isWtoEN) ObjectsFormat::FillCandidateType(W, &theW, isMC);
      }
      else {
        ObjectsFormat::FillCandidateType(Z, &theZ, isMC);
        ObjectsFormat::FillCandidateType(W, &theW, isMC);
      }
    }

    HDiCHS = theHDiCHS.mass();
    HTriCHS = theHTriCHS.mass();
    HQuadCHS = theHQuadCHS.mass();
    HDiCHSMatched = theHDiCHSMatched.mass();
    HTriCHSMatched = theHTriCHSMatched.mass();
    HQuadCHSMatched = theHQuadCHSMatched.mass();

    //HDiCalo = theHDiCalo.mass();
    //HTriCalo = theHTriCalo.mass();
    //HQuadCalo = theHQuadCalo.mass();
    //HDiCaloMatched = theHDiCaloMatched.mass();
    //HTriCaloMatched = theHTriCaloMatched.mass();
    //HQuadCaloMatched = theHQuadCaloMatched.mass();

    if (WriteVertices) for(unsigned int i = 0; i < PVertexVect.size(); i++) ObjectsFormat::FillPrimVertexType(PrimVertices[i], &PVertexVect[i]);
    if (WriteVertices) for(unsigned int i = 0; i < SVertexVect.size(); i++) {
	ObjectsFormat::FillSecVertexType(SecVertices[i], &SVertexVect[i]);
      }
    //if(WriteAllPFCandidates) for(unsigned int i = 0; i < PFCandidateVect.size(); i++) ObjectsFormat::FillPFCandidateType(PFCandidates[i], &PFCandidateVect[i], PFCandidateAK4JetIndex[i], PFCandidateVtxIndex[i]);
    if(WriteAK4JetPFCandidates || WriteAK8JetPFCandidates || WriteAllJetPFCandidates || WriteAllPFCandidates) {
    	int iAK4JetPFCand = 0;
      int iAK8JetPFCand = 0;
      int iAnyJetPFCand = 0;
	    for(unsigned int i = 0; i < PFCandidateVect.size(); i++) {
     	  if(WriteAK4JetPFCandidates && PFCandidateAK4JetIndex[i] != -1)	{
	        ObjectsFormat::FillPFCandidateType(PFCandidates[iAK4JetPFCand], &PFCandidateVect[i], PFCandidateAK4JetIndex[i], PFCandidateAK8JetIndex[i], PFCandidateVtxIndex[i]);
	        iAK4JetPFCand++;
	      }
        else if(WriteAK8JetPFCandidates && PFCandidateAK8JetIndex[i] != -1)	{
          ObjectsFormat::FillPFCandidateType(PFCandidates[iAK8JetPFCand], &PFCandidateVect[i], PFCandidateAK4JetIndex[i], PFCandidateAK8JetIndex[i], PFCandidateVtxIndex[i]);
          iAK8JetPFCand++;
        }
        else if(WriteAllJetPFCandidates && (PFCandidateAK4JetIndex[i] != -1 || PFCandidateAK8JetIndex[i] != -1)) {
          ObjectsFormat::FillPFCandidateType(PFCandidates[iAnyJetPFCand], &PFCandidateVect[i], PFCandidateAK4JetIndex[i], PFCandidateAK8JetIndex[i], PFCandidateVtxIndex[i]);
          iAnyJetPFCand++;
        }
        else if(WriteAllPFCandidates) {
          ObjectsFormat::FillPFCandidateType(PFCandidates[i], &PFCandidateVect[i], PFCandidateAK4JetIndex[i], PFCandidateAK8JetIndex[i], PFCandidateVtxIndex[i]);
        }
	    }
    }
    if (WriteLostTracks) for(unsigned int i = 0; i < LostTrackVect.size(); i++) ObjectsFormat::FillPFCandidateType(LostTracks[i], &LostTrackVect[i], -1, -1, LostTrackVtxIndex[i]); // Not matched to any jet
    if (WriteBtagInfos){
      for(unsigned int i = 0; i < bTagInfoVect.size(); i++){
	for (unsigned int idx = 0; idx < bTagInfoVect.at(i)->nVertices(); idx++) {
	    float dRSVJet = reco::deltaR(bTagInfoVect.at(i)->secondaryVertex(idx).eta(),bTagInfoVect.at(i)->secondaryVertex(idx).phi(),CHSJetsVect[indexSVJet.at(i)].eta(), CHSJetsVect[indexSVJet.at(i)].phi());
	    ObjectsFormat::FillBtagSecVertexType(BTagVertices[i], bTagInfoVect.at(i), bTagIPInfoVect.at(i), idx, dRSVJet, indexSVJet.at(i));
	}
      }
    }

    if (isTracking && WriteROITaggerScore) {
      for(unsigned int i = 0; i < ROIScores.size(); i++){
        ObjectsFormat::FillROIType(ROIs[i], &RegionsOfInterest[i], ROIScores[i], ROIDeltaR[i], ROIDeltaPhi[i], ROITrackClusterMultiplicity[i], ROIAnnulusTrackMultiplicity[i], ROIDistanceToLeadingLLP[i], ROIDistanceToSubleadingLLP[i]);
      }
    }

    if (WriteKShorts) for(unsigned int i = 0; i < KShortVect.size(); i++) ObjectsFormat::FillV0Type(KShorts[i], &KShortVect[i], KShortNMatchedROIs[i], KShortLeadingMatchedROI[i], KShortNearestMatchedROI[i], KShortLeadingMatchedROIScore[i], KShortNearestMatchedROIScore[i], KShortNearestMuon[i], KShortDistanceToNearestMuon[i], KShortNearestJet[i], KShortAbsDeltaPhiToNearestJet[i], KShortAbsDeltaPhiToMET[i]);
    if (WriteLambdas) for(unsigned int i = 0; i < LambdaVect.size(); i++) ObjectsFormat::FillV0Type(Lambdas[i], &LambdaVect[i], LambdaNMatchedROIs[i], LambdaLeadingMatchedROI[i], LambdaNearestMatchedROI[i], LambdaLeadingMatchedROIScore[i], LambdaNearestMatchedROIScore[i], LambdaNearestMuon[i], LambdaDistanceToNearestMuon[i], LambdaNearestJet[i], LambdaAbsDeltaPhiToNearestJet[i], LambdaAbsDeltaPhiToMET[i]);

    if(isVerbose) std::cout << "TREE FILL!" << std::endl;
    tree -> Fill();
    if(isVerbose) std::cout << "TREE FILLED!!!!!!!!!!!! Go to next event...--->" << std::endl;

}



// // ------------ method to calculate Nsubjettiness for only charged and/or neutral constituents -----------------
void
Ntuplizer::calcNsubjettiness(const pat::Jet & jet, float & tau1_neutral, float & tau1_charged, float & tau2_neutral, float & tau2_charged, std::vector<fastjet::PseudoJet> & currentAxes) const
{
  std::vector<fastjet::PseudoJet> fjParticles_neutral;
  std::vector<fastjet::PseudoJet> fjParticles_charged;

  // loop over jet constituents and push them in the vector of FastJet constituents
  for(const reco::CandidatePtr & daughter : jet.daughterPtrVector())
    {
      if ( daughter.isNonnull() && daughter.isAvailable() )
	{
	  const reco::Jet * subjet = dynamic_cast<const reco::Jet *>(daughter.get());
	  // if the daughter is actually a subjet
	  if( subjet && daughter->numberOfDaughters() > 1 )
	    {
	      // loop over subjet constituents and push them in the vector of FastJet constituents
	      for(size_t i=0; i<daughter->numberOfDaughters(); ++i)
		{
		  const reco::Candidate * constit = daughter->daughter(i);

		  if ( constit ){
		    if (constit->charge())
		      fjParticles_charged.push_back( fastjet::PseudoJet( constit->px(), constit->py(), constit->pz(), constit->energy() ) );
		    else
		      fjParticles_neutral.push_back( fastjet::PseudoJet( constit->px(), constit->py(), constit->pz(), constit->energy() ) );
		  }
		  else
		    edm::LogWarning("MissingJetConstituent") << "Jet constituent required for N-subjettiness computation is missing!";
		}
	    }
	  else{
	    if (daughter->charge())
	      fjParticles_charged.push_back( fastjet::PseudoJet( daughter->px(), daughter->py(), daughter->pz(), daughter->energy() ) );
	    else
	      fjParticles_neutral.push_back( fastjet::PseudoJet( daughter->px(), daughter->py(), daughter->pz(), daughter->energy() ) );

	  }
	}
      else
	edm::LogWarning("MissingJetConstituent") << "Jet constituent required for N-subjettiness computation is missing!";
    }

  // N-subjettiness calculator
  fastjet::contrib::Njettiness njettiness(fastjet::contrib::OnePass_KT_Axes(), fastjet::contrib::NormalizedMeasure(1.0,0.4));

  // calculate N-subjettiness
  tau1_neutral = njettiness.getTau(1, fjParticles_neutral);
  tau2_neutral = njettiness.getTau(2, fjParticles_neutral);
  tau1_charged = njettiness.getTau(1, fjParticles_charged);
  tau2_charged = njettiness.getTau(2, fjParticles_charged);
  currentAxes = njettiness.currentAxes();
}


// ------------ method called once each job just before starting event loop  ------------
void
Ntuplizer::beginJob()
{

    std::cout << "BEGIN JOB!" << std::endl;

    //Tree branches
    tree = fs->make<TTree>("tree", "tree");
    tree -> Branch("isMC" , &isMC, "isMC/O");
    tree -> Branch("EventNumber" , &EventNumber , "EventNumber/L");
    tree -> Branch("LumiNumber" , &LumiNumber , "LumiNumber/L");
    tree -> Branch("RunNumber" , &RunNumber , "RunNumber/L");
    tree -> Branch("EventWeight", &EventWeight, "EventWeight/F");
    tree -> Branch("GenEventWeight", &GenEventWeight, "GenEventWeight/F");
    tree -> Branch("PUWeight", &PUWeight, "PUWeight/F");
    tree -> Branch("PUWeightUp", &PUWeightUp, "PUWeightUp/F");
    tree -> Branch("PUWeightDown", &PUWeightDown, "PUWeightDown/F");
    if (isTracking && is2018) {
      tree -> Branch("PUWeight_HLT_Mu7_IP4", &PUWeight_HLT_Mu7_IP4, "PUWeight_HLT_Mu7_IP4/F");
      tree -> Branch("PUWeightUp_HLT_Mu7_IP4", &PUWeightUp_HLT_Mu7_IP4, "PUWeightUp_HLT_Mu7_IP4/F");
      tree -> Branch("PUWeightDown_HLT_Mu7_IP4", &PUWeightDown_HLT_Mu7_IP4, "PUWeightDown_HLT_Mu7_IP4/F");
      tree -> Branch("PUWeight_HLT_Mu9_IP6", &PUWeight_HLT_Mu9_IP6, "PUWeight_HLT_Mu9_IP6/F");
      tree -> Branch("PUWeightUp_HLT_Mu9_IP6", &PUWeightUp_HLT_Mu9_IP6, "PUWeightUp_HLT_Mu9_IP6/F");
      tree -> Branch("PUWeightDown_HLT_Mu9_IP6", &PUWeightDown_HLT_Mu9_IP6, "PUWeightDown_HLT_Mu9_IP6/F");
      tree -> Branch("PUWeight_HLT_Mu12_IP6", &PUWeight_HLT_Mu12_IP6, "PUWeight_HLT_Mu12_IP6/F");
      tree -> Branch("PUWeightUp_HLT_Mu12_IP6", &PUWeightUp_HLT_Mu12_IP6, "PUWeightUp_HLT_Mu12_IP6/F");
      tree -> Branch("PUWeightDown_HLT_Mu12_IP6", &PUWeightDown_HLT_Mu12_IP6, "PUWeightDown_HLT_Mu12_IP6/F");
      tree -> Branch("PUWeight_HLT_Mu9_IP6_v6", &PUWeight_HLT_Mu9_IP6_v6, "PUWeight_HLT_Mu9_IP6_v6/F");
      tree -> Branch("PUWeightUp_HLT_Mu9_IP6_v6", &PUWeightUp_HLT_Mu9_IP6_v6, "PUWeightUp_HLT_Mu9_IP6_v6/F");
      tree -> Branch("PUWeightDown_HLT_Mu9_IP6_v6", &PUWeightDown_HLT_Mu9_IP6_v6, "PUWeightDown_HLT_Mu9_IP6_v6/F");
    }
    if (isControl){
      if (isShort) {
        tree -> Branch("EventWeight_leptonSF", &EventWeight_leptonSF, "EventWeight_leptonSF/F");
        tree -> Branch("EventWeight_leptonSFUp", &EventWeight_leptonSFUp, "EventWeight_leptonSFUp/F");
        tree -> Branch("EventWeight_leptonSFDown", &EventWeight_leptonSFDown, "EventWeight_leptonSFDown/F");
      }
      tree -> Branch("LeptonWeight", &LeptonWeight, "LeptonWeight/F");
      tree -> Branch("LeptonWeightUp", &LeptonWeightUp, "LeptonWeightUp/F");
      tree -> Branch("LeptonWeightDown", &LeptonWeightDown, "LeptonWeightDown/F");
    }
    if (isShort){
      tree -> Branch("bTagWeight_central", &bTagWeight_central, "bTagWeight_central/F");
      tree -> Branch("bTagWeight_jesup", &bTagWeight_jesup, "bTagWeight_jesup/F");
      tree -> Branch("bTagWeight_jesdown", &bTagWeight_jesdown, "bTagWeight_jesdown/F");
      tree -> Branch("bTagWeight_lfup", &bTagWeight_lfup, "bTagWeight_lfup/F");
      tree -> Branch("bTagWeight_lfdown", &bTagWeight_lfdown, "bTagWeight_lfdown/F");
      tree -> Branch("bTagWeight_hfup", &bTagWeight_hfup, "bTagWeight_hfup/F");
      tree -> Branch("bTagWeight_hfdown", &bTagWeight_hfdown, "bTagWeight_hfdown/F");
      tree -> Branch("bTagWeight_hfstats1up", &bTagWeight_hfstats1up, "bTagWeight_hfstats1up/F");
      tree -> Branch("bTagWeight_hfstats1down", &bTagWeight_hfstats1down, "bTagWeight_hfstats1down/F");
      tree -> Branch("bTagWeight_hfstats2up", &bTagWeight_hfstats2up, "bTagWeight_hfstats2up/F");
      tree -> Branch("bTagWeight_hfstats2down", &bTagWeight_hfstats2down, "bTagWeight_hfstats2down/F");
      tree -> Branch("bTagWeight_lfstats1up", &bTagWeight_lfstats1up, "bTagWeight_lfstats1up/F");
      tree -> Branch("bTagWeight_lfstats1down", &bTagWeight_lfstats1down, "bTagWeight_lfstats1down/F");
      tree -> Branch("bTagWeight_lfstats2up", &bTagWeight_lfstats2up, "bTagWeight_lfstats2up/F");
      tree -> Branch("bTagWeight_lfstats2down", &bTagWeight_lfstats2down, "bTagWeight_lfstats2down/F");
      tree -> Branch("bTagWeight_cferr1up", &bTagWeight_cferr1up, "bTagWeight_cferr1up/F");
      tree -> Branch("bTagWeight_cferr1down", &bTagWeight_cferr1down, "bTagWeight_cferr1down/F");
      tree -> Branch("bTagWeight_cferr2up", &bTagWeight_cferr2up, "bTagWeight_cferr2up/F");
      tree -> Branch("bTagWeight_cferr2down", &bTagWeight_cferr2down, "bTagWeight_cferr2down/F");
    }

    tree -> Branch("ZewkWeight", &ZewkWeight, "ZewkWeight/F");
    tree -> Branch("WewkWeight", &WewkWeight, "WewkWeight/F");
    tree -> Branch("model",       &model_);
    tree -> Branch("AtLeastOneTrigger" , &AtLeastOneTrigger , "AtLeastOneTrigger/O");
    tree -> Branch("AtLeastOneL1Filter" , &AtLeastOneL1Filter , "AtLeastOneL1Filter/O");
    tree -> Branch("Prefired" , &Prefired , "Prefired/O");
    tree -> Branch("nPV" , &nPV , "nPV/L");
    tree -> Branch("nSV" , &nSV , "nSV/L");
    tree -> Branch("MeanNumInteractions" , &MeanNumInteractions , "MeanNumInteractions/I");
    tree -> Branch("nGenLL" , &nGenLL , "nGenLL/L");
    tree -> Branch("nGenBquarks" , &nGenBquarks , "nGenBquarks/L");
    tree -> Branch("nGenMuons" , &nGenMuons , "nGenMuons/L");
    tree -> Branch("nMatchedCHSJets" , &nMatchedCHSJets , "nMatchedCHSJets/L");
    tree -> Branch("nMatchedFatJets" , &nMatchedFatJets , "nMatchedFatJets/L");
    tree -> Branch("number_of_b_matched_to_CHSJets", &number_of_b_matched_to_CHSJets, "number_of_b_matched_to_CHSJets/L");
    tree -> Branch("number_of_b_matched_to_FatJets", &number_of_b_matched_to_FatJets, "number_of_b_matched_to_FatJets/L");
    //tree -> Branch("nAllBarrelJets" , &nAllBarrelJets , "nAllBarrelJets/L");
    tree -> Branch("nVBFGenMatchedJets", & nVBFGenMatchedJets, "nVBFGenMatchedJets/L");
    tree -> Branch("nAllJets" , &nAllJets , "nAllJets/L");
    tree -> Branch("nCHSJets" , &nCHSJets , "nCHSJets/L");
    tree -> Branch("nLooseCHSJets" , &nLooseCHSJets , "nLooseCHSJets/L");
    tree -> Branch("nTightCHSJets" , &nTightCHSJets , "nTightCHSJets/L");
    tree -> Branch("nCHSFatJets" , &nCHSFatJets , "nCHSFatJets/L");
    tree -> Branch("nLooseCHSFatJets" , &nLooseCHSFatJets , "nLooseCHSFatJets/L");
    tree -> Branch("nTightCHSFatJets" , &nTightCHSFatJets , "nTightCHSFatJets/L");
    tree -> Branch("nLooseCaloTagJets" , &nLooseCaloTagJets , "nLooseCaloTagJets/L");
    tree -> Branch("nCaloTagJets" , &nCaloTagJets , "nCaloTagJets/L");
    //tree -> Branch("nCaloJets" , &nCaloJets , "nCaloJets/L");
    //tree -> Branch("nMatchedCaloJets" , &nMatchedCaloJets , "nMatchedCaloJets/L");
    //tree -> Branch("nMatchedCaloJetsWithGenJets" , &nMatchedCaloJetsWithGenJets , "nMatchedCaloJetsWithGenJets/L");
    //tree -> Branch("number_of_b_matched_to_CaloJets", &number_of_b_matched_to_CaloJets, "number_of_b_matched_to_CaloJets/L");
    //tree -> Branch("number_of_b_matched_to_CaloJetsWithGenJets", &number_of_b_matched_to_CaloJetsWithGenJets, "number_of_b_matched_to_CaloJetsWithGenJets/L");
    tree -> Branch("nElectrons", &nElectrons, "nElectrons/I");
    tree -> Branch("nMuons", &nMuons, "nMuons/I");
    tree -> Branch("nTaus", &nTaus, "nTaus/I");
    tree -> Branch("nPhotons", &nPhotons, "nPhotons/I");
    tree -> Branch("nTightElectrons", &nTightElectrons, "nTightElectrons/I");
    tree -> Branch("nTightMuons", &nTightMuons, "nTightMuons/I");
    if (isTracking) {
      tree -> Branch("nLooseNotTightElectrons", &nLooseElectrons, "nLooseElectrons/I");
      tree -> Branch("nLooseNotTightMuons", &nLooseMuons, "nLooseMuons/I");
      tree -> Branch("nTriggerMuons", &nTriggerMuons, "nTriggerMuons/I");
      tree -> Branch("nKShorts", &nKShorts, "nKShorts/I");
      tree -> Branch("nLambdas", &nLambdas, "nLambdas/I");
    }
    if (!isShort){
      tree -> Branch("nPFCandidates" , &nPFCandidates, "nPFCandidates/I");
      tree -> Branch("nPFCandidatesTrack", &nPFCandidatesTrack, "nPFCandidatesTrack/I");
      tree -> Branch("nPFCandidatesHighPurityTrack", &nPFCandidatesHighPurityTrack, "nPFCandidatesHighPurityTrack/I");
      tree -> Branch("nPFCandidatesFullTrackInfo", &nPFCandidatesFullTrackInfo, "nPFCandidatesFullTrackInfo/I");
      tree -> Branch("nPFCandidatesFullTrackInfo_pt", &nPFCandidatesFullTrackInfo_pt, "nPFCandidatesFullTrackInfo_pt/I");
      tree -> Branch("nPFCandidatesFullTrackInfo_hasTrackDetails", &nPFCandidatesFullTrackInfo_hasTrackDetails, "nPFCandidatesFullTrackInfo_hasTrackDetails/I");
    }
    tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
    tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
    tree -> Branch("Flag_ECALCalib", &ECALCalibFlag, "Flag_ECALCalib/O");
    tree -> Branch("isVBF" , &isVBF, "isVBF/O");
    tree -> Branch("isggH" , &isggH, "isggH/O");
    tree -> Branch("isTriggerVBF" , &isTriggerVBF, "isTriggerVBF/O");
    if (isControl) {
      tree -> Branch("isTightMM" , &isTightMM, "isTightMM/O");
      tree -> Branch("isOppositeSignTightMM" , &isOppositeSignTightMM, "isOppositeSignTightMM/O");
      tree -> Branch("isZtoMM" , &isZtoMM, "isZtoMM/O");

      tree -> Branch("isTightEE" , &isTightEE, "isTightEE/O");
      tree -> Branch("isOppositeSignTightEE" , &isOppositeSignTightEE, "isOppositeSignTightEE/O");
      tree -> Branch("isZtoEE" , &isZtoEE, "isZtoEE/O");

      tree -> Branch("isTightM" , &isTightM, "isTightM/O");
      tree -> Branch("isWtoMN" , &isWtoMN, "isWtoMN/O");

      tree -> Branch("isTightE" , &isTightE, "isTightE/O");
      tree -> Branch("isWtoEN" , &isWtoEN, "isWtoEN/O");

      tree -> Branch("isTightEM" , &isTightEM, "isTightEM/O");
      tree -> Branch("isLooseEM" , &isLooseEM, "isLooseEM/O");
      tree -> Branch("isTtoEM" , &isTtoEM, "isTtoEM/O");
    }
    tree -> Branch("HT" , &HT , "HT/F");
    tree -> Branch("MinJetMetDPhi", &MinJetMetDPhi, "MinJetMetDPhi/F");
    tree -> Branch("ggHJetMetDPhi", &ggHJetMetDPhi , "ggHJetMetDPhi/F");
    tree -> Branch("MinJetMetDPhiAllJets", &MinJetMetDPhiAllJets, "MinJetMetDPhiAllJets/F");
    tree -> Branch("gen_b_radius" , &gen_b_radius , "gen_b_radius/F");
    tree -> Branch("m_pi" , &m_pi , "m_pi/F");

    // Set trigger branches
    for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
    if(isVerboseTrigger)//save PS values in ntuple
        {
  	    for(auto it = PrescalesTriggerMap.begin(); it != PrescalesTriggerMap.end(); it++) {
	        tree->Branch( ("PS_" + it->first).c_str(), &(it->second), ("PS_" + it->first+"/I").c_str());
	    }
        }
    for(auto it = MetFiltersMap.begin(); it != MetFiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
    //for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());//commented, filters treated differently in 2016/2017-8

    tree -> Branch("HDiCHS", &HDiCHS, "HDiCHS/F");
    tree -> Branch("HTriCHS", &HTriCHS, "HTriCHS/F");
    tree -> Branch("HQuadCHS", &HQuadCHS, "HQuadCHS/F");
    tree -> Branch("HDiCHSMatched", &HDiCHSMatched, "HDiCHSMatched/F");
    tree -> Branch("HTriCHSMatched", &HTriCHSMatched, "HTriCHSMatched/F");
    tree -> Branch("HQuadCHSMatched", &HQuadCHSMatched, "HQuadCHSMatched/F");

    tree -> Branch("LeadingLLP", &LeadingLLP);

    if (isTracking) {
      tree -> Branch("nROIs", &nROIs, "nROIs/I");
    }
    if (isTracking && WriteROITaggerScore){
      tree -> Branch("LeadingROI", &LeadingROI);
      // tree -> Branch("SubleadingROI", &SubleadingROI);
      tree -> Branch("SubleadingROI_dPhi2p0", &SubleadingROI_dPhi2p0);
      tree -> Branch("LeadingROILog10BackgroundScore", &LeadingROIScore);
      // tree -> Branch("SubleadingROIScore", &SubleadingROIScore);
      tree -> Branch("SubleadingROILog10BackgroundScore_dPhi2p0", &SubleadingROIScore_dPhi2p0);
      tree -> Branch("MaxDisplacedJet", &MaxDisplacedJet);
    }


    //tree -> Branch("HDiCalo", &HDiCalo, "HDiCalo/F");
    //tree -> Branch("HTriCalo", &HTriCalo, "HTriCalo/F");
    //tree -> Branch("HQuadCalo", &HQuadCalo, "HQuadCalo/F");
    //tree -> Branch("HDiCaloMatched", &HDiCaloMatched, "HDiCaloMatched/F");
    //tree -> Branch("HTriCaloMatched", &HTriCaloMatched, "HTriCaloMatched/F");
    //tree -> Branch("HQuadCaloMatched", &HQuadCaloMatched, "HQuadCaloMatched/F");

    tree->Branch("MEt", &MEt.pt, ObjectsFormat::ListMEtType().c_str());

    ////for(int i = 0; i < WriteNJets; i++) CHSJets.push_back( JetType() );
    ////    for(int i = 0; i < WriteNFatJets; i++) CHSFatJets.push_back( FatJetType() );
    //for(int i = 0; i < WriteNMatchedJets; i++) MatchedCHSJets.push_back( JetType() );
    ////for(int i = 0; i < WriteNMatchedJets; i++) MatchedCaloJets.push_back( CaloJetType() );
    ////for(int i = 0; i < WriteNGenBquarks; i++) GenBquarks.push_back( GenPType() );
    ////for(int i = 0; i < WriteNGenLongLiveds; i++) GenLongLiveds.push_back( GenPType() );
    ////for(int i = 0; i < WriteNLeptons; i++) Leptons.push_back( LeptonType() );
    //      for(int i = 0; i < WriteNLeptons; i++) Muons.push_back( LeptonType() );
    //      for(int i = 0; i < WriteNLeptons; i++) Electrons.push_back( LeptonType() );
    if (isShort && isControl){
      tree -> Branch("TightMuons", &Muons);
      tree -> Branch("TightElectrons", &Electrons);
    }

    //Set branches for objects
    //!! We save only MatchedJets for cross-checks with vectors
    ////for(int i = 0; i < WriteNJets; i++) tree->Branch(("CHSJet"+std::to_string(i+1)).c_str(), &(CHSJets[i].pt), ObjectsFormat::ListJetType().c_str());
    ////    for(int i = 0; i < WriteNFatJets; i++) tree->Branch(("CHSFatJet"+std::to_string(i+1)).c_str(), &(CHSFatJets[i].pt), ObjectsFormat::ListFatJetType().c_str());
    //for(int i = 0; i < WriteNMatchedJets; i++) tree->Branch(("MatchedCHSJet"+std::to_string(i+1)).c_str(), &(MatchedCHSJets[i].pt), ObjectsFormat::ListJetType().c_str());
    ////for(int i = 0; i < WriteNMatchedJets; i++) tree->Branch(("MatchedCaloJet"+std::to_string(i+1)).c_str(), &(MatchedCaloJets[i].pt), ObjectsFormat::ListCaloJetType().c_str());
    ////for(int i = 0; i < WriteNGenBquarks; i++) tree->Branch(("GenBquark"+std::to_string(i+1)).c_str(), &(GenBquarks[i].pt), ObjectsFormat::ListGenPType().c_str());
    ////for(int i = 0; i < WriteNGenLongLiveds; i++) tree->Branch(("GenLongLived"+std::to_string(i+1)).c_str(), &(GenLongLiveds[i].pt), ObjectsFormat::ListGenPType().c_str());
    tree -> Branch("GenVBFquarks", &GenVBFquarks);
    tree -> Branch("GenHiggs", &GenHiggs);
    tree -> Branch("GenLLPs", &GenLLPs);
    tree -> Branch("GenBquarks", &GenBquarks);
    if (isTracking && WriteGenMuons) tree -> Branch("GenMuons", &GenMuons);
    ////for(int i = 0; i < WriteNLeptons; i++) tree->Branch(("Lepton"+std::to_string(i+1)).c_str(), &(Leptons[i].pt), ObjectsFormat::ListLeptonType().c_str());
    //for(int i = 0; i < WriteNLeptons; i++) tree->Branch(("Muon"+std::to_string(i+1)).c_str(), &(Muons[i].pt), ObjectsFormat::ListLeptonType().c_str());
    //for(int i = 0; i < WriteNLeptons; i++) tree->Branch(("Electron"+std::to_string(i+1)).c_str(), &(Electrons[i].pt), ObjectsFormat::ListLeptonType().c_str());

    tree -> Branch("VBFPair", &VBF.pt, ObjectsFormat::ListCandidateType().c_str());
    if (isControl){
      tree -> Branch("Z", &Z.pt, ObjectsFormat::ListCandidateType().c_str());
      tree -> Branch("W", &W.pt, ObjectsFormat::ListCandidateType().c_str());
    }

    tree -> Branch("Jets", &CHSJets);
    //tree -> Branch("CaloJets", &CaloJets);
    if (!isTracking) {
      tree -> Branch("VBFPairJets", &VBFPairJets);
      tree -> Branch("ggHJet", &ggHJet);
    }
    //tree -> Branch("AllBarrelJets", &AllBarrelJets);

    if (isTracking) {
      tree -> Branch("TriggerMuons", &Muons);
      if (isControl) tree -> Branch("TightMuons", &TightMuons);
      tree -> Branch("LooseNotTightMuons", &LooseMuons);
      if (isControl) tree -> Branch("TightElectrons", &Electrons);
      tree -> Branch("LooseNotTightElectrons", &LooseElectrons);

      if (WriteROITaggerInputs) {
        tree -> Branch("Vertices", &VerticesROI);
        tree -> Branch("LostTracks", &LostTracksROI);
        tree -> Branch("PFCandidates", &PFCandidatesROI);
        tree -> Branch("TrackClusters", &TrackClusters);
        tree -> Branch("RegionsOfInterest", &RegionsOfInterest);
      }

      if (WriteROITaggerScore) tree -> Branch("ROIs", &ROIs);
    }

    if (WriteAllJets) tree -> Branch("AllJets", &AllJets);
    if (WriteFatJets) tree -> Branch("FatJets", &CHSFatJets);
    if (WriteVertices) tree -> Branch("PrimaryVertices", &PrimVertices);
    if (WriteVertices) tree -> Branch("SecondaryVertices", &SecVertices);
    if (WriteKShorts) tree -> Branch("KShorts", &KShorts);
    if (WriteLambdas) tree -> Branch("Lambdas", &Lambdas);
    if (WriteAK4JetPFCandidates || WriteAK8JetPFCandidates || WriteAllJetPFCandidates || WriteAllPFCandidates) tree -> Branch("PFCandidates", &PFCandidates);
    if (WriteLostTracks) tree -> Branch("LostTracks", &LostTracks);
    if (WriteBtagInfos) tree->Branch("BTagVertices", &BTagVertices);

    //Histograms
    //Matching_to_b_AK4Jets = fs->make<TH1F>("Matching_to_b_AK4Jets", "Matching_to_b_AK4Jets", 10,0,10);

}

// ------------ method called once each job just after ending the event loop  ------------
void
Ntuplizer::endJob()
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
Ntuplizer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(Ntuplizer);
