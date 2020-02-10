#! /usr/bin/env python

import os, multiprocessing
import copy
import math
import numpy as np
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TMultiGraph, TGraphAsymmErrors, TSpline, TSpline3
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox


#from Analyzer.LLP2018.samples_v3 import sample, samples
from Analyzer.LLP2018.samples import sample, samples
from Analyzer.LLP2018.selections import selection
from Analyzer.LLP2018.variables import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v1_gen_production_calo/"
#sign = ['VBFH_M30_ctau100','VBFH_M30_ctau1000','VBFH_M30_ctau10000']
NTUPLEDIR = ""

def plot_2D(sign,var,nbins=50,minimum=0,maximum=2000,filename="",string=""):
    chain = {}
    hist = {}
    r_ecal = 129
    r_hcal = 179
    r_magnet = 295
    r_mb1 = 402

    z_ecal = 300
    z_hcal = 376
    z_magnet = 0
    z_mb1 = 560

    if var=="radius2D":
        v_ecal = TLine(r_ecal,minimum,r_ecal,maximum)
        v_hcal = TLine(r_hcal,minimum,r_hcal,maximum)
        v_magnet = TLine(r_magnet,minimum,r_magnet,maximum)
        v_mb1 = TLine(r_mb1,minimum,r_mb1,maximum)
        h_ecal = TLine(minimum,r_ecal,maximum,r_ecal)
        h_hcal = TLine(minimum,r_hcal,maximum,r_hcal)
        h_magnet = TLine(minimum,r_magnet,maximum,r_magnet)
        h_mb1 = TLine(minimum,r_mb1,maximum,r_mb1)
    elif var=="z":
        v_ecal = TLine(z_ecal,minimum,z_ecal,maximum)
        v_hcal = TLine(z_hcal,minimum,z_hcal,maximum)
        v_magnet = TLine(z_magnet,minimum,z_magnet,maximum)
        v_mb1 = TLine(z_mb1,minimum,z_mb1,maximum)
        h_ecal = TLine(minimum,z_ecal,maximum,z_ecal)
        h_hcal = TLine(minimum,z_hcal,maximum,z_hcal)
        h_magnet = TLine(minimum,z_magnet,maximum,z_magnet)
        h_mb1 = TLine(minimum,z_mb1,maximum,z_mb1)
    else:
        v_ecal = TLine(r_ecal,minimum,r_ecal,maximum)
        v_hcal = TLine(r_hcal,minimum,r_hcal,maximum)
        v_magnet = TLine(r_magnet,minimum,r_magnet,maximum)
        v_mb1 = TLine(r_mb1,minimum,r_mb1,maximum)
        h_ecal = TLine(minimum,r_ecal,maximum,r_ecal)
        h_hcal = TLine(minimum,r_hcal,maximum,r_hcal)
        h_magnet = TLine(minimum,r_magnet,maximum,r_magnet)
        h_mb1 = TLine(minimum,r_mb1,maximum,r_mb1)

    v_ecal.SetLineColor(2)
    h_ecal.SetLineColor(2)
    v_hcal.SetLineColor(881)
    h_hcal.SetLineColor(881)
    v_magnet.SetLineColor(1)
    h_magnet.SetLineColor(1)
    v_mb1.SetLineColor(801)
    h_mb1.SetLineColor(801)

    v_ecal.SetLineWidth(4)
    h_ecal.SetLineWidth(4)
    v_hcal.SetLineWidth(4)
    h_hcal.SetLineWidth(4)
    v_magnet.SetLineWidth(4)
    h_magnet.SetLineWidth(4)
    v_mb1.SetLineWidth(4)
    h_mb1.SetLineWidth(4)

    v_ecal.SetLineStyle(3)
    h_ecal.SetLineStyle(3)
    v_hcal.SetLineStyle(2)
    h_hcal.SetLineStyle(2)
    v_magnet.SetLineStyle(4)
    h_magnet.SetLineStyle(4)
    v_mb1.SetLineStyle(8)
    h_mb1.SetLineStyle(8)

    leg = TLegend(0.75, 0.75, 0.9, 0.9)
    leg.AddEntry(v_ecal,"ECAL","L")
    leg.AddEntry(v_hcal,"HCAL","L")
    leg.AddEntry(v_magnet,"solenoid","L")
    leg.AddEntry(v_mb1,"MB1","L")

    #pal= 68 #kAvocado
    #pal= 64 #kAquamarine, very readable
    #pal= 75 #kCherry 75, awful
    #pal= 85 #kIsland 85, not beautiful but readable
    #pal= 86 #kLake 86, too violet
    #pal= 87 #kLightTemperature 87, used for trigger
    #pal= 91 #kPastel 91, too purple
    #pal= 100 #kSolar 100, very red and orange
    pal= 98 #kSandyTerrain 98, quite fine
    #pal= 99 #kSienna 99, a bit hard to read
    gStyle.SetPalette(pal)
    gStyle.SetPaintTextFormat(".0f")

    cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 )*(EventWeight)"
    cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 && HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v)*(EventWeight)"
    cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 && HLT_HT650_DisplacedDijet60_Inclusive_v)*(EventWeight)"
    #cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 && (HLT_IsoMu24_v || HLT_Ele27_WPTight_Gsf_v))*(EventWeight)"
    #cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 && HLT_VBF_DisplacedJet40_VTightID_Hadronic_v)*(EventWeight)"
    ##cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 && HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v && MEt.pt>200)*(EventWeight)"
    #cutstring = "(fabs(GenBquarks[0].eta)<2.4 && fabs(GenBquarks[2].eta)<2.4 && HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v)*(EventWeight)"

    for i, s in enumerate(sign):
        chain[s] = TChain("ntuple/tree")
        if filename=="":
            for p, ss in enumerate(samples[s]['files']):
                chain[s].Add(NTUPLEDIR + ss + ".root")
        else:
            chain[s].Add(filename+".root")
        #filename[s] = TFile("VBFH_HToSSTobbbb_MH-125_MS-30_ctauS-1000.root", "READ")
        hist[s] = TH2F(s, "", nbins, minimum, maximum, nbins, minimum, maximum)
        hist[s].Sumw2()
        if var=="z":
            #chain[s].Project(s, "sqrt(pow(GenBquarks[0].radius,2) - pow(GenBquarks[0].radius2D,2)) * GenBquarks[0].eta/abs(GenBquarks[0].eta):sqrt(pow(GenBquarks[2].radius,2) - pow(GenBquarks[2].radius2D,2)) * GenBquarks[0].eta/abs(GenBquarks[0].eta)", cutstring)
            #sign of eta for getting the right z value!
            chain[s].Project(s, "sqrt(pow(GenBquarks[0].radius,2) - pow(GenBquarks[0].radius2D,2)):sqrt(pow(GenBquarks[2].radius,2) - pow(GenBquarks[2].radius2D,2))", cutstring)
        else:
            chain[s].Project(s, "GenBquarks[0]."+var+":GenBquarks[2]."+var+"", cutstring)
        hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
        c1 = TCanvas("c1", "c1", 1000, 1000)
        c1.cd()
        c1.SetGrid()
        c1.SetLogz()
        #c1.SetLogx()
        #c1.SetLogy()
        hist[s].GetYaxis().SetTitle("Leading #pi transverse decay length (cm)")#("GenBquarks[0] "+var+" (cm)")
        hist[s].GetYaxis().SetTitleOffset(1.4)
        hist[s].GetXaxis().SetTitle("Sub-leading #pi transverse decay length (cm)")#("GenBquarks[2] "+var+" (cm)")
        hist[s].SetTitle(samples[s]['label'] if filename=="" else filename)
        hist[s].SetMarkerColor(0)
        hist[s].Draw("colztext")
        v_ecal.Draw("sames")
        h_ecal.Draw("sames")
        v_hcal.Draw("sames")
        h_hcal.Draw("sames")
        v_magnet.Draw("sames")
        h_magnet.Draw("sames")
        v_mb1.Draw("sames")
        h_mb1.Draw("sames")
        leg.Draw("sames")
        c1.Print("macro/2D_gen_b_quark_"+var+"_"+(s if filename=="" else filename)+string+".png")
        c1.Print("macro/2D_gen_b_quark_"+var+"_"+(s if filename=="" else filename)+string+".pdf")

        if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
        c1.Close()

