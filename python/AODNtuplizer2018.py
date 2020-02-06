import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')


## Var parsing, for CRAB
#options.register(
#    "runLocal", True,
#    VarParsing.multiplicity.singleton,
#    VarParsing.varType.bool,
#    "Decide if CRAB should overwrite variables"
#)
options.register(
    "runLocal", True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Decide if CRAB should overwrite variables"
)

options.register(
    "PisData", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isData parser flag"
)
options.register(
    "PisReHLT", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isReHLT parser flag"
)
options.register(
    "PisReReco", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isReReco parser flag"
)
options.register(
    "PisReMiniAod", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isReMiniAod parser flag"
)
options.register(
    "PisPromptReco", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isPromptReco parser flag"
)
options.register(
    "Pis2017", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "is2017 parser flag"
)
options.register(
    "PnoLHEinfo", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "noLHEinfo parser flag"
)
options.register(
    "PisbbH", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isbbH parser flag"
)
options.register(
    "PisSignal", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isSignal parser flag"
)
options.register(
    "PGT", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "GT parser flag"
)
options.register(
    "PJECstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "JECstring parser flag"
)
options.register(
    "PjsonName", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    " jsonName parser flag"
)
options.register(
    "PtriggerTag", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "triggerTag parser flag"
)
options.register(
    "PfilterString", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "filterString parser flag"
)
options.register(
    "Pcalo", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "calo parser flag"
)
options.register(
    "PVBF", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "VBF parser flag"
)
options.register(
    "PggH", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "ggH parser flag"
)


options.parseArguments()
process = cms.Process("ntuple")
task = cms.Task()

## Important: decide if keeping local options register or CRAB options register
#RunLocalCMS = cms.bool( options.runLocal )
RunLocal = cms.bool( options.runLocal )

if RunLocal:
   print "Taking configurations from cfg file; not designed for CRAB submission!"


process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True),
)

#Enable multithreading!
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #test 2017 MC:
            '/store/user/mcitron/ProjectMetis/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-1000mm_privateMC_102X_RECO_v1_generation_forMS/output_8.root'
            
        )
    )

if RunLocal:
    isData = ('/store/data/' in process.source.fileNames[0])
else:
    isData = options.PisData

process.TFileService = cms.Service( "TFileService",
    fileName = cms.string('output.root' if len(options.outputFile)==0 else options.outputFile),
    closeFileFast = cms.untracked.bool(True),
)

#-----------------------#
#     DATA FLAGS        #
#-----------------------#

if RunLocal:
    isData            = ('/store/data/' in process.source.fileNames[0])
    isReHLT           = ('_reHLT_' in process.source.fileNames[0])
    isReReco          = ('23Sep2016' in process.source.fileNames[0])
    isReMiniAod       = ('03Feb2017' in process.source.fileNames[0])
    is2017            = ('RunIIFall17MiniAODv2' in process.source.fileNames[0])
    isPromptReco      = ('PromptReco' in process.source.fileNames[0])
    noLHEinfo         = True if ('WW_TuneCUETP8M1_13TeV-pythia8' or 'WZ_TuneCUETP8M1_13TeV-pythia8' or 'ZZ_TuneCUETP8M1_13TeV-pythia8') in process.source.fileNames[0] else False #check for PythiaLO samples
    isbbH             = True if ('bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo' in process.source.fileNames[0]) else False #bbH has a different label in LHEEventProduct
    isSignal          = True if ('HToSSTobbbb_MH-125' in process.source.fileNames[0]) else False
    isCalo            = True #HERE for calo analyses!!!
    isVBF             = True
    isggH             = False
    isHeavyHiggs      = True

else:
    isData            = options.PisData
    isReHLT           = options.PisReHLT
    isReReco          = options.PisReReco
    isReMiniAod       = options.PisReMiniAod
    is2017            = options.Pis2017
    isPromptReco      = options.PisPromptReco
    noLHEinfo         = options.PnoLHEinfo
    isbbH             = options.PisbbH
    isSignal          = options.PisSignal
    isCalo            = options.Pcalo
    isVBF             = options.PVBF
    isggH             = options.PggH
    isHeavyHiggs      = True


