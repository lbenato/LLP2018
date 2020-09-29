#! /usr/bin/env python

import os, multiprocessing
import copy
import math
import numpy as np
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors, TF1
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox

from Analyzer.LLP.samples import sample, samples
from Analyzer.LLP.variables import *
from Analyzer.LLP.selections import *
from Analyzer.LLP.drawUtils import *
from collections import defaultdict

########## SETTINGS ##########

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="met_pt_nomu")#"nPV")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="met_test")
parser.add_option("-C", "--compare", action="store", type="string", dest="compare", default="")
parser.add_option("-D", "--drawsignal", action="store_true", dest="drawsignal", default=False)
parser.add_option("-n", "--normalized", action="store_true", dest="normalized", default=False)
parser.add_option("-d", "--dataset", action="store", type="string", dest="dataset", default="mu")#"mu3nPV"
parser.add_option("-r", "--run", action="store", type="string", dest="run", default="G")
parser.add_option("-e", "--efficiency", action="store_true", dest="efficiency", default=False)
parser.add_option("-s", "--sample", action="store", type="string", dest="sample", default="All")
parser.add_option("-g", "--goodplots", action="store_true", default=False, dest="goodplots")#not needed in 2016
parser.add_option("-a", "--all", action="store_true", default=False, dest="all")
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
parser.add_option("-f", "--final", action="store_true", default=False, dest="final")
parser.add_option("-R", "--rebin", action="store_true", default=False, dest="rebin")
parser.add_option("-p", "--public", action="store_true", default=False, dest="public")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

########## SETTINGS ##########

gStyle.SetOptStat(0)

NTUPLEDIR          = "/nfs/dust/cms/group/cms-llp/v8_TripleJet50_trigger/"
REBIN              = options.rebin
NICE               = False
SAVE               = True
LUMIGmu            = 7543.233758#v8_TripleJet50_trigger
LUMICmu            = 0.


##HLT paths

PROBE = "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v"
##L1 paths
PROBEL1 = ""#"hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300"
PS_probe = ""

COMPARE = options.compare
DRAWSIGNAL = options.drawsignal

########## SAMPLES ##########

colors = [856, 1,  634, 420, 806, 882, 401, 418, 881, 798, 602, 921]
markers = [20,21]#[24,25,21,20]
########## ######## ##########

#gROOT.SetBatch(True)

sign_sampl = {}
sign_sampl_mu = {
    'test' : {
        'order' : 5,
        'files' : ['output'],
        'howmany' : "RunA",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "SingleMu",
        'nice_label' : "Single Muon RunA",
        'weight': 1.,
        'plot': True,
    },
    'SingleMuRunC' : {
        'order' : 5,
        'files' : ['SingleMuonRun2016C-03Feb2017-v1',],#'SingleMuon_Run2018C-PromptReco-v2','SingleMuon_Run2018C-PromptReco-v3'],
        'howmany' : "RunC",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "SingleMu",
        'nice_label' : "Single Muon RunC",
        'weight': 1.,
        'plot': True,
    },
    'SingleMuRunG' : {
        'order' : 5,
        'files' : ['SingleMuonRun2016G-03Feb2017-v1'],#['SingleMuon_test_PS'],#
        'howmany' : "RunG",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "SingleMu",
        'nice_label' : "Single Muon RunG",
        'weight': 1.,
        'plot': True,
    },
}

