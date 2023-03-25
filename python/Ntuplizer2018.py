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
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #Central production 2017:
            # 'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_rp_94X_mc2017_realistic_v14-v1/00000/0093CC5C-E152-EA11-AA49-0CC47A706FFE.root',
            #Central production 2018:
            # 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/00000/1CAA3AC7-DFB2-A14D-90C1-084D867FB078.root',
            # 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/120000/04A4F8B8-1FC5-C042-A6FF-9E474A712334.root',
            # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/2921539A-9EEE-3040-B2C2-A7C27BE3DCAD.root',
            #Privately produced signal point:
            # "file:/pnfs/desy.de/cms/tier2/store/user/kjpena/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/PrivateMC_MINIAODSIM-102X_upgrade2018_realistic_v15-v1/230126_204439/0000/step4_ggH_HToSSTobbbb_MH-125_MS-15_ctauS-1_13TeV_50.root"
            #JiaJing's
            #'/store/group/phys_exotica/jmao/aodsim/RunIISummer16/MINIAODSIM/MSSM-1d-prod/n3n2-n1-hbb-hbb_mh300_pl1000_ev100000/crab_CMSSW_9_4_12_n3n2-n1-hbb-hbb_mchi300_pl1000_ev100000_MINIAODSIM_CaltechT2/200222_061026/0000/SUS-RunIIFall17DRPremix-00183_MINIAOD_9.root'
            #'/store/user/kjpena/miniAODv3_08Feb2020/VBFH_HToSSTobbbb_MH-125_MS-50_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_MINIAODSIM/200209_083121/0000/output_1.root'
            #'file:/nfs/dust/cms/user/lbenato/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_privateMC_102X_RECO_v1_generation_forMS_output_100_MINIAOD.root'
            #test 2017 MC:
            #'/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D0CB832F-0742-E811-87A1-0CC47A4D76AC.root'
#          '/store/mc/RunIIFall17MiniAODv2/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/966FD47C-6FB8-E811-8B1A-0242AC1C0500.root'
            #'/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/3017154C-F483-964E-855B-E06F2590FD6B.root'#2018 MC with muons!  #
            #2016 background
            #'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/00214FA3-001F-E911-AC83-0CC47A4F1CF6.root',
            # '/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/C6031D62-7BF1-E811-BC1C-001E672480BB.root',
            #'/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E65DC503-55C9-E611-9A11-02163E019C7F.root',
            #'/store/mc/RunIISummer16MiniAODv3/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FE8AFB84-5DEA-E811-83C4-68CC6EA5BD1A.root',
            #'/store/mc/RunIISummer16MiniAODv3/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/001B3D66-B4C0-E811-B670-44A84225C4EB.root'
          #'/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/16099EC8-13EA-E811-9559-0CC47A4C7340.root',
          #'/store/mc/RunIISummer16MiniAODv3/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/08E2D468-67EF-E811-850B-7CD30ABD295A.root',
          #'/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/00A80353-4FEA-E811-9282-6CC2173CAAE0.root'
            #2018 background
            # 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/037A79A2-18C7-314B-AD6B-A8DA89B1447B.root',
            # 'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/00000/0271701E-A142-B343-B514-0267656D901D.root',
            #'file:/pnfs/desy.de/cms/tier2//store/mc/RunIIAutumn18MiniAOD/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/270000/FFB1D063-1653-9441-BCE5-088A8DB0086D.root'
            # 'file:/pnfs/desy.de/cms/tier2/store/mc/RunIIAutumn18MiniAOD/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/100000/02DCC1DD-1EEF-2A4D-9641-8703D1D025FB.root',
            # 'file:/pnfs/desy.de/cms/tier2/store/mc/RunIIAutumn18MiniAOD/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/120000/8D294FFA-4895-DC4F-A0AB-12855041E202.root',
            # 'file:/pnfs/desy.de/cms/tier2/store/mc/RunIIAutumn18MiniAOD/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/120000/946007D8-EE1B-D748-8B7C-A44CFCB51A2E.root',
            # 'file:/pnfs/desy.de/cms/tier2//store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/17D5FDFE-C156-FE47-9202-F819E74881D3.root',
            #2017 background?
            #'root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/00000/007D59B8-82B3-E811-A052-EC0D9A0B30E0.root',
            #'file:/pnfs/desy.de/cms/tier2/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0047429F-5042-E811-81C4-003048CDCDE0.root',
           #'/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-100To200_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0047429F-5042-E811-81C4-003048CDCDE0.root',
            #'file:/pnfs/desy.de/cms/tier2//store/mc/RunIIAutumn18MiniAOD/WW_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/7639FB10-DF53-8242-89D8-7A5E5817A3E4.root'
            #'file:/afs/desy.de/user/e/eichm/public/forLisa/VBFH_m20_ctau500.root'
#            'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_Summer16_MINIAODSIM_calojets_Tranche2/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_Tranche2_MINIAODSIM_calojets/181218_125055/0000/miniaod_1.root',
            #'/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_Summer16_MINIAODSIM_24May2018/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_MINIAODSIM_24May2018/180529_093853/0000/miniaod_15.root'

            #2018 data:
            # '/store/data/Run2018A/ParkingBPH6/MINIAOD/05May2019-v1/10000/006A9697-3892-B349-B110-C67EEBE19601.root',
            '/store/data/Run2018A/ParkingBPH3/MINIAOD/05May2019-v1/100000/00E44CC8-4FFC-FF4F-9549-FAB57802DB89.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/130000/262AFD38-A2F6-8444-BC76-5095518254EA.root',
            #'/store/data/Run2018A/DisplacedJet/MINIAOD/17Sep2018-v1/110000/058F82F8-9D9D-544D-A7AA-387D778D67DF.root',
            #'file:/pnfs/desy.de/cms/tier2//store/data/Run2018C/MET/MINIAOD/17Sep2018-v1/60000/ED1603BC-E2EC-D042-8262-6FF525FA0CA5.root'
            # '/store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/270000/4682963C-2EFF-FF4D-B234-8ED5973F70E4.root',
        ),
        # eventsToProcess = cms.untracked.VEventRange('1:26195013-1:26195015','1:27082933-1:27082935'),

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
    is2018            = True if('RunIIAutumn18' in process.source.fileNames[0] or 'Run2018' in process.source.fileNames[0] or '102X_upgrade2018' in process.source.fileNames[0]) else False
    isPromptReco      = ('PromptReco' in process.source.fileNames[0])
    noLHEinfo         = True if ('WW_TuneCUETP8M1_13TeV-pythia8' or 'WZ_TuneCUETP8M1_13TeV-pythia8' or 'ZZ_TuneCUETP8M1_13TeV-pythia8' or 'WW_TuneCP5_13TeV-pythia8' or 'WZ_TuneCP5_13TeV-pythia8' or 'ZZ_TuneCP5_13TeV-pythia8') in process.source.fileNames[0] else False #check for PythiaLO samples
    isbbH             = True if ('bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo' in process.source.fileNames[0]) else False #bbH has a different label in LHEEventProduct
    isSignal          = True if ('HToSSTobbbb' in process.source.fileNames[0] or 'HToSSTo4b' in process.source.fileNames[0]) else False
    isCentralProd     = True if (isSignal and '/store/mc/' in process.source.fileNames[0]) else False
    isCalo            = False #HERE for calo analyses!!!
    isTracking        = True
    isShort           = False #HERE for short lifetime analyses!!!
    isControl         = False #HERE for control region!!!
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
print 'isCentralProd', isCentralProd

if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSY)>1):
   print "More than one theoretical model selected! Aborting...."
   exit()

if(int(isCalo) + int(isTracking) + int(isShort)>1):
   print "More than one phase space selected! Aborting...."
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

if isTracking:
    print "\n"
    print "***************************************"
    print "***************************************"
    print "***************************************"
    print "\n"
    print "Performing TRACKING LIFETIMES analysis!"
    print "\n"
    print "***************************************"
    print "***************************************"
    print "***************************************"
    print "\n"

if isShort:
    print "\n"
    print "***************************************"
    print "***************************************"
    print "***************************************"
    print "\n"
    print "Performing analysis for SHORT LIFETIMES!"
    print "\n"
    print "***************************************"
    print "***************************************"
    print "***************************************"
    print "\n"

if isControl:
   print "\n"
   print "***************************************"
   print "***************************************"
   print "***************************************"
   print "\n"
   print "Running CONTROL REGION!"
   print "\n"
   print "***************************************"
   print "***************************************"
   print "***************************************"
   print "\n"

if(isTwinHiggs and isCalo):
    pt_AK4 = 5
