#include "ROIAnalyzer.h"


ROIAnalyzer::ROIAnalyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
  verticesToken(CColl.consumes<edm::View<reco::Vertex> >(PSet.getParameter<edm::InputTag>("vertices"))),
  lostTracksToken(CColl.consumes<edm::View<PackedCandidate> >(PSet.getParameter<edm::InputTag>("lostTracks"))),
  packedPFCandidatesToken(CColl.consumes<edm::View<PackedCandidate> >(PSet.getParameter<edm::InputTag>("packedPFCandidates"))),
  trackClustersToken(CColl.consumes<edm::View<VertexCompositeCandidate> >(PSet.getParameter<edm::InputTag>("trackClusters"))),
  regionsOfInterestToken(CColl.consumes<edm::View<PseudoROI> >(PSet.getParameter<edm::InputTag>("regionsOfInterest")))
{
  //TODO: Make configurable!!!
  std::string baseDir(getenv("CMSSW_BASE"));
  model = baseDir + "/src/HiggsLongLived/DeepSets/data/WTopHalfMixedTest_Phi-64-128-256_32-64-128_F-256-128-32_Dropout-0.2_Model.pb";

  std::cout << " --- ROIAnalyzer initialization ---" << std::endl;
  std::cout << " Using model: " << std::endl;
  std::cout << model << std::endl;
  std::cout << std::endl;

  tensorflow::GraphDef *trainedModel = tensorflow::loadGraphDef(model);
  tfsession = tensorflow::createSession(trainedModel);
}

ROIAnalyzer::~ROIAnalyzer() {
  tensorflow::closeSession(tfsession);
  // delete trainedModel;
  // delete tfsession;
}

// ---------- Vertices ----------
// std::vector<Vertex> ROIAnalyzer::SetVertexVector(const edm::Event& iEvent) {
void ROIAnalyzer::SetVertexVector(const edm::Event& iEvent) {
  edm::Handle<edm::View<reco::Vertex> > vertexCollection;
  iEvent.getByToken(verticesToken, vertexCollection);

  // std::vector<Vertex> Vect;
  // for (const auto &vertex : *vertexCollection) {
  //   Vect.emplace_back(vertex);
  // }
  // return Vect;

  Vertices.clear();
  for (const auto &vertex : *vertexCollection) {
    Vertices.emplace_back(vertex);
  }

}

// ---------- LostTracks ----------
// std::vector<LostTrack> ROIAnalyzer::SetLostTrackVector(const edm::Event& iEvent, unsigned nPVs) {
void ROIAnalyzer::SetLostTrackVector(const edm::Event& iEvent, unsigned nPVs) {
  edm::Handle<edm::View<PackedCandidate> > lostTrackCollection;
  iEvent.getByToken(lostTracksToken, lostTrackCollection);

  // std::vector<LostTrack> Vect;
  // for (const auto &lostTrack : *lostTrackCollection) {
  //   if (!lostTrack.hasTrackDetails())
  //     continue;
  //   Vect.emplace_back(lostTrack, nPVs);
  // }
  // return Vect;

  LostTracks.clear();
  for (const auto &lostTrack : *lostTrackCollection) {
    if (!lostTrack.hasTrackDetails())
      continue;
    LostTracks.emplace_back(lostTrack, nPVs);
  }

}

// ---------- PFCandidates ----------
// std::vector<PackedPFCandidate> ROIAnalyzer::SetPFCandidateVector(const edm::Event& iEvent, unsigned nPVs) {
void ROIAnalyzer::SetPFCandidateVector(const edm::Event& iEvent, unsigned nPVs) {
  edm::Handle<edm::View<PackedCandidate> > packedPFCandidateCollection;
  iEvent.getByToken(packedPFCandidatesToken, packedPFCandidateCollection);

  // std::vector<PackedPFCandidate> Vect;
  // for (const auto &packedPFCandidate : *packedPFCandidateCollection) {
  //   if (packedPFCandidate.charge() && !packedPFCandidate.hasTrackDetails())
  //     continue;
  //   Vect.emplace_back(packedPFCandidate, nPVs);
  // }
  // return Vect;

  PFCandidates.clear();
  for (const auto &packedPFCandidate : *packedPFCandidateCollection) {
    if (packedPFCandidate.charge() && !packedPFCandidate.hasTrackDetails())
      continue;
    PFCandidates.emplace_back(packedPFCandidate, nPVs);
  }

}

