//#include "RecoilCorrector.hh" // From: https://github.com/cms-met/MetTools/tree/master/RecoilCorrections

#include "JetAnalyzer.h"


JetAnalyzer::JetAnalyzer(edm::ParameterSet& PSet, edm::ConsumesCollector&& CColl):
    JetToken(CColl.consumes<std::vector<pat::Jet> >(PSet.getParameter<edm::InputTag>("jets"))),
    MetToken(CColl.consumes<std::vector<pat::MET> >(PSet.getParameter<edm::InputTag>("met"))),
    QGToken(CColl.consumes<edm::ValueMap<float>>(edm::InputTag("QGTagger", "qgLikelihood"))),
    ebRecHitsToken(CColl.consumes<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > >(PSet.getParameter<edm::InputTag>("ebRecHits"))),
    eeRecHitsToken(CColl.consumes<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > >(PSet.getParameter<edm::InputTag>("eeRecHits"))),
    esRecHitsToken(CColl.consumes<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > >(PSet.getParameter<edm::InputTag>("esRecHits"))),
    hcalRecHitsHOToken(CColl.consumes<edm::SortedCollection<HORecHit,edm::StrictWeakOrdering<HORecHit>>>(edm::InputTag("reducedHcalRecHits","horeco"))),
    hcalRecHitsHBHEToken(CColl.consumes<edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit>>>(edm::InputTag("reducedHcalRecHits","hbhereco"))),
    JetId(PSet.getParameter<int>("jetid")),
    DataEra(PSet.getParameter<std::string>("dataEra")),
    Jet1Pt(PSet.getParameter<double>("jet1pt")),
    Jet2Pt(PSet.getParameter<double>("jet2pt")),
    JetEta(PSet.getParameter<double>("jeteta")),
    IsAOD(PSet.getParameter<bool>("isAOD")),
    AddQG(PSet.getParameter<bool>("addQGdiscriminator")),
//RecalibrateJets(PSet.getParameter<bool>("recalibrateJets")),
//RecalibrateMass(PSet.getParameter<bool>("recalibrateMass")),
//RecalibratePuppiMass(PSet.getParameter<bool>("recalibratePuppiMass")),
    SoftdropPuppiMassString(PSet.getParameter<std::string>("softdropPuppiMassString")),
    SmearJets(PSet.getParameter<bool>("smearJets")),
    JECUncertaintyName(PSet.getParameter<std::string>("jecUncertaintyName")),
//JECUncertaintyMC(PSet.getParameter<std::string>("jecUncertaintyMC")),
//JECUncertaintyDATA(PSet.getParameter<std::string>("jecUncertaintyDATA")),
//JetCorrectorMC(PSet.getParameter<std::vector<std::string> >("jecCorrectorMC")),
//JetCorrectorDATA(PSet.getParameter<std::vector<std::string> >("jecCorrectorDATA")),
//MassCorrectorMC(PSet.getParameter<std::vector<std::string> >("massCorrectorMC")),
//MassCorrectorDATA(PSet.getParameter<std::vector<std::string> >("massCorrectorDATA")),
//MassCorrectorPuppi(PSet.getParameter<std::string>("massCorrectorPuppi")),
    VertexToken(CColl.consumes<reco::VertexCollection>(PSet.getParameter<edm::InputTag>("vertices"))),
    RhoToken(CColl.consumes<double>(PSet.getParameter<edm::InputTag>("rho"))),
    UseReshape(PSet.getParameter<bool>("reshapeBTag")),
    BTag(PSet.getParameter<std::string>("btag")),
    Jet1BTag(PSet.getParameter<int>("jet1btag")),
    Jet2BTag(PSet.getParameter<int>("jet2btag")),
    BTagDB(PSet.getParameter<std::string>("btagDB")),
    UseRecoil(PSet.getParameter<bool>("metRecoil")),
    RecoilMCFile(PSet.getParameter<std::string>("metRecoilMC")),
    RecoilDataFile(PSet.getParameter<std::string>("metRecoilData")),
    MetTriggerFileName(PSet.getParameter<std::string>("metTriggerFileName")),
    JerName_res(PSet.getParameter<std::string>("jerNameRes")),
    JerName_sf(PSet.getParameter<std::string>("jerNameSf"))
    //    BTagNames(PSet.getParameter<std::vector<std::string> > ("bTagInfos"))
{

    //jecUncMC = new JetCorrectionUncertainty(JECUncertaintyMC);
    //jecUncDATA = new JetCorrectionUncertainty(JECUncertaintyDATA);

    isMetTriggerFile = false;

    if (JECUncertaintyName.find("AK8") != std::string::npos)
      {
	Rparameter = 0.8;
	dRMatch=1.0;
      }

    else 
      {
	Rparameter = 0.4;
	dRMatch=0.5;
      }

    ////obsolete, kept only as future reference for FWLite
    //if(RecalibrateJets) {
    //std::vector<JetCorrectorParameters> jetParMC;
    //    for ( std::vector<std::string>::const_iterator payloadBegin = JetCorrectorMC.begin(), payloadEnd = JetCorrectorMC.end(), ipayload = payloadBegin; ipayload != payloadEnd; ++ipayload ) {
    //        //std::cout << *ipayload << "\n";
    //        jetParMC.push_back(JetCorrectorParameters(*ipayload));
    //    }    
    //    std::vector<JetCorrectorParameters> jetParDATA;
    //    for ( std::vector<std::string>::const_iterator payloadBegin = JetCorrectorDATA.begin(), payloadEnd = JetCorrectorDATA.end(), ipayload = payloadBegin; ipayload != payloadEnd; ++ipayload ) {
    //        //std::cout << *ipayload << "\n";
    //        jetParDATA.push_back(JetCorrectorParameters(*ipayload));
    //  }
    //    // Make the FactorizedJetCorrector
    //    jetCorrMC = boost::shared_ptr<FactorizedJetCorrector> ( new FactorizedJetCorrector(jetParMC) );
    //    jetCorrDATA = boost::shared_ptr<FactorizedJetCorrector> ( new FactorizedJetCorrector(jetParDATA) );
    //}
    
    ////obsolete, kept only as future reference for FWLite
    //if(RecalibrateMass) {
    //    std::vector<JetCorrectorParameters> massParMC;
    //    for ( std::vector<std::string>::const_iterator payloadBegin = MassCorrectorMC.begin(), payloadEnd = MassCorrectorMC.end(), ipayload = payloadBegin; ipayload != payloadEnd; ++ipayload ) {
    //        massParMC.push_back(JetCorrectorParameters(*ipayload));
    //    }    
    //    std::vector<JetCorrectorParameters> massParDATA;
    //    for ( std::vector<std::string>::const_iterator payloadBegin = MassCorrectorDATA.begin(), payloadEnd = MassCorrectorDATA.end(), ipayload = payloadBegin; ipayload != payloadEnd; ++ipayload ) {
    //        massParDATA.push_back(JetCorrectorParameters(*ipayload));
    //    }
    //    // Make the FactorizedJetCorrector
    //    massCorrMC = boost::shared_ptr<FactorizedJetCorrector> ( new FactorizedJetCorrector(massParMC) );
    //    massCorrDATA = boost::shared_ptr<FactorizedJetCorrector> ( new FactorizedJetCorrector(massParDATA) );
    //}
    
    ////if(SmearJets) {
    ////    resolution    = JME::JetResolution::get(iSetup, JerName_res);//new JME::JetResolution(JerName_res);
    ////    resolution_sf = JME::JetResolutionScaleFactor::get(iSetup, JerName_sf);//new JME::JetResolutionScaleFactor(JerName_sf);
    ////    if (JerName_res.find("AK8") != std::string::npos)
    ////        Rparameter = 0.8;
    ////    else 
    ////        Rparameter = 0.4;
    ////}
    
    //if(RecalibratePuppiMass) {
    //  PuppiCorrFile = new TFile(MassCorrectorPuppi.c_str(), "READ");
    //    PuppiJECcorr_gen = (TF1*)PuppiCorrFile->Get("puppiJECcorr_gen");
    //    PuppiJECcorr_reco_0eta1v3 = (TF1*)PuppiCorrFile->Get("puppiJECcorr_reco_0eta1v3");
    //    PuppiJECcorr_reco_1v3eta2v5 = (TF1*)PuppiCorrFile->Get("puppiJECcorr_reco_1v3eta2v5");
    //}
    
    // BTag calibrator
    if(UseReshape) {
        calib           = new BTagCalibration("tagger", BTagDB);
	
	// Modified with code from https://twiki.cern.ch/twiki/bin/view/CMS/BTagCalibration#Code_example_in_C and https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagShapeCalibration

        sf_mode = "iterativefit";
	// Map of flavor type
	flavour_map = {{5, BTagEntry::FLAV_B},
		       {4, BTagEntry::FLAV_C},
		       {0, BTagEntry::FLAV_UDSG}};

	reader = new BTagCalibrationReader(BTagEntry::OP_RESHAPING, "central", {"up_jes","down_jes",
	      "up_lf","down_lf",
	      "up_hf","down_hf",
	      "up_hfstats1","down_hfstats1",
	      "up_hfstats2","down_hfstats2",
	      "up_lfstats1","down_lfstats1",
	      "up_lfstats2","down_lfstats2",
	      "up_cferr1","down_cferr1",
	      "up_cferr2","down_cferr2"});
	for (const auto & kv : flavour_map)
	  reader->load(*calib, kv.second, sf_mode);



	//old code
	/*
	// Set up readers for systematics. This code is largely thanks to Martino & Pablo in
	// https://github.com/cms-hh-pd/alp_analysis/blob/master/interface/BTagFilterOperator.h

	// Systematics to use for each flavor type
	syst_map = {{BTagEntry::FLAV_B, {"up_jes","down_jes",
					 "up_lf","down_lf",
					 "up_hfstats1", "down_hfstats1",
					 "up_hfstats2", "down_hfstats2"}},
                    {BTagEntry::FLAV_C, {"up_cferr1","down_cferr1",
                                         "up_cferr2", "down_cferr2"}},
                    {BTagEntry::FLAV_UDSG, {"up_jes","down_jes",
                                            "up_hf","down_hf",
                                            "up_lfstats1", "down_lfstats1",
					    "up_lfstats2", "down_lfstats2"}}};
	
	sf_mode = "iterativefit";
	
	// Load the reader with each systematic type.
	cr_map.emplace("central",
		       BTagCalibrationReader{BTagEntry::OP_RESHAPING,
			       "central", {}});
	for (const auto & kv : flavour_map) 
	    cr_map.at("central").load(*calib, kv.second, sf_mode);
	// for every flavour
	for (const auto & kv : syst_map) {
	    auto & syst_vector = kv.second;
	    // for every systematic relevant per flavour
	    for (const auto & syst : syst_vector) {
		auto it = cr_map.find(syst);
		if (it ==cr_map.end()) {
		    // return iterator as first pair element
		    it = cr_map.emplace(syst,
					BTagCalibrationReader{BTagEntry::OP_RESHAPING,
						syst, {}})
			.first;
		}
		// load calibration for this flavour and reader
		it->second.load(*calib, kv.first, sf_mode);
	    }//syst_vector loop
	}//syst_map loop
*/
    }//use reshape end
    
    //    BTagInfos_ =edm::vector_transform(BTagNames, [this](edm::InputTag const & tag){return CColl.mayConsume<edm::View<reco::BaseTagInfo> >(tag);});
    //    BTagInfos(edm::vector_transform(BTagNames, [this](std::string const & tag){return CColl.mayConsume<edm::View<reco::BaseTagInfo> >(tag);}))

    // Recoil Corrector
    if(UseRecoil) {
        recoilCorr = new RecoilCorrector(RecoilMCFile);
        recoilCorr->addDataFile(RecoilDataFile);
        recoilCorr->addMCFile(RecoilMCFile);
    }

    MetTriggerFile=new TFile(MetTriggerFileName.c_str(), "READ");
    if(!MetTriggerFile->IsZombie()) {
        MetTriggerHisto=(TH1F*)MetTriggerFile->Get("SingleMuAll_numOR");
        isMetTriggerFile=true;
    }
    else {
        throw cms::Exception("JetAnalyzer", "No Met Trigger File");
        return;
    }

    std::cout << " --- JetAnalyzer initialization ---" << std::endl;
    //std::cout << "  jet collection    :\t" << JetToken << std::endl;
    std::cout << "  jet Id            :\t" << JetId << std::endl;
    std::cout << "  jet pT [1, 2]     :\t" << Jet1Pt << "\t" << Jet2Pt << std::endl;
    std::cout << "  jet eta           :\t" << JetEta << std::endl;
    std::cout << "  R parameter       :\t" << Rparameter << std::endl;
    std::cout << "  b-tagging algo    :\t" << BTag << std::endl;
    std::cout << "  b-tag cut [1, 2]  :\t" << Jet1BTag << "\t" << Jet2BTag << std::endl;
    std::cout << "  apply recoil corr :\t" << (UseRecoil ? "YES" : "NO") << std::endl;
    std::cout << "  apply jet smearing:\t" << (SmearJets ? "YES" : "NO") << " file: \t: " << JerName_res << std::endl;
    //std::cout << "  recoil file MC    :\t" << RecoilMCFile << std::endl;
    //std::cout << "  recoil file Data  :\t" << RecoilDataFile << std::endl;
    std::cout << std::endl;
}

