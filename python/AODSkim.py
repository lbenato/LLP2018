import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # One light file from each QCD dataset:
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/60000/B8B2C094-1ADA-3D49-9CE2-5AEFA7288DF5.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/910000/FAD8A409-B694-4646-A702-2C88396B4310.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/810000/FB6C58E2-9DF2-E641-AFE6-EB519650D750.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/60002/ECCDD787-8BCE-A048-9D56-315EC66F4FE0.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/80000/5192BC30-B35D-2D40-B3A3-780173C92BC3.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/80000/FC3BEFF7-CF38-104A-B794-34E4D2A15146.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/80000/E1769A13-ABC2-DB43-9056-48111194BA13.root',
        #'/store/mc/RunIIAutumn18DRPremix/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/100000/23E295AC-95A1-B44E-86EA-2FF7476A01CF.root',
        # Large local files:
        '/store/mc/RunIIAutumn18DRPremix/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/80000/E607571E-9A42-A843-BBC0-D81659E57193.root'
    ),
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.options = cms.untracked.PSet(
#    numberOfThreads=cms.untracked.uint32(8),
#    numberOfStreams=cms.untracked.uint32(0),
    wantSummary = cms.untracked.bool(True),
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('eventCounter.root'),
    closeFileFast = cms.untracked.bool(True),
)

#------------------------------------------
# Load standard sequences.
#------------------------------------------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v20'

#-----------------------#
#       COUNTER         #
#-----------------------#
process.counter = cms.EDAnalyzer('CounterAnalyzer',
    #lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
    genProduct = cms.InputTag('generator'),
    pythiaLOSample = cms.bool(False),
)

process.counterPath = cms.Path(process.counter)

#------------------------------------------
# Parameters for HLT-path filtering
#------------------------------------------

# See 2018 menu: https://docs.google.com/spreadsheets/d/1D_og1_J6Hp4uALUg-R4Hkq3CF0VN6IK5komHPHv5R-o/edit#gid=585230569
#HLTPathList =

# HLT EDFilter
process.hltDisplacedJet = cms.EDFilter('HLTHighLevel',
    TriggerResultsTag = cms.InputTag('TriggerResults','','HLT'),
    HLTPaths = cms.vstring(# List of HLT paths (or patterns)
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v*',     #prescaled   (control)
        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v*',     #unprescaled (signal)
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v*',     #unprescaled (backup)
        'HLT_HT500_DisplacedDijet40_DisplacedTrack_v*',     #unprescaled (backup)
        'HLT_HT550_DisplacedDijet60_Inclusive_v*',          #prescaled   (control)
        'HLT_HT650_DisplacedDijet60_Inclusive_v*'           #unprescaled (backup)
    ),#See list just above!
    eventSetupPathsKey = cms.string(''),#Use paths from AlCaRecoTriggerBitsRcd via this key. Otherwise, keep empty
    andOr = cms.bool(True),#True = OR (accept if ANY path is true), False = AND (accept only if ALL paths are true)
    throw = cms.bool(True),#Throw exception on unknown path names
)

# Process Path
process.hltDisplacedJetPath = cms.Path(process.hltDisplacedJet)

#------------------------------------------
# Output
#------------------------------------------

process.outputSkim = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("DisplacedDijetSkim_TestCounter.root"),
    outputCommands = cms.untracked.vstring('keep *'),#Tried: process.AODSIMEventContent.outputCommands, but some collections missing!
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('hltDisplacedJetPath')),
    dataset = cms.untracked.PSet(
      dataTier = cms.untracked.string('AODSIM'),
      filterName = cms.untracked.string('DisplacedDijetSkim')
    ),
)

process.outputPath = cms.EndPath(process.outputSkim)

