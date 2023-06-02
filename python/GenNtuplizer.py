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
    "PisCentralProd", False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "isCentralProd parser flag"
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
    "PjsonName", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    " jsonName parser flag"
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
    "PtriggerTag", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "triggerTag parser flag"
)
options.register(
    "PtriggerString", "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "triggerString parser flag"
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
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
         fileNames = cms.untracked.vstring(
            'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH_HToSSTobbbb_MH-125_MS-20_ctauS-1000_Summer16_MINIAODSIM_calojets/GluGluH_HToSSTobbbb_MH-125_MS-20_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_MINIAODSIM_calojets/181203_140031/0000/miniaod_1.root'
            #'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_Summer16_MINIAODSIM_calojets_Tranche2/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_Tranche2_MINIAODSIM_calojets/181218_125055/0000/miniaod_1.root',
            #'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_Summer16_AODSIM_Tranche2/VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_Tranche2_AODSIM/181214_110243/0000/aodsim_1.root'
            #'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FE57DDB4-DDBA-E611-A344-0025905A6064.root',
            #'file:/pnfs/desy.de/cms/tier2/store/data/Run2016G/MET/AOD/07Aug17-v1/110000/3C4239F2-E9A0-E711-82F7-02163E014117.root' 
            #JiaJing's:
            #'/store/group/phys_exotica/jmao/aodsim/RunIISummer16/MINIAODSIM/MSSM-1d-prod/n3n2-n1-hbb-hbb_mh300_pl1000_ev100000/crab_CMSSW_9_4_12_n3n2-n1-hbb-hbb_mchi300_pl1000_ev100000_MINIAODSIM_CaltechT2/200222_061026/0000/SUS-RunIIFall17DRPremix-00183_MINIAOD_9.root'
            #'/store/group/phys_exotica/jmao/aodsim/RunIISummer16/MINIAODSIM/MSSM-1d-prod/n3n2-n1-hbb-hbb_mh200_pl1000_ev100000/crab_CMSSW_9_4_12_n3n2-n1-hbb-hbb_mchi200_pl1000_ev100000_MINIAODSIM_CaltechT2/200222_061142/0000/SUS-RunIIFall17DRPremix-00183_MINIAOD_9.root'
           #'/store/group/phys_exotica/jmao/aodsim/RunIISummer16/MINIAODSIM/MSSM-1d-prod/n3n2-n1-hbb-hbb_mh400_pl1000_ev100000/crab_CMSSW_9_4_12_n3n2-n1-hbb-hbb_mchi400_pl1000_ev100000_MINIAODSIM_CaltechT2/200222_060935/0000/SUS-RunIIFall17DRPremix-00183_MINIAOD_9.root'

            #my heavy higgs GEN-SIM:
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_1.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_2.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_3.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_4.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_5.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_6.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_7.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_8.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_9.root',
          # 'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_Fall18/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC/RunIIFall18wmGS-102X_upgrade2018_realistic_v11_GENSIM/200302_153817/0000/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output_10.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-10000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-500_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-2000_output.root',
          #'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-5000_output.root',

          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-8_ctauS-1000_output.root',
          ##'file:/nfs/dust/cms/user/lbenato/GenerationFolder/CMSSW_10_2_18/src/GluGluH2_H2ToSSTobbbb_MH-125_MS-8_ctauS-10000_output.root',

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
    isSignal          = True if ('HToSSTobbbb_MH-125' in process.source.fileNames[0] or 'HToSSTo4b_MH-125' in process.source.fileNames[0]) else False
    isCentralProd     = True if ('HToSSTo4b_MH-125' in process.source.fileNames[0] or 'ggH_HToSSTobbbb_MH-125' in process.source.fileNames[0]) else False
    isCalo            = False #HERE for calo analyses!!!
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
print 'isCentralProd', isCentralProd

if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSY)>1):
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
#       COUNTER         #
#-----------------------#
process.counter = cms.EDAnalyzer('CounterAnalyzer',
    genProduct = cms.InputTag('generator'),
    #lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
    pythiaLOSample = cms.bool(True if noLHEinfo else False),
)

#-----------------------#
#       ANALYZER        #
#-----------------------#

process.ntuple = cms.EDAnalyzer('GenNtuplizer',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        lheProduct = cms.InputTag('externalLHEProducer'),
        genParticles = cms.InputTag('prunedGenParticles' if "MINIAOD" in process.source.fileNames[0] else 'genParticles'),
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
    #Define gen decay:
    idLLP = cms.int32(idLLP),
    idHiggs = cms.int32(idHiggs),
    idMotherB = cms.int32(idMotherB),
    statusLLP = cms.int32(statusLLP),
    statusHiggs = cms.int32(statusHiggs),

    minGenBpt = cms.double(0.),#(15.),#gen b quarks in acceptance
    maxGenBeta = cms.double(999.),#(2.4),#gen b quarks in acceptance
    minGenBradius2D = cms.double(0.),#new!! in cm
    maxGenBradius2D = cms.double(10.),#new!! in cm
    minGenBetaAcc = cms.double(0.),#(2.4),#
    maxGenBetaAcc = cms.double(2.4),#(2.4),#
    ###writeGenVBFquarks = cms.bool(True),
    writeGenHiggs = cms.bool(True),
    writeGenBquarks = cms.bool(True), #Acceptance cuts a few lines above!
    writeGenLLPs = cms.bool(True),
    verbose = cms.bool(False),
    iscentralprod = cms.bool(isCentralProd),
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