JetAnalyzer::~JetAnalyzer() {
    //if(RecalibratePuppiMass) PuppiCorrFile->Close();

    if(UseReshape) {
	delete calib;
	delete reader;
    }
    //delete jecUncMC;
    //delete jecUncDATA;
    if(UseRecoil) delete recoilCorr;
    MetTriggerFile->Close();
}


std::vector<pat::Jet> JetAnalyzer::FillJetVector(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
    bool isMC(!iEvent.isRealData());
    int BTagTh(Jet1BTag);
    float PtTh(Jet1Pt), EtaTh(JetEta);
    std::vector<pat::Jet> Vect;
    // Declare and open collection
    edm::Handle<std::vector<pat::Jet> > PFJetsCollection;
    iEvent.getByToken(JetToken, PFJetsCollection);
    
    // Open QG value maps
    edm::Handle<edm::ValueMap<float>> QGHandle;
    if(AddQG) iEvent.getByToken(QGToken, QGHandle);

    // Vertex collection
    edm::Handle<reco::VertexCollection> PVCollection;
    iEvent.getByToken(VertexToken, PVCollection);

    // ECAL rechits
    edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > ebRecHitsCollection;
    iEvent.getByToken(ebRecHitsToken, ebRecHitsCollection);
    
    edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > eeRecHitsCollection;
    iEvent.getByToken(eeRecHitsToken, eeRecHitsCollection);
    
    edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > esRecHitsCollection;
    iEvent.getByToken(esRecHitsToken, esRecHitsCollection);
  
    // HCAL rechits
    edm::Handle<edm::SortedCollection<HORecHit,edm::StrictWeakOrdering<HORecHit>>> hcalRecHitsHOCollection;
    iEvent.getByToken(hcalRecHitsHOToken, hcalRecHitsHOCollection);
    
    edm::Handle<edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit>>> hcalRecHitsHBHECollection;
    iEvent.getByToken(hcalRecHitsHBHEToken, hcalRecHitsHBHECollection);


    edm::ESHandle<CaloGeometry> geoHandle;
    iSetup.get<CaloGeometryRecord>().get(geoHandle);
    const CaloSubdetectorGeometry *barrelGeometry = geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalBarrel);
    const CaloSubdetectorGeometry *endcapGeometry = geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalEndcap);
    const CaloSubdetectorGeometry *hbGeometry = geoHandle->getSubdetectorGeometry(DetId::Hcal, HcalBarrel);
    const CaloSubdetectorGeometry *heGeometry = geoHandle->getSubdetectorGeometry(DetId::Hcal, HcalEndcap);
    const CaloSubdetectorGeometry *hoGeometry = geoHandle->getSubdetectorGeometry(DetId::Hcal, HcalOuter);
  
    // Rho handle
    edm::Handle<double> rho_handle;
    iEvent.getByToken(RhoToken, rho_handle);
 
    auto tagInfosOut = std::make_unique<edm::OwnVector<reco::BaseTagInfo>>();

    //    std::vector<edm::Handle<edm::View<reco::BaseTagInfo> > >  jetTagInfos;
    //    jetTagInfos.resize(BTagInfos.size());
    //    for (size_t i = 0; i < BTagInfos_.size(); ++i) {
    //      iEvent.getByToken(BTagInfos_[i], jetTagInfos[i]);
    //    }
    
    // Loop on Jet collection
    for(std::vector<pat::Jet>::const_iterator it=PFJetsCollection->begin(); it!=PFJetsCollection->end(); ++it) {

        if(Vect.size()>0) {
            PtTh=Jet2Pt;
            BTagTh=Jet2BTag;
        }
        pat::Jet jet=*it;
        int idx=it-PFJetsCollection->begin();
        jet.addUserInt("Index", idx);
        pat::JetRef jetRef(PFJetsCollection, idx);

        // First pt cut, to avoid issues with AK8!
        if(jet.pt()<PtTh) continue;
	//std::cout << "check isPFJet()" << jet.isPFJet() << std::endl;
	//std::cout << "check isJPTJet()" << jet.isJPTJet() << std::endl;
        //if( !(jet.isJPTJet() or jet.isPFJet()) ) std::cout<< " - - - - NOT VALID! SKIP!!! - - - - - " << std::endl;
        if( !(jet.isJPTJet() or jet.isPFJet()) ) continue;
	

	//First of all, jet id selections
        // Quality cut
        if(JetId==1 && !isLooseJet(jet,DataEra)) continue;
        if(JetId==2 && !isTightJet(jet,DataEra)) continue;
        if(JetId==3 && !isTightLepVetoJet(jet,DataEra)) continue;
        
        // b-tagging
        if(BTagTh==1 && jet.bDiscriminator(BTag)<BTagTh) continue;
        // Save jet ID
        jet.addUserInt("isLoose", isLooseJet(jet,DataEra) ? 1 : 0);
        jet.addUserInt("isTight", isTightJet(jet,DataEra) ? 1 : 0);
        jet.addUserInt("isTightLepVeto", isTightLepVetoJet(jet,DataEra) ? 1 : 0);
	// Save jet energy fractions as user floats, since they are affected by JER smearing
	jet.addUserFloat("cHadEFrac", jet.chargedHadronEnergyFraction());
	jet.addUserFloat("nHadEFrac", jet.neutralHadronEnergyFraction());
	jet.addUserFloat("nEmEFrac", jet.neutralEmEnergyFraction());
	jet.addUserFloat("cEmEFrac", jet.chargedEmEnergyFraction());
	jet.addUserFloat("cmuEFrac", jet.chargedMuEnergyFraction());
	jet.addUserFloat("muEFrac", jet.muonEnergyFraction());
	jet.addUserFloat("eleEFrac", jet.electronEnergyFraction());
	jet.addUserFloat("photonEFrac", jet.photonEnergyFraction());

	//std::cout << "cHadEFrac   ORIGINAL: " << jet.chargedHadronEnergyFraction()  << std::endl;
	//std::cout << "nHadEFrac   ORIGINAL: " << jet.neutralHadronEnergyFraction()  << std::endl;
	//std::cout << "nEmEFrac    ORIGINAL: " << jet.neutralEmEnergyFraction()  << std::endl;
	//std::cout << "cEmEFrac    ORIGINAL: " << jet.chargedEmEnergyFraction()  << std::endl;
	//std::cout << "cmuEFrac    ORIGINAL: " << jet.chargedMuEnergyFraction()  << std::endl;
	//std::cout << "muEFrac     ORIGINAL: " << jet.muonEnergyFraction()  << std::endl;
	//std::cout << "eleEFrac    ORIGINAL: " << jet.electronEnergyFraction()  << std::endl;
	//std::cout << "photonEFrac ORIGINAL: " << jet.photonEnergyFraction()  << std::endl;


	//	//Add TagInfos to pat jets, taken from: https://github.com/cms-sw/cmssw/blob/02d4198c0b6615287fd88e9a8ff650aea994412e/PhysicsTools/PatAlgos/plugins/PATJetUpdater.cc#L172
	//	for (size_t k=0; k<jetTagInfos.size(); ++k) {
	//	  const edm::View<reco::BaseTagInfo> & taginfos = *jetTagInfos[k];
	//	  // This is not associative, so we have to search the jet
	//	  edm::Ptr<reco::BaseTagInfo> match;
	//	  // Try first by 'same index'
	//	  if ((idx < taginfos.size()) && (taginfos[idx].jet() == jetRef)) {
	//	    match = taginfos.ptrAt(idx);
	//	  } else {
	//	    // otherwise fail back to a simple search
	//	    for (edm::View<reco::BaseTagInfo>::const_iterator itTI = taginfos.begin(), edTI = taginfos.end(); itTI != edTI; ++itTI) {
	//	      if (itTI->jet() == jetRef) { match = taginfos.ptrAt( itTI - taginfos.begin() ); break; }
	//	    }
	//	  }
	//	  if (match.isNonnull()) {
	//	    tagInfosOut->push_back( match->clone() );
	//	    // set the "forward" ptr to the thinned collection
	//	    edm::Ptr<reco::BaseTagInfo> tagInfoForwardPtr ( h_tagInfosOut.id(), &tagInfosOut->back(), tagInfosOut->size() - 1 );
	//	    // set the "backward" ptr to the original collection for association
	//	    const edm::Ptr<reco::BaseTagInfo>& tagInfoBackPtr ( match );
	//	    // make FwdPtr
	//	    TagInfoFwdPtrCollection::value_type tagInfoFwdPtr( tagInfoForwardPtr, tagInfoBackPtr ) ;
	//	    ajet.addTagInfo(tagInfoLabels_[k], tagInfoFwdPtr );
	//	  }
	//    }	


	////Already done via updateJetCollection. Kept as future reference for FW lite
        //if(RecalibrateJets) CorrectJet(jet, *rho_handle, PVCollection->size(), isMC);
	edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
	iSetup.get<JetCorrectionsRecord>().get(JECUncertaintyName,JetCorParColl); 
	JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
	JetCorrectionUncertainty *jecUnc = new JetCorrectionUncertainty(JetCorPar);
	jecUnc->setJetEta(jet.eta());
	jecUnc->setJetPt(jet.pt()); // here you must use the CORRECTED jet pt
	jet.addUserFloat("JESUncertainty", jecUnc->getUncertainty(true));

        //// JEC Uncertainty, old method
        //if (!isMC){
        //    jecUncDATA->setJetEta(jet.eta());
        //    jecUncDATA->setJetPt(jet.pt()); // here you must use the CORRECTED jet pt
        //    jet.addUserFloat("JESUncertaintyOld", jecUncDATA->getUncertainty(true));
        //} else {
        //    jecUncMC->setJetEta(jet.eta());
        //    jecUncMC->setJetPt(jet.pt()); // here you must use the CORRECTED jet pt
        //    jet.addUserFloat("JESUncertaintyOld", jecUncMC->getUncertainty(true));
        //}

	//ADD HERE JET PT UP - DOWN!
	jet.addUserFloat("ptJESUp", (   jet.hasUserFloat("JESUncertainty") ? (jet.pt() * (1+jet.userFloat("JESUncertainty")) ) : jet.pt()   ) );
	jet.addUserFloat("ptJESDown", (   jet.hasUserFloat("JESUncertainty") ? (jet.pt() * (1-jet.userFloat("JESUncertainty")) ) : jet.pt()   ) );


	//std::cout << "JES uncertainty: " << jet.userFloat("JESUncertainty") <<std::endl;
        // PUPPI soft drop mass for AK8 jets
        if(jet.hasSubjets("SoftDropPuppi")) {
//            TLorentzVector puppiSoftdrop, puppiSoftdropSubjet;
//            auto const & sdSubjetsPuppi = jet.subjets("SoftDropPuppi");
//            for (auto const & it : sdSubjetsPuppi) {
//                puppiSoftdropSubjet.SetPtEtaPhiM(it->pt(), it->eta(), it->phi(), it->mass());
//                puppiSoftdrop += puppiSoftdropSubjet;
//            }
            reco::Particle::LorentzVector puppiSoftdrop;
            for (auto const & it : jet.subjets("SoftDropPuppi")) puppiSoftdrop += it->correctedP4(0);
            jet.addUserFloat("ak8PFJetsPuppiSoftDropPt", puppiSoftdrop.pt());
            jet.addUserFloat("ak8PFJetsPuppiSoftDropEta", puppiSoftdrop.eta());
            jet.addUserFloat("ak8PFJetsPuppiSoftDropPhi", puppiSoftdrop.phi());
            jet.addUserFloat("ak8PFJetsPuppiSoftDropEnergy", puppiSoftdrop.energy());
            jet.addUserFloat("ak8PFJetsPuppiSoftDropMass", puppiSoftdrop.mass());
            
            //float tau21 = jet.userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau2")/jet.userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau1");
            float tau21 = jet.hasUserFloat("NjettinessAK8Puppi:tau2") ? jet.userFloat("NjettinessAK8Puppi:tau2")/jet.userFloat("NjettinessAK8Puppi:tau1") : -1.;
            float ddt = jet.hasUserFloat("ak8PFJetsPuppiSoftDropMass") ? tau21 + 0.063 * log( jet.userFloat("ak8PFJetsPuppiSoftDropMass")*jet.userFloat("ak8PFJetsPuppiSoftDropMass")/jet.userFloat("ak8PFJetsPuppiSoftDropPt") ) : -1.;
            jet.addUserFloat("ddtTau21", ddt);
        }
        
        //if(RecalibrateMass) CorrectMass(jet, *rho_handle, PVCollection->size(), isMC);
        //if(RecalibratePuppiMass) CorrectPuppiMass(jet, isMC);
        

        // JER NEW IMPLEMENTATION


        if(SmearJets) {//Note: use (isMC && SmearJets) to apply JER only to data

        //if(SmearJets) {
            resolution    = JME::JetResolution::get(iSetup, JerName_res);//new JME::JetResolution(JerName_res);
            resolution_sf = JME::JetResolutionScaleFactor::get(iSetup, JerName_sf);//new JME::JetResolutionScaleFactor(JerName_sf);
            if (JerName_res.find("AK8") != std::string::npos)
                Rparameter = 0.8;
            else 
                Rparameter = 0.4;
        //}

            JME::JetParameters TheJetParameters;
            TheJetParameters.setJetPt(jet.pt());
            TheJetParameters.setJetEta(jet.eta());
            TheJetParameters.setRho(*rho_handle);

	    reco::Candidate::LorentzVector unsmearedJet = jet.correctedP4(0);
	    reco::Candidate::LorentzVector smearedJet(unsmearedJet);

            float smearFactor = 1.;
            float smearFactorUp = 1.;
            float smearFactorDown = 1.;
	    float JERresolution = -1.;
	    float JERsf = -1.;
	    float JERsfUp = -1.;
	    float JERsfDown = -1.;

            if(isMC) {

                JERresolution = resolution.getResolution(TheJetParameters);
                JERsf         = resolution_sf.getScaleFactor(TheJetParameters);
                JERsfUp       = resolution_sf.getScaleFactor(TheJetParameters, Variation::UP);
                JERsfDown     = resolution_sf.getScaleFactor(TheJetParameters, Variation::DOWN);
                //std::cout << "JERresolution " << JERresolution << "\n";
                //std::cout << "JERsf         " << JERsf << "\n";
                //std::cout << "JERsfUp       " << JERsfUp << "\n";
                //std::cout << "JERsfDown     " << JERsfDown << "\n";
                const reco::GenJet* genJet=jet.genJet();
                if(genJet) {
                    if ( ( sqrt( pow(jet.eta() - genJet->eta(),2) + pow(jet.phi() - genJet->phi(),2) ) < 0.5*Rparameter )  &&
                         fabs( jet.pt() - genJet->pt()) < 3.*JERresolution*jet.pt() ) { // (DeltaR < R/2) AND (DeltaPt < 3*PtRes)
                        smearFactor = max(0.,genJet->pt()+JERsf*(jet.pt() - genJet->pt()))/jet.pt();
                        smearFactorUp = max(0.,genJet->pt()+JERsfUp*(jet.pt() - genJet->pt()))/jet.pt();
                        smearFactorDown = max(0.,genJet->pt()+JERsfDown*(jet.pt() - genJet->pt()))/jet.pt();
                    }  
                    else {
                        TRandom3 rnd(0);
                        smearFactor = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsf*JERsf-1.)));
                        smearFactorUp = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsfUp*JERsfUp-1.)));
                        smearFactorDown = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsfDown*JERsfDown-1.)));
                    }
                }
		else {
		    TRandom3 rnd(0);
		    smearFactor = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsf*JERsf-1.)));
		    smearFactorUp = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsfUp*JERsfUp-1.)));
		    smearFactorDown = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsfDown*JERsfDown-1.)));
                }
            }        
            //std::cout << "Rparameter      " << Rparameter << "\n";
            //std::cout << "smearFactor     " << smearFactor << "\n";
            //std::cout << "smearFactorUp   " << smearFactorUp << "\n";
            //std::cout << "smearFactorDown " << smearFactorDown << "\n";
	    pat::Jet jetJER     = jet;
	    pat::Jet jetJERUp   = jet;
	    pat::Jet jetJERDown = jet;
            //equivalent??//jet.setP4(jet.p4() * smearFactor);
            //equivalent??//jetJERUp.setP4(jet.p4() * smearFactorUp);
            //equivalent??//jetJERDown.setP4(jet.p4() * smearFactorDown);

            jetJER.setP4(smearedJet * smearFactor);
            jetJERUp.setP4(smearedJet * smearFactorUp);
            jetJERDown.setP4(smearedJet * smearFactorDown);

            jet.addUserFloat("ptJER", jetJER.pt());
            jet.addUserFloat("etaJER", jetJER.eta());
            jet.addUserFloat("phiJER", jetJER.phi());
            jet.addUserFloat("energyJER", jetJER.energy());
            jet.addUserFloat("ptJERUp", jetJERUp.pt());
            jet.addUserFloat("etaJERUp", jetJERUp.eta());
            jet.addUserFloat("phiJERUp", jetJERUp.phi());
            jet.addUserFloat("energyJERUp", jetJERUp.energy());
            jet.addUserFloat("ptJERDown", jetJERDown.pt());
            jet.addUserFloat("etaJERDown", jetJERDown.eta());
            jet.addUserFloat("phiJERDown", jetJERDown.phi());
            jet.addUserFloat("energyJERDown", jetJERDown.energy());

	    //Save SF in case a computation is needed in post-processing
            jet.addUserFloat("JERresolution", JERresolution);
            jet.addUserFloat("JERsf", JERsf);
            jet.addUserFloat("JERsfUp", JERsfUp);
            jet.addUserFloat("JERsfDown", JERsfDown);
            jet.addUserFloat("JERsmearFactor", smearFactor);
            jet.addUserFloat("JERsmearFactorUp", smearFactorUp);
            jet.addUserFloat("JERsmearFactorDown", smearFactorDown);



            //std::cout<< "DEBUG" << std::endl;
	    //std::cout << "Jet considered: " << idx << std::endl;
	    //std::cout << "cHadEFrac   after JER: " << jet.chargedHadronEnergyFraction()  << std::endl;
	    //std::cout << "nHadEFrac   after JER: " << jet.neutralHadronEnergyFraction()  << std::endl;
	    //std::cout << "nEmEFrac    after JER: " << jet.neutralEmEnergyFraction()  << std::endl;
	    //std::cout << "cEmEFrac    after JER: " << jet.chargedEmEnergyFraction()  << std::endl;
	    //std::cout << "cmuEFrac    after JER: " << jet.chargedMuEnergyFraction()  << std::endl;
	    //std::cout << "muEFrac     after JER: " << jet.muonEnergyFraction()  << std::endl;
	    //std::cout << "eleEFrac    after JER: " << jet.electronEnergyFraction()  << std::endl;
	    //std::cout << "photonEFrac after JER: " << jet.photonEnergyFraction()  << std::endl;

	    //std::cout << "cHadEFrac   CORRECT: " << jet.userFloat("cHadEFrac")  << std::endl;
	    //std::cout << "nHadEFrac   CORRECT: " << jet.userFloat("nHadEFrac")  << std::endl;
	    //std::cout << "nEmEFrac    CORRECT: " << jet.userFloat("nEmEFrac")  << std::endl;
	    //std::cout << "cEmEFrac    CORRECT: " << jet.userFloat("cEmEFrac")  << std::endl;
	    //std::cout << "cmuEFrac    CORRECT: " << jet.userFloat("cmuEFrac")  << std::endl;
	    //std::cout << "muEFrac     CORRECT: " << jet.userFloat("muEFrac")  << std::endl;
	    //std::cout << "eleEFrac    CORRECT: " << jet.userFloat("eleEFrac")  << std::endl;
	    //std::cout << "photonEFrac CORRECT: " << jet.userFloat("photonEFrac")  << std::endl;


            //jet.addUserFloat("smearFactor", smearFactor);
            //jet.addUserFloat("smearFactorUp", smearFactorUp);
            //jet.addUserFloat("smearFactorDown", smearFactorDown);           
        }        
        // JER NEW IMPLEMENTATION        

