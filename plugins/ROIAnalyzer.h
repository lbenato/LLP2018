#ifndef ROIANALYZER_H
#define ROIANALYZER_H

#include <iostream>
#include <cmath>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

//ROI info
#include "DataFormats/Common/interface/View.h"
//#include "HiggsLongLived/TreeMaker/interface/TreeClasses/Common.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/Vertex.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/MINIAOD/LostTrack.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/MINIAOD/PackedPFCandidate.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/TrackCluster.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/RegionOfInterest.h"
#include "HiggsLongLived/TreeMaker/interface/PackedCandidate.h"
#include "HiggsLongLived/TreeMaker/interface/VertexCompositeCandidate.h"
#include "HiggsLongLived/TreeMaker/interface/PseudoROI.h"
//#include "HiggsLongLived/TreeMaker/plugins/TreeMakerMINIAOD.h"

// ROI tagger:
#include "HiggsLongLived/AnalysisCommon/interface/AnalysisCommon.h"
// #include "HiggsLongLived/ControlRegionStudies/interface/TreeClasses.h"
#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"
// #include "DataFormats/Math/interface/Point3D.h"
// #include "DataFormats/Math/interface/Vector3D.h"
// #include "DataFormats/Math/interface/deltaR.h"
// #include "DataFormats/Math/interface/deltaPhi.h"

#include "TFile.h"
#include "TH1.h"

class ROIAnalyzer {
 public:
  ROIAnalyzer(edm::ParameterSet&, edm::ConsumesCollector&&);
  ~ROIAnalyzer();

  // Set input vectors (
  // virtual std::vector<Vertex> SetVertexVector(const edm::Event&);
  // virtual std::vector<LostTrack> SetLostTrackVector(const edm::Event&, unsigned);
  // virtual std::vector<PackedPFCandidate> SetPFCandidateVector(const edm::Event&, unsigned);
  // virtual std::vector<TrackCluster> SetTrackClusterVector(const edm::Event&);
  // virtual std::vector<RegionOfInterest> SetROIVector(const edm::Event&);
  virtual void SetVertexVector(const edm::Event&);
  virtual void SetLostTrackVector(const edm::Event&, unsigned);
  virtual void SetPFCandidateVector(const edm::Event&, unsigned);
  virtual void SetTrackClusterVector(const edm::Event&);
  virtual void SetROIVector(const edm::Event&);
  virtual void SetAllTaggerInputVectors(const edm::Event&);

  virtual void SetTaggerScores(const edm::Event&);
  virtual void SetOverlapRemovalInfo();
  virtual void SetGenMatchingInfo(const bool, const math::XYZPoint, const math::XYZPoint);
  virtual void SetAnalysisInfo(const edm::Event&, const bool, const math::XYZPoint, const math::XYZPoint);

  // Tagger input vectors
  virtual std::vector<Vertex> GetVertexVector();
  virtual std::vector<LostTrack> GetLostTrackVector();
  virtual std::vector<PackedPFCandidate> GetPFCandidateVector();
  virtual std::vector<TrackCluster> GetTrackClusterVector();
  virtual std::vector<RegionOfInterest> GetROIVector();

  // Tagger scores
  virtual std::vector<float> GetTaggerScores();

  // ROI & isolation annulus multiplicities
  virtual std::vector<int> GetTrackClusterMultiplicityVector();
  virtual std::vector<int> GetAnnulusTrackMultiplicityVector();

  // Overlap removal info
  virtual std::vector<float> GetDeltaRVector();
  virtual std::vector<float> GetDeltaPhiVector();

  // Gen-matching info
  virtual std::vector<float> GetDistanceToLeadingLLPVector();
  virtual std::vector<float> GetDistanceToSubleadingLLPVector();

  // Indices of (sub)leading ROI
  virtual int GetLeadingROIIndex();
  virtual int GetSubleadingROIIndex();

  // DeltaPhi (e.g. for jet matching)
  virtual float GetAbsDeltaPhiToLeadingROI(const float);
  virtual float GetAbsDeltaPhiToSubleadingROI(const float);

 private:
   edm::EDGetTokenT<edm::View<reco::Vertex> > verticesToken;
   edm::EDGetTokenT<edm::View<PackedCandidate> > lostTracksToken;
   edm::EDGetTokenT<edm::View<PackedCandidate> > packedPFCandidatesToken;
   edm::EDGetTokenT<edm::View<VertexCompositeCandidate> > trackClustersToken;
   edm::EDGetTokenT<edm::View<PseudoROI> > regionsOfInterestToken;

   std::string model;
   tensorflow::Session *tfsession = nullptr;

   std::vector<Vertex> Vertices;
   std::vector<LostTrack> LostTracks;
   std::vector<PackedPFCandidate> PFCandidates;
   std::vector<TrackCluster> TrackClusters;
   std::vector<RegionOfInterest> RegionsOfInterest;

   std::vector<float> TaggerScores;

   std::vector<float> DeltaR_wrtLeadingROI;
   std::vector<float> DeltaPhi_wrtLeadingROI;
   // std::vector<float> AbsDeltaPhi_wrtLeadingROI; // Compute directly in FillROIType

   std::vector<int> TrackClusterMultiplicity;
   std::vector<int> AnnulusTrackMultiplicity;

   // std::vector<float> DistanceToNearestLLP; // Compute directly in FillROIType
   std::vector<float> DistanceToLeadingLLP;
   std::vector<float> DistanceToSubleadingLLP;

   // std::vector<bool> MatchedToLLP; // Compute directly in FillROIType
   // std::vector<bool> MatchedToLeadingLLP; // Compute directly in FillROIType
   // std::vector<bool> MatchedToSubleadingLLP; // Compute directly in FillROIType

   math::XYZPoint leadingROIPosition, subleadingROIPosition;

   int   LeadingROI, SubleadingROI_dPhi2p0;
   float LeadingScore, SubleadingScore_dPhi2p0;

};

#endif
