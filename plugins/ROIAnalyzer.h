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
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/MINIAOD/LostTrack.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/MINIAOD/PackedPFCandidate.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/TrackCluster.h"
#include "HiggsLongLived/TreeMaker/interface/TreeClasses/RegionOfInterest.h"
#include "HiggsLongLived/TreeMaker/interface/PackedCandidate.h"
#include "HiggsLongLived/TreeMaker/interface/VertexCompositeCandidate.h"
#include "HiggsLongLived/TreeMaker/interface/PseudoROI.h"
//#include "HiggsLongLived/TreeMaker/plugins/TreeMakerMINIAOD.h"

#include "TFile.h"
#include "TH1.h"

class ROIAnalyzer {
 public:
  ROIAnalyzer(edm::ParameterSet&, edm::ConsumesCollector&&);
  ~ROIAnalyzer();
  virtual std::vector<LostTrack> FillLostTrackVector(const edm::Event&, unsigned);
  virtual std::vector<PackedPFCandidate> FillPFCandidateVector(const edm::Event&, unsigned);
  virtual std::vector<TrackCluster> FillTrackClusterVector(const edm::Event&);
  virtual std::vector<RegionOfInterest> FillROIVector(const edm::Event&);

 private:
   edm::EDGetTokenT<edm::View<PackedCandidate> > lostTracksToken;
   edm::EDGetTokenT<edm::View<PackedCandidate> > packedPFCandidatesToken;
   edm::EDGetTokenT<edm::View<VertexCompositeCandidate> > trackClustersToken;
   edm::EDGetTokenT<edm::View<PseudoROI> > regionsOfInterestToken;

};

#endif
