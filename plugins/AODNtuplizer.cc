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
#include <numeric>
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
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

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
      static bool pt_sorter(const pat::PackedCandidate&, const pat::PackedCandidate&);

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
    edm::ParameterSet CHSFatJetPSet;
    edm::ParameterSet ElectronPSet;
    edm::ParameterSet MuonPSet;
    edm::ParameterSet TauPSet;
    edm::ParameterSet PhotonPSet;
    edm::ParameterSet VertexPSet;
    edm::ParameterSet PFCandidatePSet;
    //edm::ParameterSet DTPSet;
    //edm::ParameterSet CSCSet;
    //edm::ParameterSet StandAloneMuonsPSet;
    //edm::ParameterSet DisplacedStandAloneMuonsPSet;
    edm::EDGetTokenT<reco::PFJetCollection> jetToken;
    //edm::EDGetTokenT<std::vector<pat::MET> > metToken;
    
    edm::EDGetTokenT<vector<reco::Track> > generalTracksToken;
    edm::EDGetTokenT<edm::View<reco::Track> > generalTracksViewToken;


    JetAnalyzer* theCHSJetAnalyzer;
    CaloJetAnalyzer* theCaloJetAnalyzer;
    JetAnalyzer* theVBFJetAnalyzer;
    JetAnalyzer* theCHSFatJetAnalyzer;
    GenAnalyzer* theGenAnalyzer;
    PileupAnalyzer* thePileupAnalyzer;
    TriggerAnalyzer* theTriggerAnalyzer;
    ElectronAnalyzer* theElectronAnalyzer;
    MuonAnalyzer* theMuonAnalyzer;
    TauAnalyzer* theTauAnalyzer;
    PhotonAnalyzer* thePhotonAnalyzer;
    VertexAnalyzer* theVertexAnalyzer;
    PFCandidateAnalyzer* thePFCandidateAnalyzer;
    //DTAnalyzer* theDTAnalyzer;
    //CSCAnalyzer* theCSCAnalyzer;
    //StandAloneMuonsAnalyzer* theStandAloneMuonsAnalyzer;
    //StandAloneMuonsAnalyzer* theDisplacedStandAloneMuonsAnalyzer;

    //edm::EDGetTokenT<reco::JetTagCollection> JetTagWP0p01Token;
    //edm::EDGetTokenT<reco::JetTagCollection> JetTagWP0p1Token;
    //edm::EDGetTokenT<reco::JetTagCollection> JetTagWP1Token;
    //edm::EDGetTokenT<reco::JetTagCollection> JetTagWP10Token;
    //edm::EDGetTokenT<reco::JetTagCollection> JetTagWP100Token;
    //edm::EDGetTokenT<reco::JetTagCollection> JetTagWP1000Token;
    

    int idLLP1, idLLP2;
    int idHiggs, idMotherB, statusLLP, statusHiggs;
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
    std::vector<ecalRecHitType> EcalRecHitsAK4;
    std::vector<hcalRecHitType> HcalRecHitsAK4;
    std::vector<ecalRecHitType> EcalRecHitsAK8;
    std::vector<hcalRecHitType> HcalRecHitsAK8;
    std::vector<JetType> VBFPairJets;
    std::vector<FatJetType> CHSFatJets;
    std::vector<JetType> ggHJet;
    //std::vector<RecoJetType> ManualJets;
    std::vector<CaloJetType> CaloJets;
    std::vector<LeptonType> Muons;
    std::vector<LeptonType> Electrons;
    std::vector<PhotonType> Photons;
    std::vector<GenPType> GenVBFquarks;
    std::vector<GenPType> GenBquarks;
    std::vector<GenPType> GenLLPs;
    std::vector<GenPType> GenHiggs;
    //std::vector<DT4DSegmentType> DTRecSegments4D;    
    //std::vector<CSCSegmentType> CSCSegments;
    //std::vector<TrackType> StandAloneMuons;
    //std::vector<TrackType> DisplacedStandAloneMuons;

    std::vector<PFCandidateType> PFCandidates;//old, just for debugging
    std::vector<PFCandidateType> PFCandidatesAK4;
    std::vector<PFCandidateType> PFCandidatesAK8;

    MEtType MEt;
    //RecoMEtType RecoMEt;
    CandidateType VBF;//VBF tagging

    std::map<std::string, bool> TriggerMap;
    std::map<std::string, int> PrescalesTriggerMap;
    std::map<std::string, bool> MetFiltersMap;
    std::map<std::string, bool> L1FiltersMap;

    bool isVerbose, isVerboseTrigger, isSignal, isCalo;
    
    //pfCands
    //edm::EDGetTokenT<reco::PFCandidateCollection> PFCandsToken_;
    //new met filters, Matthew
    edm::EDGetTokenT<bool> globalSuperTightHalo2016FilterToken_;
    edm::EDGetTokenT<bool> globalTightHalo2016FilterToken_;
    edm::EDGetTokenT<bool> BadChargedCandidateFilterToken_;
    edm::EDGetTokenT<bool> BadPFMuonFilterToken_;
    edm::EDGetTokenT<bool> EcalDeadCellTriggerPrimitiveFilterToken_;
    edm::EDGetTokenT<bool> HBHENoiseFilterToken_;
    edm::EDGetTokenT<bool> HBHEIsoNoiseFilterToken_;
    edm::EDGetTokenT<bool> ecalBadCalibFilterToken_;
    edm::EDGetTokenT<bool> eeBadScFilterToken_;
    edm::EDGetTokenT<bool> primaryVertexFilterToken_;  
    
    bool isMC;
    bool isVBF;
    bool isggH;
    long int EventNumber, LumiNumber, RunNumber, nPV, nSV;
    bool AtLeastOneTrigger, AtLeastOneL1Filter;
    float EventWeight;
    float GenEventWeight;
    float PUWeight, PUWeightUp, PUWeightDown;
    long int nCHSJets;
    long int nCHSFatJets;
    long int nCaloJets;
    long int nElectrons, nMuons, nTaus, nPhotons;
    long int nTightMuons, nTightElectrons;
    long int nMatchedCHSJets;
    long int nMatchedCaloJets;
    long int nVBFGenMatchedCHSJets;
    long int nVBFGenMatchedVBFJets;
    long int number_of_b_matched_to_CHSJets;
    long int number_of_b_matched_to_CHSFatJets;
    long int number_of_b_matched_to_CaloJets;
    long int number_of_VBFGen_matched_to_CHSJets;
    long int number_of_VBFGen_matched_to_VBFJets;
    //long int number_of_b_matched_to_DTSegment4D;
    //long int number_of_b_matched_to_CSCSegment;
    //long int number_of_VBF_matched_to_DTSegment4D;
    //long int number_of_VBF_matched_to_CSCSegment;
    //int n_segments_around_b_quark_0;
    //int n_segments_around_b_quark_1;
    //int n_segments_around_b_quark_2;
    //int n_segments_around_b_quark_3;
    //long int nDTSegments, nDTSegmentsStation1, nDTSegmentsStation2, nDTSegmentsStation3, nDTSegmentsStation4;
    //long int nCSCSegments;
    //long int nMatchedDTsegmentstob;
    //long int nMatchedCSCsegmentstob;
    //long int nMatchedDTsegmentstoVBF;
    //long int nMatchedCSCsegmentstoVBF;
    //long int nStandAloneMuons, nMatchedStandAloneMuons;
    //long int nDisplacedStandAloneMuons, nMatchedDisplacedStandAloneMuons;
    
    AddFourMomenta addP4;
    float HT;
    float HTNoSmear;
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
    int nLLPInCalo;
    
    
    //Geometry and propagator
    const MagneticField* MagneticFieldTag;
    edm::ESHandle<Propagator> PropagatorHandle;
    edm::ESHandle<TransientTrackBuilder> BuilderHandle;
    
    //new met filters, matthew
    bool Flag2_globalSuperTightHalo2016Filter;
    bool Flag2_globalTightHalo2016Filter;
    bool Flag2_goodVertices;
    bool Flag2_BadChargedCandidateFilter;
    bool Flag2_BadPFMuonFilter;
    bool Flag2_EcalDeadCellTriggerPrimitiveFilter;
    bool Flag2_HBHENoiseFilter;
    bool Flag2_HBHEIsoNoiseFilter;
    bool Flag2_ecalBadCalibFilter;
    bool Flag2_eeBadScFilter;
    
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
    CHSFatJetPSet(iConfig.getParameter<edm::ParameterSet>("chsFatJetSet")),
    ElectronPSet(iConfig.getParameter<edm::ParameterSet>("electronSet")),
    MuonPSet(iConfig.getParameter<edm::ParameterSet>("muonSet")),
    TauPSet(iConfig.getParameter<edm::ParameterSet>("tauSet")),
    PhotonPSet(iConfig.getParameter<edm::ParameterSet>("photonSet")),
    VertexPSet(iConfig.getParameter<edm::ParameterSet>("vertexSet")),
    PFCandidatePSet(iConfig.getParameter<edm::ParameterSet>("pfCandidateSet")),
    //DTPSet(iConfig.getParameter<edm::ParameterSet>("dtSet")),
    //CSCSet(iConfig.getParameter<edm::ParameterSet>("cscSet")),
    //StandAloneMuonsPSet(iConfig.getParameter<edm::ParameterSet>("standaloneMuonsSet")),
    //DisplacedStandAloneMuonsPSet(iConfig.getParameter<edm::ParameterSet>("displacedStandaloneMuonsSet")),
    idLLP1(iConfig.getParameter<int>("idLLP1")),
    idLLP2(iConfig.getParameter<int>("idLLP2")),
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
    isCalo(iConfig.getParameter<bool> ("iscalo")),
    //PFCandsToken_(consumes<reco::PFCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfCands"))),
    globalSuperTightHalo2016FilterToken_(consumes<bool>(edm::InputTag("globalSuperTightHalo2016Filter"))),
    globalTightHalo2016FilterToken_(consumes<bool>(edm::InputTag("globalTightHalo2016Filter"))),
    BadChargedCandidateFilterToken_(consumes<bool>(edm::InputTag("BadChargedCandidateFilter"))),
    BadPFMuonFilterToken_(consumes<bool>(edm::InputTag("BadPFMuonFilter"))),
    EcalDeadCellTriggerPrimitiveFilterToken_(consumes<bool>(edm::InputTag("EcalDeadCellTriggerPrimitiveFilter"))),
    HBHENoiseFilterToken_(consumes<bool>(edm::InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"))),
    HBHEIsoNoiseFilterToken_(consumes<bool>(edm::InputTag("HBHENoiseFilterResultProducer","HBHEIsoNoiseFilterResult"))),
    ecalBadCalibFilterToken_(consumes<bool>(edm::InputTag("ecalBadCalibReducedMINIAODFilter"))),
    eeBadScFilterToken_(consumes<bool>(edm::InputTag("eeBadScFilter"))),
    primaryVertexFilterToken_(consumes<bool>(edm::InputTag("primaryVertexFilter")))

{

    // Check writePFCandidate flags
    // No more needed. Want to save both AK4 and AK8 PF candidates
    //int PFCandidateFlags = 0;
    //if (WriteAK4JetPFCandidates) PFCandidateFlags++;
    //if (WriteAK8JetPFCandidates) PFCandidateFlags++;
    //if (WriteAllJetPFCandidates) PFCandidateFlags++;
    //if (WriteAllPFCandidates)    PFCandidateFlags++;
    //if (PFCandidateFlags > 1)   throw cms::Exception("Configuration") << "More than one writePFCandidates flag selected. Please choose one option only!";


    theCHSJetAnalyzer       = new JetAnalyzer(CHSJetPSet, consumesCollector());
    theCaloJetAnalyzer      = new CaloJetAnalyzer(CaloJetPSet, consumesCollector());
    theVBFJetAnalyzer       = new JetAnalyzer(VBFJetPSet, consumesCollector());
    theCHSFatJetAnalyzer   = new JetAnalyzer(CHSFatJetPSet, consumesCollector());
    theGenAnalyzer          = new GenAnalyzer(GenPSet, consumesCollector());
    thePileupAnalyzer       = new PileupAnalyzer(PileupPSet, consumesCollector());
    theTriggerAnalyzer      = new TriggerAnalyzer(TriggerPSet, consumesCollector());
    theElectronAnalyzer     = new ElectronAnalyzer(ElectronPSet, consumesCollector());
    theMuonAnalyzer         = new MuonAnalyzer(MuonPSet, consumesCollector());
    theTauAnalyzer          = new TauAnalyzer(TauPSet, consumesCollector());
    thePhotonAnalyzer       = new PhotonAnalyzer(PhotonPSet, consumesCollector());
    theVertexAnalyzer       = new VertexAnalyzer(VertexPSet, consumesCollector());
    thePFCandidateAnalyzer  = new PFCandidateAnalyzer(PFCandidatePSet, consumesCollector());
    //theDTAnalyzer           = new DTAnalyzer(DTPSet, consumesCollector());
    //theCSCAnalyzer          = new CSCAnalyzer(CSCSet, consumesCollector());
    //theStandAloneMuonsAnalyzer          = new StandAloneMuonsAnalyzer(StandAloneMuonsPSet,  consumesCollector());
    //theDisplacedStandAloneMuonsAnalyzer = new StandAloneMuonsAnalyzer(DisplacedStandAloneMuonsPSet,  consumesCollector());

    std::vector<std::string> TriggerList(TriggerPSet.getParameter<std::vector<std::string> >("paths"));
    for(unsigned int i = 0; i < TriggerList.size(); i++) TriggerMap[ TriggerList[i] ] = false;
    for(unsigned int i = 0; i < TriggerList.size(); i++) PrescalesTriggerMap[ TriggerList[i] ] = -1;
    std::vector<std::string> MetFiltersList(TriggerPSet.getParameter<std::vector<std::string> >("metpaths"));
    for(unsigned int i = 0; i < MetFiltersList.size(); i++) MetFiltersMap[ MetFiltersList[i] ] = false;

    //Imperial College Tagger
    //edm::InputTag JetTagWP0p01 = edm::InputTag("pfXTags:0p01:ntuple");
    //JetTagWP0p01Token= consumes<reco::JetTagCollection>(JetTagWP0p01);

    //edm::InputTag JetTagWP0p1 = edm::InputTag("pfXTags:0p1:ntuple");
    //JetTagWP0p1Token= consumes<reco::JetTagCollection>(JetTagWP0p1);

    //edm::InputTag JetTagWP1 = edm::InputTag("pfXTags:1:ntuple");
    //JetTagWP1Token= consumes<reco::JetTagCollection>(JetTagWP1);

    //edm::InputTag JetTagWP10 = edm::InputTag("pfXTags:10:ntuple");
    //JetTagWP10Token= consumes<reco::JetTagCollection>(JetTagWP10);

    //edm::InputTag JetTagWP100 = edm::InputTag("pfXTags:100:ntuple");
    //JetTagWP100Token= consumes<reco::JetTagCollection>(JetTagWP100);

    //edm::InputTag JetTagWP1000 = edm::InputTag("pfXTags:1000:ntuple");
    //JetTagWP1000Token= consumes<reco::JetTagCollection>(JetTagWP1000);

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
    delete theCHSFatJetAnalyzer;
    delete theGenAnalyzer;
    delete thePileupAnalyzer;
    delete theTriggerAnalyzer;
    delete theElectronAnalyzer;
    delete theMuonAnalyzer;
    delete theTauAnalyzer;
    delete thePhotonAnalyzer;
    delete theVertexAnalyzer;
    delete thePFCandidateAnalyzer;
    //delete theDTAnalyzer;
    //delete theCSCAnalyzer;
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

  //if(isVerbose) std::cout << " Starting analyze..... " << std::endl;
    auto start = std::chrono::system_clock::now();//time!
    using namespace edm;
    using namespace reco;
    using namespace std;

    // Initialize types
    //ObjectsFormat::ResetGenPType(GenHiggs);
    ObjectsFormat::ResetCandidateType(VBF);


    nCHSJets = nCaloJets = nCHSFatJets = 0;
    nElectrons = nMuons = nTaus = nPhotons = 0;
    nTightMuons = nTightElectrons = 0;
    //nStandAloneMuons = nDisplacedStandAloneMuons =0;
    //nDTSegments = nDTSegmentsStation1 = nDTSegmentsStation2 = nDTSegmentsStation3 = nDTSegmentsStation4 = nCSCSegments = 0;
    //nMatchedStandAloneMuons = nMatchedDisplacedStandAloneMuons =0;
    isMC = false;
    isVBF = false;
    isggH = false;
    EventNumber = LumiNumber = RunNumber = nPV = 0;
    GenEventWeight = EventWeight = PUWeight = PUWeightDown = PUWeightUp = 1.;
    HT = 0.;
    HTNoSmear = 0.;
    nMatchedCHSJets = 0;
    nMatchedCaloJets = 0;
    nVBFGenMatchedCHSJets = 0;
    nVBFGenMatchedVBFJets = 0;
    number_of_b_matched_to_CHSJets = 0;
    number_of_b_matched_to_CaloJets = 0;
    number_of_b_matched_to_CHSFatJets = 0;
    number_of_VBFGen_matched_to_CHSJets = 0;
    number_of_VBFGen_matched_to_VBFJets = 0;
    //number_of_b_matched_to_DTSegment4D=0;
    //number_of_b_matched_to_CSCSegment=0;
    //number_of_VBF_matched_to_DTSegment4D=0;
    //number_of_VBF_matched_to_CSCSegment=0;
    //n_segments_around_b_quark_0 = 0;
    //n_segments_around_b_quark_1 = 0;
    //n_segments_around_b_quark_2 = 0;
    //n_segments_around_b_quark_3 = 0;
    MinJetMetDPhi = MinJetMetDPhiAllJets = ggHJetMetDPhi = 10.;
    nGenBquarks = nGenLL = 0;
    nLLPInCalo = 0;
    m_pi = 0.;
    gen_b_radius = -1.;
    gen_b_radius_2D = -1.;
    Prefired = false;
    AtLeastOneTrigger = AtLeastOneL1Filter = false;
    nPFCandidates = nPFCandidatesTrack = nPFCandidatesHighPurityTrack = nPFCandidatesFullTrackInfo = nPFCandidatesFullTrackInfo_pt = nPFCandidatesFullTrackInfo_hasTrackDetails = 0;
    number_of_PV = number_of_SV = 0;
    
    Flag2_globalSuperTightHalo2016Filter = false;
    Flag2_globalTightHalo2016Filter = false;
    Flag2_goodVertices = false;
    Flag2_BadChargedCandidateFilter = false;
    Flag2_BadPFMuonFilter = false;
    Flag2_EcalDeadCellTriggerPrimitiveFilter = false;
    Flag2_HBHENoiseFilter = false;
    Flag2_HBHEIsoNoiseFilter = false;
    Flag2_ecalBadCalibFilter = false;
    Flag2_eeBadScFilter = false;

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
    //if(isVerbose) std::cout << "Trigger and met filters" << std::endl;
    //debug!
    theTriggerAnalyzer->FillTriggerMap(iEvent, TriggerMap, PrescalesTriggerMap, isVerboseTrigger);
    theTriggerAnalyzer->FillMetFiltersMap(iEvent, MetFiltersMap);
    BadPFMuonFlag = theTriggerAnalyzer->GetBadPFMuonFlag(iEvent);
    BadChCandFlag = theTriggerAnalyzer->GetBadChCandFlag(iEvent);

    //pfCands
    //edm::Handle<reco::PFCandidateCollection> pfCands;
    //iEvent.getByToken(PFCandsToken_, pfCands);

    //new met filters, matthew
    //new handle here
    edm::Handle<bool> globalSuperTightHalo2016Filter;
    edm::Handle<bool> globalTightHalo2016Filter;
    edm::Handle<bool> BadChargedCandidateFilter;
    edm::Handle<bool> BadPFMuonFilter;
    edm::Handle<bool> EcalDeadCellTriggerPrimitiveFilter;
    edm::Handle<bool> ecalBadCalibReducedMINIAODFilter;
    edm::Handle<bool> eeBadScFilter;
    edm::Handle<bool> HBHENoiseFilter;
    edm::Handle<bool> HBHEIsoNoiseFilter;
    edm::Handle<bool> primaryVertexFilter;
    
    iEvent.getByToken(globalSuperTightHalo2016FilterToken_, globalSuperTightHalo2016Filter);
    iEvent.getByToken(globalTightHalo2016FilterToken_, globalTightHalo2016Filter);
    iEvent.getByToken(BadChargedCandidateFilterToken_, BadChargedCandidateFilter);
    iEvent.getByToken(BadPFMuonFilterToken_, BadPFMuonFilter);
    iEvent.getByToken(EcalDeadCellTriggerPrimitiveFilterToken_, EcalDeadCellTriggerPrimitiveFilter);
    iEvent.getByToken(HBHENoiseFilterToken_, HBHENoiseFilter);
    iEvent.getByToken(HBHEIsoNoiseFilterToken_, HBHEIsoNoiseFilter);
    iEvent.getByToken(ecalBadCalibFilterToken_, ecalBadCalibReducedMINIAODFilter);
    iEvent.getByToken(eeBadScFilterToken_, eeBadScFilter);
    //iEvent.getByToken(primaryVertexFilterToken_, primaryVertexFilter);
    
    Flag2_globalSuperTightHalo2016Filter = *globalSuperTightHalo2016Filter;
    Flag2_globalTightHalo2016Filter = *globalTightHalo2016Filter;
    Flag2_BadChargedCandidateFilter = *BadChargedCandidateFilter;
    Flag2_BadPFMuonFilter = *BadPFMuonFilter;
    Flag2_EcalDeadCellTriggerPrimitiveFilter = *EcalDeadCellTriggerPrimitiveFilter;
    Flag2_HBHENoiseFilter = *HBHENoiseFilter;
    Flag2_HBHEIsoNoiseFilter = *HBHEIsoNoiseFilter;
    Flag2_ecalBadCalibFilter = *ecalBadCalibReducedMINIAODFilter;
    Flag2_eeBadScFilter = *eeBadScFilter;
    //Flag2_goodVertices = *primaryVertexFilter;



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
    
    HT = theCHSJetAnalyzer->CalculateHT(iEvent,iSetup,3,15,3.,true);
    HTNoSmear = theCHSJetAnalyzer->CalculateHT(iEvent,iSetup,3,15,3.,false);

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Electrons
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Electrons
    //if(isVerbose) std::cout << "Electrons" << std::endl;
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
    //if(isVerbose) std::cout << "Photons" << std::endl;
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
    //if(HT<100) return;//Avoid events with low HT//WAIT!!
    //17.12.2020 : remove MET cut
    //if(isCalo && MET.pt()<120) return;//Avoid events with very low MET for calo analysis
    //17.12.2020 : remove lepton veto
    //if(isCalo && nMuons>0) return;//Veto leptons and photons!
    //if(isCalo && nTaus>0) return;//Veto leptons and photons!
    //if(isCalo && nElectrons>0) return;//Veto leptons and photons!
    //if(isCalo && nPhotons>0) return;//Veto leptons and photons!


    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // Gen particles
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------


    //if(isVerbose) std::cout << "Gen Particles" << std::endl;

    GenVBFquarks.clear();
    GenHiggs.clear();
    GenLLPs.clear();
    GenBquarks.clear();

    std::vector<reco::GenParticle> GenVBFVect = theGenAnalyzer->FillVBFGenVector(iEvent);
    std::vector<reco::GenParticle> GenHiggsVect = theGenAnalyzer->FillGenVectorByIdAndStatus(iEvent,idHiggs,statusHiggs);
    std::vector<reco::GenParticle> GenLongLivedVect = theGenAnalyzer->FillGenVectorByTwoIdsAndStatus(iEvent,idLLP1,idLLP2,statusLLP);
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
    
    float ecal_radius = 129.0;
    float max_calo_radius = 184.;
    float max_calo_z = 376.;
    float min_displacement_radius = 30;
    
    //Calculate calo corrections
    std::vector<float> corrEtaDaughterLLP;
    std::vector<float> corrPhiDaughterLLP;
    std::vector<float> corrEtaGrandDaughterLLP;
    std::vector<float> corrPhiGrandDaughterLLP;
    std::vector<float> LLPRadius_Dau;
    std::vector<float> LLPX_Dau;
    std::vector<float> LLPY_Dau;
    std::vector<float> LLPZ_Dau;
    std::vector<float> LLPRadius_GrandDau;
    std::vector<float> LLPX_GrandDau;
    std::vector<float> LLPY_GrandDau;
    std::vector<float> LLPZ_GrandDau;

    std::vector<bool>  LLPInCalo;
    std::vector<bool>  DaughterOfLLPInCalo;
    std::vector<bool>  GrandDaughterOfLLPInCalo;
    
    std::vector<float> checkPtDaughterLLP;
    std::vector<float> checkPtGrandDaughterLLP;
    std::vector<float> checkEtaDaughterLLP;
    std::vector<float> checkEtaGrandDaughterLLP;
    std::vector<float> checkPhiDaughterLLP;
    std::vector<float> checkPhiGrandDaughterLLP;

    
    //use idmotherb to determine wether one needs dau or grand dau corrections (heavy higgs: dau; susy: grand dau)
    //std::vector<const reco::Candidate*> LLPs;
  
    
    for(unsigned int l=0; l<GenLongLivedVect.size(); l++)
    {
         if(GenLongLivedVect.size()>1 && GenLongLivedVect.at(l).numberOfDaughters()>1)
         {
         //must conver reco::GenParticles into const reco::Candidate*, otherwise daughter method does not work
         const reco::Candidate *candLLP = &(GenLongLivedVect)[l];

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
             if(abs(candLLP->daughter(i)->pdgId())==idHiggs || abs(candLLP->daughter(i)->pdgId())==5)//consider only higgs and b quarks
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
                            
               
               const reco::Candidate *tmpDauParticle = candLLP->daughter(i);
               for (unsigned int g = 0; g < tmpDauParticle->numberOfDaughters(); g++ )
               {
               
                  if(abs(candLLP->daughter(i)->daughter(g)->pdgId())==5 && idMotherB==25)
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
    
    //std::cout << "check pt higgs: " << std::endl;
    //for(unsigned int a=0;a<GenHiggsVect.size();a++) std::cout << GenHiggsVect.at(a).pt() << std::endl;
    //std::cout << "check pt bquarks: " << std::endl;
    //for(unsigned int a=0;a<GenBquarksVect.size();a++) std::cout << GenBquarksVect.at(a).pt() << std::endl;
    //std::cout << "checkPtDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<checkPtDaughterLLP.size();a++) std::cout << checkPtDaughterLLP.at(a) << std::endl;
    //std::cout << "checkPtGrandDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<checkPtGrandDaughterLLP.size();a++) std::cout << checkPtGrandDaughterLLP.at(a) << std::endl;
    //std::cout << "check eta higgs: " << std::endl;
    //for(unsigned int a=0;a<GenHiggsVect.size();a++) std::cout << GenHiggsVect.at(a).eta() << std::endl;
    //std::cout << "check eta bquarks: " << std::endl;
    //for(unsigned int a=0;a<GenBquarksVect.size();a++) std::cout << GenBquarksVect.at(a).eta() << std::endl;
    //std::cout << "checkEtaDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<checkEtaDaughterLLP.size();a++) std::cout << checkEtaDaughterLLP.at(a) << std::endl;
    //std::cout << "corrEtaDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<corrEtaDaughterLLP.size();a++) std::cout << corrEtaDaughterLLP.at(a) << std::endl;
    //std::cout << "checkEtaGrandDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<checkEtaGrandDaughterLLP.size();a++) std::cout << checkEtaGrandDaughterLLP.at(a) << std::endl; 
    //std::cout << "corrEtaGrandDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<corrEtaGrandDaughterLLP.size();a++) std::cout << corrEtaGrandDaughterLLP.at(a) << std::endl;   
    //std::cout << "check phi higgs: " << std::endl;
    //for(unsigned int a=0;a<GenHiggsVect.size();a++) std::cout << GenHiggsVect.at(a).phi() << std::endl;
    //std::cout << "check phi bquarks: " << std::endl;
    //for(unsigned int a=0;a<GenBquarksVect.size();a++) std::cout << GenBquarksVect.at(a).phi() << std::endl;
    //std::cout << "checkPhiDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<checkPhiDaughterLLP.size();a++) std::cout << checkPhiDaughterLLP.at(a) << std::endl;
    //std::cout << "corrPhiDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<corrPhiDaughterLLP.size();a++) std::cout << corrPhiDaughterLLP.at(a) << std::endl;
    //std::cout << "checkPhiGrandDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<checkPhiGrandDaughterLLP.size();a++) std::cout << checkPhiGrandDaughterLLP.at(a) << std::endl; 
    //std::cout << "corrPhiGrandDaughterLLP: " << std::endl;
    //for(unsigned int a=0;a<corrPhiGrandDaughterLLP.size();a++) std::cout << corrPhiGrandDaughterLLP.at(a) << std::endl;
    

    for(unsigned int i = 0; i < GenVBFVect.size(); i++) GenVBFquarks.push_back( GenPType() );
    for(unsigned int i = 0; i < GenHiggsVect.size(); i++) GenHiggs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) GenLLPs.push_back( GenPType() );
    for(unsigned int i = 0; i < GenBquarksVect.size(); i++) GenBquarks.push_back( GenPType() );

    if(nGenBquarks>0) gen_b_radius = GenBquarksVect.at(0).mother()? sqrt(pow(GenBquarksVect.at(0).vx() - GenBquarksVect.at(0).mother()->vx(),2) + pow(GenBquarksVect.at(0).vy() - GenBquarksVect.at(0).mother()->vy(),2) + pow(GenBquarksVect.at(0).vz() - GenBquarksVect.at(0).mother()->vz(),2)) : -1.;
    if(nGenLL>0) m_pi = GenLongLivedVect.at(0).mass();

    //Fill gen objects here; needed later for jet matching
    //std::cout<< " Seg violation alert!!!" << std::endl;
    if (WriteGenVBFquarks) for(unsigned int i = 0; i < GenVBFVect.size(); i++) ObjectsFormat::FillGenPType(GenVBFquarks[i], &GenVBFVect[i]);
    if (WriteGenLLPs)  for(unsigned int i = 0; i < GenLongLivedVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenLLPs[i], &GenLongLivedVect[i], LLPInCalo[i], -9., -9., -1000.,-10000.,-10000.,-10000.);
    if (WriteGenHiggs) for(unsigned int i = 0; i < GenHiggsVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenHiggs[i], &GenHiggsVect[i], idMotherB==25 ? DaughterOfLLPInCalo[i] : false, idMotherB==25 ? corrEtaDaughterLLP[i] : -9., idMotherB==25 ? corrPhiDaughterLLP[i] : -9., idMotherB==25 ? LLPRadius_Dau[i] : -1000., idMotherB==25 ? LLPX_Dau[i] : -10000., idMotherB==25 ? LLPY_Dau[i] : -10000., idMotherB==25 ? LLPZ_Dau[i] : -10000.);

    //std::cout << GenBquarksVect.size() << std::endl;
    //std::cout << LLPRadius_Dau.size() << std::endl;
    //std::cout << LLPRadius_GrandDau.size() << std::endl;
    if(WriteGenBquarks && (LLPZ_GrandDau.size()==GenBquarksVect.size() || LLPZ_Dau.size()==GenBquarksVect.size()) ) for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenBquarks[i], &GenBquarksVect[i],
    idMotherB==25 && GrandDaughterOfLLPInCalo.size()==GenBquarksVect.size() ? GrandDaughterOfLLPInCalo[i] : DaughterOfLLPInCalo[i],
    idMotherB==25 && corrEtaGrandDaughterLLP.size()==GenBquarksVect.size() ? corrEtaGrandDaughterLLP[i] : corrEtaDaughterLLP[i],
    idMotherB==25 && corrPhiGrandDaughterLLP.size()==GenBquarksVect.size()? corrPhiGrandDaughterLLP[i] : corrPhiDaughterLLP[i],
    idMotherB==25 && LLPRadius_GrandDau.size()==GenBquarksVect.size() ? LLPRadius_GrandDau[i] : LLPRadius_Dau[i],
    idMotherB==25 && LLPX_GrandDau.size()==GenBquarksVect.size() ? LLPX_GrandDau[i] : LLPX_Dau[i],
    idMotherB==25 && LLPY_GrandDau.size()==GenBquarksVect.size() ? LLPY_GrandDau[i] : LLPY_Dau[i],
    idMotherB==25 && LLPZ_GrandDau.size()==GenBquarksVect.size() ? LLPZ_GrandDau[i] : LLPZ_Dau[i]);
    //some non empty gen b quarks
    //for(unsigned int i = 0; i < GenBquarksVect.size(); i++) ObjectsFormat::FillCaloGenPType(GenBquarks[i], &GenBquarksVect[i], false, -1., -1., -1., -1.);
    //std::cout<< " Not diedddd!!!" << std::endl;

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
    //if(isVerbose) std::cout << "VBF jets" << std::endl;

    

    std::vector<pat::Jet> VBFJetsVect = theVBFJetAnalyzer->FillJetVector(iEvent,iSetup);
    //if(isVerbose) std::cout << "VBF jets vect left empty on purpose" << std::endl;
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
    //if(isVerbose) std::cout << "VBF jet gen matching" << std::endl;
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
    //if(isVerbose) std::cout << "AK4 CHS jets" << std::endl;
    std::vector<pat::Jet> CHSJetsVect = theCHSJetAnalyzer->FillJetVector(iEvent,iSetup);

    //Ecal and Hcal rec hits
    EcalRecHitsAK4 = theCHSJetAnalyzer->FillEcalRecHitVector(iEvent,iSetup,CHSJetsVect);
    HcalRecHitsAK4 = theCHSJetAnalyzer->FillHcalRecHitVector(iEvent,iSetup,CHSJetsVect);

    for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
      {
	CHSJetsVect.at(a).addUserFloat( "dPhi_met",reco::deltaPhi(CHSJetsVect.at(a).phi(),MET.phi()) );
      }

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


    // Gen-matching: old approach
    std::vector<pat::Jet> MatchedCHSJetsVect;
    int matching_index_CHSJets;//local variable
    float delta_R_CHSJets;//local variable
    float current_delta_R_CHSJets;//local variable
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R_CHSJets = 1000.;
	current_delta_R_CHSJets = 1000.;
	matching_index_CHSJets = -1;
	for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
	  {
	    current_delta_R_CHSJets = fabs(reco::deltaR(CHSJetsVect[a].eta(),CHSJetsVect[a].phi(),GenBquarks[b].eta,GenBquarks[b].phi));
	    if(current_delta_R_CHSJets<0.4 && current_delta_R_CHSJets<delta_R_CHSJets && CHSJetsVect[a].genParton() && (fabs(CHSJetsVect[a].hadronFlavour())==5 || fabs(CHSJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[a].genParton()) )==idMotherB)
	      //this implements all the reasonable possibilities!
	      {
		delta_R_CHSJets = min(delta_R_CHSJets,current_delta_R_CHSJets);
		matching_index_CHSJets = a;
		CHSJetsVect[a].addUserInt("original_jet_index",a+1);
		CHSJetsVect[a].addUserFloat("radiusLLP",GenBquarks[b].travelRadiusLLP);
		CHSJetsVect[a].addUserFloat("xLLP",GenBquarks[b].travelXLLP);
		CHSJetsVect[a].addUserFloat("yLLP",GenBquarks[b].travelYLLP);
		CHSJetsVect[a].addUserFloat("zLLP",GenBquarks[b].travelZLLP);
		CHSJetsVect[a].addUserFloat("xGenb",GenBquarks[b].vx);
		CHSJetsVect[a].addUserFloat("yGenb",GenBquarks[b].vy);
		CHSJetsVect[a].addUserFloat("zGenb",GenBquarks[b].vz);
		//CHSJetsVect[a].addUserFloat("genbRadius2D", GenBquarksVect[b].mother()? sqrt(pow(GenBquarksVect[b].vx() - GenBquarksVect[b].mother()->vx(),2) + pow(GenBquarksVect[b].vy() - GenBquarksVect[b].mother()->vy(),2)) : -1000.);
		//CHSJetsVect[a].addUserFloat("genbEta",GenBquarksVect[b].eta());
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
	      }

	  }
	//add number of b's matched to jet
	current_delta_R_CHSJets = 1000.;
	int number_bs_matched_to_CHSJet = 0;
	for (unsigned int b = 0; b<GenBquarks.size(); b++){
	  current_delta_R_CHSJets = fabs(reco::deltaR(CHSJetsVect[r].eta(),CHSJetsVect[r].phi(),GenBquarks[b].eta,GenBquarks[b].phi));
	  if(current_delta_R_CHSJets<0.4 && CHSJetsVect[r].genParton() && (fabs(CHSJetsVect[r].hadronFlavour())==5 || fabs(CHSJetsVect[r].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[r].genParton()) )==idMotherB)
	    //this implements all the reasonable possibilities!
	    {
	      number_bs_matched_to_CHSJet += 1;
	    }
	}
	CHSJetsVect[r].addUserInt("nMatchedGenBquarks",number_bs_matched_to_CHSJet);
      }

    // Gen-matching: LLP in calo acceptance
    std::vector<pat::Jet> TempMatchedCHSJetsVect;
    float delta_R;//local variable
    float current_delta_R;//local variable
    //Loop over GenBquarks structure, we need corrections and gen info
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R = 1000.;
	current_delta_R = 1000.;
	for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
	  {
	    current_delta_R = fabs(reco::deltaR(CHSJetsVect[a].eta(),CHSJetsVect[a].phi(),GenBquarks[b].eta,GenBquarks[b].phi));
	    if(current_delta_R<0.4 && current_delta_R<delta_R && CHSJetsVect[a].genParton() && (fabs(CHSJetsVect[a].hadronFlavour())==5 || fabs(CHSJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[a].genParton()) )==idMotherB && GenBquarks[b].isLLPInCaloAcceptance)

	      {
		delta_R = min(delta_R,current_delta_R);
		TempMatchedCHSJetsVect.push_back(CHSJetsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }

      }

    //Remove duplicates from Temp Matched CHSJets Vector
    auto comp_tmp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    auto last_tmp = std::unique(TempMatchedCHSJetsVect.begin(), TempMatchedCHSJetsVect.end(),comp_tmp);
    TempMatchedCHSJetsVect.erase(last_tmp, TempMatchedCHSJetsVect.end());


    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<TempMatchedCHSJetsVect.size(); s++)
	  {

	    if(TempMatchedCHSJetsVect[s].pt()==CHSJetsVect[r].pt()) CHSJetsVect[r].addUserInt("isGenMatchedLLPAccept",1);

	  }

      }
      
    TempMatchedCHSJetsVect.clear();

    // Gen-matching: calo corrections
    //Loop over GenBquarks structure, we need corrections and gen info
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R = 1000.;
	current_delta_R = 1000.;
	for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
	  {
	    current_delta_R = fabs(reco::deltaR(CHSJetsVect[a].eta(),CHSJetsVect[a].phi(),GenBquarks[b].corrCaloEta,GenBquarks[b].corrCaloPhi));
	    if(current_delta_R<0.4 && current_delta_R<delta_R && CHSJetsVect[a].genParton() && (fabs(CHSJetsVect[a].hadronFlavour())==5 || fabs(CHSJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[a].genParton()) )==idMotherB)

	      {
		delta_R = min(delta_R,current_delta_R);
		TempMatchedCHSJetsVect.push_back(CHSJetsVect[a]);//duplicates possible, must be removed afterwards!
		CHSJetsVect[a].addUserFloat("radiusLLPCaloCorr",GenBquarks[b].travelRadiusLLP);
		CHSJetsVect[a].addUserFloat("xLLPCaloCorr",GenBquarks[b].travelXLLP);
		CHSJetsVect[a].addUserFloat("yLLPCaloCorr",GenBquarks[b].travelYLLP);
		CHSJetsVect[a].addUserFloat("zLLPCaloCorr",GenBquarks[b].travelZLLP);
		CHSJetsVect[a].addUserFloat("xGenbCaloCorr",GenBquarks[b].vx);
		CHSJetsVect[a].addUserFloat("yGenbCaloCorr",GenBquarks[b].vy);
		CHSJetsVect[a].addUserFloat("zGenbCaloCorr",GenBquarks[b].vz);
	      }
	  }

      }

    //Remove duplicates from Temp Matched CHSJets Vector
    //auto comp_tmp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    last_tmp = std::unique(TempMatchedCHSJetsVect.begin(), TempMatchedCHSJetsVect.end(),comp_tmp);
    TempMatchedCHSJetsVect.erase(last_tmp, TempMatchedCHSJetsVect.end());


    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<TempMatchedCHSJetsVect.size(); s++)
	  {

	    if(TempMatchedCHSJetsVect[s].pt()==CHSJetsVect[r].pt()) CHSJetsVect[r].addUserInt("isGenMatchedCaloCorr",1);

	  }
	  
	  
	  
	//add number of b's matched to jet
	current_delta_R = 1000.;
	int number_bs_matched_to_CHSJet_CaloCorr = 0;
	for (unsigned int b = 0; b<GenBquarks.size(); b++){
	  current_delta_R = fabs(reco::deltaR(CHSJetsVect[r].eta(),CHSJetsVect[r].phi(),GenBquarks[b].corrCaloEta,GenBquarks[b].corrCaloPhi));
	  if(current_delta_R<0.4 && CHSJetsVect[r].genParton() && (fabs(CHSJetsVect[r].hadronFlavour())==5 || fabs(CHSJetsVect[r].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[r].genParton()) )==idMotherB)
	    //this implements all the reasonable possibilities!
	    {
	      number_bs_matched_to_CHSJet_CaloCorr += 1;
	    }
	}
	CHSJetsVect[r].addUserInt("nMatchedGenBquarksCaloCorr",number_bs_matched_to_CHSJet_CaloCorr);

      }
      
    TempMatchedCHSJetsVect.clear();
      
      
    // Gen-matching: calo corrections and LLP in acceptance 
    //Loop over GenBquarks structure, we need corrections and gen info
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R = 1000.;
	current_delta_R = 1000.;
	for(unsigned int a = 0; a<CHSJetsVect.size(); a++)
	  {
	    current_delta_R = fabs(reco::deltaR(CHSJetsVect[a].eta(),CHSJetsVect[a].phi(),GenBquarks[b].corrCaloEta,GenBquarks[b].corrCaloPhi));
	    if(current_delta_R<0.4 && current_delta_R<delta_R && CHSJetsVect[a].genParton() && (fabs(CHSJetsVect[a].hadronFlavour())==5 || fabs(CHSJetsVect[a].partonFlavour())==5) && abs( Utilities::FindMotherId(CHSJetsVect[a].genParton()) )==idMotherB && GenBquarks[b].isLLPInCaloAcceptance)

	      {
		delta_R = min(delta_R,current_delta_R);
		TempMatchedCHSJetsVect.push_back(CHSJetsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }

      }

    //Remove duplicates from Temp Matched CHSJets Vector
    //auto comp_tmp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    last_tmp = std::unique(TempMatchedCHSJetsVect.begin(), TempMatchedCHSJetsVect.end(),comp_tmp);
    TempMatchedCHSJetsVect.erase(last_tmp, TempMatchedCHSJetsVect.end());


    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<TempMatchedCHSJetsVect.size(); s++)
	  {

	    if(TempMatchedCHSJetsVect[s].pt()==CHSJetsVect[r].pt()) CHSJetsVect[r].addUserInt("isGenMatchedCaloCorrLLPAccept",1);

	  }

      }
      
    TempMatchedCHSJetsVect.clear();      
      
      
      




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
 
 
    //Number of track constituents    
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

      //Cross-check with PFCandidates
      //This gives exceptions:  "PFJet constituent is not of PFCandidate type"
      //std::cout<< "AK4 jet n. " << j << " has these const: " <<  CHSJetsVect.at(j).getPFConstituents().size() << std::endl;
      //for (uint l=0; l < CHSJetsVect.at(j).getPFConstituents().size(); l++)
      //{
      //  std::cout<< "const. n. " << l << " pt: " << CHSJetsVect.at(j).getPFConstituents()[l]->pt() << std::endl; 
      //}

    }




    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // AK4 CHS Jets: Imperial College Tagger
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------

    //First attempt to read Imperial Tagger
    //edm::Handle<reco::JetTagCollection> pfXTagWP0p01Handle;
    //iEvent.getByToken(JetTagWP0p01Token, pfXTagWP0p01Handle);
    //const reco::JetTagCollection & pfXWP0p01Tags = *(pfXTagWP0p01Handle.product());

    //edm::Handle<reco::JetTagCollection> pfXTagWP0p1Handle;
    //iEvent.getByToken(JetTagWP0p1Token, pfXTagWP0p1Handle);
    //const reco::JetTagCollection & pfXWP0p1Tags = *(pfXTagWP0p1Handle.product());

    //edm::Handle<reco::JetTagCollection> pfXTagWP1Handle;
    //iEvent.getByToken(JetTagWP1Token, pfXTagWP1Handle);
    //const reco::JetTagCollection & pfXWP1Tags = *(pfXTagWP1Handle.product());

    //edm::Handle<reco::JetTagCollection> pfXTagWP10Handle;
    //iEvent.getByToken(JetTagWP10Token, pfXTagWP10Handle);
    //const reco::JetTagCollection & pfXWP10Tags = *(pfXTagWP10Handle.product());

    //edm::Handle<reco::JetTagCollection> pfXTagWP100Handle;
    //iEvent.getByToken(JetTagWP100Token, pfXTagWP100Handle);
    //const reco::JetTagCollection & pfXWP100Tags = *(pfXTagWP100Handle.product());

    //edm::Handle<reco::JetTagCollection> pfXTagWP1000Handle;
    //iEvent.getByToken(JetTagWP1000Token, pfXTagWP1000Handle);
    //const reco::JetTagCollection & pfXWP1000Tags = *(pfXTagWP1000Handle.product());

    ////Addd per-jet user float including Imperial Tagger
    //for(unsigned int r = 0; r<CHSJetsVect.size(); r++)
    //  {
    //	for(unsigned int s = 0; s<pfXWP0p01Tags.size(); s++)
    //	  {
    //	    //if(pfXWP0p01Tags[s].first->eta()==CHSJetsVect[r].eta())
    //        if( reco::deltaR(pfXWP0p01Tags[s].first->eta(),pfXWP0p01Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
    //	      {
    //            //std::cout << "CHS Jets n. " << r << " and pfXWP0p01 n. " << s << "are matching!" << std::endl;
    //		CHSJetsVect[r].addUserFloat("pfXWP0p01",pfXWP0p01Tags[s].second);
    //	      }
    //	  }

    //	for(unsigned int s = 0; s<pfXWP0p1Tags.size(); s++)
    //      {
    //        //if(pfXWP0p1Tags[s].first->eta()==CHSJetsVect[r].eta())
    //        if( reco::deltaR(pfXWP0p1Tags[s].first->eta(),pfXWP0p1Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
    //          {
    //            //std::cout << "CHS Jets n. " << r << " and pfXWP0p1 n. " << s << "are matching!" << std::endl;
    //            CHSJetsVect[r].addUserFloat("pfXWP0p1",pfXWP0p1Tags[s].second);
    //          }
    //      }

    //	for(unsigned int s = 0; s<pfXWP1Tags.size(); s++)
    //	  {
    //	    //if(pfXWP1Tags[s].first->eta()==CHSJetsVect[r].eta())
    //       if( reco::deltaR(pfXWP1Tags[s].first->eta(),pfXWP1Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
    //	      {
    //            //std::cout << "CHS Jets n. " << r << " and pfXWP1 n. " << s << "are matching!" << std::endl;
    //		CHSJetsVect[r].addUserFloat("pfXWP1",pfXWP1Tags[s].second);
    //	      }
    //	  }


    //	for(unsigned int s = 0; s<pfXWP10Tags.size(); s++)
    //	  {
    //        if( reco::deltaR(pfXWP10Tags[s].first->eta(),pfXWP10Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
    //	      {
    //		CHSJetsVect[r].addUserFloat("pfXWP10",pfXWP10Tags[s].second);
    //	      }
    //	  }

    //	for(unsigned int s = 0; s<pfXWP100Tags.size(); s++)
    //	  {
    //            if( reco::deltaR(pfXWP100Tags[s].first->eta(),pfXWP100Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
    //	      {
    //		CHSJetsVect[r].addUserFloat("pfXWP100",pfXWP100Tags[s].second);
    //	      }
    //	  }



    //	for(unsigned int s = 0; s<pfXWP1000Tags.size(); s++)
    //	  {
    //	    //if(pfXWP1000Tags[s].first->eta()==CHSJetsVect[r].eta())
    //            if( reco::deltaR(pfXWP1000Tags[s].first->eta(),pfXWP1000Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) < 0.01 )
    //	      {
    //                if(isVerbose) std::cout << "CHS Jets n. " << r << " and pfXWP1000 n. " << s << " are matching; dR: " << reco::deltaR(pfXWP1000Tags[s].first->eta(),pfXWP1000Tags[s].first->phi(),CHSJetsVect[r].eta(),CHSJetsVect[r].phi()) << std::endl;
    //		CHSJetsVect[r].addUserFloat("pfXWP1000",pfXWP1000Tags[s].second);
    //	      }
    //	  }
    //      }


    //# Loop over jets and study b tag info.

    //    if(isVerbose) {
    //      for (unsigned int i = 0; i != pfXWP1000Tags.size(); ++i) {
    //          if(pfXWP1000Tags[i].first->pt()>1 && abs(pfXWP1000Tags[i].first->eta())<2.4) std::cout << "  pfX WP1000 tag jet  [" << i << "]\tpt: " << pfXWP1000Tags[i].first->pt() << "\teta: " << pfXWP1000Tags[i].first->eta() << "\tphi: " << pfXWP1000Tags[i].first->phi() << "\tpfXTags: " << pfXWP1000Tags[i].second << std::endl;
    //      }
    //    }

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
    // AK8 CHS jets
    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    //if(isVerbose) std::cout << "AK8 CHS jets" << std::endl;
    std::string SoftdropPuppiMassString(CHSFatJetPSet.getParameter<std::string>("softdropPuppiMassString"));
    //std::cout << "Here filling AK8, calling FillJetVector method " << std::endl;
    //std::cout << "softdrop mass string: " << SoftdropPuppiMassString << std::endl;
    std::vector<pat::Jet> CHSFatJetsVect = theCHSFatJetAnalyzer->FillJetVector(iEvent,iSetup);

    EcalRecHitsAK8 = theCHSFatJetAnalyzer->FillEcalRecHitVector(iEvent,iSetup,CHSFatJetsVect);
    HcalRecHitsAK8 = theCHSFatJetAnalyzer->FillHcalRecHitVector(iEvent,iSetup,CHSFatJetsVect);


    for(unsigned int a = 0; a<CHSFatJetsVect.size(); a++)
      {
	//std::cout << "Check tag info of fat jet n. " << a << std::endl;
	//std::cout << "R param: " << CHSFatJetsVect.at(a).userFloat("Rparameter") << std::endl;
	//if(CHSFatJetsVect.at(a).tagInfoLabels().size() > 0 and CHSFatJetsVect.at(a).hasTagInfo("pfSecondaryVertex")) std::cout << " nselected tracks " << CHSFatJetsVect.at(a).tagInfoCandSecondaryVertex("pfSecondaryVertex")->nSelectedTracks() << std::endl;
	CHSFatJetsVect.at(a).addUserFloat( "dPhi_met",reco::deltaPhi(CHSFatJetsVect.at(a).phi(),MET.phi()) );
      }

    //number of constituents
    for(unsigned int j = 0; j < CHSFatJetsVect.size(); j++){
      //std::cout << "AK8 Jet n. " << j <<std::endl;//debug
      int nTrackConstituentsAK8 = 0;
      //per jet tag: number of jet constituents and number of tracks
      std::vector<edm::Ptr<reco::PFCandidate>> JetConstituentAK8Vect = CHSFatJetsVect[j].getPFConstituents();
      //std::vector<edm::Ptr<reco::Candidate>> JetConstituentAK8Vect = CHSFatJetsVect[j].getJetConstituents();
      CHSFatJetsVect.at(j).addUserInt("nConstituents",JetConstituentAK8Vect.size());

      std::vector<double> PF_eta_AK8;
      std::vector<double> PF_pt_AK8;
      std::vector<double> PF_pt_squared_AK8;
      std::vector<double> PF_phi_AK8;
      std::pair< std::pair<float,float> ,float> sigPF_AK8;

      for(unsigned int k = 0; k < JetConstituentAK8Vect.size(); k++){
	//std::cout << "const [" << k << "] pt: " << JetConstituentAK8Vect[k]->pt() << " , eta: " << JetConstituentAK8Vect[k]->eta()  << " , phi: " << JetConstituentAK8Vect[k]->phi() <<std::endl;//debug


        if(JetConstituentAK8Vect[k]->charge()!=0){
          nTrackConstituentsAK8++;
        }

	if(JetConstituentAK8Vect[k]->pt()>1)
	  {
	    //std::cout << " cand " << k << std::endl;
	    //std::cout << "charge " << JetConstituentAK8Vect[k]->charge() << std::endl;
	    //std::cout << "vx pf cand " << JetConstituentAK8Vect[k]->vx() << std::endl;
	    //if(JetConstituentAK8Vect[k]->charge()) std::cout << "vx track " << JetConstituentAK8Vect[k]->trackRef()->vx() << std::endl;
	    ////std::cout << "dxy pf cand " << JetConstituentAK8Vect[k]->dxy()  << std::endl;
	    //if(JetConstituentAK8Vect[k]->charge())std::cout << "dxy track "  << JetConstituentAK8Vect[k]->trackRef()->dxy()  << std::endl;
	    //std::cout << "dxy error pf cand " << JetConstituentAK8Vect[k]->dxyError()  << std::endl;
	    //if(JetConstituentAK8Vect[k]->charge())std::cout << "dxy error track "  << JetConstituentAK8Vect[k]->trackRef()->dxyError()  << std::endl;
	    
	    PFCandidateType CandStruct;
	    CandStruct.pt              = JetConstituentAK8Vect[k]->pt();
	    CandStruct.eta             = JetConstituentAK8Vect[k]->eta();
	    CandStruct.phi             = JetConstituentAK8Vect[k]->phi();
	    CandStruct.energy          = JetConstituentAK8Vect[k]->energy();
	    CandStruct.mass            = JetConstituentAK8Vect[k]->mass();
	    CandStruct.isTrack         = JetConstituentAK8Vect[k]->charge() ? true : false;
	    //nope//CandStruct.jetIndex        = -1;
	    CandStruct.fatJetIndex     = j;
	    //nope//CandStruct.pvIndex         = vtxIdx;
	    //nope//CandStruct.hasTrackDetails = JetConstituentAK8Vect[k]->hasTrackDetails();
	    CandStruct.trackHighPurity = JetConstituentAK8Vect[k]->trackRef().isNonnull() && JetConstituentAK8Vect[k]->trackRef()->highPurity==2 ? true : false;
	    CandStruct.px              = JetConstituentAK8Vect[k]->px();
	    CandStruct.py              = JetConstituentAK8Vect[k]->py();
	    CandStruct.pz              = JetConstituentAK8Vect[k]->pz();
	    CandStruct.dxy             = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->dxy() : -9999.;//making it consistent with method for AK4
	    CandStruct.dxyError        = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->dxyError() : -99.;
	    CandStruct.dz             = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->dz() : -9999.;//making it consistent with method for AK4
	    CandStruct.dzError        = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->dzError() : -99.;
	    CandStruct.nHits           = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->hitPattern().numberOfValidTrackerHits() : -1;
	    CandStruct.nPixelHits      = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->hitPattern().numberOfValidPixelHits() : -1;
	    CandStruct.lostInnerHits   = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->numberOfLostHits() : -1;
	    CandStruct.charge          = JetConstituentAK8Vect[k]->charge();
	    CandStruct.POCA_x          = JetConstituentAK8Vect[k]->vx();
	    CandStruct.POCA_y          = JetConstituentAK8Vect[k]->vy();
	    CandStruct.POCA_z          = JetConstituentAK8Vect[k]->vz();
	    //CandStruct.POCA_phi        = JetConstituentAK8Vect[k]->phiAtVtx();
	    CandStruct.pdgId           = JetConstituentAK8Vect[k]->pdgId();
	    CandStruct.ptError         = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->ptError() : -1.;
	    CandStruct.etaError        = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->etaError() : -1.;
	    CandStruct.phiError        = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->phiError() : -1.;
	    CandStruct.theta           = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->theta() : -9.;
	    CandStruct.thetaError      = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->thetaError() : -1.;
	    CandStruct.chi2            = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->chi2() : -1.;
	    CandStruct.ndof            = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->ndof() : -1;
	    CandStruct.normalizedChi2  = JetConstituentAK8Vect[k]->trackRef().isNonnull() ? JetConstituentAK8Vect[k]->trackRef()->normalizedChi2() : -1.;
	    CandStruct.time = JetConstituentAK8Vect[k]->time();
	    CandStruct.timeError = JetConstituentAK8Vect[k]->timeError();
	    CandStruct.isTimeValid = JetConstituentAK8Vect[k]->isTimeValid();
	    CandStruct.ecalEnergy = JetConstituentAK8Vect[k]->ecalEnergy();
	    CandStruct.hcalEnergy = JetConstituentAK8Vect[k]->hcalEnergy();
	    CandStruct.hcalDepth1EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(1);
	    CandStruct.hcalDepth2EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(2);
	    CandStruct.hcalDepth3EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(3);
	    CandStruct.hcalDepth4EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(4);
	    CandStruct.hcalDepth5EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(5);
	    CandStruct.hcalDepth6EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(6);
	    CandStruct.hcalDepth7EnergyFraction = JetConstituentAK8Vect[k]->hcalDepthEnergyFraction(7);
	    CandStruct.rawEcalEnergy = JetConstituentAK8Vect[k]->rawEcalEnergy();
	    CandStruct.rawHcalEnergy = JetConstituentAK8Vect[k]->rawHcalEnergy();
	    CandStruct.vertexChi2 = JetConstituentAK8Vect[k]->vertexChi2();
	    CandStruct.vertexNdof = JetConstituentAK8Vect[k]->vertexNdof();
	    CandStruct.vertexNormalizedChi2 = JetConstituentAK8Vect[k]->vertexNormalizedChi2();


	    PFCandidatesAK8.push_back(CandStruct);
	    PF_eta_AK8.push_back(JetConstituentAK8Vect[k]->eta());
	    PF_phi_AK8.push_back(JetConstituentAK8Vect[k]->phi());
	    PF_pt_AK8.push_back(JetConstituentAK8Vect[k]->pt());
	    PF_pt_squared_AK8.push_back(pow(JetConstituentAK8Vect[k]->pt(),2));
	  }

      }//loop on AK8 constituents
      CHSFatJetsVect.at(j).addUserInt("nTrackConstituents",nTrackConstituentsAK8);

      //jet shape
      sigPF_AK8 = theCHSFatJetAnalyzer->JetSecondMoments(PF_pt_AK8, PF_eta_AK8, PF_phi_AK8);
      //std::cout << "check ak8 sig pf " << sigPF_AK8.first.first << sigPF_AK8.first.second << sigPF_AK8.second << std::endl;
      //std::cout << "size of PF_pt_squared_AK8 " << PF_pt_squared_AK8.size() << std::endl;
      //std::cout << "size of PF_eta_AK8 " << PF_eta_AK8.size() << std::endl;
      //std::cout << "size of PF_phi_AK8 " << PF_phi_AK8.size() << std::endl;
      //std::cout << "Fat Jet n. " << j << " constituents saved: "  << std::endl;//debug
      //for(unsigned int a=0; a<PF_pt_AK8.size(); a++) 
      //{
      //std::cout << "[" << a << "] pt: " << PF_pt_AK8.at(a) << " , eta: " << PF_eta_AK8.at(a) << " , phi: " << PF_phi_AK8.at(a) << std::endl;
      //}

      CHSFatJetsVect[j].addUserFloat("sig1PF", sigPF_AK8.first.first>0 ? sigPF_AK8.first.first : -1.);
      CHSFatJetsVect[j].addUserFloat("sig2PF", sigPF_AK8.first.second>0 ? sigPF_AK8.first.second : -1.);
      CHSFatJetsVect[j].addUserFloat("sigAvPF", (sigPF_AK8.first.first>0 and sigPF_AK8.first.second>0) ? sqrt( pow(sigPF_AK8.first.first,2) + pow(sigPF_AK8.first.second,2) )  : -1.);
      CHSFatJetsVect[j].addUserFloat("tan2thetaPF", sigPF_AK8.second);
      CHSFatJetsVect[j].addUserFloat("ptDPF", accumulate(PF_pt_AK8.begin(),PF_pt_AK8.end(),0) > 0 ? sqrt(accumulate(PF_pt_squared_AK8.begin(),PF_pt_squared_AK8.end(),0)) / accumulate(PF_pt_AK8.begin(),PF_pt_AK8.end(),0) : -1.);


      /* To be added: jet shapes!
      //Loop over PFCandidates for AK8 jet shape
      
      for (unsigned int i = 0; i < PFCandidateVectAK8.size(); i++){
	int jj = j;
	if (jj == PFAK8JetIndex[i])
	  {
	  //jet shapes variables
	  }
      }



      */





      //Si's way
      //Loop on reco::particleFlow to check matching
      /*
      for (uint q=0; q< pfCands->size(); q++) 
	{
	  //const reco::PFCandidate *p = &(*pfCands)[q];
	  reco::PFCandidatePtr p_ptr(pfCands,q);

	  for (uint l=0; l < CHSFatJetsVect.at(j).getPFConstituents().size(); l++)
	    {
	      //std::cout << "True getPFConstituents pt:  " << CHSFatJetsVect.at(j).getPFConstituents()[l]->pt() << std::endl;
	      //if (p_ptr == CHSFatJetsVect.at(j).getPFConstituents()[l])
		//{
		  //std::cout << "Matched pfCand: " << CHSFatJetsVect.at(j).getPFConstituents()[l]->pt() << std::endl;
		//}
	      if (CHSFatJetsVect.at(j).getPFConstituents()[l]->pt()==p_ptr->pt())
		{

		  std::cout << "same pt: " << p_ptr->pt() << std::endl; 
		  std::cout<< CHSFatJetsVect.at(j).getPFConstituents()[l]->trackRef()->pt() << std::endl;
		  std::cout<< CHSFatJetsVect.at(j).getPFConstituents()[l]->trackRef()->hitPattern().numberOfValidTrackerHits() << std::endl;
		}
	    }

	}//loop on pfCands
      */
    }
    
    //Debug ak8 features
    //for(unsigned int i = 0; i<CHSFatJetsVect.size(); i++)
    //{
        //std::cout << "Fat jet n. " << i << std::endl;
        //std::cout << CHSFatJetsVect.at(i).pt() << std::endl;
        
        //if reclustered 
        
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMassReclustered") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("NjettinessAK8Reclustered:tau1") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("NjettinessAK8Reclustered:tau2") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("NjettinessAK8Reclustered:tau3") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsCHSPrunedMassReclustered") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsCHSSoftDropMassReclustered") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau1Reclustered") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau2Reclustered") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsPuppiValueMap:ak8PFJetsPuppiPrunedMassReclustered") << std::endl;
        
        //if not reclustered

        //std::cout << "softdrop puppi" << CHSFatJetsVect.at(i).userFloat("ak8PFJetsPuppiSoftDropMass") << std::endl;
        //std::cout << "pruned chs" << CHSFatJetsVect.at(i).userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass") << std::endl;
        //std::cout << "softdrop chs" << CHSFatJetsVect.at(i).userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("NjettinessAK8Puppi:tau1") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsCHSValueMap:NjettinessAK8CHSTau1") << std::endl;
        //std::cout << CHSFatJetsVect.at(i).userFloat("ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2") << std::endl;
    //}


    
    // Gen-matching: old approach
    std::vector<pat::Jet> MatchedFatJetsVect;
    int matching_index_FatJets;//local variable
    float delta_R_FatJets;//local variable
    float current_delta_R_FatJets;//local variable
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R_FatJets = 1000.;
	current_delta_R_FatJets = 1000.;
	matching_index_FatJets = -1;
	for(unsigned int a = 0; a<CHSFatJetsVect.size(); a++)
	  {
	    current_delta_R_FatJets = fabs(reco::deltaR(CHSFatJetsVect[a].eta(),CHSFatJetsVect[a].phi(),GenBquarks[b].eta,GenBquarks[b].phi));
	    if(current_delta_R_FatJets<0.8 && current_delta_R_FatJets<delta_R_FatJets)
	      //this implements all the reasonable possibilities!
	      {
		delta_R_FatJets = min(delta_R_FatJets,current_delta_R_FatJets);
		matching_index_FatJets = a;
		CHSFatJetsVect[a].addUserFloat("radiusLLP",GenBquarks[b].travelRadiusLLP);
		CHSFatJetsVect[a].addUserFloat("xLLP",GenBquarks[b].travelXLLP);
		CHSFatJetsVect[a].addUserFloat("yLLP",GenBquarks[b].travelYLLP);
		CHSFatJetsVect[a].addUserFloat("zLLP",GenBquarks[b].travelZLLP);
		CHSFatJetsVect[a].addUserFloat("xGenb",GenBquarks[b].vx);
		CHSFatJetsVect[a].addUserFloat("yGenb",GenBquarks[b].vy);
		CHSFatJetsVect[a].addUserFloat("zGenb",GenBquarks[b].vz);
		MatchedFatJetsVect.push_back(CHSFatJetsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }
	if(matching_index_FatJets>=0){
	  number_of_b_matched_to_CHSFatJets++;
	}
      }


    //Remove duplicates from Matched CHSJets Vector
    for(unsigned int r = 0; r<MatchedFatJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedFatJetsVect.size(); s++)
	  {
	    if(r!=s && MatchedFatJetsVect[s].pt()==MatchedFatJetsVect[r].pt()) MatchedFatJetsVect.erase(MatchedFatJetsVect.begin()+s);
	  }//duplicates removed
      }

    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSFatJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<MatchedFatJetsVect.size(); s++)
	  {

	    if(MatchedFatJetsVect[s].pt()==CHSFatJetsVect[r].pt())
	      {
		//let's add flags helping to find matched jets corresponding to original Jets vector
		CHSFatJetsVect[r].addUserInt("isGenMatched",1);
	      }

	  }
	//add number of b's matched to jet
	current_delta_R_FatJets = 1000.;
	int number_bs_matched_to_FatJet = 0;
	for (unsigned int b = 0; b<GenBquarks.size(); b++){
	  current_delta_R_FatJets = fabs(reco::deltaR(CHSFatJetsVect[r].eta(),CHSFatJetsVect[r].phi(),GenBquarks[b].eta,GenBquarks[b].phi));
	  if(current_delta_R_FatJets<0.8)
	    //this implements all the reasonable possibilities!
	    {
	      number_bs_matched_to_FatJet += 1;
	    }
	}
	CHSFatJetsVect[r].addUserInt("nMatchedGenBquarks",number_bs_matched_to_FatJet);
      }

    

    // Gen-matching: calo corrections
    std::vector<pat::Jet> TempMatchedFatJetsVect;
    
    //Loop over GenBquarks structure, we need corrections and gen info
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R = 1000.;
	current_delta_R = 1000.;
	for(unsigned int a = 0; a<CHSFatJetsVect.size(); a++)
	  {
	    current_delta_R = fabs(reco::deltaR(CHSFatJetsVect[a].eta(),CHSFatJetsVect[a].phi(),GenBquarks[b].corrCaloEta,GenBquarks[b].corrCaloPhi));
	    if(current_delta_R<0.8 && current_delta_R<delta_R)

	      {
		delta_R = min(delta_R,current_delta_R);
		TempMatchedFatJetsVect.push_back(CHSFatJetsVect[a]);//duplicates possible, must be removed afterwards!
		CHSFatJetsVect[a].addUserFloat("radiusLLPCaloCorr",GenBquarks[b].travelRadiusLLP);
		CHSFatJetsVect[a].addUserFloat("xLLPCaloCorr",GenBquarks[b].travelXLLP);
		CHSFatJetsVect[a].addUserFloat("yLLPCaloCorr",GenBquarks[b].travelYLLP);
		CHSFatJetsVect[a].addUserFloat("zLLPCaloCorr",GenBquarks[b].travelZLLP);
		CHSFatJetsVect[a].addUserFloat("xGenbCaloCorr",GenBquarks[b].vx);
		CHSFatJetsVect[a].addUserFloat("yGenbCaloCorr",GenBquarks[b].vy);
		CHSFatJetsVect[a].addUserFloat("zGenbCaloCorr",GenBquarks[b].vz);
	      }
	  }

      }

    //Remove duplicates from Temp Matched CHSJets Vector
    //auto comp_tmp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    last_tmp = std::unique(TempMatchedFatJetsVect.begin(), TempMatchedFatJetsVect.end(),comp_tmp);
    TempMatchedFatJetsVect.erase(last_tmp, TempMatchedFatJetsVect.end());


    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSFatJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<TempMatchedFatJetsVect.size(); s++)
	  {

	    if(TempMatchedFatJetsVect[s].pt()==CHSFatJetsVect[r].pt()) CHSFatJetsVect[r].addUserInt("isGenMatchedCaloCorr",1);

	  }
	  
	  
	//add number of b's matched to jet
	current_delta_R = 1000.;
	int number_bs_matched_to_FatJet_CaloCorr = 0;
	for (unsigned int b = 0; b<GenBquarks.size(); b++){
	  current_delta_R = fabs(reco::deltaR(CHSFatJetsVect[r].eta(),CHSFatJetsVect[r].phi(),GenBquarks[b].corrCaloEta,GenBquarks[b].corrCaloPhi));
	  if(current_delta_R<0.8)
	    //this implements all the reasonable possibilities!
	    {
	      number_bs_matched_to_FatJet_CaloCorr += 1;
	    }
	}
	CHSFatJetsVect[r].addUserInt("nMatchedGenBquarksCaloCorr",number_bs_matched_to_FatJet_CaloCorr);

      }
      
    TempMatchedFatJetsVect.clear();
     




    // Gen-matching: calo corrections and LLP in acceptance 
    //Loop over GenBquarks structure, we need corrections and gen info
    for(unsigned int b = 0; b<GenBquarks.size(); b++)
      {
	delta_R = 1000.;
	current_delta_R = 1000.;
	for(unsigned int a = 0; a<CHSFatJetsVect.size(); a++)
	  {
	    current_delta_R = fabs(reco::deltaR(CHSFatJetsVect[a].eta(),CHSFatJetsVect[a].phi(),GenBquarks[b].corrCaloEta,GenBquarks[b].corrCaloPhi));
	    if(current_delta_R<0.8 && current_delta_R<delta_R && GenBquarks[b].isLLPInCaloAcceptance)

	      {
		delta_R = min(delta_R,current_delta_R);
		TempMatchedFatJetsVect.push_back(CHSFatJetsVect[a]);//duplicates possible, must be removed afterwards!
	      }
	  }

      }

    //Remove duplicates from Temp Matched CHSJets Vector
    //auto comp_tmp = [] ( const pat::Jet& lhs, const pat::Jet& rhs ) {return lhs.pt() ==rhs.pt();};
    last_tmp = std::unique(TempMatchedFatJetsVect.begin(), TempMatchedFatJetsVect.end(),comp_tmp);
    TempMatchedFatJetsVect.erase(last_tmp, TempMatchedFatJetsVect.end());


    // add b-matching infos into original jet
    for(unsigned int r = 0; r<CHSFatJetsVect.size(); r++)
      {
	for(unsigned int s = 0; s<TempMatchedFatJetsVect.size(); s++)
	  {

	    if(TempMatchedFatJetsVect[s].pt()==CHSFatJetsVect[r].pt()) CHSFatJetsVect[r].addUserInt("isGenMatchedCaloCorrLLPAccept",1);

	  }

      }
      
    TempMatchedFatJetsVect.clear();      




    /////////////////////////////////////////////////////////////

    //Remove jets tagged as VBF from the list of potential signal...later!!!
    /*
    if(PerformVBF)
      {

	for(unsigned int r = 0; r<CHSFatJetsVect.size(); r++)
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
    */
    nCHSFatJets = CHSFatJetsVect.size();










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
    //old, just for debugging
    //PFCandidates.clear();

    // PFCandidate variables
    std::vector<pat::PackedCandidate> PFCandidateVect;
    std::vector<int> PFCandidateAK4JetIndex;
    //std::vector<int> PFCandidateAK8JetIndex;
    std::vector<int> PFCandidateVtxIndex;

    //simpler
    std::vector<pat::PackedCandidate> PFCandidateVectAK4;
    //std::vector<pat::PackedCandidate> PFCandidateVectAK8;
    std::vector<int> PFAK4JetIndex;
    //std::vector<int> PFAK8JetIndex;//not very good


    std::vector<reco::CandSecondaryVertexTagInfo *> bTagInfoVect;
    std::vector<reco::CandIPTagInfo *> bTagIPInfoVect;
    std::vector<int> indexSVJet;

    PFCandidateVect = thePFCandidateAnalyzer->FillPFCandidateVector(iEvent);
    //Here sort in pt
    std::sort(PFCandidateVect.begin(), PFCandidateVect.end(), AODNtuplizer::pt_sorter);

    // Initialize PFCandidate variables: Set indices to -1 (not matched)
    for(unsigned int i = 0; i < PFCandidateVect.size(); i++){
      PFCandidateAK4JetIndex.push_back(-1);
      //PFCandidateAK8JetIndex.push_back(-1);
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
	    //simpler:
	    PFCandidateVectAK4.push_back(PFCandidateVect[i]);
	    PFAK4JetIndex.push_back(j);
	    PFCandidateAK4JetIndex[i]=j;
	    nMatchedAK4Jets++;
	    nPFCandidatesMatchedToAK4Jet++;
            //nPFCandidatesMatchedToAnyJet++;
	  }

	}

      }
      //std::cout << "size of pf candidates: " << PFCandidateVect.size() << std::endl;
      //std::cout << "size of AK4 pf candidates: " << PFCandidateVectAK4.size() << std::endl;
      //std::cout << "nPFCandidatesMatchedToAK4Jet: " << nPFCandidatesMatchedToAK4Jet<< std::endl;

      if (nMatchedAK4Jets > 1) edm::LogWarning("PFCandidate-Jet Matching") << "More than 1 AK4 jet constituent has been matched to PFCandidate";



     // PVs
      for(unsigned int j = 0; j < PVertexVect.size(); j++){

	if (PFCandidateVect[i].vertexRef()->position() == PVertexVect[j].position()){
	  PFCandidateVtxIndex[i]=j;
	  nMatchedPVs++;
	}
      }

      if (nMatchedPVs > 1) edm::LogWarning("PFCandidate-PV") << "WARNING: More than 1 PV has been matched to PFCandidate " << i << std::endl;


    }



    //Remove duplicates from PFCandidateVectAK8
    //Dangerous, might mismatch jet indices association, must do it in a loop
    //auto comp_pf = [] ( const pat::PackedCandidate& lhs, const pat::PackedCandidate& rhs ) {return lhs.pt() ==rhs.pt();};
    //auto last_pf = std::unique(PFCandidateVectAK8.begin(), PFCandidateVectAK8.end(),comp_pf);
    //PFCandidateVectAK8.erase(last_pf, PFCandidateVectAK8.end());

    //if(WriteAK4JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK4Jet; i++) PFCandidates.push_back( PFCandidateType() );
    if(WriteAK4JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK4Jet; i++) PFCandidatesAK4.push_back( PFCandidateType() );
    //different//if(WriteAK8JetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAK8Jet; i++) PFCandidatesAK8.push_back( PFCandidateType() );
    //if(WriteAllJetPFCandidates) for(unsigned int i = 0; i < nPFCandidatesMatchedToAnyJet; i++) PFCandidates.push_back( PFCandidateType() );
    //if(WriteAllPFCandidates)    for(unsigned int i = 0; i < PFCandidateVect.size();       i++) PFCandidates.push_back( PFCandidateType() );

    //------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------
    // EXO-16-003 variables and and n(Pixel)Hits
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
 

    //AK8 jets, new loops with new variables
   

