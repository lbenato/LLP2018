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
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 500

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #test 2017 MC:
            #'/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D0CB832F-0742-E811-87A1-0CC47A4D76AC.root'
            #'/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/3017154C-F483-964E-855B-E06F2590FD6B.root'#2018 MC with muons!  #
            #'/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-200To400_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E65DC503-55C9-E611-9A11-02163E019C7F.root',
            #'file:/afs/desy.de/user/e/eichm/public/forLisa/VBFH_m20_ctau500.root'
            'file:/pnfs/desy.de/cms/tier2/store/user/lbenato/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_Summer16_MINIAODSIM_calojets_Tranche2/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC/RunIISummer16-PU_premix-Moriond17_80X_mcRun2_2016_Tranche2_MINIAODSIM_calojets/181218_125055/0000/miniaod_1.root',
            
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
        if isReMiniAod and any(s in process.source.fileNames[0] for s in theRunH): GT = '80X_dataRun2_Prompt_v16'
        else: GT = '80X_dataRun2_2016SeptRepro_v7'#'auto:run2_data'#'80X_dataRun2_2016LegacyRepro_v4'#
    elif not(isData):
        GT = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'#Moriond17 GT
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
setupEgammaPostRecoSeq(process,runEnergyCorrections=False,era='2016-Legacy')#era='2018-Prompt'

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
#        FILTERS        #
#-----------------------#

# JSON filter
if isData:
    import FWCore.PythonUtilities.LumiList as LumiList
    jsonName = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON"#"Cert_294927-305364_13TeV_PromptReco_Collisions17_JSON"#"Cert_294927-301567_13TeV_PromptReco_Collisions17_JSON" #golden json
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