//         // (very)OLD Jet Energy Smearing
//         if(isMC) {
//             const reco::GenJet* genJet=jet.genJet();
//             if(genJet) {
//                 float smearFactor=GetResolutionRatio(jet.eta());
//                 reco::Candidate::LorentzVector smearedP4;
//                 smearedP4=jet.p4()-genJet->p4();
//                 smearedP4*=smearFactor; // +- 3*smearFactorErr;
//                 smearedP4+=genJet->p4();
//                 jet.setP4(smearedP4);
//             }
//         }
        

        // Pt and eta cut
        if(jet.pt()<PtTh || fabs(jet.eta())>EtaTh) continue;
	/*
	  // THE LINES BELOW WON'T WORK! Check new implementation.
	std::vector<float> reshapedDiscriminator = ReshapeBtagDiscriminator(jet);
        jet.addUserFloat("ReshapedDiscriminator", reshapedDiscriminator[0]);
        jet.addUserFloat("ReshapedDiscriminatorUp", reshapedDiscriminator[1]);
        jet.addUserFloat("ReshapedDiscriminatorDown", reshapedDiscriminator[2]);
	*/

        // CSV reshaping for soft drop subjets
	/*
        if(jet.hasSubjets("SoftDrop")) {
            auto const & sdSubjets = jet.subjets("SoftDrop");
            short nsj = 1;
            for (auto const & it : sdSubjets) {
                pat::Jet subjet = it;
		std::vector<float> reshapedDiscriminatorSubjet = ReshapeBtagDiscriminator(subjet);
                jet.addUserFloat(Form("ReshapedDiscriminator%d",nsj), reshapedDiscriminatorSubjet[0]);
                jet.addUserFloat(Form("ReshapedDiscriminatorUp%d",nsj), reshapedDiscriminatorSubjet[1]);
                jet.addUserFloat(Form("ReshapedDiscriminatorDown%d",nsj), reshapedDiscriminatorSubjet[2]);
                ++nsj;
            }
        }
        
        //QG tagger for AK4 jets
        if(AddQG && jet.nSubjetCollections()<=0) {
            jet.addUserFloat("QGLikelihood", (*QGHandle)[jetRef]);
        }
        */


        //Find ECAL/HCAL recHits
        //Initialize
        float jet_energy_frac(0.);
        float jetRechitE_Error_EB(0.);
        float jetRechitE_EB(0.);
        float jetRechitT_EB(0.);
        float jetRechitT_rms_EB(0.);
        float jetRechitX_EB(0.);
        float jetRechitY_EB(0.);
        float jetRechitZ_EB(0.);
        float jetRechitRadius_EB(0.);
        int n_matched_rechits_EB(0);
        
        float jetRechitE_Error_EE(0.);
        float jetRechitE_EE(0.);
        float jetRechitT_EE(0.);
        float jetRechitT_rms_EE(0.);
        float jetRechitX_EE(0.);
        float jetRechitY_EE(0.);
        float jetRechitZ_EE(0.);
        float jetRechitRadius_EE(0.);
        int n_matched_rechits_EE(0);
                
        //float jet_energy_frac_HBHE(0.);
        float jetRechitE_Error_HB(0.);
        float jetRechitE_HB(0.);
        float jetRechitT_HB(0.);
        float jetRechitT_rms_HB(0.);
        float jetRechitX_HB(0.);
        float jetRechitY_HB(0.);
        float jetRechitZ_HB(0.);
        float jetRechitRadius_HB(0.);
        int n_matched_rechits_HB(0);
         
        float jetRechitE_Error_HE(0.);
        float jetRechitE_HE(0.);
        float jetRechitT_HE(0.);
        float jetRechitT_rms_HE(0.);
        float jetRechitX_HE(0.);
        float jetRechitY_HE(0.);
        float jetRechitZ_HE(0.);
        float jetRechitRadius_HE(0.);
        int n_matched_rechits_HE(0);

	//vectors used to calculate hit showers spread
	std::vector<double> EB_eta;
	std::vector<double> EB_et;
	std::vector<double> EB_et_squared;
	std::vector<double> EB_phi;
	std::vector<double> EE_eta;
	std::vector<double> EE_et;
	std::vector<double> EE_et_squared;
	std::vector<double> EE_phi;
	std::vector<double> HB_eta;
	std::vector<double> HB_et;
	std::vector<double> HB_et_squared;
	std::vector<double> HB_phi;

	std::pair< std::pair<float,float> ,float> sigEB;
	std::pair< std::pair<float,float> ,float> sigEE;
	std::pair< std::pair<float,float> ,float> sigHB;

	//std::cout << " - - Jet pt: " << jet.pt() << std::endl;

        if(IsAOD)
        {
	  //Just for debugging purposes
	  jet.addUserFloat("Rparameter", Rparameter);

          //Loop on EB rec hits
          for(unsigned int q=0; q<ebRecHitsCollection->size(); q++){
            const EcalRecHit *recHit = &(*ebRecHitsCollection)[q];
            const DetId recHitId = recHit->detid();
            const auto recHitPos = barrelGeometry->getGeometry(recHitId)->getPosition();

            //Discard "bad" rechits            
            if (recHit->checkFlag(EcalRecHit::kSaturated) || recHit->checkFlag(EcalRecHit::kLeadingEdgeRecovered) || recHit->checkFlag(EcalRecHit::kPoorReco) || recHit->checkFlag(EcalRecHit::kWeird) || recHit->checkFlag(EcalRecHit::kDiWeird)) continue;
            if (recHit->timeError() < 0 || recHit->timeError() > 100) continue;
            if (abs(recHit->time()) > 12.5) continue;
            
            //Calculate jet timestamps
            if ( reco::deltaR(jet.eta(), jet.phi(), recHitPos.eta(), recHitPos.phi()) < Rparameter) {
                //if (reco::deltaR(jet.eta(), jet.phi(), recHitPos.eta(), recHitPos.phi()) < 0.15 && recHit->energy() > Rechit_cut) jet_energy_frac += recHit->energy();//needed???

                if (recHit->energy() > Rechit_cut) {

 		    EB_eta.push_back(recHitPos.eta());
		    EB_phi.push_back(recHitPos.phi());
		    EB_et.push_back(recHit->energy()/cosh(recHitPos.eta()));
		    EB_et_squared.push_back( pow(recHit->energy()/cosh(recHitPos.eta()),2) );

                    jetRechitE_Error_EB += recHit->energyError() * recHit->energyError();
                    jetRechitE_EB += recHit->energy();
                    jetRechitT_EB += recHit->time()*recHit->energy();
                    jetRechitT_rms_EB += recHit->time()*recHit->time();
                    jetRechitX_EB += recHitPos.x()*recHit->energy();
                    jetRechitY_EB += recHitPos.y()*recHit->energy();
                    jetRechitZ_EB += recHitPos.z()*recHit->energy();
                    jetRechitRadius_EB += sqrt( pow(recHitPos.x()*recHit->energy(),2) + pow(recHitPos.y()*recHit->energy(),2) );
                    n_matched_rechits_EB++;
                }
                
                
            }
            
          }//loop over ebRecHits
          
                   
          //Loop on EE rec hits
          for(unsigned int q=0; q<eeRecHitsCollection->size(); q++){
            const EcalRecHit *recHit = &(*eeRecHitsCollection)[q];
            const DetId recHitId = recHit->detid();
            const auto recHitPos = endcapGeometry->getGeometry(recHitId)->getPosition();

            //Discard "bad" rechits            
            if (recHit->checkFlag(EcalRecHit::kSaturated) || recHit->checkFlag(EcalRecHit::kLeadingEdgeRecovered) || recHit->checkFlag(EcalRecHit::kPoorReco) || recHit->checkFlag(EcalRecHit::kWeird) || recHit->checkFlag(EcalRecHit::kDiWeird)) continue;
            if (recHit->timeError() < 0 || recHit->timeError() > 100) continue;
            if (abs(recHit->time()) > 12.5) continue;
            
            //Calculate jet timestamps
            if ( reco::deltaR(jet.eta(), jet.phi(), recHitPos.eta(), recHitPos.phi()) < Rparameter) {
                //if (reco::deltaR(jet.eta(), jet.phi(), recHitPos.eta(), recHitPos.phi()) < 0.15 && recHit->energy() > Rechit_cut) jet_energy_frac += recHit->energy();//needed???

                if (recHit->energy() > Rechit_cut) {

 		    EE_eta.push_back(recHitPos.eta());
		    EE_phi.push_back(recHitPos.phi());
		    EE_et.push_back(recHit->energy()/cosh(recHitPos.eta()));
		    EE_et_squared.push_back( pow(recHit->energy()/cosh(recHitPos.eta()),2) );

                    jetRechitE_Error_EE += recHit->energyError() * recHit->energyError();
                    jetRechitE_EE += recHit->energy();
                    jetRechitT_EE += recHit->time()*recHit->energy();
                    jetRechitT_rms_EE += recHit->time()*recHit->time();
                    jetRechitX_EE += recHitPos.x()*recHit->energy();
                    jetRechitY_EE += recHitPos.y()*recHit->energy();
                    jetRechitZ_EE += recHitPos.z()*recHit->energy();
                    jetRechitRadius_EE += sqrt( pow(recHitPos.x()*recHit->energy(),2) + pow(recHitPos.y()*recHit->energy(),2) );
                    n_matched_rechits_EE++;
                }
                
                
            }
            
          }//loop over eeRecHits	  
	      
	  //loop over hcal hits
	  for (unsigned int iHit = 0; iHit < hcalRecHitsHBHECollection->size(); iHit ++){
	    const HBHERecHit *recHit = &(*hcalRecHitsHBHECollection)[iHit];

	    float hiteta = -999;
	    float hitphi = -999;
	    float hitx   = -99999999.;
	    float hity   = -99999999.;
	    float hitz   = -99999999.;
	    if (recHit->energy() < 0.1) continue;
	    const HcalDetId recHitId = recHit->detid();
	    //std::cout << "valid HCAL rec hit n. " << iHit << std::endl;
	    //std::cout << "depth " << recHitId.depth() << std::endl;
	    //std::cout << "eta id " << recHitId.ieta() << std::endl;
	    //std::cout << "phi id " << recHitId.iphi() << std::endl;
	    if (recHit->detid().subdetId() == HcalBarrel)
	      {
	        //std::cout << "Debug, segfault at HB? " << std::endl;
		const auto recHitPos = hbGeometry->getGeometry(recHitId)->getPosition();
		hiteta = recHitPos.eta();
		hitphi = recHitPos.phi();
		//std::cout << " passed id barrel " << std::endl;
		//std::cout << "eta " << hiteta  << std::endl;
		//std::cout << "phi " << hitphi  << std::endl;
		hitx   = recHitPos.x();
		hity   = recHitPos.y();
		hitz   = recHitPos.z();
	      
		if ( reco::deltaR(jet.eta(), jet.phi(), hiteta, hitphi) < Rparameter )//why 0.5??
		  {
  		    //std::cout << "Debug, segfault at matching AK4 and HB? " << std::endl;
		    //jetRechitE_Error_HBHE += recHit->energyError() * recHit->energyError();

 		    HB_eta.push_back(recHitPos.eta());
		    HB_phi.push_back(recHitPos.phi());
		    HB_et.push_back(recHit->energy()/cosh(recHitPos.eta()));
		    HB_et_squared.push_back( pow(recHit->energy()/cosh(recHitPos.eta()),2) );

		    jetRechitE_HB += recHit->energy();
		    jetRechitT_HB += recHit->time()*recHit->energy();
		    jetRechitT_rms_HB += recHit->time()*recHit->time();
		    jetRechitX_HB += hitx*recHit->energy();
		    jetRechitY_HB += hity*recHit->energy();
		    jetRechitZ_HB += hitz*recHit->energy();
		    jetRechitRadius_HB += sqrt( pow(hitx*recHit->energy(),2) + pow(hity*recHit->energy(),2) );
		    n_matched_rechits_HB++;
		  }
            
	      }
	    /*
	    else if (recHit->detid().subdetId() == HcalEndcap)
	      {
	        std::cout << "Debug, segfault at HE? " << std::endl;
		const auto recHitPos = heGeometry->getGeometry(recHitId)->getPosition();
		std::cout << "HE get position failing? " << std::endl;
		hiteta = recHitPos.eta();
		hitphi = recHitPos.phi();
		hitx   = recHitPos.x();
		hity   = recHitPos.y();
		hitz   = recHitPos.z();
	      
		if ( reco::deltaR(jet.eta(), jet.phi(), hiteta, hitphi) < Rparameter )//why 0.5??
		  {
		    std::cout << "Debug, segfault at matching AK4 and HE? " << std::endl;
		    //jetRechitE_Error_HBHE += recHit->energyError() * recHit->energyError();
		    jetRechitE_HE += recHit->energy();
		    jetRechitT_HE += recHit->time()*recHit->energy();
		    jetRechitT_rms_HE += recHit->time()*recHit->time();
		    jetRechitX_HE += hitx*recHit->energy();
		    jetRechitY_HE += hity*recHit->energy();
		    jetRechitZ_HE += hitz*recHit->energy();
		    jetRechitRadius_HE += sqrt( pow(hitx*recHit->energy(),2) + pow(hity*recHit->energy(),2) );
		    n_matched_rechits_HE++;
		  }
	      }
	    
	    else
	      {
		std::cout << "Error: HCAL Rechit has detId subdet = " << recHit->detid().subdetId() << "  which is not HcalBarrel or HcalEndcap. skipping it. \n";
	      }
	      */
            

	  }//loop over hcal hbhe hits          
          
                   
          
          
        }//IsAOD condition

	//Wrap up second momenta
	sigEB = JetAnalyzer::JetSecondMoments(EB_et, EB_eta, EB_phi);
	sigEE = JetAnalyzer::JetSecondMoments(EE_et, EE_eta, EE_phi);
	sigHB = JetAnalyzer::JetSecondMoments(HB_et, HB_eta, HB_phi);

	//std::cout << sigEB.first.first << std::endl;
	//std::cout << sigEB.first.second << std::endl;
	//std::cout << sigEB.second << std::endl;
	//std::cout<< "Check values of second moments: " << sigEB.first << sigEB.second << std::endl;

        jet.addUserInt("nRecHitsEB", n_matched_rechits_EB);
        jet.addUserFloat("timeRecHitsEB", jetRechitE_EB>0 ? jetRechitT_EB/jetRechitE_EB : -100.);
        jet.addUserFloat("timeRMSRecHitsEB", n_matched_rechits_EB>0 ? sqrt(jetRechitT_rms_EB) : -1.);
        jet.addUserFloat("energyRecHitsEB", n_matched_rechits_EB>0 ? jetRechitE_EB : -1.);
        jet.addUserFloat("energyErrorRecHitsEB", n_matched_rechits_EB>0 ? sqrt(jetRechitE_Error_EB) : -1.);
        jet.addUserFloat("xRecHitsEB", jetRechitE_EB>0 ? jetRechitX_EB/jetRechitE_EB : -1000.);
        jet.addUserFloat("yRecHitsEB", jetRechitE_EB>0 ? jetRechitY_EB/jetRechitE_EB : -1000.);
        jet.addUserFloat("zRecHitsEB", jetRechitE_EB>0 ? jetRechitZ_EB/jetRechitE_EB : -1000.);
        jet.addUserFloat("radiusRecHitsEB", jetRechitE_EB>0 ? jetRechitRadius_EB/jetRechitE_EB : -1000.);

        jet.addUserFloat("sig1EB", sigEB.first.first>0 ? sigEB.first.first : -1.);
        jet.addUserFloat("sig2EB", sigEB.first.second>0 ? sigEB.first.second : -1.);
        jet.addUserFloat("sigAvEB", (sigEB.first.first>0 and sigEB.first.second>0) ? sqrt( pow(sigEB.first.first,2) + pow(sigEB.first.second,2) ) : -1.);
        jet.addUserFloat("tan2thetaEB", sigEB.second);
	jet.addUserFloat("ptDEB", accumulate(EB_et.begin(),EB_et.end(),0) > 0 ? sqrt(accumulate(EB_et_squared.begin(),EB_et_squared.end(),0)) / accumulate(EB_et.begin(),EB_et.end(),0) : -1.);

        jet.addUserInt("nRecHitsEE", n_matched_rechits_EE);
        jet.addUserFloat("timeRecHitsEE", jetRechitE_EE>0 ? jetRechitT_EE/jetRechitE_EE : -100.);
        jet.addUserFloat("timeRMSRecHitsEE", n_matched_rechits_EE>0 ? sqrt(jetRechitT_rms_EE) : -1.);
        jet.addUserFloat("energyRecHitsEE", n_matched_rechits_EE>0 ? jetRechitE_EE : -1.);
        jet.addUserFloat("energyErrorRecHitsEE", n_matched_rechits_EE>0 ? sqrt(jetRechitE_Error_EE) : -1.);
        jet.addUserFloat("xRecHitsEE", jetRechitE_EE>0 ? jetRechitX_EE/jetRechitE_EE : -1000.);
        jet.addUserFloat("yRecHitsEE", jetRechitE_EE>0 ? jetRechitY_EE/jetRechitE_EE : -1000.);
        jet.addUserFloat("zRecHitsEE", jetRechitE_EE>0 ? jetRechitZ_EE/jetRechitE_EE : -1000.);
        jet.addUserFloat("radiusRecHitsEE", jetRechitE_EE>0 ? jetRechitRadius_EE/jetRechitE_EE : -1000.);        

        jet.addUserFloat("sig1EE", sigEE.first.first>0 ? sigEE.first.first : -1.);
        jet.addUserFloat("sig2EE", sigEE.first.second>0 ? sigEE.first.second : -1.);
        jet.addUserFloat("sigAvEE", (sigEE.first.first>0 and sigEE.first.second>0) ? sqrt( pow(sigEE.first.first,2) + pow(sigEE.first.second,2) ) : -1.);
        jet.addUserFloat("tan2thetaEE", sigEE.second);
	jet.addUserFloat("ptDEE", accumulate(EE_et.begin(),EE_et.end(),0) > 0 ? sqrt(accumulate(EE_et_squared.begin(),EE_et_squared.end(),0)) / accumulate(EE_et.begin(),EE_et.end(),0) : -1.);
        
        jet.addUserInt("nRecHitsHB", n_matched_rechits_HB);
        jet.addUserFloat("timeRecHitsHB", jetRechitE_HB>0 ? jetRechitT_HB/jetRechitE_HB : -100.);
        jet.addUserFloat("timeRMSRecHitsHB", n_matched_rechits_HB>0 ? sqrt(jetRechitT_rms_HB) : -1.);
        jet.addUserFloat("energyRecHitsHB", n_matched_rechits_HB>0 ? jetRechitE_HB : -1.);
        jet.addUserFloat("energyErrorRecHitsHB", n_matched_rechits_HB>0 ? sqrt(jetRechitE_Error_HB) : -1.);
        jet.addUserFloat("xRecHitsHB", jetRechitE_HB>0 ? jetRechitX_HB/jetRechitE_HB : -1000.);
        jet.addUserFloat("yRecHitsHB", jetRechitE_HB>0 ? jetRechitY_HB/jetRechitE_HB : -1000.);
        jet.addUserFloat("zRecHitsHB", jetRechitE_HB>0 ? jetRechitZ_HB/jetRechitE_HB : -1000.);
        jet.addUserFloat("radiusRecHitsHB", jetRechitE_HB>0 ? jetRechitRadius_HB/jetRechitE_HB : -1000.);

        jet.addUserFloat("sig1HB", sigHB.first.first>0 ? sigHB.first.first : -1.);
        jet.addUserFloat("sig2HB", sigHB.first.second>0 ? sigHB.first.second : -1.);
        jet.addUserFloat("sigAvHB", (sigHB.first.first>0 and sigHB.first.second>0) ? sqrt( pow(sigHB.first.first,2) + pow(sigHB.first.second,2) ) : -1.);
        jet.addUserFloat("tan2thetaHB", sigHB.second);
	jet.addUserFloat("ptDHB", accumulate(HB_et.begin(),HB_et.end(),0) > 0 ? sqrt(accumulate(HB_et_squared.begin(),HB_et_squared.end(),0)) / accumulate(HB_et.begin(),HB_et.end(),0) : -1.);

        /*
        jet.addUserInt("nRecHitsHE", n_matched_rechits_HE);
        jet.addUserFloat("timeRecHitsHE", jetRechitE_HE>0 ? jetRechitT_HE/jetRechitE_HE : -100.);
        jet.addUserFloat("timeRMSRecHitsHE", n_matched_rechits_HE>0 ? sqrt(jetRechitT_rms_HE) : -1.);
        jet.addUserFloat("energyRecHitsHE", n_matched_rechits_HE>0 ? jetRechitE_HE : -1.);
        jet.addUserFloat("energyErrorRecHitsHE", n_matched_rechits_HE>0 ? sqrt(jetRechitE_Error_HE) : -1.);
        jet.addUserFloat("xRecHitsHE", jetRechitE_HE>0 ? jetRechitX_HE/jetRechitE_HE : -1000.);
        jet.addUserFloat("yRecHitsHE", jetRechitE_HE>0 ? jetRechitY_HE/jetRechitE_HE : -1000.);
        jet.addUserFloat("zRecHitsHE", jetRechitE_HE>0 ? jetRechitZ_HE/jetRechitE_HE : -1000.);
        jet.addUserFloat("radiusRecHitsHE", jetRechitE_HE>0 ? jetRechitRadius_HE/jetRechitE_HE : -1000.);        
	*/
        Vect.push_back(jet); // Fill vector
    }

    return Vect;
}


