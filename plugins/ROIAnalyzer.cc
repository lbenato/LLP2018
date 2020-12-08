#include "ROIAnalyzer.h"


ROIAnalyzer::ROIAnalyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
  lostTracksToken(CColl.consumes<edm::View<PackedCandidate> >(PSet.getParameter<edm::InputTag>("lostTracks"))),
  packedPFCandidatesToken(CColl.consumes<edm::View<PackedCandidate> >(PSet.getParameter<edm::InputTag>("packedPFCandidates"))),
  trackClustersToken(CColl.consumes<edm::View<VertexCompositeCandidate> >(PSet.getParameter<edm::InputTag>("trackClusters"))),
  regionsOfInterestToken(CColl.consumes<edm::View<PseudoROI> >(PSet.getParameter<edm::InputTag>("regionsOfInterest")))
{
  std::cout << " --- ROIAnalyzer initialization ---" << std::endl;
  std::cout << std::endl;
}

ROIAnalyzer::~ROIAnalyzer() {

}


// ---------- LostTracks ----------
std::vector<LostTrack> ROIAnalyzer::FillLostTrackVector(const edm::Event& iEvent, unsigned nPVs) {
  edm::Handle<edm::View<PackedCandidate> > lostTrackCollection;
  iEvent.getByToken(lostTracksToken, lostTrackCollection);
  std::vector<LostTrack> Vect;
  for (const auto &lostTrack : *lostTrackCollection) {
    if (!lostTrack.hasTrackDetails())
      continue;
    Vect.emplace_back(lostTrack, nPVs);
  }
  return Vect;
}

// ---------- PFCandidates ----------
std::vector<PackedPFCandidate> ROIAnalyzer::FillPFCandidateVector(const edm::Event& iEvent, unsigned nPVs) {
  edm::Handle<edm::View<PackedCandidate> > packedPFCandidateCollection;
  iEvent.getByToken(packedPFCandidatesToken, packedPFCandidateCollection);
  std::vector<PackedPFCandidate> Vect;
  for (const auto &packedPFCandidate : *packedPFCandidateCollection) {
    if (packedPFCandidate.charge() && !packedPFCandidate.hasTrackDetails())
      continue;
    Vect.emplace_back(packedPFCandidate, nPVs);
  }
  return Vect;
}

// ---------- TrackClusters ----------
std::vector<TrackCluster> ROIAnalyzer::FillTrackClusterVector(const edm::Event& iEvent) {
  edm::Handle<edm::View<VertexCompositeCandidate> > trackClusterCollection;
  iEvent.getByToken(trackClustersToken, trackClusterCollection);
  std::vector<TrackCluster> Vect;
  for (const auto &trackCluster : *trackClusterCollection) {
    Vect.emplace_back(trackCluster);
  }
  return Vect;
}

// ---------- RegionsOfInterest ----------
std::vector<RegionOfInterest> ROIAnalyzer::FillROIVector(const edm::Event& iEvent) {
  edm::Handle<edm::View<PseudoROI> > regionOfInterestCollection;
  iEvent.getByToken(regionsOfInterestToken, regionOfInterestCollection);
  std::vector<RegionOfInterest> Vect;
  for (const auto &regionOfInterest : *regionOfInterestCollection) {
    Vect.emplace_back(regionOfInterest);
  }
  return Vect;
}