theRunBCD = ['Run2016B','Run2016C','Run2016D']
theRunEF  = ['Run2016E','Run2016F']
theRunG   = ['Run2016G']
theRunH   = ['Run2016H']

print 'isData',isData
print 'isReHLT',isReHLT
print 'isReReco',isReReco
print 'isReMiniAod',isReMiniAod
print 'isPromptReco',isPromptReco
print 'isSignal', isSignal

if isHeavyHiggs:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing HEAVY HIGGS analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"

if isVBF:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing analysis for VBF!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"

if isggH:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing analysis for ggH!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"

if isCalo:
    print "\n"
    print "***************************************"
    print "***************************************"
    print "***************************************"
    print "\n"
    print "Performing analysis for CALO LIFETIMES!"
    print "\n"
    print "***************************************"
    print "***************************************"
    print "***************************************"
    print "\n"

#-----------------------#
#     GLOBAL TAG        #
#-----------------------#

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
GT = ''

if RunLocal:
    if isData:
        #if isReMiniAod and any(s in process.source.fileNames[0] for s in theRunH): GT = '80X_dataRun2_Prompt_v16'
        #else:
        GT = '102X_dataRun2_v12'
    elif not(isData):
        GT = '102X_upgrade2018_realistic_v20'#2018!
else:
    GT = options.PGT

process.GlobalTag = GlobalTag(process.GlobalTag, GT)
print 'GlobalTag loaded: ', GT


#-----------------------#
#        FILTERS        #
#-----------------------#

# JSON filter
if isData:
    import FWCore.PythonUtilities.LumiList as LumiList
    jsonName = "Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON"
    process.source.lumisToProcess = LumiList.LumiList(filename = 'data/JSON/'+jsonName+'.txt').getVLuminosityBlockRange()
    print "JSON file loaded: ", jsonName

if RunLocal:
    # Trigger filter
    triggerTag = 'HLT2' if isReHLT else 'HLT'

    # MET filters string
    if isData:
        filterString = "RECO"
    else:
        filterString = "RECO"#"PAT"
else:
    triggerTag = options.PtriggerTag
    filterString = options.PfilterString

#########################################################

#-----------------------#
#     PAT OBJECTS       #
#-----------------------#

#Transient track builder needed for vertices
process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")


## Processing
import PhysicsTools.PatAlgos.tools.helpers as configtools
patAlgosToolsTask = configtools.getPatAlgosToolsTask(process)


#Puppi
process.load('CommonTools.PileupAlgos.Puppi_cff')
process.load('PhysicsTools.PatAlgos.slimming.puppiForMET_cff')
process.pfNoLepPUPPI = cms.EDFilter("PdgIdCandViewSelector",
                                    src = cms.InputTag("particleFlow"),
                                    pdgId = cms.vint32( 1,2,22,111,130,310,2112,211,-211,321,-321,999211,2212,-2212 )
                                    )
patAlgosToolsTask.add(process.pfNoLepPUPPI)
patAlgosToolsTask.add(process.puppi)

process.puppiNoLep = process.puppi.clone()
process.puppiNoLep.candName = cms.InputTag('pfNoLepPUPPI')
patAlgosToolsTask.add(process.puppiNoLep)


process.load( "PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff" )
patAlgosToolsTask.add(process.patCandidatesTask)
##Temporary customize to the unit tests that fail due to old input samples
process.patTaus.skipMissingTauID = True

#for some reasons, complaining about patTrigger
process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )
patAlgosToolsTask.add(process.patTrigger)
patAlgosToolsTask.add(process.patTriggerEvent)