// ---------- TrackClusters ----------
// std::vector<TrackCluster> ROIAnalyzer::SetTrackClusterVector(const edm::Event& iEvent) {
void ROIAnalyzer::SetTrackClusterVector(const edm::Event& iEvent) {
  edm::Handle<edm::View<VertexCompositeCandidate> > trackClusterCollection;
  iEvent.getByToken(trackClustersToken, trackClusterCollection);

  // std::vector<TrackCluster> Vect;
  // for (const auto &trackCluster : *trackClusterCollection) {
  //   Vect.emplace_back(trackCluster);
  // }
  // return Vect;

  TrackClusters.clear();
  for (const auto &trackCluster : *trackClusterCollection) {
    TrackClusters.emplace_back(trackCluster);
  }

}

// ---------- RegionsOfInterest ----------
// std::vector<RegionOfInterest> ROIAnalyzer::SetROIVector(const edm::Event& iEvent) {
void ROIAnalyzer::SetROIVector(const edm::Event& iEvent) {
  edm::Handle<edm::View<PseudoROI> > regionOfInterestCollection;
  iEvent.getByToken(regionsOfInterestToken, regionOfInterestCollection);

  // std::vector<RegionOfInterest> Vect;
  // for (const auto &regionOfInterest : *regionOfInterestCollection) {
  //   Vect.emplace_back(regionOfInterest);
  // }
  // return Vect;

  RegionsOfInterest.clear();
  for (const auto &regionOfInterest : *regionOfInterestCollection) {
    RegionsOfInterest.emplace_back(regionOfInterest);
  }

}

void ROIAnalyzer::SetAllTaggerInputVectors(const edm::Event& iEvent) {
  // Note: Done in each Set*Vector
  // Vertices.clear();
  // LostTracks.clear();
  // PFCandidates.clear();
  // TrackClusters.clear();
  // RegionsOfInterest.clear();

  // Note: Now void instead of returning object
  // Vertices = ROIAnalyzer::SetVertexVector(iEvent);
  // LostTracks = ROIAnalyzer::SetLostTrackVector(iEvent, Vertices.size());
  // PFCandidates = ROIAnalyzer::SetPFCandidateVector(iEvent, Vertices.size());
  // TrackClusters = ROIAnalyzer::SetTrackClusterVector(iEvent);
  // RegionsOfInterest = ROIAnalyzer::SetROIVector(iEvent);

  ROIAnalyzer::SetVertexVector(iEvent);
  ROIAnalyzer::SetLostTrackVector(iEvent, Vertices.size());
  ROIAnalyzer::SetPFCandidateVector(iEvent, Vertices.size());
  ROIAnalyzer::SetTrackClusterVector(iEvent);
  ROIAnalyzer::SetROIVector(iEvent);
}

std::vector<Vertex> ROIAnalyzer::GetVertexVector() {return Vertices;}

std::vector<LostTrack> ROIAnalyzer::GetLostTrackVector() {return LostTracks;}

std::vector<PackedPFCandidate> ROIAnalyzer::GetPFCandidateVector() {return PFCandidates;}

std::vector<TrackCluster> ROIAnalyzer::GetTrackClusterVector() {return TrackClusters;}

std::vector<RegionOfInterest> ROIAnalyzer::GetROIVector() {return RegionsOfInterest;}

