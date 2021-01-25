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
    "Pis2016", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "is2016 parser flag"
)
options.register(
    "Pis2017", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "is2017 parser flag"
)
options.register(
    "Pis2018", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "is2018 parser flag"
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
options.register(
    "PTwinHiggs", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "TwinHiggs parser flag"
)
options.register(
    "PHeavyHiggs", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "HeavyHiggs parser flag"
)
options.register(
    "PSUSY", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "SUSY parser flag"
)
options.parseArguments()

## Important: decide if keeping local options register or CRAB options register
#RunLocalCMS = cms.bool( options.runLocal )
RunLocal = cms.bool( options.runLocal )

if RunLocal:
   print "Taking configurations from cfg file; not designed for CRAB submission!"

process = cms.Process("ntuple")
task = cms.Task()

process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True),
)

#Enable multithreading!
#process.options.numberOfThreads=cms.untracked.uint32(8)
#process.options.numberOfStreams=cms.untracked.uint32(0)

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 500

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
          #RPV
          #'/store/mc/RunIISummer16MiniAODv3/DisplacedSUSY_StopToBL_M-900_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/044FBE56-ADC7-E911-8E0C-A4BF01158AD8.root',
          #split susy
          #'/store/mc/RunIIAutumn18DRPremix/GluinoGluinoToNeutralinoNeutralinoTo2T2B2S_M-2400_CTau-1000mm_TuneCP2_13TeV-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/20000/01AA08C8-76E0-8E4C-8818-DD9B24DFF988.root',
          #jet jet
          '/store/mc/RunIIAutumn18MiniAOD/XXTo4J_M1000_CTau1000mm_TuneCP2_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/50000/14A803F4-C9E4-3F41-B748-D19DEC529F31.root',
          #2HDM
          #'/store/mc/RunIISummer16MiniAODv3/SUSYGluGluToHToAA_AToMuMu_AToTauTau_mH-750_mA-7_TuneCUETP8M1_13TeV_madgraph_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/A6629877-BCEF-E811-8F66-0CC47AC52E44.root'
          #25?'/store/mc/RunIISummer16MiniAODv3/SUSYGluGluToHToAA_AToMuMu_AToTauTau_mH-750_mA-15_TuneCUETP8M1_13TeV_madgraph_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/602D800A-AF43-E911-B95A-0025904C641C.root',
          #?#'/store/mc/RunIIFall17MiniAODv2/NMSSM_HToAATo4Mu_mH_125_mA_3_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6A7763FF-E8CE-E811-A2AA-008CFAFBFB7C.root',
          #'/store/mc/RunIIFall17MiniAODv2/NMSSM_HToAATo4Mu_mH_150_mA_0p5_TuneCP5_13TeV-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/10C5A916-63B3-E811-9797-5065F381E151.root'
          #'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15_AODSIM/200318_124011/0000/output_1.root'
          #'file:/afs/desy.de/user/p/penaka/public/forLisa/miniAODv3_test.root'
          #'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH_HToSSTobbbb_MH-125_MS-20_ctauS-1000_Summer16_MINIAODSIM_calojets/GluGluH_HToSSTobbbb_MH-125_MS-20_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_MINIAODSIM_calojets/181203_140031/0000/miniaod_1.root'
#            'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_Summer16_MINIAODSIM_calojets_Tranche2/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_Tranche2_MINIAODSIM_calojets/181218_125055/0000/miniaod_1.root',
            #'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_Summer16_AODSIM_Tranche2/VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_Tranche2_AODSIM/181214_110243/0000/aodsim_1.root'
            #'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FE57DDB4-DDBA-E611-A344-0025905A6064.root',
            #'file:/pnfs/desy.de/cms/tier2/store/data/Run2016G/MET/AOD/07Aug17-v1/110000/3C4239F2-E9A0-E711-82F7-02163E014117.root' 
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
    is2016            = ('RunIISummer16' in process.source.fileNames[0])
    is2017            = ('RunIIFall17' in process.source.fileNames[0])
    is2018            = ('RunIIAutumn18' in process.source.fileNames[0]) or ('n3n2-n1-hbb-hbb' in process.source.fileNames[0])
    isPromptReco      = ('PromptReco' in process.source.fileNames[0])
    noLHEinfo         = True if ('WW_TuneCUETP8M1_13TeV-pythia8' or 'WZ_TuneCUETP8M1_13TeV-pythia8' or 'ZZ_TuneCUETP8M1_13TeV-pythia8' or 'WW_TuneCP5_13TeV-pythia8' or 'WZ_TuneCP5_13TeV-pythia8' or 'ZZ_TuneCP5_13TeV-pythia8') in process.source.fileNames[0] else False #check for PythiaLO samples
    isbbH             = True if ('bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo' in process.source.fileNames[0]) else False #bbH has a different label in LHEEventProduct
    isSignal          = True if ('HToSSTobbbb_MH-125' in process.source.fileNames[0]) else False
    isCalo            = True #HERE for calo analyses!!!
    isVBF             = False
    isggH             = False
    isTwinHiggs       = False
    isHeavyHiggs      = False
    isSUSY            = False
    is2HDM            = False
    isRPV             = False
    isSplit           = False
    isJetJet          = True

