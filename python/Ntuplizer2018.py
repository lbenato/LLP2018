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

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

## Messagge logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 500

## Input files
if len(options.inputFiles) == 0:

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #'/store/mc/RunIIAutumn18DRPremix/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/3017154C-F483-964E-855B-E06F2590FD6B.root'#2018 MC with muons!  #
            'file:/afs/desy.de/user/e/eichm/public/forLisa/VBFH_m20_ctau500.root'
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
    isPromptReco      = ('PromptReco' in process.source.fileNames[0])
    noLHEinfo         = True if ('WW_TuneCUETP8M1_13TeV-pythia8' or 'WZ_TuneCUETP8M1_13TeV-pythia8' or 'ZZ_TuneCUETP8M1_13TeV-pythia8') in process.source.fileNames[0] else False #check for PythiaLO samples
    isbbH             = True if ('bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo' in process.source.fileNames[0]) else False #bbH has a different label in LHEEventProduct
    isSignal          = True if ('HToSSTobbbb_MH-125' in process.source.fileNames[0]) else False
    isCalo            = True #HERE for calo analyses!!!

else:
    isData            = options.PisData
    isReHLT           = options.PisReHLT
    isReReco          = options.PisReReco
    isReMiniAod       = options.PisReMiniAod
    isPromptReco      = options.PisPromptReco
    noLHEinfo         = options.PnoLHEinfo
    isbbH             = options.PisbbH
    isSignal          = options.PisSignal
    isCalo            = options.Pcalo

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
    vertexCollection = cms.InputTag('offlinePrimaryVertices'),
    minimumNDOF = cms.uint32(4),
    maxAbsZ = cms.double(24),
    maxd0 = cms.double(2)
)
task.add(process.primaryVertexFilter)

#-----------------------#
#  E-MU-GAMMA MODULES   #
#-----------------------#

#later...

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
    lheProduct = cms.InputTag('externalLHEProducer' if not isbbH else 'source'),
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

jets_after_btag_tools = 'updatedPatJetsTransientCorrected'+postfix
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


process.seq = cms.Sequence(
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
    process.counter# *
    #process.ntuple
)

process.p = cms.Path(process.seq)
process.p.associate(task)

outFile = open("tmpConfig_Ntuplizer2018.py","w")
outFile.write(process.dumpPython())
outFile.close()

