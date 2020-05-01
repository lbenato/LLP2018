// -*- C++ -*-
//
// Package:    Analyzer/AODNtuplizer
// Class:      AODNtuplizer
// 
/**\class AODNtuplizer AODNtuplizer.cc Analyzer/LLP2018/plugins/AODNtuplizer.cc

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

//Track classes
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/Measurement1D.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/TrajectoryState/interface/FreeTrajectoryState.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateTransform.h"

#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "TrackingTools/GeomPropagators/interface/StateOnTrackerBound.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateTransform.h"
#include "TrackingTools/MaterialEffects/interface/PropagatorWithMaterial.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"

#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"

#include "PhysicsTools/RecoUtils/interface/CheckHitPattern.h"
#include "RecoVertex/ConfigurableVertexReco/interface/ConfigurableVertexReconstructor.h"
#include "RecoVertex/VertexTools/interface/VertexCompatibleWithBeam.h"
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleFitter.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticle.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"
#include "RecoVertex/VertexPrimitives/interface/ConvertToFromReco.h"
#include "RecoVertex/VertexPrimitives/interface/ConvertError.h"

#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimDataFormats/TrackerDigiSimLink/interface/StripDigiSimLink.h"

//Pat classes
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TTree.h"
#include <string>

#include "JetAnalyzer.h"
//#include "RecoJetAnalyzer.h"
#include "CaloJetAnalyzer.h"
#include "GenAnalyzer.h"
#include "PileupAnalyzer.h"
//#include "RecoTriggerAnalyzer.h"
#include "TriggerAnalyzer.h"
#include "PFCandidateAnalyzer.h"
#include "VertexAnalyzer.h"
#include "ElectronAnalyzer.h"
//#include "RecoElectronAnalyzer.h"
#include "MuonAnalyzer.h"
#include "TauAnalyzer.h"
#include "PhotonAnalyzer.h"
//#include "RecoPhotonAnalyzer.h"
#include "RecoObjects.h"
#include "RecoObjectsFormat.h"
#include "Objects.h"
#include "ObjectsFormat.h"
#include "DTAnalyzer.h"
#include "CSCAnalyzer.h"
#include "StandAloneMuonsAnalyzer.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class AODNtuplizer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit AODNtuplizer(const edm::ParameterSet&);
      ~AODNtuplizer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

    // ----------member data ---------------------------
    edm::ParameterSet GenPSet;
    edm::ParameterSet PileupPSet;
    edm::ParameterSet TriggerPSet;
    edm::ParameterSet CHSJetPSet;
    edm::ParameterSet CaloJetPSet;
    edm::ParameterSet VBFJetPSet;
    edm::ParameterSet ElectronPSet;
    edm::ParameterSet MuonPSet;
    edm::ParameterSet TauPSet;
    edm::ParameterSet PhotonPSet;
    edm::ParameterSet VertexPSet;
    edm::ParameterSet PFCandidatePSet;
    edm::ParameterSet DTPSet;
    edm::ParameterSet CSCSet;
    edm::ParameterSet StandAloneMuonsPSet;
    edm::ParameterSet DisplacedStandAloneMuonsPSet;
    edm::EDGetTokenT<reco::PFJetCollection> jetToken;
    //edm::EDGetTokenT<std::vector<pat::MET> > metToken;
    
    edm::EDGetTokenT<vector<reco::Track> > generalTracksToken;
    edm::EDGetTokenT<edm::View<reco::Track> > generalTracksViewToken;


    JetAnalyzer* theCHSJetAnalyzer;
    CaloJetAnalyzer* theCaloJetAnalyzer;
    JetAnalyzer* theVBFJetAnalyzer;
    GenAnalyzer* theGenAnalyzer;
    PileupAnalyzer* thePileupAnalyzer;
    TriggerAnalyzer* theTriggerAnalyzer;
    ElectronAnalyzer* theElectronAnalyzer;
    MuonAnalyzer* theMuonAnalyzer;
    TauAnalyzer* theTauAnalyzer;
    PhotonAnalyzer* thePhotonAnalyzer;
    VertexAnalyzer* theVertexAnalyzer;
    PFCandidateAnalyzer* thePFCandidateAnalyzer;
    DTAnalyzer* theDTAnalyzer;
    CSCAnalyzer* theCSCAnalyzer;
    //StandAloneMuonsAnalyzer* theStandAloneMuonsAnalyzer;
    //StandAloneMuonsAnalyzer* theDisplacedStandAloneMuonsAnalyzer;

    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP0p01Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP0p1Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP1Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP10Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP100Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP1000Token;

    int idLLP, idHiggs, idMotherB, statusLLP, statusHiggs;
    double MinGenBpt, MaxGenBeta, MinGenBradius2D, MaxGenBradius2D, MinGenBetaAcc, MaxGenBetaAcc;
    double InvmassVBF, DetaVBF;//VBF tagging
    bool WriteGenVBFquarks, WriteGenHiggs, WriteGenBquarks, WriteGenLLPs;
    int  WriteNMatchedJets;
    int  WriteNLeptons;
    bool WriteOnlyTriggerEvents, WriteOnlyL1FilterEvents, WriteOnlyisVBFEvents;
    bool WriteFatJets;
    bool WriteAllJets;
    bool WriteAK4JetPFCandidates, WriteAK8JetPFCandidates;
    bool WriteAllJetPFCandidates, WriteAllPFCandidates;
    bool WriteLostTracks;
    bool WriteVertices;
    bool WriteBtagInfos;
    bool CalculateNsubjettiness;
    bool PerformPreFiringStudies;
    bool PerformVBF;
    bool PerformggH;

    std::vector<JetType> CHSJets;
    std::vector<JetType> VBFPairJets;
    std::vector<JetType> ggHJet;
    //std::vector<RecoJetType> ManualJets;
    std::vector<CaloJetType> CaloJets;
    //std::vector<LeptonType> Muons; //maybe later!
    std::vector<GenPType> GenVBFquarks;
    std::vector<GenPType> GenBquarks;
    std::vector<GenPType> GenLLPs;
    std::vector<GenPType> GenHiggs;
    std::vector<DT4DSegmentType> DTRecSegments4D;    
    std::vector<CSCSegmentType> CSCSegments;
    //std::vector<TrackType> StandAloneMuons;
    //std::vector<TrackType> DisplacedStandAloneMuons;

    std::vector<PFCandidateType> PFCandidates;

    MEtType MEt;
    //RecoMEtType RecoMEt;
    CandidateType VBF;//VBF tagging

    std::map<std::string, bool> TriggerMap;
    std::map<std::string, int> PrescalesTriggerMap;
    std::map<std::string, bool> MetFiltersMap;
    std::map<std::string, bool> L1FiltersMap;

    bool isVerbose, isVerboseTrigger, isSignal, isCalo;
    bool isMC;
    bool isVBF;
    bool isggH;
    long int EventNumber, LumiNumber, RunNumber, nPV, nSV;
    bool AtLeastOneTrigger, AtLeastOneL1Filter;
    float EventWeight;
    float GenEventWeight;
    float PUWeight, PUWeightUp, PUWeightDown;
    long int nCHSJets;
    long int nCaloJets;
    long int nElectrons, nMuons, nTaus, nPhotons;
    long int nTightMuons, nTightElectrons;
    long int nMatchedCHSJets;
    long int nMatchedCaloJets;
    long int nVBFGenMatchedCHSJets;
    long int nVBFGenMatchedVBFJets;
    long int number_of_b_matched_to_CHSJets;
    long int number_of_b_matched_to_CaloJets;
    long int number_of_VBFGen_matched_to_CHSJets;
    long int number_of_VBFGen_matched_to_VBFJets;
    long int number_of_b_matched_to_DTSegment4D;
    long int number_of_b_matched_to_CSCSegment;
    long int number_of_VBF_matched_to_DTSegment4D;
    long int number_of_VBF_matched_to_CSCSegment;
    int n_segments_around_b_quark_0;
    int n_segments_around_b_quark_1;
    int n_segments_around_b_quark_2;
    int n_segments_around_b_quark_3;
    long int nDTSegments, nDTSegmentsStation1, nDTSegmentsStation2, nDTSegmentsStation3, nDTSegmentsStation4;
    long int nCSCSegments;
    long int nMatchedDTsegmentstob;
    long int nMatchedCSCsegmentstob;
    long int nMatchedDTsegmentstoVBF;
    long int nMatchedCSCsegmentstoVBF;
    //long int nStandAloneMuons, nMatchedStandAloneMuons;
    //long int nDisplacedStandAloneMuons, nMatchedDisplacedStandAloneMuons;
    
    AddFourMomenta addP4;
    float HT;
    float MinJetMetDPhi;
    float MinJetMetDPhiAllJets;
    float ggHJetMetDPhi;
    float m_pi, gen_b_radius, gen_b_radius_2D;
    long int nPFCandidates, nPFCandidatesTrack, nPFCandidatesHighPurityTrack, nPFCandidatesFullTrackInfo, nPFCandidatesFullTrackInfo_pt, nPFCandidatesFullTrackInfo_hasTrackDetails;
    long int number_of_PV;
    long int number_of_SV;
    //MET filters
    bool BadPFMuonFlag, BadChCandFlag;
    //Pre-firing
    bool Prefired;
    long int nGenBquarks, nGenLL;
    
    
    //Geometry and propagator
    const MagneticField* MagneticFieldTag;
    edm::ESHandle<Propagator> PropagatorHandle;
    edm::ESHandle<TransientTrackBuilder> BuilderHandle;
    
    
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
AODNtuplizer::AODNtuplizer(const edm::ParameterSet& iConfig):
    GenPSet(iConfig.getParameter<edm::ParameterSet>("genSet")),
    PileupPSet(iConfig.getParameter<edm::ParameterSet>("pileupSet")),
    TriggerPSet(iConfig.getParameter<edm::ParameterSet>("triggerSet")),
    CHSJetPSet(iConfig.getParameter<edm::ParameterSet>("chsJetSet")),
    CaloJetPSet(iConfig.getParameter<edm::ParameterSet>("caloJetSet")),
    VBFJetPSet(iConfig.getParameter<edm::ParameterSet>("vbfJetSet")),
    ElectronPSet(iConfig.getParameter<edm::ParameterSet>("electronSet")),
    MuonPSet(iConfig.getParameter<edm::ParameterSet>("muonSet")),
    TauPSet(iConfig.getParameter<edm::ParameterSet>("tauSet")),
    PhotonPSet(iConfig.getParameter<edm::ParameterSet>("photonSet")),
    VertexPSet(iConfig.getParameter<edm::ParameterSet>("vertexSet")),
    PFCandidatePSet(iConfig.getParameter<edm::ParameterSet>("pfCandidateSet")),
    DTPSet(iConfig.getParameter<edm::ParameterSet>("dtSet")),
    CSCSet(iConfig.getParameter<edm::ParameterSet>("cscSet")),
    StandAloneMuonsPSet(iConfig.getParameter<edm::ParameterSet>("standaloneMuonsSet")),
    DisplacedStandAloneMuonsPSet(iConfig.getParameter<edm::ParameterSet>("displacedStandaloneMuonsSet")),
    idLLP(iConfig.getParameter<int>("idLLP")),
    idHiggs(iConfig.getParameter<int>("idHiggs")),
    idMotherB(iConfig.getParameter<int>("idMotherB")),
    statusLLP(iConfig.getParameter<int>("statusLLP")),
    statusHiggs(iConfig.getParameter<int>("statusHiggs")),
    MinGenBpt(iConfig.getParameter<double>("minGenBpt")),
    MaxGenBeta(iConfig.getParameter<double>("maxGenBeta")),
    InvmassVBF(iConfig.getParameter<double>("invmassVBF")),
    DetaVBF(iConfig.getParameter<double>("detaVBF")),
    WriteGenVBFquarks(iConfig.getParameter<bool>("writeGenVBFquarks")),
    WriteGenHiggs(iConfig.getParameter<bool>("writeGenHiggs")),
    WriteGenBquarks(iConfig.getParameter<bool>("writeGenBquarks")),
    WriteGenLLPs(iConfig.getParameter<bool>("writeGenLLPs")),
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
    CalculateNsubjettiness(iConfig.getParameter<bool>("calculateNsubjettiness")),
    PerformPreFiringStudies(iConfig.getParameter<bool>("performPreFiringStudies")),
    PerformVBF(iConfig.getParameter<bool>("performVBF")),
    PerformggH(iConfig.getParameter<bool>("performggH")),
    isVerbose(iConfig.getParameter<bool> ("verbose")),
    isVerboseTrigger(iConfig.getParameter<bool> ("verboseTrigger")),
    isSignal(iConfig.getParameter<bool> ("signal")),
    isCalo(iConfig.getParameter<bool> ("iscalo"))

{

    // Check writePFCandidate flags
    int PFCandidateFlags = 0;
    if (WriteAK4JetPFCandidates) PFCandidateFlags++;
    if (WriteAK8JetPFCandidates) PFCandidateFlags++;
    if (WriteAllJetPFCandidates) PFCandidateFlags++;
    if (WriteAllPFCandidates)    PFCandidateFlags++;
    if (PFCandidateFlags > 1)   throw cms::Exception("Configuration") << "More than one writePFCandidates flag selected. Please choose one option only!";


    theCHSJetAnalyzer       = new JetAnalyzer(CHSJetPSet, consumesCollector());
    theCaloJetAnalyzer      = new CaloJetAnalyzer(CaloJetPSet, consumesCollector());
    theVBFJetAnalyzer       = new JetAnalyzer(VBFJetPSet, consumesCollector());
    theGenAnalyzer          = new GenAnalyzer(GenPSet, consumesCollector());
    thePileupAnalyzer       = new PileupAnalyzer(PileupPSet, consumesCollector());
    theTriggerAnalyzer      = new TriggerAnalyzer(TriggerPSet, consumesCollector());
    theElectronAnalyzer     = new ElectronAnalyzer(ElectronPSet, consumesCollector());
    theMuonAnalyzer         = new MuonAnalyzer(MuonPSet, consumesCollector());
    theTauAnalyzer          = new TauAnalyzer(TauPSet, consumesCollector());
    thePhotonAnalyzer       = new PhotonAnalyzer(PhotonPSet, consumesCollector());
    theVertexAnalyzer       = new VertexAnalyzer(VertexPSet, consumesCollector());
    thePFCandidateAnalyzer  = new PFCandidateAnalyzer(PFCandidatePSet, consumesCollector());
    theDTAnalyzer           = new DTAnalyzer(DTPSet, consumesCollector());
    theCSCAnalyzer          = new CSCAnalyzer(CSCSet, consumesCollector());
    //theStandAloneMuonsAnalyzer          = new StandAloneMuonsAnalyzer(StandAloneMuonsPSet,  consumesCollector());
    //theDisplacedStandAloneMuonsAnalyzer = new StandAloneMuonsAnalyzer(DisplacedStandAloneMuonsPSet,  consumesCollector());

    std::vector<std::string> TriggerList(TriggerPSet.getParameter<std::vector<std::string> >("paths"));
    for(unsigned int i = 0; i < TriggerList.size(); i++) TriggerMap[ TriggerList[i] ] = false;
    for(unsigned int i = 0; i < TriggerList.size(); i++) PrescalesTriggerMap[ TriggerList[i] ] = -1;
    std::vector<std::string> MetFiltersList(TriggerPSet.getParameter<std::vector<std::string> >("metpaths"));
    for(unsigned int i = 0; i < MetFiltersList.size(); i++) MetFiltersMap[ MetFiltersList[i] ] = false;

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

    edm::InputTag IT_jets = edm::InputTag("ak4PFJetsCHS");
    jetToken = consumes<reco::PFJetCollection>(IT_jets);
    edm::InputTag lheProduct_ = edm::InputTag("lheProduct");


    //general tracks
    edm::InputTag IT_generalTracks = edm::InputTag("generalTracks");
    generalTracksToken = consumes<std::vector<reco::Track>>(IT_generalTracks);
    generalTracksViewToken = consumes<edm::View<reco::Track>>(IT_generalTracks);
        
    ////edm::InputTag IT_met = edm::InputTag("patMETs");
    ////edm::InputTag IT_met = edm::InputTag("slimmedMETs");
    ////metToken = consumes<std::vector<pat::MET>>(IT_met);
    //now do what ever initialization is needed

    usesResource("TFileService");

    if(isVerbose) std::cout << "---------- STARTING ----------" << std::endl;


}


AODNtuplizer::~AODNtuplizer()
{
 
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    if(isVerbose) std::cout << "---------- ENDING  ----------" << std::endl;

    delete theCHSJetAnalyzer;
    delete theCaloJetAnalyzer;
    delete theVBFJetAnalyzer;
    delete theGenAnalyzer;
    delete thePileupAnalyzer;
    delete theTriggerAnalyzer;
    delete theElectronAnalyzer;
    delete theMuonAnalyzer;
    delete theTauAnalyzer;
    delete thePhotonAnalyzer;
    delete theVertexAnalyzer;
    delete thePFCandidateAnalyzer;
    delete theDTAnalyzer;
    delete theCSCAnalyzer;
    //delete theStandAloneMuonsAnalyzer;
    //delete theDisplacedStandAloneMuonsAnalyzer;
}


//
// member functions
//

// ------------ method called for each event  ------------
void
AODNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  if(isVerbose) std::cout << " Starting analyze..... " << std::endl;
    auto start = std::chrono::system_clock::now();//time!
    using namespace edm;
    using namespace reco;
    using namespace std;

    // Initialize types
    //ObjectsFormat::ResetGenPType(GenHiggs);
    ObjectsFormat::ResetCandidateType(VBF);


    nCHSJets = nCaloJets = 0;
    nElectrons = nMuons = nTaus = nPhotons = 0;
    nTightMuons = nTightElectrons = 0;
    //nStandAloneMuons = nDisplacedStandAloneMuons =0;
    nDTSegments = nDTSegmentsStation1 = nDTSegmentsStation2 = nDTSegmentsStation3 = nDTSegmentsStation4 = nCSCSegments = 0;
    //nMatchedStandAloneMuons = nMatchedDisplacedStandAloneMuons =0;
    isMC = false;
    isVBF = false;
    isggH = false;
    EventNumber = LumiNumber = RunNumber = nPV = 0;
    GenEventWeight = EventWeight = PUWeight = PUWeightDown = PUWeightUp = 1.;
    HT = 0.;
    nMatchedCHSJets = 0;
    nMatchedCaloJets = 0;
    nVBFGenMatchedCHSJets = 0;
    nVBFGenMatchedVBFJets = 0;
    number_of_b_matched_to_CHSJets = 0;
    number_of_b_matched_to_CaloJets = 0;
    number_of_VBFGen_matched_to_CHSJets = 0;
    number_of_VBFGen_matched_to_VBFJets = 0;
    number_of_b_matched_to_DTSegment4D=0;
    number_of_b_matched_to_CSCSegment=0;
    number_of_VBF_matched_to_DTSegment4D=0;
    number_of_VBF_matched_to_CSCSegment=0;
    n_segments_around_b_quark_0 = 0;
    n_segments_around_b_quark_1 = 0;
    n_segments_around_b_quark_2 = 0;
    n_segments_around_b_quark_3 = 0;
    MinJetMetDPhi = MinJetMetDPhiAllJets = ggHJetMetDPhi = 10.;
    nGenBquarks = nGenLL = 0;
    m_pi = 0.;
    gen_b_radius = -1.;
    gen_b_radius_2D = -1.;
    Prefired = false;
    AtLeastOneTrigger = AtLeastOneL1Filter = false;
    nPFCandidates = nPFCandidatesTrack = nPFCandidatesHighPurityTrack = nPFCandidatesFullTrackInfo = nPFCandidatesFullTrackInfo_pt = nPFCandidatesFullTrackInfo_hasTrackDetails = 0;
    number_of_PV = number_of_SV = 0;

    //Event info                                                                
    isMC = !iEvent.isRealData();
    EventNumber = iEvent.id().event();
    LumiNumber = iEvent.luminosityBlock();
    RunNumber = iEvent.id().run();
    //std::cout << "\n";
    //std::cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << std::endl;
    //std::cout << " Event Number: " << EventNumber << std::endl;


    //GenEventWeight
    GenEventWeight = theGenAnalyzer->GenEventWeight(iEvent);
    EventWeight *= GenEventWeight;

    //Not needed anymore
    edm::Handle<reco::PFJetCollection> JetColl;
    iEvent.getByToken( jetToken, JetColl );


    if(PerformVBF and PerformggH) throw cms::Exception("Configuration") << "VBF and ggH selections can't be performed together! Please choose one option only!";


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Trigger and MET filters
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    // Trigger and MET filters
    if(isVerbose) std::cout << "Trigger and met filters" << std::endl;
    //debug!
    theTriggerAnalyzer->FillTriggerMap(iEvent, TriggerMap, PrescalesTriggerMap, isVerboseTrigger);
    theTriggerAnalyzer->FillMetFiltersMap(iEvent, MetFiltersMap);
    BadPFMuonFlag = theTriggerAnalyzer->GetBadPFMuonFlag(iEvent);
    BadChCandFlag = theTriggerAnalyzer->GetBadChCandFlag(iEvent);

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
      }

    ////if(!AtLeastOneTrigger && WriteOnlyTriggerEvents) std::cout << "This event can be rejected" << std::endl;
    if(!AtLeastOneTrigger && WriteOnlyTriggerEvents) return;
    if(!AtLeastOneL1Filter && WriteOnlyL1FilterEvents) return;

    //Pre-firing
    if(PerformPreFiringStudies)
      {
	Prefired = theTriggerAnalyzer->EvaluatePrefiring(iEvent);
      }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // HT
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    
    HT = theCHSJetAnalyzer->CalculateHT(iEvent,3,15,3.);

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Electrons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Electrons
    if(isVerbose) std::cout << "Electrons" << std::endl;
    std::vector<pat::Electron> ElecVect = theElectronAnalyzer->FillElectronVector(iEvent);
    std::vector<pat::Electron> TightElecVect;

    for(unsigned int a = 0; a<ElecVect.size(); a++)
      {
	if(ElecVect.at(a).hasUserInt("isTight") && ElecVect.at(a).userInt("isTight")>0)
	  {
	    TightElecVect.push_back(ElecVect.at(a));
	    nTightElectrons++;
	  }
      }
    nElectrons = ElecVect.size();

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Muons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(isVerbose) std::cout << "Muons" << std::endl;
    std::vector<pat::Muon> MuonVect = theMuonAnalyzer->FillMuonVector(iEvent);
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

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Taus
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(isVerbose) std::cout << "Taus" << std::endl;
    std::vector<pat::Tau> TauVect = theTauAnalyzer->FillTauVector(iEvent);
    //theTauAnalyzer->CleanTausFromMuons(TauVect, MuonVect, 0.4);//synch caltech
    //theTauAnalyzer->CleanTausFromElectrons(TauVect, ElecVect, 0.4);//synch caltech
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
    // Missing Energy
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(isVerbose) std::cout << "MET" << std::endl;
    //reco::PFMET RecoMET = theCHSJetAnalyzer->FillRecoMetVector(iEvent);
    pat::MET MET = theCHSJetAnalyzer->FillMetVector(iEvent);
    //For debugging:
    ////edm::Handle<std::vector<pat::MET> > MetCollection;
    ////iEvent.getByToken(metToken, MetCollection);
    ////pat::MET MET = MetCollection->front();
    //std::cout << " MET features: " << std::endl;
    //std::cout << MET.pt() << std::endl;
    //std::cout << MET.metSignificance() << std::endl;
    //if(MET.caloMETPt()) std::cout << MET.caloMETPt() << std::endl;
    //if(MET.genMET()) std::cout << MET.genMET()->pt()<<std::endl;
    //std::cout << MET.uncorPt() << std::endl;
    //if(MET.shiftedPt(pat::MET::METUncertainty::UnclusteredEnDown)) std::cout << MET.shiftedPt(pat::MET::METUncertainty::UnclusteredEnDown)<<std::endl;

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Preselections
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(EventNumber!=44169) return;
    if(HT<100) return;//Avoid events with low HT//WAIT!!
    if(isCalo && MET.pt()<120) return;//Avoid events with very low MET for calo analysis
    if(isCalo && nMuons>0) return;//Veto leptons and photons!
    if(isCalo && nTaus>0) return;//Veto leptons and photons!
    if(isCalo && nElectrons>0) return;//Veto leptons and photons!
    if(isCalo && nPhotons>0) return;//Veto leptons and photons!


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

    std::vector<reco::GenParticle> GenVBFVect = theGenAnalyzer->FillVBFGenVector(iEvent);
    std::vector<reco::GenParticle> GenHiggsVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idHiggs,statusHiggs);
    std::vector<reco::GenParticle> GenLongLivedVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idLLP,statusLLP);
    std::vector<reco::GenParticle> GenBquarksVect;

    nGenLL = GenLongLivedVect.size();

    if(nGenLL>0)
      {
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdStatusAndMotherAndKin(iEvent,5,23,idMotherB,float(MinGenBpt),float(MaxGenBeta));
      }
    else
      {
	GenBquarksVect = theGenAnalyzer->FillGenVectorByIdAndStatusAndKin(iEvent,5,23,float(MinGenBpt),float(MaxGenBeta));
      }

    nGenBquarks = GenBquarksVect.size();

    for(unsigned int i = 0; i < GenVBFVect.size(); i++) GenVBFquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenHiggsVect.size(); i++) GenHiggs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) GenLLPs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenBquarksVect.size(); i++) GenBquarks.push_back( GenPType() );

    if(nGenBquarks>0) gen_b_radius = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2) + pow(GenBquarksVect.at(0).vz() - GenBquarksVect.at(0).mother()->vz(),2)) : -1.;
    if(nGenLL>0) m_pi = GenLongLivedVect.at(0).mass();


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Pu weight and number of vertices
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(isVerbose) std::cout << "Pile-up" << std::endl;
    PUWeight     = thePileupAnalyzer->GetPUWeight(iEvent);//calculates pileup weights
    PUWeightUp   = thePileupAnalyzer->GetPUWeightUp(iEvent);//syst uncertainties due to pileup
    PUWeightDown = thePileupAnalyzer->GetPUWeightDown(iEvent);//syst uncertainties due to pileup
    nPV = thePileupAnalyzer->GetPV(iEvent);//calculates number of vertices
    
    EventWeight *= PUWeight;
    
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // VBF Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    std::vector<pat::Jet> VBFJetsVect = theVBFJetAnalyzer->FillJetVector(iEvent,iSetup);
    pat::CompositeCandidate theVBF;
    std::vector<pat::Jet> VBFPairJetsVect;
   
    float delta_eta_reco (0.), curr_delta_eta_reco(0.) ;
    int j1(-1), j2(-1);
    float curr_mjj(0.);
    reco::CompositeCandidate current_VBF;
    
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

    ////
    std::vector<pat::Jet> VBFGenMatchedVBFJetsVect;//That is for gluon fusion, mainly
    int VBF_matching_index_VBFJets;
    float VBF_delta_R_VBFJets;
    float VBF_current_delta_R_VBFJets;
    for(unsigned int b = 0; b<GenVBFVect.size(); b++)
      {
	VBF_delta_R_VBFJets = 1000.;
	VBF_current_delta_R_VBFJets = 1000.;
	VBF_matching_index_VBFJets = -1;
	for(unsigned int a = 0; a<VBFJetsVect.size(); a++)
	  {
	    VBF_current_delta_R_VBFJets = fabs(reco::deltaR(VBFJetsVect[a].eta(),VBFJetsVect[a].phi(),GenVBFVect[b].eta(),GenVBFVect[b].phi()));
	    if(VBF_current_delta_R_VBFJets<0.4 && VBF_current_delta_R_VBFJets<VBF_delta_R_VBFJets)
	      {
		VBF_delta_R_VBFJets = min(VBF_delta_R_VBFJets,VBF_current_delta_R_VBFJets);
		VBF_matching_index_VBFJets = a;
		VBFGenMatchedVBFJetsVect.push_back(VBFJetsVect[a]);
	      }
	  }
	if(VBF_matching_index_VBFJets>=0)
	{
	  number_of_VBFGen_matched_to_VBFJets++;
	}
      }

    auto comp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    auto last = std::unique(VBFGenMatchedVBFJetsVect.begin(), VBFGenMatchedVBFJetsVect.end(),comp);
    VBFGenMatchedVBFJetsVect.erase(last, VBFGenMatchedVBFJetsVect.end());
    nVBFGenMatchedVBFJets = VBFGenMatchedVBFJetsVect.size();

    // add VBF Gen matching infos into original jet
    for(unsigned int r = 0; r<VBFJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<VBFGenMatchedVBFJetsVect.size(); s++)
	  {
	    if(VBFGenMatchedVBFJetsVect[s].pt()==VBFJetsVect[r].pt())
	      {
		VBFJetsVect[r].addUserInt("isVBFGenMatched",1);
	      }
	  }
      }


    ////

    if(theVBF.pt()>0 && theVBF.mass()>InvmassVBF && abs(theVBF.daughter(1)->eta() - theVBF.daughter(0)->eta())>DetaVBF) {isVBF = true;}
    if(WriteOnlyisVBFEvents)//set in cfg file
      {
	if(!isVBF) return;
      }

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 CHS jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    std::vector<pat::Jet> CHSJetsVect = theCHSJetAnalyzer->FillJetVector(iEvent,iSetup);


    //Filling Jet structure manually, without filling a vector first. Used as cross-check.
    //for(reco::PFJetCollection::const_iterator it=JetColl->begin(); it!=JetColl->end(); ++it) {
    //   if(it->pt()>15 and abs(it->eta())<2.4) 
    //	{
    //	  reco::Jet jet=*it;
    //     ManualJets.push_back( RecoJetType() );
    //     RecoObjectsFormat::ResetRecoJetType(ManualJets[nJets]);
    //     RecoObjectsFormat::FillRecoJetType(ManualJets[nJets], &jet, isMC);
    //     nJets++;
    //   }
    //}

    //std::cout << " --------------- " << std::endl;
    //std::cout<<nJets<<std::endl;
    //std::cout << ManualJets.size() << std::endl;


    //One way to implement jet-gen b-quark matching is performed here
    //if(isVerbose) std::cout << "AK4 CHS matching to b quarks" << std::endl;
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
		//std::cout<<"Vertex of the gen b ( "<< GenBquarksVect.at(b).vx() <<" , "<< GenBquarksVect.at(b).vy() <<" , "<< GenBquarksVect.at(b).vz() <<" )" << std::endl; 
		//std::cout<<"Vertex of the matched jet ( "<< CHSJetsVect.at(a).vx() <<" , "<< CHSJetsVect.at(a).vy() <<" , "<< CHSJetsVect.at(a).vz() <<" )" << std::endl; 
		//std::cout<<"Vertex[0] of the matched jet ( "<< CHSJetsVect.at(a).vertex() <<" )" << std::endl; 
		CHSJetsVect[a].addUserInt("original_jet_index",a+1);
		CHSJetsVect[a].addUserFloat("genbRadius2D", GenBquarksVect[b].mother()? sqrt(pow(GenBquarksVect[b].vx() - GenBquarksVect[b].mother()->vx(),2) + pow(GenBquarksVect[b].vy() - GenBquarksVect[b].mother()->vy(),2)) : -1000.);
		CHSJetsVect[a].addUserFloat("genbEta",GenBquarksVect[b].eta());
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



    std::vector<pat::Jet> VBFGenMatchedCHSJetsVect;//That is for gluon fusion, mainly
    int VBF_matching_index_CHSJets;
    float VBF_delta_R_CHSJets;
    float VBF_current_delta_R_CHSJets;
    for(unsigned int b = 0; b<GenVBFVect.size(); b++)
      {
	VBF_delta_R_CHSJets = 1000.;
	VBF_current_delta_R_CHSJets = 1000.;
	VBF_matching_index_CHSJets = -1;
	for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
	  {
	    VBF_current_delta_R_CHSJets = fabs(reco::deltaR(CHSJetsVect[a].eta(),CHSJetsVect[a].phi(),GenVBFVect[b].eta(),GenVBFVect[b].phi()));
	    if(VBF_current_delta_R_CHSJets<0.4 && VBF_current_delta_R_CHSJets<VBF_delta_R_CHSJets)
	      {
		VBF_delta_R_CHSJets = min(VBF_delta_R_CHSJets,VBF_current_delta_R_CHSJets);
		VBF_matching_index_CHSJets = a;
		VBFGenMatchedCHSJetsVect.push_back(CHSJetsVect[a]);
	      }
	  }
	if(VBF_matching_index_CHSJets>=0)
	{
	  number_of_VBFGen_matched_to_CHSJets++;
	}
      }

    auto comp_VBF = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    auto last_VBF = std::unique(VBFGenMatchedCHSJetsVect.begin(), VBFGenMatchedCHSJetsVect.end(),comp_VBF);
    VBFGenMatchedCHSJetsVect.erase(last_VBF, VBFGenMatchedCHSJetsVect.end());
    nVBFGenMatchedCHSJets = VBFGenMatchedCHSJetsVect.size();

    // add VBF Gen matching infos into original jet
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<VBFGenMatchedCHSJetsVect.size(); s++)
	  {
	    if(VBFGenMatchedCHSJetsVect[s].pt()==CHSJetsVect[r].pt())
	      {
		CHSJetsVect[r].addUserInt("isVBFGenMatched",1);
	      }
	  }
      }

    //search for gluon fusion jets:
    std::vector<pat::Jet> ggHJetVect;
    int ggH_matching_index_CHSJets;
    
    ggH_matching_index_CHSJets = -1;
    //int chosen_ggh(-1);

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


    /////////////////////////////////////////////////////////////

    //Remove jets tagged as VBF from the list of potential signal
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
	      }//VBF jet pair removed
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

    //Check for PU jet ID:
    /*
    for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
      {
	if(CHSJetsVect.at(a).pt()<=50) 
	  {
	    //std::cout << "jet n. " << a << ", pt " << CHSJetsVect.at(a).pt()  << std::endl;
	    std::cout << "---------------------------------------------------------------" << std::endl;
	    std::cout << "jet n. " << a << ", pt " << CHSJetsVect.at(a).pt() << ", pileup mva disc " << CHSJetsVect.at(a).userFloat("pileupJetId:fullDiscriminant") << ", PU ID: " << CHSJetsVect.at(a).userInt("pileupJetId:fullId");
	    if(CHSJetsVect.at(a).hasUserInt("isGenMatched") && CHSJetsVect.at(a).userInt("isGenMatched")>0) std::cout << "  --> isGenMatched";
	    std::cout << "" << std::endl;
	  }
      }
    */

    //QCD killer cut
    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) if(fabs(reco::deltaPhi(CHSJetsVect[i].phi(), MET.phi())) < MinJetMetDPhi) MinJetMetDPhi = fabs(reco::deltaPhi(CHSJetsVect[i].phi(), MET.phi()));

    //QCD killer with ggH jet
    for(unsigned int i = 0; i < ggHJetVect.size(); i++) if(fabs(reco::deltaPhi(ggHJetVect[i].phi(), MET.phi())) < ggHJetMetDPhi) ggHJetMetDPhi = fabs(reco::deltaPhi(ggHJetVect[i].phi(), MET.phi()));


    //VBFPairJets
    //add b-matching infos into original jet
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

    if(isVerbose) {
      for (unsigned int i = 0; i != pfXWP1000Tags.size(); ++i) {
          if(pfXWP1000Tags[i].first->pt()>1 && abs(pfXWP1000Tags[i].first->eta())<2.4) std::cout << "  pfX WP1000 tag jet  [" << i << "]\tpt: " << pfXWP1000Tags[i].first->pt() << "\teta: " << pfXWP1000Tags[i].first->eta() << "\tphi: " << pfXWP1000Tags[i].first->phi() << "\tpfXTags: " << pfXWP1000Tags[i].second << std::endl;
      }
    }

    //If you have a Jet, rather than a JetTag, and wish to know if it is b-tagged, there are several ways of doing so. One which always works is to perform angular matching between the Jet and the JetTag::jet(). (The match should be perfect if your JetCollection was used to produce the JetTagCollection).




    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 Calo Jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    std::vector<reco::CaloJet> CaloJetsVect = theCaloJetAnalyzer->FillJetVector(iEvent);
    float delta_R_CaloJets_asVBF;//local variable
    float current_delta_R_CaloJets_asVBF;//local variable
    float delta_R_CaloJets_asggH;
    float current_delta_R_CaloJets_asggH;

    if(PerformVBF)
      //Remove calo jets overlapped with VBF pair
      //We must perform a DR matching, since pT might be different
      //int matching_index_CaloJets_asVBF;//local variable
      {
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
		    //if(isVerbose) std::cout << "This calo jet removed because overlaps VBF pair: pt " << CaloJetsVect[r].pt() << " ; eta: " << CaloJetsVect[r].eta() << " ; phi: " << CaloJetsVect[r].phi() << std::endl;
		    CaloJetsVect.erase(CaloJetsVect.begin()+r);
		  }
	      }//VBF jet pair removed
	  }

      }

    if(PerformggH)
      {
	//Remove calo jets overlapped with ggH candidate
	//We must perform a DR matching, since pT might be different
	for(unsigned int r = 0; r<CaloJetsVect.size(); r++)
	  {
	    delta_R_CaloJets_asggH = 1000.;
	    current_delta_R_CaloJets_asggH = 1000.;
	    for(unsigned int s = 0; s<ggHJetVect.size(); s++)
	      {
		current_delta_R_CaloJets_asggH = fabs(reco::deltaR(CaloJetsVect[r].eta(),CaloJetsVect[r].phi(),ggHJetVect[s].eta(),ggHJetVect[s].phi()));
		if(current_delta_R_CaloJets_asggH<0.4 && current_delta_R_CaloJets_asggH<delta_R_CaloJets_asggH && isggH)
		  //this implements all the reasonable possibilities!
		  {
		    delta_R_CaloJets_asggH = min(delta_R_CaloJets_asggH,current_delta_R_CaloJets_asggH);
		    //if(isVerbose) std::cout << "This calo jet removed because overlaps VBF pair: pt " << CaloJetsVect[r].pt() << " ; eta: " << CaloJetsVect[r].eta() << " ; phi: " << CaloJetsVect[r].phi() << std::endl;
		    CaloJetsVect.erase(CaloJetsVect.begin()+r);
		  }
	      }//ggH jet removed
	  }


      }

    nCaloJets = CaloJetsVect.size();


    // for gen matching, to be filled later
    std::vector<bool> caloGenMatched;
    std::vector<float> caloGenMatchedRadius2D;
    std::vector<float> caloGenMatchedEta;
    for(unsigned int i = 0; i < CaloJetsVect.size(); i++) 
      {
	caloGenMatched.push_back(false);//to be implemented later
	caloGenMatchedRadius2D.push_back(-1000.);
	caloGenMatchedEta.push_back(-999.);
      }

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
	      caloGenMatchedRadius2D[a] = GenBquarksVect[b].mother()? sqrt(pow(GenBquarksVect[b].vx() - GenBquarksVect[b].mother()->vx(),2) + pow(GenBquarksVect[b].vy() - GenBquarksVect[b].mother()->vy(),2)) : -1000.;
	      caloGenMatchedEta[a] = GenBquarksVect[b].eta();
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

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Vertices
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //if(isVerbose) std::cout << "Vertices" << std::endl;
    //PrimVertices.clear();
    //SecVertices.clear();

    std::vector<reco::Vertex> PVertexVect;
    std::vector<reco::VertexCompositePtrCandidate> SVertexVect;

    PVertexVect = theVertexAnalyzer->FillPvVector(iEvent);
    SVertexVect = theVertexAnalyzer->FillSvVector(iEvent);

    //for(unsigned int i = 0; i < PVertexVect.size(); i++) PrimVertices.push_back( VertexType() );
    //for(unsigned int i = 0; i < SVertexVect.size(); i++) SecVertices.push_back( VertexType() );

    //if(isVerbose) std::cout<< "PV position: x,y,z: " << PVertexVect.at(0).x() << " "<< PVertexVect.at(0).y() << " " << PVertexVect.at(0).z() << std::endl;
    number_of_PV = PVertexVect.size();
    number_of_SV = SVertexVect.size();
    nSV = number_of_SV;

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // PFCandidates
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //if(isVerbose) std::cout << "PF candidates" << std::endl;
    PFCandidates.clear();

    // PFCandidate variables
    std::vector<pat::PackedCandidate> PFCandidateVect;
    std::vector<int> PFCandidateAK4JetIndex;
    std::vector<int> PFCandidateAK8JetIndex;
    std::vector<int> PFCandidateVtxIndex;

    std::vector<reco::CandSecondaryVertexTagInfo *> bTagInfoVect;
    std::vector<reco::CandIPTagInfo *> bTagIPInfoVect;
    std::vector<int> indexSVJet;

    PFCandidateVect = thePFCandidateAnalyzer->FillPFCandidateVector(iEvent);

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
    //unsigned int nPFCandidatesMatchedToAK8Jet = 0;
    //unsigned int nPFCandidatesMatchedToAnyJet = 0;

    for(unsigned int i = 0; i < PFCandidateVect.size(); i++){

      int nMatchedAK4Jets = 0; // TODO: Remove if no warnings are observed during a large production.
      int nMatchedAK8Jets = 0;
      int nMatchedPVs = 0;

      // AK4 Jets
      for(unsigned int j = 0; j < CHSJetsVect.size(); j++){

	std::vector<edm::Ptr<reco::Candidate>> JetConstituentVect = CHSJetsVect[j].getJetConstituents();
	for(unsigned int k = 0; k < JetConstituentVect.size(); k++){
	  if (PFCandidateVect[i].p4() == JetConstituentVect[k]->p4()){
            //std::cout<<"debug zero!!! nothing matches bw jet constituents and pf cand!!!" <<std::endl;
	    PFCandidateAK4JetIndex[i]=j;
	    nMatchedAK4Jets++;
	    nPFCandidatesMatchedToAK4Jet++;
            //nPFCandidatesMatchedToAnyJet++;
	  }

	}

      }

      if (nMatchedAK4Jets > 1) edm::LogWarning("PFCandidate-Jet Matching") << "More than 1 AK4 jet contituent has been matched to PFCandidate";


     // PVs
      for(unsigned int j = 0; j < PVertexVect.size(); j++){

	if (PFCandidateVect[i].vertexRef()->position() == PVertexVect[j].position()){
	  PFCandidateVtxIndex[i]=j;
	  nMatchedPVs++;
	}
      }

      if (nMatchedPVs > 1) edm::LogWarning("PFCandidate-PV") << "WARNING: More than 1 PV has been matched to PFCandidate " << i << std::endl;


    }

    if(WriteAK4JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK4Jet; i++) PFCandidates.push_back( PFCandidateType() );
    //if(WriteAK8JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK8Jet; i++) PFCandidates.push_back( PFCandidateType() );
    //if(WriteAllJetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAnyJet; i++) PFCandidates.push_back( PFCandidateType() );
    if(WriteAllPFCandidates)    for(unsigned int i = 0; i < PFCandidateVect.size();       i++) PFCandidates.push_back( PFCandidateType() );

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // EXO-16-003 variables and and n(Pixel)Hits //TODO: Move to separate analyzer!
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //general tracks handle
    edm::Handle<std::vector<reco::Track>> generalTracks;
    iEvent.getByToken(generalTracksToken,generalTracks);
    //std::cout << "general tracks size? " << generalTracks->size() << std::endl;
    
    edm::Handle<edm::View<reco::Track> > generalTracksView;
    iEvent.getByToken(generalTracksViewToken,generalTracksView);


    // Magnetic field
    edm::ESHandle<MagneticField> MagneticField;
    iSetup.get<IdealMagneticFieldRecord>().get(MagneticField);
    MagneticFieldTag = &*MagneticField;
    // Propagator
    std::string PropagatorName = "PropagatorWithMaterial";
    iSetup.get<TrackingComponentsRecord>().get(PropagatorName,PropagatorHandle);
    StateOnTrackerBound stateOnTracker(PropagatorHandle.product());

    //Loop on jets    
    for (unsigned int j = 0; j < CHSJetsVect.size(); j++){
    
      //std::cout << "- - - - - - - - - - - -" << std::endl;
      //std::cout << "Jet n. " << j << std::endl;
      //int jj = j;
      // Initialize jet variables from PFCandidates:
      //float sumPtJet = 0.;
      //std::vector<float> sumPtPV;
      //std::vector<float> deltaRPV;//L
      //std::vector<float> sigIP2D;
      //std::vector<float> theta2D;
      //std::vector<float> POCA_theta2D;
      //std::vector<float> nPixelHits;
      //std::vector<float> nHits;
      //std::vector<float> dzVect;
      //std::vector<float> dxyVect;


      //Caltech; some still to be understood
      reco::Vertex primaryVertex = PVertexVect.at(0);
      std::vector<float> IP2Ds;
      std::vector<float> theta2Ds;
      std::vector<float> nPixelHits;//method seems not available
      std::vector<float> nHits;
      std::vector<float> dzVect;
      std::vector<float> dxyVect;
      
      float ptAllTracks = 0.;//Caltech: pt sum of generalTracks inside jet cone
      float ptAllPVTracks = 0.;//Caltech: pt sum of tracks belonging to any PV inside jet cone
      float ptPVTracksMax = 0.;//Caltech: maximum pt sum of tracks in a vertex inside jet cone
      int   nTracksAll = 0;//Caltech: num of generalTracks inside jet cone
      int   nTracksPVMax = 0;//Caltech: maximum number of tracks in a vertex inside jet cone
      
      float medianIP2D = -10000.;
      float medianTheta2D = -100.;
      
      float alphaMax = -100.;
      float betaMax = -100.;
      float gammaMax = -100.;
      float gammaMaxEM = -100.;
      float gammaMaxHadronic = -100.;
      float gammaMaxET = -100.;
      //float sigIP2DMedian = -10000.;
      //float theta2DMedian = -100.;
      //float POCA_theta2DMedian = -100.;
      float nPixelHitsMedian = -1.;
      float nHitsMedian = -1.;
      float dzMedian = -9999.;
      float dxyMedian = -9999.;
      float minDeltaRAllTracks = 999.;//Caltech: min DR bw generalTracks and current jet
      float minDeltaRPVTracks = 999.;//Caltech: min DR bw a track included in a vertex and current jet; there is a pt constraint on the total pt of tracks associated to a jet. Ask why
      
      //int nTrackConstituentsWithPtLarger0p95 = 0;
      //int nTrackConstituentsWithTrackDetails = 0;
      //int nTrackConstituentsWithTrackDetailsPtLarger0p95 = 0; 
 


      /* Track loop */
      //int iterator_valid_track = 0;
      for (unsigned int iTrack = 0; iTrack < generalTracks->size(); iTrack ++){

        // Track propagation
        FreeTrajectoryState fts = trajectoryStateTransform::initialFreeState (generalTracksView->at(iTrack),MagneticFieldTag);
        TrajectoryStateOnSurface outer = stateOnTracker(fts);
        if(!outer.isValid()) continue;
        GlobalPoint outerPos = outer.globalPosition();

        TLorentzVector generalTrackVecTemp;
        generalTrackVecTemp.SetPtEtaPhiM((generalTracks->at(iTrack)).pt(), outerPos.eta(), outerPos.phi(), 0);

        if ((generalTracks->at(iTrack)).pt() > 1) {
          //std::cout << "Valid track n. " << iterator_valid_track << std::endl;
          //iterator_valid_track++;
          //std::cout << "Valid track: " << generalTracks->at(iTrack).pt() << std::endl;
          if (minDeltaRAllTracks > reco::deltaR(generalTrackVecTemp.Eta(),generalTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi()) )
	  {
	      minDeltaRAllTracks =  reco::deltaR(generalTrackVecTemp.Eta(),generalTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi());
	      //std::cout << "minDeltaRAllTracks " << minDeltaRAllTracks << std::endl;
	  }
	  if (reco::deltaR(generalTrackVecTemp.Eta(),generalTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi()) < 0.4)
	  {
    	  	nTracksAll ++;
    	  	//tot pt for alpha
    	 	ptAllTracks += (generalTracks->at(iTrack)).pt();	                   
                 nPixelHits.push_back((generalTracks->at(iTrack)).hitPattern().numberOfValidPixelHits());
                 nHits.push_back((generalTracks->at(iTrack)).hitPattern().numberOfValidTrackerHits());
                 dzVect.push_back((generalTracks->at(iTrack)).dz());
                 dxyVect.push_back((generalTracks->at(iTrack)).dxy());
    	 	//std::cout << "Track n. " << iterator_valid_track << " in jet! its pt" << (generalTracks->at(iTrack)).pt() << ", nTracksAll: " << nTracksAll << ", ptAllTracks: " << ptAllTracks  << std::endl;

           }//if track in jet cone
        }//if tracks pt>1 GeV
        
      }//loop on general tracks
 


      /*Vertex loop */
      if (ptAllTracks > 0.9){
        //No matched jets
        //int iterator_vertex = 0;
        for (auto vertex = PVertexVect.begin(); vertex != PVertexVect.end(); vertex++){
          double ptPVTracks = 0.;//pt of tracks associated to one singular PV and inside current jet cone
          int nTracksPVTemp = 0;//number of tracks associated to one singular PV and inside current jet cone
          if(!vertex->isValid())continue;
          if (vertex->isFake())continue;
          //std::cout << "Valid vertex n. " << iterator_vertex << std::endl;
          //iterator_vertex++;
          for(auto pvTrack=vertex->tracks_begin(); pvTrack!=vertex->tracks_end(); pvTrack++){

              // Track propagation
              FreeTrajectoryState ftspv = trajectoryStateTransform::initialFreeState (**pvTrack, MagneticFieldTag);
              TrajectoryStateOnSurface outerpv = stateOnTracker(ftspv);
              if(!outerpv.isValid()) continue;
              GlobalPoint outerpvPos = outerpv.globalPosition();

    	      TLorentzVector pvTrackVecTemp;
    	      pvTrackVecTemp.SetPtEtaPhiM((*pvTrack)->pt(),outerpvPos.eta(),outerpvPos.phi(),0);
  	      //If pv track associated with jet add pt to ptPVTracks
    	      if ((*pvTrack)->pt() > 1)
    	      {
    	        if (minDeltaRPVTracks > reco::deltaR(pvTrackVecTemp.Eta(),pvTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi()))
    	        {
    	          minDeltaRPVTracks =  reco::deltaR(pvTrackVecTemp.Eta(),pvTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi());
    	        }
    	        if(reco::deltaR(pvTrackVecTemp.Eta(),pvTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi()) < 0.4)
    	        {
    	           //std::cout << "Valid track inside vertex n. " << iterator_vertex << "; track pt: " << (*pvTrack)->pt() << std::endl;
                   ptPVTracks += (*pvTrack)->pt();//pt sum per vertex
                   ptAllPVTracks += (*pvTrack)->pt();//pt sum over all vertices
                   nTracksPVTemp++;//number of tracks associated to one particular vertex
    	        }//jet matching
              }//minimum track pt
           
              if (ptPVTracks > ptPVTracksMax) {
      	        ptPVTracksMax = ptPVTracks;
      	        nTracksPVMax = nTracksPVTemp;
      	      }
      	     
          }//loop on vertex tracks
           
         //alphaMax = ptAllTracks>0 ? ptPVTracksMax/ptAllTracks : -100.;
         //std::cout << "Still inside vertex n. " << iterator_vertex << "; ptPVTracksMax: " << ptPVTracksMax << "; nTracksPVMax: " << nTracksPVMax << "; alphaMax: " << alphaMax << std::endl;
  	}//loop on vertices
  	
      }//if pt all tracks
 


      /* Track loop, without propagator, for sigIP2D and theta2D */
      for (unsigned int iTrack = 0; iTrack < generalTracks->size(); iTrack ++){
  	reco::Track generalTrack = generalTracks->at(iTrack);
  	TLorentzVector generalTrackVecTemp;
  	generalTrackVecTemp.SetPtEtaPhiM(generalTrack.pt(),generalTrack.eta(),generalTrack.phi(),0);

  	if (generalTrack.pt() > 1) {
	    if (reco::deltaR(generalTrackVecTemp.Eta(),generalTrackVecTemp.Phi(),CHSJetsVect.at(j).eta(),CHSJetsVect.at(j).phi()) < 0.4){
    		// Theta 2D
    		//WARNING! This gives product not found! TODO!
    		//ROOT::Math::XYZPoint innerPos = generalTrack.innerPosition();
    		//std::cout << innerPos << std::endl;
    		//ROOT::Math::XYZPoint vertexPos = primaryVertex.position();
    		//std::cout << vertexPos << std::endl;
    		//ROOT::Math::XYZVector deltaPos = innerPos - vertexPos;
    		//ROOT::Math::XYZVector momentum = generalTrack.innerMomentum();
    		//double mag2DeltaPos = TMath::Sqrt((deltaPos.x()*deltaPos.x()) + (deltaPos.y()*deltaPos.y()));
    		//double mag2Mom = TMath::Sqrt((momentum.x()*momentum.x()) + (momentum.y()*momentum.y()));
    		//double theta2D = TMath::ACos((deltaPos.x()*momentum.x()+deltaPos.y()*momentum.y())/(mag2Mom*mag2DeltaPos));
    		//theta2Ds.push_back(theta2D);

    		// IP sig
    		edm::ESHandle<TransientTrackBuilder> theB;
    		iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);
    		reco::TransientTrack transTrack = theB->build(generalTrack);
    		TrajectoryStateClosestToBeamLine traj = transTrack.stateAtBeamLine();
    		Measurement1D meas = traj.transverseImpactParameter();
    		std::pair<bool, Measurement1D> ip2d = IPTools::absoluteTransverseImpactParameter(transTrack,primaryVertex);
    		IP2Ds.push_back(ip2d.second.value()/ip2d.second.error());
            }//jet DR matching
        }//track pt>1 GeV
        
      }//second loop on general tracks



      std::sort(IP2Ds.begin(),IP2Ds.end());
      //if (IP2Ds.size() % 2 == 0) medianIP2D = ((IP2Ds[IP2Ds.size()/2 -1] + IP2Ds[IP2Ds.size()/2) /2);//HH
      //else medianIP2D = IP2Ds[IP2Ds.size()/2];//HH
      if (IP2Ds.size() > 0){
	   medianIP2D = IP2Ds[IP2Ds.size()/2];
      }
      
      std::sort(theta2Ds.begin(),theta2Ds.end());
      //if (theta2Ds.size() % 2 == 0) medianTheta2D = ((theta2Ds[theta2Ds.size()/2 -1] + theta2Ds[theta2Ds.size()/2) /2);//HH
      //else medianTheta2D = theta2Ds[theta2Ds.size()/2];//HH
      if (theta2Ds.size() > 0){
          medianTheta2D = theta2Ds[theta2Ds.size()/2];
      }

      std::sort(nPixelHits.begin(), nPixelHits.end());
      if (nPixelHits.size() > 0) {   
        if (nPixelHits.size() % 2 ==0) nPixelHitsMedian = ((nPixelHits[nPixelHits.size()/2 -1] + nPixelHits[nPixelHits.size()/2]) /2);
        else nPixelHitsMedian = nPixelHits[nPixelHits.size()/2];
      }
      
      std::sort(nHits.begin(), nHits.end());
      if (nHits.size() > 0) {   
        if (nHits.size() % 2 ==0) nHitsMedian = ((nHits[nHits.size()/2 -1] + nHits[nHits.size()/2]) /2);
        else nHitsMedian = nHits[nHits.size()/2];
      }

      std::sort(dxyVect.begin(), dxyVect.end());
      if (dxyVect.size() > 0) {
	if (dxyVect.size() % 2 ==0) dxyMedian = ((dxyVect[dxyVect.size()/2 -1] + dxyVect[dxyVect.size()/2]) /2);
	else dxyMedian = dxyVect[dxyVect.size()/2];
      }

      std::sort(dzVect.begin(), dzVect.end());
      if (dzVect.size() > 0) {
	if (dzVect.size() % 2 ==0) dzMedian = ((dzVect[dzVect.size()/2 -1] + dzVect[dzVect.size()/2]) /2);
	else dzMedian = dzVect[dzVect.size()/2];
      }
      
      //std::cout << "Out of vertex loop, recalculate alphaMax " << std::endl;
      alphaMax         = ptAllTracks>0 ? ptPVTracksMax/ptAllTracks : -100.;
      betaMax          = ptAllTracks>0 ? ptPVTracksMax/CHSJetsVect[j].pt() : -100.;
      gammaMax         = ptAllTracks>0 ? ptPVTracksMax/CHSJetsVect[j].energy() : -100.;
      gammaMaxEM       = ( (CHSJetsVect[j].userFloat("photonEFrac") + CHSJetsVect[j].userFloat("eleEFrac"))>0 && ptAllTracks>0 ) ? ptPVTracksMax/(CHSJetsVect[j].energy()*(CHSJetsVect[j].userFloat("photonEFrac") + CHSJetsVect[j].userFloat("eleEFrac"))) : -100.;
      gammaMaxHadronic = ( (CHSJetsVect[j].userFloat("cHadEFrac") + CHSJetsVect[j].userFloat("nHadEFrac"))>0 && ptAllTracks>0 ) ? ptPVTracksMax/(CHSJetsVect[j].energy()*(CHSJetsVect[j].userFloat("cHadEFrac") + CHSJetsVect[j].userFloat("nHadEFrac"))) : -100.;
      gammaMaxET       = ptAllTracks>0 ? ptPVTracksMax/CHSJetsVect[j].et() : -100.;    
      //std::cout << "Jet[" << j << "] has nTracksAll: " << nTracksAll << "; and ptAllTracks: " << ptAllTracks << " and nTracksPVMax " << nTracksPVMax << " and ptPVTracksMax " << ptPVTracksMax << "; alphaMax " << alphaMax << "; medianIP2D " << medianIP2D << "; medianTheta2D " << medianTheta2D << std::endl;


      CHSJetsVect[j].addUserInt("nTracksAll", nTracksAll);
      CHSJetsVect[j].addUserInt("nTracksPVMax", nTracksPVMax);
      CHSJetsVect[j].addUserFloat("ptAllTracks", ptAllTracks>0 ? ptAllTracks : -1.);
      CHSJetsVect[j].addUserFloat("ptAllPVTracks", ptAllPVTracks>0 ? ptAllPVTracks : -1.);
      CHSJetsVect[j].addUserFloat("ptPVTracksMax", ptPVTracksMax>0 ? ptPVTracksMax : -1.);
      CHSJetsVect[j].addUserFloat("alphaMax", alphaMax);
      CHSJetsVect[j].addUserFloat("betaMax", betaMax);//zero if no tracks
      CHSJetsVect[j].addUserFloat("gammaMax", gammaMax);//zero if no tracks
      CHSJetsVect[j].addUserFloat("gammaMaxEM", gammaMaxEM);//zero if no tracks, but -100 if no EM EFrac
      CHSJetsVect[j].addUserFloat("gammaMaxHadronic", gammaMaxHadronic);//zero if no tracks, but -100 if no hadronEFrac
      CHSJetsVect[j].addUserFloat("gammaMaxET", gammaMaxET);//zero if no tracks
      CHSJetsVect[j].addUserFloat("minDeltaRAllTracks",minDeltaRAllTracks);
      CHSJetsVect[j].addUserFloat("minDeltaRPVTracks",minDeltaRPVTracks);
      CHSJetsVect[j].addUserFloat("medianIP2D", medianIP2D);
      CHSJetsVect[j].addUserFloat("medianTheta2D", medianTheta2D);
      CHSJetsVect[j].addUserFloat("nPixelHitsMedian", nPixelHitsMedian);
      CHSJetsVect[j].addUserFloat("nHitsMedian", nHitsMedian);
      CHSJetsVect[j].addUserFloat("dxyMedian", dxyMedian);
      CHSJetsVect[j].addUserFloat("dzMedian", dzMedian);
      
    }//loop on AK4 jets
 

 
   


    // AK4 jets
    /* OLD LOOP, with PFCandidates */
    for (unsigned int j = 0; j < CHSJetsVect.size(); j++){
    
      int jj = j;
      // Initialize jet variables from PFCandidates:
      float sumPtJetOld = 0.;
      std::vector<float> sumPtPVOld;
      //std::vector<float> deltaRPV;//L
      std::vector<float> sigIP2DOld;
      std::vector<float> theta2DOld;
      std::vector<float> POCA_theta2DOld;
      std::vector<float> nPixelHitsOld;
      std::vector<float> nHitsOld;
      std::vector<float> dzVectOld;
      std::vector<float> dxyVectOld;


      float alphaMaxOld = -100.;
      float betaMaxOld = -100.;
      float gammaMaxOld = -100.;
      float gammaMaxEMOld = -100.;
      float gammaMaxHadronicOld = -100.;
      float gammaMaxETOld = -100.;
      float sigIP2DMedianOld = -10000.;
      float theta2DMedianOld = -100.;
      float POCA_theta2DMedianOld = -100.;
      float nPixelHitsMedianOld = -1.;
      float nHitsMedianOld = -1.;
      float dzMedianOld = -9999.;
      float dxyMedianOld = -9999.;
      //float minDeltaRAllTracks = 999.;
      //float minDeltaRPVTracks = 999.;//L
      //float minDeltaRAllTracksInJet = 999.;
      //float minDeltaRPVTracksInJet = 999.;//L

      int nTracks0PixelHitsOld = 0;
      int nTracks1PixelHitOld = 0;
      int nTracks2PixelHitsOld = 0;
      int nTracks3PixelHitsOld = 0;
      int nTracks4PixelHitsOld = 0;
      int nTracks5PixelHitsOld = 0;
      int nTracksAtLeast6PixelHitsOld = 0;
      int nTracksValidHitInBPix1Old = 0;
      int nTracks0LostInnerHitsOld = 0;
      int nTracks1LostInnerHitOld = 0;
      int nTracksAtLeast2LostInnerHitsOld = 0;
      
      int nTrackConstituentsWithPtLarger0p95 = 0;
      int nTrackConstituentsWithTrackDetails = 0;
      int nTrackConstituentsWithTrackDetailsPtLarger0p95 = 0;

      // Initialize vertex variable
      for(unsigned int i = 0; i < PVertexVect.size(); i++)
      {
          sumPtPVOld.push_back(0.);
          //deltaRPV.push_back(999.);//L
      }

      //calculate Caltech's variable
      //for(unsigned int v = 0; v < PVertexVect.size(); v++)
      //{
      //    //std::cout << "Vertex n. " << v << std::endl;
      //    float temp_DR = 999.;//re-initialize every vertex
      //    float temp_DR_in_jet = 999.;
      //    for(unsigned int p = 0; p < PFCandidateVect.size(); p++)
      //    {
      //        
      //        if(PFCandidateVect[p].charge()!=0 and (PFCandidateVect[p].vertexRef()->position() == PVertexVect[v].position()) )//if pfcand has a charge and pf cand in same vertex position
      //        {
      //        	 //std::cout << "PF cand n. " << p << std::endl;
      //            if( temp_DR > reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi()) )
      //            {
      //                temp_DR = reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi());
      //                //std::cout<< "temp_DR " << temp_DR << std::endl;
      //            }
      //            
      //            if(jj == PFCandidateAK4JetIndex[p] && (temp_DR_in_jet > reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi())) )
      //            {temp_DR_in_jet = reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi());}
      //        }
      //       
      //       
      //    }//loop on PF candidates
      //    //std::cout << "Best DR: " << temp_DR << std::endl;
      //    //std::cout << "***********" << std::endl;
      //    if(minDeltaRPVTracks>temp_DR) minDeltaRPVTracks=temp_DR;
      //    if(minDeltaRPVTracksInJet>temp_DR_in_jet) minDeltaRPVTracksInJet=temp_DR_in_jet;
      // 
      //}//loop on vertices
      ////std::cout << "Chosen DR: " << minDeltaRPVTracks << std::endl; 

      for(unsigned int p = 0; p < PFCandidateVect.size(); p++)
      {
            ////Calculate DR between jet and all tracks in the jet
            //if (PFCandidateVect[p].charge()!=0 and  (minDeltaRAllTracks > reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi())) )
            //{
            //    minDeltaRAllTracks =  reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi());
	    //}
	    
	    //if (jj == PFCandidateAK4JetIndex[p] && PFCandidateVect[p].charge()!=0 and  (minDeltaRAllTracksInJet > reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi())) )
            //{
            //    minDeltaRAllTracksInJet =  reco::deltaR(CHSJetsVect[j].eta(),CHSJetsVect[j].phi(),PFCandidateVect[p].eta(),PFCandidateVect[p].phi());
	    //}
	    
	    if (jj == PFCandidateAK4JetIndex[p] && PFCandidateVect[p].charge()!=0 && PFCandidateVect[p].pt()>0.95) nTrackConstituentsWithPtLarger0p95++;
	    if (jj == PFCandidateAK4JetIndex[p] && PFCandidateVect[p].charge()!=0 && PFCandidateVect[p].hasTrackDetails()) nTrackConstituentsWithTrackDetails++;
	    if (jj == PFCandidateAK4JetIndex[p] && PFCandidateVect[p].charge()!=0 && PFCandidateVect[p].hasTrackDetails() && PFCandidateVect[p].pt()>0.95) nTrackConstituentsWithTrackDetailsPtLarger0p95++;


      }//second loop over pf candidates

      for (unsigned int i = 0; i < PFCandidateVect.size(); i++){

	if (jj == PFCandidateAK4JetIndex[i]){
          //std::cout << " debugggggggg 1! " << std::endl;
	  //if (PFCandidateVect[i].charge()){
	  if (PFCandidateVect[i].charge() && PFCandidateVect[i].hasTrackDetails()){//NEW, more comparable to generalTracks
	    sumPtJetOld += PFCandidateVect[i].pt();
	    sumPtPVOld[PFCandidateVtxIndex[i]] += PFCandidateVect[i].pt();
	    
	    //sigIP2D.push_back(PFCandidateVect[i].dxy()/PFCandidateVect[i].dxyError()); //dxyError stored only for pT>0.95 (see below)
	    if (CHSJetsVect[j].hasTagInfo("pfSecondaryVertex")) {
	      reco::CandSecondaryVertexTagInfo const *svTagInfo = CHSJetsVect[j].tagInfoCandSecondaryVertex("pfSecondaryVertex");
	      if (svTagInfo->nVertices() > 0) {
		const GlobalVector &dir = svTagInfo->flightDirection(0);
		theta2DOld.push_back( std::acos( ( dir.x()*PFCandidateVect[i].px() + dir.y()*PFCandidateVect[i].py() ) /
					      ( std::sqrt(dir.x()*dir.x()+dir.y()*dir.y()) * PFCandidateVect[i].pt() ) ) );
					                  //if( (std::sqrt(dir.x()*dir.x()+dir.y()*dir.y()) * PFCandidateVect[i].pt()) ==0) std::cout<<"---> Warning, den 0 in theta2D!! " << EventNumber << std::endl;
	      }
	    }

            float px = PFCandidateVect[i].pt()*TMath::Cos(PFCandidateVect[i].phiAtVtx());
            float py = PFCandidateVect[i].pt()*TMath::Sin(PFCandidateVect[i].phiAtVtx());
            float vR = std::sqrt(PFCandidateVect[i].vx()*PFCandidateVect[i].vx() + PFCandidateVect[i].vy()*PFCandidateVect[i].vy());
            POCA_theta2DOld.push_back(std::acos((PFCandidateVect[i].vx()*px + PFCandidateVect[i].vy()*py) / (vR*PFCandidateVect[i].pt())));

            //if(PFCandidateVect[i].vx() ==0) std::cout<<"---> Warning, den 0 in POCA_theta2D!! " << EventNumber << std::endl;
	    // Full tracking info stored only for pT>0.95 GeV
	    // https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#Embedded_track_information
	    //if(PFCandidateVect[i].pt()>0.95 && PFCandidateVect[i].hasTrackDetails()) {//this looks more conservative
	    if(PFCandidateVect[i].hasTrackDetails()) {//NEW, more comparable to generalTracks
              //std::cout << " debugggggggg 2! " << std::endl;
              sigIP2DOld.push_back(PFCandidateVect[i].dxy()/PFCandidateVect[i].dxyError());

              nPixelHitsOld.push_back(PFCandidateVect[i].numberOfPixelHits());
              nHitsOld.push_back(PFCandidateVect[i].numberOfHits());

              if (PFCandidateVect[i].numberOfPixelHits() == 0) nTracks0PixelHitsOld++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 1) nTracks1PixelHitOld++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 2) nTracks2PixelHitsOld++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 3) nTracks3PixelHitsOld++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 4) nTracks4PixelHitsOld++;
              else if (PFCandidateVect[i].numberOfPixelHits() == 5) nTracks5PixelHitsOld++;
              else nTracksAtLeast6PixelHitsOld++;

              if (PFCandidateVect[i].lostInnerHits() == -1) nTracksValidHitInBPix1Old++;
              else if (PFCandidateVect[i].lostInnerHits() == 0) nTracks0LostInnerHitsOld++;
              else if (PFCandidateVect[i].lostInnerHits() == 1) nTracks1LostInnerHitOld++;
              else if (PFCandidateVect[i].lostInnerHits() == 2) nTracksAtLeast2LostInnerHitsOld++;

	      dxyVectOld.push_back(PFCandidateVect[i].dxy());
	      dzVectOld.push_back(PFCandidateVect[i].dz());

            } // pT selection
	  } // charge
	} // jet index
      } // loop over PFCandidates

      // TODO: Implement a median function to use for all vectors below:

      if (sumPtPVOld.size() > 0) {
	std::sort(sumPtPVOld.begin(), sumPtPVOld.end());
	alphaMaxOld = sumPtJetOld>0 ? sumPtPVOld[sumPtPVOld.size()-1]/sumPtJetOld : -100.;
	betaMaxOld  = sumPtJetOld>0 ? sumPtPVOld[sumPtPVOld.size()-1]/CHSJetsVect[j].pt() : -100.;
	gammaMaxOld = sumPtJetOld>0 ? sumPtPVOld[sumPtPVOld.size()-1]/CHSJetsVect[j].energy() : -100.;
	gammaMaxEMOld = ( (CHSJetsVect[j].userFloat("photonEFrac") + CHSJetsVect[j].userFloat("eleEFrac"))>0 && sumPtJetOld>0 ) ? sumPtPVOld[sumPtPVOld.size()-1]/(CHSJetsVect[j].energy()*(CHSJetsVect[j].userFloat("photonEFrac") + CHSJetsVect[j].userFloat("eleEFrac"))) : -100.;
	gammaMaxHadronicOld = ( (CHSJetsVect[j].userFloat("cHadEFrac") + CHSJetsVect[j].userFloat("nHadEFrac"))>0 && sumPtJetOld>0 ) ? sumPtPVOld[sumPtPVOld.size()-1]/(CHSJetsVect[j].energy()*(CHSJetsVect[j].userFloat("cHadEFrac") + CHSJetsVect[j].userFloat("nHadEFrac"))) : -100.;
	gammaMaxETOld = sumPtJetOld>0 ? sumPtPVOld[sumPtPVOld.size()-1]/CHSJetsVect[j].et() : -100.;
      }
      if (sigIP2DOld.size() > 0) {
	std::sort(sigIP2DOld.begin(), sigIP2DOld.end());
	if (sigIP2DOld.size() % 2 ==0) sigIP2DMedianOld = ((sigIP2DOld[sigIP2DOld.size()/2 -1] + sigIP2DOld[sigIP2DOld.size()/2]) /2);
	else sigIP2DMedianOld = sigIP2DOld[sigIP2DOld.size()/2];
      }
      if (theta2DOld.size() > 0) {
	std::sort(theta2DOld.begin(), theta2DOld.end());
	if (theta2DOld.size() % 2 ==0) theta2DMedianOld = ((theta2DOld[theta2DOld.size()/2 -1] + theta2DOld[theta2DOld.size()/2]) /2);
	else theta2DMedianOld = theta2DOld[theta2DOld.size()/2];
      }
      if (POCA_theta2DOld.size() > 0) {
        std::sort(POCA_theta2DOld.begin(), POCA_theta2DOld.end());
        if (POCA_theta2DOld.size() % 2 ==0) POCA_theta2DMedianOld = ((POCA_theta2DOld[POCA_theta2DOld.size()/2 -1] + POCA_theta2DOld[POCA_theta2DOld.size()/2]) /2);
        else POCA_theta2DMedianOld = POCA_theta2DOld[POCA_theta2DOld.size()/2];
      }
      if (nPixelHitsOld.size() > 0) {
        std::sort(nPixelHitsOld.begin(), nPixelHitsOld.end());
        if (nPixelHitsOld.size() % 2 ==0) nPixelHitsMedianOld = ((nPixelHitsOld[nPixelHitsOld.size()/2 -1] + nPixelHitsOld[nPixelHitsOld.size()/2]) /2);
        else nPixelHitsMedianOld = nPixelHitsOld[nPixelHitsOld.size()/2];
      }
      if (nHitsOld.size() > 0) {
        std::sort(nHitsOld.begin(), nHitsOld.end());
        if (nHitsOld.size() % 2 ==0) nHitsMedianOld = ((nHitsOld[nHitsOld.size()/2 -1] + nHitsOld[nHitsOld.size()/2]) /2);
        else nHitsMedianOld = nHitsOld[nHitsOld.size()/2];
      }

      if (CHSJetsVect[j].hasTagInfo("pfSecondaryVertex")) {
	reco::CandSecondaryVertexTagInfo const *svTagInfo = CHSJetsVect[j].tagInfoCandSecondaryVertex("pfSecondaryVertex");
	bTagInfoVect.push_back(svTagInfo->clone());
	reco::CandIPTagInfo const *ipTagInfo = CHSJetsVect[j].tagInfoCandIP("pfImpactParameter");
        bTagIPInfoVect.push_back(ipTagInfo->clone());
	indexSVJet.push_back(j);
      }

      if (dxyVectOld.size() > 0) {
	std::sort(dxyVectOld.begin(), dxyVectOld.end());
	if (dxyVectOld.size() % 2 ==0) dxyMedianOld = ((dxyVectOld[dxyVectOld.size()/2 -1] + dxyVectOld[dxyVectOld.size()/2]) /2);
	else dxyMedianOld = dxyVectOld[dxyVectOld.size()/2];
      }

      if (dzVectOld.size() > 0) {
	std::sort(dzVectOld.begin(), dzVectOld.end());
	if (dzVectOld.size() % 2 ==0) dzMedianOld = ((dzVectOld[dzVectOld.size()/2 -1] + dzVectOld[dzVectOld.size()/2]) /2);
	else dzMedianOld = dzVectOld[dzVectOld.size()/2];
      }

      CHSJetsVect[j].addUserFloat("alphaMaxOld", alphaMaxOld);
      CHSJetsVect[j].addUserFloat("sumPtJetOld", sumPtJetOld>0 ? sumPtJetOld : -1.);
      CHSJetsVect[j].addUserFloat("betaMaxOld", betaMaxOld);//zero if no tracks
      CHSJetsVect[j].addUserFloat("gammaMaxOld", gammaMaxOld);//zero if no tracks
      CHSJetsVect[j].addUserFloat("gammaMaxEMOld", gammaMaxEMOld);//zero if no tracks, but -100 if no EM EFrac
      CHSJetsVect[j].addUserFloat("gammaMaxHadronicOld", gammaMaxHadronicOld);//zero if no tracks, but -100 if no hadronEFrac
      CHSJetsVect[j].addUserFloat("gammaMaxETOld", gammaMaxETOld);//zero if no tracks
      
      //CHSJetsVect[j].addUserFloat("minDeltaRAllTracks",minDeltaRAllTracks);
      //CHSJetsVect[j].addUserFloat("minDeltaRPVTracks",minDeltaRPVTracks);
      //CHSJetsVect[j].addUserFloat("minDeltaRAllTracksInJet",minDeltaRAllTracksInJet);
      //CHSJetsVect[j].addUserFloat("minDeltaRPVTracksInJet",minDeltaRPVTracksInJet);
      
      CHSJetsVect[j].addUserFloat("sigIP2DMedianOld", sigIP2DMedianOld);
      CHSJetsVect[j].addUserFloat("theta2DMedianOld", theta2DMedianOld);
      CHSJetsVect[j].addUserFloat("POCA_theta2DMedianOld", POCA_theta2DMedianOld);
      CHSJetsVect[j].addUserFloat("nPixelHitsMedianOld", nPixelHitsMedianOld);
      CHSJetsVect[j].addUserFloat("nHitsMedianOld", nHitsMedianOld);

      CHSJetsVect[j].addUserFloat("dxyMedianOld", dxyMedianOld);
      CHSJetsVect[j].addUserFloat("dzMedianOld", dzMedianOld);
    
      CHSJetsVect[j].addUserInt("nTracks0PixelHits", nTracks0PixelHitsOld);
      CHSJetsVect[j].addUserInt("nTracks1PixelHit", nTracks1PixelHitOld);
      CHSJetsVect[j].addUserInt("nTracks2PixelHits", nTracks2PixelHitsOld);
      CHSJetsVect[j].addUserInt("nTracks3PixelHits", nTracks3PixelHitsOld);
      CHSJetsVect[j].addUserInt("nTracks4PixelHits", nTracks4PixelHitsOld);
      CHSJetsVect[j].addUserInt("nTracks5PixelHits", nTracks5PixelHitsOld);
      CHSJetsVect[j].addUserInt("nTracksAtLeast6PixelHits", nTracksAtLeast6PixelHitsOld);
      CHSJetsVect[j].addUserInt("nTracksValidHitInBPix1", nTracksValidHitInBPix1Old);
      CHSJetsVect[j].addUserInt("nTracks0LostInnerHits", nTracks0LostInnerHitsOld);
      CHSJetsVect[j].addUserInt("nTracks1LostInnerHit", nTracks1LostInnerHitOld);
      CHSJetsVect[j].addUserInt("nTracksAtLeast2LostInnerHits", nTracksAtLeast2LostInnerHitsOld);
      
      CHSJetsVect[j].addUserInt("nTrackConstituentsWithPtLarger0p95",nTrackConstituentsWithPtLarger0p95);
      CHSJetsVect[j].addUserInt("nTrackConstituentsWithTrackDetails",nTrackConstituentsWithTrackDetails);
      CHSJetsVect[j].addUserInt("nTrackConstituentsWithTrackDetailsPtLarger0p95",nTrackConstituentsWithTrackDetailsPtLarger0p95);

    }//end of EXO-16-003 variables for AK4 Jets
    
    

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // DT segments
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
   

    std::vector<DTRecSegment4D> DTSegmentVect = theDTAnalyzer->FillDTSegment4DVector(iEvent);
    std::vector<GlobalPoint> DTSegment_Global_points = theDTAnalyzer->FillGlobalPointDT4DSegmentVector(iEvent, iSetup,DTSegmentVect);
    for(unsigned int i =0; i< DTSegmentVect.size();i++) DTRecSegments4D.push_back( DT4DSegmentType() );

    nDTSegments = DTSegmentVect.size();
    for(unsigned int i = 0; i < DTSegmentVect.size(); i++)
      {
	//std::cout << DTSegmentVect.at(i).recHits << std::endl;
	if(DTSegmentVect.at(i).chamberId().station()==1) nDTSegmentsStation1++;
	if(DTSegmentVect.at(i).chamberId().station()==2) nDTSegmentsStation2++;
	if(DTSegmentVect.at(i).chamberId().station()==3) nDTSegmentsStation3++;
	if(DTSegmentVect.at(i).chamberId().station()==4) nDTSegmentsStation4++;
      }
    

    for(unsigned int s = 0; s < DTSegment_Global_points.size(); s++)
      {

	for(unsigned int b = 0; b < GenBquarksVect.size(); b++)
	  {

	    if(reco::deltaR(DTSegment_Global_points[s].eta(),DTSegment_Global_points[s].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi())<0.4)
	      {
		if(b==0) n_segments_around_b_quark_0++;
		if(b==1) n_segments_around_b_quark_1++;
		if(b==2) n_segments_around_b_quark_2++;
		if(b==3) n_segments_around_b_quark_3++;
	      }
	  }
      }

    // Match DT Segments to Gen b quarks
   
    // for gen matching, to be filled later
    std::vector<bool> DTGenMatched;
    for(unsigned int i = 0; i < DTSegmentVect.size(); i++) DTGenMatched.push_back(false);//to be implemented later

    std::vector<DTRecSegment4D> MatchedDTSegment4DVect;
    //Matching the b quarks to AK4 calo jets
    //Starting point: b-quark
    int matching_index_DTSegment4D;//local variable
    float delta_R_DTSegment4D;//local variable
    float current_delta_R_DTSegment4D;//local variable
    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
        {
        delta_R_DTSegment4D = 1000.;
        current_delta_R_DTSegment4D = 1000.;
        matching_index_DTSegment4D = -1;
        for(unsigned int a = 0; a<DTSegmentVect.size(); a++)
            {
            current_delta_R_DTSegment4D = fabs(reco::deltaR(DTSegment_Global_points[a].eta(),DTSegment_Global_points[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
            if(current_delta_R_DTSegment4D<0.4 && current_delta_R_DTSegment4D<delta_R_DTSegment4D)
                //this implements all the reasonable possibilities!
                {
                delta_R_DTSegment4D = min(delta_R_DTSegment4D,current_delta_R_DTSegment4D);
                matching_index_DTSegment4D = a;
                DTGenMatched[a] = true;
                //JetsVect[a].addUserInt("original_jet_index",a+1);
                MatchedDTSegment4DVect.push_back(DTSegmentVect[a]);//avoid duplicates!
                }
            }
        if(matching_index_DTSegment4D>=0){
            number_of_b_matched_to_DTSegment4D++;
        }
        }
    //Remove duplicates from Matched Jets Vector
    for(unsigned int r = 0; r<MatchedDTSegment4DVect.size(); r++)
        {
        for(unsigned int s = 0; s<MatchedDTSegment4DVect.size(); s++)
            {
            if(r!=s && MatchedDTSegment4DVect[s].localPosition()==MatchedDTSegment4DVect[r].localPosition()) MatchedDTSegment4DVect.erase(MatchedDTSegment4DVect.begin()+s);
            }//duplicates removed
        }
    nMatchedDTsegmentstob = MatchedDTSegment4DVect.size();

    // Match DT Segments to VBF jets
    
    
    // for gen matching, to be filled later
    std::vector<bool> DTVBFMatched;
    for(unsigned int i = 0; i < DTSegmentVect.size(); i++) DTVBFMatched.push_back(false);//to be implemented later

    std::vector<DTRecSegment4D> MatchedDTSegment4DtoVBFVect;
    //Matching the b quarks to AK4 calo jets
    //Starting point: b-quark
    int matching_index_DTSegment4D_VBF;//local variable
    float delta_R_DTSegment4D_VBF;//local variable
    float current_delta_R_DTSegment4D_VBF;//local variable
    for(unsigned int j = 0; j<VBFPairJetsVect.size(); j++)
        {
        delta_R_DTSegment4D_VBF = 1000.;
        current_delta_R_DTSegment4D_VBF = 1000.;
        matching_index_DTSegment4D_VBF = -1;
        for(unsigned int a = 0; a<DTSegmentVect.size(); a++)
            {
            current_delta_R_DTSegment4D = fabs(reco::deltaR(DTSegment_Global_points[a].eta(),DTSegment_Global_points[a].phi(),VBFPairJetsVect[j].eta(),VBFPairJetsVect[j].phi()));
            if(current_delta_R_DTSegment4D_VBF<0.4 && current_delta_R_DTSegment4D_VBF<delta_R_DTSegment4D_VBF)
                //this implements all the reasonable possibilities!
                {
                delta_R_DTSegment4D_VBF = min(delta_R_DTSegment4D_VBF,current_delta_R_DTSegment4D_VBF);
                matching_index_DTSegment4D_VBF = a;
                DTVBFMatched[a] = true;
                //JetsVect[a].addUserInt("original_jet_index",a+1);
                MatchedDTSegment4DtoVBFVect.push_back(DTSegmentVect[a]);//avoid duplicates!
                }
            }
        if(matching_index_DTSegment4D_VBF>=0){
            number_of_VBF_matched_to_DTSegment4D++;
        }
        }
    //Remove duplicates from Matched Jets Vector
    for(unsigned int r = 0; r<MatchedDTSegment4DtoVBFVect.size(); r++)
        {
        for(unsigned int s = 0; s<MatchedDTSegment4DtoVBFVect.size(); s++)
            {
            if(r!=s && MatchedDTSegment4DtoVBFVect[s].localPosition()==MatchedDTSegment4DtoVBFVect[r].localPosition()) MatchedDTSegment4DtoVBFVect.erase(MatchedDTSegment4DtoVBFVect.begin()+s);
            }//duplicates removed
        }
    nMatchedDTsegmentstoVBF = MatchedDTSegment4DtoVBFVect.size();
    
    
   
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // CSC segments
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    

    std::vector<CSCSegment> CSCSegmentVect = theCSCAnalyzer->FillCSCSegmentVector(iEvent);
    std::vector<GlobalPoint> CSCSegment_Global_points = theCSCAnalyzer->FillGlobalPointCSCSegmentVector(iEvent, iSetup,CSCSegmentVect);
    for(unsigned int i =0; i< CSCSegmentVect.size();i++) CSCSegments.push_back( CSCSegmentType() );
    nCSCSegments = CSCSegmentVect.size();

    // Match DT Segments to Gen b quarks

    // for gen matching, to be filled later
    std::vector<bool> CSCGenMatched;
    for(unsigned int i = 0; i < CSCSegmentVect.size(); i++) CSCGenMatched.push_back(false);//to be implemented later

    std::vector<CSCSegment> MatchedCSCSegmentVect;
    //Matching the b quarks to AK4 calo jets
    //Starting point: b-quark
    int matching_index_CSCSegment;//local variable
    float delta_R_CSCSegment;//local variable
    float current_delta_R_CSCSegment;//local variable
    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
        {
        delta_R_CSCSegment = 1000.;
        current_delta_R_CSCSegment = 1000.;
        matching_index_CSCSegment = -1;
        for(unsigned int a = 0; a<CSCSegmentVect.size(); a++)
            {
            current_delta_R_CSCSegment = fabs(reco::deltaR(CSCSegment_Global_points[a].eta(),CSCSegment_Global_points[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
            if(current_delta_R_CSCSegment<0.4 && current_delta_R_CSCSegment<delta_R_CSCSegment)
                //this implements all the reasonable possibilities!
                {
                delta_R_CSCSegment = min(delta_R_CSCSegment,current_delta_R_CSCSegment);
                matching_index_CSCSegment = a;
                CSCGenMatched[a] = true;
                //JetsVect[a].addUserInt("original_jet_index",a+1);
                MatchedCSCSegmentVect.push_back(CSCSegmentVect[a]);//avoid duplicates!
                }
            }
        if(matching_index_CSCSegment>=0){
            number_of_b_matched_to_CSCSegment++;
        }
        }
    //Remove duplicates from Matched Jets Vector
    for(unsigned int r = 0; r<MatchedCSCSegmentVect.size(); r++)
        {
        for(unsigned int s = 0; s<MatchedCSCSegmentVect.size(); s++)
            {
            if(r!=s && MatchedCSCSegmentVect[s].localPosition()==MatchedCSCSegmentVect[r].localPosition()) MatchedCSCSegmentVect.erase(MatchedCSCSegmentVect.begin()+s);
            }//duplicates removed
        }
    nMatchedCSCsegmentstob = MatchedCSCSegmentVect.size();
   
    
    // Match CSC Segments to VBF jets
    
    
    // for gen matching, to be filled later
    std::vector<bool> CSCVBFMatched;
    for(unsigned int i = 0; i < CSCSegmentVect.size(); i++) CSCVBFMatched.push_back(false);//to be implemented later

    std::vector<CSCSegment> MatchedCSCSegmenttoVBFVect;
    //Matching the b quarks to AK4 calo jets
    //Starting point: b-quark
    int matching_index_CSCSegment_VBF;//local variable
    float delta_R_CSCSegment_VBF;//local variable
    float current_delta_R_CSCSegment_VBF;//local variable
    for(unsigned int j = 0; j<VBFPairJetsVect.size(); j++)
        {
        delta_R_CSCSegment_VBF = 1000.;
        current_delta_R_CSCSegment_VBF = 1000.;
        matching_index_CSCSegment_VBF = -1;
        for(unsigned int a = 0; a<CSCSegmentVect.size(); a++)
            {
            current_delta_R_CSCSegment = fabs(reco::deltaR(CSCSegment_Global_points[a].eta(),CSCSegment_Global_points[a].phi(),VBFPairJetsVect[j].eta(),VBFPairJetsVect[j].phi()));
            if(current_delta_R_CSCSegment_VBF<0.4 && current_delta_R_CSCSegment_VBF<delta_R_CSCSegment_VBF)
                //this implements all the reasonable possibilities!
                {
                delta_R_CSCSegment_VBF = min(delta_R_CSCSegment_VBF,current_delta_R_CSCSegment_VBF);
                matching_index_CSCSegment_VBF = a;
                CSCVBFMatched[a] = true;
                //JetsVect[a].addUserInt("original_jet_index",a+1);
                MatchedCSCSegmenttoVBFVect.push_back(CSCSegmentVect[a]);//avoid duplicates!
                }
            }
        if(matching_index_CSCSegment_VBF>=0){
            number_of_VBF_matched_to_CSCSegment++;
        }
        }
    //Remove duplicates from Matched Jets Vector
    for(unsigned int r = 0; r<MatchedCSCSegmenttoVBFVect.size(); r++)
        {
        for(unsigned int s = 0; s<MatchedCSCSegmenttoVBFVect.size(); s++)
            {
            if(r!=s && MatchedCSCSegmenttoVBFVect[s].localPosition()==MatchedCSCSegmenttoVBFVect[r].localPosition()) MatchedCSCSegmenttoVBFVect.erase(MatchedCSCSegmenttoVBFVect.begin()+s);
            }//duplicates removed
        }
    nMatchedCSCsegmentstoVBF = MatchedCSCSegmenttoVBFVect.size();


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // StandAloneMuons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
   
    /*
    std::vector<reco::Track> StandAloneMuonsVect = theStandAloneMuonsAnalyzer->FillStandAloneMuonsVector(iEvent);
    for(unsigned int i =0; i< StandAloneMuonsVect.size();i++) StandAloneMuons.push_back( TrackType() );
    nStandAloneMuons = StandAloneMuonsVect.size();
    std::vector<bool> GenStandAloneMuonsFlag;
    for(unsigned int i =0; i< StandAloneMuonsVect.size();i++) GenStandAloneMuonsFlag.push_back(false);

    //One way to implement jet-gen b-quark matching is performed here
    std::vector<reco::Track> MatchedStandAloneMuonsVect;

    //Matching the b quarks to StandAloneMuons
    //Starting point: b-quark
    int matching_index_StandAloneMuons;//local variable
    float delta_R_StandAloneMuons;//local variable
    float current_delta_R_StandAloneMuons;//local variable
    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
      {
	delta_R_StandAloneMuons = 1000.;
	current_delta_R_StandAloneMuons = 1000.;
	matching_index_StandAloneMuons = -1;
	for(unsigned int a = 0; a<StandAloneMuonsVect.size(); a++)
	  {
	    current_delta_R_StandAloneMuons = fabs(reco::deltaR(StandAloneMuonsVect[a].eta(),StandAloneMuonsVect[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
	    //std::cout << "comparing gen b n. " << b << " and standalone muon n." << a << std::endl;
	    //std::cout << current_delta_R_StandAloneMuons << std::endl;
	    if(current_delta_R_StandAloneMuons<0.4 && current_delta_R_StandAloneMuons<delta_R_StandAloneMuons)
	      //this implements all the reasonable possibilities!
	      {
	      delta_R_StandAloneMuons = min(delta_R_StandAloneMuons,current_delta_R_StandAloneMuons);
	      matching_index_StandAloneMuons = a;
	      MatchedStandAloneMuonsVect.push_back(StandAloneMuonsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }
	if(matching_index_StandAloneMuons>=0){
	  //std::cout << "~~~~~~~~~~~~~~~~~~~~~~~~~" << std::endl;
	  //std::cout << "standalone muon matched: " << matching_index_StandAloneMuons  <<std::endl;
	  GenStandAloneMuonsFlag.at(matching_index_StandAloneMuons) = true;
	  //number_of_b_matched_to_CHSJets++;//wait
	}
      }


    //Remove duplicates from Matched CHSJets Vector
    for(unsigned int r = 0; r<MatchedStandAloneMuonsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedStandAloneMuonsVect.size(); s++)
	  {
	    if(r!=s && MatchedStandAloneMuonsVect[s].pt()==MatchedStandAloneMuonsVect[r].pt()) MatchedStandAloneMuonsVect.erase(MatchedStandAloneMuonsVect.begin()+s);
	  }//duplicates removed
      }
    nMatchedStandAloneMuons = MatchedStandAloneMuonsVect.size();//wait

    //int n_StandAloneMuons_in_CHSJets = 0;
    //for(unsigned int m = 0; m < StandAloneMuonsVect.size(); m++) {
    //for(unsigned int j = 0; j < CHSJetsVect.size(); ) {
    //	if(deltaR(CHSJetsVect.at(j), StandAloneMuonsVect.at(m)) < 0.4) n_StandAloneMuons_in_CHSJets++;
    //}
    //}
    //std::cout << "Standalone muons in jets: " << n_StandAloneMuons_in_CHSJets << std::endl;
    */

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // DisplacedStandAloneMuons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    /*
    std::vector<reco::Track> DisplacedStandAloneMuonsVect = theDisplacedStandAloneMuonsAnalyzer->FillStandAloneMuonsVector(iEvent);
    for(unsigned int i =0; i< DisplacedStandAloneMuonsVect.size();i++) DisplacedStandAloneMuons.push_back( TrackType() );
    nDisplacedStandAloneMuons = DisplacedStandAloneMuonsVect.size();
    std::vector<bool> GenDisplacedStandAloneMuonsFlag;
    for(unsigned int i =0; i< DisplacedStandAloneMuonsVect.size();i++) GenDisplacedStandAloneMuonsFlag.push_back(false);

    //One way to implement jet-gen b-quark matching is performed here
    std::vector<reco::Track> MatchedDisplacedStandAloneMuonsVect;

    //Matching the b quarks to DisplacedStandAloneMuons
    //Starting point: b-quark
    int matching_index_DisplacedStandAloneMuons;//local variable
    float delta_R_DisplacedStandAloneMuons;//local variable
    float current_delta_R_DisplacedStandAloneMuons;//local variable
    for(unsigned int b = 0; b<GenBquarksVect.size(); b++)
      {
	delta_R_DisplacedStandAloneMuons = 1000.;
	current_delta_R_DisplacedStandAloneMuons = 1000.;
	matching_index_DisplacedStandAloneMuons = -1;
	for(unsigned int a = 0; a<DisplacedStandAloneMuonsVect.size(); a++)
	  {
	    current_delta_R_DisplacedStandAloneMuons = fabs(reco::deltaR(DisplacedStandAloneMuonsVect[a].eta(),DisplacedStandAloneMuonsVect[a].phi(),GenBquarksVect[b].eta(),GenBquarksVect[b].phi()));
	    //std::cout << "comparing gen b n. " << b << " and displaced standalone muon n." << a << std::endl;
	    //std::cout << current_delta_R_DisplacedStandAloneMuons << std::endl;
	    if(current_delta_R_DisplacedStandAloneMuons<0.4 && current_delta_R_DisplacedStandAloneMuons<delta_R_DisplacedStandAloneMuons)
	      //this implements all the reasonable possibilities!
	      {
	      delta_R_DisplacedStandAloneMuons = min(delta_R_DisplacedStandAloneMuons,current_delta_R_DisplacedStandAloneMuons);
	      matching_index_DisplacedStandAloneMuons = a;
	      MatchedDisplacedStandAloneMuonsVect.push_back(DisplacedStandAloneMuonsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }
	if(matching_index_DisplacedStandAloneMuons>=0){
	  //std::cout << "++++++++++++++++++++++++++++++++++" << std::endl;
	  //std::cout << "displaced standalone muon matched: " << matching_index_DisplacedStandAloneMuons  <<std::endl;
	  GenDisplacedStandAloneMuonsFlag.at(matching_index_DisplacedStandAloneMuons) = true;
	  //number_of_b_matched_to_CHSJets++;//wait
	}
      }


    //Remove duplicates from Matched CHSJets Vector
    for(unsigned int r = 0; r<MatchedDisplacedStandAloneMuonsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedDisplacedStandAloneMuonsVect.size(); s++)
	  {
	    if(r!=s && MatchedDisplacedStandAloneMuonsVect[s].pt()==MatchedDisplacedStandAloneMuonsVect[r].pt()) MatchedDisplacedStandAloneMuonsVect.erase(MatchedDisplacedStandAloneMuonsVect.begin()+s);
	  }//duplicates removed
      }
    nMatchedDisplacedStandAloneMuons = MatchedDisplacedStandAloneMuonsVect.size();//wait
    */

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
    
    if (WriteGenVBFquarks) for(unsigned int i = 0; i < GenVBFVect.size(); i++) ObjectsFormat::FillGenPType(GenVBFquarks[i], &GenVBFVect[i]);
    if (WriteGenHiggs) for(unsigned int i = 0; i < GenHiggsVect.size(); i++) ObjectsFormat::FillGenPType(GenHiggs[i], &GenHiggsVect[i]);
    if (WriteGenLLPs) for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) ObjectsFormat::FillGenPType(GenLLPs[i], &GenLongLivedVect[i]);
    if (WriteGenBquarks) for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillGenPType(GenBquarks[i], &GenBquarksVect[i]);
    //RecoObjectsFormat::FillRecoMEtType(RecoMEt, &RecoMET, isMC);//wait, to be fixed
    ObjectsFormat::FillMEtType(MEt, &MET, isMC);//wait, to be fixed
    ObjectsFormat::FillCandidateType(VBF, &theVBF, isMC);//wait, to be fixed

    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) CHSJets.push_back( JetType() );
    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) ObjectsFormat::FillJetType(CHSJets[i], &CHSJetsVect[i], isMC);

    //for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) VBFPairJets.push_back( JetType() );//slim ntuple
    //for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) ObjectsFormat::FillJetType(VBFPairJets[i], &VBFPairJetsVect[i], isMC);//slim ntuple

    // for(unsigned int i = 0; i < ggHJetVect.size(); i++) ggHJet.push_back( JetType() );//slim ntuple
    //for(unsigned int i = 0; i < ggHJetVect.size(); i++) ObjectsFormat::FillJetType(ggHJet[i], &ggHJetVect[i], isMC);//slim ntuple

    //for(unsigned int i = 0; i < CaloJetsVect.size(); i++) CaloJets.push_back( CaloJetType() );//slim ntuple
    //for(unsigned int i = 0; i < CaloJetsVect.size(); i++) ObjectsFormat::FillCaloJetType(CaloJets[i], &CaloJetsVect[i], isMC, caloGenMatched[i], caloGenMatchedRadius2D[i], caloGenMatchedEta[i]);//slim ntuple
    //DTSegments
    //for(unsigned int i =0; i< DTSegmentVect.size();i++) ObjectsFormat::FillDT4DSegmentType(DTRecSegments4D[i], &DTSegmentVect[i],&DTSegment_Global_points[i]);//slim ntuple

    //CSCSegments
    //for(unsigned int i =0; i< CSCSegmentVect.size();i++) ObjectsFormat::FillCSCSegmentType(CSCSegments[i], &CSCSegmentVect[i],&CSCSegment_Global_points[i]);//slim ntuple

    //PFCandidates
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

    ////StandAloneMuons
    //for(unsigned int i =0; i< StandAloneMuonsVect.size();i++) ObjectsFormat::FillTrackType(StandAloneMuons[i], &StandAloneMuonsVect[i], GenStandAloneMuonsFlag[i]);
    ////DisplacedStandAloneMuons
    //for(unsigned int i =0; i< DisplacedStandAloneMuonsVect.size();i++) ObjectsFormat::FillTrackType(DisplacedStandAloneMuons[i], &DisplacedStandAloneMuonsVect[i],GenDisplacedStandAloneMuonsFlag[i]);
      


    if(isVerbose) {
      //Write a summary, in verbose mode
      std::cout << " --- Event n. " << iEvent.id().event() << ", lumi " << iEvent.luminosityBlock() << ", run " << iEvent.id().run() << std::endl;

      std::cout << "number of CHS AK4 jets:  " << CHSJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < CHSJetsVect.size(); i++) std::cout << "  CHS AK4 jet  [" << i << "]\tpt: " << CHSJetsVect[i].pt() << "\teta: " << CHSJetsVect[i].eta() << "\tphi: " << CHSJetsVect[i].phi() << "\tmass: " << CHSJetsVect[i].mass() << "\tnTrackConstituents: " << CHSJetsVect[i].chargedMultiplicity() << std::endl;

      //std::cout << "VBF jets pair:  " << VBFPairJetsVect.size() << std::endl;
      //if(isVBF) std::cout << "VBF conditions satisfied" << std::endl;
      //for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) std::cout << "  VBF jet  [" << i << "]\tpt: " << VBFPairJetsVect[i].pt() << "\teta: " << VBFPairJetsVect[i].eta() << "\tphi: " << VBFPairJetsVect[i].phi() << "\tmass: " << VBFPairJetsVect[i].mass() << std::endl;

      std::cout << "number of Gen B quarks:  " << GenBquarksVect.size() << std::endl;
      for(unsigned int i = 0; i < GenBquarksVect.size(); i++) {std::cout << "  Gen B quark  [" << i << "]\tpt: " << GenBquarksVect[i].pt() << "\teta: " << GenBquarksVect[i].eta() << "\tphi: " << GenBquarksVect[i].phi() << "\tradius (in cm): " << ( GenBquarksVect[i].mother() ? sqrt(pow(GenBquarksVect[i].vx() - GenBquarksVect[i].mother()->vx(),2) + pow(GenBquarksVect[i].vy() - GenBquarksVect[i].mother()->vy(),2) + pow(GenBquarksVect[i].vz() - GenBquarksVect[i].mother()->vz(),2)) : -1000. ) << "\tradius 2D (in cm): " << ( GenBquarksVect[i].mother() ? sqrt(pow(GenBquarksVect[i].vx() - GenBquarksVect[i].mother()->vx(),2) + pow(GenBquarksVect[i].vy() - GenBquarksVect[i].mother()->vy(),2)) : -1000. ) << std::endl;}

      std::cout << "Missing ET:  " << std::endl;
      std::cout << "  pt: " << MET.pt() << "\tphi: " << MET.phi() << std::endl;

      std::cout << "number of CHS AK4 jets matched to b quarks:  " << MatchedCHSJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < MatchedCHSJetsVect.size(); i++) std::cout << "  Matched CHS AK4 jet  [" << i << "]\tpt: " << MatchedCHSJetsVect[i].pt() << "\teta: " << MatchedCHSJetsVect[i].eta() << "\tphi: " << MatchedCHSJetsVect[i].phi() << "\tmass: " << MatchedCHSJetsVect[i].mass() << "\tnTrackConstituents: " << MatchedCHSJetsVect[i].chargedMultiplicity() << std::endl;

      std::cout << "number of Calo AK4 jets:  " << CaloJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < CaloJetsVect.size(); i++) std::cout << "  Calo AK4 jet  [" << i << "]\tpt: " << CaloJetsVect[i].pt() << "\teta: " << CaloJetsVect[i].eta() << "\tphi: " << CaloJetsVect[i].phi() << "\tmass: " << CaloJetsVect[i].mass() << "\temEnergyFraction " << CaloJetsVect[i].emEnergyFraction() << std::endl;

      std::cout << "number of Matched Calo AK4 jets:  " << MatchedCaloJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < MatchedCaloJetsVect.size(); i++) std::cout << "  Calo AK4 jet  [" << i << "]\tpt: " << MatchedCaloJetsVect[i].pt() << "\teta: " << MatchedCaloJetsVect[i].eta() << "\tphi: " << MatchedCaloJetsVect[i].phi() << "\tmass: " << MatchedCaloJetsVect[i].mass() << "\temEnergyFraction " << MatchedCaloJetsVect[i].emEnergyFraction() << std::endl;

      //std::cout << "number of StandAloneMuons: " << StandAloneMuonsVect.size() << std::endl;
      //for(unsigned int i = 0; i < StandAloneMuonsVect.size(); i++) std::cout << "  StandAloneMuons  [" << i << "]\tpt: " << StandAloneMuonsVect[i].pt() << "\teta: " << StandAloneMuonsVect[i].eta() << "\tphi: " << StandAloneMuonsVect[i].phi() << std::endl;

      //std::cout << "number of DisplacedStandAloneMuons: " << DisplacedStandAloneMuonsVect.size() << std::endl;
      //for(unsigned int i = 0; i < DisplacedStandAloneMuonsVect.size(); i++) std::cout << "  DisplacedStandAloneMuons  [" << i << "]\tpt: " << DisplacedStandAloneMuonsVect[i].pt() << "\teta: " << DisplacedStandAloneMuonsVect[i].eta() << "\tphi: " << DisplacedStandAloneMuonsVect[i].phi() << std::endl;

      std::cout << "number of DT segments:  " << DTSegmentVect.size() << std::endl;
      std::cout << "number of DT global position:  " << DTSegment_Global_points.size() << std::endl;
      for(unsigned int i = 0; i < DTSegment_Global_points.size(); i++) std::cout << "  Global position of DT segment [" << i << "]\teta: " << DTSegment_Global_points[i].eta() << "\tphi: " << DTSegment_Global_points[i].phi() << "\tsize of rech hits: "<< DTSegmentVect.at(i).recHits().size() << std::endl;


      //std::cout << "number of CSC segments:  " << CSCSegmentVect.size() << std::endl;
      //std::cout << "number of CSC global position:  " << CSCSegment_Global_points.size() << std::endl;
      //for(unsigned int i = 0; i < CSCSegment_Global_points.size(); i++) std::cout << "  Global position of CSC segment [" << i << "]\teta: " << CSCSegment_Global_points[i].eta() << "\tphi: " << CSCSegment_Global_points[i].phi() << std::endl;
      //std::cout << "number of CHS AK8 jets:  " << CHSFatJetsVect.size() << std::endl;
      //for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) std::cout << "  AK8 jet  [" << i << "]\tpt: " << CHSFatJetsVect[i].pt() << "\teta: " << CHSFatJetsVect[i].eta() << "\tphi: " << CHSFatJetsVect[i].phi() << "\tmass: " << CHSFatJetsVect[i].mass() << std::endl;
    }



    //Fill tree
    tree -> Fill();
    if(isVerbose) std::cout << "TREE FILLED!!!!!!!!!!!! Go to next event...--->" << std::endl;

    //ManualJets.clear();
    CHSJets.clear();
    CaloJets.clear();
    VBFPairJets.clear();
    ggHJet.clear();

    DTRecSegments4D.clear();
    CSCSegments.clear();

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
AODNtuplizer::beginJob()
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
   tree -> Branch("PUWeight", &PUWeight, "PUWeight/F");
   tree -> Branch("PUWeightUp", &PUWeightUp, "PUWeightUp/F");
   tree -> Branch("PUWeightDown", &PUWeightDown, "PUWeightDown/F");
   tree -> Branch("AtLeastOneTrigger" , &AtLeastOneTrigger , "AtLeastOneTrigger/O");
   tree -> Branch("AtLeastOneL1Filter" , &AtLeastOneL1Filter , "AtLeastOneL1Filter/O");
   tree -> Branch("Prefired" , &Prefired , "Prefired/O");
   tree -> Branch("nPV" , &nPV , "nPV/L");
   tree -> Branch("isVBF" , &isVBF, "isVBF/O");
   tree -> Branch("isggH" , &isggH, "isggH/O");
   tree -> Branch("HT" , &HT , "HT/F");
   tree -> Branch("MinJetMetDPhi", &MinJetMetDPhi, "MinJetMetDPhi/F");
   tree -> Branch("ggHJetMetDPhi", &ggHJetMetDPhi , "ggHJetMetDPhi/F");
   tree -> Branch("nGenBquarks" , &nGenBquarks , "nGenBquarks/L");
   tree -> Branch("nGenLL" , &nGenLL , "nGenLL/L");
   tree -> Branch("gen_b_radius" , &gen_b_radius , "gen_b_radius/F");
   tree -> Branch("gen_b_radius_2D" , &gen_b_radius_2D , "gen_b_radius_2D/F");
   tree -> Branch("m_pi" , &m_pi , "m_pi/F");
   tree -> Branch("nElectrons", &nElectrons, "nElectrons/I");
   tree -> Branch("nMuons", &nMuons, "nMuons/I");
   tree -> Branch("nTaus", &nTaus, "nTaus/I");
   tree -> Branch("nPhotons", &nPhotons, "nPhotons/I");
   tree -> Branch("nTightMuons", &nTightMuons, "nTightMuons/I");
   tree -> Branch("nTightElectrons", &nTightElectrons, "nTightElectrons/I");
    tree -> Branch("nPFCandidates" , &nPFCandidates, "nPFCandidates/I");
    tree -> Branch("nPFCandidatesTrack", &nPFCandidatesTrack, "nPFCandidatesTrack/I");
    tree -> Branch("nPFCandidatesHighPurityTrack", &nPFCandidatesHighPurityTrack, "nPFCandidatesHighPurityTrack/I");
    tree -> Branch("nPFCandidatesFullTrackInfo", &nPFCandidatesFullTrackInfo, "nPFCandidatesFullTrackInfo/I");
    tree -> Branch("nPFCandidatesFullTrackInfo_pt", &nPFCandidatesFullTrackInfo_pt, "nPFCandidatesFullTrackInfo_pt/I");
    tree -> Branch("nPFCandidatesFullTrackInfo_hasTrackDetails", &nPFCandidatesFullTrackInfo_hasTrackDetails, "nPFCandidatesFullTrackInfo_hasTrackDetails/I");
   tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
   tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
   tree -> Branch("nCHSJets" , &nCHSJets , "nCHSJets/L");
   tree -> Branch("nCaloJets" , &nCaloJets , "nCaloJets/L");
   tree -> Branch("nMatchedCHSJets" , &nMatchedCHSJets , "nMatchedCHSJets/L");
   tree -> Branch("nMatchedCaloJets" , &nMatchedCaloJets , "nMatchedCaloJets/L");
   tree -> Branch("nVBFGenMatchedCHSJets", & nVBFGenMatchedCHSJets, "nVBFGenMatchedCHSJets/L");
   tree -> Branch("nVBFGenMatchedVBFJets", & nVBFGenMatchedVBFJets, "nVBFGenMatchedVBFJets/L");
   tree -> Branch("nDTSegments", &nDTSegments, "nDTSegments/L");
   tree -> Branch("nDTSegmentsStation1", &nDTSegmentsStation1, "nDTSegmentsStation1/L");
   tree -> Branch("nDTSegmentsStation2", &nDTSegmentsStation2, "nDTSegmentsStation2/L");
   tree -> Branch("nDTSegmentsStation3", &nDTSegmentsStation3, "nDTSegmentsStation3/L");
   tree -> Branch("nDTSegmentsStation4", &nDTSegmentsStation4, "nDTSegmentsStation4/L");
   tree -> Branch("nCSCSegments", &nCSCSegments, "nCSCSegments/L");
   tree -> Branch("nMatchedDTsegmentstob", &nMatchedDTsegmentstob, "nMatchedDTsegmentstob/L");
   tree -> Branch("nMatchedCSCsegmentstob", &nMatchedCSCsegmentstob, "nMatchedCSCsegmentstob/L");
   tree -> Branch("nMatchedDTsegmentstoVBF", &nMatchedDTsegmentstoVBF, "nMatchedDTsegmentstoVBF/L");
   tree -> Branch("nMatchedCSCsegmentstoVBF", &nMatchedCSCsegmentstoVBF, "nMatchedCSCsegmentstoVBF/L");
   tree -> Branch("number_of_b_matched_to_CHSJets", &number_of_b_matched_to_CHSJets, "number_of_b_matched_to_CHSJets/L");
   tree -> Branch("number_of_b_matched_to_CaloJets", &number_of_b_matched_to_CaloJets, "number_of_b_matched_to_CaloJets/L");
   tree -> Branch("number_of_VBFGen_matched_to_CHSJets", &number_of_VBFGen_matched_to_CHSJets, "number_of_VBFGen_matched_to_CHSJets/L");
   tree -> Branch("number_of_VBFGen_matched_to_VBFJets", &number_of_VBFGen_matched_to_VBFJets, "number_of_VBFGen_matched_to_VBFJets/L");
   tree -> Branch("number_of_b_matched_to_DTSegment4D", &number_of_b_matched_to_DTSegment4D, "number_of_b_matched_to_DTSegment4D/L");
   tree -> Branch("number_of_b_matched_to_CSCSegment", &number_of_b_matched_to_CSCSegment, "number_of_b_matched_to_CSCSegment/L");
   tree -> Branch("number_of_VBF_matched_to_CSCSegment", &number_of_VBF_matched_to_CSCSegment, "number_of_VBF_matched_to_CSCSegment/L");
   tree -> Branch("number_of_VBF_matched_to_DTSegment4D", &number_of_VBF_matched_to_DTSegment4D, "number_of_VBF_matched_to_DTSegment4D/L");
   tree -> Branch("n_segments_around_b_quark_0",&n_segments_around_b_quark_0, "n_segments_around_b_quark_0/I");
   tree -> Branch("n_segments_around_b_quark_1",&n_segments_around_b_quark_1, "n_segments_around_b_quark_1/I");
   tree -> Branch("n_segments_around_b_quark_2",&n_segments_around_b_quark_2, "n_segments_around_b_quark_2/I");
   tree -> Branch("n_segments_around_b_quark_3",&n_segments_around_b_quark_3, "n_segments_around_b_quark_3/I");
   //tree -> Branch("nStandAloneMuons", &nStandAloneMuons, "nStandAloneMuons/L");
   //tree -> Branch("nDisplacedStandAloneMuons", &nDisplacedStandAloneMuons, "nDisplacedStandAloneMuons/L");
   //tree -> Branch("nMatchedStandAloneMuons", &nMatchedStandAloneMuons, "nMatchedStandAloneMuons/L");
   //tree -> Branch("nMatchedDisplacedStandAloneMuons", &nMatchedDisplacedStandAloneMuons, "nMatchedDisplacedStandAloneMuons/L");
   
   tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
   tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
   // Set trigger branches
   for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   for(auto it = MetFiltersMap.begin(); it != MetFiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   //for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());

   //tree -> Branch("ManualJets", &ManualJets);
   tree -> Branch("GenHiggs", &GenHiggs);
   tree -> Branch("GenLLPs", &GenLLPs);
   tree -> Branch("GenBquarks", &GenBquarks);
   //tree -> Branch("GenVBFquarks", &GenVBFquarks);//slim ntuples
   //tree -> Branch("DTSegments", &DTRecSegments4D);//slim ntuples
   //tree -> Branch("CSCSegments", &CSCSegments);//slim ntuples
   //tree -> Branch("StandAloneMuons", &StandAloneMuons);
   //tree -> Branch("DisplacedStandAloneMuons", &DisplacedStandAloneMuons);
   ////tree -> Branch("RecoMEt", &RecoMEt.pt, RecoObjectsFormat::ListRecoMEtType().c_str());

   //tree -> Branch("MEt", &MEt.pt, ObjectsFormat::ListMEtType().c_str());

   tree -> Branch("MEt", &MEt);
   tree -> Branch("Jets", &CHSJets);
   //tree -> Branch("VBFPairJets", &VBFPairJets);//slim ntuples
   //tree -> Branch("ggHJet", &ggHJet);//slim ntuples
   //tree -> Branch("CaloJets", &CaloJets);//slim ntuples
   //tree -> Branch("VBFPair", &VBF.pt, ObjectsFormat::ListCandidateType().c_str());//wai!//slim ntuples
   if (WriteAK4JetPFCandidates || WriteAK8JetPFCandidates || WriteAllJetPFCandidates || WriteAllPFCandidates) tree -> Branch("PFCandidates", &PFCandidates);


}

// ------------ method called once each job just after ending the event loop  ------------
void 
AODNtuplizer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
AODNtuplizer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(AODNtuplizer);
