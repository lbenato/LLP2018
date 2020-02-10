#! /usr/bin/env python                                                          
                                                                                
import os, multiprocessing                                                      
import copy                                                                     
import math                                                                     
from array import array                                                         
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory                 
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph        
from ROOT import TStyle, TCanvas, TPad                                          
from ROOT import TLegend, TLatex, TText, TLine

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
#parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)
gStyle.SetOptStat(0)

NTUPLEDIR = "/nfs/dust/cms/user/lbenato/RecoStudies_ntuples_v5/"
PLOTDIR = "/afs/desy.de/user/l/lbenato/LongLivedReconstruction/CMSSW_8_0_26_patch1/src/Analyzer/LongLivedReco/macro/plots/"

samples = {
    'ZH_MS-40_ctauS-0' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 0 mm',
        'type': 'reconstruction',
        },
    'ZH_MS-40_ctauS-0p05' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 0.05 mm',
        'type': 'reconstruction',
        },
    'ZH_MS-40_ctauS-1' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 1 mm',
        'type': 'reconstruction',
        },
    'ZH_MS-40_ctauS-10' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 10 mm',
        'type': 'reconstruction',
        },
    'ZH_MS-40_ctauS-100' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 100 mm',
        'type': 'reconstruction',
        },
    'ZH_MS-40_ctauS-1000' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 1 m',
        'type': 'reconstruction',
        },
    'ZH_MS-40_ctauS-10000' : 
    {
        'file' : 'ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 10 m',
        'type': 'reconstruction',
        },
    'TT' :
        {
        'file' : 'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8',
        'leg_name' : 'ttbar',
        'type': 'reconstruction',
        },
    'QCD_HT200to300' :
        {
        'file' : 'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
        'leg_name' : 'QCD HT200to300',
        'type': 'reconstruction',
        },
    'VBFH_MS-40_ctauS-0' :
        {
        'file' : 'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8',
        'leg_name' : 'm_{#pi} = 40 GeV, c#tau = 0 mm, VBF',
        'type': 'reconstruction',
        },
    'VBFHToBB' :
        {
        'file' : 'VBFHToBB_M-125_13TeV_powheg_pythia8',
        'leg_name' : 'H to bb, VBF',
        'type': 'reconstruction',
        },
}