sign_sampl_mc = {
    'VBFH_M35_ctau0p05' : {
        'order' : 5,
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-35_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "VBFH_M35_ctau0p05",
        'nice_label' : "VBFH_M35_ctau0p05",
        'weight': 1.,
        'plot': True,
    },
    'TTbar' : {
        'order' : 5,
        'files' : ['TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "TTbar",
        'nice_label' : "TTbar",
        'weight': 1.,
        'plot': True,
    },
    'WJetsToLNu' : {
        'order' : 5,
        'files' : ['WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "WJetsToLNu",
        'nice_label' : "WJetsToLNu",
        'weight': 1.,
        'plot': True,
    },

    'DYJetsToLL' : {
        'order' : 5,
        'files' : ['DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "DYJetsToLL",
        'nice_label' : "DYJetsToLL",
        'weight': 1.,
        'plot': True,
    },

    'QCD' : {
        'order' : 5,
        'files' : ['QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "QCD",
        'nice_label' : "QCD",
        'weight': 1.,
        'plot': True,
    },


    'QCD_TT_WJets' : {
        'order' : 5,
        'files' : ['QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-v1','WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "QCD_TT_Wjets",
        'nice_label' : "QCD_TT_Wjets",
        'weight': 1.,
        'plot': True,
    },

    'QCD_TT_WJets_DY' : {
        'order' : 5,
        'files' : ['QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-v1','WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "QCD_TT_DY_Wjets",
        'nice_label' : "QCD_TT_DY_Wjets",
        'weight': 1.,
        'plot': True,
    },

    'DY_WJets' : {
        'order' : 5,
        'files' : ['WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2-v1'],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "DY_Wjets",
        'nice_label' : "DY_Wjets",
        'weight': 1.,
        'plot': True,
    },

    'All' : {
        'order' : 5,
        'files' : ['QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-v1','WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1','DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2-v1','ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v1','ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v1','ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v1','ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v1','ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v1','DYJetsToNuNu_PtZ-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1','DYJetsToNuNu_PtZ-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1','DYJetsToNuNu_PtZ-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1','DYJetsToNuNu_PtZ-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1','DYJetsToNuNu_PtZ-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1','DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8-v1','WJetsToQQ_HT180_13TeV-madgraphMLM-pythia8-v1','WW_TuneCUETP8M1_13TeV-pythia8-v1','WZ_TuneCUETP8M1_13TeV-pythia8-v1','ZZ_TuneCUETP8M1_13TeV-pythia8-v1','VBFHToBB_M-125_13TeV_powheg_pythia8-v1','ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8-v1','WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v1','WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v1', 'GluGluHToBB_M125_13TeV_powheg_pythia8-v1',],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "AllBkg",
        'nice_label' : "AllBkg",
        'weight': 1.,
        'plot': True,
    },


    'signal' : {
        'order' : 5,
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            ],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "signal",
        'nice_label' : "signal m_{#pi} = 15, 20 GeV",
        'weight': 1.,
        'plot': True,
    },

    'signal15' : {
        'order' : 5,
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            ],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "signal15",
        'nice_label' : "signal15",
        'weight': 1.,
        'plot': True,
    },

    'signal20' : {
        'order' : 5,
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            'VBFH_HToSSTobbbb_MH-125_MS-20_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_Tranche2_PRIVATE-MC',
            ],
        'howmany' : "",
        'fillcolor' : 60,
        'fillstyle' : 1001,
        'linecolor' : 60,
        'linewidth' : 2,
        'linestyle' : 1,
        'marker' : 25,
        'label' : "signal20",
        'nice_label' : "signal20",
        'weight': 1.,
        'plot': True,
    },

}
chain = defaultdict(dict)
hist = defaultdict(dict)
eff = defaultdict(dict)
graph = defaultdict(dict)
graph_num = defaultdict(dict)
hist_num = defaultdict(dict)
hist_den = defaultdict(dict)
chain_num = defaultdict(dict)
chain_den = defaultdict(dict)
goodstring = ''
goodlabel = ''
var = "Lepton1.pt"

sample_list = []
signal_dict = {}
name_mc = name_data = ""


if COMPARE!="":
    sample_list.append(COMPARE)
    name_mc = COMPARE
    #sample_list.append("QCD")
    #sample_list.append("WJetsToLNu")
    #sample_list.append("signal")

if DRAWSIGNAL:
    #sample_list.append(COMPARE)
    #sample_list.append("QCD")
    #sample_list.append("WJetsToLNu")
    sample_list.append("signal")


s=''

if ("mu" in str(options.dataset)):
    sign_sampl = sign_sampl_mu
    if (options.run=="C"):
        s+="SingleMuRunC"
        sample_list.append("SingleMuRunC")
        LUMI = LUMICmu
        name_data = "SingleMuRunC"

    elif (options.run=="G"):
        s+="SingleMuRunG"
        sample_list.append("SingleMuRunG")
        LUMI = LUMIGmu
        name_data = "SingleMuRunG"

elif ("mc" in str(options.dataset)):
    sign_sampl = sign_sampl_mc
    s+= options.sample
    sample_list.append(options.sample)
    LUMI = 0.
    name_data = options.sample


if DRAWSIGNAL:
    sign_sampl['signal'] = sign_sampl_mc['signal']

if COMPARE!="":
    if COMPARE in sign_sampl_mc.keys():
        sign_sampl[COMPARE] = sign_sampl_mc[COMPARE]
    #sign_sampl['QCD'] = sign_sampl_mc['QCD']
    #sign_sampl['WJetsToLNu'] = sign_sampl_mc['WJetsToLNu']
    #sign_sampl['signal'] = sign_sampl_mc['signal']
    else:
        print "MC samples not listed, aborting. . . "
        exit()


#Trigger of interest: https://twiki.cern.ch/twiki/bin/view/CMS/HamburgWikiAnalysisLongLived#VBF_DisplacedJet_trigger_studies
#   * HLT_VBF_DisplacedJet40_VTightID_Hadronic_v L1 seed: hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300
#   * HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v  L1 seed: hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300
#
#   * HLT_IsoMu24_v L1 seed: hltL1sSingleMu22
#   * HLT_IsoMu27_v L1 seed: hltL1sV0SingleMu22IorSingleMu25
#   * HLT_Mu50_v L1 seed: hltL1sV0SingleMu22IorSingleMu25
#   * HLT_L1_TripleJet_VBF_v L1 seed: hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet
#   * HLT_QuadPFJet_VBF_v L1 seed: hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet
#   * HLT_DiPFJetAve40_v L1 seed: hltL1sZeroBias
#   * HLT_DiPFJetAve60_v L1 seed: hltL1sZeroBias
#   * HLT_DiPFJetAve80_v L1 seed: hltL1sSingleJet60
#   * HLT_PFJet40_v L1 seed: hltL1sZeroBias
#   * HLT_PFJet60_v L1 seed: hltL1sSingleJet35
#   * HLT_PFJet80_v L1 seed: hltL1sSingleJet60
#
# Signal paths for HIG-17-031:
#   * HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200_v: L1seed hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet
#   * HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v: L1seed hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet
#   * HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460_v: L1seed hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet
#   * HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v: L1seed hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet


#Studies in HIG-17-021 (VBF H>bb)
#all events are required to have four offline (pT ordered) jets with transverse momenta pT > 92, 76, 64, 30 GeV
#den: control HLT paths
#turn on curves vs jet pt and csv

#We can try first eff like HIG-17-031 paths over:
# HLT_L1_TripleJet_VBF_v
# HLT_QuadPFJet_VBF_v
# HLT_DiPFJetAve80_v
# HLT_PFJet60_v
# HLT_PFJet80_v
# num: HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v: L1seed hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet

#set of cuts:
bins_special = np.array([])
ref = probe = ""
maxeff = 1.
PROBE_label = ""
#name_mc = ""
#name_data = ""
ratio = 0 if COMPARE=="" else 4

###############
# Sequence of filters:

# L1
# hltTripleJet50
# hltDoubleJet65
# hltSingleJet80
# hltVBFFilterDisplacedJets
#

##############################################
if options.cut == "met_test":
    ref = "HLT_IsoMu24_v && nJets>=3 && isVBF"
    ref_signal = "nJets>=3 && isVBF"
    maxeff = 1.01
    probe = "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v" 
    PROBE_label = "PFMETNoMu120"
    cut_den = ref + " && nTightMuons==1  && " + selection["METfilters"]
    cut_den_signal = ref_signal + " && " + selection["METfilters"]
    cut_num = cut_den + " && " + probe
    cut_num_signal = cut_den_signal + " && " + probe

if options.cut == "met_test_sharper":
    ref = "HLT_IsoMu24_v && nJets>=3 && isVBF && Jets.Jets[0].pt>40 && Jets.Jets[1].pt>40 && Jets.Jets[2].pt>20"
    ref_signal = "nJets>=3 && isVBF && Jets.Jets[0].pt>40 && Jets.Jets[1].pt>40 && Jets.Jets[2].pt>20"
    maxeff = 1.01
    probe = "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v" 
    PROBE_label = "PFMETNoMu120"
    cut_den = ref + " && nTightMuons==1  && " + selection["METfilters"]
    cut_den_signal = ref_signal + " && " + selection["METfilters"]
    cut_num = cut_den + " && " + probe
    cut_num_signal = cut_den_signal + " && " + probe


##############################################

print "Ntuple dir: ", NTUPLEDIR
print "Samples considered: ", sample_list

print "Data: ", name_data
if COMPARE!="":
    print "MC to be compared: ", name_mc
###
#proper reweight

cut_den = "EventWeight * ( "+ cut_den  + " )"
cut_den_signal = "EventWeight * ( "+ cut_den_signal  + " )"
cut_num = "EventWeight * ( "+ cut_num  + " )"
cut_num_signal = "EventWeight * ( "+ cut_num_signal  + " )"

###
def compare_num_den(ratio=ratio):
###
    
    for i,a in enumerate(sample_list):
        print a

        chain[a] = TChain("trigger/tree")
        for j,ss in enumerate(sign_sampl[a]['files']):
            print "ss: ", ss
            chain[a].Add(NTUPLEDIR + ss + ".root")
        if variable[options.variable]['nbins']>0:
            hist[a] = TH1F(a, ";"+variable[options.variable]['title'], variable[options.variable]['nbins'], variable[options.variable]['min'], variable[options.variable]['max'])
            hist_num[a] = TH1F(a+"_num", ";"+variable[options.variable]['title'], variable[options.variable]['nbins'], variable[options.variable]['min'], variable[options.variable]['max'])
        hist_num[a].Sumw2()
        hist[a].Sumw2()

        print "variable: ", options.variable
        if "signal" in a:
            chain[a].Project(a, options.variable, cut_den_signal)           
            print "cut denominator signal: ", cut_den_signal
            print "cut numerator signal: ", cut_num_signal
        else:
            chain[a].Project(a, options.variable, cut_den)           
            print "cut denominator: ", cut_den
            print "cut numerator: ", cut_num


        hist[a].SetOption("%s" % chain[a].GetTree().GetEntriesFast())

        if "signal" in a:
            chain[a].Project(a+"_num", options.variable, cut_num_signal)
        else:
            chain[a].Project(a+"_num", options.variable, cut_num)
    
        hist_num[a].SetOption("%s" % chain[a].GetTree().GetEntriesFast())
    
    

        if options.variable == "nPV":
            bins = np.array([0.,10.,15.,20.,25.,30.,35.,40.,50.,70.])
        else:
            bins = np.array([0.,20.,40.,60.,80.,100.,120.,140.,160.,180.,200.,250.,300.,500.,1000.])
            if len(bins_special):
                bins=bins_special
    
        if REBIN:
            hist[a] = hist[a].Rebin(len(bins)-1,a+"_den2",bins)
            hist_num[a] = hist_num[a].Rebin(len(bins)-1,a+"_num2",bins)


    can = TCanvas("can","can", 1000, 800)#900 if ratio else 800)
    if COMPARE!="":
        can.Divide(1, 2)
        setTopPad(can.GetPad(1), ratio)
        setBotPad(can.GetPad(2), ratio)
        can.cd(1)
        can.cd(1).SetGrid()
    else:
        ratio = 0
        can.SetGrid()
        can.cd()

    if ratio:
        if probe!=PROBEL1:
            #leg = TLegend(0.12+0.3, 0.1, 0.68+0.2, 0.3)#0.45)
            leg = TLegend(0.12+0.3, 0.1, 0.68+0.25, 0.3+0.15)#0.45)#DCMS
        else:
            #leg = TLegend(0.12+0.3, 0.1, 0.68+0.2, 0.3)#0.45)
            leg = TLegend(0.12+0.3, 0.1, 0.68+0.5, 0.3+0.5)#0.45)
        leg.SetTextSize(0.032)
        leg.SetTextSize(0.045)#DCMS

    else:
        if probe!=PROBEL1:
            leg = TLegend(0.1, 0.75, 0.68, 0.88)#0.45)
        else:
            leg = TLegend(0.1, 0.12, 0.68, 0.25)#0.45)
        leg.SetTextSize(0.028)


    if "DPG" in options.cut:
        leg = TLegend(0.3, 0.12, 0.88, 0.35)

    if not options.efficiency:
        can.SetLogy()
        leg = TLegend(0.5, 0.65, 0.68, 0.9)#0.45)
        leg.SetTextSize(0.028)


    #leg.SetFillStyle(0)


    for i,s in enumerate(sample_list):
        if options.efficiency:
            graph[s] = TGraphAsymmErrors()
            graph[s].BayesDivide(hist_num[s],hist[s])
        else:
            if options.normalized:
                hist[s].Scale(1./hist[s].Integral())
                hist_num[s].Scale(1./hist_num[s].Integral())
            graph[s] = TGraphAsymmErrors(hist[s])
            graph_num[s] = TGraphAsymmErrors(hist_num[s])
        graph[s].SetMarkerSize(1.)
        graph[s].SetMarkerStyle(markers[i])#(sign_sampl[s]['marker'])
        graph[s].SetMarkerColor(colors[i])#(2)
        graph[s].SetFillColor(colors[i])#(2) 
        graph[s].SetLineColor(colors[i])#(2)
        graph[s].SetLineWidth(2)
        if options.efficiency:
            graph[s].GetYaxis().SetRangeUser(0.,maxeff)
            graph[s].GetYaxis().SetTitle("Efficiency")#("Efficiency (L1+HLT)")
            graph[s].GetYaxis().SetTitleOffset(0.9)#("Efficiency (L1+HLT)")
            graph[s].GetYaxis().SetTitleSize(0.05)#DCMS
        else:
            graph[s].SetMinimum(0.01)
            graph_num[s].SetMarkerSize(1.)
            graph_num[s].SetMarkerStyle(markers[i])#(sign_sampl[s]['marker'])
            graph_num[s].SetMarkerColor(colors[i+3])#(2)
            graph_num[s].SetFillColor(colors[i+3])#(2) 
            graph_num[s].SetLineColor(colors[i+3])#(2)
            graph_num[s].SetLineWidth(2)
            graph_num[s].SetLineStyle(2)
        graph[s].GetXaxis().SetRangeUser(variable[options.variable]['min'], variable[options.variable]['max'])
        graph[s].GetXaxis().SetTitle(variable[options.variable]['title'])
        graph[s].GetXaxis().SetTitleSize(0.04)#DCMS
        graph[s].GetXaxis().SetTitleOffset(1.1)
        #?#if COMPARE=="":
        #?#    graph[s].GetYaxis().SetTitleOffset(1.5)
        #?#else:
        #?#    graph[s].GetYaxis().SetTitleOffset(1)
        eff[s] = TH1F()
        eff[s].Sumw2()
        eff[s] = hist_num[s].Clone("eff_"+s)
        eff[s].Divide(eff[s],hist[s],1,1,"cl=0.683 b(1,1) mode")
        if i==0:
            graph[s].Draw("AP")
        else:
            graph[s].Draw("P,sames")
    
        if not options.efficiency:
            graph_num[s].Draw("P,sames")
            if PROBE_label!="":
                leg.SetHeader("#splitline{Ref: "+ref+"}{"+PROBE_label+"}")
            else:
                leg.SetHeader("#splitline{Ref: "+ref+"}{"+probe+"}")
            leg.AddEntry(graph[s], s+ ', den', 'PL' )
            leg.AddEntry(graph_num[s], s+ ', num', 'PL')
    
    
        if COMPARE!="" and options.efficiency:
            if PROBE_label!="":
                leg.SetHeader("#splitline{Ref: "+ref+"}{Probe: "+PROBE_label+"}")
            else:
                leg.SetHeader("#splitline{Ref: "+ref+"}{"+probe+"}")
            if s=="signal":
                leg.AddEntry(graph[s],"Signal, m_{#pi} = 15, 20 GeV",'PL')
            else:
                leg.AddEntry(graph[s],s,'PL')

        elif COMPARE=="" and options.efficiency:
            leg.SetHeader("Ref: "+ref)
            if PROBE_label=="":
                leg.AddEntry(graph[s], probe,'PL')
            else:
                leg.AddEntry(graph[s], PROBE_label,'PL')                
    
                    
    
        if "DPG" in options.cut:
            leg.Clear()
            leg.SetHeader("Den: #mu trigger & 1 offline #mu; num: L1 seed")
            #leg.AddEntry(graph[s],s,'PL')
            leg.SetTextSize(0.036)
    
            #new_file = TFile("macro/rootfiles/MET_trigger_eff_data_" + sign_sampl[s]['label'] + sign_sampl[s]['howmany'] + "_" + str(options.variable) + "_" +  options.dataset+ "_v5.root",'RECREATE')
            #graph[s].Write("graph_2018")
    



    if "DPG" in options.cut:
        leg.Clear()
        leg.SetHeader("Den: #mu trigger & 1 offline #mu; num: L1 seed")
        leg.AddEntry(graph[name_data],'Data','PL')
        leg.AddEntry(graph[name_mc],'MC backgrounds','PL')
        leg.SetTextSize(0.036)
    
    leg.SetBorderSize(0)
    leg.Draw()

    etichetta = TLatex()
    etichetta.SetNDC()
    etichetta.SetTextSize(0.04)
    etichetta.SetTextColor(1)
    if COMPARE=="":
        etichetta.DrawLatex(0.3, 0.4, sign_sampl[s]['nice_label'])

    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.047)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    latex.SetTextSize(0.051)#47
    if LUMI>0:
        if ratio:
            #latex.DrawLatex(0.9, 0.985, "%.1f fb^{-1}  (13 TeV, 2016)" % (float(LUMI/1000.)))
            latex.DrawLatex(0.9, 0.99, "%.1f fb^{-1}  (13 TeV, 2016)" % (float(LUMI/1000.)))#DCMS
        else:
            latex.DrawLatex(0.9, 0.96, "%.1f fb^{-1}  (13 TeV, 2016)" % (float(LUMI/1000.)))
    latex.SetTextFont(62)
    if ratio:
        latex.DrawLatex(0.20, 0.98, "CMS")
    else:
        latex.DrawLatex(0.20, 0.96, "CMS")
    latex.SetTextFont(52)
    if "DPG" in options.cut:
        if ratio:
            latex.DrawLatex(0.46, 0.98, "Work in Progress")
        else:
            latex.DrawLatex(0.46, 0.96, "Work in Progress")
    else:
        if ratio:
            if "SingleMu" in name_data:
                latex.DrawLatex(0.36, 0.98, "Preliminary")
            else:
                latex.DrawLatex(0.36, 0.98, "Simulation")
        else:
            if "SingleMu" in name_data:
                latex.DrawLatex(0.36, 0.96, "Preliminary")
            else:
                latex.DrawLatex(0.36, 0.96, "Simulation")

    can.Update()


    if COMPARE and name_mc!="" and name_data!="":
        can.cd(2)
        can.cd(2).SetGrid()
        err = eff[name_mc].Clone("EffErr;")
        err.SetTitle("")
        err.GetYaxis().SetTitle("Data / MC")
        err.GetYaxis().SetTitleOffset(0.9)
        err.GetYaxis().SetTitleSize(0.05)#DCMS
        err.GetXaxis().SetTitleSize(0.05)#DCMS
        for a in range(1, err.GetNbinsX()+1):
            err.SetBinContent(a, 1)
            if eff[name_mc].GetBinContent(a) > 0:
                err.SetBinError(a, eff[name_mc].GetBinError(a))#?#/eff[name_mc].GetBinContent(a))
        setBotStyle(err,miny=0.5,maxy=1.5)
        errLine = err.Clone("errLine")
        errLine.SetLineWidth(2)
        errLine.SetFillStyle(0)
        errLine.SetLineColor(2)#L#
        errLine.SetLineStyle(2)#L#
        err.Draw("E2")
        errLine.Draw("SAME, HIST")
        res = eff[name_data].Clone("Residues")
        for a in range(0, res.GetNbinsX()+1):
            if eff[name_mc].GetBinContent(a) > 0: 
                res.SetBinContent(a, res.GetBinContent(a)/eff[name_mc].GetBinContent(a))
                res.SetBinError(a, res.GetBinError(a)/eff[name_mc].GetBinContent(a))
        setBotStyle(res,miny=0.,maxy=2.)
        res.SetMarkerStyle(21)
        res.SetMarkerColor(1)
        res.SetLineColor(1)
        res.SetLineWidth(1)
        res.Draw("SAME, PE0")
    can.Update()

    outpath = ""
    outpath += "/afs/desy.de/user/l/lbenato/LLP_code/CMSSW_8_0_26_patch1/src/Analyzer/LLP/macro/TriggerTurnOn/"

    if not options.efficiency:
        outpath+= "Distributions/"

    if options.goodplots:
        outpath = "/afs/desy.de/user/l/lbenato/LLP_code/CMSSW_8_0_26_patch1/src/Analyzer/LLP/macro/TriggerTurnOn/good_plots/"


    if COMPARE!="":
        compare_string = "_vs_"+COMPARE+"_"
    else:
        compare_string= ""

    if options.normalized:
        norm_label= "_norm"
    else:
        norm_label = ""

    if SAVE:
        if PROBE_label =="":
            can.Print(outpath + "TriggerTurnOn_" + sign_sampl[s]['label'] + sign_sampl[s]['howmany'] + compare_string + "_" + str((options.variable).replace('.','_')) + "_" + str(probe) + "_" + str(options.cut) + "_" + options.dataset + goodstring+norm_label+"_v8trigger_DCMS.png")
            can.Print(outpath + "TriggerTurnOn_" + sign_sampl[s]['label'] + sign_sampl[s]['howmany'] + compare_string + "_" + str((options.variable).replace('.','_')) + "_" + str(probe) + "_" + str(options.cut)  +  "_" + options.dataset + goodstring+norm_label+"_v8trigger_DCMS.pdf")

        else:
            can.Print(outpath + "TriggerTurnOn_" + sign_sampl[s]['label'] + sign_sampl[s]['howmany'] + compare_string + "_" + str((options.variable).replace('.','_')) + "_" + PROBE_label + "_" + str(options.cut) + "_" + options.dataset + goodstring+norm_label+"_v8trigger_DCMS.png")
            can.Print(outpath + "TriggerTurnOn_" + sign_sampl[s]['label'] + sign_sampl[s]['howmany'] + compare_string + "_" + str((options.variable).replace('.','_')) + "_" + PROBE_label + "_" + str(options.cut)  +  "_" + options.dataset + goodstring+norm_label+"_v8trigger_DCMS.pdf")    


    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")









compare_num_den()

exit()

