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

#ifndef TRIGGERSTUDIES_H
#define TRIGGERSTUDIES_H

// system include files
#include <memory>

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

#include "CommonTools/CandUtils/interface/AddFourMomenta.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TTree.h"
#include <string>
#include "JetAnalyzer.h"
#include "GenAnalyzer.h"
#include "PileupAnalyzer.h"
#include "TriggerAnalyzer.h"
#include "ElectronAnalyzer.h"
#include "MuonAnalyzer.h"
#include "TauAnalyzer.h"
#include "PhotonAnalyzer.h"
#include "VertexAnalyzer.h"
#include "PFCandidateAnalyzer.h"
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

class TriggerStudies : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit TriggerStudies(const edm::ParameterSet&);
      ~TriggerStudies();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
    edm::ParameterSet GenPSet;
    edm::ParameterSet PileupPSet;
    edm::ParameterSet TriggerPSet;
    edm::ParameterSet JetPSet;
  //    edm::ParameterSet VBFJetPSet;//VBF tagging
    edm::ParameterSet CHSFatJetPSet;
    edm::ParameterSet ElectronPSet;
    edm::ParameterSet MuonPSet;
    edm::ParameterSet TauPSet;
    edm::ParameterSet PhotonPSet;
    edm::ParameterSet VertexPSet;
    edm::ParameterSet PFCandidatePSet;

    JetAnalyzer* theJetAnalyzer;
  //    JetAnalyzer* theVBFJetAnalyzer;//VBF tagging
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

    double MinGenBpt, MaxGenBeta;
    double InvmassVBF, DetaVBF;//VBF tagging
    //int WriteNJets, WriteNFatJets;//unused, we have vectors now
    int WriteNGenBquarks, WriteNGenLongLiveds, WriteNMatchedJets;
    int WriteNLeptons;
    bool WriteOnlyTriggerEvents, WriteOnlyL1FilterEvents, WriteOnlyisVBFEvents;
    bool WriteFatJets;
    bool WriteJetPFCandidates;
    bool WriteAllPFCandidates;
    bool WriteLostTracks;
    bool WriteVertices;
    bool PerformPreFiringStudies;

    //L1 bits information; thanks to dijet scouting team
    //https://github.com/CMSDIJET/DijetScoutingRootTreeMaker/blob/master/plugins/DijetCaloScoutingTreeProducer.h
    edm::EDGetToken algToken_;
    l1t::L1TGlobalUtil *l1GtUtils_;
    std::vector<std::string> l1Seeds_;
    std::map<std::string, bool> L1BitsMap;
    std::vector<bool> *l1Result_;
    //bool bit_L1_TripleJet_84_68_48_VBF, bit_L1_TripleJet_88_72_56_VBF, bit_L1_TripleJet_92_76_64_VBF, bit_L1_HTT300;


  //std::vector<JetType> MatchedJets;
    std::vector<JetType> Jets;
    std::vector<TriggerObjectType> TriggerObjects;
    std::vector<JetType> DisplacedJets;
    std::vector<JetType> VBFPairJets;
    std::vector<JetType> SelectedVBFJets;
    std::vector<JetType> SelectedDisplacedJet;
  //std::vector<TriggerObjectType> TriggerVBFPairJets;
  //std::vector<TriggerObjectType> TriggerDisplacedJets;
  ////std::vector<FatJetType> CHSFatJets;
  ////std::vector<GenPType> GenBquarks;
  ////std::vector<GenPType> GenLongLiveds;
  ////std::vector<VertexType> PrimVertices;
  ////std::vector<VertexType> SecVertices;
  ////std::vector<VertexType> SecVerticesVert;
    //std::vector<LeptonType> Leptons;
    std::vector<LeptonType> Muons;
    std::vector<LeptonType> Electrons;
    //Jet const vector
    //std::vector<PFCandidateType> PFCandidates;
    //std::vector<PFCandidateType> LostTracks;

    MEtType MEt;
    CandidateType VBF;//VBF tagging
    CandidateType TriggerVBF;
  //CandidateType Z, W;//Z, W CR

    std::map<std::string, bool> TriggerMap;
    std::map<std::string, int> PrescalesTriggerMap;
    std::map<std::string, bool> MetFiltersMap;
    std::map<std::string, bool> L1FiltersMap;

    //Initialize tree
    edm::Service<TFileService> fs;
    TTree* tree;

    bool isVerbose, isVerboseTrigger, isSignal;
    bool isMC;
    long int EventNumber, LumiNumber, RunNumber, nPV, nSV;
    bool AtLeastOneTrigger, AtLeastOneL1Filter;
    long int nLooseJets, nTightJets, nJets, nVBFPairJets;
    long int nTriggerObjects, nTriggerVBFPairJets;
    long int nLooseCHSFatJets, nTightCHSFatJets, nCHSFatJets, nGenBquarks, nGenLL; 
    long int nMatchedJets;
    long int nSelectedDisplacedJet, nSelectedVBFJets;
    long int nDisplaced;
    long int number_of_b_matched_to_Jets;
    long int nElectrons, nMuons, nTaus, nPhotons;
    long int nTightElectrons, nTightMuons;
    long int number_of_PV;
    long int number_of_SV;
    long int nTriggerObjectsTripleJet50;
    long int nTriggerObjectsTripleJet50WithDuplicates;
    float EventWeight;
    float PUWeight, PUWeightUp, PUWeightDown;
    float FacWeightUp, FacWeightDown, RenWeightUp, RenWeightDown, CorrWeightUp, CorrWeightDown;
    float PdfWeight;
    float LeptonWeight;
    float ZewkWeight, WewkWeight;
    float HT;
    float MinJetMetDPhi;
    //MET filters
    bool BadPFMuonFlag, BadChCandFlag;
    //Pre-firing
    bool Prefired;
    //VBF tagging
    bool isVBF, isTriggerVBF;
    //Z-W-T CR
    bool isZtoMM, isZtoEE, isWtoMN, isWtoEN, isTtoEM;
    AddFourMomenta addP4;
    //Displaced calo tagging
    long int nLooseCaloTagJets;
    long int nCaloTagJets;

    float muon1_pt, muon1_eta, muon1_phi;
    float met_pt_nomu;

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
