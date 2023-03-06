#include "V0Analyzer.h"


V0Analyzer::V0Analyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
  KShortToken(CColl.consumes<std::vector<reco::VertexCompositePtrCandidate> >(PSet.getParameter<edm::InputTag>("kShorts"))),
  LambdaToken(CColl.consumes<std::vector<reco::VertexCompositePtrCandidate> >(PSet.getParameter<edm::InputTag>("lambdas")))
{
  std::cout << " --- V0Analyzer initialization ---" << std::endl;
  std::cout << std::endl;
}

V0Analyzer::~V0Analyzer() {

}

// ---------- KShorts ----------

std::vector<reco::VertexCompositePtrCandidate> V0Analyzer::FillKShortVector(const edm::Event& iEvent) {
  edm::Handle<reco::VertexCompositePtrCandidateCollection> KShortCollection;
  iEvent.getByToken(KShortToken, KShortCollection);
  return *KShortCollection;
}

// ---------- Lambdas ----------

std::vector<reco::VertexCompositePtrCandidate> V0Analyzer::FillLambdaVector(const edm::Event& iEvent) {
  edm::Handle<reco::VertexCompositePtrCandidateCollection> LambdaCollection;
  iEvent.getByToken(LambdaToken, LambdaCollection);
  return *LambdaCollection;
}