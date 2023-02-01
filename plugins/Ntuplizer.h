// -*- C++ -*-
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

#ifndef NTUPLIZER_H
#define NTUPLIZER_H

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

#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "DataFormats/Candidate/interface/CompositePtrCandidate.h"
#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

// Split up signal samples
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"

//TagInfo
#include "DataFormats/BTauReco/interface/FeaturesTagInfo.h"
#include "LLPReco/DataFormats/interface/XTagInfo.h"
#include "LLPReco/DataFormats/interface/XTagFeatures.h"

#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

#include "fastjet/PseudoJet.hh"
#include "fastjet/contrib/Njettiness.hh"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TTree.h"
#include <string>
#include "JetAnalyzer.h"
//#include "CaloJetAnalyzer.h"
#include "GenAnalyzer.h"
#include "PileupAnalyzer.h"
#include "TriggerAnalyzer.h"
#include "ElectronAnalyzer.h"
#include "MuonAnalyzer.h"
#include "TauAnalyzer.h"
#include "PhotonAnalyzer.h"
#include "VertexAnalyzer.h"
#include "PFCandidateAnalyzer.h"
#include "ROIAnalyzer.h"
#include "Objects.h"
#include "ObjectsFormat.h"
#include "Utilities.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class Ntuplizer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit Ntuplizer(const edm::ParameterSet&);
      //explicit Ntuplizer(const edm::ParameterSet&, edm::ConsumesCollector&&);
      ~Ntuplizer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void calcNsubjettiness(const pat::Jet&, float&, float&, float&, float&, std::vector<fastjet::PseudoJet>&) const;
      virtual void endJob() override;

      // ----------member data ---------------------------
    edm::ParameterSet GenPSet;
    edm::ParameterSet PileupPSet;
    edm::ParameterSet TriggerPSet;
    edm::ParameterSet AllJetPSet;
    edm::ParameterSet CHSJetPSet;
    edm::ParameterSet VBFJetPSet;//VBF tagging
    edm::ParameterSet CHSFatJetPSet;
  //edm::ParameterSet CaloJetPSet;
    edm::ParameterSet ElectronPSet;
    edm::ParameterSet MuonPSet;
    edm::ParameterSet TauPSet;
    edm::ParameterSet PhotonPSet;
    edm::ParameterSet VertexPSet;
    edm::ParameterSet PFCandidatePSet;
    edm::ParameterSet ROIPSet;

    edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
    TString     model_;

    JetAnalyzer* AllJetAnalyzer;
    JetAnalyzer* theCHSJetAnalyzer;
    JetAnalyzer* theVBFJetAnalyzer;//VBF tagging
    JetAnalyzer* theCHSFatJetAnalyzer;
  //CaloJetAnalyzer* theCaloJetAnalyzer;
    GenAnalyzer* theGenAnalyzer;
    PileupAnalyzer* thePileupAnalyzer;
    PileupAnalyzer* thePileupAnalyzer_HLT_Mu7_IP4;
    PileupAnalyzer* thePileupAnalyzer_HLT_Mu9_IP6;
    PileupAnalyzer* thePileupAnalyzer_HLT_Mu12_IP6;
    PileupAnalyzer* thePileupAnalyzer_HLT_Mu9_IP6_v6;
    TriggerAnalyzer* theTriggerAnalyzer;
    ElectronAnalyzer* theElectronAnalyzer;
    MuonAnalyzer* theMuonAnalyzer;
    TauAnalyzer* theTauAnalyzer;
    PhotonAnalyzer* thePhotonAnalyzer;
    VertexAnalyzer* theVertexAnalyzer;
    PFCandidateAnalyzer* thePFCandidateAnalyzer;
    ROIAnalyzer* theROIAnalyzer;

    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP0p01Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP0p1Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP1Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP10Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP100Token;
    edm::EDGetTokenT<reco::JetTagCollection> JetTagWP1000Token;

    int idLLP, idHiggs, idMotherB, statusLLP, statusHiggs;
    double MinGenBpt, MaxGenBeta;
    double MinHT;
    double InvmassVBF, DetaVBF;//VBF tagging
    //int WriteNJets, WriteNFatJets;//unused, we have vectors now
    int WriteNFatJets;
    //int WriteNGenBquarks, WriteNGenLongLiveds;//unused, we have vectors now
    bool WriteGenVBFquarks, WriteGenHiggs, WriteGenLLPs, WriteGenBquarks, WriteGenMuons;
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
    bool WriteROITaggerScore;
    bool WriteROITaggerInputs;
    bool CalculateNsubjettiness;
    bool PerformPreFiringStudies;
    bool PerformVBF;
    bool PerformggH;

    std::vector<JetType> MatchedCHSJets;
    //std::vector<JetType> AllBarrelJets;
    std::vector<JetType> AllJets;
    std::vector<JetType> CHSJets;
    std::vector<JetType> VBFPairJets;
    std::vector<JetType> ggHJet;
    std::vector<FatJetType> CHSFatJets;
    //std::vector<CaloJetType> CaloJets;
    //std::vector<CaloJetType> MatchedCaloJets;
    //std::vector<CaloJetType> MatchedCaloJetsWithGenJets;
    std::vector<GenPType> GenVBFquarks;
    std::vector<GenPType> GenHiggs;
    std::vector<GenPType> GenLLPs;
    std::vector<GenPType> GenBquarks;
    std::vector<GenPType> GenMuons;
    std::vector<VertexType> PrimVertices;
    std::vector<VertexType> SecVertices;
    std::vector<VertexType> SecVerticesVert;
    //std::vector<LeptonType> Leptons;
    std::vector<LeptonType> Muons;
    std::vector<LeptonType> TightMuons;
    std::vector<LeptonType> LooseMuons;
    std::vector<LeptonType> Electrons;
    std::vector<LeptonType> LooseElectrons;
    //Jet const vector
    std::vector<PFCandidateType> PFCandidates;
    std::vector<PFCandidateType> LostTracks;
    std::vector<VertexType> BTagVertices;
    // Input objects for ROI tagger:
    std::vector<Vertex> VerticesROI;
    std::vector<LostTrack> LostTracksROI;
    std::vector<PackedPFCandidate> PFCandidatesROI;
    std::vector<TrackCluster> TrackClusters;
    std::vector<RegionOfInterest> RegionsOfInterest;
    // ROI object for ntuples
    std::vector<ROIType> ROIs;
    std::vector<float> ROIScores;
    std::vector<float> ROIDeltaR;
    std::vector<float> ROIDeltaPhi;
    std::vector<int> ROITrackClusterMultiplicity;
    std::vector<int> ROIAnnulusTrackMultiplicity;
    std::vector<float> ROIDistanceToLeadingLLP;
    std::vector<float> ROIDistanceToSubleadingLLP;



    // --------------------------------
    // TODO: Add the following (below):
    // --------------------------------
    // int nROIs; // Defined already above
    // int nROIsMatchedToLeadingLLP;
    // int nROIsMatchedToSubleadingLLP;

    int LeadingLLP, LeadingROI, SubleadingROI_dPhi2p0, MaxDisplacedJet;
    float LeadingROIScore, SubleadingROIScore_dPhi2p0;

    MEtType MEt;
    CandidateType VBF;//VBF tagging
    CandidateType Z, W;//Z, W CR

    std::map<std::string, bool> TriggerMap;
    std::map<std::string, int> PrescalesTriggerMap;
    std::map<std::string, bool> MetFiltersMap;
    std::map<std::string, bool> L1FiltersMap;

    //Initialize tree
    edm::Service<TFileService> fs;
    TTree* tree;


    //edm::EDGetTokenT<reco::JetTagCollection> BTagToken;

    bool isVerbose, isVerboseTrigger, isSignal, isCalo, isTracking, isShort, isControl, isCentralProd, is2016, is2017, is2018;
    bool isVBF, isggH;
    bool isMC;
    long int EventNumber, LumiNumber, RunNumber;
    long int nPV, nSV, nROIs;
    int MeanNumInteractions;
    bool AtLeastOneTrigger, AtLeastOneL1Filter;
    bool isIsoMu24_OR_IsoTkMu24, isMu50_OR_TkMu50;
    long int nLooseCHSJets, nTightCHSJets, nCHSJets, nAllBarrelJets, nAllJets, nVBFGenMatchedJets;
    long int nLooseCHSFatJets, nTightCHSFatJets, nCHSFatJets, nGenLL, nGenBquarks, nGenMuons;
    long int nMatchedCHSJets, nMatchedFatJets;
  //long int nCaloJets, nMatchedCaloJets, nMatchedCaloJetsWithGenJets;
    long int number_of_b_matched_to_CHSJets;
    long int number_of_b_matched_to_FatJets;
    long int number_of_VBFGen_matched_to_AllJets;
  //long int number_of_b_matched_to_CaloJets, number_of_b_matched_to_CaloJetsWithGenJets;
    long int nElectrons, nMuons, nTaus, nPhotons;
    long int nTightElectrons, nTightMuons;
    long int nLooseElectrons, nLooseMuons, nTriggerMuons;
    long int number_of_PV;
    long int number_of_SV;
    long int nPFCandidates, nPFCandidatesTrack, nPFCandidatesHighPurityTrack, nPFCandidatesFullTrackInfo, nPFCandidatesFullTrackInfo_pt, nPFCandidatesFullTrackInfo_hasTrackDetails;
    float EventWeight;
    float EventWeight_leptonSF;
    float EventWeight_leptonSFUp;
    float EventWeight_leptonSFDown;
    float GenEventWeight;
    float PUWeight, PUWeightUp, PUWeightDown;
    float PUWeight_HLT_Mu7_IP4, PUWeightUp_HLT_Mu7_IP4, PUWeightDown_HLT_Mu7_IP4;
    float PUWeight_HLT_Mu9_IP6, PUWeightUp_HLT_Mu9_IP6, PUWeightDown_HLT_Mu9_IP6;
    float PUWeight_HLT_Mu12_IP6, PUWeightUp_HLT_Mu12_IP6, PUWeightDown_HLT_Mu12_IP6;
    float PUWeight_HLT_Mu9_IP6_v6, PUWeightUp_HLT_Mu9_IP6_v6, PUWeightDown_HLT_Mu9_IP6_v6;
    float FacWeightUp, FacWeightDown, RenWeightUp, RenWeightDown, CorrWeightUp, CorrWeightDown;
    float PdfWeight;
    float LeptonWeight, LeptonWeightUp, LeptonWeightDown;
    float bTagWeight_central, bTagWeight_jesup, bTagWeight_jesdown, bTagWeight_lfup, bTagWeight_lfdown, bTagWeight_hfup, bTagWeight_hfdown, bTagWeight_hfstats1up, bTagWeight_hfstats1down, bTagWeight_hfstats2up, bTagWeight_hfstats2down, bTagWeight_lfstats1up, bTagWeight_lfstats1down, bTagWeight_lfstats2up, bTagWeight_lfstats2down, bTagWeight_cferr1up, bTagWeight_cferr1down, bTagWeight_cferr2up, bTagWeight_cferr2down;
    float ZewkWeight, WewkWeight;
    float HT;
    float MinJetMetDPhi;
    float MinJetMetDPhiAllJets;
    float ggHJetMetDPhi;
    float m_pi, gen_b_radius;
    //MET filters
    bool BadPFMuonFlag, BadChCandFlag, ECALCalibFlag;
    //Pre-firing
    bool Prefired;
    //VBF tagging
    //bool isVBF;
    bool isTriggerVBF;
    //Z-W-T CR
    bool isTightMM, isTightEE, isTightM, isTightE, isTightEM, isLooseEM;
    bool isOppositeSignTightMM, isOppositeSignTightEE;
    bool isZtoMM, isZtoEE, isWtoMN, isWtoEN, isTtoEM;
    AddFourMomenta addP4;
    //Displaced calo tagging
    long int nLooseCaloTagJets;
    long int nCaloTagJets;
    //Higgs reconstruction
    float HDiCHS, HTriCHS, HQuadCHS;
    float HDiCHSMatched, HTriCHSMatched, HQuadCHSMatched;
  //float HDiCalo, HTriCalo, HQuadCalo;
  //float HDiCaloMatched, HTriCaloMatched, HQuadCaloMatched;

    //Histograms
    //TH2F* jetMass_SVdisplacement2d;
    //TH2F* vertexMass_SVdisplacement2d;
    //TH2F* jetMass_SVdisplacement3d;
    //TH2F* vertexMass_SVdisplacement3d;
    //TH2F* jetMass_nVertexTracks;
    //TH2F* vertexMass_nVertexTracks;


    //Example to define an histogram:
    //TH1F* Matching_to_b_AK4Jets;

};

#endif
