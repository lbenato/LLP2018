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
        filterString = "PAT"
else:
    triggerTag = options.PtriggerTag
    filterString = options.PfilterString


# MET filters
#process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
#process.BadPFMuonFilter.muons = cms.InputTag('slimmedMuons')
#process.BadPFMuonFilter.PFCandidates = cms.InputTag('packedPFCandidates')

#process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
#process.BadChargedCandidateFilter.muons = cms.InputTag('slimmedMuons')
#process.BadChargedCandidateFilter.PFCandidates = cms.InputTag('packedPFCandidates')

#task.add(process.BadPFMuonFilter)
#task.add(process.BadChargedCandidateFilter)


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



# make patCandidates
#from PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff import *

# make selectedPatCandidates
#from PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff import *

# make cleanPatCandidates
#from PhysicsTools.PatAlgos.cleaningLayer1.cleanPatCandidates_cff import *

# count cleanPatCandidates (including total number of leptons)
#from PhysicsTools.PatAlgos.selectionLayer1.countPatCandidates_cff import *

#patDefaultSequence = cms.Sequence(
    #patCandidates #*
    #selectedPatCandidates *
    #cleanPatCandidates #*
    #countPatCandidates
#)

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

process.test = cms.EDAnalyzer('LLP2018',
    electrons = cms.untracked.InputTag('slimmedElectrons'),
    eleVetoIdMap = cms.untracked.string('cutBasedElectronID-Fall17-94X-V2-veto'),
)



process.seq = cms.Sequence(
    process.counter *
    process.test
    #process.slimmedJets
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

