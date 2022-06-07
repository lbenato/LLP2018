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
NTUPLEDIR = "/nfs/dust/cms/group/cms-llp/test_heavy_higgs_GENSIM/"
#NTUPLEDIR = "/nfs/dust/cms/group/cms-llp/test_SUSY/"


NTUPLEDIR = "/nfs/dust/cms/group/cms-llp/v0_SUSY_calo_MINIAOD_2018/"
from Analyzer.LLP2018.samplesMINIAOD2018 import sample, samples
OUTPUTDIR = "plots/v0_SUSY_calo_MINIAOD_2018/METPreSelSUSYAOD/"

#NTUPLEDIR = "/nfs/dust/cms/group/cms-llp/HeavyHiggs_GENSIM/"
#OUTPUTDIR = "plots/HeavyHiggs_GENSIM/"
#from Analyzer.LLP2018.samples import sample, samples

### Parking 2018:
from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
from Analyzer.LLP2018.variables_Parking2018 import *
from Analyzer.LLP2018.selections_Parking2018 import *
NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v2_central_2018miniAOD_tracking_03Feb2021/"     ###### Gen Level plots
# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v5_central_2018miniAOD_tracking_12Mar2021/"     # With gen & reco muon info, ROI info. Trigger requirement (HT inclusive). All MC samples & DisplacedJet data

OUTPUTDIR   = "plots/v2_central2018_genLevel_17Aug2021/track_2D_decayRadius/"              ###### Gen Level plots