elif(isShort):
   pt_AK4 = 20
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
   if isData:#TODO: Change to v14 for 2016, 2017 & 2018 A-C
      if is2016:
         GT = '102X_dataRun2_v13'
      elif is2017:
         GT = '102X_dataRun2_v13'
      elif is2018:
         if any(s in process.source.fileNames[0] for s in theRun2018ABC): GT = '102X_dataRun2_v14'
         if any(s in process.source.fileNames[0] for s in theRun2018D):   GT = '102X_dataRun2_Prompt_v16'
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
#       JEC/JER         #
#-----------------------#

# Jet corrector https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrOnTheFly
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')


JECstring = ''
if RunLocal:
    if isData and (isReReco or isReMiniAod):
      if any(s in process.source.fileNames[0] for s in theRunBCD2016):
        JECstring = "Summer16_23Sep2016BCDV3_DATA" #if isReMiniAod else "Summer16_23Sep2016BCDV3_DATA"
      if any(s in process.source.fileNames[0] for s in theRunEF2016):
        JECstring = "Summer16_23Sep2016EFV3_DATA" #if isReMiniAod else "Summer16_23Sep2016EFV3_DATA"
      if any(s in process.source.fileNames[0] for s in theRunG2016):
        JECstring = "Summer16_23Sep2016GV3_DATA" #if isReMiniAod else "Summer16_23Sep2016GV3_DATA"
      if any(s in process.source.fileNames[0] for s in theRunH2016):
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
      # if isControl: exit()
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
        if isTracking:
            jsonName = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON"
        else:
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

process.load('RecoMET.METFilters.ecalBadCalibFilter_cfi')
process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter("EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal       = cms.vuint32([872439604,872422825,872420274,872423218,
                                    872423215,872416066,872435036,872439336,
                                    872420273,872436907,872420147,872439731,
                                    872436657,872420397,872439732,872439339,
                                    872439603,872422436,872439861,872437051,
                                    872437052,872420649,872422436,872421950,
                                    872437185,872422564,872421566,872421695,
                                    872421955,872421567,872437184,872421951,
                                    872421694,872437056,872437057,872437313]),
    taggingMode      = cms.bool(True),
    debug            = cms.bool(False)
)

task.add(process.BadPFMuonFilter)
task.add(process.BadChargedCandidateFilter)
task.add(process.ecalBadCalibReducedMINIAODFilter)

#-----------------------#
#       COUNTER         #
#-----------------------#
process.counter = cms.EDAnalyzer('CounterAnalyzer',
    #lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
    genProduct = cms.InputTag('generator'),
    pythiaLOSample = cms.bool(True if noLHEinfo else False),
)

#-----------------------#
#  b TAGGING tagInfos   #
#-----------------------#

bTagInfos = [
    'pfImpactParameterTagInfos'
   ,'pfSecondaryVertexTagInfos'
   ,'pfInclusiveSecondaryVertexFinderTagInfos'
]

bTagDiscriminators = [
   'pfCombinedInclusiveSecondaryVertexV2BJetTags'
   ,'pfCombinedSecondaryVertexV2BJetTags'
   ,'pfBoostedDoubleSecondaryVertexAK8BJetTags'
   ]

# # taken from here: https://github.com/cms-sw/cmssw/blob/02d4198c0b6615287fd88e9a8ff650aea994412e/RecoBTag/ImpactParameter/python/impactParameterTagInfos_cfi.py
process.load("RecoBTag.ImpactParameter.pfImpactParameterTagInfos_cfi")
process.pfImpactParameterTagInfos.primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pfImpactParameterTagInfos.maximumChiSquared = cms.double(99999.9)
process.pfImpactParameterTagInfos.maximumLongitudinalImpactParameter = cms.double(99999.9)
process.pfImpactParameterTagInfos.maximumTransverseImpactParameter = cms.double(99999.9)
process.pfImpactParameterTagInfos.minimumNumberOfHits = cms.int32(0)
process.pfImpactParameterTagInfos.minimumNumberOfPixelHits = cms.int32(1)#at least 1, otherwise tracking issues!13Dec
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

for n in ['pfSecondaryVertexTagInfos', 'pfInclusiveSecondaryVertexFinderTagInfos', 'pfSecondaryVertexNegativeTagInfos', 'pfInclusiveSecondaryVertexFinderNegativeTagInfos', 'pfInclusiveSecondaryVertexFinderCvsLTagInfos', 'pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos']:
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

process.load('RecoBTag/SoftLepton/softPFMuonTagInfos_cfi')
process.load('RecoBTag/SoftLepton/softPFElectronTagInfos_cfi')

#-----------------------#
#    Recluster jets     #
#-----------------------#

#Jet labels
print "pt_AK4: ", pt_AK4
if isCalo and pt_AK4<10:
   print "\n"
   print "AK4 will be reclustered!"
   print "pt_AK4 = ", pt_AK4
   chosen_JEC = "AK4PFchs"
   chosen_jet_source = 'ak4PFJetsCHSCustom'
   chosen_label = 'Reclustered'
   chosen_pfcand = 'pfCHS'
   chosen_jets = "patJets"+ chosen_label
   #pt_AK4 = 5
else:
   print "\n"
   print "AK4 won't be reclustered!"
   print "pt_AK4 = ", pt_AK4
   print "\n"
   chosen_jets = "slimmedJets"
   #pt_AK4 = 15

## packedPFCandidates with CHS are used by both AK4 and AK8
process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
task.add(process.pfCHS)

## Filter out neutrinos from packed GenParticles
if not isData:
   process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))
   task.add(process.packedGenParticlesForJetsNoNu)

## Define GenJets
if not isData:
   from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
   process.ak4GenJetsNoNu = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu')
   task.add(process.ak4GenJetsNoNu)

#-----------------------#
#    AK4 only for CALO  # #NEW
#-----------------------#

if isCalo and pt_AK4<10:

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
      jetCorrections = (chosen_JEC, ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),#correct JEC
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

pt_AK8 = 170