void ROIAnalyzer::SetTaggerScores(const edm::Event& iEvent) { // TODO: Rename to include multiplicities
  // Clear quantities to be set
  TaggerScores.clear();
  TrackClusterMultiplicity.clear();
  AnnulusTrackMultiplicity.clear();
  LeadingROI = -1;
  LeadingScore = 1.0;

  // Make sure input objects are set
  if (RegionsOfInterest.size() < 1) SetAllTaggerInputVectors(iEvent);

  // TF input vectors
  std::vector<std::vector<float>> trackClusters = std::vector<std::vector<float>>(); //regionsOfInterest
  std::vector<std::vector<float>> tracks = std::vector<std::vector<float>>(); //annuliOfInterest
  std::vector<float> roiLevel = std::vector<float>(); //auxiliaryInfo

  // Loop over all ROI's and get TF input & score
  for (unsigned int thisROI = 0; thisROI < RegionsOfInterest.size(); thisROI++) {
    trackClusters.clear();
    tracks.clear();
    roiLevel.clear();

    AnalysisCommon::getTensorFlowInput(RegionsOfInterest.at(thisROI), Vertices.at(0), TrackClusters, PFCandidates, LostTracks, trackClusters, tracks, roiLevel);
    float thisScore = AnalysisCommon::runTensorFlowGraph(trackClusters, tracks, roiLevel, tfsession);
    TaggerScores.push_back(thisScore);
    TrackClusterMultiplicity.push_back(trackClusters.size());
    AnnulusTrackMultiplicity.push_back(tracks.size());

    if (thisScore < LeadingScore) {
      // SubleadingROI = LeadingROI;
      // SubleadingScore = LeadingScore;
      LeadingROI = thisROI;
      LeadingScore = thisScore;
    }

    // else if (thisScore >= SubleadingScore) {
    //   SubleadingROI = thisROI;
    //   SubleadingScore = thisScore;
    // }
  }

  if (LeadingROI != -1) {
    leadingROIPosition.SetXYZ(RegionsOfInterest.at(LeadingROI).vx(), RegionsOfInterest.at(LeadingROI).vy(), RegionsOfInterest.at(LeadingROI).vz());
    // LeadingPhi = leadingROIPosition.phi(); // Not needed. Done directly in FillROIType
  }

  // Not needed. LeadingScore not used anywhere else!
  // else {
  //   LeadingScore = -1.0;
  // }

}

std::vector<float> ROIAnalyzer::GetTaggerScores() {return TaggerScores;}

std::vector<int> ROIAnalyzer::GetTrackClusterMultiplicityVector() {return TrackClusterMultiplicity;}

std::vector<int> ROIAnalyzer::GetAnnulusTrackMultiplicityVector() {return AnnulusTrackMultiplicity;}

void ROIAnalyzer::SetOverlapRemovalInfo() {
  // Clear objects to be set
  DeltaR_wrtLeadingROI.clear();
  DeltaPhi_wrtLeadingROI.clear();
  SubleadingROI_dPhi2p0 = -1;
  SubleadingScore_dPhi2p0 = 1.0;

  // Not needed. Done already above!
  // if (RegionsOfInterest.size() > 0) {
  //   leadingROIPosition.SetXYZ(RegionsOfInterest.at(LeadingROI).vx(), RegionsOfInterest.at(LeadingROI).vy(), RegionsOfInterest.at(LeadingROI).vz());
  // }

  // ROI variables
  double thisDeltaR                  = -1;
  double thisDeltaPhi                = -1;
  double thisAbsDeltaPhi             = -1;
  double thisScore                   = -1;

  // ROI deltaR & deltaPhi w.r.t. leading ROI
  for (uint thisROI = 0; thisROI < RegionsOfInterest.size(); thisROI++) {
    math::XYZPoint thisROIPosition(RegionsOfInterest.at(thisROI).vx(), RegionsOfInterest.at(thisROI).vy(), RegionsOfInterest.at(thisROI).vz());

    // DeltaR & DeltaPhi leading & subleading ROIs
    thisDeltaR = reco::deltaR(thisROIPosition, leadingROIPosition);
    thisDeltaPhi = reco::deltaPhi(thisROIPosition.phi(), leadingROIPosition.phi());
    thisAbsDeltaPhi = TMath::Abs(thisDeltaPhi);
    thisScore = TaggerScores.at(thisROI);

    DeltaR_wrtLeadingROI.push_back(thisDeltaR);
    DeltaPhi_wrtLeadingROI.push_back(thisDeltaPhi);
    // ROIAbsDeltaPhi.push_back(thisAbsDeltaPhi); // Not needed. Done directly in FillROIType

    if (thisAbsDeltaPhi > 2.0 && thisScore <= SubleadingScore_dPhi2p0) {
      SubleadingROI_dPhi2p0 = thisROI;
      SubleadingScore_dPhi2p0 = thisScore;
    }

  }

  if (SubleadingROI_dPhi2p0 != -1) {
    subleadingROIPosition.SetXYZ(RegionsOfInterest.at(SubleadingROI_dPhi2p0).vx(), RegionsOfInterest.at(SubleadingROI_dPhi2p0).vy(), RegionsOfInterest.at(SubleadingROI_dPhi2p0).vz());
    // SubleadingPhi_dPhi2p0 = subleadingROIPosition.phi(); // Not needed. Done directly in FillROIType
    // SubleadingIsolation_dPhi2p0 = ROIAnnulusTrackMultiplicity.at(thisROI); // Not needed.
    // SubleadingNClusters_dPhi2p0 = ROITrackClusterMultiplicity.at(thisROI); // Not needed.
  }

  // Not needed. Subleading score not used anywhere else!
  // else {
  //   SubleadingScore_dPhi2p0 = -1.0;
  // }

}