def plot_2D(sign,var,nbins=50,minimum=0,maximum=2000,bins=np.array([]),filename="",string="",part_var="GenBquarks",particle="#pi",norm=False):
    chain = {}
    hist = {}
    # r_ecal = 129
    # r_hcal = 179
    # r_magnet = 295
    # r_mb1 = 402
    # r_mb4 = 738
    #
    # z_ecal = 300
    # z_hcal = 376
    # z_magnet = 0
    # z_mb1 = 560

    # if var=="radius2D":
    #     v_ecal = TLine(r_ecal,minimum,r_ecal,maximum)
    #     v_hcal = TLine(r_hcal,minimum,r_hcal,maximum)
    #     v_magnet = TLine(r_magnet,minimum,r_magnet,maximum)
    #     v_mb1 = TLine(r_mb1,minimum,r_mb1,maximum)
    #     v_mb4 = TLine(r_mb4,minimum,r_mb4,maximum)
    #     h_ecal = TLine(minimum,r_ecal,maximum,r_ecal)
    #     h_hcal = TLine(minimum,r_hcal,maximum,r_hcal)
    #     h_magnet = TLine(minimum,r_magnet,maximum,r_magnet)
    #     h_mb1 = TLine(minimum,r_mb1,maximum,r_mb1)
    #     h_mb4 = TLine(minimum,r_mb4,maximum,r_mb4)
    # elif var=="z":
    #     v_ecal = TLine(z_ecal,minimum,z_ecal,maximum)
    #     v_hcal = TLine(z_hcal,minimum,z_hcal,maximum)
    #     v_magnet = TLine(z_magnet,minimum,z_magnet,maximum)
    #     v_mb1 = TLine(z_mb1,minimum,z_mb1,maximum)
    #     h_ecal = TLine(minimum,z_ecal,maximum,z_ecal)
    #     h_hcal = TLine(minimum,z_hcal,maximum,z_hcal)
    #     h_magnet = TLine(minimum,z_magnet,maximum,z_magnet)
    #     h_mb1 = TLine(minimum,z_mb1,maximum,z_mb1)
    # else:
    #     v_ecal = TLine(r_ecal,minimum,r_ecal,maximum)
    #     v_hcal = TLine(r_hcal,minimum,r_hcal,maximum)
    #     v_magnet = TLine(r_magnet,minimum,r_magnet,maximum)
    #     v_mb1 = TLine(r_mb1,minimum,r_mb1,maximum)
    #     h_ecal = TLine(minimum,r_ecal,maximum,r_ecal)
    #     h_hcal = TLine(minimum,r_hcal,maximum,r_hcal)
    #     h_magnet = TLine(minimum,r_magnet,maximum,r_magnet)
    #     h_mb1 = TLine(minimum,r_mb1,maximum,r_mb1)

    # v_ecal.SetLineColor(2)
    # h_ecal.SetLineColor(2)
    # v_hcal.SetLineColor(881)
    # h_hcal.SetLineColor(881)
    # v_magnet.SetLineColor(1)
    # h_magnet.SetLineColor(1)
    # v_mb1.SetLineColor(801)
    # v_mb4.SetLineColor(4)
    # h_mb1.SetLineColor(801)
    # h_mb4.SetLineColor(4)
    #
    # v_ecal.SetLineWidth(4)
    # h_ecal.SetLineWidth(4)
    # v_hcal.SetLineWidth(4)
    # h_hcal.SetLineWidth(4)
    # v_magnet.SetLineWidth(4)
    # h_magnet.SetLineWidth(4)
    # v_mb1.SetLineWidth(4)
    # h_mb1.SetLineWidth(4)
    # v_mb4.SetLineWidth(3)
    # h_mb4.SetLineWidth(3)
    #
    # v_ecal.SetLineStyle(3)
    # h_ecal.SetLineStyle(3)
    # v_hcal.SetLineStyle(2)
    # h_hcal.SetLineStyle(2)
    # v_magnet.SetLineStyle(4)
    # h_magnet.SetLineStyle(4)
    # v_mb1.SetLineStyle(8)
    # h_mb1.SetLineStyle(8)
    # v_mb4.SetLineStyle(9)
    # h_mb4.SetLineStyle(9)

    # leg = TLegend(1-0.9, 0.75, 1-0.75, 0.9)
    # leg.AddEntry(v_ecal,"ECAL","L")
    # leg.AddEntry(v_hcal,"HCAL","L")
    # leg.AddEntry(v_magnet,"solenoid","L")
    # leg.AddEntry(v_mb1,"MB1","L")
    # leg.AddEntry(v_mb4,"MB4","L")

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
    # gStyle.SetPalette(pal)
    gStyle.SetPaintTextFormat(".00f")

    if part_var=="GenBquarks":
        cutstring = "(EventWeight) * ( (HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v && Flag_BadPFMuon && Flag_BadChCand) && nMuons==0 && nElectrons==0 && nPhotons==0 && nTaus==0 && HT>100 && MEt.pt>120 )"
        #cutstring = "(EventWeight)"
        #cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 )*(EventWeight)"
        #cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 && HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v)*(EventWeight)"
        #cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 && HLT_HT650_DisplacedDijet60_Inclusive_v)*(EventWeight)"
        #cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 && (HLT_IsoMu24_v || HLT_Ele27_WPTight_Gsf_v))*(EventWeight)"
        #cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 && HLT_VBF_DisplacedJet40_VTightID_Hadronic_v)*(EventWeight)"
        ##cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 && HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v && MEt.pt>200)*(EventWeight)"
        #cutstring = "(fabs("+part_var+"[0].eta)<2.4 && fabs("+part_var+"[2].eta)<2.4 && HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v)*(EventWeight)"
    else:
        # cutstring = "(EventWeight) * ( (HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v && Flag_BadPFMuon && Flag_BadChCand) && nMuons==0 && nElectrons==0 && nPhotons==0 && nTaus==0 && HT>100 && MEt.pt>120 )"
        #MINIAOD: cutstring = "(EventWeight) * ( (HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && nMuons==0 && nElectrons==0 && nPhotons==0 && nTaus==0 && HT>100 && MEt.pt>120 )"
        #cutstring = "isMC"
        cutstring = "(EventWeight)"
        #cutstring = "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v)*(EventWeight)"
        #cutstring = "isMC"
        # cutstring = "(EventWeight) * HLT_Mu9_IP6_part0_v"
        # cutstring = "(EventWeight/PUWeight) * PUWeight_HLT_Mu9_IP6 * HLT_Mu9_IP6_part0_v"


    for i, s in enumerate(sign):
        chain[s] = TChain("ntuple/tree")
        if filename=="":
            for p, ss in enumerate(samples[s]['files']):
                chain[s].Add(NTUPLEDIR + ss + ".root")
        else:
            chain[s].Add(NTUPLEDIR + filename+".root")
        print "Entries: ", chain[s].GetEntries()
        #filename[s] = TFile("VBFH_HToSSTobbbb_MH-125_MS-30_ctauS-1000.root", "READ")
        if len(bins) ==0:
            hist[s] = TH2F(s, "", nbins, minimum, maximum, nbins, minimum, maximum)
        else:
            hist[s] = TH2F(s, "", len(bins)-1, bins, len(bins)-1, bins)
        hist[s].Sumw2()
        if "_MaxMin" in var:
            varname = var.replace("MaxMin","")
            chain[s].Project(s, "Max$("+part_var+"."+varname+"):Min$("+part_var+"."+varname+")", cutstring)
            print "Plotting: Max$("+part_var+"."+varname+"):Min$("+part_var+"."+varname+")"
        elif "_LeadSubleadPt" in var and part_var=="GenLLPs":
            varname = var.replace("_LeadSubleadPt","")
            chain[s].Project(s, "(GenLLPs[0].travelRadius*(GenLLPs[0].pt>GenLLPs[1].pt)+GenLLPs[1].travelRadius*(GenLLPs[1].pt>GenLLPs[0].pt)):(GenLLPs[1].travelRadius*(GenLLPs[0].pt>GenLLPs[1].pt)+GenLLPs[0].travelRadius*(GenLLPs[1].pt>GenLLPs[0].pt))", cutstring)
            # chain[s].Project(s, +part_var+"[0]."+varname+":"+part_var+"[1]."+varname+")", cutstring)
            # print "Plotting: Max$("+part_var+"."+varname+"):Min$("+part_var+"."+varname+")"
        elif var=="z":
            #chain[s].Project(s, "sqrt(pow("+part_var+"[0].radius,2) - pow("+part_var+"[0].radius2D,2)) * "+part_var+"[0].eta/abs("+part_var+"[0].eta):sqrt(pow("+part_var+"[2].radius,2) - pow("+part_var+"[2].radius2D,2)) * "+part_var+"[0].eta/abs("+part_var+"[0].eta)", cutstring)
            #sign of eta for getting the right z value!
            chain[s].Project(s, "sqrt(pow("+part_var+"[0].radius,2) - pow("+part_var+"[0].radius2D,2)):sqrt(pow("+part_var+"[2].radius,2) - pow("+part_var+"[2].radius2D,2))", cutstring)
        else:
            if part_var=="GenBquarks":
                chain[s].Project(s, ""+part_var+"[0]."+var+":"+part_var+"[2]."+var+"", cutstring)
            else:
                chain[s].Project(s, ""+part_var+"[0]."+var+":"+part_var+"[1]."+var+"", cutstring)
        hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
        if norm:
            hist[s].Scale(100./hist[s].Integral())
            gStyle.SetPaintTextFormat('5.2f')
        c1 = TCanvas("c1", "c1", 1000, 1000)
        c1.cd()
        #c1.SetGrid()
        c1.SetLogz()
        c1.SetLogx()
        c1.SetLogy()
        hist[s].GetZaxis().SetTitle("%")
        hist[s].GetZaxis().SetRangeUser(0.001,10)
        hist[s].GetYaxis().SetTitle("Leading "+particle+" decay radius (cm)")#(""+part_var+"[0] "+var+" (cm)")
        # hist[s].GetYaxis().SetTitle("Leading "+particle+" decay z-position (cm)")#(""+part_var+"[0] "+var+" (cm)")
        hist[s].GetYaxis().SetTitleOffset(1.4)
        hist[s].GetXaxis().SetTitle("Subleading "+particle+" decay radius (cm)")#(""+part_var+"[2] "+var+" (cm)")
        # hist[s].GetXaxis().SetTitle("Subleading "+particle+" decay z-position (cm)")#(""+part_var+"[2] "+var+" (cm)")
        hist[s].SetTitle(samples[s]['label'] if filename=="" else filename)
        hist[s].SetMarkerColor(0)#(2)#
        hist[s].Draw("colz")#()#
        # v_ecal.Draw("sames")
        # h_ecal.Draw("sames")
        # v_hcal.Draw("sames")
        # h_hcal.Draw("sames")
        # v_magnet.Draw("sames")
        # h_magnet.Draw("sames")
        # v_mb1.Draw("sames")
        # h_mb1.Draw("sames")
        # v_mb4.Draw("sames")
        # h_mb4.Draw("sames")
        hist[s].SetMarkerSize(1.2)#(2)#
        hist[s].Draw("text,sames")#()#
        # leg.Draw("sames")
        c1.Print(OUTPUTDIR+"2D_"+particle+"_"+var+"_"+(s if filename=="" else filename)+string+".png")
        c1.Print(OUTPUTDIR+"2D_"+particle+"_"+var+"_"+(s if filename=="" else filename)+string+".pdf")

        if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
        c1.Close()

