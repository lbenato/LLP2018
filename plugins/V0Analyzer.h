#ifndef V0ANALYZER_H
#define V0ANALYZER_H

#include <iostream>
#include <cmath>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "DataFormats/Candidate/interface/VertexCompositePtrCandidate.h"

#include "TFile.h"
#include "TH1.h"

class V0Analyzer {
 public:
  V0Analyzer(edm::ParameterSet&, edm::ConsumesCollector&&);
  ~V0Analyzer();

  virtual std::vector<reco::VertexCompositePtrCandidate> FillKShortVector(const edm::Event&);
  virtual std::vector<reco::VertexCompositePtrCandidate> FillLambdaVector(const edm::Event&);

 private:
  edm::EDGetTokenT<std::vector<reco::VertexCompositePtrCandidate> > KShortToken;
  edm::EDGetTokenT<std::vector<reco::VertexCompositePtrCandidate> > LambdaToken;
};

#endif