std::vector<float> ROIAnalyzer::GetDeltaRVector() {return DeltaR_wrtLeadingROI;}

std::vector<float> ROIAnalyzer::GetDeltaPhiVector() {return DeltaPhi_wrtLeadingROI;}

void ROIAnalyzer::SetGenMatchingInfo(const bool isSignal, const math::XYZPoint leadingLLPPosition, const math::XYZPoint subleadingLLPPosition) {
  // Clear objects to be set
  DistanceToLeadingLLP.clear();
  DistanceToSubleadingLLP.clear();

  // Signal matching variables
  math::XYZVector thisROIVectorFromLeadingLLP, thisROIVectorFromSubleadingLLP;

  for (uint thisROI = 0; thisROI < RegionsOfInterest.size(); thisROI++) {
    math::XYZPoint thisROIPosition(RegionsOfInterest.at(thisROI).vx(), RegionsOfInterest.at(thisROI).vy(), RegionsOfInterest.at(thisROI).vz());

    if (isSignal){
      thisROIVectorFromLeadingLLP = thisROIPosition - leadingLLPPosition;
      thisROIVectorFromSubleadingLLP = thisROIPosition - subleadingLLPPosition;

      DistanceToLeadingLLP.push_back(thisROIVectorFromLeadingLLP.R());
      DistanceToSubleadingLLP.push_back(thisROIVectorFromSubleadingLLP.R());

      // Not needed. Done directly in FillROIType
      // DistanceToNearestLLP.push_back(TMath::Min(thisROIVectorFromLeadingLLP.R(),thisROIVectorFromSubleadingLLP.R()));
      // ROIFromLeadingLLP.push_back(thisROIVectorFromLeadingLLP.R()<1);
      // ROIFromSubleadingLLP.push_back(thisROIVectorFromSubleadingLLP.R()<1);

      // Not needed. Get directly when plotting!
      // nROIsFromLeadingLLP = std::accumulate(ROIFromLeadingLLP.begin(), ROIFromLeadingLLP.end(), 0);
      // nROIsFromSubleadingLLP = std::accumulate(ROIFromSubleadingLLP.begin(), ROIFromSubleadingLLP.end(), 0);
    }

    else{
      DistanceToLeadingLLP.push_back(-1.0);
      DistanceToSubleadingLLP.push_back(-1.0);
    }

  }
}

std::vector<float> ROIAnalyzer::GetDistanceToLeadingLLPVector() {return DistanceToLeadingLLP;}

std::vector<float> ROIAnalyzer::GetDistanceToSubleadingLLPVector() {return DistanceToSubleadingLLP;}

float ROIAnalyzer::GetAbsDeltaPhiToLeadingROI(const float jetPhi) {
  if (LeadingROI != -1) return TMath::Abs(reco::deltaPhi(jetPhi, leadingROIPosition.phi()));
  return -1.0;
}

float ROIAnalyzer::GetAbsDeltaPhiToSubleadingROI(const float jetPhi) {
  if (SubleadingROI_dPhi2p0 != -1) return TMath::Abs(reco::deltaPhi(jetPhi, subleadingROIPosition.phi()));
  return -1.0;
}


void ROIAnalyzer::SetAnalysisInfo(const edm::Event& iEvent, const bool isSignal, const math::XYZPoint leadingLLPPosition, const math::XYZPoint subleadingLLPPosition) {
  ROIAnalyzer::SetTaggerScores(iEvent);
  ROIAnalyzer::SetOverlapRemovalInfo();
  ROIAnalyzer::SetGenMatchingInfo(isSignal, leadingLLPPosition, subleadingLLPPosition);
  // ROIAnalyzer::SetJetMatchingInfo();
}

int ROIAnalyzer::GetLeadingROIIndex() {return LeadingROI;}

int ROIAnalyzer::GetSubleadingROIIndex() {return SubleadingROI_dPhi2p0;}