taglio = "_acceptance"
taglio = "_MET_trigger"
taglio = "_displaced_dijet_trigger"
#taglio = "_single_lepton_trigger"
#taglio = "_VBF_displaced_jet_trigger"
signal_15 = {
#    'ZH_M15_ctau100' :
#        {
#        'max' : 50,
#        },
    'VBFH_M15_ctau100' :
        {
        'max' : 50,
        },
#    'ggH_M15_ctau100' :
#        {
#        'max' : 50,
#        },
#    'ZH_M15_ctau1000' :
#        {
#        'max' : 500,
#        },
    'VBFH_M15_ctau1000' :
        {
        'max' : 500,
        },
#    'ggH_M15_ctau1000' :
#        {
#        'max' : 500,
#        },
#    'ZH_M15_ctau10000' :
#        {
#        'max' : 4000,
#        },
    'VBFH_M15_ctau10000' :
        {
        'max' : 4000,
        },
#    'ggH_M15_ctau10000' :
#        {
#        'max' : 4000,
#        },
}

signal = {
#    'ZH_M40_ctau100' :
#        {
#        'max' : 50,
#        },
    'VBFH_M30_ctau100' :
        {
        'max' : 50,
        },
#    'ggH_M30_ctau100' :
#        {
#        'max' : 50,
#        },
#    'ZH_M40_ctau1000' :
#        {
#        'max' : 500,
#        },
    'VBFH_M30_ctau1000' :
        {
        'max' : 500,
        },
#    'ggH_M30_ctau1000' :
#        {
#        'max' : 500,
#        },
#    'ZH_M40_ctau10000' :
#        {
#        'max' : 4000,
#        },
    'VBFH_M30_ctau10000' :
        {
        'max' : 4000,
        },
#    'ggH_M30_ctau10000' :
#        {
#        'max' : 4000,
#        },
}