else:
    isData            = options.PisData
    isReHLT           = options.PisReHLT
    isReReco          = options.PisReReco
    isReMiniAod       = options.PisReMiniAod
    is2016            = options.Pis2016
    is2017            = options.Pis2017
    is2018            = options.Pis2018
    isPromptReco      = options.PisPromptReco
    noLHEinfo         = options.PnoLHEinfo
    isbbH             = options.PisbbH
    isSignal          = options.PisSignal
    isCalo            = options.Pcalo
    isVBF             = options.PVBF
    isggH             = options.PggH
    isTwinHiggs       = options.PTwinHiggs
    isHeavyHiggs      = options.PHeavyHiggs
    isSUSY            = options.PSUSY
    is2HDM            = False
    isRPV             = False
    isSplit           = False
    isJetJet          = False


theRunBCD2016 = ['Run2016B','Run2016C','Run2016D']
theRunEF2016  = ['Run2016E','Run2016F']
theRunG2016   = ['Run2016G']
theRunH2016   = ['Run2016H']

theRun2018ABC = ['Run2018A','Run2018B','Run2018C']
theRun2018D   = ['Run2018D']

print "\n"
print 'Data era: '
if is2016: print "2016"
if is2017: print "2017"
if is2018: print "2018"
print "\n"
print 'isData',isData
print 'isReHLT',isReHLT
print 'isReReco',isReReco
print 'isReMiniAod',isReMiniAod
print 'isPromptReco',isPromptReco
print 'isSignal', isSignal

if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSY) + int(is2HDM)>1):
   print "More than one theoretical model selected! Aborting...."
   exit()

if isTwinHiggs:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing TWIN HIGGS analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 9000006
    idHiggs     = 25
    idMotherB   = 9000006
    statusLLP   = 22
    statusHiggs = 62

if isHeavyHiggs:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing HEAVY HIGGS analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 6000113
    idHiggs     = 35
    idMotherB   = 6000113
    statusLLP   = 22
    statusHiggs = 62

if is2HDM:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing H->AA analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 36#A
    idHiggs     = 25
    idMotherB   = 36#A
    statusLLP   = 22
    statusHiggs = 62

if isSUSY:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing SUSY analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 1000023
    #Warning! There is also 1000025!!
    idHiggs     = 25
    idMotherB   = 25
    statusLLP   = 62
    statusHiggs = 22
    #isVBF = False
    #isggH = False
    #Jet pt seems higher. Do not recluster
    #isCalo = False

if isRPV:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing RPV stop->bl analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 1000006
    idHiggs     = 25
    idMotherB   = 1000006
    statusLLP   = 106
    statusHiggs = 22

if isSplit:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing split susy   analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 1000022
    idHiggs     = 1000021
    idMotherB   = 1000022
    statusLLP   = 22
    statusHiggs = 62

if isJetJet:
    print "\n"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Performing XX->4J analysis!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n"
    idLLP       = 36
    idHiggs     = 35
    idMotherB   = 36
    statusLLP   = 62
    statusHiggs = 62

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

if(isTwinHiggs and isCalo):
    pt_AK4 = 5
else:
    pt_AK4 = 15

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
        if is2016:
            GT = '80X_dataRun2_2016SeptRepro_v7'
        elif is2017:
            GT = '94X_dataRun2_v11'
        elif is2018:
            if theRun2018ABC: GT = '102X_dataRun2_v12'
            if theRun2018D:   GT = '102X_dataRun2_Prompt_v15'
    elif not(isData):
        if is2016:
            GT = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
        elif is2017:
            GT = '94X_mc2017_realistic_v17'
        elif is2018:
            GT = '102X_upgrade2018_realistic_v20'
else:
    GT = options.PGT