process.load( "PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff" )
patAlgosToolsTask.add(process.selectedPatCandidatesTask)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("RecoVertex.AdaptiveVertexFinder.inclusiveVertexing_cff")
patAlgosToolsTask.add(process.inclusiveVertexingTask)
patAlgosToolsTask.add(process.inclusiveCandidateVertexingTask)
patAlgosToolsTask.add(process.inclusiveCandidateVertexingCvsLTask)

#MET giving problems...
#slimmedMETs
process.load('PhysicsTools.PatAlgos.producersLayer1.metProducer_cff')
process.patMETs.computeMETSignsificance = cms.bool(True)
process.patMETs.srcJets = cms.InputTag("patJets")
process.patMETs.addGenMET = cms.bool(False if isData else True)
process.load('PhysicsTools.PatAlgos.selectionLayer1.metSelector_cfi')
patAlgosToolsTask.add(process.patMETs)


#Calculating met corrections, uncertainties and slimmed mets
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import *
#runMetCorAndUncForMiniAODProduction(process,
#                                    jetSelection="pt>543 && abs(eta)<9.9",#this is important!
#                                    )

runMETCorrectionsAndUncertainties = RunMETCorrectionsAndUncertainties()
##
metType="PF"
#jetCollUnskimmed="patJets"
jetCollUnskimmed="patJets"
photonColl="selectedPatPhotons"
electronColl="selectedPatElectrons"
muonColl="selectedPatMuons"
tauColl="selectedPatTaus"
pfCandColl = "particleFlow"
jetCleaning="LepClean"
jetSelection="pt>543 && abs(eta)<9.9"
jecUnFile=""
jetFlavor="AK4PFchs"
recoMetFromPFCs=False
postfix=""

runMETCorrectionsAndUncertainties(process,
                                  metType=metType,
                                  correctionLevel=["T0","T1","T2","Smear","Txy"],
                                  computeUncertainties=False,
                                  produceIntermediateCorrections=True,
                                  addToPatDefaultSequence=False,
                                  jetCollectionUnskimmed=jetCollUnskimmed,
                                  photonCollection=photonColl,
                                  electronCollection=electronColl,
                                  muonCollection=muonColl,
                                  tauCollection=tauColl,
                                  pfCandCollection =pfCandColl,
                                  autoJetCleaning=jetCleaning,
                                  jecUncertaintyFile=jecUnFile,
                                  jetSelection=jetSelection,
                                  jetFlavor=jetFlavor,
                                  recoMetFromPFCs=recoMetFromPFCs,
                                  postfix=postfix,
                                  runOnData = True if isData else False
                                  )

#MET T1 uncertainties
runMETCorrectionsAndUncertainties(process,
                                  metType=metType,
                                  correctionLevel=["T1"],
                                  computeUncertainties=True,
                                  produceIntermediateCorrections=False,
                                  addToPatDefaultSequence=False,
                                  jetCollectionUnskimmed=jetCollUnskimmed,
                                  photonCollection=photonColl,
                                  electronCollection=electronColl,
                                  muonCollection=muonColl,
                                  tauCollection=tauColl,
                                  pfCandCollection =pfCandColl,
                                  autoJetCleaning=jetCleaning,
                                  jecUncertaintyFile=jecUnFile,
                                  jetSelection=jetSelection,
                                  jetFlavor=jetFlavor,
                                  recoMetFromPFCs=recoMetFromPFCs,
                                  postfix=postfix,
                                  runOnData = True if isData else False
                                  )

#MET T1 Smeared JER uncertainties
runMETCorrectionsAndUncertainties(process,
                                  metType=metType,
                                  correctionLevel=["T1","Smear"],
                                  computeUncertainties=True,
                                  produceIntermediateCorrections=False,
                                  addToPatDefaultSequence=False,
                                  jetCollectionUnskimmed=jetCollUnskimmed,
                                  photonCollection=photonColl,
                                  electronCollection=electronColl,
                                  muonCollection=muonColl,
                                  tauCollection=tauColl,
                                  pfCandCollection =pfCandColl,
                                  autoJetCleaning=jetCleaning,
                                  jecUncertaintyFile=jecUnFile,
                                  jetSelection=jetSelection,
                                  jetFlavor=jetFlavor,
                                  recoMetFromPFCs=recoMetFromPFCs,
                                  postfix=postfix,
                                  runOnData = True if isData else False
                                  )

