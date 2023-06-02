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
    "PisCentralProd", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isCentralProd parser flag"
)
options.register(
    "PJERstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "JERstring parser flag"
)
options.register(
    "PMuonSFIDstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MuonSFIDstring parser flag"
)
options.register(
    "PMuonSFISOstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MuonSFISOstring parser flag"
)
options.register(
    "PMuonSFTriggerstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MuonSFTriggerstring parser flag"
)
options.register(
    "PeleVetoIDstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PeleVetoIDstring parser flag"
)
options.register(
    "PeleLooseIdstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PeleLooseIdstring parser flag"
)
options.register(
    "PeleMediumIdstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PeleMediumIdstring parser flag"
)
options.register(
    "PeleTightIdstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PeleTightIdstring parser flag"
)
options.register(
    "PeleMVA90noISOstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PeleMVA90noISOstring parser flag"
)
options.register(
    "PeleMVA80noISOstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PeleMVA80noISOstring parser flag"
)
options.register(
    "PphoLooseIdFilestring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PphoLooseIdFilestring parser flag"
)
options.register(
    "PphoMediumIdFilestring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PphoMediumIdFilestring parser flag"
)
options.register(
    "PphoTightIdFilestring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PphoTightIdFilestring parser flag"
)
options.register(
    "PphoMVANonTrigMediumIdFilestring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "PphoMVANonTrigMediumIdFilestring parser flag"
)
options.register(
    "PbtagSFstring", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "btagSFstring parser flag"
)
options.register(
    "PtriggerString", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "triggerString parser flag"
)
options.register(
    "Pcalo", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "calo parser flag"
)
options.register(
    "Ptracking", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "tracking parser flag"
)
options.register(
    "Pshort", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "short parser flag"
)
options.register(
    "Pcontrol", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "control parser flag"
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
process = cms.Process("ntuple")
task = cms.Task()

## Important: decide if keeping local options register or CRAB options register
#RunLocalCMS = cms.bool( options.runLocal )
RunLocal = cms.bool( options.runLocal )

if RunLocal:
   print "Take things as they are"

process = cms.Process("ALPHA")

process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True),
)

##Enable multithreading!
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 500

## Input files
if len(options.inputFiles) == 0:#to be checked
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
           #2016 data
           '/store/data/Run2016G/SingleMuon/MINIAOD/17Jul2018-v1/00000/00252084-588F-E811-801F-008CFAFC5984.root',
           #2016 background
#           '/store/mc/RunIISummer16MiniAODv3/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/001B3D66-B4C0-E811-B670-44A84225C4EB.root'
        ),
        #
        #skipEvents = cms.untracked.uint32(1314),
        #
        ###firstEvent = cms.untracked.uint32(176769),
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
    is2016            = True if('RunIISummer16' in process.source.fileNames[0] or 'Run2016' in process.source.fileNames[0]) else False
    is2017            = True if('RunIIFall17' in process.source.fileNames[0] or 'Run2017' in process.source.fileNames[0]) else False
    is2018            = True if('RunIIAutumn18' in process.source.fileNames[0] or 'Run2018' in process.source.fileNames[0]) else False
    isPromptReco      = ('PromptReco' in process.source.fileNames[0])
    noLHEinfo         = True if ('WW_TuneCUETP8M1_13TeV-pythia8' or 'WZ_TuneCUETP8M1_13TeV-pythia8' or 'ZZ_TuneCUETP8M1_13TeV-pythia8' or 'WW_TuneCP5_13TeV-pythia8' or 'WZ_TuneCP5_13TeV-pythia8' or 'ZZ_TuneCP5_13TeV-pythia8') in process.source.fileNames[0] else False #check for PythiaLO samples
    isbbH             = True if ('bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo' in process.source.fileNames[0]) else False #bbH has a different label in LHEEventProduct
    isSignal          = True if ('HToSSTobbbb_MH-125' in process.source.fileNames[0] or 'HToSSTo4b_MH-125' in process.source.fileNames[0]) else False
    isCentralProd     = True if ('HToSSTo4b_MH-125' in process.source.fileNames[0]) else False
    isCalo            = False #HERE for calo analyses!!!
    isTracking        = False
    isShort           = True #HERE for short lifetime analyses!!!
    isControl         = False #HERE for short lifetime control region!!!
    isVBF             = False
    isggH             = False
    isTwinHiggs       = True
    isHeavyHiggs      = False
    isSUSY            = False

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
    isCentralProd     = options.PisCentralProd
    isCalo            = options.Pcalo
    isTracking        = options.Ptracking
    isShort           = options.Pshort
    isControl         = options.Pcontrol
    isVBF             = options.PVBF
    isggH             = options.PggH
    isTwinHiggs       = options.PTwinHiggs
    isHeavyHiggs      = options.PHeavyHiggs
    isSUSY            = options.PSUSY

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
#     GLOBAL TAG        #
#-----------------------#

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
GT = ''