process.GlobalTag = GlobalTag(process.GlobalTag, GT)
print 'GlobalTag loaded: ', GT

#-----------------------#
#    VERTEX FILTER      #
#-----------------------#

import RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi
process.primaryVertexFilter = cms.EDFilter('GoodVertexFilter',
    vertexCollection = cms.InputTag('offlineSlimmedPrimaryVertices'),
    minimumNDOF = cms.uint32(4),
    maxAbsZ = cms.double(24),
    maxd0 = cms.double(2)
)
task.add(process.primaryVertexFilter)

#-----------------------#
#         JEC           #
#-----------------------#

# Jet corrector https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrOnTheFly
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')


JECstring = ''
if RunLocal:
    if isData:# and (isReReco or isReMiniAod):
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
#       COUNTER         #
#-----------------------#
process.counter = cms.EDAnalyzer('CounterAnalyzer',
    genProduct = cms.InputTag('generator'),
    #lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
    pythiaLOSample = cms.bool(True if noLHEinfo else False),
)


#-----------------------#
#     PAT OBJECTS       #
#-----------------------#

#Transient track builder needed for vertices
process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")


#-----------------------#
#        FILTERS        #
#-----------------------#

# JSON filter
if isData:
    import FWCore.PythonUtilities.LumiList as LumiList
    jsonName = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON"#"Cert_294927-305364_13TeV_PromptReco_Collisions17_JSON"#"Cert_294927-301567_13TeV_PromptReco_Collisions17_JSON" #golden json
    process.source.lumisToProcess = LumiList.LumiList(filename = 'data_gen/JSON/'+jsonName+'.txt').getVLuminosityBlockRange()
    print "JSON file loaded: ", jsonName

if RunLocal:
    # Trigger filter
    triggerTag = 'HLT2' if isReHLT else 'HLT'

    # MET filters string
    filterString = "RECO"
    if isData:
        filterString = "RECO"
    else:
        filterString = "PAT" if 'MINIAOD' in process.source.fileNames[0] else "RECO"
else:
    triggerTag = options.PtriggerTag
    filterString = options.PfilterString


## MET filters, not available on AOD? TODO
process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.BadPFMuonFilter.muons = cms.InputTag('slimmedMuons' if 'MINIAOD' in process.source.fileNames[0] else 'muons')
process.BadPFMuonFilter.PFCandidates = cms.InputTag('packedPFCandidates' if 'MINIAOD' in process.source.fileNames[0] else 'particleFlow')

process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
process.BadChargedCandidateFilter.muons = cms.InputTag('slimmedMuons' if 'MINIAOD' in process.source.fileNames[0] else 'muons')
process.BadChargedCandidateFilter.PFCandidates = cms.InputTag('packedPFCandidates' if 'MINIAOD' in process.source.fileNames[0] else 'particleFlow')

task.add(process.BadPFMuonFilter)
task.add(process.BadChargedCandidateFilter)

#-----------------------#
#       ANALYZER        #
#-----------------------#