/////////////////////////////////////////////
//obsolete, kept only as future reference for FWLite
/*
void JetAnalyzer::CorrectJet(pat::Jet& jet, float rho, float nPV, bool isMC) {
    double corr(1.);
    reco::Candidate::LorentzVector uncorrJet = jet.correctedP4(0);
    
    if(!isMC) {
        jetCorrDATA->setJetEta( uncorrJet.Eta() );
        jetCorrDATA->setJetPt ( uncorrJet.Pt() );
        jetCorrDATA->setJetE  ( uncorrJet.E() );
        jetCorrDATA->setJetA  ( jet.jetArea() );
        jetCorrDATA->setRho   ( rho );
        jetCorrDATA->setNPV   ( nPV );
        corr = jetCorrDATA->getCorrection();
    }
    else {
        jetCorrMC->setJetEta( uncorrJet.Eta() );
        jetCorrMC->setJetPt ( uncorrJet.Pt() );
        jetCorrMC->setJetE  ( uncorrJet.E() );
        jetCorrMC->setJetA  ( jet.jetArea() );
        jetCorrMC->setRho   ( rho );
        jetCorrMC->setNPV   ( nPV );
        corr = jetCorrMC->getCorrection();
    }

    reco::Candidate::LorentzVector corrJet(uncorrJet);
    jet.setP4(corrJet * corr);

}

void JetAnalyzer::CorrectMass(pat::Jet& jet, float rho, float nPV, bool isMC) {
    double corr(1.);
    reco::Candidate::LorentzVector uncorrJet = jet.correctedP4(0);
    
    if(!isMC) {
        massCorrDATA->setJetEta( uncorrJet.Eta() );
        massCorrDATA->setJetPt ( uncorrJet.Pt() );
        massCorrDATA->setJetE  ( uncorrJet.E() );
        massCorrDATA->setJetA  ( jet.jetArea() );
        massCorrDATA->setRho   ( rho );
        massCorrDATA->setNPV   ( nPV );
        corr = massCorrDATA->getCorrection();
    }
    else {
        massCorrMC->setJetEta( uncorrJet.Eta() );
        massCorrMC->setJetPt ( uncorrJet.Pt() );
        massCorrMC->setJetE  ( uncorrJet.E() );
        massCorrMC->setJetA  ( jet.jetArea() );
        massCorrMC->setRho   ( rho );
        massCorrMC->setNPV   ( nPV );
        corr = massCorrMC->getCorrection();
    }
    if(jet.hasUserFloat("ak8PFJetsCHSPrunedMass")) jet.addUserFloat("ak8PFJetsCHSPrunedMassCorr", jet.userFloat("ak8PFJetsCHSPrunedMass") * corr);
    if(jet.hasUserFloat("ak8PFJetsCHSSoftDropMass")) jet.addUserFloat("ak8PFJetsCHSSoftDropMassCorr", jet.userFloat("ak8PFJetsCHSSoftDropMass") * corr);
    if(jet.hasUserFloat("ak8PFJetsPrunedMass")) jet.addUserFloat("ak8PFJetsPrunedMassCorr", jet.userFloat("ak8PFJetsPrunedMass") * corr);
    if(jet.hasUserFloat("ak8PFJetsSoftDropMass")) jet.addUserFloat("ak8PFJetsSoftDropMassCorr", jet.userFloat("ak8PFJetsSoftDropMass") * corr);
    //if(jet.hasUserFloat("ak8PFJetsPuppiSoftDropMass")) jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorr", jet.userFloat("ak8PFJetsPuppiSoftDropMass") * corr);
}


void JetAnalyzer::CorrectPuppiMass(pat::Jet& jet, bool isMC) {
    bool hasInfo( jet.hasUserFloat(SoftdropPuppiMassString) && jet.hasUserFloat("ak8PFJetsPuppiSoftDropPt") && jet.hasUserFloat("ak8PFJetsPuppiSoftDropEta") );
    float corr(1.), genCorr(1.), recoCorr(1.);
    if(hasInfo && jet.userFloat(SoftdropPuppiMassString) > 0.) {
        genCorr = PuppiJECcorr_gen->Eval( jet.userFloat("ak8PFJetsPuppiSoftDropPt") );
        if(fabs(jet.userFloat("ak8PFJetsPuppiSoftDropEta")) <= 1.3) 
            recoCorr = PuppiJECcorr_reco_0eta1v3->Eval( jet.userFloat("ak8PFJetsPuppiSoftDropPt") );
        else if(fabs(jet.userFloat("ak8PFJetsPuppiSoftDropEta")) > 1.3 ) 
            recoCorr = PuppiJECcorr_reco_1v3eta2v5->Eval( jet.userFloat("ak8PFJetsPuppiSoftDropPt") );
        corr = genCorr * recoCorr;
    }
    if(corr < 0.) corr = 0.;
    jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorr", jet.hasUserFloat(SoftdropPuppiMassString) ? jet.userFloat(SoftdropPuppiMassString) * corr : -1.);
    jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrNotSmeared", jet.hasUserFloat(SoftdropPuppiMassString) ? jet.userFloat(SoftdropPuppiMassString) * corr : -1.);

    if(isMC){
      float JMSSf  = 1.;//Moriond17
        float JMSUnc = 0.0094;//Moriond17
        float JESUnc = jet.userFloat("JESUncertainty");    
        jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrJMS", jet.userFloat("ak8PFJetsPuppiSoftDropMassCorr")       * JMSSf);
        jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrJMSUp", jet.userFloat("ak8PFJetsPuppiSoftDropMassCorr")     * (JMSSf + sqrt(JMSUnc*JMSUnc + JESUnc*JESUnc) ) );
        jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrJMSDown", jet.userFloat("ak8PFJetsPuppiSoftDropMassCorr")   * (JMSSf - sqrt(JMSUnc*JMSUnc + JESUnc*JESUnc) ) );
        
        float JMRSf   = 1.;//Moriond17
        float JMRUnc  = 0.20;//Moriond17
        TRandom3 rnd(0);
        float smearJMR    = rnd.Gaus(1.,JMRSf-1.);
        float smearJMRUp    = rnd.Gaus(1.,(JMRSf-1.)*(1. + JMRUnc/JMRSf));
	float smearJMRDown    = rnd.Gaus(1.,(JMRSf -1.)*(1. - JMRUnc/JMRSf));
        jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrJMR", jet.userFloat("ak8PFJetsPuppiSoftDropMassCorr")       * smearJMR);
        jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrJMRUp", jet.userFloat("ak8PFJetsPuppiSoftDropMassCorr")     * smearJMRUp);
        jet.addUserFloat("ak8PFJetsPuppiSoftDropMassCorrJMRDown", jet.userFloat("ak8PFJetsPuppiSoftDropMassCorr")   * smearJMRDown);
    }
}
*/

