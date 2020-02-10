#! /usr/bin/env python

import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors, TSpline, TSpline3, TMultiGraph
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox, TGaxis
import numpy as np


LOCAL = False

if LOCAL:
    from samples import sample, samples
else:
    from Analyzer.LLP2018.samples import sample, samples
########## SETTINGS ##########

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
#parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-d", "--dataera", action="store", type="string", dest="dataera", default="2016")
parser.add_option("-m", "--mode", action="store", type="string", dest="mode", default="ggH")
#parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
#parser.add_option("-r", "--region", action="store", type="string", dest="region", default="")
parser.add_option("-f", "--fiducial", action="store_true", default=False, dest="fiducial")
parser.add_option("-e", "--efficiency", action="store_true", default=True, dest="efficiency")
parser.add_option("-t", "--top", action="store_true", default=False, dest="top")
parser.add_option("-T", "--times", action="store_true", default=False, dest="times")

parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
#parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
#parser.add_option("-f", "--final", action="store_true", default=False, dest="final")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)

########## SETTINGS ##########

gStyle.SetOptStat(0)

#LUMI        = 36814 # in pb-1
SIGNAL      = 1.
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
BLIND       = False
POISSON     = False
jobs        = []

FIDUCIAL_ONLY = options.fiducial
TRIGGER_TOP_FIDUCIAL = options.top
EFFICIENCY = options.efficiency
TRIGGER_TIMES_FIDUCIAL = options.times

verbose = False

if EFFICIENCY and FIDUCIAL_ONLY and TRIGGER_TOP_FIDUCIAL:
    print "WRONG SETTING, ABORTING"
    exit()
if EFFICIENCY and FIDUCIAL_ONLY:
    print "WRONG SETTING, ABORTING"
    exit()
if FIDUCIAL_ONLY and TRIGGER_TOP_FIDUCIAL:
    print "WRONG SETTING, ABORTING"
    exit()
if EFFICIENCY and TRIGGER_TOP_FIDUCIAL:
    print "WRONG SETTING, ABORTING"
    exit()
########## SAMPLES ##########