#import PhysicsTools.PatAlgos.tools.helpers as configtools
#postfix=''
#configtools.removeIfInSequence(process, "selectedPatJetsForMetT1T2Corr", "patPFMetT1T2CorrSequence", postfix )
process.patSmearedJets.skipGenMatching = cms.bool(True if isData else False)

from PhysicsTools.PatAlgos.producersLayer1.metProducer_cfi import patMETs
process.patCaloMet = patMETs.clone(
    metSource = cms.InputTag('caloMetM'),
    addMuonCorrections = cms.bool(False),
    genMETSource = cms.InputTag('genMetTrue'),
    addGenMET = cms.bool(False if isData else True)
)
patAlgosToolsTask.add(process.patCaloMet)

#  ==================  CHSMET
from PhysicsTools.PatAlgos.tools.metTools import addMETCollection
process.CHSCands = cms.EDFilter("CandPtrSelector",
                                    src=cms.InputTag("packedPFCandidates"),
                                    cut=cms.string("fromPV(0) > 0")
                                    )
patAlgosToolsTask.add(process.CHSCands)

process.pfMetCHS = cms.EDProducer("PFMETProducer",
                                      src = cms.InputTag("CHSCands"),
                                      alias = cms.string('pfMet'),
                                      globalThreshold = cms.double(0.0),
                                      calculateSignificance = cms.bool(False),
                                      )
patAlgosToolsTask.add(process.pfMetCHS)    

addMETCollection(process,
                     labelName = "patCHSMet",
                     metSource = "pfMetCHS"
                     )

process.patCHSMet.computeMETSignificance = cms.bool(False)#??#

#  ==================  TrkMET 
process.TrkCands = cms.EDFilter("CandPtrSelector",
                                    src=cms.InputTag("packedPFCandidates"),
                                    cut=cms.string("charge()!=0 && pvAssociationQuality()>=4 && vertexRef().key()==0")
                                    )
patAlgosToolsTask.add(process.TrkCands)

process.pfMetTrk = cms.EDProducer("PFMETProducer",
                                      src = cms.InputTag("TrkCands"),
                                      alias = cms.string('pfMet'),
                                      globalThreshold = cms.double(0.0),
                                      calculateSignificance = cms.bool(False),
                                      )

patAlgosToolsTask.add(process.pfMetTrk)

addMETCollection(process,
                     labelName = "patTrkMet",
                     metSource = "pfMetTrk"
                     )

process.patTrkMet.computeMETSignificance = cms.bool(False)

process.load('PhysicsTools.PatAlgos.slimming.slimmedMETs_cfi')
patAlgosToolsTask.add(process.slimmedMETs)


#random stuff failing for no reason
#patAlgosToolsTask.add(process.packedPatJetsAK8)

process.load("PhysicsTools.PatAlgos.slimming.slimming_cff")
patAlgosToolsTask.add(process.slimmingTask)

###MOAR????does this help? no idea..... hoping it will deal with electrons and photons at least
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeCommon, miniAOD_customizeMC
miniAOD_customizeCommon(process)
miniAOD_customizeMC(process)
if isData:
    miniAOD_customizeData(process)
else:
    miniAOD_customizeMC(process)