process.ntuple = cms.EDAnalyzer('TriggerGenNtuplizer',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        lheProduct = cms.InputTag('externalLHEProducer'),
        genParticles = cms.InputTag('prunedGenParticles' if 'MINIAOD' in process.source.fileNames[0] else 'genParticles'),
        pdgId = cms.vint32(5,9000006,23,24,25,1000006,1000021,1000022,36,35),#(1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 23, 24, 25, 36, 39, 1000022, 9100000, 9000001, 9000002, 9100012, 9100022, 9900032, 1023),
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
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
#'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
#'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',

##single lepton
#'HLT_IsoMu24_v','HLT_Ele27_WPTight_Gsf_v',
##others:
#'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v','HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v','HLT_PFHT300_PFMET110_v','HLT_RsqMR270_Rsq0p09_MR200_v','HLT_RsqMR270_Rsq0p09_MR200_4jet_v','HLT_HT650_v',
### b-like
#'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v', 'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v', 'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', 'HLT_QuadJet45_TripleBTagCSV_p087_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v','HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v', 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v',
#'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v'
### displaced tracks
#'HLT_VBF_DisplacedJet40_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v', 'HLT_HT350_DisplacedDijet40_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v', 'HLT_HT650_DisplacedDijet80_Inclusive_v', 'HLT_HT750_DisplacedDijet80_Inclusive_v',
### calo lifetimes
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v',
###
#'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v', 'HLT_MET200_v', 'HLT_MET250_v', 'HLT_MET75_IsoTrk50_v', 'HLT_MET90_IsoTrk50_v', 'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v', 'HLT_PFMET110_PFMHT110_IDTight_v', 'HLT_PFMET120_PFMHT120_IDTight_v', 'HLT_PFMET170_HBHECleaned_v', 'HLT_PFMET300_v', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
###production for MET
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
### All studied triggers:
#
###Control paths for VBF, prescaled
#'HLT_L1_TripleJet_VBF_v', 'HLT_QuadPFJet_VBF_v','HLT_DiPFJetAve40_v','HLT_DiPFJetAve60_v','HLT_DiPFJetAve80_v','HLT_PFJet40_v','HLT_PFJet60_v','HLT_PFJet80_v',
###TEST
##'HLT_AK8PFJet450_v',###########TEST
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v'#,'HLT_AK4PFJet30_v7'
### Displaced Muons
#'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v', 'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v', 'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v',
#'HLT_L2Mu10_NoVertex_NoBPTX3BX_v','HLT_L2Mu10_NoVertex_NoBPTX_v','HLT_L2Mu40_NoVertex_3Sta_NoBPTX3BX_v','HLT_L2Mu45_NoVertex_3Sta_NoBPTX3BX_v',
#'HLT_DoubleMu3_PFMET50_v', 'HLT_DoubleMu0_v', 'HLT_DoubleMu18NoFiltersNoVtx_v','HLT_Mu17_Mu8_v', 'HLT_Mu17_v', 'HLT_Mu8_v','HLT_TripleMu_12_10_5_v', 'HLT_IsoMu20_v', 'HLT_IsoMu24_v','HLT_IsoTkMu24_v', 'HLT_Mu20_v', 'HLT_Mu27_v','HLT_TkMu17_v', 'HLT_TkMu20_v', 'HLT_TkMu27_v5',
]
        ),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter','Flag_badMuons','Flag_duplicateMuons','Flag_noBadMuons') if isReMiniAod else cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter'),
        prescales = cms.InputTag('patTrigger','','PAT'),
        l1Minprescales = cms.InputTag('patTrigger','l1min','PAT'),
        l1Maxprescales = cms.InputTag('patTrigger','l1max','PAT'),
        objects = cms.InputTag('selectedPatTrigger','','PAT'),
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
    #Define gen decay:
    idLLP = cms.int32(idLLP),
    idHiggs = cms.int32(idHiggs),
    idMotherB = cms.int32(idMotherB),
    statusLLP = cms.int32(statusLLP),
    statusHiggs = cms.int32(statusHiggs),

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
    l1Seeds = cms.vstring("L1_TripleJet_84_68_48_VBF","L1_TripleJet_88_72_56_VBF","L1_TripleJet_92_76_64_VBF","L1_HTT280","L1_HTT300","L1_HTT320","L1_SingleJet170","L1_SingleJet180","L1_SingleJet200","L1_DoubleJetC100","L1_DoubleJetC112","L1_DoubleJetC120","L1_QuadJetC50", "L1_QuadJetC60", "L1_ETM100", "L1_ETM105", "L1_ETM110", "L1_ETM115", "L1_ETM120", "L1_DoubleMu_13_6", "L1_DoubleMu_12_5", "L1_DoubleMu_11_4", "L1_DoubleMu0er1p4_dEta_Max1p8_OS","L1_SingleMuOpen_NotBptxOR_3BX","L1_SingleMuOpen_NotBptxOR","L1_SingleMuOpen_NotBptxOR_3BX","L1_SingleMuOpen_NotBptxOR_3BX", "L1_Mu3_JetC16_dEta_Max0p4_dPhi_Max0p4",  "L1_Mu3_JetC60_dEta_Max0p4_dPhi_Max0p4", "L1_Mu3_JetC120_dEta_Max0p4_dPhi_Max0p4", "L1_TripleMu_5_0_0", "L1_TripleMu0", "L1_TripleMu_5_5_3", "L1_Mu8_HTT150", "L1_QuadMu0", "L1_SingleMu7", "L1_SingleMu14", "L1_SingleMu16", "L1_SingleMu18", "L1_DoubleMu0_ETM55", "L1_DoubleMu0_ETM65", "L1_Mu3_JetC16"),
    ReadPrescalesFromFile = cms.bool(True),
)

process.demo = cms.EDAnalyzer('Demo'
)

process.seq = cms.Sequence(
    process.counter *
    process.ntuple
)

process.p = cms.Path(process.seq)
process.p.associate(task)

outFile = open("tmpConfig_GenNtuplizer.py","w")
outFile.write(process.dumpPython())
outFile.close()