sign_ctau_VBFH = [
'VBFH_M15_ctau0','VBFH_M15_ctau0p05','VBFH_M15_ctau0p1','VBFH_M15_ctau1','VBFH_M15_ctau5','VBFH_M15_ctau10','VBFH_M15_ctau25','VBFH_M15_ctau50','VBFH_M15_ctau100','VBFH_M15_ctau500','VBFH_M15_ctau1000','VBFH_M15_ctau2000','VBFH_M15_ctau5000','VBFH_M15_ctau10000',
'VBFH_M20_ctau0','VBFH_M20_ctau0p05','VBFH_M20_ctau0p1','VBFH_M20_ctau1','VBFH_M20_ctau5','VBFH_M20_ctau10','VBFH_M20_ctau25','VBFH_M20_ctau50','VBFH_M20_ctau100','VBFH_M20_ctau500','VBFH_M20_ctau1000','VBFH_M20_ctau2000','VBFH_M20_ctau5000','VBFH_M20_ctau10000',
'VBFH_M25_ctau0','VBFH_M25_ctau0p05','VBFH_M25_ctau0p1','VBFH_M25_ctau1','VBFH_M25_ctau5','VBFH_M25_ctau10','VBFH_M25_ctau25','VBFH_M25_ctau50','VBFH_M25_ctau100','VBFH_M25_ctau500','VBFH_M25_ctau1000','VBFH_M25_ctau2000','VBFH_M25_ctau5000','VBFH_M25_ctau10000',
'VBFH_M30_ctau0','VBFH_M30_ctau0p05','VBFH_M30_ctau0p1','VBFH_M30_ctau1','VBFH_M30_ctau5','VBFH_M30_ctau10','VBFH_M30_ctau25','VBFH_M30_ctau50','VBFH_M30_ctau100','VBFH_M30_ctau500','VBFH_M30_ctau1000','VBFH_M30_ctau2000','VBFH_M30_ctau5000','VBFH_M30_ctau10000',
'VBFH_M35_ctau0',
'VBFH_M35_ctau0p05',#
'VBFH_M35_ctau0p1','VBFH_M35_ctau1','VBFH_M35_ctau5','VBFH_M35_ctau10','VBFH_M35_ctau25','VBFH_M35_ctau50','VBFH_M35_ctau100','VBFH_M35_ctau500','VBFH_M35_ctau1000','VBFH_M35_ctau2000','VBFH_M35_ctau5000','VBFH_M35_ctau10000',
'VBFH_M40_ctau0','VBFH_M40_ctau0p05','VBFH_M40_ctau0p1','VBFH_M40_ctau1','VBFH_M40_ctau5','VBFH_M40_ctau10','VBFH_M40_ctau25','VBFH_M40_ctau50','VBFH_M40_ctau100','VBFH_M40_ctau500','VBFH_M40_ctau1000','VBFH_M40_ctau2000','VBFH_M40_ctau5000','VBFH_M40_ctau10000',
'VBFH_M45_ctau0','VBFH_M45_ctau0p05','VBFH_M45_ctau0p1','VBFH_M45_ctau1','VBFH_M45_ctau5','VBFH_M45_ctau10','VBFH_M45_ctau25','VBFH_M45_ctau50','VBFH_M45_ctau100','VBFH_M45_ctau500','VBFH_M45_ctau1000','VBFH_M45_ctau2000','VBFH_M45_ctau5000','VBFH_M45_ctau10000',
'VBFH_M50_ctau0','VBFH_M50_ctau0p05','VBFH_M50_ctau0p1','VBFH_M50_ctau1','VBFH_M50_ctau5','VBFH_M50_ctau10','VBFH_M50_ctau25','VBFH_M50_ctau50','VBFH_M50_ctau100','VBFH_M50_ctau500','VBFH_M50_ctau1000','VBFH_M50_ctau2000','VBFH_M50_ctau5000','VBFH_M50_ctau10000',
'VBFH_M55_ctau0','VBFH_M55_ctau0p05','VBFH_M55_ctau0p1','VBFH_M55_ctau1','VBFH_M55_ctau5','VBFH_M55_ctau10','VBFH_M55_ctau25','VBFH_M55_ctau50','VBFH_M55_ctau100','VBFH_M55_ctau500','VBFH_M55_ctau1000','VBFH_M55_ctau2000','VBFH_M55_ctau5000','VBFH_M55_ctau10000',
'VBFH_M60_ctau0','VBFH_M60_ctau0p05','VBFH_M60_ctau0p1','VBFH_M60_ctau1','VBFH_M60_ctau5','VBFH_M60_ctau10',
'VBFH_M60_ctau25',#
'VBFH_M60_ctau50','VBFH_M60_ctau100','VBFH_M60_ctau500','VBFH_M60_ctau1000','VBFH_M60_ctau2000','VBFH_M60_ctau5000','VBFH_M60_ctau10000',
]

sign_ctau_WminusH = [
'WminusH_M15_ctau0','WminusH_M15_ctau0p05','WminusH_M15_ctau1','WminusH_M15_ctau10','WminusH_M15_ctau100','WminusH_M15_ctau1000','WminusH_M15_ctau10000',
#'WminusH_M40_ctau0',
'WminusH_M40_ctau0p05',
'WminusH_M40_ctau1',
'WminusH_M40_ctau10','WminusH_M40_ctau100','WminusH_M40_ctau1000','WminusH_M40_ctau10000',
'WminusH_M55_ctau0','WminusH_M55_ctau0p05','WminusH_M55_ctau1','WminusH_M55_ctau10','WminusH_M55_ctau100','WminusH_M55_ctau1000','WminusH_M55_ctau10000',
]

sign_ctau_WplusH = [
'WplusH_M15_ctau0','WplusH_M15_ctau0p05','WplusH_M15_ctau1',
#'WplusH_M15_ctau10',
'WplusH_M15_ctau100', 'WplusH_M15_ctau1000',
#'WplusH_M15_ctau10000',
#'WplusH_M40_ctau0',
'WplusH_M40_ctau0p05',
'WplusH_M40_ctau1',
'WplusH_M40_ctau10','WplusH_M40_ctau100','WplusH_M40_ctau1000','WplusH_M40_ctau10000',
'WplusH_M55_ctau0','WplusH_M55_ctau0p05','WplusH_M55_ctau1','WplusH_M55_ctau10','WplusH_M55_ctau100','WplusH_M55_ctau1000','WplusH_M55_ctau10000',
]