void JetAnalyzer::CleanJetsFromMuons(std::vector<pat::Jet>& Jets, std::vector<pat::Muon>& Muons, float angle) {
    for(unsigned int m = 0; m < Muons.size(); m++) {
        for(unsigned int j = 0; j < Jets.size(); ) {
            if(deltaR(Jets[j], Muons[m]) < angle) Jets.erase(Jets.begin() + j);
            else j++;
        }
    }
}

void JetAnalyzer::CleanJetsFromElectrons(std::vector<pat::Jet>& Jets, std::vector<pat::Electron>& Electrons, float angle) {
    for(unsigned int e = 0; e < Electrons.size(); e++) {
        for(unsigned int j = 0; j < Jets.size(); ) {
            if(deltaR(Jets[j], Electrons[e]) < angle) Jets.erase(Jets.begin() + j);
            else j++;
        }
    }
}

void JetAnalyzer::CleanFatJetsFromAK4(std::vector<pat::Jet>& FatJets, std::vector<pat::Jet>& AK4Jets, float angle) {
  for(unsigned int a = 0; a < AK4Jets.size(); a++){
    for(unsigned int f = 0; f < FatJets.size(); ) {
      if(deltaR(FatJets[f], AK4Jets[a]) < angle) FatJets.erase(FatJets.begin() + f);
      else f++;
    }
  }
}

void JetAnalyzer::AddVariables(std::vector<pat::Jet>& Jets, pat::MET& MET) {
    for(unsigned int j = 0; j < Jets.size(); j++) {
        Jets[j].addUserFloat("dPhi_met", fabs(reco::deltaPhi(Jets[j].phi(), MET.phi())));
        Jets[j].addUserFloat("dPhi_Jet1", fabs(reco::deltaPhi(Jets[j].phi(), Jets[0].phi())));
    }
}

void JetAnalyzer::GenMatcher(std::vector<pat::Jet>& Jets, std::vector<reco::GenParticle>& Quarks, std::string label) {
    for(unsigned int j = 0; j < Jets.size(); j++){
        for(unsigned int q = 0; q < Quarks.size(); q++) {
	  //std::cout << "jet: " << j << " quark: " << q << " delta R: " <<fabs(reco::deltaR(Jets[j].eta(),Jets[j].phi(),Quarks[q].eta(),Quarks[q].phi()) ) << std::endl;
	  //std::cout << ("dR_q"+std::to_string(q)).c_str() << std::endl;
	  //std::cout <<  ("dR_"+label+std::to_string(q+1)).c_str() << std::endl;
	  Jets[j].addUserFloat(("dR_"+label+std::to_string(q+1)).c_str(), fabs(reco::deltaR(Jets[j].eta(),Jets[j].phi(),Quarks[q].eta(),Quarks[q].phi())) );
	  if(Jets[j].hasSubjets("SoftDrop"))
	     {
	       if(Jets[j].subjets("SoftDrop").size() > 0) Jets[j].addUserFloat(("dR_"+label+std::to_string(q+1)+"_sj1").c_str(), fabs(reco::deltaR(Jets[j].subjets("SoftDrop")[0]->eta(),Jets[j].subjets("SoftDrop")[0]->phi(),Quarks[q].eta(),Quarks[q].phi())) );
	       if(Jets[j].subjets("SoftDrop").size() > 1) Jets[j].addUserFloat(("dR_"+label+std::to_string(q+1)+"_sj2").c_str(), fabs(reco::deltaR(Jets[j].subjets("SoftDrop")[1]->eta(),Jets[j].subjets("SoftDrop")[1]->phi(),Quarks[q].eta(),Quarks[q].phi())) );
	     }
            //Jets[j].addUserFloat("quark_index", fabs(reco::deltaPhi(Jets[j].phi(), Jets[0].phi())));
	}
    }
}

