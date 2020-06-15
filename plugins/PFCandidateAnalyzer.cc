#include "PFCandidateAnalyzer.h"


PFCandidateAnalyzer::PFCandidateAnalyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
  PFCandidateToken(CColl.consumes<std::vector<pat::PackedCandidate> >(PSet.getParameter<edm::InputTag>("pfCandidates"))),
  LostTrackToken(CColl.consumes<std::vector<pat::PackedCandidate> >(PSet.getParameter<edm::InputTag>("lostTracks"))),
  PFCandMinPt(PSet.getParameter<double>("pfCandMinPt"))
{   
  std::cout << " --- PFCandidateAnalyzer initialization ---" << std::endl;
  std::cout << "  min pf pT:     :\t" << PFCandMinPt << std::endl;
  std::cout << std::endl;
}

PFCandidateAnalyzer::~PFCandidateAnalyzer() {

}


// ---------- PFCandidates and LostTracks ----------

std::vector<pat::PackedCandidate> PFCandidateAnalyzer::FillPFCandidateVector(const edm::Event& iEvent) {
  float MinPt(PFCandMinPt);
  std::vector<pat::PackedCandidate> Vect;
  edm::Handle<std::vector<pat::PackedCandidate>> PFCandidatesCollection;
  iEvent.getByToken(PFCandidateToken, PFCandidatesCollection);
  for(std::vector<pat::PackedCandidate>::const_iterator it=PFCandidatesCollection->begin(); it!=PFCandidatesCollection->end(); ++it)
    {
      pat::PackedCandidate pf=*it;
      if(pf.pt()<MinPt) continue;
      Vect.push_back(pf);
    }
  return Vect;
  //return *PFCandidates;
}


std::vector<pat::PackedCandidate> PFCandidateAnalyzer::FillLostTrackVector(const edm::Event& iEvent) {
  edm::Handle<std::vector<pat::PackedCandidate>> LostTracks;
  iEvent.getByToken(LostTrackToken,LostTracks);
  return *LostTracks;
}