if RunLocal:
#from https://indico.cern.ch/event/920726/contributions/3868370/attachments/2055396/3446379/20-06-11_News_PPD.pdf
   if isData:
      if is2016:
         GT = '102X_dataRun2_v13'
      elif is2017:
         GT = '102X_dataRun2_v13'
      elif is2018:
         if theRun2018ABC: GT = '102X_dataRun2_v13'
         if theRun2018D:   GT = '102X_dataRun2_Prompt_v16'
   elif not(isData):
      if is2016:
         GT = '102X_mcRun2_asymptotic_v8'
      elif is2017:
         GT = '102X_mc2017_realistic_v8'
      elif is2018:
         GT = '102X_upgrade2018_realistic_v21'
else:
    GT = options.PGT

process.GlobalTag = GlobalTag(process.GlobalTag, GT)
print 'GlobalTag loaded: ', GT


#-----------------------#
#  E-MU-GAMMA MODULES   #
#-----------------------#

from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
era_string = ''
if is2016:
   era_string = '2016-Legacy'
elif is2017:
   era_string = '2017-Nov17ReReco'
elif is2018:
   era_string = '2018-Prompt'
setupEgammaPostRecoSeq(process,runEnergyCorrections=False,era=era_string)#era='2018-Prompt'

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
    else:#dummy!
       print "WARNING! Dummy JEC for other run eras!!!!!!!!!!!"
       JECstring = "Summer16_23Sep2016HV3_DATA"

else:
    JECstring = options.PJECstring
print "JEC ->",JECstring


JERstring = ''
MuonSFTriggerstring = ''
MuonSFISOstring = ''
MuonSFIDstring = ''
eleVetoIDstring = ''
eleLooseIdstring = ''
eleMediumIdstring = ''
eleTightIdstring = ''
eleMVA90noISOstring = ''
eleMVA80noISOstring = ''
phoLooseIdFilestring = ''
phoMediumIdFilestring = ''
phoTightIdFilestring = ''
phoMVANonTrigMediumIdFilestring = ''
btagSFstring = ''
if RunLocal:
   if is2016:
      JERstring = 'Summer16_25nsV1b_MC'
      #WARNING! Muon SF should not be here applied for 2016! It needed to be a lumi weighted SF and hence only calculated after full run and brilcalc procedure! Needed to be done after ntuplizer process!
      MuonSFTriggerstring = 'MuonTrigger_average_RunBtoH_SF_Run2_2016'
      MuonSFISOstring = 'MuonISO_average_RunBtoH_SF_Run2_2016'
      MuonSFIDstring = 'MuonID_average_RunBtoH_SF_Run2_2016'
      eleVetoIDstring = '2016_ElectronWPVeto_Fall17V2'
      eleLooseIdstring = '2016LegacyReReco_ElectronLoose_Fall17V2'
      eleMediumIdstring = '2016LegacyReReco_ElectronMedium_Fall17V2'
      eleTightIdstring = '2016LegacyReReco_ElectronTight_Fall17V2'
      eleMVA90noISOstring = '2016LegacyReReco_ElectronMVA90noiso_Fall17V2'
      eleMVA80noISOstring = '2016LegacyReReco_ElectronMVA80noiso_Fall17V2'
      phoLooseIdFilestring = 'Fall17V2_2016_Loose_photons'
      phoMediumIdFilestring = 'egammaPlots_MWP_PhoSFs_2016_LegacyReReco_New'
      phoTightIdFilestring = 'Fall17V2_2016_Tight_photons'
      phoMVANonTrigMediumIdFilestring = 'Fall17V2_2016_MVAwp90_photons'
      btagSFstring = 'DeepJet_2016LegacySF_V1'
   elif is2017:
      JERstring = 'Fall17_V3b_MC'
      MuonSFTriggerstring = 'MuonTrigger_EfficienciesAndSF_RunBtoF_Nov17Nov2017'
      MuonSFISOstring = 'MuonISO_2017_RunBCDEF_SF_ISO_Nov17'
      MuonSFIDstring = 'MuonID_2017_RunBCDEF_SF_ID_Nov17'
      eleVetoIDstring = '2017_ElectronWPVeto_Fall17V2'
      eleLooseIdstring = '2017_ElectronLoose_Fall17V2'
      eleMediumIdstring = '2017_ElectronMedium_Fall17V2'
      eleTightIdstring = '2017_ElectronTight_Fall17V2'
      eleMVA90noISOstring = '2017_ElectronMVA90noiso_Fall17V2'
      eleMVA80noISOstring = '2017_ElectronMVA80noiso_Fall17V2'
      phoLooseIdFilestring = '2017_PhotonsLoose'
      phoMediumIdFilestring = '2017_PhotonsMedium'
      phoTightIdFilestring = '2017_PhotonsTight'
      phoMVANonTrigMediumIdFilestring = '2017_PhotonsMVAwp90'
      btagSFstring = 'DeepFlavour_94XSF_V4_B_F_Run2017'
   elif is2018:
      JERstring = 'Autumn18_V7b_MC'
      MuonSFTriggerstring = 'MuonTrigger_EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_AfterMuonHLTUpdate'
      print "WARNING! There is another SF root file for single muon triggers for Run A: run < 316361 it is called: MuonTrigger_EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_BeforeMuonHLTUpdate. TO BE IMPLEMENTED SOMEHOW!"
      if isControl: exit()
      MuonSFISOstring = 'MuonISO_EfficienciesStudies_2018_rootfiles_RunABCD_SF_ISO'
      MuonSFIDstring = 'MuonID_EfficienciesStudies_2018_rootfiles_RunABCD_SF_ID'
      eleVetoIDstring = '2018_ElectronWPVeto_Fall17V2'
      eleLooseIdstring = '2018_ElectronLoose_Fall17V2'
      eleMediumIdstring = '2018_ElectronMedium_Fall17V2'
      eleTightIdstring = '2018_ElectronTight_Fall17V2'
      eleMVA90noISOstring = '2018_ElectronMVA90noiso_Fall17V2'
      eleMVA80noISOstring = '2018_ElectronMVA80noiso_Fall17V2'
      phoLooseIdFilestring = '2018_PhotonsLoose'
      phoMediumIdFilestring = '2018_PhotonsMedium'
      phoTightIdFilestring = '2018_PhotonsTight'
      phoMVANonTrigMediumIdFilestring = '2018_PhotonsMVAwp90'
      btagSFstring = 'DeepJet_102XSF_V2_Run2018'