/* nice prototype, do not delete!
std::map<std::string,float> JetAnalyzer::RecoGenMatcher(std::vector<reco::PFJet>& Jets, std::vector<reco::GenParticle>& Quarks, std::string label) {
    std::map<std::string,float> mappa;
    for(unsigned int j = 0; j < Jets.size(); j++) {
        for(unsigned int q = 0; q < Quarks.size(); q++) {
	  //std::cout << "jet: " << j << " quark: " << q << " delta R: " <<fabs(reco::deltaR(Jets[j].eta(),Jets[j].phi(),Quarks[q].eta(),Quarks[q].phi()) ) << std::endl;
	  //std::cout << ("dR_q"+std::to_string(q)).c_str() << std::endl;
	  //std::cout <<  ("dR_"+label+std::to_string(q+1)).c_str() << std::endl;
	  mappa.insert(std::make_pair(("dR_"+label+std::to_string(q+1)).c_str(), fabs(reco::deltaR(Jets[j].eta(),Jets[j].phi(),Quarks[q].eta(),Quarks[q].phi())) ));
	  //Jets[j].addUserFloat(("dR_"+label+std::to_string(q+1)).c_str(), fabs(reco::deltaR(Jets[j].eta(),Jets[j].phi(),Quarks[q].eta(),Quarks[q].phi())) );
            //Jets[j].addUserFloat("quark_index", fabs(reco::deltaPhi(Jets[j].phi(), Jets[0].phi())));
        }
    }
    return mappa;
}
*/

int JetAnalyzer::GetNBJets(std::vector<pat::Jet>& Jets) {
    int n(0);
    for(unsigned int i = 0; i < Jets.size(); i++) if(abs(Jets[i].hadronFlavour()) == 5) n++;
    return n;
}


float JetAnalyzer::GetMetTriggerEfficiency(pat::MET& MET) {
    if(!isMetTriggerFile) return 1.;
    double pt = std::min( std::max( MetTriggerHisto->GetXaxis()->GetXmin(), MET.pt() ) , MetTriggerHisto->GetXaxis()->GetXmax() - 0.000001 );
    return(MetTriggerHisto->Interpolate(pt));
}

pat::MET JetAnalyzer::FillMetVector(const edm::Event& iEvent) {
    
    edm::Handle<std::vector<pat::MET> > MetCollection;
    iEvent.getByToken(MetToken, MetCollection);
    pat::MET MEt = MetCollection->front();
    MEt.addUserFloat("ptShiftJetResUp", MEt.shiftedPt(pat::MET::METUncertainty::JetResUp));
    MEt.addUserFloat("ptShiftJetResDown", MEt.shiftedPt(pat::MET::METUncertainty::JetResDown));
    MEt.addUserFloat("ptShiftJetEnUp", MEt.shiftedPt(pat::MET::METUncertainty::JetEnUp));
    MEt.addUserFloat("ptShiftJetEnDown", MEt.shiftedPt(pat::MET::METUncertainty::JetEnDown));

    //MEt.addUserFloat("ptShiftJetResUpSmear", MEt.shiftedPt(pat::MET::METUncertainty::JetResUpSmear));
    //MEt.addUserFloat("ptShiftJetResDownSmear", MEt.shiftedPt(pat::MET::METUncertainty::JetResDownSmear));
    MEt.addUserFloat("ptShiftMuonEnUp", MEt.shiftedPt(pat::MET::METUncertainty::MuonEnUp));
    MEt.addUserFloat("ptShiftMuonEnDown", MEt.shiftedPt(pat::MET::METUncertainty::MuonEnDown));
    MEt.addUserFloat("ptShiftElectronEnUp", MEt.shiftedPt(pat::MET::METUncertainty::ElectronEnUp));
    MEt.addUserFloat("ptShiftElectronEnDown", MEt.shiftedPt(pat::MET::METUncertainty::ElectronEnDown));
    MEt.addUserFloat("ptShiftTauEnUp", MEt.shiftedPt(pat::MET::METUncertainty::TauEnUp));
    MEt.addUserFloat("ptShiftTauEnDown", MEt.shiftedPt(pat::MET::METUncertainty::TauEnDown));
    MEt.addUserFloat("ptShiftPhotonEnUp", MEt.shiftedPt(pat::MET::METUncertainty::PhotonEnUp));
    MEt.addUserFloat("ptShiftPhotonEnDown", MEt.shiftedPt(pat::MET::METUncertainty::PhotonEnDown));
    MEt.addUserFloat("ptShiftNoShift", MEt.shiftedPt(pat::MET::METUncertainty::NoShift));
    //MEt.addUserFloat("ptShiftMETUncertaintySize", MEt.shiftedPt(pat::MET::METUncertainty::METUncertaintySize));
    //MEt.addUserFloat("ptShiftMETFullUncertaintySize", MEt.shiftedPt(pat::MET::METUncertainty::METFullUncertaintySize));

    MEt.addUserFloat("ptShiftUnclusteredEnUp", MEt.shiftedPt(pat::MET::METUncertainty::UnclusteredEnUp));
    MEt.addUserFloat("ptShiftUnclusteredEnDown", MEt.shiftedPt(pat::MET::METUncertainty::UnclusteredEnDown));
    MEt.addUserFloat("ptRaw", MEt.uncorPt());
    MEt.addUserFloat("phiRaw", MEt.uncorPhi());
    return MEt;
}


void JetAnalyzer::ApplyRecoilCorrections(pat::MET& MET, const reco::Candidate::LorentzVector* GenV, const reco::Candidate::LorentzVector* RecoV, int nJets) {
    double MetPt(MET.pt()), MetPhi(MET.phi()), MetPtScaleUp(MET.pt()), MetPhiScaleUp(MET.phi()), MetPtScaleDown(MET.pt()), MetPhiScaleDown(MET.phi()), MetPtResUp(MET.pt()), MetPhiResUp(MET.phi()), MetPtResDown(MET.pt()), MetPhiResDown(MET.phi());
    double GenPt(0.), GenPhi(0.), LepPt(0.), LepPhi(0.), LepPx(0.), LepPy(0.);
    double RecoilX(0.), RecoilY(0.), Upara(0.), Uperp(0.);
    
    if(GenV) {
        GenPt = GenV->pt();
        GenPhi = GenV->phi();
    }
    else {
        throw cms::Exception("JetAnalyzer", "GenV boson is null. No Recoil Correction can be derived");
        return;
    }
    
    if(RecoV) {
        LepPt = RecoV->pt();
        LepPhi = RecoV->phi();
        LepPx = RecoV->px();
        LepPy = RecoV->py();
        RecoilX = - MET.px() - LepPx;
        RecoilY = - MET.py() - LepPy;
        Upara = (RecoilX*LepPx + RecoilY*LepPy) / LepPt;
        Uperp = (RecoilX*LepPy - RecoilY*LepPx) / LepPt;
    }
    
    // Apply Recoil Corrections
    if(UseRecoil) {
        recoilCorr->CorrectType2(MetPt,          MetPhi,          GenPt, GenPhi, LepPt, LepPhi, Upara, Uperp,  0,  0, nJets);
        recoilCorr->CorrectType2(MetPtScaleUp,   MetPhiScaleUp,   GenPt, GenPhi, LepPt, LepPhi, Upara, Uperp,  3,  0, nJets);
        recoilCorr->CorrectType2(MetPtScaleDown, MetPhiScaleDown, GenPt, GenPhi, LepPt, LepPhi, Upara, Uperp, -3,  0, nJets);
        recoilCorr->CorrectType2(MetPtResUp,     MetPhiResUp,     GenPt, GenPhi, LepPt, LepPhi, Upara, Uperp,  0,  3, nJets);
        recoilCorr->CorrectType2(MetPtResDown,   MetPhiResDown,   GenPt, GenPhi, LepPt, LepPhi, Upara, Uperp,  0, -3, nJets);
    }
    
    // Set userFloats for systematics
    MET.addUserFloat("ptScaleUp", MetPtScaleUp);
    MET.addUserFloat("ptScaleDown", MetPtScaleDown);
    MET.addUserFloat("ptResUp", MetPtResUp);
    MET.addUserFloat("ptResDown", MetPtResDown);
    
    // Set new P4
    MET.setP4(reco::Candidate::PolarLorentzVector(MetPt, MET.eta(), MetPhi, MET.mass()));
}


float JetAnalyzer::CalculateHT(const edm::Event& iEvent, const edm::EventSetup& iSetup, int id, float pt, float eta, bool smear) {

    std::vector<pat::Jet> Vect;
    // Declare and open collection
    edm::Handle<std::vector<pat::Jet> > PFJetsCollection;
    iEvent.getByToken(JetToken, PFJetsCollection);
    
    // Vertex collection
    edm::Handle<reco::VertexCollection> PVCollection;
    iEvent.getByToken(VertexToken, PVCollection);
    
    // Rho handle
    edm::Handle<double> rho_handle;
    iEvent.getByToken(RhoToken, rho_handle);
 
    bool isMC(!iEvent.isRealData());

    //Eta and pt thresholds most commonly used for HT
    float HT = 0.;
    int JetId = id;//common setting: 2, tight jets
    float PtTh = pt;//common setting: 15 GeV
    float EtaTh = eta;//common setting: 3

    // Loop on Jet collection
    for(std::vector<pat::Jet>::const_iterator it=PFJetsCollection->begin(); it!=PFJetsCollection->end(); ++it) {

        pat::Jet jet=*it;
        //int idx=it-PFJetsCollection->begin();
        //jet.addUserInt("Index", idx);
        //pat::JetRef jetRef(PFJetsCollection, idx);

	//First of all, jet id selections
        // Quality cut
        if(JetId==2 && !isTightJet(jet,DataEra)) continue;
        if(JetId==1 && !isLooseJet(jet,DataEra)) continue;
	//obsolete
        ////if(RecalibrateJets) CorrectJet(jet, *rho_handle, PVCollection->size(), isMC);

        // JEC Uncertainty
        //if (!isMC){
        //    jecUncDATA->setJetEta(jet.eta());
        //    jecUncDATA->setJetPt(jet.pt()); // here you must use the CORRECTED jet pt
        //} else {
        //    jecUncMC->setJetEta(jet.eta());
        //    jecUncMC->setJetPt(jet.pt()); // here you must use the CORRECTED jet pt
        //}
	//obsolete
        ////if(RecalibrateMass) CorrectMass(jet, *rho_handle, PVCollection->size(), isMC);

        // JER NEW IMPLEMENTATION
	
        //if(SmearJets) {//Note: use (isMC && SmearJets) to apply JER only to data
        if(smear) {//Note: use (isMC && SmearJets) to apply JER only to data
            resolution    = JME::JetResolution::get(iSetup, JerName_res);//new JME::JetResolution(JerName_res);
            resolution_sf = JME::JetResolutionScaleFactor::get(iSetup, JerName_sf);//new JME::JetResolutionScaleFactor(JerName_sf);
            if (JerName_res.find("AK8") != std::string::npos)
                Rparameter = 0.8;
            else
                Rparameter = 0.4;

            JME::JetParameters TheJetParameters;
            TheJetParameters.setJetPt(jet.pt());
            TheJetParameters.setJetEta(jet.eta());
            TheJetParameters.setRho(*rho_handle);

            float smearFactor = 1.;

            if(isMC) {
                //float JERresolution = resolution->getResolution(TheJetParameters);
                //float JERsf         = resolution_sf->getScaleFactor(TheJetParameters);
                
                float JERresolution = resolution.getResolution(TheJetParameters);
                float JERsf         = resolution_sf.getScaleFactor(TheJetParameters);
                
                const reco::GenJet* genJet=jet.genJet();
                if(genJet) {
                    if ( ( sqrt( pow(jet.eta() - genJet->eta(),2) + pow(jet.phi() - genJet->phi(),2) ) < 0.5*Rparameter )  &&
                         fabs( jet.pt() - genJet->pt()) < 3.*JERresolution*jet.pt() ) { // (DeltaR < R/2) AND (DeltaPt < 3*PtRes)
                        smearFactor = max(0.,genJet->pt()+JERsf*(jet.pt() - genJet->pt()))/jet.pt();
                    }  
                    else {
                        TRandom3 rnd(0);
                        smearFactor = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsf*JERsf-1.)));
                    }
                }
		else {
		    TRandom3 rnd(0);
		    smearFactor = 1. + rnd.Gaus(0.,JERresolution*sqrt(max(0.,JERsf*JERsf-1.)));
                }
            }        
            jet.setP4(jet.p4() * smearFactor);
        }        

        if(jet.pt()<PtTh || fabs(jet.eta())>EtaTh) continue;
	HT += jet.pt();
    }
    return HT;
}


