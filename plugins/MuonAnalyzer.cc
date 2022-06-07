#include "MuonAnalyzer.h"

MuonAnalyzer::MuonAnalyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
    MuonToken(CColl.consumes<std::vector<pat::Muon> >(PSet.getParameter<edm::InputTag>("muons"))),
    VertexToken(CColl.consumes<reco::VertexCollection>(PSet.getParameter<edm::InputTag>("vertices"))),
    //    MuonTrkFileName(PSet.getParameter<std::string>("muonTrkFileName")),// removed obsolete things for now
    MuonIdFileName(PSet.getParameter<std::string>("muonIdFileName")),
    MuonIsoFileName(PSet.getParameter<std::string>("muonIsoFileName")),
    //    MuonTrkHighptFileName(PSet.getParameter<std::string>("muonTrkHighptFileName")), // removed obsolete things for now
    MuonTriggerFileName(PSet.getParameter<std::string>("muonTriggerFileName")),
    //    DoubleMuonTriggerFileName(PSet.getParameter<std::string>("doubleMuonTriggerFileName")), //obsolete
    Muon1Id(PSet.getParameter<int>("muon1id")),
    Muon2Id(PSet.getParameter<int>("muon2id")),
    Muon1Iso(PSet.getParameter<int>("muon1iso")),
    Muon2Iso(PSet.getParameter<int>("muon2iso")),
    Muon1Pt(PSet.getParameter<double>("muon1pt")),
    Muon2Pt(PSet.getParameter<double>("muon2pt")),
    Muon1Eta(PSet.getParameter<double>("muon1eta")),
    Muon2Eta(PSet.getParameter<double>("muon2eta")),
    UseTuneP(PSet.getParameter<bool>("useTuneP")),
    DoRochester(PSet.getParameter<bool>("doRochester"))
{
    isMuonTriggerFile = isMuonIdFile = false;
    isFile2016 = isFile2017 = isFile2018 = false;

// //removed obsolete things for now
//     // isDoubleMuonTriggerFile = isMuonTrkFile = isMuonTrkHighptFile =false;
//     // Double Muon trigger: obsolete! --> todo: what about this??? Super old stuff!
//     // https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonReferenceEffs --> last updated in 2014!
//     DoubleMuonTriggerFile=new TFile(DoubleMuonTriggerFileName.c_str(), "READ");
//     if(!DoubleMuonTriggerFile->IsZombie()) {
//         MuonTriggerLt20=(TH2F*)DoubleMuonTriggerFile->Get("DATA_over_MC_Mu17Mu8_Tight_Mu1_10To20_&_Mu2_20ToInfty_with_SYST_uncrt");
//         MuonTriggerGt20=(TH2F*)DoubleMuonTriggerFile->Get("DATA_over_MC_Mu17Mu8_Tight_Mu1_20ToInfty_&_Mu2_20ToInfty_with_SYST_uncrt");
//         for(int i=1; i<=MuonTriggerGt20->GetNbinsX(); i++) {
//             for(int j=1; j<=MuonTriggerGt20->GetNbinsY(); j++) {
//                 if(j>i) {
//                     if(MuonTriggerGt20->GetBinContent(i, j)>0.) std::cout << " - MuonAnalyzer Warning: Trying to symmetrize diagonal matrix in bin " << i << ", " << j << std::endl;
//                     MuonTriggerGt20->SetBinContent(i, j, MuonTriggerGt20->GetBinContent(j, i));
//                     MuonTriggerGt20->SetBinError(i, j, MuonTriggerGt20->GetBinError(j, i));
//                 }
//             }
//         }
//         isDoubleMuonTriggerFile=true;
//     }
//     else {
//         throw cms::Exception("MuonAnalyzer", "No Double Muon Trigger Weight File");
//         return;
//     }

    //Single Muon Trigger, 2016
    //NOTE -> SF APPLIED AS PER-EVENT WEIGHTS
    MuonTriggerFile=new TFile(MuonTriggerFileName.c_str(), "READ");
    if(!MuonTriggerFile->IsZombie()) {
        MuonTriggerIsoMu24=(TH2F*)MuonTriggerFile->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio");
        MuonTriggerMu50   =(TH2F*)MuonTriggerFile->Get("Mu50_OR_TkMu50_PtEtaBins/pt_abseta_ratio");
        isMuonTriggerFile=true;
    }
    else {
        throw cms::Exception("MuonAnalyzer", "No Muon Trigger Weight File");
        return;
    }

    // //removed obsolete things for now
    // //Muon tracker eff
    // // FIXME -> STILL ICHEP-2016 -> TO BE UPDATED ? --> todo: super old stuff! Is there something to exchange?
    // MuonTrkFile=new TFile(MuonTrkFileName.c_str(), "READ");
    // if(!MuonTrkFile->IsZombie()) {
    //     MuonTrkGraph=(TGraphAsymmErrors*)MuonTrkFile->Get("ratio_eff_eta3_dr030e030_corr");
    //     MuonTrk=(TH1F*)ConvertTGraph(MuonTrkGraph);
    //     isMuonTrkFile=true;
    // }
    // else {
    //     throw cms::Exception("MuonAnalyzer", "No MuonTrk Weight File");
    //     return;
    // }


    //Muon id, 2016
    //NOTE -> SF APPLIED AS PER-EVENT WEIGHTS
    MuonIdFile=new TFile(MuonIdFileName.c_str(), "READ");
    if(!MuonIdFile->IsZombie()) {
      if(MuonIdFileName.find("2016") != std::string::npos){
        MuonIdLoose =(TH2F*)MuonIdFile->Get("NUM_LooseID_DEN_genTracks_eta_pt");
        MuonIdMedium=(TH2F*)MuonIdFile->Get("NUM_MediumID_DEN_genTracks_eta_pt");
        MuonIdTight =(TH2F*)MuonIdFile->Get("NUM_TightID_DEN_genTracks_eta_pt");
        MuonIdHighpt=(TH2F*)MuonIdFile->Get("NUM_HighPtID_DEN_genTracks_eta_pair_newTuneP_probe_pt"); // done wrt tune-p pt
	isFile2016 = true;
      }
      else if(MuonIdFileName.find("2017") != std::string::npos){
	MuonIdLoose =(TH2F*)MuonIdFile->Get("NUM_LooseID_DEN_genTracks_pt_abseta");
        MuonIdMedium=(TH2F*)MuonIdFile->Get("NUM_MediumID_DEN_genTracks_pt_abseta");
        MuonIdTight =(TH2F*)MuonIdFile->Get("NUM_TightID_DEN_genTracks_pt_abseta");
        MuonIdHighpt=(TH2F*)MuonIdFile->Get("NUM_HighPtID_DEN_genTracks_pair_newTuneP_probe_pt_abseta");
        isFile2017 = true;
      }
      else if(MuonIdFileName.find("2018") != std::string::npos){
	MuonIdLoose =(TH2F*)MuonIdFile->Get("NUM_LooseID_DEN_TrackerMuons_pt_abseta");
        MuonIdMedium=(TH2F*)MuonIdFile->Get("NUM_MediumID_DEN_TrackerMuons_pt_abseta");
        MuonIdTight =(TH2F*)MuonIdFile->Get("NUM_TightID_DEN_TrackerMuons_pt_abseta");
        MuonIdHighpt=(TH2F*)MuonIdFile->Get("NUM_HighPtID_DEN_TrackerMuons_pair_newTuneP_probe_pt_abseta");
        isFile2018 = true;
      }
      else throw cms::Exception("MuonAnalyzer", "Run era not in Muon Id Weight File Name");
        isMuonIdFile=true;
    }
    else {
        throw cms::Exception("MuonAnalyzer", "No MuonId Weight File");
        return;
    }

    //Muon iso, 2016
    //NOTE -> SF APPLIED AS PER-EVENT WEIGHTS
    MuonIsoFile=new TFile(MuonIsoFileName.c_str(), "READ");
    if(!MuonIsoFile->IsZombie()) {
      if(MuonIsoFileName.find("2016") != std::string::npos){
	MuonIsoHighpt=(TH2F*)MuonIsoFile->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_eta_pair_newTuneP_probe_pt");
	MuonIsoLoose=(TH2F*)MuonIsoFile->Get("NUM_LooseRelIso_DEN_LooseID_eta_pt");
	MuonIsoTight=(TH2F*)MuonIsoFile->Get("NUM_TightRelIso_DEN_TightID_eta_pt");
        isFile2016 = true;
      }
      else if(MuonIsoFileName.find("2017") != std::string::npos || MuonIsoFileName.find("2018") != std::string::npos){
	MuonIsoHighpt=(TH2F*)MuonIsoFile->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_pair_newTuneP_probe_pt_abseta");
	MuonIsoLoose=(TH2F*)MuonIsoFile->Get("NUM_LooseRelIso_DEN_LooseID_pt_abseta");
	MuonIsoTight=(TH2F*)MuonIsoFile->Get("NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta");
        isFile2017 = MuonIsoFileName.find("2017") != std::string::npos;
        isFile2018 = MuonIsoFileName.find("2018") != std::string::npos;
      }
      else throw cms::Exception("MuonAnalyzer", "Run era not in Muon ISO Weight File Name");
      isMuonIsoFile=true;
    }
    else {
        throw cms::Exception("MuonAnalyzer", "No MuonIso Weight File");
        return;
    }

    // //Muon custom TrackerHighPt id, 2016
    // // FIXME -> STILL ICHEP-2016 -> TO BE UPDATED ?
    // MuonTrkHighptFile=new TFile(MuonTrkHighptFileName.c_str(), "READ");
    // if(!MuonTrkHighptFile->IsZombie()) {
    //     MuonIdTrkHighpt=(TH2F*)MuonTrkHighptFile->Get("scalefactor");
    //     isMuonTrkHighptFile=true;
    // }
    // else {
    //     throw cms::Exception("MuonAnalyzer", "No MuonTrkHighpt Weight File");
    //     return;
    // }

    rmcor = new rochcor2016();

    std::cout << " --- MuonAnalyzer initialization ---" << std::endl;
    std::cout << "  mu Id  [1, 2]     :\t" << Muon1Id << "\t" << Muon2Id << std::endl;
    std::cout << "  mu Iso [1, 2]     :\t" << Muon1Iso << "\t" << Muon2Iso << std::endl;
    std::cout << "  mu pT  [1, 2]     :\t" << Muon1Pt << "\t" << Muon2Pt << std::endl;
    std::cout << "  mu eta [1, 2]     :\t" << Muon1Eta << "\t" << Muon2Eta << std::endl;
    std::cout << "  DoRochester       :\t" << DoRochester << std::endl;
    std::cout << "  ID SF file        :\t" << MuonIdFile->GetName() << std::endl;
    // std::cout << "  ID SF hist (Tight):\t" << MuonIdTight->GetName() << std::endl;
    std::cout << "  Iso SF file       :\t" << MuonIsoFile->GetName() << std::endl;
    // std::cout << "  Iso SF hist (Tight):\t" << MuonIsoTight->GetName() << std::endl;

    std::cout << std::endl;

}