else:
   JERstring = options.PJERstring
   MuonSFIDstring = options.PMuonSFIDstring
   MuonSFISOstring = options.PMuonSFISOstring
   MuonSFTriggerstring = options.PMuonSFTriggerstring
   eleVetoIDstring = options.PeleVetoIDstring
   eleLooseIdstring = options.PeleLooseIdstring
   eleMediumIdstring = options.PeleMediumIdstring
   eleTightIdstring = options.PeleTightIdstring
   eleMVA90noISOstring = options.PeleMVA90noISOstring
   eleMVA80noISOstring = options.PeleMVA80noISOstring
   phoLooseIdFilestring = options.PphoLooseIdFilestring
   phoMediumIdFilestring = options.PphoMediumIdFilestring
   phoTightIdFilestring = options.PphoTightIdFilestring
   phoMVANonTrigMediumIdFilestring = options.PphoMVANonTrigMediumIdFilestring
   btagSFstring = options.PbtagSFstring
print "JER ->", JERstring

#-----------------------#
#        FILTERS        #
#-----------------------#

# JSON filter
if isData:
    import FWCore.PythonUtilities.LumiList as LumiList
    if is2016:
        jsonName = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON"#"Cert_294927-305364_13TeV_PromptReco_Collisions17_JSON"#"Cert_294927-301567_13TeV_PromptReco_Collisions17_JSON" #golden json
    elif is2017:
        jsonName = "Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON"
    elif is2018:
        jsonName = "Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON"
    process.source.lumisToProcess = LumiList.LumiList(filename = 'data/JSON/'+jsonName+'.txt').getVLuminosityBlockRange()
    print "JSON file loaded: ", jsonName

if RunLocal:
    # Trigger filter
    triggerTag = 'HLT2' if isReHLT else 'HLT'

    # MET filters string
    if isData:
        filterString = "RECO"
        triggerString = "DQM"
    else:
        filterString = "PAT"
        triggerString = "PAT"
else:
    triggerTag = options.PtriggerTag
    filterString = options.PfilterString
    triggerString = options.PtriggerString


# MET filters
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
#    lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
    genProduct = cms.InputTag('generator'),
    pythiaLOSample = cms.bool(True if noLHEinfo else False),
)


#-----------------------#
#       B-Tag           #
#-----------------------#

from PhysicsTools.PatAlgos.tools.jetTools import *

#Seth
jetSource = "slimmedJets"
jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
pfCandidates = 'packedPFCandidates'
pvSource = 'offlineSlimmedPrimaryVertices'
svSource = 'slimmedSecondaryVertices'
muSource = 'slimmedMuons'
elSource = 'slimmedElectrons'

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
postfix = 'Final'#TODO

#-----------------------#
#       Vertices        # 
#-----------------------# 
'''
# taken from: https://github.com/cms-sw/cmssw/blob/02d4198c0b6615287fd88e9a8ff650aea994412e/PhysicsTools/PatAlgos/test/btag-from-packedPat.py
process.unpackTV = cms.EDProducer('PATTrackAndVertexUnpacker',
 slimmedVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
 slimmedSecondaryVertices = cms.InputTag("slimmedSecondaryVertices"),
 additionalTracks= cms.InputTag("lostTracks"),
 packedCandidates = cms.InputTag("packedPFCandidates")
)

process.jetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("unpackTV"),
    coneSize = cms.double(0.4),
    useAssigned = cms.bool(True),
    pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    jets = cms.InputTag("slimmedJets")
)
'''

# # taken from here: https://github.com/cms-sw/cmssw/blob/02d4198c0b6615287fd88e9a8ff650aea994412e/RecoBTag/ImpactParameter/python/impactParameterTagInfos_cfi.py
process.load("RecoBTag.ImpactParameter.pfImpactParameterTagInfos_cfi")
process.pfImpactParameterTagInfos.primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pfImpactParameterTagInfos.maximumChiSquared = cms.double(99999.9)
process.pfImpactParameterTagInfos.maximumLongitudinalImpactParameter = cms.double(99999.9)
process.pfImpactParameterTagInfos.maximumTransverseImpactParameter = cms.double(99999.9)
process.pfImpactParameterTagInfos.minimumNumberOfHits = cms.int32(0)
process.pfImpactParameterTagInfos.minimumNumberOfPixelHits = cms.int32(1)
process.pfImpactParameterTagInfos.minimumTransverseMomentum = cms.double(1.0)
process.pfImpactParameterTagInfos.computeGhostTrack = cms.bool(True)