std::vector<ecalRecHitType> JetAnalyzer::FillEcalRecHitVector(const edm::Event& iEvent, const edm::EventSetup& iSetup, std::vector<pat::Jet>& Jets) {

    // ECAL rechits
    edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > ebRecHitsCollection;
    iEvent.getByToken(ebRecHitsToken, ebRecHitsCollection);    
    //edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > eeRecHitsCollection;
    //iEvent.getByToken(eeRecHitsToken, eeRecHitsCollection);
    edm::ESHandle<CaloGeometry> geoHandle;
    iSetup.get<CaloGeometryRecord>().get(geoHandle);
    const CaloSubdetectorGeometry *barrelGeometry = geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalBarrel);
    //const CaloSubdetectorGeometry *endcapGeometry = geoHandle->getSubdetectorGeometry(DetId::Ecal, EcalEndcap);

    std::vector<ecalRecHitType> Vect;

    //First loop on the rec hits, that are a larger collection
    //Then loop over surviving jets, that are less
    //for(unsigned int a = 0; a<Jets.size(); a++)
    //  {
    //  }

    
    if(IsAOD)
      {
	//Loop on EB rec hits
	for(unsigned int q=0; q<ebRecHitsCollection->size(); q++)
	  {
	    const EcalRecHit *recHit = &(*ebRecHitsCollection)[q];
	    const DetId recHitId = recHit->detid();
	    const auto recHitPos = barrelGeometry->getGeometry(recHitId)->getPosition();
	    ecalRecHitType recHitStruct;

	    //Discard "bad" rechits            
	    if (recHit->checkFlag(EcalRecHit::kSaturated) || recHit->checkFlag(EcalRecHit::kLeadingEdgeRecovered) || recHit->checkFlag(EcalRecHit::kPoorReco) || recHit->checkFlag(EcalRecHit::kWeird) || recHit->checkFlag(EcalRecHit::kDiWeird)) continue;
	    if (recHit->timeError() < 0 || recHit->timeError() > 100) continue;
	    if (abs(recHit->time()) > 12.5) continue;
            

	    //Jet matching
	    for(unsigned int a = 0; a<Jets.size(); a++)
	      {
		//if(a==1 and Jets.at(a).pt()>=242 and Jets.at(a).pt()<250) std::cout<< "THIS jet n.1! " <<  Jets.at(a).pt()   << std::endl;
		if (reco::deltaR(Jets.at(a).eta(), Jets.at(a).phi(), recHitPos.eta(), recHitPos.phi()) < dRMatch)
		  {
		    //if(a==1 and Jets.at(a).pt()>=242 and Jets.at(a).pt()<250) std::cout<< "Rec hit: " << recHit->energy()  << std::endl;
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
			recHitStruct.jetPt = Jets.at(a).pt(); 
			recHitStruct.jetIndex = a; 
			recHitStruct.jetDR = reco::deltaR(Jets.at(a).eta(), Jets.at(a).phi(), recHitPos.eta(), recHitPos.phi()); 
			Vect.push_back(recHitStruct);
		      }//valid rec hit
		  }//matched rec hit
	      }//loop on jets
	  }//loop on rec hits
      }//if AOD
    
    return Vect;

}


std::vector<hcalRecHitType> JetAnalyzer::FillHcalRecHitVector(const edm::Event& iEvent, const edm::EventSetup& iSetup, std::vector<pat::Jet>& Jets) {

    //hereeee
    // HCAL rechits
    //edm::Handle<edm::SortedCollection<HORecHit,edm::StrictWeakOrdering<HORecHit>>> hcalRecHitsHOCollection;
    //iEvent.getByToken(hcalRecHitsHOToken, hcalRecHitsHOCollection);
    edm::Handle<edm::SortedCollection<HBHERecHit,edm::StrictWeakOrdering<HBHERecHit>>> hcalRecHitsHBHECollection;
    iEvent.getByToken(hcalRecHitsHBHEToken, hcalRecHitsHBHECollection);

    edm::ESHandle<CaloGeometry> geoHandle;
    iSetup.get<CaloGeometryRecord>().get(geoHandle);
    const CaloSubdetectorGeometry *hbGeometry = geoHandle->getSubdetectorGeometry(DetId::Hcal, HcalBarrel);
    //const CaloSubdetectorGeometry *heGeometry = geoHandle->getSubdetectorGeometry(DetId::Hcal, HcalEndcap);
    //const CaloSubdetectorGeometry *hoGeometry = geoHandle->getSubdetectorGeometry(DetId::Hcal, HcalOuter);

    std::vector<hcalRecHitType> Vect;

    
    if(IsAOD)
      {
	//Loop on HB rec hits
	for(unsigned int q=0; q<hcalRecHitsHBHECollection->size(); q++)
	  {
	    const HBHERecHit *recHit = &(*hcalRecHitsHBHECollection)[q];
	    hcalRecHitType recHitStruct;

	    //Discard "bad" rechits            
	    if (recHit->energy() < 0.1) continue;
            const HcalDetId recHitId = recHit->detid();
	    if (recHit->detid().subdetId() == HcalBarrel)
	      {
		const auto recHitPos = hbGeometry->getGeometry(recHitId)->getPosition();

		//Jet matching
		for(unsigned int a = 0; a<Jets.size(); a++)
		  {
		    if (reco::deltaR(Jets.at(a).eta(), Jets.at(a).phi(), recHitPos.eta(), recHitPos.phi()) < dRMatch)
		      {
			recHitStruct.eta = recHitPos.eta();
			recHitStruct.phi = recHitPos.phi();
			recHitStruct.x = recHitPos.x();
			recHitStruct.y = recHitPos.y();
			recHitStruct.z = recHitPos.z();
			recHitStruct.energy = recHit->energy();
			recHitStruct.time = recHit->time();
			recHitStruct.depth = recHitId.depth();
			recHitStruct.iEta = recHitId.ieta();
			recHitStruct.iPhi = recHitId.iphi();
			recHitStruct.jetPt = Jets.at(a).pt(); 
			recHitStruct.jetIndex = a; 
			recHitStruct.jetDR = reco::deltaR(Jets.at(a).eta(), Jets.at(a).phi(), recHitPos.eta(), recHitPos.phi()); 
			Vect.push_back(recHitStruct);			
		      }//if DR matching
		  }//loop on Jets

	      }//select only HcalBarrel

	  }//loop on hcal rec hits
      }//isAOD

    return Vect;

}

std::pair< std::pair<float,float>  , float> JetAnalyzer::JetSecondMoments(std::vector<double> &et,std::vector<double> &eta,std::vector<double> &phi) {
  
  float tan2theta = -99999999.;
  float sig1 = -1.0;
  float sig2 = -1.0;
  float mean_eta = 0.0;
  float mean_phi = 0.0;
  float et_squared = 0.0;
  for(unsigned int i = 0;i < eta.size();i++)
    {
      mean_eta += float(et[i]*et[i]*eta[i]);
      mean_phi += float(et[i]*et[i]*phi[i]);
      et_squared += float(et[i]*et[i]);
    }
  mean_eta = mean_eta/et_squared;
  mean_phi = mean_phi/et_squared;

  float m11(0.0),m22(0.0),m12(0.0);
  for(unsigned int i = 0;i < eta.size();i++)
    {
      m11 += et[i]*et[i]*(eta[i]-mean_eta)*(eta[i]-mean_eta);
      m22 += et[i]*et[i]*(phi[i]-mean_phi)*(phi[i]-mean_phi);
      m12 += et[i]*et[i]*(phi[i]-mean_phi)*(eta[i]-mean_eta);
    }
  float a = (m11+m22)/2;
  float b = 0.5*sqrt(pow(m11+m22,2)-4*(m11*m22-m12*m12));
  sig1 = sqrt(abs(a+b)/et_squared);
  sig2 = sqrt(abs(a-b)/et_squared);
  tan2theta = abs(m11-m22)>0 ? (2*m12)/(m11-m22) : -99999999.;//https://arxiv.org/pdf/1306.6291.pdf
  std::pair<float,float> sig;
  sig.first  = sig1;
  sig.second = sig2;
  return std::pair< std::pair<float,float>, float>(sig, tan2theta);
}

// // https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution
// float JetAnalyzer::GetResolutionRatio(float eta) {
//     eta=fabs(eta);
//     if(eta>=0.0 && eta<0.5) return 1.122; 
//     if(eta>=0.5 && eta<0.8) return 1.167;
//     if(eta>=0.8 && eta<1.1) return 1.168;
//     if(eta>=1.1 && eta<1.3) return 1.029;
//     if(eta>=1.3 && eta<1.7) return 1.115;
//     if(eta>=1.7 && eta<1.9) return 1.041;
//     if(eta>=1.9 && eta<2.1) return 1.167;
//     if(eta>=2.1 && eta<2.3) return 1.094;
//     if(eta>=2.3 && eta<2.5) return 1.168;
//     if(eta>=2.5 && eta<2.8) return 1.266;
//     if(eta>=2.8 && eta<3.0) return 1.595;
//     if(eta>=3.0 && eta<3.2) return 0.998;
//     if(eta>=3.2 && eta<5.0) return 1.226;
//     return -1.;
// }
// float JetAnalyzer::GetResolutionErrorUp(float eta) {
//     eta=fabs(eta);
//     if(eta>=0.0 && eta<0.5) return 1.122 + 0.026; 
//     if(eta>=0.5 && eta<0.8) return 1.167 + 0.048;
//     if(eta>=0.8 && eta<1.1) return 1.168 + 0.046;
//     if(eta>=1.1 && eta<1.3) return 1.029 + 0.066;
//     if(eta>=1.3 && eta<1.7) return 1.115 + 0.030;
//     if(eta>=1.7 && eta<1.9) return 1.041 + 0.062;
//     if(eta>=1.9 && eta<2.1) return 1.167 + 0.086;
//     if(eta>=2.1 && eta<2.3) return 1.094 + 0.093;
//     if(eta>=2.3 && eta<2.5) return 1.168 + 0.120;
//     if(eta>=2.5 && eta<2.8) return 1.266 + 0.132;
//     if(eta>=2.8 && eta<3.0) return 1.595 + 0.175;
//     if(eta>=3.0 && eta<3.2) return 0.998 + 0.066;
//     if(eta>=3.2 && eta<5.0) return 1.226 + 0.145;
//     return -1.;
// }
// float JetAnalyzer::GetResolutionErrorDown(float eta) {
//     eta=fabs(eta);
//     if(eta>=0.0 && eta<0.5) return 1.122 - 0.026; 
//     if(eta>=0.5 && eta<0.8) return 1.167 - 0.048;
//     if(eta>=0.8 && eta<1.1) return 1.168 - 0.046;
//     if(eta>=1.1 && eta<1.3) return 1.029 - 0.066;
//     if(eta>=1.3 && eta<1.7) return 1.115 - 0.030;
//     if(eta>=1.7 && eta<1.9) return 1.041 - 0.062;
//     if(eta>=1.9 && eta<2.1) return 1.167 - 0.086;
//     if(eta>=2.1 && eta<2.3) return 1.094 - 0.093;
//     if(eta>=2.3 && eta<2.5) return 1.168 - 0.120;
//     if(eta>=2.5 && eta<2.8) return 1.266 - 0.132;
//     if(eta>=2.8 && eta<3.0) return 1.595 - 0.175;
//     if(eta>=3.0 && eta<3.2) return 0.998 - 0.066;
//     if(eta>=3.2 && eta<5.0) return 1.226 - 0.145;
//     return -1.;
// }

// PFJet Quality ID 2015-2016: see https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data
bool JetAnalyzer::isLooseJet(pat::Jet& jet , std::string dataEra) {
    //2016
    if(dataEra.find("2016") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.7)
	  {
	    
	    if(fabs(jet.eta())<=2.4)
	      {
		if(jet.neutralHadronEnergyFraction()<0.99 and jet.neutralEmEnergyFraction()<0.99 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0 and jet.chargedEmEnergyFraction()<0.99) return true;
		else return false;
	      }
	    else
	      {
		if(jet.neutralHadronEnergyFraction()<0.99 and jet.neutralEmEnergyFraction()<0.99 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1) return true;
		else return false;
	      }

	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()>0.01 and jet.neutralHadronEnergyFraction()<0.98 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.2 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;	
      }
    //2017
    else if(dataEra.find("2017") != std::string::npos)
      {
	//Loose jet ID does not exist anymore in 2017
	return false;
      }
    //2018
    else if(dataEra.find("2018") != std::string::npos)
      {
	//Loose jet ID does not exist anymore in 2018
	return false;
      }
    else return false;
    /*
    if(fabs(jet.eta())<=2.7){ /// |eta| < 2.7
        if(jet.neutralHadronEnergyFraction()>=0.99) return false;
        if(jet.neutralEmEnergyFraction()>=0.99) return false;
        if((jet.chargedMultiplicity()+jet.neutralMultiplicity())<=1) return false;
        if(fabs(jet.eta())<=2.4) { /// |eta| < 2.4
            if(jet.chargedHadronEnergyFraction()<=0.) return false;
            if(jet.chargedMultiplicity()<=0) return false;
            if(jet.chargedEmEnergyFraction()>=0.99) return false;
        }
    }
    else{ /// |eta| > 2.7
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if (fabs(jet.eta())<=3.0) { /// 2.7 < |eta| < 3.0
            if(jet.neutralMultiplicity()<=2) return false;
        }
        else{ /// |eta| > 3.0
            if(jet.neutralMultiplicity()<=10) return false;
        }
    }
    return true;
    */
}

bool JetAnalyzer::isTightJet(pat::Jet& jet, std::string dataEra) {
    //2016
    if(dataEra.find("2016") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.7)
	  {
	    
	    if(fabs(jet.eta())<=2.4)
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0 and jet.chargedEmEnergyFraction()<0.99) return true;
		else return false;
	      }
	    else
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1) return true;
		else return false;
	      }

	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()>0.01 and jet.neutralHadronEnergyFraction()<0.98 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.2 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;	
      }
    //2017
    else if(dataEra.find("2017") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.7)
	  {
	    
	    if(fabs(jet.eta())<=2.4)
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0) return true;
		else return false;
	      }
	    else
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1) return true;
		else return false;
	      }

	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()<0.99 and jet.neutralEmEnergyFraction()>0.02 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.2 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralHadronEnergyFraction()>0.2 and jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;

      }
    //2018
    else if(dataEra.find("2018") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.6)
	  {
	    if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=2.7 and fabs(jet.eta())>2.6)
	  {
	    if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.99 and jet.chargedMultiplicity()>0) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()<0.99 and jet.neutralEmEnergyFraction()>0.02 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.0 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralHadronEnergyFraction()>0.2 and jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;
      }
    else return false;
    /*
    if(fabs(jet.eta())<=2.7){ /// |eta| < 2.7
        if(jet.neutralHadronEnergyFraction()>=0.90) return false;
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if((jet.chargedMultiplicity()+jet.neutralMultiplicity())<=1) return false;
        if(fabs(jet.eta())<=2.4) { /// |eta| < 2.4
            if(jet.chargedHadronEnergyFraction()<=0.) return false;
            if(jet.chargedMultiplicity()<=0) return false;
            if(jet.chargedEmEnergyFraction()>=0.99) return false;
        }
    }
    else{ /// |eta| > 2.7
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if (fabs(jet.eta())<=3.0) { /// 2.7 < |eta| < 3.0
            if(jet.neutralMultiplicity()<=2) return false;
        }
        else{ /// |eta| > 3.0
            if(jet.neutralMultiplicity()<=10) return false;
        }
    }
    return true;
    */
}