signal_50 = {
    'ZH_M55_ctau100' :
        {
        'max' : 30,
        },
    'VBFH_M50_ctau100' :
        {
        'max' : 30,
        },
    'ggH_M50_ctau100' :
        {
        'max' : 30,
        },
    'ZH_M55_ctau1000' :
        {
        'max' : 400,
        },
    'VBFH_M50_ctau1000' :
        {
        'max' : 400,
        },
    'ggH_M50_ctau1000' :
        {
        'max' : 400,
        },
    'ZH_M55_ctau10000' :
        {
        'max' : 2000,
        },
    'VBFH_M50_ctau10000' :
        {
        'max' : 2000,
        },
    'ggH_M50_ctau10000' :
        {
        'max' : 2000,
        },
}

#for a in signal.keys():
#    print a
#    plot_2D([a],"radius2D",nbins=20,minimum=0,maximum=signal[a]['max'],filename="",string=taglio)

signal = ["HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-1000mm","HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm"]
for a in signal:
    plot_2D([a],"radius2D",nbins=20,minimum=0,maximum=500,filename=a,string=taglio)

#plot_2D(a,"radius2D",nbins=20,minimum=0,maximum=500,filename=a,string=taglio)

#plot_2D("radius2D",nbins=20,minimum=0,maximum=1000,filename="VBFH_HToSSTobbbb_MH-125_MS-30_ctauS-1000",string=taglio)
#plot_2D("radius2D",nbins=20,minimum=0,maximum=2000,filename="ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000",string=taglio)
#plot_2D("z",nbins=10,minimum=0,maximum=1000,filename="VBFH_HToSSTobbbb_MH-125_MS-30_ctauS-1000")