process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

process.load("RecoBTag.SecondaryVertex.pfSecondaryVertexTagInfos_cfi")
process.load('RecoBTag/SecondaryVertex/pfInclusiveSecondaryVertexFinderTagInfos_cfi')
process.load("RecoBTag.SecondaryVertex.pfSecondaryVertexNegativeTagInfos_cfi")
process.load('RecoBTag/SecondaryVertex/pfInclusiveSecondaryVertexFinderNegativeTagInfos_cfi')
process.load('RecoBTag/CTagging/pfInclusiveSecondaryVertexFinderCvsLTagInfos_cfi')
process.load('RecoBTag/CTagging/pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos_cfi')

for n in ['pfSecondaryVertexTagInfos', 'pfInclusiveSecondaryVertexFinderTagInfos', 'pfSecondaryVertexNegativeTagInfos', 'pfInclusiveSecondaryVertexFinderNegativeTagInfos', 'pfInclusiveSe\
condaryVertexFinderCvsLTagInfos', 'pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos']:
    setattr( getattr(process,n), 'useExternalSV', cms.bool(False) )
    setattr( getattr(process,n), 'extSVCollection', cms.InputTag("") )
    setattr( getattr(process,n), 'useSVClustering', cms.bool(True) )
    setattr( getattr(process,n), 'jetAlgorithm', cms.string("AntiKt") )
    setattr( getattr(process,n), 'rParam', cms.double(0.4) )
    setattr( getattr(process,n), 'trackSelection', cms.PSet(
            max_pT = cms.double(99999.9),
            max_pT_dRcut = cms.double(99999.9),
            max_pT_trackPTcut = cms.double(99999.9),
            min_pT = cms.double(-99999.9),
            min_pT_dRcut = cms.double(-99999.9),
            pixelHitsMin = cms.uint32(0),
            totalHitsMin = cms.uint32(0)
            ))
    setattr( getattr(process,n), 'vertexCuts', cms.PSet(
            distVal2dMax = cms.double(99999.9),
            distSig2dMin = cms.double(-99999.9),
            distSig2dMax = cms.double(99999.9),
            distVal2dMin = cms.double(-99999.9),
            minimumTrackWeight = cms.double(-99999.9),
            massMax = cms.double(99999.9),
            multiplicityMin = cms.uint32(2),#Lisa???!
))


# process.load("RecoBTag.SecondaryVertex.pfSecondaryVertexTagInfos_cfi")

# process.load('RecoBTag/SecondaryVertex/pfInclusiveSecondaryVertexFinderTagInfos_cfi') 
# process.pfInclusiveSecondaryVertexFinderTagInfos.extSVCollection = cms.InputTag("")
# process.pfInclusiveSecondaryVertexFinderTagInfos.useExternalSV = cms.bool(False)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.distVal2dMax = cms.double(99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.distSig2dMin = cms.double(-99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.distSig2dMax = cms.double(99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.distVal2dMin = cms.double(-99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.useExternalSV = cms.bool(False)
# process.pfInclusiveSecondaryVertexFinderTagInfos.useSVClustering = cms.bool(True)
# process.pfInclusiveSecondaryVertexFinderTagInfos.jetAlgorithm = cms.string("AntiKt")
# process.pfInclusiveSecondaryVertexFinderTagInfos.rParam = cms.double(0.4)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.minimumTrackWeight = cms.double(-99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.massMax = cms.double(99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.vertexCuts.multiplicityMin = cms.uint32(0)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.max_pT = cms.double(99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.max_pT_dRcut = cms.double(99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.max_pT_trackPTcut = cms.double(99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.min_pT = cms.double(-99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.min_pT_dRcut = cms.double(-99999.9)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.pixelHitsMin = cms.uint32(0)
# process.pfInclusiveSecondaryVertexFinderTagInfos.trackSelection.totalHitsMin = cms.uint32(0)

# process.load("RecoBTag.SecondaryVertex.pfSecondaryVertexNegativeTagInfos_cfi")
# process.load('RecoBTag/SecondaryVertex/pfInclusiveSecondaryVertexFinderNegativeTagInfos_cfi')
process.load('RecoBTag/SoftLepton/softPFMuonTagInfos_cfi')
process.load('RecoBTag/SoftLepton/softPFElectronTagInfos_cfi')


updateJetCollection(
    process,
    jetSource = cms.InputTag(jetSource),
    jetCorrections = jetCorrectionsAK4,
    pfCandidates = cms.InputTag(pfCandidates),
    pvSource = cms.InputTag(pvSource),
    svSource = cms.InputTag(svSource),
    muSource = cms.InputTag(muSource),
    elSource = cms.InputTag(elSource),
    btagInfos = bTagInfos,
    btagDiscriminators = list(bTagDiscriminators),
    explicitJTA = useExplicitJTA,
    postfix = postfix#,
    )

for m in ['updatedPatJets'+postfix, 'updatedPatJetsTransientCorrected'+postfix]:
    setattr( getattr(process,m), 'addTagInfos', cms.bool(True) )

jets_to_be_used = 'updatedPatJetsTransientCorrected'+postfix