taglio = "_preselections"
#taglio = "_nocuts"
#taglio = "_acceptance"
#taglio = "_MET_trigger"
#taglio = "_displaced_dijet_trigger"
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
#    plot_2D([a],"radius2D",nbins=20,minimum=0,maximum=signal[a]['max'],bins=np.array([]),filename="",string=taglio)

'''
#SUSY
signal = ["mchi200_pl1000","mchi300_pl1000","mchi400_pl1000"]
for a in signal:
    plot_2D([a],"radius2D",nbins=50,minimum=9.9,maximum=50000,bins=np.array([9.9,25,50,100,250,500,1000,5000,10000,50000]),filename=a,string=taglio,part_var="GenHiggs")

exit()
'''

'''
#Heavy Higgs
signal = ["GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-8_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-8_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-1000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-10000",    "GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-10000",   "GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-10000","GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-1000",     "GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-1000","GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-10000",    "GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-10000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-150_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-600_MS-50_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-55_ctauS-5000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-500",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-2000",
"GluGluH2_H2ToSSTobbbb_MH-125_MS-25_ctauS-5000",
]

for a in signal:
    plot_2D([a],"radius2D",nbins=50,minimum=9.9,maximum=50000,bins=np.array([9.9,50,100,250,500,1000,5000,10000,50000]),filename=a,string=taglio,part_var="GenBquarks")

'''