MuonAnalyzer::~MuonAnalyzer() {
    MuonTriggerFile->Close();
    MuonIdFile->Close();
    MuonIsoFile->Close();
    //removed obsolete things for now
    //    DoubleMuonTriggerFile->Close();
    //    MuonTrkFile->Close();
    //    MuonTrkHighptFile->Close();
}





std::vector<pat::Muon> MuonAnalyzer::FillMuonVector(const edm::Event& iEvent) {
    bool isMC(!iEvent.isRealData());
    int IdTh(Muon1Id), IsoTh(Muon1Iso);
    float PtTh(Muon1Pt), EtaTh(Muon1Eta);
    std::vector<pat::Muon> Vect;
    // Declare and open collections
    edm::Handle<std::vector<pat::Muon> > MuonCollection;
    iEvent.getByToken(MuonToken, MuonCollection);

    edm::Handle<reco::VertexCollection> PVCollection;
    iEvent.getByToken(VertexToken, PVCollection);
    const reco::Vertex* vertex=&PVCollection->front();


    // Loop on Muon collection
    for(std::vector<pat::Muon>::const_iterator it=MuonCollection->begin(); it!=MuonCollection->end(); ++it) {
        if(Vect.size()>0) {
            IdTh=Muon2Id;
            IsoTh=Muon2Iso;
            PtTh=Muon2Pt;
            EtaTh=Muon2Eta;
        }
        pat::Muon mu=*it;
        // Pt and eta
        if (UseTuneP)
            mu.setP4(reco::Candidate::PolarLorentzVector(mu.tunePMuonBestTrack()->pt(), mu.eta(), mu.phi(), mu.mass()));
        // Apply Rochester corrections
        if (DoRochester){
            TLorentzVector * mup4 = new TLorentzVector ();
            mup4->SetPtEtaPhiM(mu.pt(), mu.eta(), mu.phi(), mu.mass());
            if(!isMC)
                rmcor->momcor_mc(*mup4, float(mu.charge()), mu.innerTrack()->hitPattern().trackerLayersWithMeasurement(), float(1.0));
            else
                rmcor->momcor_data(*mup4, float(mu.charge()), 0, float(1.0));
            mu.setP4(reco::Candidate::PolarLorentzVector(mup4->Pt(), mu.eta(), mu.phi(), mu.mass()));
            delete mup4;
        }
        if(mu.pt()<PtTh || fabs(mu.eta())>EtaTh) continue;
        // Muon Quality ID 2015-2016: see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2
        //if(IdTh==0 && !IsTrackerHighPtMuon(mu, vertex)) continue;//not very useful for displacement
        if(IdTh==0 && !mu.isPFMuon()) continue;
        if(IdTh==1 && !mu.isLooseMuon()) continue;
        if(IdTh==2 && !mu.isMediumMuon()) continue;
        if(IdTh==3 && !mu.isTightMuon(*vertex)) continue;
        if(IdTh==4 && !mu.isHighPtMuon(*vertex)) continue;
        // Isolation
        float pfIso03 = (mu.pfIsolationR03().sumChargedHadronPt + std::max(mu.pfIsolationR03().sumNeutralHadronEt + mu.pfIsolationR03().sumPhotonEt - 0.5*mu.pfIsolationR03().sumPUPt, 0.) ) / mu.pt(); // PF-based pt for PFIso
        float pfIso04 = (mu.pfIsolationR04().sumChargedHadronPt + std::max(mu.pfIsolationR04().sumNeutralHadronEt + mu.pfIsolationR04().sumPhotonEt - 0.5*mu.pfIsolationR04().sumPUPt, 0.) ) / mu.pt(); // PF-based pt for PFIso
	      // Tracker iso corrected with by-hand subtraction
        float trkIso = mu.trackIso();
        // Subtrack all muons from iso cone
        for(auto mit=MuonCollection->begin(); mit!=MuonCollection->end(); ++mit) if(mit!=it && deltaR(*mit, mu)<0.3 && IsTrackerHighPtMuon(mu, vertex) && mit->track().isNonnull()) trkIso -= mit->innerTrack()->pt();
        //if(Vect.size() == 0 && std::next(it, 1)!=MuonCollection->end() && deltaR(*std::next(it, 1), mu) < 0.3) trkIso -= std::next(it, 1)->pt();
        //if(Vect.size() == 1 && deltaR(Vect[0], mu) < 0.3) trkIso -= Vect[0].tunePMuonBestTrack()->pt();
        if(trkIso < 0.) trkIso = 0.;
        trkIso /= mu.pt();
        // Muon Isolation working point 2015-2016: see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
        if(IsoTh==0 && trkIso>0.1) continue;
        if(IsoTh==1 && pfIso04>0.25) continue;
        if(IsoTh==2 && pfIso04>0.15) continue;
        // Add userFloat
        mu.addUserFloat("inTrkPt", (mu.track().isNonnull() && mu.innerTrack().isNonnull()) ? mu.innerTrack()->pt() : -1);
        mu.addUserFloat("trkIso", trkIso);
        mu.addUserFloat("pfIso03", pfIso03);
        mu.addUserFloat("pfIso04", pfIso04);
        mu.addUserFloat("dxy", mu.track().isNonnull() ? mu.muonBestTrack()->dxy(vertex->position()) : -999.);
        mu.addUserFloat("dz", mu.track().isNonnull() ? mu.muonBestTrack()->dz(vertex->position()) : -999.);
        mu.addUserFloat("dxyErr", mu.track().isNonnull() ? mu.muonBestTrack()->dxyError() : -999.);
        mu.addUserFloat("dxySig", (mu.track().isNonnull() && mu.muonBestTrack()->dxyError() > 0) ?  mu.muonBestTrack()->dxy(vertex->position()) / mu.muonBestTrack()->dxyError() : -999.);
        //mu.addUserInt("isTrackerHighPt", IsTrackerHighPtMuon(mu, vertex) ? 1 : 0);
        mu.addUserInt("isPFMuon", mu.isPFMuon() ? 1 : 0);
        mu.addUserInt("isLoose", mu.isLooseMuon() ? 1 : 0);
        mu.addUserInt("isMedium", mu.isMediumMuon() ? 1 : 0);
        mu.addUserInt("isTight", mu.isTightMuon(*vertex) ? 1 : 0);
        mu.addUserInt("isHighPt", mu.isHighPtMuon(*vertex) ? 1 : 0);
        // Trigger flags:
        mu.addUserInt("triggered_HLT_Mu12_IP6", mu.triggered("HLT_Mu12_IP6_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu10p5_IP3p5", mu.triggered("HLT_Mu10p5_IP3p5_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu9_IP6", mu.triggered("HLT_Mu9_IP6_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu9_IP5", mu.triggered("HLT_Mu9_IP5_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu9_IP4", mu.triggered("HLT_Mu9_IP4_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu8p5_IP3p5", mu.triggered("HLT_Mu8p5_IP3p5_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu8_IP6", mu.triggered("HLT_Mu8_IP6_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu8_IP5", mu.triggered("HLT_Mu8_IP5_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu8_IP3", mu.triggered("HLT_Mu8_IP3_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_HLT_Mu7_IP4", mu.triggered("HLT_Mu7_IP4_part*_v*") ? 1 : 0 );
        mu.addUserInt("triggered_BParking", mu.triggered("HLT_Mu*_IP*_part*_v*") ? 1 : 0 );
        mu.addUserInt("isSoftMuon", mu.isSoftMuon(*vertex) ? 1 : 0);
        mu.addUserInt("isSoftMuonFromCuts", IsSoftMuon(mu, vertex) ? 1 : 0);
        mu.addUserInt("isInnerTrackerMuon", mu.innerTrack().isNonnull() ? 1 : 0);
        mu.addUserInt("isTMOneStationTight", muon::isGoodMuon(mu, muon::TMOneStationTight) ? 1 : 0 );
        mu.addUserInt("nTrackerLayers", mu.innerTrack().isNonnull() ? mu.innerTrack()->hitPattern().trackerLayersWithMeasurement() : -1);
        mu.addUserInt("nPixelLayers", mu.innerTrack().isNonnull() ? mu.innerTrack()->hitPattern().pixelLayersWithMeasurement() : -1);
        mu.addUserInt("isHighPurityTrack", mu.innerTrack().isNonnull() ? mu.innerTrack()->quality(reco::TrackBase::highPurity) : false);
        mu.addUserFloat("dxyTrack", mu.innerTrack().isNonnull() ? mu.innerTrack()->dxy(vertex->position()) : -999.);
        mu.addUserFloat("dzTrack", mu.innerTrack().isNonnull() ? mu.innerTrack()->dz(vertex->position()) : -999.);
        // Fill vector
        Vect.push_back(mu);
    }
    return Vect;
}

void MuonAnalyzer::AddVariables(std::vector<pat::Muon>& Vect, pat::MET& MET) {
    for(unsigned int i = 0; i < Vect.size(); i++) {
        Vect[i].addUserFloat("dPhi_met", fabs(reco::deltaPhi(Vect[i].phi(), MET.phi())));
    }
}


bool MuonAnalyzer::IsTrackerHighPtMuon(pat::Muon& mu, const reco::Vertex* vertex) {

    if (! (mu.isMuon()) ) return false;
    if (! (mu.isTrackerMuon()) ) return false;
    if (! (mu.tunePMuonBestTrack().isNonnull()) ) return false;
    if (! (mu.numberOfMatchedStations() > 1) ) return false;
    if (! (mu.innerTrack()->hitPattern().trackerLayersWithMeasurement() > 5) ) return false;
    if (! (mu.innerTrack()->hitPattern().numberOfValidPixelHits() > 0) ) return false;
    if (! (mu.tunePMuonBestTrack()->ptError()/mu.pt() < 0.3) ) return false;
    if (! (fabs(mu.tunePMuonBestTrack()->dxy(vertex->position()) ) < 0.2) ) return false;
    if (! (fabs(mu.tunePMuonBestTrack()->dz(vertex->position()) ) < 0.5) ) return false;

    return true;

}

bool MuonAnalyzer::IsSoftMuon(pat::Muon& mu, const reco::Vertex* vertex) {
// From: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Soft_Muon
    if (! (muon::isGoodMuon(mu, muon::TMOneStationTight)) ) return false;
    if (! (mu.innerTrack()->hitPattern().trackerLayersWithMeasurement() > 5) ) return false;
    if (! (mu.innerTrack()->hitPattern().pixelLayersWithMeasurement() > 0) ) return false;
    if (! (mu.innerTrack()->quality(reco::TrackBase::highPurity) ) ) return false;
    if (! (fabs(mu.innerTrack()->dxy(vertex->position()) ) < 0.3) ) return false;
    if (! (fabs(mu.innerTrack()->dz(vertex->position()) ) < 20) ) return false;
    return true;
}

std::vector<float> MuonAnalyzer::FixTrackerIsolation(pat::Muon& mu1, pat::Muon& mu2){
    std::vector<float> FixedTrackIso;
    if(mu1.innerTrack().isNonnull() && mu2.innerTrack().isNonnull()){
        if(deltaR(mu1,mu2)<0.3){
	    FixedTrackIso.push_back(std::max(mu1.trackIso() - mu2.innerTrack()->pt(), 0.) / mu1.tunePMuonBestTrack()->pt() );
	    FixedTrackIso.push_back(std::max(mu2.trackIso() - mu1.innerTrack()->pt(), 0.) / mu2.tunePMuonBestTrack()->pt() );
            return FixedTrackIso;
        }
        else{
            FixedTrackIso.push_back(mu1.trackIso());
            FixedTrackIso.push_back(mu2.trackIso());
            return FixedTrackIso;
	}
    }
    else{
        FixedTrackIso.push_back(-1.);
        FixedTrackIso.push_back(-1.);
        return FixedTrackIso;
    }
}


std::string MuonAnalyzer::GetMuon1Id(pat::Muon& mu){
  //if(Muon1Id==0) return "isTrackerHighPt";
    if(Muon1Id==0) return "isPFMuon";
    if(Muon1Id==1) return "isLoose";
    if(Muon1Id==2) return "isMedium";
    if(Muon1Id==3) return "isTight";
    if(Muon1Id==4) return "isHighPt";
    else return "";
}

//ID
float MuonAnalyzer::GetMuonIdSF(pat::Muon& mu, int id) {
  // if (id != Muon1Id || id != Muon2Id){
  //   throw cms::Exception("MuonAnalyzer", "Muon ID set in Ntuplizer not equal to Muon ID set in config file!");
  // }
    if(id==0 && isMuonTrkHighptFile){
// //removed obsolete things for now
//         double pt = std::min( std::max( MuonIdTrkHighpt->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdTrkHighpt->GetYaxis()->GetXmax() - 0.000001 );
//         double eta = std::min( MuonIdLoose->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
//         return MuonIdTrkHighpt->GetBinContent( MuonIdTrkHighpt->FindBin(eta,pt) );

  throw cms::Exception("MuonAnalyzer", "Muon ID 0 currently not supported!");
    }
    if(id==1 && isMuonIdFile){
      if (isFile2016){
	  double pt = std::min( std::max( MuonIdLoose->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdLoose->GetYaxis()->GetXmax() - 0.000001 );
	  double eta = std::min( MuonIdLoose->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
	  return MuonIdLoose->GetBinContent( MuonIdLoose->FindBin(eta,pt) );
	}
      else if (isFile2017 || isFile2018){
	double pt = std::min( std::max( MuonIdLoose->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdLoose->GetXaxis()->GetXmax() - 0.000001 );
        double abseta = std::min( MuonIdLoose->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
        return MuonIdLoose->GetBinContent( MuonIdLoose->FindBin(pt,abseta) );
      }
    }
    if(id==2 && isMuonIdFile){
      if (isFile2016){
	double pt = std::min( std::max( MuonIdMedium->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdMedium->GetYaxis()->GetXmax() - 0.000001 );
	double eta = std::min( MuonIdMedium->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
	return MuonIdMedium->GetBinContent( MuonIdMedium->FindBin(eta,pt) );
      }
      else if (isFile2017 || isFile2018){
	double pt = std::min( std::max( MuonIdMedium->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdMedium->GetXaxis()->GetXmax() - 0.000001 );
        double abseta = std::min( MuonIdMedium->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
        return MuonIdMedium->GetBinContent( MuonIdMedium->FindBin(pt,abseta) );
      }
    }
    if(id==3 && isMuonIdFile){
      if (isFile2016){
	double pt = std::min( std::max( MuonIdTight->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdTight->GetYaxis()->GetXmax() - 0.000001 );
	double eta = std::min( MuonIdTight->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
	return MuonIdTight->GetBinContent( MuonIdTight->FindBin(eta,pt) );
      }
      else if (isFile2017 || isFile2018){
        double pt = std::min( std::max( MuonIdTight->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdTight->GetXaxis()->GetXmax() - 0.000001 );
        double abseta = std::min( MuonIdTight->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
        return MuonIdTight->GetBinContent( MuonIdTight->FindBin(pt,abseta) );
      }
    }
    if(id==4 && isMuonIdFile){
      if (isFile2016){
	double pt = std::min( std::max( MuonIdHighpt->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdHighpt->GetYaxis()->GetXmax() - 0.000001 );
	double eta = std::min( MuonIdHighpt->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
	return MuonIdHighpt->GetBinContent( MuonIdHighpt->FindBin(eta,pt) );
      }
      else if (isFile2017 || isFile2018){
        double pt = std::min( std::max( MuonIdHighpt->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdHighpt->GetXaxis()->GetXmax() - 0.000001 );
        double abseta = std::min( MuonIdHighpt->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
        return MuonIdHighpt->GetBinContent( MuonIdHighpt->FindBin(pt,abseta) );
      }
    }
    return 1.;
}

float MuonAnalyzer::GetMuonIdSFError(pat::Muon& mu, int id) {
  // if (id != Muon1Id || id != Muon2Id){
  //   throw cms::Exception("MuonAnalyzer", "Muon ID set in Ntuplizer not equal to Muon ID set in config file!");
  // }
  if(id==0 && isMuonTrkHighptFile){
// //removed obsolete things for now
//         double pt = std::min( std::max( MuonIdTrkHighpt->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdTrkHighpt->GetYaxis()->GetXmax() - 0.000001 );
//         double eta = std::min( MuonIdLoose->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
//         return MuonIdTrkHighpt->GetBinError( MuonIdTrkHighpt->FindBin(eta,pt) );

    throw cms::Exception("MuonAnalyzer", "Muon ID 0 currently not supported!");
  }
  if(id==1 && isMuonIdFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIdLoose->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdLoose->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIdLoose->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIdLoose->GetBinError( MuonIdLoose->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIdLoose->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdLoose->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIdLoose->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIdLoose->GetBinError( MuonIdLoose->FindBin(pt,abseta) );
    }
  }
  if(id==2 && isMuonIdFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIdMedium->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdMedium->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIdMedium->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIdMedium->GetBinError( MuonIdMedium->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIdMedium->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdMedium->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIdMedium->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIdMedium->GetBinError( MuonIdMedium->FindBin(pt,abseta) );
    }
  }
  if(id==3 && isMuonIdFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIdTight->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdTight->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIdTight->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIdTight->GetBinError( MuonIdTight->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIdTight->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdTight->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIdTight->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIdTight->GetBinError( MuonIdTight->FindBin(pt,abseta) );
    }
  }
  if(id==4 && isMuonIdFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIdHighpt->GetYaxis()->GetXmin(), mu.pt() ) , MuonIdHighpt->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIdHighpt->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIdHighpt->GetBinError( MuonIdHighpt->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIdHighpt->GetXaxis()->GetXmin(), mu.pt() ) , MuonIdHighpt->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIdHighpt->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIdHighpt->GetBinError( MuonIdHighpt->FindBin(pt,abseta) );
    }
  }
  return 0.;
}

//TRK
float MuonAnalyzer::GetMuonTrkSF(pat::Muon& mu) {
    if(isMuonTrkFile){
        double eta = 0.;
        if (mu.eta() > 0)
            eta = std::min( MuonTrk->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
        else
            eta = std::max( MuonTrk->GetXaxis()->GetXmin() + 0.000001 , mu.eta() );
        return MuonTrk->GetBinContent( MuonTrk->FindBin(eta) );
    }
    else return 1.;
}

float MuonAnalyzer::GetMuonTrkSFError(pat::Muon& mu) {
    if(isMuonTrkFile){
        double eta = 0.;
        if (mu.eta() > 0)
            eta = std::min( MuonTrk->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
        else
            eta = std::max( MuonTrk->GetXaxis()->GetXmin() + 0.000001 , mu.eta() );
        return MuonTrk->GetBinError( MuonTrk->FindBin(eta) );
    }
    else return 1.;
}

//ISO
float MuonAnalyzer::GetMuonIsoSF(pat::Muon& mu, int id) {
  if(id==0 && isMuonIsoFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIsoHighpt->GetYaxis()->GetXmin(), mu.pt() ) , MuonIsoHighpt->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIsoHighpt->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIsoHighpt->GetBinContent( MuonIsoHighpt->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIsoHighpt->GetXaxis()->GetXmin(), mu.pt() ) , MuonIsoHighpt->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIsoHighpt->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIsoHighpt->GetBinContent( MuonIsoHighpt->FindBin(pt,abseta) );
    }
  }
  if(id==1 && isMuonIsoFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIsoLoose->GetYaxis()->GetXmin(), mu.pt() ) , MuonIsoLoose->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIsoLoose->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIsoLoose->GetBinContent( MuonIsoLoose->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIsoLoose->GetXaxis()->GetXmin(), mu.pt() ) , MuonIsoLoose->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIsoLoose->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIsoLoose->GetBinContent( MuonIsoLoose->FindBin(pt,abseta) );
    }
  }
  if(id==2 && isMuonIsoFile) throw cms::Exception("MuonAnalyzer", "Muon medium iso (id=2) not supported. Use id=3 for tight isolation");

  if(id==3 && isMuonIsoFile){
    if (isFile2016){
      double pt = std::min( std::max( MuonIsoTight->GetYaxis()->GetXmin(), mu.pt() ) , MuonIsoTight->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIsoTight->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIsoTight->GetBinContent( MuonIsoTight->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIsoTight->GetXaxis()->GetXmin(), mu.pt() ) , MuonIsoTight->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIsoTight->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIsoTight->GetBinContent( MuonIsoTight->FindBin(pt,abseta) );
    }
  }
  return 1.;
}

float MuonAnalyzer::GetMuonIsoSFError(pat::Muon& mu, int id) {
  if(!isMuonIsoFile) return 1.;
  if(id==0){
    if (isFile2016){
      double pt = std::min( std::max( MuonIsoHighpt->GetYaxis()->GetXmin(), mu.pt() ) , MuonIsoHighpt->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIsoHighpt->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIsoHighpt->GetBinError( MuonIsoHighpt->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIsoHighpt->GetXaxis()->GetXmin(), mu.pt() ) , MuonIsoHighpt->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIsoHighpt->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIsoHighpt->GetBinError( MuonIsoHighpt->FindBin(pt,abseta) );
    }
  }
  if(id==1){
    if (isFile2016){
      double pt = std::min( std::max( MuonIsoLoose->GetYaxis()->GetXmin(), mu.pt() ) , MuonIsoLoose->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIsoLoose->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIsoLoose->GetBinError( MuonIsoLoose->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIsoLoose->GetXaxis()->GetXmin(), mu.pt() ) , MuonIsoLoose->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIsoLoose->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIsoLoose->GetBinError( MuonIsoLoose->FindBin(pt,abseta) );
    }
  }
  if(id==3){
    if (isFile2016){
      double pt = std::min( std::max( MuonIsoTight->GetYaxis()->GetXmin(), mu.pt() ) , MuonIsoTight->GetYaxis()->GetXmax() - 0.000001 );
      double eta = std::min( MuonIsoTight->GetXaxis()->GetXmax() - 0.000001 , mu.eta() );
      return MuonIsoTight->GetBinError( MuonIsoTight->FindBin(eta,pt) );
    }
    else if (isFile2017 || isFile2018){
      double pt = std::min( std::max( MuonIsoTight->GetXaxis()->GetXmin(), mu.pt() ) , MuonIsoTight->GetXaxis()->GetXmax() - 0.000001 );
      double abseta = std::min( MuonIsoTight->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
      return MuonIsoTight->GetBinError( MuonIsoTight->FindBin(pt,abseta) );
    }
  }
  return 0.;
}


//obsolete
float MuonAnalyzer::GetDoubleMuonTriggerSF(pat::Muon& mu1, pat::Muon& mu2) {
    if(!isDoubleMuonTriggerFile) return 1.;
    float eta1=fabs(mu1.eta());
    float eta2=fabs(mu2.eta());
    // Muon POG enumeration is inverted 1 <-> 2
    if(mu2.tunePMuonBestTrack()->pt()<20.) return MuonTriggerLt20->GetBinContent(MuonTriggerLt20->FindBin(eta2, eta1));
    return MuonTriggerGt20->GetBinContent(MuonTriggerGt20->FindBin(eta2, eta1));
}

//obsolete
float MuonAnalyzer::GetDoubleMuonTriggerSFError(pat::Muon& mu1, pat::Muon& mu2) {
    if(!isDoubleMuonTriggerFile) return 1.;
    float eta1=fabs(mu1.eta());
    float eta2=fabs(mu2.eta());
    // Muon POG enumeration is inverted 1 <-> 2
    if(mu2.tunePMuonBestTrack()->pt()<20.) return MuonTriggerLt20->GetBinError(MuonTriggerLt20->FindBin(eta2, eta1));
    return MuonTriggerGt20->GetBinError(MuonTriggerGt20->FindBin(eta2, eta1));
}

float MuonAnalyzer::GetMuonTriggerSFIsoMu24(pat::Muon& mu) {
    if(!isMuonTriggerFile) return 1.;
    double pt = std::min( std::max( MuonTriggerIsoMu24->GetXaxis()->GetXmin(), mu.pt() ) , MuonTriggerIsoMu24->GetXaxis()->GetXmax() - 0.000001 );
    double abseta = std::min( MuonTriggerIsoMu24->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
    return MuonTriggerIsoMu24->GetBinContent( MuonTriggerIsoMu24->FindBin(pt, abseta) );
}

float MuonAnalyzer::GetMuonTriggerSFErrorIsoMu24(pat::Muon& mu) {
    if(!isMuonTriggerFile) return 1.;
    double pt = std::min( std::max( MuonTriggerIsoMu24->GetXaxis()->GetXmin(), mu.pt() ) , MuonTriggerIsoMu24->GetXaxis()->GetXmax() - 0.000001 );
    double abseta = std::min( MuonTriggerIsoMu24->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
    return MuonTriggerIsoMu24->GetBinError( MuonTriggerIsoMu24->FindBin(pt,abseta) );
}

float MuonAnalyzer::GetMuonTriggerSFMu50(pat::Muon& mu) {
    if(!isMuonTriggerFile) return 1.;
    double pt = std::min( std::max( MuonTriggerMu50->GetXaxis()->GetXmin(), mu.pt() ) , MuonTriggerMu50->GetXaxis()->GetXmax() - 0.000001 );
    double abseta = std::min( MuonTriggerMu50->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
    return MuonTriggerMu50->GetBinContent( MuonTriggerMu50->FindBin(pt, abseta) );
}

float MuonAnalyzer::GetMuonTriggerSFErrorMu50(pat::Muon& mu) {
    if(!isMuonTriggerFile) return 1.;
    double pt = std::min( std::max( MuonTriggerMu50->GetXaxis()->GetXmin(), mu.pt() ) , MuonTriggerMu50->GetXaxis()->GetXmax() - 0.000001 );
    double abseta = std::min( MuonTriggerMu50->GetYaxis()->GetXmax() - 0.000001 , fabs(mu.eta()) );
    return MuonTriggerMu50->GetBinError( MuonTriggerMu50->FindBin(pt,abseta) );
}




TH1F* MuonAnalyzer::ConvertTGraph(TGraphAsymmErrors* g) {
    int n=g->GetN();
    float x[n+1];
    for(int i=0; i<n; i++) x[i]=g->GetX()[i]-g->GetEXlow()[i];
    x[n]=g->GetX()[n-1]+g->GetEXhigh()[n-1];

    TH1F* h=new TH1F(g->GetName(), g->GetTitle(), n, x); h->Sumw2();
    for(int i=0; i<n; i++) {
      h->SetBinContent(i+1, g->GetY()[i]);
      h->SetBinError(i+1, g->GetEYhigh()[i]);
    }

    return h;
}
