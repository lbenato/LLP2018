#ifndef JETANALYZER_H
#define JETANALYZER_H

#include <iostream>
#include <fstream>

#include <cmath>
#include <numeric>
#include <map>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Common/interface/Association.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "RecoParticleFlow/PFProducer/interface/Utils.h"
#include "DataFormats/BTauReco/interface/SoftLeptonTagInfo.h"
#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "JetMETCorrections/JetCorrector/interface/JetCorrector.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "RecoilCorrector.h" // From: https://github.com/cms-met/MetTools/tree/master/RecoilCorrections
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"


#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "JetMETCorrections/Modules/interface/JetResolution.h"
#include <CondFormats/JetMETObjects/interface/JetResolutionObject.h>

#include "CondFormats/BTauObjects/interface/BTagCalibration.h"
#include "CondTools/BTau/interface/BTagCalibrationReader.h"

#include "DataFormats/Common/interface/Ptr.h"

#include "FWCore/Utilities/interface/transform.h"

//HCAL Rec Hits
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
#include "DataFormats/HcalDetId/interface/HcalDetId.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HORecHit.h"

//ECAL Rechits
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"
#include "DataFormats/EcalDetId/interface/EcalSubdetector.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHit.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"

//ECAL conditions
#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbService.h"
#include "CalibCalorimetry/EcalLaserCorrection/interface/EcalLaserDbRecord.h"

// Geometry
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"

#include "TFile.h"
#include "TH2.h"
#include "TF1.h"
#include "TLorentzVector.h"
#include "TRandom3.h"
#include "FWCore/Utilities/interface/TypeID.h"

#include "Objects.h"

class JetAnalyzer {
    public:
        JetAnalyzer(edm::ParameterSet&, edm::ConsumesCollector&&);
        ~JetAnalyzer();
        virtual std::vector<pat::Jet> FillJetVector(const edm::Event&, const edm::EventSetup&);
        virtual std::vector<ecalRecHitType> FillEcalRecHitVector(const edm::Event&, const edm::EventSetup&, std::vector<pat::Jet> &);
        virtual std::vector<hcalRecHitType> FillHcalRecHitVector(const edm::Event&, const edm::EventSetup&, std::vector<pat::Jet> &);
	virtual std::pair< std::pair<float,float> , float> JetSecondMoments(std::vector<double> &,std::vector<double> &,std::vector<double> &);
        //virtual void CorrectJet(pat::Jet&, float, float, bool);
        //virtual void CorrectMass(pat::Jet&, float, float, bool);
        //virtual void CorrectPuppiMass(pat::Jet&, bool);
        virtual void CleanJetsFromMuons(std::vector<pat::Jet>&, std::vector<pat::Muon>&, float);
        virtual void CleanJetsFromElectrons(std::vector<pat::Jet>&, std::vector<pat::Electron>&, float);
        virtual void CleanFatJetsFromAK4(std::vector<pat::Jet>&, std::vector<pat::Jet>&, float);
        virtual void AddVariables(std::vector<pat::Jet>&, pat::MET&);
        virtual void GenMatcher(std::vector<pat::Jet>&, std::vector<reco::GenParticle>&, std::string);
        virtual int GetNBJets(std::vector<pat::Jet>&);
        virtual pat::MET FillMetVector(const edm::Event&);
	virtual float GetMetTriggerEfficiency(pat::MET&);
        virtual void ApplyRecoilCorrections(pat::MET&, const reco::Candidate::LorentzVector*, const reco::Candidate::LorentzVector*, int);
        virtual float CalculateHT(const edm::Event&, const edm::EventSetup&, int, float, float, bool);
        virtual bool isLooseJet(pat::Jet&, std::string);
        virtual bool isTightJet(pat::Jet&, std::string);
        virtual bool isTightLepVetoJet(pat::Jet&, std::string);
	//        virtual std::vector<float> ReshapeBtagDiscriminator(pat::Jet&);
	virtual std::map<std::string, float> CalculateBtagReshapeSF(std::vector<pat::Jet>&);
      