//AAAAAAAA
   
    for (unsigned int j = 0; j < CHSFatJetsVect.size(); j++){

      //Caltech; some still to be understood
      reco::Vertex primaryVertexAK8 = PVertexVect.at(0);
      std::vector<float> IP2DsAK8;
      std::vector<float> theta2DsAK8;
      std::vector<float> nPixelHitsAK8;//method seems not available
      std::vector<float> nHitsAK8;
      std::vector<float> dzVectAK8;
      std::vector<float> dxyVectAK8;
      
      float ptAllTracksAK8 = 0.;//Caltech: pt sum of generalTracks inside jet cone
      float ptAllPVTracksAK8 = 0.;//Caltech: pt sum of tracks belonging to any PV inside jet cone
      float ptPVTracksMaxAK8 = 0.;//Caltech: maximum pt sum of tracks in a vertex inside jet cone
      int   nTracksAllAK8 = 0;//Caltech: num of generalTracks inside jet cone
      int   nTracksPVMaxAK8 = 0;//Caltech: maximum number of tracks in a vertex inside jet cone
      
      float medianIP2DAK8 = -10000.;
      float medianTheta2DAK8 = -100.;
      
      float alphaMaxAK8 = -100.;
      float betaMaxAK8 = -100.;
      float gammaMaxAK8 = -100.;
      float gammaMaxEMAK8 = -100.;
      float gammaMaxHadronicAK8 = -100.;
      float gammaMaxETAK8 = -100.;
      float nPixelHitsMedianAK8 = -1.;
      float nHitsMedianAK8 = -1.;
      float dzMedianAK8 = -9999.;
      float dxyMedianAK8 = -9999.;
      float minDeltaRAllTracksAK8 = 999.;//Caltech: min DR bw generalTracks and current jet
      float minDeltaRPVTracksAK8 = 999.;//Caltech: min DR bw a track included in a vertex and current jet; there is a pt constraint on the total pt of tracks associated to a jet. Ask why
      

      /* Track loop */
      //int iterator_valid_track = 0;
      for (unsigned int iTrack = 0; iTrack < generalTracks->size(); iTrack ++){

        // Track propagation
        FreeTrajectoryState ftsAK8 = trajectoryStateTransform::initialFreeState (generalTracksView->at(iTrack),MagneticFieldTag);
        TrajectoryStateOnSurface outerAK8 = stateOnTracker(ftsAK8);
        if(!outerAK8.isValid()) continue;
        GlobalPoint outerPosAK8 = outerAK8.globalPosition();

        TLorentzVector generalTrackVecTempAK8;
        generalTrackVecTempAK8.SetPtEtaPhiM((generalTracks->at(iTrack)).pt(), outerPosAK8.eta(), outerPosAK8.phi(), 0);

        if ((generalTracks->at(iTrack)).pt() > 1) {
          if (minDeltaRAllTracksAK8 > reco::deltaR(generalTrackVecTempAK8.Eta(),generalTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi()) )
	  {
	      minDeltaRAllTracksAK8 =  reco::deltaR(generalTrackVecTempAK8.Eta(),generalTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi());
	      //std::cout << "minDeltaRAllTracks " << minDeltaRAllTracks << std::endl;
	  }
	  if (reco::deltaR(generalTrackVecTempAK8.Eta(),generalTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi()) < 0.8)
	  {
    	  	nTracksAllAK8 ++;
    	  	//tot pt for alpha
    	 	ptAllTracksAK8 += (generalTracks->at(iTrack)).pt();	                   
                 nPixelHitsAK8.push_back((generalTracks->at(iTrack)).hitPattern().numberOfValidPixelHits());
                 nHitsAK8.push_back((generalTracks->at(iTrack)).hitPattern().numberOfValidTrackerHits());
                 dzVectAK8.push_back((generalTracks->at(iTrack)).dz());
                 dxyVectAK8.push_back((generalTracks->at(iTrack)).dxy());

           }//if track in jet cone
        }//if tracks pt>1 GeV
        
      }//loop on general tracks
 


      /*Vertex loop */
      if (ptAllTracksAK8 > 0.9){
        //No matched jets
        //int iterator_vertex = 0;
        for (auto vertex = PVertexVect.begin(); vertex != PVertexVect.end(); vertex++){
          double ptPVTracksAK8 = 0.;//pt of tracks associated to one singular PV and inside current jet cone
          int nTracksPVTempAK8 = 0;//number of tracks associated to one singular PV and inside current jet cone
          if(!vertex->isValid())continue;
          if (vertex->isFake())continue;
          //std::cout << "Valid vertex n. " << iterator_vertex << std::endl;
          //iterator_vertex++;
          for(auto pvTrack=vertex->tracks_begin(); pvTrack!=vertex->tracks_end(); pvTrack++){

              // Track propagation
              FreeTrajectoryState ftspvAK8 = trajectoryStateTransform::initialFreeState (**pvTrack, MagneticFieldTag);
              TrajectoryStateOnSurface outerpvAK8 = stateOnTracker(ftspvAK8);
              if(!outerpvAK8.isValid()) continue;
              GlobalPoint outerpvPosAK8 = outerpvAK8.globalPosition();

    	      TLorentzVector pvTrackVecTempAK8;
    	      pvTrackVecTempAK8.SetPtEtaPhiM((*pvTrack)->pt(),outerpvPosAK8.eta(),outerpvPosAK8.phi(),0);
  	      //If pv track associated with jet add pt to ptPVTracks
    	      if ((*pvTrack)->pt() > 1)
    	      {
    	        if (minDeltaRPVTracksAK8 > reco::deltaR(pvTrackVecTempAK8.Eta(),pvTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi()))
    	        {
    	          minDeltaRPVTracksAK8 =  reco::deltaR(pvTrackVecTempAK8.Eta(),pvTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi());
    	        }
    	        if(reco::deltaR(pvTrackVecTempAK8.Eta(),pvTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi()) < 0.8)
    	        {
    	           //std::cout << "Valid track inside vertex n. " << iterator_vertex << "; track pt: " << (*pvTrack)->pt() << std::endl;
                   ptPVTracksAK8 += (*pvTrack)->pt();//pt sum per vertex
                   ptAllPVTracksAK8 += (*pvTrack)->pt();//pt sum over all vertices
                   nTracksPVTempAK8++;//number of tracks associated to one particular vertex
    	        }//jet matching
              }//minimum track pt
           
              if (ptPVTracksAK8 > ptPVTracksMaxAK8) {
      	        ptPVTracksMaxAK8 = ptPVTracksAK8;
      	        nTracksPVMaxAK8 = nTracksPVTempAK8;
      	      }
      	     
          }//loop on vertex tracks
           
  	}//loop on vertices
  	
      }//if pt all tracks
 


      /* Track loop, without propagator, for sigIP2D and theta2D */
      for (unsigned int iTrack = 0; iTrack < generalTracks->size(); iTrack ++){
  	reco::Track generalTrack = generalTracks->at(iTrack);
  	TLorentzVector generalTrackVecTempAK8;
  	generalTrackVecTempAK8.SetPtEtaPhiM(generalTrack.pt(),generalTrack.eta(),generalTrack.phi(),0);

  	if (generalTrack.pt() > 1) {
	    if (reco::deltaR(generalTrackVecTempAK8.Eta(),generalTrackVecTempAK8.Phi(),CHSFatJetsVect.at(j).eta(),CHSFatJetsVect.at(j).phi()) < 0.8){
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
    		std::pair<bool, Measurement1D> ip2d = IPTools::absoluteTransverseImpactParameter(transTrack,primaryVertexAK8);
    		IP2DsAK8.push_back(ip2d.second.value()/ip2d.second.error());
            }//jet DR matching
        }//track pt>1 GeV
        
      }//second loop on general tracks



      std::sort(IP2DsAK8.begin(),IP2DsAK8.end());
      //if (IP2DsAK8.size() % 2 == 0) medianIP2D = ((IP2DsAK8[IP2DsAK8.size()/2 -1] + IP2DsAK8[IP2DsAK8.size()/2) /2);//HH
      //else medianIP2D = IP2DsAK8[IP2DsAK8.size()/2];//HH
      if (IP2DsAK8.size() > 0){
	   medianIP2DAK8 = IP2DsAK8[IP2DsAK8.size()/2];
      }
      
      std::sort(theta2DsAK8.begin(),theta2DsAK8.end());
      //if (theta2DsAK8.size() % 2 == 0) medianTheta2DAK8 = ((theta2DsAK8[theta2DsAK8.size()/2 -1] + theta2DsAK8[theta2DsAK8.size()/2) /2);//HH
      //else medianTheta2DAK8 = theta2DsAK8[theta2DsAK8.size()/2];//HH
      if (theta2DsAK8.size() > 0){
          medianTheta2DAK8 = theta2DsAK8[theta2DsAK8.size()/2];
      }

      std::sort(nPixelHitsAK8.begin(), nPixelHitsAK8.end());
      if (nPixelHitsAK8.size() > 0) {   
        if (nPixelHitsAK8.size() % 2 ==0) nPixelHitsMedianAK8 = ((nPixelHitsAK8[nPixelHitsAK8.size()/2 -1] + nPixelHitsAK8[nPixelHitsAK8.size()/2]) /2);
        else nPixelHitsMedianAK8 = nPixelHitsAK8[nPixelHitsAK8.size()/2];
      }
      
      std::sort(nHitsAK8.begin(), nHitsAK8.end());
      if (nHitsAK8.size() > 0) {   
        if (nHitsAK8.size() % 2 ==0) nHitsMedianAK8 = ((nHitsAK8[nHitsAK8.size()/2 -1] + nHitsAK8[nHitsAK8.size()/2]) /2);
        else nHitsMedianAK8 = nHitsAK8[nHitsAK8.size()/2];
      }

      std::sort(dxyVectAK8.begin(), dxyVectAK8.end());
      if (dxyVectAK8.size() > 0) {
	if (dxyVectAK8.size() % 2 ==0) dxyMedianAK8 = ((dxyVectAK8[dxyVectAK8.size()/2 -1] + dxyVectAK8[dxyVectAK8.size()/2]) /2);
	else dxyMedianAK8 = dxyVectAK8[dxyVectAK8.size()/2];
      }

      std::sort(dzVectAK8.begin(), dzVectAK8.end());
      if (dzVectAK8.size() > 0) {
	if (dzVectAK8.size() % 2 ==0) dzMedianAK8 = ((dzVectAK8[dzVectAK8.size()/2 -1] + dzVectAK8[dzVectAK8.size()/2]) /2);
	else dzMedianAK8 = dzVectAK8[dzVectAK8.size()/2];
      }



      
      //std::cout << "Out of vertex loop, recalculate alphaMax " << std::endl;
      alphaMaxAK8         = ptAllTracksAK8>0 ? ptPVTracksMaxAK8/ptAllTracksAK8 : -100.;
      betaMaxAK8          = ptAllTracksAK8>0 ? ptPVTracksMaxAK8/CHSFatJetsVect[j].pt() : -100.;
      gammaMaxAK8         = ptAllTracksAK8>0 ? ptPVTracksMaxAK8/CHSFatJetsVect[j].energy() : -100.;
      gammaMaxEMAK8       = ( (CHSFatJetsVect[j].userFloat("photonEFrac") + CHSFatJetsVect[j].userFloat("eleEFrac"))>0 && ptAllTracksAK8>0 ) ? ptPVTracksMaxAK8/(CHSFatJetsVect[j].energy()*(CHSFatJetsVect[j].userFloat("photonEFrac") + CHSFatJetsVect[j].userFloat("eleEFrac"))) : -100.;
      gammaMaxHadronicAK8 = ( (CHSFatJetsVect[j].userFloat("cHadEFrac") + CHSFatJetsVect[j].userFloat("nHadEFrac"))>0 && ptAllTracksAK8>0 ) ? ptPVTracksMaxAK8/(CHSFatJetsVect[j].energy()*(CHSFatJetsVect[j].userFloat("cHadEFrac") + CHSFatJetsVect[j].userFloat("nHadEFrac"))) : -100.;
      gammaMaxETAK8       = ptAllTracksAK8>0 ? ptPVTracksMaxAK8/CHSFatJetsVect[j].et() : -100.;    
      //std::cout << "Jet[" << j << "] has nTracksAll: " << nTracksAll << "; and ptAllTracks: " << ptAllTracks << " and nTracksPVMax " << nTracksPVMax << " and ptPVTracksMax " << ptPVTracksMax << "; alphaMax " << alphaMax << "; medianIP2D " << medianIP2D << "; medianTheta2D " << medianTheta2D << std::endl;


      CHSFatJetsVect[j].addUserInt("nTracksAll", nTracksAllAK8);
      CHSFatJetsVect[j].addUserInt("nTracksPVMax", nTracksPVMaxAK8);
      CHSFatJetsVect[j].addUserFloat("ptAllTracks", ptAllTracksAK8>0 ? ptAllTracksAK8 : -1.);
      CHSFatJetsVect[j].addUserFloat("ptAllPVTracks", ptAllPVTracksAK8>0 ? ptAllPVTracksAK8 : -1.);
      CHSFatJetsVect[j].addUserFloat("ptPVTracksMax", ptPVTracksMaxAK8>0 ? ptPVTracksMaxAK8 : -1.);
      CHSFatJetsVect[j].addUserFloat("alphaMax", alphaMaxAK8);
      CHSFatJetsVect[j].addUserFloat("betaMax", betaMaxAK8);//zero if no tracks
      CHSFatJetsVect[j].addUserFloat("gammaMax", gammaMaxAK8);//zero if no tracks
      CHSFatJetsVect[j].addUserFloat("gammaMaxEM", gammaMaxEMAK8);//zero if no tracks, but -100 if no EM EFrac
      CHSFatJetsVect[j].addUserFloat("gammaMaxHadronic", gammaMaxHadronicAK8);//zero if no tracks, but -100 if no hadronEFrac
      CHSFatJetsVect[j].addUserFloat("gammaMaxET", gammaMaxETAK8);//zero if no tracks
      CHSFatJetsVect[j].addUserFloat("minDeltaRAllTracks",minDeltaRAllTracksAK8);
      CHSFatJetsVect[j].addUserFloat("minDeltaRPVTracks",minDeltaRPVTracksAK8);
      CHSFatJetsVect[j].addUserFloat("medianIP2D", medianIP2DAK8);
      CHSFatJetsVect[j].addUserFloat("medianTheta2D", medianTheta2DAK8);
      CHSFatJetsVect[j].addUserFloat("nPixelHitsMedian", nPixelHitsMedianAK8);
      CHSFatJetsVect[j].addUserFloat("nHitsMedian", nHitsMedianAK8);
      CHSFatJetsVect[j].addUserFloat("dxyMedian", dxyMedianAK8);
      CHSFatJetsVect[j].addUserFloat("dzMedian", dzMedianAK8);
      
    }//loop on AK8 jets



    // AK4 jets
    /* OLD LOOP, with PFCandidates */
    // we can calculate minor-major jet axes according to JME-13-002

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

      //jet shape
      std::vector<double> PF_eta;
      std::vector<double> PF_pt;
      std::vector<double> PF_pt_squared;
      std::vector<double> PF_phi;
      std::pair< std::pair<float,float> ,float> sigPF;

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

	  //jet shapes variables
	  PF_eta.push_back(PFCandidateVect[i].eta());
	  PF_phi.push_back(PFCandidateVect[i].phi());
	  PF_pt.push_back(PFCandidateVect[i].pt());
	  PF_pt_squared.push_back(pow(PFCandidateVect[i].pt(),2));

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

      //jet shape
      sigPF = theCHSJetAnalyzer->JetSecondMoments(PF_pt, PF_eta, PF_phi);

      CHSJetsVect[j].addUserFloat("sig1PF", sigPF.first.first>0 ? sigPF.first.first : -1.);
      CHSJetsVect[j].addUserFloat("sig2PF", sigPF.first.second>0 ? sigPF.first.second : -1.);
      CHSJetsVect[j].addUserFloat("sigAvPF", (sigPF.first.first>0 and sigPF.first.second>0) ? sqrt( pow(sigPF.first.first,2) + pow(sigPF.first.second,2) )  : -1.);
      CHSJetsVect[j].addUserFloat("tan2thetaPF", sigPF.second);
      CHSJetsVect[j].addUserFloat("ptDPF", accumulate(PF_pt.begin(),PF_pt.end(),0) > 0 ? sqrt(accumulate(PF_pt_squared.begin(),PF_pt_squared.end(),0)) / accumulate(PF_pt.begin(),PF_pt.end(),0) : -1.);


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
   
    /*
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
    
    //RecoObjectsFormat::FillRecoMEtType(RecoMEt, &RecoMET, isMC);//wait, to be fixed
    ObjectsFormat::FillMEtType(MEt, &MET, isMC);//wait, to be fixed
    ObjectsFormat::FillCandidateType(VBF, &theVBF, isMC);//wait, to be fixed

    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) CHSJets.push_back( JetType() );
    for(unsigned int i = 0; i < CHSJetsVect.size(); i++) ObjectsFormat::FillJetType(CHSJets[i], &CHSJetsVect[i], isMC);

    for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) CHSFatJets.push_back( FatJetType() );
    for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) ObjectsFormat::FillFatJetType(CHSFatJets[i], &CHSFatJetsVect[i], SoftdropPuppiMassString, isMC);
    
    for(unsigned int i = 0; i < MuonVect.size(); i++) Muons.push_back( LeptonType() );
    for(unsigned int i = 0; i < MuonVect.size(); i++) ObjectsFormat::FillMuonType(Muons[i], &MuonVect[i], isMC);

    for(unsigned int i = 0; i < ElecVect.size(); i++) Electrons.push_back( LeptonType() );
    for(unsigned int i = 0; i < ElecVect.size(); i++) ObjectsFormat::FillElectronType(Electrons[i], &ElecVect[i], isMC);

    for(unsigned int i = 0; i < PhotonVect.size(); i++) Photons.push_back( PhotonType() );
    for(unsigned int i = 0; i < PhotonVect.size(); i++) ObjectsFormat::FillPhotonType(Photons[i], &PhotonVect[i], isMC);

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
    //Unneccessaricily complicated. One loop for AK4 and one for AK8.
    /*
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
    */

    if(WriteAK4JetPFCandidates)
      {
	for(unsigned int i = 0; i < PFCandidateVectAK4.size(); i++) ObjectsFormat::FillPFCandidateType(PFCandidatesAK4[i], &PFCandidateVectAK4[i], PFAK4JetIndex[i], -1, -1);
      }

    /* FIXME!
    if(WriteAK8JetPFCandidates)
      {
	for(unsigned int i = 0; i < PFCandidateVectAK8.size(); i++) ObjectsFormat::FillPFCandidateType(PFCandidatesAK8[i], &PFCandidateVectAK8[i], -1, PFAK8JetIndex[i], -1);
      }
    */

    ////StandAloneMuons
    //for(unsigned int i =0; i< StandAloneMuonsVect.size();i++) ObjectsFormat::FillTrackType(StandAloneMuons[i], &StandAloneMuonsVect[i], GenStandAloneMuonsFlag[i]);
    ////DisplacedStandAloneMuons
    //for(unsigned int i =0; i< DisplacedStandAloneMuonsVect.size();i++) ObjectsFormat::FillTrackType(DisplacedStandAloneMuons[i], &DisplacedStandAloneMuonsVect[i],GenDisplacedStandAloneMuonsFlag[i]);
      


    if(isVerbose) {
      //Write a summary, in verbose mode
      std::cout << " --- Event n. " << iEvent.id().event() << ", lumi " << iEvent.luminosityBlock() << ", run " << iEvent.id().run() << std::endl;

      //std::cout << "Gen Higgs size:  " << GenHiggsVect.size() << std::endl;
      //for(unsigned int i = 0; i < GenHiggsVect.size(); i++)
      //{
      //std::cout <<  "[" << i  << "]"<< std::endl;
      //std::cout << "vertex coordinates: (" << GenHiggsVect.at(i).vx() << " , " << GenHiggsVect.at(i).vy() << " , " << GenHiggsVect.at(i).vz() << ")" << std::endl;
      //std::cout << "momentum: (" << GenHiggsVect.at(i).px() << " , " << GenHiggsVect.at(i).py() << " , " << GenHiggsVect.at(i).pz() << ")" << std::endl;
      //}

      //std::cout << "Gen Long Lived size:  " << GenLongLivedVect.size() << std::endl;
      //for(unsigned int i = 0; i < GenLongLivedVect.size(); i++)
      //{
      //std::cout <<  "[" << i  << "]"<< std::endl;
      //std::cout << "vertex coordinates: (" << GenLongLivedVect.at(i).vx() << " , " << GenLongLivedVect.at(i).vy() << " , " << GenLongLivedVect.at(i).vz() << ")" << std::endl;
      //std::cout << "momentum: (" << GenLongLivedVect.at(i).px() << " , " << GenLongLivedVect.at(i).py() << " , " << GenLongLivedVect.at(i).pz() << ")" << std::endl;
      //}

      //std::cout << "Gen b quarks size:  " << GenBquarksVect.size() << std::endl;
      //for(unsigned int i = 0; i < GenBquarksVect.size(); i++)
      //{
      //std::cout <<  "[" << i  << "]"<< std::endl;
      //std::cout << "vertex coordinates: (" << GenBquarksVect.at(i).vx() << " , " << GenBquarksVect.at(i).vy() << " , " << GenBquarksVect.at(i).vz() << ")" << std::endl;
      //std::cout << "momentum: (" << GenBquarksVect.at(i).px() << " , " << GenBquarksVect.at(i).py() << " , " << GenBquarksVect.at(i).pz() << ")" << std::endl;
      //std::cout << "2D cos(vertex-momentum):" << (GenBquarksVect.at(i).px()*GenBquarksVect.at(i).vx() + GenBquarksVect.at(i).py()*GenBquarksVect.at(i).vy())/(GenBquarksVect.at(i).pt()* sqrt(GenBquarksVect.at(i).vx()*GenBquarksVect.at(i).vx() + GenBquarksVect.at(i).vy()*GenBquarksVect.at(i).vy()) ) << std::endl;
      //std::cout << "3D cos(vertex-momentum):" << (GenBquarksVect.at(i).px()*GenBquarksVect.at(i).vx() + GenBquarksVect.at(i).py()*GenBquarksVect.at(i).vy() + GenBquarksVect.at(i).pz()*GenBquarksVect.at(i).vz()  )/(GenBquarksVect.at(i).p()* sqrt(GenBquarksVect.at(i).vx()*GenBquarksVect.at(i).vx() + GenBquarksVect.at(i).vy()*GenBquarksVect.at(i).vy() + GenBquarksVect.at(i).vz()*GenBquarksVect.at(i).vz()) ) << std::endl;
      //std::cout << "~~~" << std::endl;
      //std::cout << "2D cos(angle w.r.t. Higgs [0]): " << (GenBquarksVect.at(i).px()*GenHiggsVect.at(0).px() + GenBquarksVect.at(i).py()*GenHiggsVect.at(0).py())/(GenBquarksVect.at(i).pt()*GenHiggsVect.at(0).pt())  << std::endl;
      //std::cout << "2D cos(angle w.r.t. Higgs [1]): " << (GenBquarksVect.at(i).px()*GenHiggsVect.at(1).px() + GenBquarksVect.at(i).py()*GenHiggsVect.at(1).py())/(GenBquarksVect.at(i).pt()*GenHiggsVect.at(1).pt())  << std::endl;
      //std::cout << "DR w.r.t. Higgs [0]): " << reco::deltaR(GenBquarksVect.at(i).eta(),GenBquarksVect.at(i).phi(),GenHiggsVect.at(0).eta(),GenHiggsVect.at(0).phi())  << std::endl;
      //std::cout << "DR w.r.t. Higgs [1]): " << reco::deltaR(GenBquarksVect.at(i).eta(),GenBquarksVect.at(i).phi(),GenHiggsVect.at(1).eta(),GenHiggsVect.at(1).phi())  << std::endl;
      ////std::cout << "~~~" << std::endl;
      ////std::cout << "2D cos(angle w.r.t. LongLived [0]): " << (GenBquarksVect.at(i).px()*GenLongLivedVect.at(0).px() + GenBquarksVect.at(i).py()*GenLongLivedVect.at(0).py())/(GenBquarksVect.at(i).pt()*GenLongLivedVect.at(0).pt())  << std::endl;
      ////std::cout << "2D cos(angle w.r.t. LongLived [1]): " << (GenBquarksVect.at(i).px()*GenLongLivedVect.at(1).px() + GenBquarksVect.at(i).py()*GenLongLivedVect.at(1).py())/(GenBquarksVect.at(i).pt()*GenLongLivedVect.at(1).pt())  << std::endl;
      ////std::cout << "DR w.r.t. LongLived [0]): " << reco::deltaR(GenBquarksVect.at(i).eta(),GenBquarksVect.at(i).phi(),GenLongLivedVect.at(0).eta(),GenLongLivedVect.at(0).phi())  << std::endl;
      ////std::cout << "DR w.r.t. LongLived [1]): " << reco::deltaR(GenBquarksVect.at(i).eta(),GenBquarksVect.at(i).phi(),GenLongLivedVect.at(1).eta(),GenLongLivedVect.at(1).phi())  << std::endl;

      //}

      std::cout << "number of CHS AK4 jets:  " << CHSJetsVect.size() << std::endl;
      for(unsigned int i = 0; i < CHSJetsVect.size(); i++) std::cout << "  CHS AK4 jet  [" << i << "]\tpt: " << CHSJetsVect[i].pt() << "\teta: " << CHSJetsVect[i].eta() << "\tphi: " << CHSJetsVect[i].phi() << "\tmass: " << CHSJetsVect[i].mass() << "\tcHadEFrac: " << CHSJetsVect[i].userFloat("cHadEFrac") << std::endl;

      ////std::cout << "VBF jets pair:  " << VBFPairJetsVect.size() << std::endl;
      ////if(isVBF) std::cout << "VBF conditions satisfied" << std::endl;
      ////for(unsigned int i = 0; i < VBFPairJetsVect.size(); i++) std::cout << "  VBF jet  [" << i << "]\tpt: " << VBFPairJetsVect[i].pt() << "\teta: " << VBFPairJetsVect[i].eta() << "\tphi: " << VBFPairJetsVect[i].phi() << "\tmass: " << VBFPairJetsVect[i].mass() << std::endl;

      //std::cout << "number of Gen B quarks:  " << GenBquarksVect.size() << std::endl;
      //for(unsigned int i = 0; i < GenBquarksVect.size(); i++) {std::cout << "  Gen B quark  [" << i << "]\tpt: " << GenBquarksVect[i].pt() << "\teta: " << GenBquarksVect[i].eta() << "\tphi: " << GenBquarksVect[i].phi() << "\tradius (in cm): " << ( GenBquarksVect[i].mother() ? sqrt(pow(GenBquarksVect[i].vx() - GenBquarksVect[i].mother()->vx(),2) + pow(GenBquarksVect[i].vy() - GenBquarksVect[i].mother()->vy(),2) + pow(GenBquarksVect[i].vz() - GenBquarksVect[i].mother()->vz(),2)) : -1000. ) << "\tradius 2D (in cm): " << ( GenBquarksVect[i].mother() ? sqrt(pow(GenBquarksVect[i].vx() - GenBquarksVect[i].mother()->vx(),2) + pow(GenBquarksVect[i].vy() - GenBquarksVect[i].mother()->vy(),2)) : -1000. ) << std::endl;}

      std::cout << "Missing ET:  " << std::endl;
      std::cout << "  pt: " << MET.pt() << "\tphi: " << MET.phi() << std::endl;

      //std::cout << "number of CHS AK4 jets matched to b quarks:  " << MatchedCHSJetsVect.size() << std::endl;
      //for(unsigned int i = 0; i < MatchedCHSJetsVect.size(); i++) std::cout << "  Matched CHS AK4 jet  [" << i << "]\tpt: " << MatchedCHSJetsVect[i].pt() << "\teta: " << MatchedCHSJetsVect[i].eta() << "\tphi: " << MatchedCHSJetsVect[i].phi() << "\tmass: " << MatchedCHSJetsVect[i].mass() << "\tnTrackConstituents: " << MatchedCHSJetsVect[i].chargedMultiplicity() << std::endl;

      //std::cout << "number of Calo AK4 jets:  " << CaloJetsVect.size() << std::endl;
      //for(unsigned int i = 0; i < CaloJetsVect.size(); i++) std::cout << "  Calo AK4 jet  [" << i << "]\tpt: " << CaloJetsVect[i].pt() << "\teta: " << CaloJetsVect[i].eta() << "\tphi: " << CaloJetsVect[i].phi() << "\tmass: " << CaloJetsVect[i].mass() << "\temEnergyFraction " << CaloJetsVect[i].emEnergyFraction() << std::endl;

      //std::cout << "number of Matched Calo AK4 jets:  " << MatchedCaloJetsVect.size() << std::endl;
      //for(unsigned int i = 0; i < MatchedCaloJetsVect.size(); i++) std::cout << "  Calo AK4 jet  [" << i << "]\tpt: " << MatchedCaloJetsVect[i].pt() << "\teta: " << MatchedCaloJetsVect[i].eta() << "\tphi: " << MatchedCaloJetsVect[i].phi() << "\tmass: " << MatchedCaloJetsVect[i].mass() << "\temEnergyFraction " << MatchedCaloJetsVect[i].emEnergyFraction() << std::endl;

      ////std::cout << "number of StandAloneMuons: " << StandAloneMuonsVect.size() << std::endl;
      ////for(unsigned int i = 0; i < StandAloneMuonsVect.size(); i++) std::cout << "  StandAloneMuons  [" << i << "]\tpt: " << StandAloneMuonsVect[i].pt() << "\teta: " << StandAloneMuonsVect[i].eta() << "\tphi: " << StandAloneMuonsVect[i].phi() << std::endl;

      ////std::cout << "number of DisplacedStandAloneMuons: " << DisplacedStandAloneMuonsVect.size() << std::endl;
      ////for(unsigned int i = 0; i < DisplacedStandAloneMuonsVect.size(); i++) std::cout << "  DisplacedStandAloneMuons  [" << i << "]\tpt: " << DisplacedStandAloneMuonsVect[i].pt() << "\teta: " << DisplacedStandAloneMuonsVect[i].eta() << "\tphi: " << DisplacedStandAloneMuonsVect[i].phi() << std::endl;

      ////std::cout << "number of DT segments:  " << DTSegmentVect.size() << std::endl;
      ////std::cout << "number of DT global position:  " << DTSegment_Global_points.size() << std::endl;
      ////for(unsigned int i = 0; i < DTSegment_Global_points.size(); i++) std::cout << "  Global position of DT segment [" << i << "]\teta: " << DTSegment_Global_points[i].eta() << "\tphi: " << DTSegment_Global_points[i].phi() << "\tsize of rech hits: "<< DTSegmentVect.at(i).recHits().size() << std::endl;


      ////std::cout << "number of CSC segments:  " << CSCSegmentVect.size() << std::endl;
      ////std::cout << "number of CSC global position:  " << CSCSegment_Global_points.size() << std::endl;
      ////for(unsigned int i = 0; i < CSCSegment_Global_points.size(); i++) std::cout << "  Global position of CSC segment [" << i << "]\teta: " << CSCSegment_Global_points[i].eta() << "\tphi: " << CSCSegment_Global_points[i].phi() << std::endl;
      ////std::cout << "number of CHS AK8 jets:  " << CHSFatJetsVect.size() << std::endl;
      ////for(unsigned int i = 0; i < CHSFatJetsVect.size(); i++) std::cout << "  AK8 jet  [" << i << "]\tpt: " << CHSFatJetsVect[i].pt() << "\teta: " << CHSFatJetsVect[i].eta() << "\tphi: " << CHSFatJetsVect[i].phi() << "\tmass: " << CHSFatJetsVect[i].mass() << std::endl;
    }



    //Fill tree
    tree -> Fill();
    if(isVerbose) std::cout << "TREE FILLED!!!!!!!!!!!! Go to next event...--->" << std::endl;

    //ManualJets.clear();
    CHSJets.clear();
    EcalRecHitsAK4.clear();
    HcalRecHitsAK4.clear();
    EcalRecHitsAK8.clear();
    HcalRecHitsAK8.clear();
    Muons.clear();
    Electrons.clear();
    Photons.clear();
    CaloJets.clear();
    VBFPairJets.clear();
    CHSFatJets.clear();
    ggHJet.clear();
    PFCandidatesAK4.clear();
    PFCandidatesAK8.clear();


    //DTRecSegments4D.clear();
    //CSCSegments.clear();

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
   tree -> Branch("nLLPInCalo" , &nLLPInCalo , "nLLPInCalo/I");
   tree -> Branch("isVBF" , &isVBF, "isVBF/O");
   tree -> Branch("isggH" , &isggH, "isggH/O");
   tree -> Branch("HT" , &HT , "HT/F");
   tree -> Branch("HTNoSmear" , &HTNoSmear , "HTNoSmear/F");
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
   //tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
   //tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
   
   
   tree -> Branch("nCHSJets" , &nCHSJets , "nCHSJets/L");
   tree -> Branch("nCaloJets" , &nCaloJets , "nCaloJets/L");
   tree -> Branch("nCHSFatJets" , &nCHSFatJets , "nCHSFatJets/L");
   tree -> Branch("nMatchedCHSJets" , &nMatchedCHSJets , "nMatchedCHSJets/L");
   tree -> Branch("nMatchedCaloJets" , &nMatchedCaloJets , "nMatchedCaloJets/L");
   tree -> Branch("nVBFGenMatchedCHSJets", & nVBFGenMatchedCHSJets, "nVBFGenMatchedCHSJets/L");
   tree -> Branch("nVBFGenMatchedVBFJets", & nVBFGenMatchedVBFJets, "nVBFGenMatchedVBFJets/L");
   //tree -> Branch("nDTSegments", &nDTSegments, "nDTSegments/L");
   //tree -> Branch("nDTSegmentsStation1", &nDTSegmentsStation1, "nDTSegmentsStation1/L");
   //tree -> Branch("nDTSegmentsStation2", &nDTSegmentsStation2, "nDTSegmentsStation2/L");
   //tree -> Branch("nDTSegmentsStation3", &nDTSegmentsStation3, "nDTSegmentsStation3/L");
   //tree -> Branch("nDTSegmentsStation4", &nDTSegmentsStation4, "nDTSegmentsStation4/L");
   //tree -> Branch("nCSCSegments", &nCSCSegments, "nCSCSegments/L");
   //tree -> Branch("nMatchedDTsegmentstob", &nMatchedDTsegmentstob, "nMatchedDTsegmentstob/L");
   //tree -> Branch("nMatchedCSCsegmentstob", &nMatchedCSCsegmentstob, "nMatchedCSCsegmentstob/L");
   //tree -> Branch("nMatchedDTsegmentstoVBF", &nMatchedDTsegmentstoVBF, "nMatchedDTsegmentstoVBF/L");
   //tree -> Branch("nMatchedCSCsegmentstoVBF", &nMatchedCSCsegmentstoVBF, "nMatchedCSCsegmentstoVBF/L");
   tree -> Branch("number_of_b_matched_to_CHSJets", &number_of_b_matched_to_CHSJets, "number_of_b_matched_to_CHSJets/L");
   tree -> Branch("number_of_b_matched_to_CaloJets", &number_of_b_matched_to_CaloJets, "number_of_b_matched_to_CaloJets/L");
   tree -> Branch("number_of_VBFGen_matched_to_CHSJets", &number_of_VBFGen_matched_to_CHSJets, "number_of_VBFGen_matched_to_CHSJets/L");
   tree -> Branch("number_of_VBFGen_matched_to_VBFJets", &number_of_VBFGen_matched_to_VBFJets, "number_of_VBFGen_matched_to_VBFJets/L");
   //tree -> Branch("number_of_b_matched_to_DTSegment4D", &number_of_b_matched_to_DTSegment4D, "number_of_b_matched_to_DTSegment4D/L");
   //tree -> Branch("number_of_b_matched_to_CSCSegment", &number_of_b_matched_to_CSCSegment, "number_of_b_matched_to_CSCSegment/L");
   //tree -> Branch("number_of_VBF_matched_to_CSCSegment", &number_of_VBF_matched_to_CSCSegment, "number_of_VBF_matched_to_CSCSegment/L");
   //tree -> Branch("number_of_VBF_matched_to_DTSegment4D", &number_of_VBF_matched_to_DTSegment4D, "number_of_VBF_matched_to_DTSegment4D/L");
   //tree -> Branch("n_segments_around_b_quark_0",&n_segments_around_b_quark_0, "n_segments_around_b_quark_0/I");
   //tree -> Branch("n_segments_around_b_quark_1",&n_segments_around_b_quark_1, "n_segments_around_b_quark_1/I");
   //tree -> Branch("n_segments_around_b_quark_2",&n_segments_around_b_quark_2, "n_segments_around_b_quark_2/I");
   //tree -> Branch("n_segments_around_b_quark_3",&n_segments_around_b_quark_3, "n_segments_around_b_quark_3/I");
   //tree -> Branch("nStandAloneMuons", &nStandAloneMuons, "nStandAloneMuons/L");
   //tree -> Branch("nDisplacedStandAloneMuons", &nDisplacedStandAloneMuons, "nDisplacedStandAloneMuons/L");
   //tree -> Branch("nMatchedStandAloneMuons", &nMatchedStandAloneMuons, "nMatchedStandAloneMuons/L");
   //tree -> Branch("nMatchedDisplacedStandAloneMuons", &nMatchedDisplacedStandAloneMuons, "nMatchedDisplacedStandAloneMuons/L");   

   // Set trigger branches
   for(auto it = TriggerMap.begin(); it != TriggerMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   for(auto it = MetFiltersMap.begin(); it != MetFiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());
   //for(auto it = L1FiltersMap.begin(); it != L1FiltersMap.end(); it++) tree->Branch(it->first.c_str(), &(it->second), (it->first+"/O").c_str());

   tree -> Branch("Flag_BadPFMuon", &BadPFMuonFlag, "Flag_BadPFMuon/O");
   tree -> Branch("Flag_BadChCand", &BadChCandFlag, "Flag_BadChCand/O");
   
   tree->Branch("Flag2_globalSuperTightHalo2016Filter", &Flag2_globalSuperTightHalo2016Filter, "Flag2_globalSuperTightHalo2016Filter/O");
   tree->Branch("Flag2_globalTightHalo2016Filter", &Flag2_globalTightHalo2016Filter, "Flag2_globalTightHalo2016Filter/O");
   tree->Branch("Flag2_goodVertices", &Flag2_goodVertices, "Flag2_goodVertices/O");
   tree->Branch("Flag2_EcalDeadCellTriggerPrimitiveFilter", &Flag2_EcalDeadCellTriggerPrimitiveFilter, "Flag2_EcalDeadCellTriggerPrimitiveFilter/O");
   tree->Branch("Flag2_HBHENoiseFilter", &Flag2_HBHENoiseFilter, "Flag2_HBHENoiseFilter/O");
   tree->Branch("Flag2_HBHEIsoNoiseFilter", &Flag2_HBHEIsoNoiseFilter, "Flag2_HBHEIsoNoiseFilter/O");
   tree->Branch("Flag2_ecalBadCalibFilter", &Flag2_ecalBadCalibFilter, "Flag2_ecalBadCalibFilter/O");
   tree->Branch("Flag2_eeBadScFilter", &Flag2_eeBadScFilter, "Flag2_eeBadScFilter/O");
   tree->Branch("Flag2_BadPFMuonFilter", &Flag2_BadPFMuonFilter, "Flag2_BadPFMuonFilter/O");
   tree->Branch("Flag2_BadChargedCandidateFilter", &Flag2_BadChargedCandidateFilter, "Flag2_BadChargedCandidateFilter/O");

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
   tree -> Branch("FatJets", &CHSFatJets);
   tree -> Branch("Muons", &Muons);
   tree -> Branch("Electrons", &Electrons);
   tree -> Branch("Photons", &Photons);
   tree -> Branch("EcalRecHitsAK4", &EcalRecHitsAK4);
   tree -> Branch("HcalRecHitsAK4", &HcalRecHitsAK4);
   tree -> Branch("EcalRecHitsAK8", &EcalRecHitsAK8);
   tree -> Branch("HcalRecHitsAK8", &HcalRecHitsAK8);
   //tree -> Branch("VBFPairJets", &VBFPairJets);//slim ntuples
   //tree -> Branch("ggHJet", &ggHJet);//slim ntuples
   //tree -> Branch("CaloJets", &CaloJets);//slim ntuples
   //tree -> Branch("VBFPair", &VBF.pt, ObjectsFormat::ListCandidateType().c_str());//wai!//slim ntuples
   //if (WriteAK4JetPFCandidates || WriteAK8JetPFCandidates || WriteAllJetPFCandidates || WriteAllPFCandidates) tree -> Branch("PFCandidates", &PFCandidates);
   if (WriteAK4JetPFCandidates) tree -> Branch("PFCandidatesAK4", &PFCandidatesAK4);
   if (WriteAK8JetPFCandidates) tree -> Branch("PFCandidatesAK8", &PFCandidatesAK8);


}

bool AODNtuplizer::pt_sorter(const pat::PackedCandidate& x, const pat::PackedCandidate& y) { return x.pt() > y.pt(); }

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