sign_ctau_ZH = [
'ZH_M15_ctau0',
'ZH_M15_ctau0p05',
'ZH_M15_ctau1',
'ZH_M15_ctau10',
#missing#'ZH_M15_ctau100',
'ZH_M15_ctau1000',
'ZH_M15_ctau10000',
'ZH_M40_ctau0',
'ZH_M40_ctau0p05',
'ZH_M40_ctau1',
'ZH_M40_ctau10',
'ZH_M40_ctau100',#!#
'ZH_M40_ctau1000',
'ZH_M40_ctau10000',
'ZH_M55_ctau0',
'ZH_M55_ctau0p05',
'ZH_M55_ctau1',
'ZH_M55_ctau10',
'ZH_M55_ctau100',#!#
'ZH_M55_ctau1000',
'ZH_M55_ctau10000',
]


sign_ctau_ggH = ['ggH_M15_ctau500','ggH_M20_ctau0p1','ggH_M25_ctau25','ggH_M25_ctau5000','ggH_M30_ctau0p05','ggH_M30_ctau5000','ggH_M30_ctau10000']

sign_ctau_ggH = ['ggH_MH1000_M450_ctau1000','ggH_MH1000_M450_ctau10000']

back = ['QCD_HT50to100', 'QCD_HT100to200', 'QCD_HT200to300']

colors = [4, 410, 856, 2, 634, 1, 881, 798, 602, 921, 801, 3, 5, 6, ]
########## ######## ##########
gROOT.SetBatch(True)

NTUPLEDR = ""
sign_ctau = ""
if options.mode=="VBFH":
    sign_ctau = sign_ctau_VBFH
    NTUPLEDIR   = "/nfs/dust/cms/user/lbenato/RecoStudies_ntuples_v8/"#"/nfs/dust/cms/user/lbenato/VBF_and_trigger_ntuples_pt20/"#
    plot_label = "VBFH"
#elif options.mode=="WplusH":
#    sign_ctau = sign_ctau_WplusH
#elif options.mode=="WminusH":
#    sign_ctau = sign_ctau_WminusH
#elif options.mode=="ggZH":
#    sign_ctau = sign_ctau_ggZH
#elif options.mode=="ZH":
#    sign_ctau = sign_ctau_ZH
elif options.mode=="QCD":
    sign_ctau = back
    plot_label = "QCD"
    NTUPLEDIR   = "/nfs/dust/cms/user/lbenato/VBF_and_trigger_ntuples_pt20/"
elif options.mode=="ggH":
    sign_ctau = sign_ctau_ggH
    NTUPLEDIR   = "/nfs/dust/cms/user/eichm/v5/"
    NTUPLEDIR   = ""
    plot_label = "ggH"

#BASECUT = "GenBquark1.pt > 15 && GenBquark2.pt >15 && GenBquark3.pt > 15 && GenBquark4.pt > 15 && fabs(GenBquark1.eta) < 2.4 &&  fabs(GenBquark2.eta) < 2.4  && fabs(GenBquark3.eta) < 2.4 && fabs(GenBquark4.eta) < 2.4 "
#OLDBASECUT = "GenBquark1.pt > 10 && GenBquark2.pt >10 && GenBquark3.pt > 10 && GenBquark4.pt > 10 && fabs(GenBquark1.eta) < 2.5 &&  fabs(GenBquark2.eta) < 2.5  && fabs(GenBquark3.eta) < 2.5 && fabs(GenBquark4.eta) < 2.5 "
#BASECUT = "fabs(GenBquark1.eta) < 2.5 &&  fabs(GenBquark2.eta) < 2.5  && fabs(GenBquark3.eta) < 2.5 && fabs(GenBquark4.eta) < 2.5 "
#BASECUT = "GenBquark1.pt > 10 && GenBquark2.pt >10 && GenBquark3.pt > 10 && GenBquark4.pt > 10 "
#BASECUT = "GenBquark2.pt > 10 "
#BASECUT = "isVBF"
BASECUT = "isMC"

VBFXSEC = 3.782
WHXSEC = 1.373
ZHXSEC = 0.8839
ggZHXSEC = 48.58
WpluslnuHXSEC = 5.893e-02
WminuslnuHXSEC = 9.426e-02
ZllHXSEC = 2.982e-02

LUMI2016 = 35.9 * 1000  #in pb-1
LUMI2017 = 41.3 * 1000 #in pb-1


if options.dataera == "2016":
    LUMI = LUMI2016