if pt_AK8<170:
   ### Gen jets
   if not isData:
      from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
      process.ak8GenJetsNoNu = ak4GenJets.clone(src = 'prunedGenParticlesForJetsNoNu', rParam = 0.8)
      task.add(process.ak8GenJetsNoNu)

   ### Reco AK8 CHS jets
   from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
   process.ak8PFJetsCHSCustom  = ak4PFJets.clone (src = 'pfCHS', rParam = 0.8, doAreaFastjet = True, jetPtMin = pt_AK8)
   task.add(process.ak8PFJetsCHSCustom)

   ### Reco AK8 Puppi jets
   process.load('CommonTools/PileupAlgos/Puppi_cff')
   ## e.g. to run on miniAOD
   process.puppi.candName = cms.InputTag('packedPFCandidates')
   process.puppi.vertexName = cms.InputTag('offlineSlimmedPrimaryVertices')
   process.puppi.clonePackedCands   = cms.bool(True)
   process.puppi.useExistingWeights = cms.bool(True)
   task.add(process.puppi)

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
       jetCorrections = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
       genJetCollection = cms.InputTag('ak8GenJetsNoNu'),
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
       jetCorrections = ('AK8PFPuppi', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
       genJetCollection = cms.InputTag('ak8GenJetsNoNu'),
       genParticles = cms.InputTag('prunedGenParticles'),
       algo = 'AK',
       rParam = 0.8
   )
   task.add(process.patJetsAK8PuppiReclustered)

   ### Pat CHS softdrop fat jets
   addJetCollection(
      process,
      labelName = 'AK8CHSSoftDrop',
      jetSource = cms.InputTag('ak8PFJetsCHSSoftDropReclustered'),
      btagDiscriminators = ['None'],
      jetCorrections = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
      pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
      svSource = cms.InputTag('slimmedSecondaryVertices'),
      genJetCollection = cms.InputTag('ak8GenJetsNoNu'), # AK4 gen jets!
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
      jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
      explicitJTA = True,  # needed for subjet b tagging
      svClustering = True, # needed for subjet b tagging
      genJetCollection = cms.InputTag('ak4GenJetsNoNu'), # AK4 gen jets!
      genParticles = cms.InputTag('prunedGenParticles'),
      fatJets=cms.InputTag('ak8PFJetsCHSCustom'), # needed for subjet flavor clustering
      groomedFatJets=cms.InputTag('ak8PFJetsCHSSoftDropReclustered') # needed for subjet flavor clustering
   )
   task.add(process.patJetsAK8CHSSoftDropSubjets)

   ### Groomed masses CHS
   from RecoJets.JetProducers.ak8PFJetsCHS_groomingValueMaps_cfi import ak8PFJetsCHSPrunedMass, ak8PFJetsCHSSoftDropMass
   process.ak8PFJetsCHSPrunedMass = ak8PFJetsCHSPrunedMass.clone(src = cms.InputTag("ak8PFJetsCHSCustom"),matched = cms.InputTag("ak8PFJetsCHSPrunedReclustered"),)
   process.ak8PFJetsCHSSoftDropMass = ak8PFJetsCHSSoftDropMass.clone(src = cms.InputTag("ak8PFJetsCHSCustom"),matched = cms.InputTag("ak8PFJetsCHSSoftDropReclustered"),)
   process.patJetsAK8CHSReclustered.userData.userFloats.src += ['ak8PFJetsCHSPrunedMass','ak8PFJetsCHSSoftDropMass']
   task.add(process.ak8PFJetsCHSPrunedMass)
   task.add(process.ak8PFJetsCHSSoftDropMass)

   ### Groomed masses Puppi
   from RecoJets.JetProducers.ak8PFJetsPuppi_groomingValueMaps_cfi import ak8PFJetsPuppiSoftDropMass
   process.ak8PFJetsPuppiPrunedMass = ak8PFJetsCHSPrunedMass.clone(src = cms.InputTag("ak8PFJetsPuppiCustom"),matched = cms.InputTag("ak8PFJetsPuppiPrunedReclustered"),)
   process.ak8PFJetsPuppiSoftDropMass = ak8PFJetsPuppiSoftDropMass.clone(src = cms.InputTag("ak8PFJetsPuppiCustom"),matched = cms.InputTag("ak8PFJetsPuppiSoftDropReclustered"),)
   process.patJetsAK8PuppiReclustered.userData.userFloats.src += ['ak8PFJetsPuppiPrunedMass','ak8PFJetsPuppiSoftDropMass']
   task.add(process.ak8PFJetsPuppiPrunedMass)
   task.add(process.ak8PFJetsPuppiSoftDropMass)


   ## N-subjettiness
   from RecoJets.JetProducers.nJettinessAdder_cfi import *
   process.NjettinessAK8 = Njettiness.clone(src='ak8PFJetsCHSCustom')#src='ak8PFJets', cone=0.8)
   process.NjettinessAK8.cone = cms.double(0.8)
   process.patJetsAK8CHSReclustered.userData.userFloats.src += ['NjettinessAK8:tau1','NjettinessAK8:tau2','NjettinessAK8:tau3']
   task.add(process.NjettinessAK8)

   process.NjettinessAK8Puppi = Njettiness.clone(src='ak8PFJetsPuppiCustom')#src='ak8PFJets', cone=0.8)
   process.NjettinessAK8Puppi.cone = cms.double(0.8)
   process.patJetsAK8PuppiReclustered.userData.userFloats.src += ['NjettinessAK8Puppi:tau1','NjettinessAK8Puppi:tau2','NjettinessAK8Puppi:tau3']
   task.add(process.NjettinessAK8Puppi)


   ## PF AK8 matching to PF Puppi AK8
   process.ak8PFJetsPuppiValueMap = cms.EDProducer("RecoJetToPatJetDeltaRValueMapProducer",
                                                   src = cms.InputTag("ak8PFJetsCHSCustom"),#CHS
                                                   matched = cms.InputTag("patJetsAK8PuppiReclustered"),#PUPPI
                                                   distMax = cms.double(0.8),
                                                   values = cms.vstring([
            'userFloat("NjettinessAK8Puppi:tau1")',
            'userFloat("NjettinessAK8Puppi:tau2")',
            'userFloat("NjettinessAK8Puppi:tau3")',
            'userFloat("ak8PFJetsPuppiSoftDropMass")',
            'userFloat("ak8PFJetsPuppiPrunedMass")',
            'pt','eta','phi','mass'
            ]),
                                                   valueLabels = cms.vstring( [
            'NjettinessAK8PuppiTau1',
            'NjettinessAK8PuppiTau2',
            'NjettinessAK8PuppiTau3',
            'ak8PFJetsPuppiSoftDropMass',
            'ak8PFJetsPuppiPrunedMass',
            'pt','eta','phi','mass'
            ])
                                                   )

   task.add(process.ak8PFJetsPuppiValueMap)

   #Adding values to AK8
   process.patJetsAK8CHSReclustered.userData.userFloats.src += [cms.InputTag('ak8PFJetsPuppiValueMap','NjettinessAK8PuppiTau1'),
                                                         cms.InputTag('ak8PFJetsPuppiValueMap','NjettinessAK8PuppiTau2'),
                                                         cms.InputTag('ak8PFJetsPuppiValueMap','NjettinessAK8PuppiTau3'),
                                                         cms.InputTag('ak8PFJetsPuppiValueMap','ak8PFJetsPuppiSoftDropMass'),
                                                         cms.InputTag('ak8PFJetsPuppiValueMap','ak8PFJetsPuppiPrunedMass'),
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
jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
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
  , 'pfDeepCSVJetTags:probudsg'
  , 'pfDeepCSVJetTags:probb'
  , 'pfDeepCSVJetTags:probc'
  , 'pfDeepCSVJetTags:probbb'
  # , 'pfNegativeDeepCSVJetTags:probudsg'
  # , 'pfNegativeDeepCSVJetTags:probb'
  # , 'pfNegativeDeepCSVJetTags:probc'
  # , 'pfNegativeDeepCSVJetTags:probbb'
  # , 'pfPositiveDeepCSVJetTags:probudsg'
  # , 'pfPositiveDeepCSVJetTags:probb'
  # , 'pfPositiveDeepCSVJetTags:probc'
  # , 'pfPositiveDeepCSVJetTags:probbb'
  #   # DeepFlavour
  , 'pfDeepFlavourJetTags:probb'
  , 'pfDeepFlavourJetTags:probbb'
  , 'pfDeepFlavourJetTags:problepb'
  , 'pfDeepFlavourJetTags:probc'
  , 'pfDeepFlavourJetTags:probuds'
  , 'pfDeepFlavourJetTags:probg'
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
'''
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
    #jets = cms.InputTag(chosen_jets if isCalo else "slimmedJets")
    jets = cms.InputTag("slimmedJets")#!!!!wrong
)
'''

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

if pt_AK8<170:
   jetSourceSoftDrop = "selectedPatJetsAK8CHSSoftDropSubjets"
   postfixSoftDrop = "SoftDropSubjets"

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

   task.add(process.updatedPatJetsSoftDropSubjets)
   task.add(process.updatedPatJetsTransientCorrectedSoftDropSubjets)


   ## Establish references between PATified fat jets and subjets using the BoostedJetMerger
   process.slimmedJetsAK8CHSSoftDropPacked = cms.EDProducer("BoostedJetMerger",
           jetSrc=cms.InputTag("selectedPatJetsAK8CHSSoftDrop"),#here the selected pat softdrop fat jets
           subjetSrc=cms.InputTag(soft_drop_subjets_after_btag_tools),#("selectedPatJetsAK8CHSSoftDropSubjets")#("slimmedJetsAK8CHSSoftDropSubjets")#here the slimmed pat softdrop subjets
       )

   task.add(process.slimmedJetsAK8CHSSoftDropPacked)

   process.packedPatJetsAK8 = cms.EDProducer("JetSubstructurePacker",
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

   task.add(process.packedPatJetsAK8)

#patJetsAK8Reclustered
chosen_AK8 = "packedPatJetsAK8" # including SoftDrop info
#chosen_AK8 = "patJetsAK8CHSReclustered"#'slimmedJetsAK8'


#-----------------------#
#    Imperial Tagger    #
#-----------------------#

process.pfXTagInfos = cms.EDProducer("XTagInfoProducer",
    jets = cms.InputTag(jets_after_btag_tools),
    shallow_tag_infos = cms.InputTag('pfDeepCSVTagInfosFinal'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    muonSrc  = cms.InputTag("slimmedMuons"),
    electronSrc = cms.InputTag("slimmedElectrons")
)

process.pfXTags = cms.EDProducer("XTagProducer",
    graph_path=cms.FileInPath("LLPReco/XTagProducer/data/da.pb"),
    src=cms.InputTag("pfXTagInfos"),
    ctau_values=cms.vdouble(-2., -1., 0., 1., 2., 3.), # provide log(ctau/1mm) to be evaluated: i.e. 10 mum, 1 mm and 1 m here
    ctau_descriptors=cms.vstring("0p01", "0p1", "1", "10", "100", "1000") # provide log(ctau/1mm) to be evaluated: i.e. 1 mum, 1 mm and 1 m here
)

#task.add(process.patJetCorrFactors)
task.add(process.pfXTagInfos)
task.add(process.pfXTags)

#-----------------------#
#   ROI-based tagger    #
#-----------------------#

if isTracking:
    process.load("HiggsLongLived.TreeMaker.unpackedTracksAndVertices_cfi")

    from HiggsLongLived.TreeMaker.goodTrackProducer_cfi import goodTrackProducer
    process.ntupleGoodTrackProducer = goodTrackProducer.clone(
      tracks = cms.InputTag ("unpackedTracksAndVertices", "", "ntuple"),
    )

    from HiggsLongLived.TreeMaker.generalV0Candidates_cfi import generalV0Candidates
    process.ntupleGeneralV0Candidates = generalV0Candidates.clone(
       vertices = cms.InputTag('unpackedTracksAndVertices', '', 'ntuple'),
       trackRecoAlgorithm = cms.InputTag('ntupleGoodTrackProducer', '', 'ntuple'),
    )

    from HiggsLongLived.TreeMaker.regionOfInterestProducer_cfi import regionOfInterestProducer
    process.ntupleRegionOfInterestProducer = regionOfInterestProducer.clone(
        trackClusters = cms.InputTag ("ntupleGeneralV0Candidates", "Kshort", "ntuple"),
    )

    from HiggsLongLived.TreeMaker.regionOfInterestTagger_cfi import regionOfInterestTagger
    process.ntupleRegionOfInterestTagger = regionOfInterestTagger.clone(
        regionsOfInterest = cms.InputTag ("ntupleRegionOfInterestProducer", "", "ntuple"),
    )

    from HiggsLongLived.TreeMaker.clusterTrackAssociator_cfi import clusterTrackAssociator
    process.ntupleClusterTrackAssociator = clusterTrackAssociator.clone(
        regionsOfInterest  =  cms.InputTag  ("ntupleRegionOfInterestProducer",  "",              "ntuple"),
        pfCandidates       =  cms.InputTag  ("ntupleRegionOfInterestTagger",    "pfCandidates",  "ntuple"),
        lostTracks         =  cms.InputTag  ("ntupleRegionOfInterestTagger",    "lostTracks",    "ntuple"),
    )

#-----------------------#
#       PU Jet ID       #
#-----------------------#

#This recipe is suggested on the twiki but it does not work.
#from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_94x, _chsalgos_102x
#process.load("RecoJets.JetProducers.PileupJetID_cfi")
#process.pileupJetId.jets = cms.InputTag('slimmedJets')#(jets_after_btag_tools)
#process.pileupJetId.inputIsCorrected = True
#process.pileupJetId.applyJec = True#?!False
#process.pileupJetId.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
##process.pileupJetId.algos = cms.VPSet(_chsalgos_94x) # for 2017
#process.pileupJetId.algos = cms.VPSet(_chsalgos_102x) # for 2018
##task.add(process.pileupJetId)

#Added by me, but useless:
#process.pileupJetIdCalculator.jets = cms.InputTag('slimmedJets')#(jets_after_btag_tools)
#process.pileupJetIdCalculator.inputIsCorrected = True
#process.pileupJetIdCalculator.applyJec = True#?!False
#process.pileupJetIdCalculator.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")

#process.pileupJetIdEvaluator.jets = cms.InputTag('slimmedJets')#(jets_after_btag_tools)
#process.pileupJetIdEvaluator.inputIsCorrected = True
#process.pileupJetIdEvaluator.applyJec = True#?!False
#process.pileupJetIdEvaluator.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")

#This gives excpetions
#task.add(process.pileUpJetIDTask)

##Adding corrections and updating jets: this alone works, but it's not necessary w/o pileupJetId
#process.load("PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff")
#process.patJetCorrFactorsReapplyJEC = process.updatedPatJetCorrFactors.clone(
#  src = cms.InputTag(jets_after_btag_tools),
#  levels = ['L1FastJet', 'L2Relative', 'L3Absolute'] )

#process.updatedJetsPUID = process.updatedPatJets.clone(
#  jetSource = cms.InputTag(jets_after_btag_tools),
#  jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
#  )

#process.updatedJetsPUID.userData.userInts.src += ['pileupJetId:fullId']
#process.updatedJetsPUID.userData.userFloats.src += ['pileupJetId:fullDiscriminant']

#task.add(process.patJetCorrFactorsReapplyJEC)
#task.add(process.updatedJetsPUID)

#jets_to_be_used = "updatedJetsPUID"
jets_to_be_used = 'updatedPatJetsTransientCorrected'+postfix


#---------------------------------#
#       PU Jet ID-a-la-2016       #
#---------------------------------#

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
  levels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'] if isData else ['L1FastJet', 'L2Relative', 'L3Absolute']
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

process.ntuple = cms.EDAnalyzer('Ntuplizer',
    genSet = cms.PSet(
        genProduct = cms.InputTag('generator'),
        genHeader  = cms.InputTag('generator'),
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
#2016 menu!!!:
### b-like
#'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v', 'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v',
'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', 'HLT_QuadJet45_TripleBTagCSV_p087_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v',

### displaced tracks
#'HLT_VBF_DisplacedJet40_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v', 'HLT_HT350_DisplacedDijet40_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v', 'HLT_HT650_DisplacedDijet80_Inclusive_v', 'HLT_HT750_DisplacedDijet80_Inclusive_v',

### calo lifetimes
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v',
###
#'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v', 'HLT_MET200_v', 'HLT_MET250_v', 'HLT_MET75_IsoTrk50_v', 'HLT_MET90_IsoTrk50_v', 'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v', 'HLT_PFMET110_PFMHT110_IDTight_v', 'HLT_PFMET120_PFMHT120_IDTight_v', 'HLT_PFMET170_HBHECleaned_v', 'HLT_PFMET300_v', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',

###production for MET
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'

### All studied triggers:
# 'HLT_Ele27_WPTight_Gsf_v',  'HLT_Ele25_eta2p1_WPTight_Gsf_v',  'HLT_Ele27_eta2p1_WPTight_Gsf_v',  'HLT_Ele32_eta2p1_WPTight_Gsf_v',  'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',  'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',  'HLT_IsoMu24_v',  'HLT_IsoMu22_eta2p1_v',  'HLT_IsoTkMu24_v',  'HLT_IsoMu27_v',  'HLT_IsoTkMu22_eta2p1_v',  'HLT_IsoTkMu27_v',  'HLT_Mu50_v',  'HLT_TkMu50_v',  'HLT_Mu55_v',  'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',  'HLT_Mu6_PFHT200_PFMET100_v',  'HLT_Mu15_IsoVVVL_PFHT400_v',  'HLT_Ele15_IsoVVVL_PFHT400_v',  'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v',  'HLT_Mu50_IsoVVVL_PFHT400_v',  'HLT_Ele50_IsoVVVL_PFHT400_v',  'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v',  'HLT_Mu30_eta2p1_PFJet150_PFJet50_v',  'HLT_DoubleMu3_PFMET50_v',  'HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v',  'HLT_Ele15_IsoVVVL_PFHT400_PFMET50_v',  'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v',  'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v',  'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v',  'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v',  'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v',  'HLT_Ele27_WPTight_Gsf_L1JetTauSeeded_v',  'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',  'HLT_Mu30_TkMu11_v',  'HLT_Mu17_Mu8_SameSign_DZ_v',  'HLT_Mu40_TkMu11_v',  'HLT_Mu20_Mu10_SameSign_DZ_v',  'HLT_DoubleMu8_Mass8_PFHT300_v',  'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',  'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v',  'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v',  'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v',  'HLT_AK8PFJet360_TrimMass30_v',  'HLT_AK8PFJet450_v',  'HLT_AK8PFJet500_v',  'HLT_BTagMu_AK8Jet300_Mu5_v',  'HLT_BTagMu_Jet300_Mu5_v',  'HLT_CaloJet500_NoJetID_v',  'HLT_DiCentralPFJet170_CFMax0p1_v',  'HLT_DiCentralPFJet330_CFMax0p5_v',  'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v',  'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v',  'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v',  'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v',  'HLT_DoubleMu3_PFMET50_v',  'HLT_DoubleMu8_Mass8_PFHT300_v',  'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',  'HLT_Ele15_IsoVVVL_PFHT400_v',  'HLT_HT350_DisplacedDijet40_DisplacedTrack_v',  'HLT_HT350_DisplacedDijet80_DisplacedTrack_v',  'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',  'HLT_HT650_DisplacedDijet80_Inclusive_v',  'HLT_HT650_v',  'HLT_HT750_DisplacedDijet80_Inclusive_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v',  'HLT_MET300_v',  'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v',  'HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v',  'HLT_Mu15_IsoVVVL_PFHT400_v',  'HLT_Mu15_IsoVVVL_PFHT600_v',  'HLT_Mu17_Mu8_SameSign_DZ_v',  'HLT_Mu25_TkMu0_dEta18_Onia_v',  'HLT_Mu30_TkMu11_v',  'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v',  'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',  'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v',  'HLT_Mu40_eta2p1_PFJet200_PFJet50_v',  'HLT_Mu6_PFHT200_PFMET100_v',  'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v',  'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v',  'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v',  'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v',  'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v',  'HLT_PFHT450_SixJet40_BTagCSV_p056_v',  'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v',  'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v',  'HLT_PFHT900_v',  'HLT_PFJet450_v',  'HLT_PFJet500_v',  'HLT_PFMET400_v',  'HLT_PFMET500_v',  'HLT_PFMET600_v',  'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_QuadJet45_TripleBTagCSV_p087_v',  'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v',  'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v',  'HLT_Rsq0p25_v',  'HLT_Rsq0p30_v',  'HLT_RsqMR270_Rsq0p09_MR200_4jet_v',  'HLT_TkMu50_v',  'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v',  'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v',  'HLT_VBF_DisplacedJet40_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v',  'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v',  'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',  'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v',  'HLT_PFMET110_PFMHT110_IDTight_v',  'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_PFMET120_PFMHT120_IDTight_v',  'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v',  'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_PFMET170_HBHECleaned_v',  'HLT_PFHT300_PFMET110_v',  'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',  'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v',  'HLT_MET200_v',  'HLT_RsqMR270_Rsq0p09_MR200_v',  'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v',  'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v',  'HLT_MET250_v',  'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v',   'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v',  'HLT_PFMET300_v',  'HLT_MET75_IsoTrk50_v',  'HLT_MET90_IsoTrk50_v',
#
###Control paths for VBF, prescaled
#'HLT_L1_TripleJet_VBF_v', 'HLT_QuadPFJet_VBF_v','HLT_DiPFJetAve40_v','HLT_DiPFJetAve60_v','HLT_DiPFJetAve80_v','HLT_PFJet40_v','HLT_PFJet60_v','HLT_PFJet80_v',
###TEST
##'HLT_AK8PFJet450_v',###########TEST
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v'#,'HLT_AK4PFJet30_v7'

#2018 menu
#'HLT_AK8PFHT800_TrimMass50_v',
#'HLT_AK8PFHT850_TrimMass50_v',
#'HLT_AK8PFHT900_TrimMass50_v',
#'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17_v',
#'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1_v',
#'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2_v',
#'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4_v',
#'HLT_AK8PFJet360_TrimMass30_v',
#'HLT_AK8PFJet380_TrimMass30_v',
#'HLT_AK8PFJet400_TrimMass30_v',
#'HLT_AK8PFJet420_TrimMass30_v',
#'HLT_AK8PFJet500_v',
#'HLT_AK8PFJet550_v',
#'HLT_AK8PFJetFwd500_v',
#'HLT_CaloJet500_NoJetID_v',
#'HLT_CaloJet550_NoJetID_v',
#'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
#'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
#'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
#'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v',
#'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v',
#'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepCSV_4p5_v',
#'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v',
#'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v',
#'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v',
#'HLT_PFHT500_PFMET110_PFMHT110_IDTight_v',
#'HLT_PFHT700_PFMET85_PFMHT85_IDTight_v',
#'HLT_PFHT700_PFMET95_PFMHT95_IDTight_v',
#'HLT_PFHT800_PFMET75_PFMHT75_IDTight_v',
#'HLT_PFHT800_PFMET85_PFMHT85_IDTight_v',
#'HLT_PFJet500_v',
#'HLT_PFJet550_v',
#'HLT_PFJetFwd450_v',
#'HLT_PFJetFwd500_v',
#'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
#'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v',
#'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
#'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v',
#'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
#'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v',
#'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
#'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v',
#'HLT_Rsq0p35_v',
#'HLT_Rsq0p40_v',
#'HLT_RsqMR300_Rsq0p09_MR200_4jet_v',
#'HLT_RsqMR300_Rsq0p09_MR200_v',
#'HLT_RsqMR320_Rsq0p09_MR200_4jet_v',
#'HLT_RsqMR320_Rsq0p09_MR200_v',
#'HLT_CaloMET350_HBHECleaned_v',
#'HLT_DiJet110_35_Mjj650_PFMET110_v',
#'HLT_DiJet110_35_Mjj650_PFMET120_v',
#'HLT_DiJet110_35_Mjj650_PFMET130_v',
#'HLT_MET105_IsoTrk50_v',
#'HLT_MET120_IsoTrk50_v',
#'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
#'HLT_MonoCentralPFJet80_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
#'HLT_MonoCentralPFJet80_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
#'HLT_PFMET110_PFMHT110_IDTight_CaloBTagDeepCSV_3p1_v',
#'HLT_PFMET120_PFMHT120_IDTight_CaloBTagDeepCSV_3p1_v',
#'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v',
#'HLT_PFMET120_PFMHT120_IDTight_v',
#'HLT_PFMET130_PFMHT130_IDTight_CaloBTagDeepCSV_3p1_v',
#'HLT_PFMET130_PFMHT130_IDTight_v',
#'HLT_PFMET140_PFMHT140_IDTight_CaloBTagDeepCSV_3p1_v',
#'HLT_PFMET140_PFMHT140_IDTight_v',
#'HLT_PFMET200_HBHE_BeamHaloCleaned_v',
#'HLT_PFMET250_HBHECleaned_v',
#'HLT_PFMET300_HBHECleaned_v',
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v',
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
#'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
#'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
#'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
#'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
#'HLT_TripleJet110_35_35_Mjj650_PFMET110_v',
#'HLT_TripleJet110_35_35_Mjj650_PFMET120_v',
#'HLT_TripleJet110_35_35_Mjj650_PFMET130_v',
###production for MET
#'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
#'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
#'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
]
        ),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter','Flag_badMuons','Flag_duplicateMuons','Flag_noBadMuons') if isReMiniAod else cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter', 'Flag_globalSuperTightHalo2016Filter'),
        prescales = cms.InputTag('patTrigger','',triggerString),
        l1Minprescales = cms.InputTag('patTrigger','l1min',triggerString),
        l1Maxprescales = cms.InputTag('patTrigger','l1max',triggerString),
        objects = cms.InputTag('selectedPatTrigger' if is2016 else 'slimmedPatTrigger','',triggerString),
        badPFMuonFilter = cms.InputTag("BadPFMuonFilter"),
        badChCandFilter = cms.InputTag("BadChargedCandidateFilter"),
        ecalCalibFilter = cms.InputTag("ecalBadCalibReducedMINIAODFilter"),
        l1Gt = cms.InputTag("gtStage2Digis"),
        l1filters = cms.vstring('hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300','hltL1sDoubleJetC112','hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF','hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet','hltL1sSingleMu22','hltL1sV0SingleMu22IorSingleMu25','hltL1sZeroBias','hltL1sSingleJet60','hltL1sSingleJet35','hltTripleJet50','hltDoubleJet65','hltSingleJet80','hltVBFFilterDisplacedJets'),
    ),
    allJetSet = cms.PSet(
        jets = cms.InputTag(jets_to_be_used),#(jets_after_btag_tools),#('updatedPatJetsTransientCorrected'+postfix),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(15.),
        jet2pt = cms.double(15.),
        jeteta = cms.double(5.2),
        isAOD = cms.bool(False),
        addQGdiscriminator = cms.bool(False),
        ebRecHits = cms.InputTag("reducedEcalRecHitsEB", "","RECO"),
        eeRecHits  = cms.InputTag("reducedEcalRecHitsEE", "","RECO"),
        esRecHits = cms.InputTag("reducedEcalRecHitsES", "","RECO"),
        recalibrateJets = cms.bool(False),#(True if is2016 else False),
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
        reshapeBTag = cms.bool(isShort),
        btag = cms.string('deepJet'),
        btagDB = cms.string('data/%s.csv' % (btagSFstring)),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'LLP'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string("AK4PFchs_pt"),#('data/JER/%s/%s_PtResolution_AK4PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
        jerNameSf = cms.string("AK4PFchs"),#('data/JER/%s/%s_SF_AK4PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
    ),
    chsJetSet = cms.PSet(
        jets = cms.InputTag(jets_to_be_used),#(jets_after_btag_tools),#('updatedPatJetsTransientCorrected'+postfix),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(pt_AK4),
        jet2pt = cms.double(pt_AK4),
        jeteta = cms.double(2.4),
        isAOD = cms.bool(False),
        addQGdiscriminator = cms.bool(False),
        ebRecHits = cms.InputTag("reducedEcalRecHitsEB", "","RECO"),
        eeRecHits  = cms.InputTag("reducedEcalRecHitsEE", "","RECO"),
        esRecHits = cms.InputTag("reducedEcalRecHitsES", "","RECO"),
        recalibrateJets = cms.bool(False),#(True if is2016 else False),
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
        reshapeBTag = cms.bool(isShort),
        btag = cms.string('pfDeepFlavourJetTags:probb+pfDeepFlavourJetTags:probbb+pfDeepFlavourJetTags:problepb'),
        btagDB = cms.string('data/%s.csv' % (btagSFstring)),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'LLP'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string("AK4PFchs_pt"),#('data/JER/%s/%s_PtResolution_AK4PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
        jerNameSf = cms.string("AK4PFchs"),#('data/JER/%s/%s_SF_AK4PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
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
        isAOD = cms.bool(False),
        addQGdiscriminator = cms.bool(False),
        ebRecHits = cms.InputTag("reducedEcalRecHitsEB", "","RECO"),
        eeRecHits  = cms.InputTag("reducedEcalRecHitsEE", "","RECO"),
        esRecHits = cms.InputTag("reducedEcalRecHitsES", "","RECO"),
        recalibrateJets = cms.bool(False),#(True if is2016 else False),
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
        reshapeBTag = cms.bool(isShort),
        btag = cms.string('pfDeepFlavourJetTags:probb+pfDeepFlavourJetTags:probbb+pfDeepFlavourJetTags:problepb'),
        btagDB = cms.string('data/%s.csv' % (btagSFstring)),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', 'LLP'),
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string("AK4PFchs_pt"),#('data/JER/%s/%s_PtResolution_AK4PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
        jerNameSf = cms.string("AK4PFchs"),#('data/JER/%s/%s_SF_AK4PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
    ),
    chsFatJetSet = cms.PSet(
        jets = cms.InputTag(chosen_AK8),#('slimmedJetsAK8'),
        jetid = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet1pt = cms.double(pt_AK8),
        jet2pt = cms.double(pt_AK8),
        jeteta = cms.double(2.4),
        isAOD = cms.bool(False),
        addQGdiscriminator = cms.bool(False),
        ebRecHits = cms.InputTag("reducedEcalRecHitsEB", "","RECO"),
        eeRecHits  = cms.InputTag("reducedEcalRecHitsEE", "","RECO"),
        esRecHits = cms.InputTag("reducedEcalRecHitsES", "","RECO"),
        recalibrateJets = cms.bool(False),#(True if is2016 else False),
        recalibrateMass = cms.bool(False),#(True if is2016 else False),#(False),
        recalibratePuppiMass = cms.bool(False),#(True),#(False),
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
        reshapeBTag = cms.bool(isShort),
        btag = cms.string('pfDeepFlavourJetTags:probb+pfDeepFlavourJetTags:probbb+pfDeepFlavourJetTags:problepb'),
        btagDB = cms.string('data/%s.csv' % (btagSFstring)),
        jet1btag = cms.int32(0), # 0: no selection, 1: loose, 2: medium, 3: tight
        jet2btag = cms.int32(0),
        met = cms.InputTag('slimmedMETsMuEGClean', '', '') if isReMiniAod else cms.InputTag('slimmedMETs', '', ''),# 'LLP'
        metRecoil = cms.bool(False),
        metRecoilMC = cms.string('data/recoilfit_gjetsMC_Zu1_pf_v5.root'),
        metRecoilData = cms.string('data/recoilfit_gjetsData_Zu1_pf_v5.root'),
        metTriggerFileName = cms.string('data/MET_trigger_eff_data_SingleMuRunBH.root'),
        jerNameRes = cms.string("AK8PFchs_pt"),#('data/JER/%s/%s_PtResolution_AK8PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
        jerNameSf = cms.string("AK8PFchs"),#('data/JER/%s/%s_SF_AK8PFchs.txt' % (JERstring, JERstring)),#v10 is the latest
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
        muons = cms.InputTag('cleanedMuons'),#('slimmedMuons'),#
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        #        muonTrkFileName = cms.string('data/MuonTrkEfficienciesAndSF_MORIOND17.root'),# todo: is this used?
        muonIdFileName = cms.string('data/%s.root' %(MuonSFIDstring)),#('data/MuonIdEfficienciesAndSF_MORIOND17.root'),
        muonIsoFileName = cms.string('data/%s.root' %(MuonSFISOstring)),#('data/MuonIsoEfficienciesAndSF_MORIOND17.root'),
        #        muonTrkHighptFileName = cms.string('data/tkhighpt_2016full_absetapt.root'),# todo: is this used?
        muonTriggerFileName = cms.string('data/%s.root' %(MuonSFTriggerstring)),#('data/MuonTrigEfficienciesAndSF_MORIOND17.root'),
        #        doubleMuonTriggerFileName = cms.string('data/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root'),#FIXME -> obsolete# todo: what about this???
        muon1id = cms.int32(1), # 0: tracker high pt muon id, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(1),
        muon1iso = cms.int32(1), # 0: trk iso (<0.1), 1: loose (<0.25), no medium, 3: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(1),
        muon1pt = cms.double(10.),
        muon2pt = cms.double(10.),
        muon1eta = cms.double(2.4),
        muon2eta = cms.double(2.4),
        useTuneP = cms.bool(False),
        doRochester = cms.bool(False),
    ) if not isTracking else cms.PSet( #Settings for tracking lifetimes:
        muons = cms.InputTag('slimmedMuons'),#('cleanedMuons'),#
        vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
        #        muonTrkFileName = cms.string('data/MuonTrkEfficienciesAndSF_MORIOND17.root'),# todo: is this used?
        muonIdFileName = cms.string('data/%s.root' %(MuonSFIDstring)),#('data/MuonIdEfficienciesAndSF_MORIOND17.root'),
        muonIsoFileName = cms.string('data/%s.root' %(MuonSFISOstring)),#('data/MuonIsoEfficienciesAndSF_MORIOND17.root'),
        #        muonTrkHighptFileName = cms.string('data/tkhighpt_2016full_absetapt.root'),# todo: is this used?
        muonTriggerFileName = cms.string('data/%s.root' %(MuonSFTriggerstring)),#('data/MuonTrigEfficienciesAndSF_MORIOND17.root'),
        #        doubleMuonTriggerFileName = cms.string('data/MuHLTEfficiencies_Run_2012ABCD_53X_DR03-2.root'),#FIXME -> obsolete# todo: what about this???
        muon1id = cms.int32(1), # 0: tracker high pt muon id, 1: loose, 2: medium, 3: tight, 4: high pt
        muon2id = cms.int32(1),
        muon1iso = cms.int32(-1), # 0: trk iso (<0.1), 1: loose (<0.25), 2: tight (<0.15) (pfIso in cone 0.4)
        muon2iso = cms.int32(-1),
        muon1pt = cms.double(0.0),
        muon2pt = cms.double(0.0),
        muon1eta = cms.double(2.4),
        muon2eta = cms.double(2.4),
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
    roiSet = cms.PSet(
        vertices           = cms.InputTag("offlineSlimmedPrimaryVertices",  ""),
        lostTracks         = cms.InputTag("ntupleClusterTrackAssociator",   "lostTracks",   "ntuple"),
        packedPFCandidates = cms.InputTag("ntupleClusterTrackAssociator",   "pfCandidates", "ntuple"),
        trackClusters      = cms.InputTag("ntupleClusterTrackAssociator",   "",             "ntuple"),
        regionsOfInterest  = cms.InputTag("ntupleRegionOfInterestProducer", "",             "ntuple"),
    ),
    v0Set = cms.PSet(
        kShorts = cms.InputTag('slimmedKshortVertices'),
        lambdas =  cms.InputTag('slimmedLambdaVertices'),
    ),
    #Define gen decay:
    idLLP = cms.int32(idLLP),
    idHiggs = cms.int32(idHiggs),
    idMotherB = cms.int32(idMotherB),
    statusLLP = cms.int32(statusLLP),
    statusHiggs = cms.int32(statusHiggs),

    minGenBpt = cms.double(0.),#gen b quarks in acceptance
    maxGenBeta = cms.double(999),#gen b quarks in acceptance
    #Event preselections
    minHT = cms.double(0.),
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
    writeGenLLPs = cms.bool(True),
    writeGenBquarks = cms.bool(True), #Acceptance cuts a few lines above!
    writeGenMuons = cms.bool(True if isTracking else False),
    writeGenKShorts = cms.bool(True if isTracking else False),
    writeGenLambdas = cms.bool(True if isTracking else False),
    writeNMatchedJets = cms.int32(0),#(4), #Warning: List/Reset JetType functions missing several attributes. Please check before using!
    writeNLeptons = cms.int32(0),#Framework already validated
    ##
    writeOnlyTriggerEvents = cms.bool(True),#slims down ntuples a lot
    writeOnlyL1FilterEvents = cms.bool(False),#slims down ntuples a lot
    writeOnlyisVBFEvents = cms.bool(isVBF),#slims down ntuples a lot
    writeAllJets = cms.bool(False),#used for trigger studies
    writeFatJets = cms.bool(False),#not needed now
    ## PFCandidates:
    writeAK4JetPFCandidates = cms.bool(False), #Matched to AK4 only!
    writeAK8JetPFCandidates = cms.bool(False), #Matched to AK8 only!
    writeAllJetPFCandidates = cms.bool(False), #Matched to either AK4 or AK8
    writeAllPFCandidates = cms.bool(False), #All PFCandidates. Large collection: Please write only if needed!
    ##
    writeLostTracks = cms.bool(False),
    writeVertices = cms.bool(False),
    writeBtagInfos = cms.bool(False),
    writeROITaggerScore = cms.bool(False), #For tracking lifetimes see below
    writeROITaggerInputs = cms.bool(False), #For tracking lifetimes see below
    writeKShorts = cms.bool(True),
    writeLambdas = cms.bool(True),
    calculateNsubjettiness = cms.bool(False),
    performPreFiringStudies = cms.bool(True if ('unprefirable' in process.source.fileNames[0]) else False),
    performVBF = cms.bool(isVBF),
    performggH = cms.bool(isggH),
    verbose = cms.bool(False),
    verboseTrigger  = cms.bool(False),
    signal = cms.bool(isSignal),
    iscalo = cms.bool(isCalo),
    istracking = cms.bool(isTracking),
    isshort = cms.bool(isShort),
    iscontrol = cms.bool(isControl),
    iscentralprod = cms.bool(isCentralProd),
    isera2016 = cms.bool(is2016),
    isera2017 = cms.bool(is2017),
    isera2018 = cms.bool(is2018),
)

if (isTracking and is2016):
    process.ntuple.triggerSet.paths = cms.vstring(
    *[
    ## -------------------------------------------------------------------------------------
    ## DisplacedDijet triggers
    ## -------------------------------------------------------------------------------------
    'HLT_HT350_DisplacedDijet40_DisplacedTrack_v',
    'HLT_HT350_DisplacedDijet80_DisplacedTrack_v',
    'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',
    'HLT_HT650_DisplacedDijet80_Inclusive_v',
    'HLT_HT750_DisplacedDijet80_Inclusive_v',
    ])

if (isTracking and is2017):
    process.ntuple.triggerSet.paths = cms.vstring(
    *[#2017 menu
    ## -------------------------------------------------------------------------------------
    ## ParkingHT triggers:
    ## -------------------------------------------------------------------------------------
    # 'DST_CaloJet40_BTagScouting_v',#                  control prescaled       ParkingHT
    # 'DST_CaloJet40_CaloBTagScouting_v',#              control prescaled       ParkingHT
    # 'DST_CaloJet40_CaloScouting_PFScouting_v',#       control prescaled       ParkingHT
    'DST_HT250_CaloBTagScouting_v',#                    signal  unprescaled     ParkingHT
    'DST_HT250_CaloScouting_v',#                        signal  unprescaled     ParkingHT
    'DST_HT410_BTagScouting_v',#                        signal  unprescaled     ParkingHT
    'DST_HT410_PFScouting_v',#                          signal  unprescaled     ParkingHT
    # 'DST_L1HTT_BTagScouting_v',#                      control prescaled       ParkingHT
    # 'DST_L1HTT_CaloBTagScouting_v',#                  control prescaled       ParkingHT
    # 'DST_L1HTT_CaloScouting_PFScouting_v',#           control prescaled       ParkingHT
    # 'DST_ZeroBias_BTagScouting_v',#                   control prescaled       ParkingHT
    # 'DST_ZeroBias_CaloScouting_PFScouting_v',#        control prescaled       ParkingHT
    ## -------------------------------------------------------------------------------------
    ## ParkingMuon triggers:
    ## -------------------------------------------------------------------------------------
    'DST_DoubleMu3_noVtx_CaloScouting_v',#              signal  unprescaled     ParkingMuon
    # 'DST_L1DoubleMu_BTagScouting_v',#                 control prescaled       ParkingMuon
    # 'DST_L1DoubleMu_CaloScouting_PFScouting_v',#      control prescaled       ParkingMuon
    ## -------------------------------------------------------------------------------------
    ## DisplacedDijet triggers:
    ## -------------------------------------------------------------------------------------
    # 'HLT_HT400_DisplacedDijet40_DisplacedTrack_v',#   control prescaled       DisplacedJet
    # 'HLT_HT425_v',#                                   control prescaled       DisplacedJet
    'HLT_HT430_DisplacedDijet40_DisplacedTrack_v',#     signal	unprescaled     DisplacedJet
    'HLT_HT430_DisplacedDijet60_DisplacedTrack_v',#     backup	unprescaled     DisplacedJet
    'HLT_HT430_DisplacedDijet80_DisplacedTrack_v',#     backup	unprescaled     DisplacedJet
    # 'HLT_HT550_DisplacedDijet60_Inclusive_v',#        control prescaled       DisplacedJet
    # 'HLT_HT550_DisplacedDijet80_Inclusive_v',#        control prescaled       DisplacedJet
    'HLT_HT650_DisplacedDijet60_Inclusive_v',#          backup	unprescaled     DisplacedJet
    'HLT_HT650_DisplacedDijet80_Inclusive_v',#          backup	unprescaled     DisplacedJet
    'HLT_HT750_DisplacedDijet80_Inclusive_v',#          backup	unprescaled     DisplacedJet
    ])

if (isTracking and is2018):
    process.ntuple.triggerSet.paths = cms.vstring(
    *[
    ## -------------------------------------------------------------------------------------
    ## B-Parking triggers:
    ## -------------------------------------------------------------------------------------

    'HLT_Mu7_IP4_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu8_IP3_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu8_IP5_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu8p5_IP3p5_part0_v',
    'HLT_Mu8_IP6_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu9_IP0_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu9_IP3_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu9_IP4_part0_v',#!!                           signal  disabled        ParkingBPH1
    'HLT_Mu9_IP5_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu9_IP6_part0_v',#                             signal  prescaled       ParkingBPH1
    'HLT_Mu10p5_IP3p5_part0_v',
    'HLT_Mu12_IP6_part0_v',#                            signal  prescaled       ParkingBPH1

    # # 'HLT_Mu12_IP6_ToCSCS_v',#                         signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu7_IP4_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu8_IP3_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu8_IP5_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu8_IP6_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu9_IP4_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu9_IP5_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS
    # # 'HLT_Mu9_IP6_ToCSCS_v',#                          signal  disabled        ParkingBPHPromptCSCS

    'HLT_Mu7_IP4_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu8_IP3_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu8_IP5_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu8p5_IP3p5_part1_v',
    'HLT_Mu8_IP6_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu9_IP0_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu9_IP3_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu9_IP4_part1_v',#                             signal  disabled        ParkingBPH2
    'HLT_Mu9_IP5_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu9_IP6_part1_v',#                             signal  prescaled       ParkingBPH2
    'HLT_Mu10p5_IP3p5_part1_v',
    'HLT_Mu12_IP6_part1_v',#                            signal  prescaled       ParkingBPH2

    'HLT_Mu7_IP4_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu8_IP3_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu8_IP5_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu8p5_IP3p5_part2_v',
    'HLT_Mu8_IP6_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu9_IP0_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu9_IP3_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu9_IP4_part2_v',#                             signal  disabled        ParkingBPH3
    'HLT_Mu9_IP5_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu9_IP6_part2_v',#                             signal  prescaled       ParkingBPH3
    'HLT_Mu10p5_IP3p5_part2_v',
    'HLT_Mu12_IP6_part2_v',#                            signal  prescaled       ParkingBPH3

    'HLT_Mu7_IP4_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu8_IP3_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu8_IP5_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu8p5_IP3p5_part3_v',
    'HLT_Mu8_IP6_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu9_IP0_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu9_IP3_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu9_IP4_part3_v',#                             signal  disabled        ParkingBPH4
    'HLT_Mu9_IP5_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu9_IP6_part3_v',#                             signal  prescaled       ParkingBPH4
    'HLT_Mu10p5_IP3p5_part3_v',
    'HLT_Mu12_IP6_part3_v',#                            signal  prescaled       ParkingBPH4

    'HLT_Mu7_IP4_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu8_IP3_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu8_IP5_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu8p5_IP3p5_part4_v',
    'HLT_Mu8_IP6_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu9_IP0_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu9_IP3_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu9_IP4_part4_v',#                             signal  disabled        ParkingBPH5
    'HLT_Mu9_IP5_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu9_IP6_part4_v',#                             signal  prescaled       ParkingBPH5
    'HLT_Mu10p5_IP3p5_part4_v',
    'HLT_Mu12_IP6_part4_v',#                            signal  prescaled       ParkingBPH5

    'HLT_Mu7_IP4_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu8_IP3_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu8_IP5_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu8p5_IP3p5_part5_v',
    'HLT_Mu8_IP6_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu9_IP0_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu9_IP3_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu9_IP4_part5_v',#                             signal  disabled        ParkingBPH6
    'HLT_Mu9_IP5_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu9_IP6_part5_v',#                             signal  prescaled       ParkingBPH6
    'HLT_Mu10p5_IP3p5_part5_v',
    'HLT_Mu12_IP6_part5_v',#                            signal  prescaled       ParkingBPH6
    ## -------------------------------------------------------------------------------------
    ## DisplacedDijet triggers:
    ## -------------------------------------------------------------------------------------
    # # 'HLT_HT400_DisplacedDijet40_DisplacedTrack_v',#   control prescaled       DisplacedJet
    # # 'HLT_HT425_v',#                                   control prescaled       DisplacedJet
    # 'HLT_HT430_DisplacedDijet40_DisplacedTrack_v',#     signal  unprescaled     DisplacedJet
    # 'HLT_HT430_DisplacedDijet60_DisplacedTrack_v',#     backup  unprescaled     DisplacedJet
    # 'HLT_HT500_DisplacedDijet40_DisplacedTrack_v',#     backup  unprescaled     DisplacedJet
    # # 'HLT_HT550_DisplacedDijet60_Inclusive_v',#        control prescaled       DisplacedJet
    # 'HLT_HT650_DisplacedDijet60_Inclusive_v',#          backup  unprescaled     DisplacedJet
    ])


    scenario = "2018_25ns_JuneProjectionFull18_PoissonOOTPU"

    process.ntuple.pileupSet_HLT_Mu7_IP4 = process.ntuple.pileupSet.clone(
        dataFileName     = cms.string('data/PU_69200_2018-HLT_Mu7_IP4.root'),
        dataFileNameUp   = cms.string('data/PU_72380_2018-HLT_Mu7_IP4.root'),
        dataFileNameDown = cms.string('data/PU_66020_2018-HLT_Mu7_IP4.root'),
        mcFileName = cms.string('data/PU_MC_%s.root' % (scenario)),          
        mcName = cms.string(scenario),                                       
    )

    process.ntuple.pileupSet_HLT_Mu9_IP6 = process.ntuple.pileupSet.clone(
        dataFileName     = cms.string('data/PU_69200_2018-HLT_Mu9_IP6.root'),
        dataFileNameUp   = cms.string('data/PU_72380_2018-HLT_Mu9_IP6.root'),
        dataFileNameDown = cms.string('data/PU_66020_2018-HLT_Mu9_IP6.root'),
        mcFileName = cms.string('data/PU_MC_%s.root' % (scenario)),
        mcName = cms.string(scenario),
    )

    process.ntuple.pileupSet_HLT_Mu9_IP6_UL = process.ntuple.pileupSet.clone(
        dataFileName     = cms.string('data/PU_69200_2018-HLT_Mu9_IP6.root'),
        dataFileNameUp   = cms.string('data/PU_72380_2018-HLT_Mu9_IP6.root'),
        dataFileNameDown = cms.string('data/PU_66020_2018-HLT_Mu9_IP6.root'),
        # Using UL MC scenario: "2018_25ns_UltraLegacy_PoissonOOTPU"
    )

    process.ntuple.pileupSet_HLT_Mu9_IP6_v7 = process.ntuple.pileupSet.clone(
        dataFileName     = cms.string('data/PU_69200_2018-v6-HLT_Mu9_IP6.root'),#FIXME - Update to v7 after processing data
        dataFileNameUp   = cms.string('data/PU_72380_2018-v6-HLT_Mu9_IP6.root'),#FIXME - Update to v7 after processing data
        dataFileNameDown = cms.string('data/PU_66020_2018-v6-HLT_Mu9_IP6.root'),#FIXME - Update to v7 after processing data
        mcFileName = cms.string('data/PU_MC_%s.root' % (scenario)),
        mcName = cms.string(scenario),
    )

    process.ntuple.pileupSet_HLT_Mu12_IP6 = process.ntuple.pileupSet.clone(
        dataFileName     = cms.string('data/PU_69200_2018-HLT_Mu12_IP6.root'),
        dataFileNameUp   = cms.string('data/PU_72380_2018-HLT_Mu12_IP6.root'),
        dataFileNameDown = cms.string('data/PU_66020_2018-HLT_Mu12_IP6.root'),
        mcFileName = cms.string('data/PU_MC_%s.root' % (scenario)),
        mcName = cms.string(scenario),        
    )

if (isShort and is2016):
   process.ntuple.triggerSet.paths = cms.vstring(
      *[
         ## -------------------------------------------------------------------------------------
         ## Triggers for b-like lifetimes
         ## -------------------------------------------------------------------------------------
          'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v',
          'HLT_QuadJet45_TripleBTagCSV_p087_v',
          'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v',
          'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v',
          ])

if (isShort and is2017):
#   print("Update trigger menu!")
#   exit()
   process.ntuple.triggerSet.paths = cms.vstring(
      *[
         ])
if (isShort and is2018):
   print("Update trigger menu!")
   exit()
   process.ntuple.triggerSet.paths = cms.vstring(
      *[
         ])

#-----------------------#
#       TEST            #
#-----------------------#

process.test = cms.EDAnalyzer('LLP2018',
    electrons = cms.untracked.InputTag('slimmedElectrons'),
    eleVetoIdMap = cms.untracked.string('cutBasedElectronID-Fall17-94X-V2-veto'),
)

#-----------------------#
#  Particle List Drawer #
#-----------------------#

process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.ParticleListDrawer = cms.EDAnalyzer('ParticleListDrawer',
    maxEventsToPrint = cms.untracked.int32(10),
    src = cms.InputTag('prunedGenParticles'),
    printOnlyHardInteraction = cms.untracked.bool(False),
    useMessageLogger = cms.untracked.bool(False)
)

#------------------------#
#  Particle Decay Drawer #
#------------------------#

process.ParticleDecayDrawer = cms.EDAnalyzer("ParticleDecayDrawer",
    src = cms.InputTag("prunedGenParticles"),
    printP4 = cms.untracked.bool(False),
    printPtEtaPhi = cms.untracked.bool(False),
    printVertex = cms.untracked.bool(False)
)

task.add(process.patAlgosToolsTask)
#maybe here?
#task.add(process.pileupJetId, process.patAlgosToolsTask)
#task.add(process.pileUpJetIDTask)

process.printContent = cms.EDAnalyzer("EventContentAnalyzer")

process.seq = cms.Sequence(
    process.egammaPostRecoSeq *
    #process.packedPFCandidates *
    #process.packedCandsForTkIso *
    #process.lostTracksForTkIso *
    #process.lostTracks *
    #process.reducedEgamma *
    #process.heepIDVarValueMaps *
    #process.egmPhotonIDs *
    #process.egmGsfElectronIDs *
    #process.patPhotons *
    #process.patElectrons *
    #process.selectedPatPhotons *
    #process.selectedPatElectrons *
    ##process.slimmedPhotons *
    ##process.slimmedElectrons *
    ####process.fullPatMetSequenceTEST *#leading to segfault
    process.counter *
    ##process.test
    process.ntuple
)

writeROIs = True #Switch to add ROI information (set to False in the PSet above)
if isTracking and writeROIs:

    process.ntuple.writeROITaggerScore = cms.bool(True)
    process.ntuple.writeROITaggerInputs = cms.bool(False)

    process.seq = cms.Sequence(
        process.egammaPostRecoSeq *
        #process.packedPFCandidates *
        #process.packedCandsForTkIso *
        #process.lostTracksForTkIso *
        #process.lostTracks *
        #process.reducedEgamma *
        #process.heepIDVarValueMaps *
        #process.egmPhotonIDs *
        #process.egmGsfElectronIDs *
        #process.patPhotons *
        #process.patElectrons *
        #process.selectedPatPhotons *
        #process.selectedPatElectrons *
        ##process.slimmedPhotons *
        ##process.slimmedElectrons *
        ####process.fullPatMetSequenceTEST *#leading to segfault
        process.counter *
        ##process.test
        process.unpackedTracksAndVertices +
        process.ntupleGoodTrackProducer +
        process.ntupleGeneralV0Candidates +
        process.ntupleRegionOfInterestProducer +
        process.ntupleRegionOfInterestTagger +
        process.ntupleClusterTrackAssociator +
        #process.printContent *
        process.ntuple
    )

# process.seq = cms.Sequence(process.ParticleDecayDrawer)
# process.seq = cms.Sequence(process.ParticleListDrawer)

process.p = cms.Path(process.seq)
process.p.associate(task)

## If we want to keep the output miniaod:
#from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
#process.OUT = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('test.root'),
#    outputCommands = cms.untracked.vstring(['keep *', 'keep *_pfXTags_*_*', 'keep *_pfXTagInfos_*_*', 'drop *_reco*_*_*', 'drop recoVert*_*_*_*']),
#    ###outputCommands = cms.untracked.vstring(['keep *_pfXTags_*_*', 'keep *_pfXTagInfos_*_*', 'drop *']),
#)

#process.endpath= cms.EndPath(process.OUT)

outFile = open("tmpConfig_Ntuplizer2018.py","w")
outFile.write(process.dumpPython())
outFile.close()