variables = {
    'Matching_to_b_AK4Jets' :
        {
        'axis_label' : 'n. of b-quarks matched to one AK4 jet',
        'xmin' : 0.,
        'xmax' : 5,
        'rebin' : 1,
        'linecolor' : 1,
        'log' : True,
        },
    'Matching_to_b_CHSAK4Jets' :
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'xmin' : 0.,
        'xmax' : 5,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'Matching_to_pi_AK4Jets' :
        {
        'axis_label' : 'n. of #pi matched to one AK4 jet',
        'xmin' : 0.,
        'xmax' : 3,
        'rebin' : 1,
        'linecolor' : 1,
        'log' : True,
        },
    'Matching_to_pi_CHSAK4Jets' :
        {
        'axis_label' : 'Matching_to_#pi_CHSAK4Jets',
        'xmin' : 0.,
        'xmax' : 3,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'CSV_AK4Jets_matched_to_0b' :
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 0 b',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'CSV_AK4Jets_matched_to_1b':
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 1 b',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'CSV_AK4Jets_matched_to_2b' :
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 2 b',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'CSV_AK4Jets_matched_to_more_2b':
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to >2 b',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
##
    'CSV_AK4Jets_matched_to_0pi' :
        {
        'axis_label' : 'Matching_to_pi_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 0 #pi',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'CSV_AK4Jets_matched_to_1pi':
        {
        'axis_label' : 'Matching_to_pi_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 1 #pi',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
    'CSV_AK4Jets_matched_to_2pi' :
        {
        'axis_label' : 'Matching_to_pi_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 2 #pi',
        'xmin' : 0.,
        'xmax' : 1,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : False,
        },
#pT
    'pT_AK4Jets_matched_to_0b' :
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 0 b',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },
    'pT_AK4Jets_matched_to_1b':
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 1 b',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },
    'pT_AK4Jets_matched_to_2b' :
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 2 b',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },
    'pT_AK4Jets_matched_to_more_2b':
        {
        'axis_label' : 'Matching_to_b_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to >2 b',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },
##
    'pT_AK4Jets_matched_to_0pi' :
        {
        'axis_label' : 'Matching_to_pi_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 0 #pi',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },
    'pT_AK4Jets_matched_to_1pi':
        {
        'axis_label' : 'Matching_to_pi_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 1 #pi',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },
    'pT_AK4Jets_matched_to_2pi' :
        {
        'axis_label' : 'Matching_to_pi_CHSAK4Jets',
        'legend_label' : 'AK4 jets matched to 2 #pi',
        'xmin' : 0.,
        'xmax' : 1000,
        'rebin' : 1,
        'linecolor' : 2,
        'log' : True,
        },

}




colors = [4, 410, 2, 856, 634, 1, 881, 798, 602, 921, 801, 3, 5, 6, ]
nomefile = {}
histo = {}
uncert = {}

gStyle.SetOptStat(0)

def compare_samples(sample_list, var):
    cs = TCanvas("cs","cs",1000,800)
    cs.SetGrid()
    cs.cd()
    leg = TLegend(0.68, 0.6, 0.98, 0.88)
    for i, s in enumerate(sample_list):
        nomefile[s] = TFile.Open(NTUPLEDIR+samples[s]['file']+".root", 'read')
        histo[s] = nomefile[s].Get(samples[s]['type']+"/"+var)
        histo[s].SetLineColor(colors[i])
        histo[s].SetLineWidth(3)
        histo[s].SetTitle("")
        histo[s].GetXaxis().SetTitle(variables[var]['axis_label'])
        leg.AddEntry(histo[s],samples[s]['leg_name'])
        histo[s].GetXaxis().SetRangeUser(variables[var]['xmin'],variables[var]['xmax'])
        histo[s].Draw("same")
        uncert[s] = histo[s].Clone(s+"_err")
        uncert[s].SetMarkerStyle(0)
        uncert[s].SetFillColor(colors[i])
        uncert[s].SetFillStyle(3001)
        uncert[s].Draw("SAME,E2")
    if variables[var]['log']:
        cs.SetLogy()
    leg.Draw()
    latex = TLatex()                                                                                                                                              
    latex.SetNDC()                                                                                                                                                
    latex.SetTextAlign(33)                                                                                                                                        
    latex.SetTextSize(0.04)                                                                                                                                       
    latex.SetTextFont(62)                                                                                                                                         
    latex.DrawLatex(0.20, 0.96, "CMS")                                                                                                                           
    latex.SetTextFont(52)                                                                                                                                         
    latex.DrawLatex(0.36, 0.96, "Simulation")
    cs.Print(PLOTDIR+var+'.png')
    cs.Print(PLOTDIR+var+'.pdf')
    cs.Close()

def compare_variables(sample, var_list,name):
    cv = TCanvas("cv","cv",1000,800)
    cv.SetGrid()
    cv.cd()
    if "CSV" in name:
        leg = TLegend(0.12, 0.6, 0.45, 0.88)
    elif "pT" in name:
        leg = TLegend(0.62, 0.6, 0.95, 0.88)
    nomefile[sample] = TFile.Open(NTUPLEDIR+samples[sample]['file']+".root", 'read')
    leg.SetHeader(samples[sample]['leg_name'])
    massimo = 0
    for i, s in enumerate(var_list):
        histo[s] = nomefile[sample].Get(samples[sample]['type']+"/"+s)
        histo[s].SetLineColor(colors[i])
        histo[s].SetLineWidth(3)
        histo[s].SetTitle("")
        if "CSV" in name:
            histo[s].GetXaxis().SetTitle("CSV score")
        elif "pT" in name:
            histo[s].GetXaxis().SetTitle("p_{T} [GeV]")
        leg.AddEntry(histo[s],variables[s]['legend_label'])
        histo[s].GetXaxis().SetRangeUser(variables[s]['xmin'],variables[s]['xmax'])
        if sample=="ZH_MS-40_ctauS-1":
            print i,s,massimo
        massimo = max(massimo, histo[s].GetMaximum())
        histo[s].Draw("same")
        histo[s].SetMaximum(massimo*1.2)
        uncert[s] = histo[s].Clone(s+"_err")
        uncert[s].SetMarkerStyle(0)
        uncert[s].SetFillColor(colors[i])
        uncert[s].SetFillStyle(3001)
        uncert[s].Draw("SAME,E2")
    if variables[s]['log']:
        cv.SetLogy()
    leg.Draw()
    latex = TLatex()                                                                                                                                              
    latex.SetNDC()                                                                                                                                                
    latex.SetTextAlign(33)                                                                                                                                        
    latex.SetTextSize(0.04)                                                                                                                                       
    latex.SetTextFont(62)                                                                                                                                         
    latex.DrawLatex(0.20, 0.96, "CMS")                                                                                                                           
    latex.SetTextFont(52)                                                                                                                                         
    latex.DrawLatex(0.36, 0.96, "Simulation")
    cv.Print(PLOTDIR+name+"_"+sample+'.png')
    cv.Print(PLOTDIR+name+"_"+sample+'.pdf')
    cv.Close()

sampl = ['ZH_MS-40_ctauS-0','ZH_MS-40_ctauS-1','ZH_MS-40_ctauS-10','ZH_MS-40_ctauS-1000']#,'ZH_MS-40_ctauS-1000',]
variabl = 'Matching_to_b_AK4Jets'
#'Matching_to_b_CHSAK4Jets'
compare_samples(sampl,variabl)
if not gROOT.IsBatch(): raw_input("Press Enter to continue...") 


sampl = ['ZH_MS-40_ctauS-0','ZH_MS-40_ctauS-1','ZH_MS-40_ctauS-10','ZH_MS-40_ctauS-1000']#,'ZH_MS-40_ctauS-1000',]
variabl = 'Matching_to_pi_AK4Jets'
#'Matching_to_b_CHSAK4Jets'
compare_samples(sampl,variabl)
if not gROOT.IsBatch(): raw_input("Press Enter to continue...") 

one_sampl = 'ZH_MS-40_ctauS-0'
var_list = ['CSV_AK4Jets_matched_to_0b','CSV_AK4Jets_matched_to_1b','CSV_AK4Jets_matched_to_2b','CSV_AK4Jets_matched_to_more_2b']
#compare_variables(one_sampl,var_list,"CSV")


for a in ['ZH_MS-40_ctauS-0','ZH_MS-40_ctauS-0p05','ZH_MS-40_ctauS-1','ZH_MS-40_ctauS-10','ZH_MS-40_ctauS-100','ZH_MS-40_ctauS-1000','TT','QCD_HT200to300','VBFH_MS-40_ctauS-0','VBFHToBB']:
    compare_variables(a,var_list,"CSV_b")
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...") 


#one_sampl = 'ZH_MS-40_ctauS-0'
var_list = ['CSV_AK4Jets_matched_to_0pi','CSV_AK4Jets_matched_to_1pi','CSV_AK4Jets_matched_to_2pi']
#compare_variables(one_sampl,var_list,"CSV")

for a in ['ZH_MS-40_ctauS-0','ZH_MS-40_ctauS-0p05','ZH_MS-40_ctauS-1','ZH_MS-40_ctauS-10','ZH_MS-40_ctauS-100','ZH_MS-40_ctauS-1000']:
    compare_variables(a,var_list,"CSV_pi")
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...") 


var_list = ['pT_AK4Jets_matched_to_0b','pT_AK4Jets_matched_to_1b','pT_AK4Jets_matched_to_2b','pT_AK4Jets_matched_to_more_2b']
#compare_variables(one_sampl,var_list,"pT")

for a in ['ZH_MS-40_ctauS-0','ZH_MS-40_ctauS-0p05','ZH_MS-40_ctauS-1','ZH_MS-40_ctauS-10','ZH_MS-40_ctauS-100','ZH_MS-40_ctauS-1000','TT','QCD_HT200to300','VBFH_MS-40_ctauS-0','VBFHToBB']:
    compare_variables(a,var_list,"pT_b")
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...") 



var_list = ['pT_AK4Jets_matched_to_0pi','pT_AK4Jets_matched_to_1pi','pT_AK4Jets_matched_to_2pi']
#compare_variables(one_sampl,var_list,"pT")

for a in ['ZH_MS-40_ctauS-0','ZH_MS-40_ctauS-0p05','ZH_MS-40_ctauS-1','ZH_MS-40_ctauS-10','ZH_MS-40_ctauS-100','ZH_MS-40_ctauS-1000','TT','QCD_HT200to300','VBFH_MS-40_ctauS-0','VBFHToBB']:
    compare_variables(a,var_list,"pT_pi")
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...") 