task.add(process.pfImpactParameterTagInfosFinal)
task.add(process.pfInclusiveSecondaryVertexFinderTagInfosFinal)
task.add(process.pfDeepCSVTagInfosFinal)
task.add(process.updatedPatJetsFinal)
task.add(process.updatedPatJetsTransientCorrectedFinal)

#-----------------------#
#         JEC           # 
#-----------------------# 
#1 Feb
#process.ak4PFchsCorrectedJets   = cms.EDProducer('CorrectedPFJetProducer',
#    src         = cms.InputTag('updatedPatJetsTransientCorrected'+postfix),
#    correctors  = cms.VInputTag('ak4PFCHSL1FastL2L3Corrector')
#    )



#-----------------------#
# Muon trigger matching #
#-----------------------#
#from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning #needed?#
#from PhysicsTools.PatAlgos.patTemplate_cfg import * nope, messes up with our mag field and GT
#process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
#process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

#process.muonTriggerMatchHLTMuons = cms.EDProducer(
#   "PATTriggerMatcherDRLessByR"
#   , src     = cms.InputTag( 'cleanedMuons' )
#   , matched = cms.InputTag( 'patTrigger' )
#   , matchedCuts = cms.string( 'type( "TriggerMuon" ) && path( "HLT_IsoMu24_v*" )' )
#   , maxDPtRel   = cms.double( 0.5 ) # no effect here
#   , maxDeltaR   = cms.double( 0.5 )
#   , maxDeltaEta = cms.double( 0.2 ) # no effect here
#   , resolveAmbiguities    = cms.bool( True )
#   , resolveByMatchQuality = cms.bool( True )
#)

#from PhysicsTools.PatAlgos.tools.trigTools import *
#process.out = 
#switchOnTriggerStandAlone( process, outputModule = '', hltProcess = 'PAT' )
#switchOnTriggerMatchingStandAlone( process, triggerMatchers = [ 'muonTriggerMatchHLTMuons' ] , outputModule = '')




#-----------------------#
#       ANALYZER        #
#-----------------------#

#PU files
if is2016:
    data_era = "2016"
    scenario = "2016_25ns_UltraLegacy_PoissonOOTPU"
elif is2017:
    data_era = "2017"
    scenario = "2017_25ns_UltraLegacy_PoissonOOTPU"
elif is2018:
    data_era = "2018"
    scenario = "2018_25ns_UltraLegacy_PoissonOOTPU"

process.trigger = cms.EDAnalyzer('TriggerStudies',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        lheProduct = cms.InputTag('externalLHEProducer'),
        genParticles = cms.InputTag('prunedGenParticles'),
        pdgId = cms.vint32(5,9000006,23,24),#(1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 23, 24, 25, 36, 39, 1000022, 9100000, 9000001, 9000002, 9100012, 9100022, 9900032, 1023),
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
        dataFileName     = cms.string('data/PU_69200_%s.root' % (data_era)),#updated
        dataFileNameUp   = cms.string('data/PU_72380_%s.root' % (data_era)),#updated
        dataFileNameDown = cms.string('data/PU_66020_%s.root' % (data_era)),#updated
        mcFileName = cms.string('data/PU_MC_%s.root' % (scenario)),#updated
        dataName = cms.string('pileup'),
        mcName = cms.string(scenario),#updated
    ),
    triggerSet = cms.PSet(
        trigger = cms.InputTag('TriggerResults', '', triggerTag),
        paths = cms.vstring(
*[
#############################
'HLT_IsoMu24_v', 'HLT_IsoTkMu24_v','HLT_Mu50_v', 'HLT_TkMu50_v',
#prescaled:
'HLT_Mu20_v','HLT_Mu24_eta2p1_v','HLT_Mu27_v','HLT_TkMu17_v','HLT_TkMu20_v','HLT_TkMu24_eta2p1_v','HLT_TkMu27_v',
###Control paths for VBF, prescaled
'HLT_L1_TripleJet_VBF_v', 'HLT_QuadPFJet_VBF_v','HLT_DiPFJetAve40_v','HLT_DiPFJetAve60_v','HLT_DiPFJetAve80_v','HLT_PFJet40_v','HLT_PFJet60_v','HLT_PFJet80_v',

###Control paths with HT
#'HLT_HT200_v', 'HLT_HT275_v','HLT_HT325_v', 'HLT_HT425_v', 
###Signal paths for VBF Higgs
'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', 'HLT_QuadJet45_TripleBTagCSV_p087_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v',
'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v',
# former meant as broken triggers:
'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v','HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v',
#
###############################
#MET
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
#
####Others
##'HLT_HT350_DisplacedDijet40_DisplacedTrack_v',  'HLT_HT350_DisplacedDijet80_DisplacedTrack_v',  'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',  'HLT_HT650_DisplacedDijet80_Inclusive_v',  'HLT_HT750_DisplacedDijet80_Inclusive_v',  
##'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v',  'HLT_VBF_DisplacedJet40_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v',   'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v',  
]
        ),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter','Flag_badMuons','Flag_duplicateMuons','Flag_noBadMuons') if isReMiniAod else cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter'),
        prescales = cms.InputTag('patTrigger','',triggerString),
        l1Minprescales = cms.InputTag('patTrigger','l1min',triggerString),
        l1Maxprescales = cms.InputTag('patTrigger','l1max',triggerString),