'''
##Heavy Higgs gen sim
signal = [
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-500_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-2000_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-10000_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-500_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-2000_TuneCP5_13TeV-pythia8",
    "GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-5000_TuneCP5_13TeV-pythia8",
    #"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-10000_TuneCP5_13TeV-pythia8",
    ]
for a in signal:
    plot_2D([a],"radius2D",nbins=50,minimum=1,maximum=5000,bins=np.array([1.,5.,10.,50,100,250,500,1000,5000]),filename=a,string=taglio,part_var="GenBquarks", particle="S", norm=True)
'''

##SUSY

'''
signal = ['n3n2-n1-hbb-hbb_mh400_pl1000','n3n2-n1-hbb-hbb_mh300_pl1000','n3n2-n1-hbb-hbb_mh200_pl1000']

for a in signal:
    plot_2D([a],"radius2D",nbins=50,minimum=1,maximum=5000,bins=np.array([1.,5.,10.,50,100,250,500,1000,5000]),filename=a,string=taglio,part_var="GenHiggs", particle="b", norm=True)
exit()
'''

#HEAVY HIGGS

signal = ['ggH_MH1000_MS400_ctau500',
	'ggH_MH1000_MS400_ctau1000',
	'ggH_MH1000_MS400_ctau2000',
	'ggH_MH1000_MS400_ctau5000',
	'ggH_MH1000_MS400_ctau10000',

	'ggH_MH1000_MS150_ctau500',
	'ggH_MH1000_MS150_ctau1000',
	'ggH_MH1000_MS150_ctau2000',
	'ggH_MH1000_MS150_ctau5000',
	'ggH_MH1000_MS150_ctau10000']