## Define GenJets
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.ak4GenJetsNoNu = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu')
task.add(process.ak4GenJetsNoNu)

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
process.ak8GenJetsNoNu = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu', rParam = 0.8)
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
    jetCorrections = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
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
    jetCorrections = ('AK8PFPuppi', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
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
   jetCorrections = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
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
   jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
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
### b-like
#'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v', 'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v', 'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v', 'HLT_QuadJet45_TripleBTagCSV_p087_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v', 'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v',

### displaced tracks
#'HLT_VBF_DisplacedJet40_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v', 'HLT_HT350_DisplacedDijet40_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v', 'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v', 'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v', 'HLT_HT650_DisplacedDijet80_Inclusive_v', 'HLT_HT750_DisplacedDijet80_Inclusive_v',

### calo lifetimes
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v',
###
#'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v', 'HLT_MET200_v', 'HLT_MET250_v', 'HLT_MET75_IsoTrk50_v', 'HLT_MET90_IsoTrk50_v', 'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v', 'HLT_PFMET110_PFMHT110_IDTight_v', 'HLT_PFMET120_PFMHT120_IDTight_v', 'HLT_PFMET170_HBHECleaned_v', 'HLT_PFMET300_v', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',

###production for MET
'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'

### All studied triggers:
# 'HLT_Ele27_WPTight_Gsf_v',  'HLT_Ele25_eta2p1_WPTight_Gsf_v',  'HLT_Ele27_eta2p1_WPTight_Gsf_v',  'HLT_Ele32_eta2p1_WPTight_Gsf_v',  'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v',  'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',  'HLT_IsoMu24_v',  'HLT_IsoMu22_eta2p1_v',  'HLT_IsoTkMu24_v',  'HLT_IsoMu27_v',  'HLT_IsoTkMu22_eta2p1_v',  'HLT_IsoTkMu27_v',  'HLT_Mu50_v',  'HLT_TkMu50_v',  'HLT_Mu55_v',  'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v',  'HLT_Mu6_PFHT200_PFMET100_v',  'HLT_Mu15_IsoVVVL_PFHT400_v',  'HLT_Ele15_IsoVVVL_PFHT400_v',  'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v',  'HLT_Mu50_IsoVVVL_PFHT400_v',  'HLT_Ele50_IsoVVVL_PFHT400_v',  'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v',  'HLT_Mu30_eta2p1_PFJet150_PFJet50_v',  'HLT_DoubleMu3_PFMET50_v',  'HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v',  'HLT_Ele15_IsoVVVL_PFHT400_PFMET50_v',  'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v',  'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v',  'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v',  'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v',  'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v',  'HLT_Ele27_WPTight_Gsf_L1JetTauSeeded_v',  'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',  'HLT_Mu30_TkMu11_v',  'HLT_Mu17_Mu8_SameSign_DZ_v',  'HLT_Mu40_TkMu11_v',  'HLT_Mu20_Mu10_SameSign_DZ_v',  'HLT_DoubleMu8_Mass8_PFHT300_v',  'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',  'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v',  'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v',  'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v',  'HLT_AK8PFJet360_TrimMass30_v',  'HLT_AK8PFJet450_v',  'HLT_AK8PFJet500_v',  'HLT_BTagMu_AK8Jet300_Mu5_v',  'HLT_BTagMu_Jet300_Mu5_v',  'HLT_CaloJet500_NoJetID_v',  'HLT_DiCentralPFJet170_CFMax0p1_v',  'HLT_DiCentralPFJet330_CFMax0p5_v',  'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v',  'HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v',  'HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v',  'HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v',  'HLT_DoubleMu3_PFMET50_v',  'HLT_DoubleMu8_Mass8_PFHT300_v',  'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',  'HLT_Ele15_IsoVVVL_PFHT400_v',  'HLT_HT350_DisplacedDijet40_DisplacedTrack_v',  'HLT_HT350_DisplacedDijet80_DisplacedTrack_v',  'HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v',  'HLT_HT650_DisplacedDijet80_Inclusive_v',  'HLT_HT650_v',  'HLT_HT750_DisplacedDijet80_Inclusive_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v',  'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v',  'HLT_MET300_v',  'HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v',  'HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v',  'HLT_Mu15_IsoVVVL_PFHT400_v',  'HLT_Mu15_IsoVVVL_PFHT600_v',  'HLT_Mu17_Mu8_SameSign_DZ_v',  'HLT_Mu25_TkMu0_dEta18_Onia_v',  'HLT_Mu30_TkMu11_v',  'HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v',  'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v',  'HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v',  'HLT_Mu40_eta2p1_PFJet200_PFJet50_v',  'HLT_Mu6_PFHT200_PFMET100_v',  'HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v',  'HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v',  'HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v',  'HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v',  'HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v',  'HLT_PFHT450_SixJet40_BTagCSV_p056_v',  'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v',  'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v',  'HLT_PFHT900_v',  'HLT_PFJet450_v',  'HLT_PFJet500_v',  'HLT_PFMET400_v',  'HLT_PFMET500_v',  'HLT_PFMET600_v',  'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_QuadJet45_TripleBTagCSV_p087_v',  'HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v',  'HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v',  'HLT_Rsq0p25_v',  'HLT_Rsq0p30_v',  'HLT_RsqMR270_Rsq0p09_MR200_4jet_v',  'HLT_TkMu50_v',  'HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v',  'HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v',  'HLT_VBF_DisplacedJet40_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v',  'HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v',  'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v',  'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',  'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v',  'HLT_PFMET110_PFMHT110_IDTight_v',  'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_PFMET120_PFMHT120_IDTight_v',  'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v',  'HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v',  'HLT_PFMET170_HBHECleaned_v',  'HLT_PFHT300_PFMET110_v',  'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v',  'HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v',  'HLT_MET200_v',  'HLT_RsqMR270_Rsq0p09_MR200_v',  'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v',  'HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v',  'HLT_MET250_v',  'HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v',   'HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v',  'HLT_PFMET300_v',  'HLT_MET75_IsoTrk50_v',  'HLT_MET90_IsoTrk50_v',
#
###Control paths for VBF, prescaled
#'HLT_L1_TripleJet_VBF_v', 'HLT_QuadPFJet_VBF_v','HLT_DiPFJetAve40_v','HLT_DiPFJetAve60_v','HLT_DiPFJetAve80_v','HLT_PFJet40_v','HLT_PFJet60_v','HLT_PFJet80_v',
###TEST
##'HLT_AK8PFJet450_v',###########TEST
#'HLT_VBF_DisplacedJet40_VTightID_Hadronic_v', 'HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v'#,'HLT_AK4PFJet30_v7'
]
        ),
        metfilters = cms.InputTag('TriggerResults', '', filterString),
        metpaths = cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter','Flag_badMuons','Flag_duplicateMuons','Flag_noBadMuons') if isReMiniAod else cms.vstring('Flag_HBHENoiseFilter', 'Flag_HBHENoiseIsoFilter', 'Flag_EcalDeadCellTriggerPrimitiveFilter', 'Flag_goodVertices', 'Flag_eeBadScFilter', 'Flag_globalTightHalo2016Filter'),
        prescales = cms.InputTag('patTrigger','','PAT'),
        l1Minprescales = cms.InputTag('patTrigger','l1min','PAT'),
        l1Maxprescales = cms.InputTag('patTrigger','l1max','PAT'),
        objects = cms.InputTag('slimmedPatTrigger' if is2017 else 'selectedPatTrigger','','PAT'),
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
        recalibrateJets = cms.bool(False if is2017 else True),
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
        recalibrateJets = cms.bool(False if is2017 else True),
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
        recalibrateJets = cms.bool(False if is2017 else True),
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
        recalibrateJets = cms.bool(False if is2017 else True),
        recalibrateMass = cms.bool(False if is2017 else True),#(False),
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
        phoLooseId = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
        phoMediumId = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
        phoTightId = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
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


#-----------------------#
#       TEST            #
#-----------------------#

process.test = cms.EDAnalyzer('LLP2018',
    electrons = cms.untracked.InputTag('slimmedElectrons'),
    eleVetoIdMap = cms.untracked.string('cutBasedElectronID-Fall17-94X-V2-veto'),
)


task.add(process.patAlgosToolsTask)
#maybe here?
#task.add(process.pileupJetId, process.patAlgosToolsTask)
#task.add(process.pileUpJetIDTask)

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