#        objects = cms.InputTag('selectedPatTrigger' if is2016 and isData else 'slimmedPatTrigger','',triggerString),
        objects = cms.InputTag('slimmedPatTrigger','',triggerString),
        badPFMuonFilter = cms.InputTag("BadPFMuonFilter"),
        badChCandFilter = cms.InputTag("BadChargedCandidateFilter"),
        l1Gt = cms.InputTag("gtStage2Digis"),
        l1filters = cms.vstring(
           #'hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300','hltL1sDoubleJetC112','hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF','hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet','hltL1sSingleMu22','hltL1sV0SingleMu22IorSingleMu25','hltL1sZeroBias','hltL1sSingleJet60','hltL1sSingleJet35','hltTripleJet50','hltDoubleJet65','hltSingleJet80','hltVBFFilterDisplacedJets'),
           #Filters for HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6
           'hltL1sDoubleJetC112','hltPreDoubleJetsC112DoubleBTagCSVp014DoublePFJetsC112MaxDeta1p6','HLTAK4CaloJetsSequence','hltDoubleJetsC112','HLTFastPrimaryVertexSequence','hltSelectorJets80L1FastJet','hltSelectorCentralJets80L1FastJet','hltSelector6CentralJetsL1FastJet','HLTBtagCSVSequenceL3','hltBTagCaloCSVp014DoubleWithMatching','HLTAK4PFJetsSequence','hltDoublePFJetsC112','hltDoublePFJetsC112MaxDeta1p6' ,
           #Filters for HLT_ DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172
           #'hltL1sDoubleJetC112', 'HLTAK4CaloJetsSequence','hltDoubleJetsC112','HLTFastPrimaryVertexSequence','hltSelectorJets80L1FastJet','hltSelectorCentralJets80L1FastJet','hltSelector6CentralJetsL1FastJet','HLTBtagCSVSequenceL3','HLTAK4PFJetsSequence',
           'hltPreDoubleJetsC112DoubleBTagCSVp026DoublePFJetsC172','hltBTagCaloCSVp026DoubleWithMatching','hltDoublePFJetsC172',
           #Filters for HLT_ QuadJet45_TripleBTagCSV_p087
           # 'HLTAK4CaloJetsSequence','HLTFastPrimaryVertexSequence','HLTBtagCSVSequenceL3','HLTAK4PFJetsSequence',
           'hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF',
           'hltL1sQuadJetCIorTripleJetVBFIorHTT','hltPreQuadJet45TripleBTagCSVp087','hltQuadCentralJet45','hltBTagCaloCSVp087Triple','hltQuadPFCentralJetLooseID45',
           #Filters for HLT_DoubleJet90_Double30_TripleBTagCSV_p087
           'hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet', 'hltPreDoubleJet90Double30TripleBTagCSVp087',
           #'HLTAK4CaloJetsSequence',
           'hltQuadCentralJet30', 'hltDoubleCentralJet90',
           #'HLTFastPrimaryVertexSequence', 'HLTBtagCSVSequenceL3' , 'hltBTagCaloCSVp087Triple', 'HLTAK4PFJetsSequence',
           'hltQuadPFCentralJetLooseID30', 'hltDoublePFCentralJetLooseID90',
           #Filters for HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v
           'hltBTagCaloCSVp14Single','hltBTagPFCSVp056Double','hltCaloJetFilterSixC25','hltCaloJetsSix25ForHt','hltCaloSixJet25HT300','hltHtMhtCaloJetsSixC25','hltHtMhtPFJetsSixC30','hltL1sHTT280IorHTT300','hltPFJetFilterSixC30','hltPFJetsSix30ForHt','hltPFSixJet30HT400','hltPrePFHT400SixJet30DoubleBTagCSVp056',
#           'hltTripleJet50'
           #Filters for HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v
           'hltBTagCaloCSVp022Single','hltBTagPFCSVp016SingleWithMatching','hltBTagPFCSVp11DoubleWithMatching','hltDoubleJet65','hltPFDoubleJetLooseID76','hltPFQuadJetLooseID15','hltPFSingleJetLooseID92','hltPFTripleJetLooseID64','hltPreQuadPFJetBTagCSVp016p11VBFMqq240','hltQuadJet15','hltSelector6PFJets','hltSingleJet80','hltTripleJet50','hltVBFCaloJetEtaSortedMqq150Deta1p5','hltVBFPFJetCSVSortedMqq240Detaqq2p3',
           #Filters for HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v
           'hltPreQuadPFJetBTagCSVp016VBFMqq500','hltVBFPFJetCSVSortedMqq500Detaqq4p1',
),
    ),
    jetSet = cms.PSet(
        jets = cms.InputTag(jets_to_be_used),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight                                                                                    
        jet1pt = cms.double(20.),#HIG-17-021
        jet2pt = cms.double(20.),#HIG-17-021
        jeteta = cms.double(5.2),#!!!!!!#(4.7),#HIG-17-021
        isAOD = cms.bool(False),
        addQGdiscriminator = cms.bool(False),
        ebRecHits = cms.InputTag("reducedEcalRecHitsEB", "","RECO"),
        eeRecHits  = cms.InputTag("reducedEcalRecHitsEE", "","RECO"),
        esRecHits = cms.InputTag("reducedEcalRecHitsES", "","RECO"),
        recalibrateJets = cms.bool(False),###!!!! already corrected by updateJetCollection
        recalibrateMass = cms.bool(False),
        recalibratePuppiMass = cms.bool(False),
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
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'ALPHA'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string("AK4PFchs_pt"),
        jerNameSf = cms.string("AK4PFchs"),
        softdropPuppiMassString = cms.string("ak8PFJetsPuppiSoftDropMass"),#"ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMass"),# if pt_AK8<170 else "ak8PFJetsPuppiSoftDropMass"),
    ),
    chsFatJetSet = cms.PSet(
        jets = cms.InputTag('slimmedJetsAK8'),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight                                                                                    
        jet1pt = cms.double(170.),
        jet2pt = cms.double(170.),
        jeteta = cms.double(2.4),
        isAOD = cms.bool(False),
        addQGdiscriminator = cms.bool(False),
        ebRecHits = cms.InputTag("reducedEcalRecHitsEB", "","RECO"),
        eeRecHits  = cms.InputTag("reducedEcalRecHitsEE", "","RECO"),
        esRecHits = cms.InputTag("reducedEcalRecHitsES", "","RECO"),
        recalibrateJets = cms.bool(False),
        recalibrateMass = cms.bool(False),
        recalibratePuppiMass = cms.bool(False),
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
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'ALPHA'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string("AK4PFchs_pt"),
        jerNameSf = cms.string("AK4PFchs"),
        softdropPuppiMassString = cms.string("ak8PFJetsPuppiSoftDropMass"),#"ak8PFJetsPuppiValueMap:ak8PFJetsPuppiSoftDropMass"),# if pt_AK8<170 else "ak8PFJetsPuppiSoftDropMass"),
    ),
    electronSet = cms.PSet(
        electrons = cms.InputTag('slimmedElectrons'),
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        eleVetoId = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),#see https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2#Accessing_ID_result
        eleLooseId = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
        eleMediumId = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
        eleTightId = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
        eleHEEPId = cms.string('heepElectronID-HEEPV70'),
        ## Looks like the following 4 Ids are still valid: https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentificationRun2
        eleMVANonTrigMediumId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'),#see https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaMiniAODV2#Accessing_ID_result
        eleMVANonTrigTightId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
        eleMVATrigMediumId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'), ### NOTE -> SAME AS NON-TRIG IN 2017
        eleMVATrigTightId = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'), ### NOTE -> SAME AS NON-TRIG IN 2017
        ###
        eleEcalRecHitCollection = cms.InputTag("reducedEgamma:reducedEBRecHits"),
        eleSingleTriggerIsoFileName = cms.string('data/SingleEleTriggerEff.root'), # FIXME where to find most recent file?
        eleSingleTriggerFileName = cms.string('data/eleTriggerEff_MORIOND17.root'), # FIXME where to find most recent file?
        eleVetoIdFileName = cms.string('data/%s.root' % (eleVetoIDstring)),
        eleLooseIdFileName = cms.string('data/%s.root' % (eleLooseIdstring)),
        eleMediumIdFileName = cms.string('data/%s.root' % (eleMediumIdstring)),
        eleTightIdFileName = cms.string('data/%s.root' % (eleTightIdstring)),
        eleMVATrigMediumIdFileName = cms.string('data/%s.root' % (eleMVA90noISOstring)), #FIXME: Double check: added here noiso files
        eleMVATrigTightIdFileName = cms.string('data/%s.root' % (eleMVA80noISOstring)), #FIXME: Double check: added here noiso files
        eleRecoEffFileName = cms.string('data/eleRecoSF_MORIOND17.root'), # FIXME where to find most recent file?
        eleScaleSmearCorrectionName = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Moriond17_23Jan_ele'),
        electron1id = cms.int32(0), # 0: veto, 1: loose, 2: medium, 3: tight, 4: HEEP, 5: MVA medium nonTrig, 6: MVA tight nonTrig, 7: MVA medium Trig, 8: MVA tight Trig
        electron2id = cms.int32(0),
        electron1pt = cms.double(10),
        electron2pt = cms.double(10),
    ),
    muonSet = cms.PSet(
        muons = cms.InputTag('cleanedMuons'),#('muonTriggerMatchHLTMuons'),#('slimmedMuons'),#
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        #        muonTrkFileName = cms.string('data/MuonTrkEfficienciesAndSF_MORIOND17.root'),# todo: is this used?
        muonIdFileName = cms.string('data/%s.root' %(MuonSFIDstring)),#('data/MuonIdEfficienciesAndSF_MORIOND17.root'),
        muonIsoFileName = cms.string('data/%s.root' %(MuonSFISOstring)),#('data/MuonIsoEfficienciesAndSF_MORIOND17.root'),
        #        muonTrkHighptFileName = cms.string('data/tkhighpt_2016full_absetapt.root'),# todo: is this used?
        muonTriggerFileName = cms.string('data/%s.root' %(MuonSFTriggerstring)),#('data/MuonTrigEfficienciesAndSF_MORIOND17.root'),
        #        doubleMuonTriggerFileName = cms.string('data/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root'),#FIXME -> obsolete# todo: what about this???
        muon1id = cms.int32(1), # 0: tracker high pt muon id, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(1),
        muon1iso = cms.int32(1), # 0: trk iso (<0.1), 1: loose (<0.25), 2: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(1),
        muon1pt = cms.double(35.),
        muon2pt = cms.double(35.),
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
        phoLooseId = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
        phoMediumId = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
        phoTightId = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
        phoMVANonTrigMediumId = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
        phoEcalRecHitCollection = cms.InputTag("reducedEgamma:reducedEBRecHits"),
        phoLooseIdFileName = cms.string('data/%s.root' % (phoLooseIdFilestring)),
        phoMediumIdFileName = cms.string('data/%s.root' % (phoMediumIdFilestring)),
        phoTightIdFileName = cms.string('data/%s.root' % (phoTightIdFilestring)),
        phoMVANonTrigMediumIdFileName = cms.string('data/%s.root' % (phoMVANonTrigMediumIdFilestring)),
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
        pfCandMinPt = cms.double(0.),
    ),
    minGenBpt = cms.double(15.),#gen b quarks in acceptance
    maxGenBeta = cms.double(2.4),#gen b quarks in acceptance
    invmassVBF = cms.double(400.),#as per trigger####(300.),#https://indico.desy.de/indico/event/20983/contribution/0/material/slides/0.pdf
    detaVBF = cms.double(3.0),##(2.5),#https://indico.desy.de/indico/event/20983/contribution/0/material/slides/0.pdf
    writeNJets = cms.int32(0),#(1),#compare if identical
    writeNFatJets = cms.int32(0),#(2),
    writeNGenBquarks = cms.int32(4),#(4),
    writeNGenLongLiveds = cms.int32(2),#(2),
    writeNMatchedJets = cms.int32(0),#(4),
    writeNLeptons = cms.int32(2),#wait, to be restored
    ##
    writeOnlyTriggerEvents = cms.bool(False),#(False),#slims down ntuples a lot

