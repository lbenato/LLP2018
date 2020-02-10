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
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #test 2017 MC:
            'file:/nfs/dust/cms/user/lbenato/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_privateMC_102X_RECO_v1_generation_forMS_output_100.root'
            
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
    isVBF             = False
    isggH             = True
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

#Puppi, double check if needed????
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
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
'''

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
'''
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
'''


process.load('PhysicsTools.PatAlgos.slimming.slimmedMETs_cfi')
patAlgosToolsTask.add(process.slimmedMETs)


#random stuff failing for no reason
#patAlgosToolsTask.add(process.packedPatJetsAK8)

process.load("PhysicsTools.PatAlgos.slimming.slimming_cff")
patAlgosToolsTask.add(process.slimmingTask)

###MOAR????does this help? no idea..... hoping it will deal with electrons and photons at least
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeCommon, miniAOD_customizeMC
miniAOD_customizeCommon(process)
#miniAOD_customizeMC(process)
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
#  E-MU-GAMMA MODULES   #
#-----------------------#

#skip for 2018 MC?
'''
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,runEnergyCorrections=False,era='2016-Legacy')#era='2018-Prompt'
'''

#muons upstream modules
process.cleanedMuons = cms.EDProducer('PATMuonCleanerBySegments',
                                      src = cms.InputTag('slimmedMuons'),#('calibratedMuons'),#
                                      preselection = cms.string('track.isNonnull'),
                                      passthrough = cms.string('isGlobalMuon && numberOfMatches >= 2'),
                                      fractionOfSharedSegments = cms.double(0.499)
                                      )

task.add(process.cleanedMuons)

#-----------------------#
#         JEC           #
#-----------------------#

# Jet corrector https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrOnTheFly
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')


JECstring = ''
if RunLocal:
    if isData and (isReReco or isReMiniAod):
      if any(s in process.source.fileNames[0] for s in theRunBCD):
        JECstring = "Summer16_23Sep2016BCDV3_DATA" #if isReMiniAod else "Summer16_23Sep2016BCDV3_DATA"
      if any(s in process.source.fileNames[0] for s in theRunEF):
        JECstring = "Summer16_23Sep2016EFV3_DATA" #if isReMiniAod else "Summer16_23Sep2016EFV3_DATA"
      if any(s in process.source.fileNames[0] for s in theRunG):
        JECstring = "Summer16_23Sep2016GV3_DATA" #if isReMiniAod else "Summer16_23Sep2016GV3_DATA"
      if any(s in process.source.fileNames[0] for s in theRunH):
        JECstring = "Summer16_23Sep2016HV3_DATA" #if isReMiniAod else "Summer16_23Sep2016HV3_DATA"
    elif isData and isPromptReco:
        JECstring = "Spring16_25nsV6_DATA"
    elif not isData:
        JECstring = "Summer16_23Sep2016V3_MC"

else:
    JECstring = options.PJECstring
print "JEC ->",JECstring


#-----------------------#
#    Recluster jets     #
#-----------------------#

#Jet labels
if isCalo:
   chosen_JEC = "AK4PFchs"
   chosen_jet_source = 'ak4PFJetsCHSCustom'
   chosen_label = 'Reclustered'
   chosen_pfcand = 'pfCHS'
   chosen_jets = "patJets"+ chosen_label
   pt_AK4 = 5
else:
   chosen_jets = "slimmedJets"
   pt_AK4 = 15

## packedPFCandidates with CHS are used by both AK4 and AK8
process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
task.add(process.pfCHS)

## Filter out neutrinos from packed GenParticles
process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))
task.add(process.packedGenParticlesForJetsNoNu)

## Define new GenJets
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.ak4GenJetsNoNuCustom = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu')
task.add(process.ak4GenJetsNoNuCustom)

#-----------------------#
#  b TAGGING tagInfos   #
#-----------------------#

bTagInfos = [
    'pfImpactParameterTagInfos'
   ,'pfSecondaryVertexTagInfos'
   ,'pfInclusiveSecondaryVertexFinderTagInfos'
]

bTagDiscriminators = [
   'pfCombinedInclusiveSecondaryVertexV2BJetTags',
   'pfCombinedSecondaryVertexV2BJetTags',
   'pfBoostedDoubleSecondaryVertexAK8BJetTags'
   ]

#-----------------------#
#    AK4 only for CALO  # #NEW
#-----------------------#

if isCalo:

   print "% % % % % % % % % % % % % % % % % % % % % % % % % %"
   print "Performing AK4PFchs jet reclustering, pT = "+str(pt_AK4)+" GeV"
   print "% % % % % % % % % % % % % % % % % % % % % % % % % %"

   #Recluster reco jets
   from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
   #non CHS
   #process.ak4PFJets = ak4PFJets.clone(src = 'packedPFCandidates', doAreaFastjet = True, jetPtMin = pt_AK4)
   process.ak4PFJetsCHSCustom = ak4PFJets.clone(src = "pfCHS", doAreaFastjet = True, jetPtMin = pt_AK4)
   task.add(process.ak4PFJetsCHSCustom)

   
   from PhysicsTools.PatAlgos.tools.jetTools import *
   addJetCollection(
      process,
      labelName = chosen_label,#'Reclustered',
      jetSource = cms.InputTag(chosen_jet_source),#reco jets
      pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
      pfCandidates = cms.InputTag(chosen_pfcand),#pfchs substracted
      svSource = cms.InputTag('slimmedSecondaryVertices'),
      btagDiscriminators = list(bTagDiscriminators),#btagging
      btagInfos = bTagInfos,
      jetCorrections = (chosen_JEC, ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),#correct JEC
      genJetCollection = cms.InputTag('ak4GenJetsNoNu'),
      genParticles = cms.InputTag('prunedGenParticles'),
      algo = 'AK',
      rParam = 0.4
      )

   task.add(process.patJetsReclustered)
   task.add(process.patJetCorrFactorsReclustered)
   if not isData:
       task.add(process.patJetPartons)
   task.add(process.patJetFlavourAssociationReclustered)


#-----------------------#
#    AK8 reclustering   # #NEW
#-----------------------#

pt_AK8 = 40

### Gen jets
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.ak8GenJetsNoNuCustom = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu', rParam = 0.8)
task.add(process.ak8GenJetsNoNuCustom)

### Reco AK8 CHS jets
from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
process.ak8PFJetsCHSCustom  = ak4PFJets.clone (src = 'pfCHS', rParam = 0.8, doAreaFastjet = True, jetPtMin = pt_AK8)
task.add(process.ak8PFJetsCHSCustom)

from RecoJets.JetProducers.ak8PFJets_cfi import *
process.ak8PFJetsPuppiCustom = ak8PFJetsPuppi.clone (src = 'puppi', rParam = 0.8, doAreaFastjet = True, jetPtMin = pt_AK8)
task.add(process.ak8PFJetsPuppiCustom)

### Pruned AK8 CHS
process.ak8PFJetsCHSPrunedReclustered = ak8PFJetsCHSPruned.clone(rParam = 0.8, doAreaFastjet = True, src = 'pfCHS', jetPtMin = pt_AK8)
task.add(process.ak8PFJetsCHSPrunedReclustered)

### Pruned AK8 Puppi
process.ak8PFJetsPuppiPrunedReclustered = ak8PFJetsCHSPruned.clone(rParam = 0.8, doAreaFastjet = True, src = 'puppi', jetPtMin = pt_AK8)
task.add(process.ak8PFJetsPuppiPrunedReclustered)

### Softdrop AK8 CHS
process.ak8PFJetsCHSSoftDropReclustered = ak8PFJetsCHSSoftDrop.clone(R0 = 0.8, rParam = 0.8, doAreaFastjet = True, src = 'pfCHS', jetPtMin = pt_AK8)
task.add(process.ak8PFJetsCHSSoftDropReclustered)

### Softdrop AK8 Puppi
process.ak8PFJetsPuppiSoftDropReclustered = ak8PFJetsPuppiSoftDrop.clone(R0 = 0.8, rParam = 0.8, doAreaFastjet = True, src = 'puppi', jetPtMin = pt_AK8)
task.add(process.ak8PFJetsPuppiSoftDropReclustered)

### Pat AK8 CHS jets
#b-tagging must be probably reconsidered
from PhysicsTools.PatAlgos.tools.jetTools import *
addJetCollection(
    process,
    labelName = 'AK8CHSReclustered',
    jetSource = cms.InputTag('ak8PFJetsCHSCustom'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    pfCandidates = cms.InputTag('pfCHS'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    btagDiscriminators = list(bTagDiscriminators),
    btagInfos = bTagInfos,
    jetCorrections = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
    genJetCollection = cms.InputTag('ak8GenJetsNoNuCustom'),
    genParticles = cms.InputTag('prunedGenParticles'),
    algo = 'AK',
    rParam = 0.8
)
task.add(process.patJetsAK8CHSReclustered)

### Pat AK8 Puppi jets
addJetCollection(
    process,
    labelName = 'AK8PuppiReclustered',
    jetSource = cms.InputTag('ak8PFJetsPuppiCustom'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    pfCandidates = cms.InputTag('puppi'),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    btagDiscriminators = list(bTagDiscriminators),
    btagInfos = bTagInfos,
    jetCorrections = ('AK8PFPuppi', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
    genJetCollection = cms.InputTag('ak8GenJetsNoNuCustom'),
    genParticles = cms.InputTag('prunedGenParticles'),
    algo = 'AK',
    rParam = 0.8
)
task.add(process.patJetsAK8PuppiReclustered)

###Softdrop coming next
### Pat CHS softdrop fat jets
addJetCollection(
   process,
   labelName = 'AK8CHSSoftDrop',
   jetSource = cms.InputTag('ak8PFJetsCHSSoftDropReclustered'),
   btagDiscriminators = ['None'],
   jetCorrections = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
   pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
   svSource = cms.InputTag('slimmedSecondaryVertices'),
   genJetCollection = cms.InputTag('ak8GenJetsNoNuCustom'), # AK4 gen jets!
   genParticles = cms.InputTag('prunedGenParticles'),
   getJetMCFlavour = False # jet flavor disabled
   )
task.add(process.patJetsAK8CHSSoftDrop)
task.add(process.selectedPatJetsAK8CHSSoftDrop)
process.selectedPatJetsAK8CHSSoftDrop.cut = cms.string("pt > "+str(pt_AK8))

## Pat soft drop subjets -- these are AK4!
addJetCollection(
   process,
   labelName = 'AK8CHSSoftDropSubjets',
   jetSource = cms.InputTag('ak8PFJetsCHSSoftDropReclustered','SubJets'),
   algo = 'ak',  # needed for subjet flavor clustering
   rParam = 0.8, # needed for subjet flavor clustering
   pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
   #?#pfCandidates = cms.InputTag(chosen_pfcand),#pfchs substracted
   svSource = cms.InputTag('slimmedSecondaryVertices'),
   btagDiscriminators = ['pfCombinedSecondaryVertexV2BJetTags', 'pfCombinedInclusiveSecondaryVertexV2BJetTags'],
   jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
   explicitJTA = True,  # needed for subjet b tagging
   svClustering = True, # needed for subjet b tagging
   genJetCollection = cms.InputTag('ak4GenJetsNoNuCustom'), # AK4 gen jets!
   genParticles = cms.InputTag('prunedGenParticles'),
   fatJets=cms.InputTag('ak8PFJetsCHSCustom'), # needed for subjet flavor clustering
   groomedFatJets=cms.InputTag('ak8PFJetsCHSSoftDropReclustered') # needed for subjet flavor clustering
)
task.add(process.patJetsAK8CHSSoftDropSubjets)

### Groomed masses CHS
from RecoJets.JetProducers.ak8PFJetsCHS_groomingValueMaps_cfi import ak8PFJetsCHSPrunedMass, ak8PFJetsCHSSoftDropMass
process.ak8PFJetsCHSPrunedMassReclustered = ak8PFJetsCHSPrunedMass.clone(src = cms.InputTag("ak8PFJetsCHSCustom"),matched = cms.InputTag("ak8PFJetsCHSPrunedReclustered"),)
process.ak8PFJetsCHSSoftDropMassReclustered = ak8PFJetsCHSSoftDropMass.clone(src = cms.InputTag("ak8PFJetsCHSCustom"),matched = cms.InputTag("ak8PFJetsCHSSoftDropReclustered"),)
process.patJetsAK8CHSReclustered.userData.userFloats.src += ['ak8PFJetsCHSPrunedMassReclustered','ak8PFJetsCHSSoftDropMassReclustered']
task.add(process.ak8PFJetsCHSPrunedMassReclustered)
task.add(process.ak8PFJetsCHSSoftDropMassReclustered)

### Groomed masses Puppi
from RecoJets.JetProducers.ak8PFJetsPuppi_groomingValueMaps_cfi import ak8PFJetsPuppiSoftDropMass
process.ak8PFJetsPuppiPrunedMassReclustered = ak8PFJetsCHSPrunedMass.clone(src = cms.InputTag("ak8PFJetsPuppiCustom"),matched = cms.InputTag("ak8PFJetsPuppiPrunedReclustered"),)
process.ak8PFJetsPuppiSoftDropMassReclustered = ak8PFJetsPuppiSoftDropMass.clone(src = cms.InputTag("ak8PFJetsPuppiCustom"),matched = cms.InputTag("ak8PFJetsPuppiSoftDropReclustered"),)
process.patJetsAK8PuppiReclustered.userData.userFloats.src += ['ak8PFJetsPuppiPrunedMassReclustered','ak8PFJetsPuppiSoftDropMassReclustered']
task.add(process.ak8PFJetsPuppiPrunedMassReclustered)
task.add(process.ak8PFJetsPuppiSoftDropMassReclustered)

## N-subjettiness
from RecoJets.JetProducers.nJettinessAdder_cfi import *
process.NjettinessAK8Reclustered = Njettiness.clone(src='ak8PFJetsCHSCustom')#src='ak8PFJets', cone=0.8)
process.NjettinessAK8Reclustered.cone = cms.double(0.8)
process.patJetsAK8CHSReclustered.userData.userFloats.src += ['NjettinessAK8Reclustered:tau1','NjettinessAK8Reclustered:tau2','NjettinessAK8Reclustered:tau3']
task.add(process.NjettinessAK8Reclustered)

process.NjettinessAK8PuppiReclustered = Njettiness.clone(src='ak8PFJetsPuppiCustom')#src='ak8PFJets', cone=0.8)
process.NjettinessAK8PuppiReclustered.cone = cms.double(0.8)
process.patJetsAK8PuppiReclustered.userData.userFloats.src += ['NjettinessAK8PuppiReclustered:tau1','NjettinessAK8PuppiReclustered:tau2','NjettinessAK8PuppiReclustered:tau3']
task.add(process.NjettinessAK8PuppiReclustered)


## PF AK8 matching to PF Puppi AK8
process.ak8PFJetsPuppiValueMap = cms.EDProducer("RecoJetToPatJetDeltaRValueMapProducer",
                                                src = cms.InputTag("ak8PFJetsCHSCustom"),#CHS
                                                matched = cms.InputTag("patJetsAK8PuppiReclustered"),#PUPPI
                                                distMax = cms.double(0.8),
                                                values = cms.vstring([
         'userFloat("NjettinessAK8PuppiReclustered:tau1")',
         'userFloat("NjettinessAK8PuppiReclustered:tau2")',
         'userFloat("NjettinessAK8PuppiReclustered:tau3")',
         'userFloat("ak8PFJetsPuppiSoftDropMassReclustered")',
         'userFloat("ak8PFJetsPuppiPrunedMassReclustered")',
         'pt','eta','phi','mass'
         ]),
                                                valueLabels = cms.vstring( [
         'NjettinessAK8PuppiTau1Reclustered',
         'NjettinessAK8PuppiTau2Reclustered',
         'NjettinessAK8PuppiTau3Reclustered',
         'ak8PFJetsPuppiSoftDropMassReclustered',
         'ak8PFJetsPuppiPrunedMassReclustered',
         'pt','eta','phi','mass'
         ])
                                                )

task.add(process.ak8PFJetsPuppiValueMap)

#Adding values to AK8
process.patJetsAK8CHSReclustered.userData.userFloats.src += [cms.InputTag('ak8PFJetsPuppiValueMap','NjettinessAK8PuppiTau1Reclustered'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','NjettinessAK8PuppiTau2Reclustered'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','NjettinessAK8PuppiTau3Reclustered'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','ak8PFJetsPuppiSoftDropMassReclustered'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','ak8PFJetsPuppiPrunedMassReclustered'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','pt'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','eta'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','phi'),
                                                      cms.InputTag('ak8PFJetsPuppiValueMap','mass'),
                                                      ]


#-----------------------#
#       B-Tag           #
#-----------------------#

from PhysicsTools.PatAlgos.tools.jetTools import *

#Seth
jetSource = chosen_jets
jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
pfCandidates = 'particleFlow'#'packedPFCandidates'#???
pvSource = 'offlinePrimaryVertices'#'offlineSlimmedPrimaryVertices'#???
svSource = 'inclusiveCandidateSecondaryVertices'#'slimmedSecondaryVertices'#???
muSource = 'slimmedMuons'
elSource = 'slimmedElectrons'
#runIVF   = False

bTagInfos = [
    'pfImpactParameterTagInfos'
   ,'pfSecondaryVertexTagInfos'
   ,'pfInclusiveSecondaryVertexFinderTagInfos'
   ,'pfSecondaryVertexNegativeTagInfos'
   ,'pfInclusiveSecondaryVertexFinderNegativeTagInfos'
   ,'softPFMuonsTagInfos'
   ,'softPFElectronsTagInfos'
   ,'pfInclusiveSecondaryVertexFinderCvsLTagInfos'
   ,'pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos'
   ,'pfDeepCSVTagInfos' #Imperial
#   ,'pfDeepFlavourTagInfos' # not available for 2016
]


bTagDiscriminators = set([
    'pfJetBProbabilityBJetTags'
   ,'pfJetProbabilityBJetTags'
   ,'pfPositiveOnlyJetBProbabilityBJetTags'
   ,'pfPositiveOnlyJetProbabilityBJetTags'
   ,'pfNegativeOnlyJetBProbabilityBJetTags'
   ,'pfNegativeOnlyJetProbabilityBJetTags'
   ,'pfTrackCountingHighPurBJetTags'
   ,'pfTrackCountingHighEffBJetTags'
   ,'pfNegativeTrackCountingHighPurBJetTags'
   ,'pfNegativeTrackCountingHighEffBJetTags'
   ,'pfSimpleSecondaryVertexHighEffBJetTags'
   ,'pfSimpleSecondaryVertexHighPurBJetTags'
   ,'pfNegativeSimpleSecondaryVertexHighEffBJetTags'
   ,'pfNegativeSimpleSecondaryVertexHighPurBJetTags'
   ,'pfCombinedSecondaryVertexV2BJetTags'
   ,'pfPositiveCombinedSecondaryVertexV2BJetTags'
   ,'pfNegativeCombinedSecondaryVertexV2BJetTags'
   ,'pfCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'softPFMuonBJetTags'
   ,'positiveSoftPFMuonBJetTags'
   ,'negativeSoftPFMuonBJetTags'
   ,'softPFElectronBJetTags'
   ,'positiveSoftPFElectronBJetTags'
   ,'negativeSoftPFElectronBJetTags'
   ,'pfCombinedMVAV2BJetTags'
   ,'pfNegativeCombinedMVAV2BJetTags'
   ,'pfPositiveCombinedMVAV2BJetTags'
   ,'pfCombinedCvsBJetTags'
   ,'pfNegativeCombinedCvsBJetTags'
   ,'pfPositiveCombinedCvsBJetTags'
   ,'pfCombinedCvsLJetTags'
   ,'pfNegativeCombinedCvsLJetTags'
   ,'pfPositiveCombinedCvsLJetTags'
  #   # DeepCSV # From here not available for 2016
  # , 'pfDeepCSVJetTags:probudsg'
  # , 'pfDeepCSVJetTags:probb'
  # , 'pfDeepCSVJetTags:probc'
  # , 'pfDeepCSVJetTags:probbb'
  # , 'pfNegativeDeepCSVJetTags:probudsg'
  # , 'pfNegativeDeepCSVJetTags:probb'
  # , 'pfNegativeDeepCSVJetTags:probc'
  # , 'pfNegativeDeepCSVJetTags:probbb'
  # , 'pfPositiveDeepCSVJetTags:probudsg'
  # , 'pfPositiveDeepCSVJetTags:probb'
  # , 'pfPositiveDeepCSVJetTags:probc'
  # , 'pfPositiveDeepCSVJetTags:probbb'
  #   # DeepFlavour
  # , 'pfDeepFlavourJetTags:probb'
  # , 'pfDeepFlavourJetTags:probbb'
  # , 'pfDeepFlavourJetTags:problepb'
  # , 'pfDeepFlavourJetTags:probc'
  # , 'pfDeepFlavourJetTags:probuds'
  # , 'pfDeepFlavourJetTags:probg'
  # , 'pfNegativeDeepFlavourJetTags:probb'
  # , 'pfNegativeDeepFlavourJetTags:probbb'
  # , 'pfNegativeDeepFlavourJetTags:problepb'
  # , 'pfNegativeDeepFlavourJetTags:probc'
  # , 'pfNegativeDeepFlavourJetTags:probuds'
  # , 'pfNegativeDeepFlavourJetTags:probg'
])


useExplicitJTA = False #? try true also!
postfix = "" #"Update"


#-----------------------#
#       Vertices        #
#-----------------------#

# taken from: https://github.com/cms-sw/cmssw/blob/02d4198c0b6615287fd88e9a8ff650aea994412e/PhysicsTools/PatAlgos/test/btag-from-packedPat.py
#Info: these two producers seem not to be used
#process.unpackTV = cms.EDProducer('PATTrackAndVertexUnpacker',
# slimmedVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
# slimmedSecondaryVertices = cms.InputTag("slimmedSecondaryVertices"),
# additionalTracks= cms.InputTag("lostTracks"),
# packedCandidates = cms.InputTag("packedPFCandidates")
#)
#process.jetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
#    tracks = cms.InputTag("unpackTV"),
#    coneSize = cms.double(0.4),
#    useAssigned = cms.bool(True),
#    pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
#    #jets = cms.InputTag(chosen_jets if isCalo else "slimmedJets")
#    jets = cms.InputTag("slimmedJets")#!!!!wrong
#)



postfix = 'Final'#TODO

updateJetCollection(
    process,
    jetSource = cms.InputTag(jetSource),
    jetCorrections = jetCorrectionsAK4,
    pfCandidates = cms.InputTag(pfCandidates),
    pvSource = cms.InputTag(pvSource),
    svSource = cms.InputTag(svSource),
    muSource = cms.InputTag(muSource),
    elSource = cms.InputTag(elSource),
    #runIVF   = runIVF,
    btagInfos = bTagInfos,
    btagDiscriminators = list(bTagDiscriminators),
    explicitJTA = useExplicitJTA,
    postfix = postfix#,
    )

for m in ['updatedPatJets'+postfix, 'updatedPatJetsTransientCorrected'+postfix]:
    setattr( getattr(process,m), 'addTagInfos', cms.bool(True) )


#Imperial
process.updatedPatJetsFinal.addBTagInfo = cms.bool(True)
process.updatedPatJetsFinal.addDiscriminators = cms.bool(True)
process.updatedPatJetsFinal.addJetCorrFactors = cms.bool(True)
process.updatedPatJetsFinal.addTagInfos = cms.bool(True)
#Imperial
process.updatedPatJetsTransientCorrectedFinal.addBTagInfo = cms.bool(True)
process.updatedPatJetsTransientCorrectedFinal.addDiscriminators = cms.bool(True)
process.updatedPatJetsTransientCorrectedFinal.addJetCorrFactors = cms.bool(True)
process.updatedPatJetsTransientCorrectedFinal.addTagInfos = cms.bool(True)

jets_after_btag_tools = 'updatedPatJetsTransientCorrected'+postfix

task.add(process.pfImpactParameterTagInfosFinal)
task.add(process.pfInclusiveSecondaryVertexFinderTagInfosFinal)
task.add(process.pfDeepCSVTagInfosFinal)
task.add(process.updatedPatJetsFinal)
task.add(process.updatedPatJetsTransientCorrectedFinal)

#---------------------------------------#
#   B Tag info for softdrop sub jets    #
#---------------------------------------#

jetSourceSoftDrop = "selectedPatJetsAK8CHSSoftDropSubjets"
postfixSoftDrop = "SoftDropSubjetsLisa"

updateJetCollection(
    process,
    jetSource = cms.InputTag(jetSourceSoftDrop),
    jetCorrections = jetCorrectionsAK4,
    pfCandidates = cms.InputTag(pfCandidates),
    pvSource = cms.InputTag(pvSource),
    svSource = cms.InputTag(svSource),
    muSource = cms.InputTag(muSource),
    elSource = cms.InputTag(elSource),
    btagInfos = bTagInfos,
    btagDiscriminators = list(bTagDiscriminators),
    explicitJTA = useExplicitJTA,
    postfix = postfixSoftDrop,
    )

for m in ['updatedPatJets'+postfixSoftDrop, 'updatedPatJetsTransientCorrected'+postfixSoftDrop]:
    setattr( getattr(process,m), 'addTagInfos', cms.bool(True) )

soft_drop_subjets_after_btag_tools = 'updatedPatJetsTransientCorrected'+postfixSoftDrop

task.add(process.updatedPatJetsSoftDropSubjetsLisa)
task.add(process.updatedPatJetsTransientCorrectedSoftDropSubjetsLisa)


## Establish references between PATified fat jets and subjets using the BoostedJetMerger
process.slimmedJetsAK8CHSSoftDropPacked = cms.EDProducer("BoostedJetMerger",
        jetSrc=cms.InputTag("selectedPatJetsAK8CHSSoftDrop"),#here the selected pat softdrop fat jets
        subjetSrc=cms.InputTag(soft_drop_subjets_after_btag_tools),#("selectedPatJetsAK8CHSSoftDropSubjets")#("slimmedJetsAK8CHSSoftDropSubjets")#here the slimmed pat softdrop subjets
    )

task.add(process.slimmedJetsAK8CHSSoftDropPacked)

process.packedPatJetsAK8Reclustered = cms.EDProducer("JetSubstructurePacker",
            jetSrc = cms.InputTag("patJetsAK8CHSReclustered"),
            distMax = cms.double(0.8),
            algoTags = cms.VInputTag(
                # NOTE: For an optimal storage of the AK8 jet daughters, the first subjet collection listed here should be
                #       derived from AK8 jets, i.e., subjets should contain either all or a subset of AK8 constituents.
                #       The PUPPI collection has its own pointers to its own PUPPI constituents.
                cms.InputTag("slimmedJetsAK8CHSSoftDropPacked"),
                #cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked")
            ),
            algoLabels = cms.vstring(
                'SoftDrop',
                #'SoftDropPuppi'
                ),
            fixDaughters = cms.bool(False),#(True),
            packedPFCandidates = cms.InputTag("packedPFCandidates"),
    )

task.add(process.packedPatJetsAK8Reclustered)

#patJetsAK8Reclustered
chosen_AK8 = "packedPatJetsAK8Reclustered" # including SoftDrop info
#chosen_AK8 = "patJetsAK8CHSReclustered"#'slimmedJetsAK8'


jets_to_be_used = jets_after_btag_tools #FIX later!

#-----------------------#
#    Imperial Tagger    #
#-----------------------#

process.pfXTagInfos = cms.EDProducer("XTagInfoProducer",
    jets = cms.InputTag(jets_after_btag_tools),
    shallow_tag_infos = cms.InputTag('pfDeepCSVTagInfosFinal'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices")
)

process.pfXTags = cms.EDProducer("XTagProducer",
    graph_path=cms.FileInPath("LLPReco/XTagProducer/data/da.pb"),
    src=cms.InputTag("pfXTagInfos"),
    ctau_values=cms.vdouble(-2., 0., 1., 2., 3.), # provide log(ctau/1mm) to be evaluated: i.e. 10 mum, 1 mm and 1 m here
    ctau_descriptors=cms.vstring("0p01", "1", "10", "100", "1000") # provide log(ctau/1mm) to be evaluated: i.e. 1 mum, 1 mm and 1 m here
)

#task.add(process.patJetCorrFactors)
task.add(process.pfXTagInfos)
task.add(process.pfXTags)

#---------------------------------#
#       PU Jet ID-a-la-2016       #
#---------------------------------#
#This is not working... schade
'''
from RecoJets.JetProducers.PileupJetID_cfi import pileupJetId
process.pileupJetId = pileupJetId.clone(
  jets=cms.InputTag(jets_after_btag_tools),
  inputIsCorrected=True,
  applyJec=True,
  vertexes=cms.InputTag("offlineSlimmedPrimaryVertices")
  )
