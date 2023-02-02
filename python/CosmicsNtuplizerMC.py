import FWCore.ParameterSet.Config as cms

process = cms.Process("ntuple")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
            fileNames = cms.untracked.vstring(
                #MC cosmic
                '/store/mc/RunIIAutumn18DR/TKCosmic_38T_p20-3000/AODSIM/NoPU_102X_upgrade2018_realistic_v15-v8/70000/6EB17CE5-CFD9-C94F-803A-42B945FCDA3D.root' 
                ##'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/479/00000/AC189117-E694-E811-9B2A-FA163EFD04C9.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/479/00000/AC189117-E694-E811-9B2A-FA163EFD04C9.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/480/00000/D8BB202B-F194-E811-A431-FA163E793D83.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/481/00000/D413473F-F994-E811-BDA8-FA163E21D5DA.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/483/00000/D6F7A9A5-F994-E811-B1F9-02163E017FC3.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/484/00000/A037711B-FE94-E811-8146-FA163E88A3AD.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/488/00000/3E5EB256-2B95-E811-B007-FA163E4B6AD5.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/488/00000/64668B93-2D95-E811-A9CF-FA163E29C561.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/489/00000/B2B77FF9-4C95-E811-9814-FA163EB6A6A6.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/490/00000/08EEBDCF-3D95-E811-8137-FA163E581A98.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/492/00000/C25FC55D-4095-E811-BCE4-FA163E44601E.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/493/00000/CA79D50C-5A95-E811-B7F4-FA163E833127.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/494/00000/4C56C7AE-5D95-E811-9A2D-02163E01A097.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/496/00000/5ED984D8-5995-E811-80BB-FA163E53153A.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/498/00000/2057A412-6195-E811-86CC-02163E00BBEA.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/510/00000/98DD368D-1396-E811-94BB-FA163E4200C7.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/512/00000/722F3335-1696-E811-B585-FA163E787BA6.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/513/00000/847131B2-1496-E811-9244-FA163E0C6907.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/514/00000/3EFC4153-1496-E811-B6D3-FA163E35DF95.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/516/00000/EA5D3A3B-1796-E811-B683-FA163E61C9C1.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/520/00000/1CA0F219-1696-E811-93DE-FA163E054896.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/522/00000/6AAD313F-1A96-E811-8DD6-FA163E1B5CE1.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/536/00000/9AB94546-1396-E811-AABF-FA163EBE0386.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/538/00000/D062F42E-1596-E811-8555-02163E019F92.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/540/00000/8EDDD43F-1396-E811-A3E5-A4BF0112BCCC.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/541/00000/88687E50-1596-E811-98FE-FA163ED816D7.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/542/00000/10C90028-1496-E811-A6FC-FA163E0385C0.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/546/00000/EA42D1C6-1496-E811-A2BE-FA163ECF2292.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/547/00000/7624B034-1496-E811-A678-FA163E5C9713.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/550/00000/B63353A1-1496-E811-8C2D-FA163EE655A1.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/554/00000/C6852617-1496-E811-A125-FA163EEA790F.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/556/00000/1ACC866B-1596-E811-BAFD-02163E013E59.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/557/00000/AEE8AFEC-1496-E811-AFEC-02163E010E2E.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/563/00000/663D4018-1596-E811-AD54-FA163E1C5C83.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/565/00000/4CCF2CFD-1696-E811-A018-FA163E122414.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/567/00000/72E2BD78-1796-E811-8792-A4BF0112F6B8.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/593/00000/7EAB727F-5E96-E811-AD64-FA163E0BC49B.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/594/00000/B4C88EEE-6196-E811-B0BE-02163E010D67.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/597/00000/1C4996FD-6296-E811-A273-02163E010C03.root',
                #'/store/data/Run2018D/Cosmics/RAW-RECO/CosmicSP-PromptReco-v2/000/320/600/00000/3AB27914-6996-E811-AADE-FA163EF4913C.root',

            )
)



process.TFileService = cms.Service( "TFileService",
    fileName = cms.string('output.root'),
    closeFileFast = cms.untracked.bool(True),
)

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:phase1_2018_cosmics")

process.load("RecoTracker.TkNavigation.NavigationSchoolESProducer_cfi")
process.MaterialPropagator = cms.ESProducer('PropagatorWithMaterialESProducer',
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)
process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")


process.ntuple  = cms.EDAnalyzer('CosmicsAnalyzerMC',
   caloJets      = cms.untracked.InputTag('ak4CaloJets'),
   caloMet       = cms.untracked.InputTag('caloMet'),
   #data:
   #ecalRecHitsEB = cms.untracked.InputTag('ecalRecHit','EcalRecHitsEB','RECO'),
   #MC:
   ecalRecHitsEB = cms.untracked.InputTag('reducedEcalRecHitsEB','','RECO'),
   dtSegments    = cms.untracked.InputTag('dt4DSegments'),
   cscSegments    = cms.untracked.InputTag('cscSegments'),
   cosmicMuons    = cms.untracked.InputTag('cosmicMuons'),
   cosmicMuonsOneLeg    = cms.untracked.InputTag('cosmicMuons1Leg'),
   #globalCosmicMuons    = cms.untracked.InputTag('globalCosmicMuons'),
   #globalCosmicMuonsOneLeg    = cms.untracked.InputTag('globalCosmicMuons1Leg'),
   genParticles   = cms.untracked.InputTag('genParticles'),
                              )

process.p = cms.Path(process.ntuple)