# Parking 2018

sign_track_VBFH_m15 = ["VBFH_M15_ctau10","VBFH_M15_ctau50", "VBFH_M15_ctau100"]#
sign_track_VBFH_m40 = ["VBFH_M40_ctau10","VBFH_M40_ctau50", "VBFH_M40_ctau100"]#
sign_track_VBFH_m55 = ["VBFH_M55_ctau10","VBFH_M55_ctau50", "VBFH_M55_ctau100"]#

sign_track_ggH_m15 = ["ggH_M15_ctau10", "ggH_M15_ctau100", "ggH_M15_ctau1000"]# ggH_M15_ctau1 missing from central prod.
sign_track_ggH_m40 = ["ggH_M40_ctau1","ggH_M40_ctau10", "ggH_M40_ctau100", "ggH_M40_ctau1000"]#
sign_track_ggH_m55 = ["ggH_M55_ctau1","ggH_M55_ctau10", "ggH_M55_ctau100", "ggH_M55_ctau1000"]#

sign_track_VBFH_ctau10 = ["VBFH_M55_ctau10","VBFH_M40_ctau10","VBFH_M15_ctau10"]#
sign_track_ggH_ctau10 = ["ggH_M55_ctau10","ggH_M40_ctau10","ggH_M15_ctau10"]#

signal = sign_track_ggH_ctau10 + sign_track_VBFH_ctau10

suffix = "_inclusive"
# suffix = "_HLT_Mu9_IP6"


# plot_2D(signal,"radius2D",nbins=50,minimum=1,maximum=5000,bins=np.array([1.,5.,10.,50,100,250,500,1000,5000]),filename="",string=taglio,part_var="GenBquarks", particle="S", norm=True)
# plot_2D(signal,"travelRadius",nbins=50,minimum=0.1,maximum=100,filename="",string="_inclusive",part_var="GenLLPs", particle="LLP", norm=True)
plot_2D(signal,"travelRadius_LeadSubleadPt",bins=np.array([0.004,0.01,0.02,0.04,0.1,0.2,0.4,1,2,4,10,20,40,100]),filename="",string=suffix,part_var="GenLLPs", particle="LLP", norm=True)

exit()
for a in signal:
    print a
    print samples[a]['files']
    plot_2D([a],"radius2D",nbins=50,minimum=1,maximum=5000,bins=np.array([1.,5.,10.,50,100,250,500,1000,5000]),filename=a,string=taglio,part_var="GenBquarks", particle="S", norm=True)


#plot_2D(a,"radius2D",nbins=20,minimum=0,maximum=500,bins=np.array([]),filename=a,string=taglio)

#plot_2D("radius2D",nbins=20,minimum=0,maximum=1000,bins=np.array([]),filename="VBFH_HToSSTobbbb_MH-125_MS-30_ctauS-1000",string=taglio)
#plot_2D("radius2D",nbins=20,minimum=0,maximum=2000,bins=np.array([]),filename="ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10000",string=taglio)
#plot_2D("z",nbins=10,minimum=0,maximum=1000,bins=np.array([]),filename="VBFH_HToSSTobbbb_MH-125_MS-30_ctauS-1000")