task.add(process.pileupJetId)

from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJetCorrFactors, updatedPatJets
process.patJetCorrFactorsReapplyJEC = updatedPatJetCorrFactors.clone(
  src = cms.InputTag(jets_after_btag_tools),
  levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
  )
task.add(process.patJetCorrFactorsReapplyJEC)

process.updatedJetsPUID = updatedPatJets.clone(
  jetSource = cms.InputTag(jets_after_btag_tools),
  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
  )

process.updatedJetsPUID.userData.userFloats.src += ['pileupJetId:fullDiscriminant']
process.updatedJetsPUID.userData.userInts.src += ['pileupJetId:fullId']

task.add(process.updatedJetsPUID)

jets_to_be_used = "updatedJetsFinal"
jets_to_be_used = jets_after_btag_tools #FIX later!
jets_to_be_used = "updatedJetsPUID" #Test, is this readable?
'''
jets_to_be_used = jets_after_btag_tools #FIX later!


#-----------------------#
#       TEST            #
#-----------------------#

process.test = cms.EDAnalyzer('LLP2018',
    electrons = cms.untracked.InputTag('slimmedElectrons'),
    genjets = cms.InputTag('slimmedGenJets'),#('ak4GenJetsNoNu'),
    jets = cms.InputTag('patJets'),#('packedPatJetsAK8Reclustered'),
    jets2 = cms.InputTag(jets_to_be_used),
    met = cms.InputTag('slimmedMETs'),
    eleVetoIdMap = cms.untracked.string('cutBasedElectronID-Fall17-94X-V2-veto'),
)

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
#   TrigGen ANALYZER    #
#-----------------------#

process.triggen = cms.EDAnalyzer('TriggerGenNtuplizer',
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
'HLT_HT350_DisplacedDijet40_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v', 'HLT_HT650_DisplacedDijet80_Inclusive_v', 'HLT_HT750_DisplacedDijet80_Inclusive_v',
'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
'HLT_PFMETNoMu1240_PFMHTNoMu140_IDTight_v',
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


#-----------------------#
#       ANALYZER        #
#-----------------------#

process.ntuple = cms.EDAnalyzer('Ntuplizer',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        lheProduct = cms.InputTag('externalLHEProducer'),
        genParticles = cms.InputTag('prunedGenParticles'),
        pdgId = cms.vint32(5,9000006,23,24,25),#(1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 23, 24, 25, 36, 39, 1000022, 9100000, 9000001, 9000002, 9100012, 9100022, 9900032, 1023),
        status = cms.vint32(22,23),
        samplesDYJetsToLL = cms.vstring(),
        samplesZJetsToNuNu = cms.vstring(),
        samplesWJetsToLNu = cms.vstring(),
        samplesDir = cms.string('data/Stitch/'),
        sample = cms.string("" ), #( sample )
        ewkFile = cms.string('data/scalefactors_v4.root'),
        applyEWK = cms.bool(False),#(True if sample.startswith('DYJets') or sample.startswith('WJets') else False),
        applyTopPtReweigth = cms.bool(False),#(True if sample.startswith('TT_') else False),
        pythiaLOSample = cms.bool(True if noLHEinfo else False),#(True if isDibosonInclusive else False),
    ),
    pileupSet = cms.PSet(
        pileup = cms.InputTag('slimmedAddPileupInfo'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        dataFileName     = cms.string('data/PU_69200_ReReco.root'),#updated
        dataFileNameUp   = cms.string('data/PU_72380_ReReco.root'),#updated
        dataFileNameDown = cms.string('data/PU_66020_ReReco.root'),#updated
        mcFileName = cms.string('data/PU_MC_Moriond17.root'),#updated
        dataName = cms.string('pileup'),
        mcName = cms.string('2016_25ns_Moriond17MC_PoissonOOTPU'),#updated
    ),
    triggerSet = cms.PSet(
        trigger = cms.InputTag('TriggerResults', '', triggerTag),
        paths = cms.vstring(
*[
#2018 menu
'HLT_HT430_DisplacedDijet40_DisplacedTrack_v',
'HLT_HT430_DisplacedDijet60_DisplacedTrack_v',
'HLT_HT500_DisplacedDijet40_DisplacedTrack_v',
'HLT_HT650_DisplacedDijet60_Inclusive_v',
'HLT_AK8PFHT800_TrimMass50_v',
'HLT_AK8PFHT850_TrimMass50_v',
'HLT_AK8PFHT900_TrimMass50_v',
'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17_v',
'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1_v',
'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2_v',
'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4_v',
'HLT_AK8PFJet360_TrimMass30_v',
'HLT_AK8PFJet380_TrimMass30_v',
'HLT_AK8PFJet400_TrimMass30_v',
'HLT_AK8PFJet420_TrimMass30_v',
'HLT_AK8PFJet500_v',
'HLT_AK8PFJet550_v',
'HLT_AK8PFJetFwd500_v',
'HLT_CaloJet500_NoJetID_v',
'HLT_CaloJet550_NoJetID_v',
'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v',
'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v',
'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v',
'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v',
'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v',
'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v',
'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v',
'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v',
'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v',
'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v',
'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v',
'HLT_PFJet500_v',
'HLT_PFJet550_v',
'HLT_PFJetFwd450_v',
'HLT_PFJetFwd500_v',
'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v',
'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v',
'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v',
'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v',
'HLT_Rsq0p35_v',
'HLT_Rsq0p40_v',
'HLT_RsqMR300_Rsq0p09_MR200_4jet_v',
'HLT_RsqMR300_Rsq0p09_MR200_v',
'HLT_RsqMR320_Rsq0p09_MR200_4jet_v',
'HLT_RsqMR320_Rsq0p09_MR200_v',
'HLT_CaloMET350_HBHECleaned_v',
'HLT_DiJet110_35_Mjj650_PFMET110_v',
'HLT_DiJet110_35_Mjj650_PFMET120_v',
'HLT_DiJet110_35_Mjj650_PFMET130_v',
'HLT_MET105_IsoTrk50_v',
'HLT_MET120_IsoTrk50_v',
'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
'HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v',
'HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v',
'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v',
'HLT_PFMET120_PFMHT120_IDTight_v',
'HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v',
'HLT_PFMET130_PFMHT130_IDTight_v',
'HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v',
'HLT_PFMET140_PFMHT140_IDTight_v',
'HLT_PFMET200_HBHE_BeamHaloCleaned_v',
'HLT_PFMET250_HBHECleaned_v',
'HLT_PFMET300_HBHECleaned_v',
'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v',
'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
'HLT_TripleJet110_35_35_Mjj650_PFMET110_v',
'HLT_TripleJet110_35_35_Mjj650_PFMET120_v',
'HLT_TripleJet110_35_35_Mjj650_PFMET130_v',
###production for MET
'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
]
        ),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter','Flag_badMuons','Flag_duplicateMuons','Flag_noBadMuons') if isReMiniAod else cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter'),
        prescales = cms.InputTag('patTrigger','',''),
        l1Minprescales = cms.InputTag('patTrigger','l1min',''),
        l1Maxprescales = cms.InputTag('patTrigger','l1max',''),
        objects = cms.InputTag('slimmedPatTrigger' if is2017 else 'selectedPatTrigger','',''),
        badPFMuonFilter = cms.InputTag("BadPFMuonFilter"),
        badChCandFilter = cms.InputTag("BadChargedCandidateFilter"),
        l1Gt = cms.InputTag("gtStage2Digis"),
        l1filters = cms.vstring('hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300','hltL1sDoubleJetC112','hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF','hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet','hltL1sSingleMu22','hltL1sV0SingleMu22IorSingleMu25','hltL1sZeroBias','hltL1sSingleJet60','hltL1sSingleJet35','hltTripleJet50','hltDoubleJet65','hltSingleJet80','hltVBFFilterDisplacedJets'),
    ),
    allJetSet = cms.PSet(
        jets = cms.InputTag(jets_to_be_used),#(jets_after_btag_tools),#('updatedPatJetsTransientCorrected'+postfix),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(15.),
        jet2pt = cms.double(15.),
        jeteta = cms.double(5.2),
        addQGdiscriminator = cms.bool(False),
        recalibrateJets = cms.bool(False),#now the JEC are wrong
        recalibrateMass = cms.bool(False),
        recalibratePuppiMass = cms.bool(False),
        softdropPuppiMassString = cms.string("ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMass" if pt_AK8<170 else "ak8PFJetsPuppiSoftDropMass"),
        smearJets = cms.bool(True),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        rho = cms.InputTag('fixedGridRhoFastjetAll'),
        jecUncertaintyDATA = cms.string('data/%s/%s_Uncertainty_AK4PFchs.txt' % (JECstring, JECstring)),#updating
        jecUncertaintyMC = cms.string('data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt'),#updating
        jecCorrectorDATA = cms.vstring(#updating
            'data/%s/%s_L1FastJet_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2Relative_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK4PFchs.txt' % (JECstring, JECstring),
        ),
        jecCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
        ),
        massCorrectorDATA = cms.vstring(#updating!!!
            'data/%s/%s_L2Relative_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK4PFchs.txt' % (JECstring, JECstring),
        ),
        massCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
        ),
        massCorrectorPuppi = cms.string('data/puppiCorrSummer16.root'),#updating
        reshapeBTag = cms.bool(True),
        btag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        btagDB = cms.string('data/CSVv2_Moriond17_B_H.csv'),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'LLP'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string('data/JER/Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt'),#v10 is the latest
        jerNameSf = cms.string('data/JER/Spring16_25nsV10_MC_SF_AK4PFchs.txt'),#v10 is the latest
    ),
    chsJetSet = cms.PSet(
        jets = cms.InputTag(jets_to_be_used),#(jets_after_btag_tools),#('updatedPatJetsTransientCorrected'+postfix),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(pt_AK4),
        jet2pt = cms.double(pt_AK4),
        jeteta = cms.double(2.4),
        addQGdiscriminator = cms.bool(False),
        recalibrateJets = cms.bool(False),#now the JEC are wrong
        recalibrateMass = cms.bool(False),
        recalibratePuppiMass = cms.bool(False),
        softdropPuppiMassString = cms.string("ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMass" if pt_AK8<170 else "ak8PFJetsPuppiSoftDropMass"),
        smearJets = cms.bool(True),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        rho = cms.InputTag('fixedGridRhoFastjetAll'),
        jecUncertaintyDATA = cms.string('data/%s/%s_Uncertainty_AK4PFchs.txt' % (JECstring, JECstring)),#updating
        jecUncertaintyMC = cms.string('data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt'),#updating
        jecCorrectorDATA = cms.vstring(#updating
            'data/%s/%s_L1FastJet_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2Relative_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK4PFchs.txt' % (JECstring, JECstring),
        ),
        jecCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
        ),
        massCorrectorDATA = cms.vstring(#updating!!!
            'data/%s/%s_L2Relative_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK4PFchs.txt' % (JECstring, JECstring),
        ),
        massCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
        ),
        massCorrectorPuppi = cms.string('data/puppiCorrSummer16.root'),#updating
        reshapeBTag = cms.bool(True),
        btag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        btagDB = cms.string('data/CSVv2_Moriond17_B_H.csv'),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'LLP'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string('data/JER/Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt'),#v10 is the latest
        jerNameSf = cms.string('data/JER/Spring16_25nsV10_MC_SF_AK4PFchs.txt'),#v10 is the latest
    ),
    vbfJetSet = cms.PSet(
        jets = cms.InputTag(jets_to_be_used),#(jets_after_btag_tools),#('updatedPatJetsTransientCorrected'+postfix),
        jetid = cms.int32(3), # 0: no selection, 1: loose, 2: medium, 3: tight
        #jet1pt = cms.double(30.),#https://indico.desy.de/indico/event/20983/contribution/0/material/slides/0.pdf
        #jet2pt = cms.double(30.),#https://indico.desy.de/indico/event/20983/contribution/0/material/slides/0.pdf
        #new cut, motivated by calo-lifetimes trigger path
        #still to be optimized!
        jet1pt = cms.double(20.),
        jet2pt = cms.double(20.),
        jeteta = cms.double(5.2),
        addQGdiscriminator = cms.bool(False),
        recalibrateJets = cms.bool(False),#now the JEC are wrong
        recalibrateMass = cms.bool(False),
        recalibratePuppiMass = cms.bool(False),
        softdropPuppiMassString = cms.string("ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMass" if pt_AK8<170 else "ak8PFJetsPuppiSoftDropMass"),
        smearJets = cms.bool(True),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),# if not isAOD else 'offlinePrimaryVertices'),
        rho = cms.InputTag('fixedGridRhoFastjetAll'),
        jecUncertaintyDATA = cms.string('data/%s/%s_Uncertainty_AK4PFchs.txt' % (JECstring, JECstring)),#updating
        jecUncertaintyMC = cms.string('data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK4PFchs.txt'),#updating
        jecCorrectorDATA = cms.vstring(#updating
            'data/%s/%s_L1FastJet_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2Relative_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK4PFchs.txt' % (JECstring, JECstring),
        ),
        jecCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
        ),
        massCorrectorDATA = cms.vstring(#updating!!!
            'data/%s/%s_L2Relative_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK4PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK4PFchs.txt' % (JECstring, JECstring),
        ),
        massCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt',
        ),
        massCorrectorPuppi = cms.string('data/puppiCorrSummer16.root'),#updating
        reshapeBTag = cms.bool(True),
        btag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        btagDB = cms.string('data/CSVv2_Moriond17_B_H.csv'),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', 'LLP'),
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string('data/JER/Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt'),#v10 is the latest
        jerNameSf = cms.string('data/JER/Spring16_25nsV10_MC_SF_AK4PFchs.txt'),#v10 is the latest
    ),
    chsFatJetSet = cms.PSet(
        jets = cms.InputTag(chosen_AK8),#('slimmedJetsAK8'),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(pt_AK8),
        jet2pt = cms.double(pt_AK8),
        jeteta = cms.double(2.4),
        addQGdiscriminator = cms.bool(False),
        recalibrateJets = cms.bool(False),#now the JEC are wrong
        recalibrateMass = cms.bool(False),#now the JEC are wrong
        recalibratePuppiMass = cms.bool(True),#(False),
        softdropPuppiMassString = cms.string("ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMass" if pt_AK8<170 else "ak8PFJetsPuppiSoftDropMass"),
        smearJets = cms.bool(True),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        rho = cms.InputTag('fixedGridRhoFastjetAll'),
        jecUncertaintyDATA = cms.string('data/%s/%s_Uncertainty_AK8PFchs.txt' % (JECstring, JECstring)),#updating
        jecUncertaintyMC = cms.string('data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK8PFchs.txt'),#updating
        jecCorrectorDATA = cms.vstring(#updating
            'data/%s/%s_L1FastJet_AK8PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2Relative_AK8PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK8PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK8PFchs.txt' % (JECstring, JECstring),
        ),
        jecCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK8PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK8PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK8PFchs.txt',
        ),
        massCorrectorDATA = cms.vstring(#updating!!!
            'data/%s/%s_L2Relative_AK8PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L3Absolute_AK8PFchs.txt' % (JECstring, JECstring),
            'data/%s/%s_L2L3Residual_AK8PFchs.txt' % (JECstring, JECstring),
        ),
        massCorrectorMC = cms.vstring(#updating!!!
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK8PFchs.txt',
            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK8PFchs.txt',
        ),
        massCorrectorPuppi = cms.string('data/puppiCorrSummer16.root'),#updating
        reshapeBTag = cms.bool(True),
        btag = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
        btagDB = cms.string('data/CSVv2_Moriond17_B_H.csv'),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'LLP'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string('data/JER/Spring16_25nsV10_MC_PtResolution_AK8PFchs.txt'),#v10 is the latest
        jerNameSf = cms.string('data/JER/Spring16_25nsV10_MC_SF_AK8PFchs.txt'),#v10 is the latest
    ),
#    caloJetSet = cms.PSet(
#        jets = cms.InputTag('ak4CaloJets'),
#        jet1pt = cms.double(15.),
#        jet2pt = cms.double(15.),
#        jeteta = cms.double(2.4),
#        recalibrateJets = cms.bool(True),
#        recalibrateMass = cms.bool(False),
#        smearJets = cms.bool(False),
#        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
#        rho = cms.InputTag('fixedGridRhoFastjetAll'),
#        jecUncertaintyDATA = cms.string('data/%s/%s_Uncertainty_AK4Calo.txt' % (JECstring, JECstring)),
#        jecUncertaintyMC = cms.string('data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_Uncertainty_AK4Calo.txt'),
#        jecCorrectorDATA = cms.vstring(
#            'data/%s/%s_L1FastJet_AK4Calo.txt' % (JECstring, JECstring),
#            'data/%s/%s_L2Relative_AK4Calo.txt' % (JECstring, JECstring),
#            'data/%s/%s_L3Absolute_AK4Calo.txt' % (JECstring, JECstring),
#            'data/%s/%s_L2L3Residual_AK4Calo.txt' % (JECstring, JECstring),
#        ),
#        jecCorrectorMC = cms.vstring(
#            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L1FastJet_AK4Calo.txt',
#            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4Calo.txt',
#            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4Calo.txt',
#        ),
#        massCorrectorDATA = cms.vstring(
#            'data/%s/%s_L2Relative_AK4Calo.txt' % (JECstring, JECstring),
#            'data/%s/%s_L3Absolute_AK4Calo.txt' % (JECstring, JECstring),
#            'data/%s/%s_L2L3Residual_AK4Calo.txt' % (JECstring, JECstring),
#        ),
#        massCorrectorMC = cms.vstring(                                                         #
#            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L2Relative_AK4Calo.txt',
#            'data/Summer16_23Sep2016V3_MC/Summer16_23Sep2016V3_MC_L3Absolute_AK4Calo.txt',
#        ),
#        jerNameRes = cms.string('data/JER/Spring16_25nsV10_MC_PtResolution_AK8PF.txt'),#NOT PROVIDED FOR CALO JETS
#        jerNameSf = cms.string('data/JER/Spring16_25nsV10_MC_SF_AK8PF.txt'),#NOT PROVIDED FOR CALO JETS
#    ),
    electronSet = cms.PSet(
        electrons = cms.InputTag('slimmedElectrons'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        eleVetoId = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),#see https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2#Accessing_ID_result
        eleLooseId = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
        eleMediumId = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
        eleTightId = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
        eleHEEPId = cms.string('heepElectronID-HEEPV70'),
        eleMVANonTrigMediumId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'),#see https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2#Accessing_ID_result
        eleMVANonTrigTightId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
        eleMVATrigMediumId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'), ### NOTE -> SAME AS NON-TRIG IN 2017
        eleMVATrigTightId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'), ### NOTE -> SAME AS NON-TRIG IN 2017
        eleEcalRecHitCollection = cms.InputTag("reducedEgamma:reducedEBRecHits"),
        eleSingleTriggerIsoFileName = cms.string('data/SingleEleTriggerEff.root'),
        eleSingleTriggerFileName = cms.string('data/eleTriggerEff_MORIOND17.root'),
        eleVetoIdFileName = cms.string('data/eleVetoIDSF_MORIOND17.root'),
        eleLooseIdFileName = cms.string('data/eleLooseIDSF_MORIOND17.root'),
        eleMediumIdFileName = cms.string('data/eleMediumIDSF_MORIOND17.root'),
        eleTightIdFileName = cms.string('data/eleTightIDSF_MORIOND17.root'),
        eleMVATrigMediumIdFileName = cms.string('data/eleMVA90IDSF_MORIOND17.root'),
        eleMVATrigTightIdFileName = cms.string('data/eleMVA80IDSF_MORIOND17.root'),
        eleRecoEffFileName = cms.string('data/eleRecoSF_MORIOND17.root'),
        eleScaleSmearCorrectionName = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Moriond17_23Jan_ele'),
        electron1id = cms.int32(0), # 0: veto, 1: loose, 2: medium, 3: tight, 4: HEEP, 5: MVA medium nonTrig, 6: MVA tight nonTrig, 7: MVA medium Trig, 8: MVA tight Trig
        electron2id = cms.int32(0),
        electron1pt = cms.double(10),
        electron2pt = cms.double(10),
    ),
    muonSet = cms.PSet(
        muons = cms.InputTag('cleanedMuons'),#('slimmedMuons'),#
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        muonTrkFileName = cms.string('data/MuonTrkEfficienciesAndSF_MORIOND17.root'),
        muonIdFileName = cms.string('data/MuonIdEfficienciesAndSF_MORIOND17.root'),
        muonIsoFileName = cms.string('data/MuonIsoEfficienciesAndSF_MORIOND17.root'),
        muonTrkHighptFileName = cms.string('data/tkhighpt_2016full_absetapt.root'),
        muonTriggerFileName = cms.string('data/MuonTrigEfficienciesAndSF_MORIOND17.root'),
        doubleMuonTriggerFileName = cms.string('data/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root'),#FIXME -> obsolete
        muon1id = cms.int32(1), # 0: tracker high pt muon id, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(1),
        muon1iso = cms.int32(1), # 0: trk iso (<0.1), 1: loose (<0.25), 2: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(1),
        muon1pt = cms.double(10.),
        muon2pt = cms.double(10.),
        useTuneP = cms.bool(False),
        doRochester = cms.bool(False),
    ),
    tauSet = cms.PSet(
        taus = cms.InputTag('slimmedTaus'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        taupt = cms.double(18.),
        taueta = cms.double(2.3),
        tauIdByDecayMode = cms.int32(1),# 0: not set, 1: old, 2: new
        tauIdByDeltaBetaIso = cms.int32(1),# 0: not set, 1: loose, 2: medium, 3: tight
        tauIdByMVAIso = cms.int32(0),# 0: not set, 1: V loose, 2: loose, 3: medium, 4: tight, 5: V tight
        tauIdByMuonRejection = cms.int32(0),# 0: not set, 1: loose, 2: tight
        tauIdByElectronRejection = cms.int32(0),# 0: not set, 1: V loose, 2: loose, 3: medium, 4: tight
    ),
    photonSet = cms.PSet(
        photons = cms.InputTag('slimmedPhotons'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        phoLooseId = cms.string('cutBasedPhotonID-Fall17-94X-V1-loose'),
        phoMediumId = cms.string('cutBasedPhotonID-Fall17-94X-V1-medium'),
        phoTightId = cms.string('cutBasedPhotonID-Fall17-94X-V1-tight'),
        phoMVANonTrigMediumId = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
        phoEcalRecHitCollection = cms.InputTag("reducedEgamma:reducedEBRecHits"),
        phoLooseIdFileName = cms.string('data/phoLooseIDSF_MORIOND17.root'),
        phoMediumIdFileName = cms.string('data/phoMediumIDSF_MORIOND17.root'),
        phoTightIdFileName = cms.string('data/phoTightIDSF_MORIOND17.root'),
        phoMVANonTrigMediumIdFileName = cms.string('data/phoMVA90IDSF_MORIOND17.root'),
        photonid = cms.int32(1), # 1: loose, 2: medium, 3: tight, 4:MVA NonTrig medium
        photonpt = cms.double(15.),
    ),
    vertexSet = cms.PSet(
        primaryVertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        secondaryVertices =  cms.InputTag('slimmedSecondaryVertices'),
    ),
    pfCandidateSet = cms.PSet(
        pfCandidates = cms.InputTag('packedPFCandidates'),
        lostTracks = cms.InputTag('lostTracks'),
    ),
    minGenBpt = cms.double(0.),#gen b quarks in acceptance
    maxGenBeta = cms.double(999),#gen b quarks in acceptance
    #invmassVBF = cms.double(300.),#https://indico.desy.de/indico/event/20983/contribution/0/material/slides/0.pdf
    #new cut, motivated by calo-lifetimes trigger path
    invmassVBF = cms.double(250. if isCalo else 400.),
    #detaVBF = cms.double(2.5),#https://indico.desy.de/indico/event/20983/contribution/0/material/slides/0.pdf
    #new cut, motivated by calo-lifetimes trigger path
    detaVBF = cms.double(2.5 if isCalo else 3.),
    writeNJets = cms.int32(0),#(1),#compare if identical
    writeNFatJets = cms.int32(1),#(2),
    #writeNGenBquarks = cms.int32(4),#(4),
    #writeNGenLongLiveds = cms.int32(2),#(2),
    writeGenVBFquarks = cms.bool(True),
    writeGenHiggs = cms.bool(True),
    writeGenBquarks = cms.bool(True), #Acceptance cuts a few lines above!
    writeGenLLPs = cms.bool(True),
    writeNMatchedJets = cms.int32(0),#(4), #Warning: List/Reset JetType functions missing several attributes. Please check before using!
    writeNLeptons = cms.int32(0),#Framework already validated
    ##
    writeOnlyTriggerEvents = cms.bool(True),#slims down ntuples a lot
    writeOnlyL1FilterEvents = cms.bool(False),#slims down ntuples a lot
    writeOnlyisVBFEvents = cms.bool(True),#slims down ntuples a lot
    writeAllJets = cms.bool(False),#used for trigger studies
    writeFatJets = cms.bool(True),#not needed now
    ## PFCandidates:
    writeAK4JetPFCandidates = cms.bool(False), #Matched to AK4 only!
    writeAK8JetPFCandidates = cms.bool(False), #Matched to AK8 only!
    writeAllJetPFCandidates = cms.bool(False), #Matched to either AK4 or AK8
    writeAllPFCandidates = cms.bool(False), #All PFCandidates. Large collection: Please write only if needed!
    ##
    writeLostTracks = cms.bool(False),
    writeVertices = cms.bool(True),
    writeBtagInfos = cms.bool(True),
    calculateNsubjettiness = cms.bool(False),
    performPreFiringStudies = cms.bool(True if ('unprefirable' in process.source.fileNames[0]) else False),
    performVBF = cms.bool(isVBF),
    performggH = cms.bool(isggH),
    ##
    ##btagToken = cms.untracked.InputTag("pfTrackCountingHighEffBJetTagsFinal","","ntuple"),
    verbose = cms.bool(False),
    verboseTrigger  = cms.bool(False),
    svTagInfoProducer = cms.untracked.InputTag("inclusiveSecondaryVertexFinderTagInfos"),
    updatedPatJets = cms.untracked.InputTag("updatedPatJet"),
    signal = cms.bool(isSignal),
    iscalo = cms.bool(isCalo),
)




process.seq = cms.Sequence(
    process.counter *
    #process.ParticleListDrawer #*
    #process.test
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

outFile = open("tmpConfig_AODNTest.py","w")
outFile.write(process.dumpPython())
outFile.close()

