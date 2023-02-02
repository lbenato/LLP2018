// -*- C++ -*-
//
// Package:    Cosmics/CosmicsAnalyzer
// Class:      CosmicsAnalyzer
//
/**\class CosmicsAnalyzer CosmicsAnalyzer.cc Cosmics/CosmicsAnalyzer/plugins/CosmicsAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Lisa Benato
//         Created:  Sun, 23 Jan 2022 11:17:12 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
#include "DataFormats/DTRecHit/interface/DTRecClusterCollection.h"
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "Geometry/DTGeometry/interface/DTChamber.h"
#include "Geometry/DTGeometry/interface/DTSuperLayer.h"
#include "Geometry/DTGeometry/interface/DTLayer.h"
#include "Geometry/DTGeometry/interface/DTTopology.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCSegmentCollection.h"
#include "Geometry/CSCGeometry/interface/CSCGeometry.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"
#include "Geometry/Records/interface/DTRecoGeometryRcd.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
//#include "Geometry/Records/interface/MuonGeometryRecord.h"
//#include "Geometry/Records/interface/MuonGeometryRcd.h"
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

#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/CaloMETFwd.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "TTree.h"
#include <string>

#include "RecoObjects.h"
#include "RecoObjectsFormat.h"
#include "Objects.h"
#include "ObjectsFormat.h"
//#include "DTAnalyzer.h"
//#include "CSCAnalyzer.h"
//#include "StandAloneMuonsAnalyzer.h"
//#include "JetAnalyzer.h"



//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.


//using reco::TrackCollection;

class CosmicsAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit CosmicsAnalyzer(const edm::ParameterSet&);
      ~CosmicsAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::EDGetTokenT< std::vector<reco::CaloJet> > caloJetsToken_;
      edm::EDGetTokenT< std::vector<reco::CaloMET> > caloMetToken_;
      edm::EDGetTokenT< edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> >  > ecalRecHitsEBToken_;
      edm::EDGetTokenT<DTRecSegment4DCollection> dtSegmentsToken_;
      edm::EDGetTokenT<CSCSegmentCollection> cscSegmentsToken_;
      edm::EDGetTokenT<std::vector<reco::Track> > cosmicMuonsToken_;
      edm::EDGetTokenT<std::vector<reco::Track> > cosmicMuonsOneLegToken_;
      edm::EDGetTokenT<std::vector<reco::Track> > globalCosmicMuonsToken_;
      edm::EDGetTokenT<std::vector<reco::Track> > globalCosmicMuonsOneLegToken_;

  std::vector<DT4DSegmentType> DTSegmentsStruct;
  std::vector<CSCSegmentType> CSCSegmentsStruct;
  std::vector<CaloJetType> CaloJets;
  CaloMEtType CaloMEt;
  std::vector<ecalRecHitType> EcalRecHitsAK4;
  std::vector<TrackType> CosmicMuons;
  std::vector<TrackType> CosmicMuonsOneLeg;
  std::vector<TrackType> GlobalCosmicMuons;
  std::vector<TrackType> GlobalCosmicMuonsOneLeg;

  const float Rechit_cut = 0.5;
  long int EventNumber, LumiNumber, RunNumber;
  long int nCaloJets;
  long int nDTSegments;
  long int nCSCSegments;
  long int nCosmicMuons, nCosmicMuonsOneLeg;
  long int nGlobalCosmicMuons, nGlobalCosmicMuonsOneLeg;

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
CosmicsAnalyzer::CosmicsAnalyzer(const edm::ParameterSet& iConfig)
 :
  caloJetsToken_(consumes<std::vector<reco::CaloJet> >(iConfig.getUntrackedParameter<edm::InputTag>("caloJets"))),
  caloMetToken_(consumes<std::vector<reco::CaloMET> >(iConfig.getUntrackedParameter<edm::InputTag>("caloMet"))),
  ecalRecHitsEBToken_(consumes<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > >(iConfig.getUntrackedParameter<edm::InputTag>("ecalRecHitsEB"))),
  dtSegmentsToken_(consumes<DTRecSegment4DCollection>(iConfig.getUntrackedParameter<edm::InputTag>("dtSegments"))),
  cscSegmentsToken_(consumes<CSCSegmentCollection>(iConfig.getUntrackedParameter<edm::InputTag>("cscSegments"))),
  cosmicMuonsToken_(consumes<std::vector<reco::Track> >(iConfig.getUntrackedParameter<edm::InputTag>("cosmicMuons"))),
  cosmicMuonsOneLegToken_(consumes<std::vector<reco::Track> >(iConfig.getUntrackedParameter<edm::InputTag>("cosmicMuonsOneLeg"))),
  globalCosmicMuonsToken_(consumes<std::vector<reco::Track> >(iConfig.getUntrackedParameter<edm::InputTag>("globalCosmicMuons"))),
  globalCosmicMuonsOneLegToken_(consumes<std::vector<reco::Track> >(iConfig.getUntrackedParameter<edm::InputTag>("globalCosmicMuonsOneLeg")))

{
   //now do what ever initialization is needed
  usesResource("TFileService");

}


CosmicsAnalyzer::~CosmicsAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
CosmicsAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   EventNumber = LumiNumber = RunNumber = 0;
   nDTSegments = nCSCSegments = 0;
   nCosmicMuons = nCosmicMuonsOneLeg = 0;
   nGlobalCosmicMuons = nGlobalCosmicMuonsOneLeg = 0;
   nCaloJets = 0;

   EventNumber = iEvent.id().event();
   LumiNumber = iEvent.luminosityBlock();
   RunNumber = iEvent.id().run();

   Handle<std::vector<reco::CaloJet>> caloJets;
   iEvent.getByToken(caloJetsToken_, caloJets);
   Handle<std::vector<reco::CaloMET>> caloMet;
   iEvent.getByToken(caloMetToken_, caloMet);
   reco::CaloMET MET = caloMet->front();
   Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> >> ecalRecHitsEB;
   iEvent.getByToken(ecalRecHitsEBToken_, ecalRecHitsEB);
   Handle<DTRecSegment4DCollection> dtSegments;
   iEvent.getByToken(dtSegmentsToken_, dtSegments);
   Handle<CSCSegmentCollection> cscSegments;
   iEvent.getByToken(cscSegmentsToken_, cscSegments);
   Handle< std::vector<reco::Track> > cosmicMuons;
   iEvent.getByToken(cosmicMuonsToken_, cosmicMuons);
   Handle< std::vector<reco::Track> > cosmicMuonsOneLeg;
   iEvent.getByToken(cosmicMuonsOneLegToken_, cosmicMuonsOneLeg);
   Handle< std::vector<reco::Track> > globalCosmicMuons;
   iEvent.getByToken(globalCosmicMuonsToken_, globalCosmicMuons);
   Handle< std::vector<reco::Track> > globalCosmicMuonsOneLeg;
   iEvent.getByToken(globalCosmicMuonsOneLegToken_, globalCosmicMuonsOneLeg);

   //MET
   ObjectsFormat::FillCaloMEtType(CaloMEt, &MET, false);

   //CaloJets
   std::vector<reco::CaloJet> CaloJetsVect;
   for (reco::CaloJetCollection::const_iterator jet_it = caloJets->begin(); jet_it != caloJets->end();jet_it++)
     {
       reco::CaloJet jet = *jet_it;
       if(fabs(jet.eta())<1.4 and jet.pt()>20)
	 {
	   CaloJetsVect.push_back(jet);
	 }
     }
   nCaloJets = CaloJetsVect.size();
   if(nCaloJets<1) return;

   

   for(unsigned int i =0; i< CaloJetsVect.size();i++) CaloJets.push_back(CaloJetType());
   //Fill CaloJets when looping over eb rec hits
   //for(unsigned int i =0; i< CaloJetsVect.size();i++) ObjectsFormat::FillCaloJetType(CaloJets[i],&CaloJetsVect[i],false,false,-1.,-999.,0,-1.,-1.,-1.);

   //ECAL Rec hits
   float dRMatch = 0.4;
   edm::ESHandle<CaloGeometry> geoHandle;
   iSetup.get<CaloGeometryRecord>().get(geoHandle);
   const CaloSubdetectorGeometry *barrelGeometry = geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalBarrel);

   for(unsigned int a = 0; a<CaloJetsVect.size(); a++)
     {
       //EB variables
       float jetRechitE_EB(0.);
       float jetRechitT_EB(0.);
       float jetRechitT_rms_EB(0.);
       int n_matched_rechits_EB(0);
       for(unsigned int q=0; q<ecalRecHitsEB->size(); q++)
	 {

	   const EcalRecHit *recHit = &(*ecalRecHitsEB)[q];
	   const DetId recHitId = recHit->detid();
	   const auto recHitPos = barrelGeometry->getGeometry(recHitId)->getPosition();
	   ecalRecHitType recHitStruct;
	   if (recHit->checkFlag(EcalRecHit::kSaturated) || recHit->checkFlag(EcalRecHit::kLeadingEdgeRecovered) || recHit->checkFlag(EcalRecHit::kPoorReco) || recHit->checkFlag(EcalRecHit::kWeird) || recHit->checkFlag(EcalRecHit::kDiWeird)) continue;
	   //if (recHit->timeError() < 0 || recHit->timeError() > 100) continue;
	   if (abs(recHit->time()) > 12.5) continue;

	   if (reco::deltaR(CaloJetsVect.at(a).eta(), CaloJetsVect.at(a).phi(), recHitPos.eta(), recHitPos.phi()) < dRMatch)
	     {
	       if(recHit->energy() > Rechit_cut)
		 {
		   recHitStruct.eta = recHitPos.eta();
		   recHitStruct.phi = recHitPos.phi();
		   recHitStruct.x = recHitPos.x();
		   recHitStruct.y = recHitPos.y();
		   recHitStruct.z = recHitPos.z();
		   recHitStruct.energy = recHit->energy();
		   recHitStruct.time = recHit->time();
		   recHitStruct.energyError = recHit->energyError();
		   recHitStruct.timeError = recHit->timeError();
		   recHitStruct.jetPt = CaloJetsVect.at(a).pt();
		   recHitStruct.jetIndex = a;
		   recHitStruct.jetDR = reco::deltaR(CaloJetsVect.at(a).eta(), CaloJetsVect.at(a).phi(), recHitPos.eta(), recHitPos.phi());
		   EcalRecHitsAK4.push_back(recHitStruct);
		   
		   //Here: assign this to calo jet
		   jetRechitE_EB += recHit->energy();
		   jetRechitT_EB += recHit->time()*recHit->energy();
		   jetRechitT_rms_EB += recHit->time()*recHit->time();
		   n_matched_rechits_EB++;
		 }//if matched ecal rec hits
	     }//loop on ecal rec hits
	 }//loop on ecal rec hits

       ObjectsFormat::FillCaloJetType(CaloJets[a],&CaloJetsVect[a],false,false,-1.,-999.,n_matched_rechits_EB,jetRechitE_EB>0?jetRechitT_EB/jetRechitE_EB:-100.,sqrt(jetRechitT_rms_EB),jetRechitE_EB);

     }//loop on jets


   //DT segments
   edm::ESHandle<DTGeometry> dtG;
   iSetup.get<MuonGeometryRecord>().get(dtG);
   std::vector<DTRecSegment4D> DTSegmentVect;
   for (DTRecSegment4DCollection::const_iterator dt_it = dtSegments->begin(); dt_it != dtSegments->end();dt_it++)
     {
       DTRecSegment4D segment = *dt_it;
       DTSegmentVect.push_back(segment);
     }
   nDTSegments = DTSegmentVect.size();
   for(unsigned int i =0; i< DTSegmentVect.size();i++) DTSegmentsStruct.push_back(DT4DSegmentType());
   for(unsigned int i =0; i< DTSegmentVect.size();i++) ObjectsFormat::FillDT4DSegmentType(DTSegmentsStruct[i], &DTSegmentVect[i],dtG);

   //CSC Segments
   edm::ESHandle<CSCGeometry> cscG;
   iSetup.get<MuonGeometryRecord>().get(cscG);
   std::vector<CSCSegment> CSCSegmentVect;
   for (CSCSegmentCollection::const_iterator csc_it = cscSegments->begin(); csc_it != cscSegments->end();csc_it++)
     {
       CSCSegment segment = *csc_it;
       CSCSegmentVect.push_back(segment);
     }
   nCSCSegments = CSCSegmentVect.size();
   for(unsigned int i =0; i< CSCSegmentVect.size();i++) CSCSegmentsStruct.push_back(CSCSegmentType());
   for(unsigned int i =0; i< CSCSegmentVect.size();i++) ObjectsFormat::FillCSCSegmentType(CSCSegmentsStruct[i], &CSCSegmentVect[i],cscG);

   //CosmicMuons
   std::vector<reco::Track> CosmicMuonsVect;
   for(reco::TrackCollection::const_iterator track_it = cosmicMuons->begin(); track_it != cosmicMuons->end();track_it++) {
     reco::Track standalonemuon = *track_it;
     CosmicMuonsVect.push_back(standalonemuon);
   }
   nCosmicMuons = CosmicMuonsVect.size();
   for(unsigned int i =0; i< CosmicMuonsVect.size();i++) CosmicMuons.push_back(TrackType());
   for(unsigned int i =0; i< CosmicMuonsVect.size();i++) ObjectsFormat::FillTrackType(CosmicMuons[i], &CosmicMuonsVect[i]);

   std::vector<reco::Track> CosmicMuonsOneLegVect;
   for(reco::TrackCollection::const_iterator track_it = cosmicMuonsOneLeg->begin(); track_it != cosmicMuonsOneLeg->end();track_it++) {
     reco::Track standalonemuon = *track_it;
     CosmicMuonsOneLegVect.push_back(standalonemuon);
   }
   nCosmicMuonsOneLeg = CosmicMuonsOneLegVect.size();
   for(unsigned int i =0; i< CosmicMuonsOneLegVect.size();i++) CosmicMuonsOneLeg.push_back(TrackType());
   for(unsigned int i =0; i< CosmicMuonsOneLegVect.size();i++) ObjectsFormat::FillTrackType(CosmicMuonsOneLeg[i], &CosmicMuonsOneLegVect[i]);

   std::vector<reco::Track> GlobalCosmicMuonsVect;
   for(reco::TrackCollection::const_iterator track_it = globalCosmicMuons->begin(); track_it != globalCosmicMuons->end();track_it++) {
     reco::Track standalonemuon = *track_it;
     GlobalCosmicMuonsVect.push_back(standalonemuon);
   }
   nGlobalCosmicMuons = GlobalCosmicMuonsVect.size();
   for(unsigned int i =0; i< GlobalCosmicMuonsVect.size();i++) GlobalCosmicMuons.push_back(TrackType());
   for(unsigned int i =0; i< GlobalCosmicMuonsVect.size();i++) ObjectsFormat::FillTrackType(GlobalCosmicMuons[i], &GlobalCosmicMuonsVect[i]);

   std::vector<reco::Track> GlobalCosmicMuonsOneLegVect;
   for(reco::TrackCollection::const_iterator track_it = globalCosmicMuonsOneLeg->begin(); track_it != globalCosmicMuonsOneLeg->end();track_it++) {
     reco::Track standalonemuon = *track_it;
     GlobalCosmicMuonsOneLegVect.push_back(standalonemuon);
   }
   nGlobalCosmicMuonsOneLeg = GlobalCosmicMuonsOneLegVect.size();
   for(unsigned int i =0; i< GlobalCosmicMuonsOneLegVect.size();i++) GlobalCosmicMuonsOneLeg.push_back(TrackType());
   for(unsigned int i =0; i< GlobalCosmicMuonsOneLegVect.size();i++) ObjectsFormat::FillTrackType(GlobalCosmicMuonsOneLeg[i], &GlobalCosmicMuonsOneLegVect[i]);

   tree -> Fill();

   DTSegmentsStruct.clear();
   CSCSegmentsStruct.clear();
   CaloJets.clear();
   EcalRecHitsAK4.clear();
   CosmicMuons.clear();
   CosmicMuonsOneLeg.clear();
   GlobalCosmicMuons.clear();
   GlobalCosmicMuonsOneLeg.clear();


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
CosmicsAnalyzer::beginJob()
{
  tree = fs->make<TTree>("tree", "tree");
  tree -> Branch("EventNumber" , &EventNumber , "EventNumber/L");
  tree -> Branch("LumiNumber" , &LumiNumber , "LumiNumber/L");
  tree -> Branch("RunNumber" , &RunNumber , "RunNumber/L");
  tree -> Branch("nCaloJets", &nCaloJets, "nCaloJets/L");
  tree -> Branch("nDTSegments", &nDTSegments, "nDTSegments/L");
  tree -> Branch("nCSCSegments", &nCSCSegments, "nCSCSegments/L");
  tree -> Branch("nCosmicMuons", &nCosmicMuons, "nCosmicMuons/L");
  tree -> Branch("nCosmicMuonsOneLeg", &nCosmicMuonsOneLeg, "nCosmicMuonsOneLeg/L");
  tree -> Branch("nGlobalCosmicMuons", &nGlobalCosmicMuons, "nGlobalCosmicMuons/L");
  tree -> Branch("nGlobalCosmicMuonsOneLeg", &nGlobalCosmicMuonsOneLeg, "nGlobalCosmicMuonsOneLeg/L");

  tree -> Branch("CaloMEt", &CaloMEt);
  tree -> Branch("CaloJets", &CaloJets);
  tree -> Branch("EcalRecHitsAK4", &EcalRecHitsAK4);
  tree -> Branch("DTSegments", &DTSegmentsStruct);
  tree -> Branch("CSCSegments", &CSCSegmentsStruct);
  tree -> Branch("CosmicMuons", &CosmicMuons);
  tree -> Branch("CosmicMuonsOneLeg", &CosmicMuonsOneLeg);
  tree -> Branch("GlobalCosmicMuons", &GlobalCosmicMuons);
  tree -> Branch("GlobalCosmicMuonsOneLeg", &GlobalCosmicMuonsOneLeg);

}

// ------------ method called once each job just after ending the event loop  ------------
void
CosmicsAnalyzer::endJob()
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CosmicsAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CosmicsAnalyzer);