bool JetAnalyzer::isTightLepVetoJet(pat::Jet& jet, std::string dataEra) {
    //2016
    if(dataEra.find("2016") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.7)
	  {
	    
	    if(fabs(jet.eta())<=2.4)
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0 and jet.chargedEmEnergyFraction()<0.99 and jet.muonEnergyFraction()<0.8) return true;
		else return false;
	      }
	    else
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.muonEnergyFraction()<0.8) return true;
		else return false;
	      }

	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()>0.01 and jet.neutralHadronEnergyFraction()<0.98 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.2 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;	
	
      }
    //2017
    else if(dataEra.find("2017") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.7)
	  {
	    
	    if(fabs(jet.eta())<=2.4)
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0 and jet.chargedEmEnergyFraction()<0.80) return true;
		else return false;
	      }
	    else
	      {
		if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.muonEnergyFraction()<0.80) return true;
		else return false;
	      }

	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()<0.99 and jet.neutralEmEnergyFraction()>0.02 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.2 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralHadronEnergyFraction()>0.2 and jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;

       
      }
    //2018
    else if(dataEra.find("2018") != std::string::npos)
      {
	if(fabs(jet.eta())<=2.6)
	  {
	    if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.90 and jet.chargedMultiplicity()+jet.neutralMultiplicity()>1 and jet.chargedHadronEnergyFraction()>0. and jet.chargedMultiplicity()>0 and jet.muonEnergyFraction()<0.80 and jet.chargedEmEnergyFraction()<0.80) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=2.7 and fabs(jet.eta())>2.6)
	  {
	    if(jet.neutralHadronEnergyFraction()<0.90 and jet.neutralEmEnergyFraction()<0.99 and jet.chargedMultiplicity()>0 and jet.muonEnergyFraction()<0.80 and jet.chargedEmEnergyFraction()<0.80) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=3.0 and fabs(jet.eta())>2.7)
	  {
	    if(jet.neutralEmEnergyFraction()<0.99 and jet.neutralEmEnergyFraction()>0.02 and jet.neutralMultiplicity()>2) return true;
	    else return false;
	  }
	else if(fabs(jet.eta())<=5.0 and fabs(jet.eta())>3.0)
	  {
	    if(jet.neutralHadronEnergyFraction()>0.2 and jet.neutralEmEnergyFraction()<0.9 and jet.neutralMultiplicity()>10) return true;
	    else return false;
	  }
	else return false;
      }
    else return false;
    /*
    if(fabs(jet.eta())<=2.7){ /// |eta| < 2.7
        if(jet.neutralHadronEnergyFraction()>=0.90) return false;
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if((jet.chargedMultiplicity()+jet.neutralMultiplicity())<=1) return false;
        if(jet.muonEnergyFraction()>=0.80) return false;
        if(fabs(jet.eta())<=2.4) { /// |eta| < 2.4
            if(jet.chargedHadronEnergyFraction()<=0.) return false;
            if(jet.chargedMultiplicity()<=0) return false;
            if(jet.chargedEmEnergyFraction()>=0.99) return false;
        }
    }
    else{ /// |eta| > 2.7
        if(jet.neutralEmEnergyFraction()>=0.90) return false;
        if (fabs(jet.eta())<=3.0) { /// 2.7 < |eta| < 3.0
            if(jet.neutralMultiplicity()<=2) return false;
        }
        else{ /// |eta| > 3.0
            if(jet.neutralMultiplicity()<=10) return false;
        }
    }
    return true;
    */
}


std::map<std::string, float> JetAnalyzer::CalculateBtagReshapeSF(std::vector<pat::Jet>& jets){
  //follow the instructions here: https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration and here: https://twiki.cern.ch/twiki/bin/view/CMS/BTagCalibration
  std::map<std::string, float> btagWeights;

  //setup here all weights
  float weight_central = 1.0;
  float weight_jesup = 1.0;
  float weight_jesdown = 1.0;
  float weight_lfup = 1.0;
  float weight_lfdown = 1.0;
  float weight_hfup = 1.0;
  float weight_hfdown = 1.0;
  float weight_hfstats1up = 1.0;
  float weight_hfstats1down = 1.0;
  float weight_hfstats2up = 1.0;
  float weight_hfstats2down = 1.0;
  float weight_lfstats1up = 1.0;
  float weight_lfstats1down = 1.0;
  float weight_lfstats2up = 1.0;
  float weight_lfstats2down = 1.0;
  float weight_cferr1up = 1.0;
  float weight_cferr1down = 1.0;
  float weight_cferr2up = 1.0;
  float weight_cferr2down = 1.0;

  //loop over jets and update weights depending on the flavour of the jet
  for(unsigned int a = 0; a<jets.size(); a++){
    float jet_pt(jets.at(a).pt()), jet_eta(jets.at(a).eta()), jet_btagdisc(0.);
    if (BTag.find("deepJet")){
      jet_btagdisc = (jets.at(a).bDiscriminator("pfDeepFlavourJetTags:probb")+ jets.at(a).bDiscriminator("pfDeepFlavourJetTags:probbb") + jets.at(a).bDiscriminator("pfDeepFlavourJetTags:problepb"));
    }
    else throw cms::Exception("JetAnalyzer", "BTagger not supportet. Change BTag variable in config file.");
    int hadron_flavour = std::abs(jets.at(a).hadronFlavour());
    BTagEntry::JetFlavor jet_flavour = BTagEntry::FLAV_UDSG;
    if (hadron_flavour == 5) jet_flavour = BTagEntry::FLAV_B;
    if (hadron_flavour == 4) jet_flavour = BTagEntry::FLAV_C;
    if (jet_pt > 20. && fabs(jet_eta) < 2.4){
      weight_central *= reader->eval_auto_bounds("central",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
      if (jet_flavour == BTagEntry::FLAV_B){
	weight_jesup *= reader->eval_auto_bounds("up_jes",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_jesdown *= reader->eval_auto_bounds("down_jes",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_lfup *= reader->eval_auto_bounds("up_lf",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_lfdown *= reader->eval_auto_bounds("down_lf",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_hfstats1up *= reader->eval_auto_bounds("up_hfstats1",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_hfstats1down *= reader->eval_auto_bounds("down_hfstats1",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_hfstats2up *= reader->eval_auto_bounds("up_hfstats2",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_hfstats2down *= reader->eval_auto_bounds("down_hfstats2",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
      }
      else if (jet_flavour == BTagEntry::FLAV_C){
	weight_cferr1up *= reader->eval_auto_bounds("up_cferr1",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_cferr1down *= reader->eval_auto_bounds("down_cferr1",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_cferr2up *= reader->eval_auto_bounds("up_cferr2",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_cferr2down *= reader->eval_auto_bounds("down_cferr2",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
      }
      else if (jet_flavour == BTagEntry::FLAV_UDSG){
	weight_jesup *= reader->eval_auto_bounds("up_jes",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_jesdown *= reader->eval_auto_bounds("down_jes",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_hfup *= reader->eval_auto_bounds("up_hf",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_hfdown *= reader->eval_auto_bounds("down_hf",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_lfstats1up *= reader->eval_auto_bounds("up_lfstats1",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_lfstats1down *= reader->eval_auto_bounds("down_lfstats1",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_lfstats2up *= reader->eval_auto_bounds("up_lfstats2",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
	weight_lfstats2down *= reader->eval_auto_bounds("down_lfstats2",jet_flavour, jet_eta, jet_pt, jet_btagdisc);
      }
    }
  }//end loop over jets

  btagWeights["weight_central"] = weight_central;
  btagWeights["weight_jesup"] = weight_jesup;
  btagWeights["weight_jesdown"] = weight_jesdown;
  btagWeights["weight_hfup"] = weight_hfup;
  btagWeights["weight_hfdown"] = weight_hfdown;
  btagWeights["weight_hfstats1up"] = weight_hfstats1up;
  btagWeights["weight_hfstats1down"] = weight_hfstats1down;
  btagWeights["weight_hfstats2up"] = weight_hfstats2up;
  btagWeights["weight_hfstats2down"] = weight_hfstats2down;
  btagWeights["weight_cferr1up"] = weight_cferr1up;
  btagWeights["weight_cferr1down"] = weight_cferr1down;
  btagWeights["weight_cferr2up"] = weight_cferr2up;
  btagWeights["weight_cferr2down"] = weight_cferr2down;
  btagWeights["weight_lfup"] = weight_lfup;
  btagWeights["weight_lfdown"] = weight_lfdown;
  btagWeights["weight_lfstats1up"] = weight_lfstats1up;
  btagWeights["weight_lfstats1down"] = weight_lfstats1down;
  btagWeights["weight_lfstats2up"] = weight_lfstats2up;
  btagWeights["weight_lfstats2down"] = weight_lfstats2down;

  return btagWeights;
}


//old code for b-tag reshaping SF method!
/*
std::vector<float> JetAnalyzer::ReshapeBtagDiscriminator(pat::Jet& jet) {
    float pt(jet.pt()), eta(fabs(jet.eta())), discr(jet.bDiscriminator(BTag));
    int hadronFlavour_ = std::abs(jet.hadronFlavour());
    std::vector<float> reshapedDiscr(3, discr);
    
    if(UseReshape) {
        BTagEntry::JetFlavor jf = BTagEntry::FLAV_UDSG;
        if (hadronFlavour_ == 5) jf = BTagEntry::FLAV_B;
	else if (hadronFlavour_ == 4) jf = BTagEntry::FLAV_C;
	else if (hadronFlavour_ == 0) jf = BTagEntry::FLAV_UDSG;

	auto central_sf = cr_map.at("central").eval_auto_bounds("central", jf, eta, pt, discr);
	// default to 1 rather than 0 if out of bounds
	if (central_sf == 0) central_sf = 1.0;
	
	// Get the systematic shifts. For the time being just add up the differences from the central
	// value in quadrature and take that as the overall systematic.
	float up_total2 = 0;
	float down_total2 = 0;
	for (const auto & syst : syst_map.at(jf)) {
	    auto syst_sf = cr_map.at(syst).eval_auto_bounds(syst, jf, eta, pt, discr);
	    // default to 1, as above
	    if (syst_sf == 0) syst_sf = 1.0;

	    if (syst.find("up") != std::string::npos) {
		up_total2 += (syst_sf-central_sf)*(syst_sf-central_sf);
	    } else if (syst.find("down") != std::string::npos) {
		down_total2 += (syst_sf-central_sf)*(syst_sf-central_sf);
	    } else {
		std::cerr << "Unknown systematic " << syst << " -- don't know if this is up or down!" << std::endl;
	    }
	}
	float up_sf = central_sf - sqrt(up_total2);
	float down_sf = central_sf + sqrt(down_total2);

	reshapedDiscr[0] = discr*central_sf;
	reshapedDiscr[1] = discr*up_sf;
	reshapedDiscr[2] = discr*down_sf;
	  
	//std::cout << Form("pt, eta, b-tag, flav, reshapedDiscr : %f, %f, %f, %d, %f, %f, %f\n",
	// 		  pt, eta, discr, jf, reshapedDiscr[0], reshapedDiscr[1], reshapedDiscr[2]);
    }
    return reshapedDiscr;
}
*/

/*
bool JetAnalyzer::isMediumJet(pat::Jet& jet) {
    if(jet.neutralHadronEnergyFraction()>0.95) return false;
    if(jet.neutralEmEnergyFraction()>0.95) return false;
    if(jet.numberOfDaughters()<=1) return false;
    if(fabs(jet.eta())<2.4) {
      if(jet.chargedHadronEnergyFraction()<=0.) return false;
      if(jet.chargedEmEnergyFraction()>0.99) return false;
      if(jet.chargedMultiplicity()<=0) return false;
    }
    return true;
}
bool JetAnalyzer::isTightJet(pat::Jet& jet) {
    if(jet.neutralHadronEnergyFraction()>0.90) return false;
    if(jet.neutralEmEnergyFraction()>0.90) return false;
    if(jet.numberOfDaughters()<=1) return false;
    if(fabs(jet.eta())<2.4) {
      if(jet.chargedHadronEnergyFraction()<=0.) return false;
      if(jet.chargedEmEnergyFraction()>0.99) return false;
      if(jet.chargedMultiplicity()<=0) return false;
    }
    return true;
}

*/