## Output
'''
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.out = cms.OutputModule(
  "PoolOutputModule"
, fileName = cms.untracked.string( 'patTuple_data.root' )
, outputCommands = cms.untracked.vstring(
    *patEventContentNoCleaning
  )
)
process.out.outputCommands += [ 'drop recoGenJets_*_*_*' ]
process.out.outputCommands += [
    #'keep edmTriggerResults_TriggerResults*_*_*',
    #'keep *_hltTriggerSummaryAOD_*_*',
    #'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
    'drop *',
    'keep *_offlineSlimmedPrimaryVertices_*_*',
    'keep *_slimmedPhotons_*_*', 
    'keep *_slimmedElectrons_*_*', 
    'keep *_slimmedMuons_*_*', 
    'keep *_slimmedTaus_*_*', 
    'keep *_slimmedCaloJets_*_*', 
    'keep *_slimmedJets_*_*',
    #'keep *_patJets_*_*',
    'keep *_slimmedJetsAK8_*_*',  
    'keep *_slimmedMETs_*_*', 
    'keep *_slimmedSecondaryVertices_*_*', 
    'keep *_slimmedPatTrigger_*_*',
    'keep *_slimmedGenJets__*', 
    'keep *_slimmedGenJetsAK8__*', 
]
process.outpath = cms.EndPath(
  process.out, patAlgosToolsTask
)
'''

#########################################################
#-----------------------#
#    VERTEX FILTER      #
#-----------------------#

#import RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi
#process.primaryVertexFilter = cms.EDFilter('GoodVertexFilter',
#    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
#    minimumNDOF = cms.uint32(4),
#    maxAbsZ = cms.double(24),
#    maxd0 = cms.double(2)
#)
#task.add(process.primaryVertexFilter)

#-----------------------#
#     MET FILTERS       #
#-----------------------#

## MET filters, not available on AOD? TODO
process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.muons = cms.InputTag('slimmedMuons')
process.BadPFMuonFilter.PFCandidates = cms.InputTag('packedPFCandidates')

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.muons = cms.InputTag('slimmedMuons')
process.BadChargedCandidateFilter.PFCandidates = cms.InputTag('packedPFCandidates')

task.add(process.BadPFMuonFilter)
task.add(process.BadChargedCandidateFilter)

#-----------------------#
#       COUNTER         #
#-----------------------#
process.counter = cms.EDAnalyzer('CounterAnalyzer',
    #lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
    genProduct = cms.InputTag('generator'),
    pythiaLOSample = cms.bool(True if noLHEinfo else False),
)

#-----------------------#
#       TEST            #
#-----------------------#

#process.test = cms.EDAnalyzer('LLP2018',
#    electrons = cms.untracked.InputTag('slimmedElectrons'),
#    eleVetoIdMap = cms.untracked.string('cutBasedElectronID-Fall17-94X-V2-veto'),
#)

#-----------------------#
#  Particle List Drawer #
#-----------------------#

process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.ParticleListDrawer = cms.EDAnalyzer('ParticleListDrawer',
                                            maxEventsToPrint = cms.untracked.int32(1),
                                            src = cms.InputTag('prunedGenParticles'),#collection of particles being considered: prunedGenParticles works for miniaod
##                                            src = cms.InputTag('genParticles'),#genParticles works for aod
                                            printOnlyHardInteraction = cms.untracked.bool(False),
                                            useMessageLogger = cms.untracked.bool(False)
                                            )


#-----------------------#
#       ANALYZER        #
#-----------------------#

