#include "StandAloneMuonsAnalyzer.h"


StandAloneMuonsAnalyzer::StandAloneMuonsAnalyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
  StandAloneMuonsToken(CColl.consumes<reco::TrackCollection>(PSet.getParameter<edm::InputTag>("standaloneMuons"))),
  StandAloneMuonsViewToken(CColl.consumes< edm::View<reco::Track> >(PSet.getParameter<edm::InputTag>("standaloneMuons")))

{
    
    std::cout << " --- StandAloneMuonsAnalyzer initialization ---" << std::endl;

    // std::cout << "  sample            :\t" << Sample << std::endl;
    // if(ApplyEWK) std::cout << "  EWK file          :\t" << EWKFileName << std::endl;
    std::cout << std::endl;
}

StandAloneMuonsAnalyzer::~StandAloneMuonsAnalyzer() {

}



std::vector<reco::Track> StandAloneMuonsAnalyzer::FillStandAloneMuonsVector(const edm::Event& iEvent) {
    
    std::vector<reco::Track> Vect;
    
    // Declare and open collections
    edm::Handle<reco::TrackCollection> StandAloneMuonsCollection;
    iEvent.getByToken(StandAloneMuonsToken, StandAloneMuonsCollection); 
    
    // Iterate over StandAloneMuonsCollection and save in vect     
    for (reco::TrackCollection::const_iterator track_it = StandAloneMuonsCollection->begin(); track_it != StandAloneMuonsCollection->end();track_it++) {
        reco::Track standalonemuon = *track_it;
	//std::cout << "Standalone muon quality: " << standalonemuon.theta() << std::endl;
        Vect.push_back(standalonemuon);
        
    }
    
    
    return Vect;
}

std::vector<TLorentzVector> StandAloneMuonsAnalyzer::FillStandAloneMuonsPropagatedVector(const edm::Event& iEvent, const edm::EventSetup& iSetup) {    

    const MagneticField* MagneticFieldTag;
    edm::ESHandle<Propagator> PropagatorHandle;
    edm::ESHandle<TransientTrackBuilder> BuilderHandle;
    // Magnetic field
    edm::ESHandle<MagneticField> MagneticField;
    iSetup.get<IdealMagneticFieldRecord>().get(MagneticField);
    MagneticFieldTag = &*MagneticField;
    // Propagator
    std::string PropagatorName = "PropagatorWithMaterial";
    iSetup.get<TrackingComponentsRecord>().get(PropagatorName,PropagatorHandle);
    StateOnTrackerBound stateOnTracker(PropagatorHandle.product());

    // Declare and open collections
    edm::Handle<reco::TrackCollection> StandAloneMuonsCollection;
    iEvent.getByToken(StandAloneMuonsToken, StandAloneMuonsCollection); 
    edm::Handle<edm::View<reco::Track> > StandAloneMuonsView;
    iEvent.getByToken(StandAloneMuonsViewToken,StandAloneMuonsView);

    std::vector<TLorentzVector> Vect;
    // Iterate over StandAloneMuonsCollection and save in vect     
    for (unsigned int track_it = 0; track_it < StandAloneMuonsCollection->size(); track_it ++){
	//Track propagation
	FreeTrajectoryState fts = trajectoryStateTransform::initialFreeState (StandAloneMuonsView->at(track_it),MagneticFieldTag);
	TrajectoryStateOnSurface outer = stateOnTracker(fts);
	//std::cout << "doing track propagation, check if valid : " << outer.isValid() << std::endl;
        if(!outer.isValid()) continue;
        GlobalPoint outerPos = outer.globalPosition();
        TLorentzVector trackTemp;
        trackTemp.SetPtEtaPhiM( (StandAloneMuonsCollection->at(track_it)) .pt(), outerPos.eta(), outerPos.phi(), 0);
	Vect.push_back(trackTemp);
    }
    return Vect;
}


std::map<std::string,float> StandAloneMuonsAnalyzer::GenMatcherStandAloneMuons(std::vector<reco::Track>& StandAloneMuon, std::vector<reco::GenParticle>& Quarks, std::string label) {
    std::map<std::string,float> match_map;
    
     for(unsigned int j = 0; j < StandAloneMuon.size(); j++) {
        for(unsigned int q = 0; q < Quarks.size(); q++) {
	  match_map.insert(std::make_pair(("dR_j"+std::to_string(j+1)+label+std::to_string(q+1)).c_str(), fabs(reco::deltaR(StandAloneMuon[j].eta(),StandAloneMuon[j].phi(),Quarks[q].eta(),Quarks[q].phi())) ));
        }
    }
    return match_map;
    
}