###########################
### THESE MUST BE KEPT: ###
###########################

# commenting 11 Jun 2019, only for debugging purposes

    writeOnlyL1FilterEvents = cms.bool(False),#!!!!!!!!!!!!!!!!!!!!#slims down ntuples a lot
    writeOnlyisVBFEvents = cms.bool(isVBF),#slims down ntuples a lot
    writeFatJets = cms.bool(False),#not needed now
    writeJetPFCandidates = cms.bool(False),
    writeAllPFCandidates = cms.bool(False),
    writeLostTracks = cms.bool(False),
    writeVertices = cms.bool(True),#(True),
    performPreFiringStudies = cms.bool(False),#cms.bool(True if ('unprefirable' in process.source.fileNames[0]) else False),
    ##
    verbose = cms.bool(False),
    verboseTrigger  = cms.bool(False),#(False),
    svTagInfoProducer = cms.untracked.InputTag("inclusiveSecondaryVertexFinderTagInfos"),
    updatedPatJets = cms.untracked.InputTag("updatedPatJet"),
    signal = cms.bool(isSignal),
    AlgInputTag = cms.InputTag("gtStage2Digis"),
    l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
    l1Seeds = cms.vstring("L1_TripleJet_84_68_48_VBF","L1_TripleJet_88_72_56_VBF","L1_TripleJet_92_76_64_VBF","L1_HTT280","L1_HTT300","L1_HTT320","L1_SingleJet170","L1_SingleJet180","L1_SingleJet200","L1_DoubleJetC100","L1_DoubleJetC112","L1_DoubleJetC120","L1_QuadJetC50", "L1_QuadJetC60", "L1_ETM100", "L1_ETM105", "L1_ETM110", "L1_ETM115", "L1_ETM120","L1_ZeroBias","L1_SingleJet60","L1_SingleJet35",),
    ReadPrescalesFromFile = cms.bool(True),
)