process.ntuple = cms.EDAnalyzer('TriggerGenNtuplizer',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        lheProduct = cms.InputTag('externalLHEProducer'),
        genParticles = cms.InputTag('prunedGenParticles'),
        pdgId = cms.vint32(5,9000006,6000113,23,24,25),#(1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 23, 24, 25, 36, 39, 1000022, 9100000, 9000001, 9000002, 9100012, 9100022, 9900032, 1023),
        status = cms.vint32(22,23),
        samplesDYJetsToLL = cms.vstring(),
        samplesZJetsToNuNu = cms.vstring(),
        samplesWJetsToLNu = cms.vstring(),
        samplesDir = cms.string('data_gen/Stitch/'),
        sample = cms.string("" ), #( sample )
        ewkFile = cms.string('data_gen/scalefactors_v4.root'),
        applyEWK = cms.bool(False),#(True if sample.startswith('DYJets') or sample.startswith('WJets') else False),
        applyTopPtReweigth = cms.bool(False),#(True if sample.startswith('TT_') else False),
        pythiaLOSample = cms.bool(True if noLHEinfo else False),#(True if isDibosonInclusive else False),
    ),
    triggerSet = cms.PSet(
        trigger = cms.InputTag('TriggerResults', '', triggerTag),
        paths = cms.vstring(
*[
##single lepton
'HLT_IsoMu24_v','HLT_Ele27_WPTight_Gsf_v',
##others:
'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v','HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v','HLT_PFHT300_PFMET110_v','HLT_RsqMR270_Rsq0p09_MR200_v','HLT_RsqMR270_Rsq0p09_MR200_4jet_v','HLT_HT650_v',
### b-like
'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v', 'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v', 'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', 'HLT_QuadJet45_TripleBTagCSV_p087_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v','HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v',
'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v'
### displaced tracks
'HLT_VBF_DisplacedJet40_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v', 'HLT_HT350_DisplacedDijet40_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v', 'HLT_HT650_DisplacedDijet80_Inclusive_v', 'HLT_HT750_DisplacedDijet80_Inclusive_v',
### calo lifetimes
'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v',
###
#'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v', 'HLT_MET200_v', 'HLT_MET250_v', 'HLT_MET75_IsoTrk50_v', 'HLT_MET90_IsoTrk50_v', 'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v', 'HLT_PFMET110_PFMHT110_IDTight_v', 'HLT_PFMET120_PFMHT120_IDTight_v', 'HLT_PFMET170_HBHECleaned_v', 'HLT_PFMET300_v', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
###production for MET
'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
'HLT_PFMETNoMu1240_PFMHTNoMu140_IDTight_v',
### All studied triggers:
#
###Control paths for VBF, prescaled
#'HLT_L1_TripleJet_VBF_v', 'HLT_QuadPFJet_VBF_v','HLT_DiPFJetAve40_v','HLT_DiPFJetAve60_v','HLT_DiPFJetAve80_v','HLT_PFJet40_v','HLT_PFJet60_v','HLT_PFJet80_v',
###TEST
##'HLT_AK8PFJet450_v',###########TEST
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v'#,'HLT_AK4PFJet30_v7'
### Displaced Muons
'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v', 'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v', 'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v',
'HLT_L2Mu10_NoVertex_NoBPTX3BX_v2','HLT_L2Mu10_NoVertex_NoBPTX_v3','HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v2','HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v1',
]
        ),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter','Flag_badMuons','Flag_duplicateMuons','Flag_noBadMuons') if isReMiniAod else cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter'),
        prescales = cms.InputTag('patTrigger','','ntuple'),
        l1Minprescales = cms.InputTag('patTrigger','l1min','ntuple'),
        l1Maxprescales = cms.InputTag('patTrigger','l1max','ntuple'),
        objects = cms.InputTag('selectedPatTrigger','','ntuple'),
        badPFMuonFilter = cms.InputTag("BadPFMuonFilter"),
        badChCandFilter = cms.InputTag("BadChargedCandidateFilter"),
        l1Gt = cms.InputTag("gtStage2Digis"),
        l1filters = cms.vstring('hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300','hltL1sDoubleJetC112','hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF','hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet','hltL1sSingleMu22','hltL1sV0SingleMu22IorSingleMu25','hltL1sZeroBias','hltL1sSingleJet60','hltL1sSingleJet35','hltTripleJet50','hltDoubleJet65','hltSingleJet80','hltVBFFilterDisplacedJets'),
    ),
    muonSet = cms.PSet(
        muons = cms.InputTag('slimmedMuons'),#let's be inclusive!
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        muonTrkFileName = cms.string('data_gen/MuonTrkEfficienciesAndSF_MORIOND17.root'),
        muonIdFileName = cms.string('data_gen/MuonIdEfficienciesAndSF_MORIOND17.root'),
        muonIsoFileName = cms.string('data_gen/MuonIsoEfficienciesAndSF_MORIOND17.root'),
        muonTrkHighptFileName = cms.string('data_gen/tkhighpt_2016full_absetapt.root'),
        muonTriggerFileName = cms.string('data_gen/MuonTrigEfficienciesAndSF_MORIOND17.root'),
        doubleMuonTriggerFileName = cms.string('data_gen/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root'),#FIXME -> obsolete
        muon1id = cms.int32(0), # 0: pass PF ID, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(0),
        muon1iso = cms.int32(-1), # 0: trk iso (<0.1), 1: loose (<0.25), 2: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(-1),
        muon1pt = cms.double(5.),
        muon2pt = cms.double(5.),
        useTuneP = cms.bool(False),
        doRochester = cms.bool(False),
    ),
    idLLP = cms.int32(6000113 if isHeavyHiggs else 9000006),
    idHiggs = cms.int32(35),
    statusHiggs = cms.int32(62 if isHeavyHiggs else 22),
    minGenBpt = cms.double(0.),#(15.),#gen b quarks in acceptance
    maxGenBeta = cms.double(999.),#(2.4),#gen b quarks in acceptance
    minGenBradius2D = cms.double(129.),#new!! in cm
    maxGenBradius2D = cms.double(402.),#new!! in cm
    minGenBetaAcc = cms.double(0.),#(2.4),#
    maxGenBetaAcc = cms.double(1.1),#(2.4),#
    ###writeGenVBFquarks = cms.bool(True),
    writeGenHiggs = cms.bool(True),
    writeGenBquarks = cms.bool(True), #Acceptance cuts a few lines above!
    writeGenLLPs = cms.bool(True),
    verbose = cms.bool(False),
    AlgInputTag = cms.InputTag("gtStage2Digis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1Seeds = cms.vstring("L1_TripleJet_84_68_48_VBF","L1_TripleJet_88_72_56_VBF","L1_TripleJet_92_76_64_VBF","L1_HTT280","L1_HTT300","L1_HTT320","L1_SingleJet170","L1_SingleJet180","L1_SingleJet200","L1_DoubleJetC100","L1_DoubleJetC112","L1_DoubleJetC120","L1_QuadJetC50", "L1_QuadJetC60", "L1_ETM100", "L1_ETM105", "L1_ETM110", "L1_ETM115", "L1_ETM120", "L1_DoubleMu_13_6", "L1_DoubleMu_12_5", "L1_DoubleMu0er1p4_dEta_Max1p8_OS","L1_SingleMuOpen_NotBptxOR_3BX","L1_SingleMuOpen_NotBptxOR","L1_SingleMuOpen_NotBptxOR_3BX","L1_SingleMuOpen_NotBptxOR_3BX"),
    ReadPrescalesFromFile = cms.bool(True),
)

process.seq = cms.Sequence(
    process.counter *
    #process.ParticleListDrawer #*
    process.ntuple
)

process.p = cms.Path(process.seq)
#process.p.associate(task)
process.p.associate(task, patAlgosToolsTask)



'''
## If we want to keep the output miniaod:
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.OUT = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('test.root'),
    outputCommands = cms.untracked.vstring(['keep *']),
#    outputCommands = cms.untracked.vstring(['keep *', 'keep *_pfXTags_*_*', 'keep *_pfXTagInfos_*_*', 'drop *_reco*_*_*', 'drop recoVert*_*_*_*']),
#    ###outputCommands = cms.untracked.vstring(['keep *_pfXTags_*_*', 'keep *_pfXTagInfos_*_*', 'drop *']),
)

process.endpath= cms.EndPath(process.OUT)
process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)
'''

outFile = open("tmpConfig_AODNtuplizer2018.py","w")
outFile.write(process.dumpPython())
outFile.close()