elif options.dataera == "2017":
    LUMI = LUMI2017
else:
    LUMI = 0.
#######################################################
#
#
if EFFICIENCY:
    print "Calculating only efficiency alone!"
elif TRIGGER_TIMES_FIDUCIAL:
    print "Calculating trigger efficiency times fiducial cut efficiency!"
elif FIDUCIAL_ONLY:
    print "Calculating fiducial cut efficiency!"
elif TRIGGER_TOP_FIDUCIAL:
    print "Calculating trigger efficiency on top of fiducial cut efficiency!"
else:
    print "Calculating event rate considering trigger efficiency times fiducial cut efficiency!"

########################################################
#
#  2D mass vs ctau
#
########################################################

def eff_2D(cutlist, labellist=[], zmax=30, pal=109):
    print "Ntuples:\n"
    print NTUPLEDIR

    basecut = BASECUT
    if not EFFICIENCY:
        print "basecut considered: ", basecut
    signame = ""
    ncuts = len(cutlist)
    if labellist == []:
        labellist=cutlist
        gStyle.SetPalette(87)#87:light temperature #104 temperature map #69:beach(!) #70:black body #86:lake #109:cool(!)
    else:
        gStyle.SetPalette(pal)#87:light temperature #104 temperature map #69:beach(!) #70:black body #86:lake #109:cool(!)

    file = {}
    nevt = {}
    tree = {}
    effs = {}
    eff_dict = { k:{} for k in cutlist}
    #print eff_dict
    sign = sign_ctau
    XSEC = 0

    for i, s in enumerate(sign):
        if 'WplusH' in samples[s]['files'][0]:
            signame = "WplusH"
            XSEC = WpluslnuHXSEC
        elif 'WminusH' in samples[s]['files'][0]:
            signame = "WminusH"
            XSEC = WminuslnuHXSEC
        elif 'ZH' in samples[s]['files'][0] and not 'ggZH' in samples[s]['files'][0]:
            signame = "ZH"
            XSEC = ZllHXSEC
        elif 'ggZH' in samples[s]['files'][0]:
            signame = "ggZH"
            XSEC = ggZHXSEC
        elif 'VBF' in samples[s]['files'][0]:
            signame = "VBFH"
            XSEC = VBFXSEC
        elif 'QCD' in samples[s]['files'][0]:
            signame = "QCD"
            XSEC = samples[s]['xsec']
            #print s, samples[s]['xsec']
        elif 'GluGlu' in samples[s]['files'][0]:
            signame = "ggH"
            XSEC = 1.
            #print s, samples[s]['xsec']
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile

        if EFFICIENCY or FIDUCIAL_ONLY or TRIGGER_TOP_FIDUCIAL or TRIGGER_TIMES_FIDUCIAL:
            XSEC = 100./LUMI
        #print file[s]
        ##nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        #tree[s] = file[s].Get("reconstruction/tree") # Read TTree
        #nevt[s] = file[s].Get("reconstruction/tree").GetEntriesFast()
        tree[s] = file[s].Get("ntuple/tree") # Read TTree
        nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        if verbose:
            print "nevt: ", tree[s].GetEntries()
            print "nevt after basecut: ", tree[s].GetEntries(basecut)
        effs[s] = [0]*(ncuts+1)
        for j, c in enumerate(cutlist):
            br = 1.
            if FIDUCIAL_ONLY:
                tot_gen = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
                n = tree[s].GetEntries(basecut)
                if verbose:
                    print "den: ", tot_gen
                    print "num: ", n
            elif TRIGGER_TOP_FIDUCIAL: 
                tot_gen = tree[s].GetEntries(basecut)
                n = tree[s].GetEntries("(" + cutlist[j] + ")" + " && " + basecut)
                if verbose:
                    print "den: ", tree[s].GetEntries(basecut)
                    print "evt passing trigger: ", tree[s].GetEntries(cutlist[j])
                    print "num: ", tree[s].GetEntries("(" + cutlist[j] + ")" + " && " + basecut)
            elif TRIGGER_TIMES_FIDUCIAL:
                tot_gen = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
                n = tree[s].GetEntries("(" + cutlist[j] + ")" + " && " + basecut)
                if verbose:
                    print "den: ", tot_gen
                    print "num: ", n
            elif EFFICIENCY:
                tot_gen = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
                n = tree[s].GetEntries("(" + cutlist[j] + ")")
                if verbose:
                    print "den: ", tot_gen
                    print "num: ", n
            else:
                tot_gen = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
                n = tree[s].GetEntries("(" + cutlist[j] + ")" + " && " + basecut)
                if verbose:
                    print "den: ", tot_gen
                    print "num: ", n
            #exit()
            #d = tree[s].GetEntries(basecut)#nevt[s]#d = sample[samples[s]['files'][0]]['nevents']#
            effs[s][j] = (float(n)/(tot_gen)) * XSEC * LUMI
            eff_dict[c][s] = {'mass' : samples[s]['mass'], 'ctau' : samples[s]['ctau'], 'eff' :effs[s][j]}
            ###########
    x_array = [50000]
    y_array = [10]
    if options.mode == "QCD":
        y_array=[300]
    for j, c in enumerate(cutlist):
        for i, s in enumerate(sign):
            x_val = (samples[s]['ctau'])
            y_val = float(samples[s]['mass'])
            if x_val not in x_array: x_array.append(x_val)
            if y_val not in y_array: y_array.append(y_val)
        #if 35 not in y_array:
        #    print "FIXME! Just because we have few mass points!!!"
        #    y_array.append(35)

        #print x_array
        np_x_array = np.array(x_array)
        np_y_array = np.array(y_array)
        np_x_array.sort()
        np_y_array.sort()
        if options.mode == "VBFH":
            h = TH2F("try", labellist[j], len(np_x_array)-1,np_x_array, len(np_y_array)-1,np_y_array+2.5)
        elif options.mode == "ggH":
            h = TH2F("try", labellist[j], len(np_x_array)-1,np_x_array, len(np_y_array)-1,np_y_array+2.5)
        else:
            h = TH2F("try", labellist[j], len(np_x_array)-1,np_x_array, len(np_y_array)-1,np_y_array)
        for b in np_y_array:#[1:]:
            for a in np_x_array:
                #print "ctau looping on: ", a
                #print "mass looping on: ", b
                #print "bin with those ctau and mass: ", h.FindBin(a,b)
                la=str(a)
                lb=str(int(b))
                if signame=="VBFH":
                    if la== "0.001":
                        st = signame+"_M"+str(lb)+"_ctau0"
                    elif la=="0.05" or la=="0.1":
                        st = signame+"_M"+str(lb)+"_ctau"+str(la.replace("0.","0p"))
                    else:
                        st = signame+"_M"+str(lb)+"_ctau"+str(int(a))
                elif signame=="ggH":
                    if la== "0.001":
                        st = signame+"_M"+str(lb)+"_ctau0"
                    elif la=="0.05" or la=="0.1":
                        st = signame+"_M"+str(lb)+"_ctau"+str(la.replace("0.","0p"))
                    else:
                        st = signame+"_M"+str(lb)+"_ctau"+str(int(a))
                elif signame=="QCD":
                    if b==50:
                        st = "QCD_HT50to100"
                    elif b==100:
                        st = "QCD_HT100to200"
                    elif b==200:
                        st = "QCD_HT200to300"
                if st in eff_dict[c].keys():
                    h.SetBinContent(h.FindBin(a,b),float("{0:.4f}".format(eff_dict[c][st]['eff'])))
                    if eff_dict[c][st]['eff'] == 0:
                        h.SetBinContent(h.FindBin(a,b),float("{0:.4f}".format(0.0001)))
                else:
                    h.SetBinContent(h.FindBin(a,b),float(0.))
                h.GetXaxis().SetTitle("c #tau (mm)")
                h.GetYaxis().SetTitle("m_{#pi} (GeV)")
                h.GetXaxis().SetTitleSize(0.045)
                h.GetYaxis().SetTitleSize(0.045)
                if not options.mode=="QCD":
                    h.GetYaxis().SetNdivisions(len(np_y_array));
                if options.mode=="QCD":
                    h.GetXaxis().SetTitle("")
                    h.GetYaxis().SetTitle("H_{T} (GeV)")
                    h.GetXaxis().SetTitleSize(0)
                    h.GetXaxis().SetLabelSize(0)
                    h.GetYaxis().SetRangeUser(50,300)

        c1 = TCanvas("c1", "Signals", 1200, 600)
        if not options.mode=="QCD":
            c1.SetLogx()
        c1.cd()
        #c1.GetPad(0).SetTopMargin(0.06)
        #c1.GetPad(0).SetRightMargin(0.05)
        c1.GetPad(0).SetTicks(1, 1)
        ###TGaxis.SetMaxDigits(2)
        h.SetMarkerColor(10)
        if EFFICIENCY or TRIGGER_TIMES_FIDUCIAL:
            h.GetZaxis().SetRangeUser(0., 32)
            h.SetMarkerSize(1.7)
        elif FIDUCIAL_ONLY:
            h.GetZaxis().SetRangeUser(0., 60)
            h.SetMarkerSize(1.7)
        elif TRIGGER_TOP_FIDUCIAL:
            h.GetZaxis().SetRangeUser(0., 70)
            h.SetMarkerSize(1.7)
        else:
            h.GetZaxis().SetRangeUser(0., zmax)
            h.SetMarkerSize(1.35)
            #RATE: max 16500
        #print h.GetZaxis().GetLabelOffset()
        #print h.GetZaxis().GetLabelSize()
        #print h.GetZaxis().SetLabelOffset(1)
        if EFFICIENCY or FIDUCIAL_ONLY or TRIGGER_TOP_FIDUCIAL or TRIGGER_TIMES_FIDUCIAL:
            gStyle.SetPaintTextFormat(".1f")#(".1e")
            if options.mode == "QCD":
                gStyle.SetPaintTextFormat(".3f")#(".1e")
        else:
            gStyle.SetPaintTextFormat(".0f")
        stri = h.GetTitle()
        if EFFICIENCY:
            h.SetTitle(signame+" trigger efficiency in " +options.dataera+ ": "+stri)
        elif TRIGGER_TIMES_FIDUCIAL:
            h.SetTitle(signame+" trigger efficiency times fiducial cut efficiency in " +options.dataera+ ": "+stri)
        elif FIDUCIAL_ONLY:
            h.SetTitle(signame+" fiducial cut efficiency in " +options.dataera+ ": "+stri)
        elif TRIGGER_TOP_FIDUCIAL:
            h.SetTitle(signame+" trigger efficiency on top of fiducial cut efficiency in " +options.dataera+ ": "+stri)
        else:
            h.SetTitle(signame+" number of events in " +options.dataera+ ": "+stri)
        h.Draw("COLZTEXT")
        if EFFICIENCY:
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/EffStandalone_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.pdf")
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/EffStandalone_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.png")
        elif TRIGGER_TIMES_FIDUCIAL:
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/Eff_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.pdf")
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/Eff_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.png")
        elif FIDUCIAL_ONLY:
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/FiducialEff_2D_"+options.dataera+"_"+plot_label+"_v5.pdf")
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/FiducialEff_2D_"+options.dataera+"_"+plot_label+"_v5.png")
        elif TRIGGER_TOP_FIDUCIAL:
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/TriggerTopFiducialEff_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.pdf")
            c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/TriggerTopFiducialEff_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.png")
        else:
            if BASECUT == "isMC":
                c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/RateNoFiducial_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.pdf")
                c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/RateNoFiducial_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.png")
            else:
                if "isVBF" in BASECUT:
                    c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/RateVBF_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.pdf")
                    c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/RateVBF_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.png")
                else:
                    c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/Rate_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.pdf")
                    c1.Print("$CMSSW_BASE/src/Analyzer/LLP/macro/Efficiency/Rate_2D_"+options.dataera+"_"+str(labellist[j])+"_"+plot_label+"_v5.png")
        c1.Close()
        h.Clear()