    private:

        edm::EDGetTokenT<std::vector<pat::Jet> > JetToken;
        edm::EDGetTokenT<std::vector<pat::MET> > MetToken;
        edm::EDGetTokenT<edm::ValueMap<float>> QGToken;
        edm::EDGetTokenT<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > ebRecHitsToken;
        edm::EDGetTokenT<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > eeRecHitsToken;
        edm::EDGetTokenT<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > esRecHitsToken;
        edm::EDGetTokenT<edm::SortedCollection<HORecHit,edm::StrictWeakOrdering<HORecHit>>>       hcalRecHitsHOToken;
        edm::EDGetTokenT<edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit>>>       hcalRecHitsHBHEToken;
        int JetId;
	std::string DataEra;
        float Jet1Pt, Jet2Pt, JetEta;
        bool IsAOD;
        bool AddQG;
	//bool RecalibrateJets, RecalibrateMass, RecalibratePuppiMass; 
	std::string SoftdropPuppiMassString;
        bool SmearJets;
        std::string JECUncertaintyName;
	//obsolete methods
        //std::string JECUncertaintyMC;
        //std::string JECUncertaintyDATA;
        //std::vector<std::string> JetCorrectorMC;
        //std::vector<std::string> JetCorrectorDATA;
        //std::vector<std::string> MassCorrectorMC;
        //std::vector<std::string> MassCorrectorDATA;
        //std::string MassCorrectorPuppi;
        edm::EDGetTokenT<reco::VertexCollection> VertexToken;        
        edm::EDGetTokenT<double> RhoToken;
        bool UseReshape;
        std::string BTag;
        int Jet1BTag, Jet2BTag;
        std::string BTagDB;
        bool UseRecoil;
        std::string RecoilMCFile;
        std::string RecoilDataFile;
        std::string MetTriggerFileName;
        std::string JerName_res;
        std::string JerName_sf;
	std::vector<std::string> BTagNames;
        float Rparameter;
	float dRMatch;
        //Ecal RecHits
        const float Rechit_cut = 0.5;
        
        //TFile* PuppiCorrFile;
        //TF1* PuppiJECcorr_gen;
        //TF1* PuppiJECcorr_reco_0eta1v3;
        //TF1* PuppiJECcorr_reco_1v3eta2v5;

	TFile* MetTriggerFile;
	TH1F* MetTriggerHisto;
	bool isMetTriggerFile;

	//obsolete
        //// JEC Uncertainty
        //JetCorrectionUncertainty* jecUncMC;
        //JetCorrectionUncertainty* jecUncDATA;
        
        //boost::shared_ptr<FactorizedJetCorrector> jetCorrMC;
        //boost::shared_ptr<FactorizedJetCorrector> jetCorrDATA;
        //boost::shared_ptr<FactorizedJetCorrector> massCorrMC;
        //boost::shared_ptr<FactorizedJetCorrector> massCorrDATA;
        
        // Btag calibrations
        BTagCalibration        * calib;
	BTagCalibrationReader * reader;
	std::map < int , BTagEntry::JetFlavor > flavour_map; 
	std::map< BTagEntry::JetFlavor, std::vector<std::string>> syst_map; 
	std::map<std::string, BTagCalibrationReader> cr_map;
	std::string sf_mode;

	//	std::vector<edm::EDGetTokenT<edm::View<reco::BaseTagInfo> > > BTagInfos_;
        
        //JME
        //JME::JetResolution              * resolution;
        //JME::JetResolutionScaleFactor   * resolution_sf;        
        JME::JetResolution              resolution;
        JME::JetResolutionScaleFactor   resolution_sf; 
                
        // Recoil corrections
        RecoilCorrector* recoilCorr;
};

#endif