task.add(process.patAlgosToolsTask)


process.seq = cms.Sequence(
##unscheduled:
    process.egammaPostRecoSeq *
    process.counter *
#    process.BadPFMuonFilter *
#    process.BadChargedCandidateFilter *
#    process.primaryVertexFilter *
#    process.EGMRegression * process.EGMSmearerElectrons * process.EGMSmearerPhotons *
#    process.egmGsfElectronIDSequence *
#    process.egmPhotonIDSequence *
#    process.cleanedMuons *
    #process.muonTriggerMatchHLTMuons *
#    process.unpackTV *
#    process.jetTracksAssociatorAtVertex *
#    process.updatedPatJets *
#    process.pfImpactParameterTagInfos *
#    process.pfSecondaryVertexTagInfos *
#    process.pfInclusiveSecondaryVertexFinderTagInfos *
#    process.pfSecondaryVertexNegativeTagInfos *
#    process.softPFMuonsTagInfos *
#    process.softPFElectronsTagInfos *
#    process.updatedPatJetsTransientCorrected *
#    process.ak4PFchsCorrectedJets *#1 Feb
    process.trigger
)


process.p = cms.Path(process.seq)
process.p.associate(task)
#print process.p

#open('pydump_recluster_and_reconstruct.py','w').write(process.dumpPython())

outFile = open("tmpConfig_TriggerStudies.py","w")
outFile.write(process.dumpPython())
outFile.close()