########################################################
if not FIDUCIAL_ONLY:
#GOOD!
    eff_2D(
    ["HLT_Ele27_WPTight_Gsf_v || HLT_Ele25_eta2p1_WPTight_Gsf_v || HLT_Ele27_eta2p1_WPTight_Gsf_v || HLT_Ele32_eta2p1_WPTight_Gsf_v || HLT_Ele27_WPLoose_Gsf_WHbbBoost_v || HLT_Ele115_CaloIdVT_GsfTrkIdT_v || HLT_IsoMu24_v || HLT_IsoMu22_eta2p1_v || HLT_IsoTkMu24_v || HLT_IsoMu27_v || HLT_IsoTkMu22_eta2p1_v || HLT_IsoTkMu27_v || HLT_Mu50_v || HLT_TkMu50_v || HLT_Mu55_v || HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v || HLT_Mu6_PFHT200_PFMET100_v || HLT_Mu15_IsoVVVL_PFHT400_v || HLT_Ele15_IsoVVVL_PFHT400_v || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v || HLT_Mu50_IsoVVVL_PFHT400_v || HLT_Ele50_IsoVVVL_PFHT400_v || HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v || HLT_Mu30_eta2p1_PFJet150_PFJet50_v || HLT_DoubleMu3_PFMET50_v || HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v || HLT_Ele15_IsoVVVL_PFHT400_PFMET50_v || HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v || HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v || HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v || HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v || HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v || HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v || HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v || HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v || HLT_Ele27_WPTight_Gsf_L1JetTauSeeded_v || HLT_VLooseIsoPFTau140_Trk50_eta2p1_v || HLT_Mu30_TkMu11_v || HLT_Mu17_Mu8_SameSign_DZ_v || HLT_Mu40_TkMu11_v || HLT_Mu20_Mu10_SameSign_DZ_v || HLT_DoubleMu8_Mass8_PFHT300_v || HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v || HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v || HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v || HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v || HLT_AK8PFJet360_TrimMass30_v || HLT_AK8PFJet450_v || HLT_AK8PFJet500_v || HLT_BTagMu_AK8Jet300_Mu5_v || HLT_BTagMu_Jet300_Mu5_v || HLT_CaloJet500_NoJetID_v || HLT_DiCentralPFJet170_CFMax0p1_v || HLT_DiCentralPFJet330_CFMax0p5_v || HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v || HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v || HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v || HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v || HLT_DoubleMu3_PFMET50_v || HLT_DoubleMu8_Mass8_PFHT300_v || HLT_Ele115_CaloIdVT_GsfTrkIdT_v || HLT_Ele15_IsoVVVL_PFHT400_v || HLT_HT350_DisplacedDijet40_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v || HLT_HT650_DisplacedDijet80_Inclusive_v || HLT_HT650_v || HLT_HT750_DisplacedDijet80_Inclusive_v || HLT_LooseIsoPFTau50_Trk30_eta2p1_MET110_v || HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v || HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v || HLT_MET300_v || HLT_Mu10_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT350_PFMETNoMu60_v || HLT_Mu15_IsoVVVL_PFHT400_PFMET50_v || HLT_Mu15_IsoVVVL_PFHT400_v || HLT_Mu15_IsoVVVL_PFHT600_v || HLT_Mu17_Mu8_SameSign_DZ_v || HLT_Mu25_TkMu0_dEta18_Onia_v || HLT_Mu30_TkMu11_v || HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v || HLT_Mu40_eta2p1_PFJet200_PFJet50_v || HLT_Mu6_PFHT200_PFMET100_v || HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v || HLT_Mu8_TrkIsoVVL_DiPFJet40_DEta3p5_MJJ750_HTT300_PFMETNoMu60_v || HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v || HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v || HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v || HLT_PFHT450_SixJet40_BTagCSV_p056_v || HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v || HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v || HLT_PFHT900_v || HLT_PFJet450_v || HLT_PFJet500_v || HLT_PFMET400_v || HLT_PFMET500_v || HLT_PFMET600_v || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_QuadJet45_TripleBTagCSV_p087_v || HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v || HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v || HLT_Rsq0p25_v || HLT_Rsq0p30_v || HLT_RsqMR270_Rsq0p09_MR200_4jet_v || HLT_TkMu50_v || HLT_TrkMu17_DoubleTrkMu8NoFiltersNoVtx_v || HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v || HLT_VBF_DisplacedJet40_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v || HLT_VLooseIsoPFTau140_Trk50_eta2p1_v || HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v || HLT_PFMET110_PFMHT110_IDTight_v || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_PFMET120_PFMHT120_IDTight_v || HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v || HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_PFMET170_HBHECleaned_v || HLT_PFHT300_PFMET110_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v || HLT_MET200_v || HLT_RsqMR270_Rsq0p09_MR200_v || HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v || HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v || HLT_MET250_v || HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v  || HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v || HLT_PFMET300_v || HLT_MET75_IsoTrk50_v || HLT_MET90_IsoTrk50_v",
     ],
    ['chosen_OR',
     ],
    11000,
    55
    )

else:
    eff_2D(
    ["",
     ],
    ['',
     ],
    100,
    55
    )

