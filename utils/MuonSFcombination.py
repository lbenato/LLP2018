#! /usr/bin/env python

import os
from array import array
from ROOT import gStyle, TFile, TH1F, TCanvas, TLegend, ROOT, gROOT
import numpy as np

gStyle.SetOptStat(0)

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-r", "--runera", action="store", type="string", default="", dest="runera")
parser.add_option("-f", "--full", action="store_true", default=False, dest="full")
parser.add_option("-o", "--one", action="store_true", default=False, dest="one")# take only runs B-F
parser.add_option("-t", "--two", action="store_true", default=False, dest="two")# take only runs G+H
(options, args) = parser.parse_args()

lumi_BCDEF = 0.
lumi_GH = 0.
lumi_tot = 0.
if options.full and (options.one or options.two):
    print "Wrong setting for lumi! Aborting..."
    print "set full in addition with one or two run sets"
    exit()
elif options.full:
    if options.runera=="2016":
        lumi_BCDEF = 18.8442 ## fb^-1 full recorded lumi for runs b-f --> todo: adjust to your runs from golden JSON file!
        lumi_GH = 16.00 ## fb^-1 recorded lumi for runs g-h melanie golden JSON --> todo: adjust to your runs from golden JSON file!
        lumi_tot = lumi_BCDEF + lumi_GH
    else:
        print "run era beside 2016 not implemented yet!"
        exit()

if lumi_tot == 0.:
    print "no runera defined - no lumi set"
    exit()


print "###################"
print "START WITH MUON ID:"
print "###################"

rootDir = 'data/'

muSFID_AtoF = TFile(rootDir+"Muon_RunBCDEF_SF_ID_Run2_"+str(options.runera)+".root", "READ")
muSFID_GtoH = TFile(rootDir+"Muon_RunGH_SF_ID_Run2_"+str(options.runera)+".root", "READ")

outfile_Name = "MuonID_average_RunBtoH_SF_Run2_"+str(options.runera)
outFile_ID = TFile(rootDir+outfile_Name+".root", "RECREATE")
ID={"LooseID","MediumID","MediumID","TightID", "HighPtID"}
var={"pt"}
hist = ''

for h, i in enumerate(ID):
    if(i=="HighPtID" ):
        var={"pair_newTuneP_probe_pt"}      
    for g,j in enumerate(var):
        hist= "NUM_"
        hist+=i
        hist+="_DEN_genTracks_eta_"
        hist+=j
    print "hist name: ", hist
    
    # Run BCDEF & GH
    h_BCDEF_eta_ratio = muSFID_AtoF.Get(hist)
    h_GH_eta_ratio = muSFID_GtoH.Get(hist)

    # Scale with lumi
    h_BCDEF_eta_ratio.Scale(lumi_BCDEF)
    h_GH_eta_ratio.Scale(lumi_GH)
    
    # add histograms BCDEF + GH
    h_BCDEF_eta_ratio.Add(h_GH_eta_ratio)
    # save as new histogram
    new_eta_ratio = h_BCDEF_eta_ratio
    # weight histogram
    new_eta_ratio.Scale(1./lumi_tot)

    new_eta_ratio.Write()
outFile_ID.Close()
print "Muon ID file written:", rootDir+outfile_Name+".root"
muSFID_AtoF.Close()
muSFID_GtoH.Close()

print "####################"
print "START WITH MUON ISO:"
print "####################"

muSFISO_AtoF = TFile(rootDir+"Muon_RunBCDEF_SF_ISO_Run2_"+str(options.runera)+".root", "READ")
muSFISO_GtoH = TFile(rootDir+"Muon_RunGH_SF_ISO_Run2_"+str(options.runera)+".root", "READ")

outfile_Name = "MuonISO_average_RunBtoH_SF_Run2_"+str(options.runera)
outFile_ISO = TFile(rootDir+outfile_Name+".root", "RECREATE")
isolation={"TightRelIso_","LooseRelIso_"}
ID={"LooseID","MediumID","TightID", "highptID"}
var={"_eta_pt"}
hist = ''


for f,k in enumerate(isolation):
    if k=="LooseRelTkIso_": 
        ID={"HighPtIDandIPCut"}
        var={"_eta_pair_newTuneP_probe_pt"}
    if k=="TightRelIso_": 
        ID={"MediumID","TightIDandIPCut"}
        var={"_eta_pt" }
    if k=="LooseRelIso_": 
        ID={"MediumID","TightIDandIPCut","LooseID"}
        var={"_eta_pt"}
   
    for h, i in enumerate(ID):
        for g,j in enumerate(var):
            hist = "NUM_"
            hist+= k
            hist+="DEN_"
            hist+=i
            hist+=j
    print "hist name: ", hist

    # Run BCDEF & GH
    h_BCDEF_eta_ratio = muSFISO_AtoF.Get(hist)
    h_GH_eta_ratio = muSFISO_GtoH.Get(hist)

    # Scale with lumi
    h_BCDEF_eta_ratio.Scale(lumi_BCDEF)
    h_GH_eta_ratio.Scale(lumi_GH)

    # add histograms BCDEF + GH
    h_BCDEF_eta_ratio.Add(h_GH_eta_ratio)
    # save as new histogram
    new_eta_ratio = h_BCDEF_eta_ratio
    # weight histogram
    new_eta_ratio.Scale(1./lumi_tot)

    new_eta_ratio.Write()
outFile_ISO.Close()
print "Muon ISO file written:", rootDir+outfile_Name+".root"
muSFISO_AtoF.Close()
muSFISO_GtoH.Close()


print "#########################"
print "START WITH MUON Trigger:"
print "#########################"

muSFTrigger_AtoF = TFile(rootDir+"Muon_EfficienciesAndSF_RunBtoF_Trigger_Run2_"+str(options.runera)+".root", "READ")
muSFTrigger_GtoH = TFile(rootDir+"Muon_EfficienciesAndSF_Period4_RunGH_Trigger_Run2_"+str(options.runera)+".root", "READ")

outfile_Name = "MuonTrigger_average_RunBtoH_SF_Run2_"+str(options.runera)
outFile_Trigger = TFile(rootDir+outfile_Name+".root", "RECREATE")

#Trigger Mu24
h_MU24_BCDEF_eta_ratio = muSFTrigger_AtoF.Get("IsoMu24_OR_IsoTkMu24_EtaBins/eta_ratio")
h_MU24_BCDEF_abseta_pt_ratio = muSFTrigger_AtoF.Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio")
h_MU24_BCDEF_pt_abseta_ratio = muSFTrigger_AtoF.Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio")
h_MU24_BCDEF_pt_ratio = muSFTrigger_AtoF.Get("IsoMu24_OR_IsoTkMu24_PtBins/pt_ratio")

#Trigger Mu 50
h_MU50_BCDEF_eta_ratio = muSFTrigger_AtoF.Get("Mu50_OR_TkMu50_EtaBins/eta_ratio")
h_MU50_BCDEF_abseta_pt_ratio = muSFTrigger_AtoF.Get("Mu50_OR_TkMu50_PtEtaBins/abseta_pt_ratio")
h_MU50_BCDEF_pt_abseta_ratio = muSFTrigger_AtoF.Get("Mu50_OR_TkMu50_PtEtaBins/pt_abseta_ratio")
h_MU50_BCDEF_pt_ratio = muSFTrigger_AtoF.Get("Mu50_OR_TkMu50_PtBins/pt_ratio")

#Trigger Mu24
h_MU24_GH_eta_ratio = muSFTrigger_GtoH.Get("IsoMu24_OR_IsoTkMu24_EtaBins/eta_ratio")
h_MU24_GH_abseta_pt_ratio = muSFTrigger_GtoH.Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio")
h_MU24_GH_pt_abseta_ratio = muSFTrigger_GtoH.Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio")
h_MU24_GH_pt_ratio = muSFTrigger_GtoH.Get("IsoMu24_OR_IsoTkMu24_PtBins/pt_ratio")

#Trigger Mu 50
h_MU50_GH_eta_ratio = muSFTrigger_GtoH.Get("Mu50_OR_TkMu50_EtaBins/eta_ratio")
h_MU50_GH_abseta_pt_ratio = muSFTrigger_GtoH.Get("Mu50_OR_TkMu50_PtEtaBins/abseta_pt_ratio")
h_MU50_GH_pt_abseta_ratio = muSFTrigger_GtoH.Get("Mu50_OR_TkMu50_PtEtaBins/pt_abseta_ratio")
h_MU50_GH_pt_ratio = muSFTrigger_GtoH.Get("Mu50_OR_TkMu50_PtBins/pt_ratio")

### Scale Run BCDEF #####

#Trigger Mu 24
h_MU24_BCDEF_eta_ratio.Scale(lumi_BCDEF)
h_MU24_BCDEF_abseta_pt_ratio.Scale(lumi_BCDEF) 
h_MU24_BCDEF_pt_abseta_ratio.Scale(lumi_BCDEF)
h_MU24_BCDEF_pt_ratio.Scale(lumi_BCDEF) 

#Trigger Mu 50
h_MU50_BCDEF_eta_ratio.Scale(lumi_BCDEF)
h_MU50_BCDEF_abseta_pt_ratio.Scale(lumi_BCDEF) 
h_MU50_BCDEF_pt_abseta_ratio.Scale(lumi_BCDEF)
h_MU50_BCDEF_pt_ratio.Scale(lumi_BCDEF)


### Scale Run GH #####

#Trigger Mu 24
h_MU24_GH_eta_ratio.Scale(lumi_GH)
h_MU24_GH_abseta_pt_ratio.Scale(lumi_GH) 
h_MU24_GH_pt_abseta_ratio.Scale(lumi_GH)
h_MU24_GH_pt_ratio.Scale(lumi_GH) 

#Trigger Mu 50
h_MU50_GH_eta_ratio.Scale(lumi_GH)
h_MU50_GH_abseta_pt_ratio.Scale(lumi_GH) 
h_MU50_GH_pt_abseta_ratio.Scale(lumi_GH)
h_MU50_GH_pt_ratio.Scale(lumi_GH)



### Add histograms Run BCDEF + GH #####
#Trigger Mu 24
h_MU24_BCDEF_eta_ratio.Add(h_MU24_GH_eta_ratio)
h_MU24_BCDEF_abseta_pt_ratio.Add(h_MU24_GH_abseta_pt_ratio)
h_MU24_BCDEF_pt_abseta_ratio.Add(h_MU24_GH_pt_abseta_ratio)
h_MU24_BCDEF_pt_ratio.Add(h_MU24_GH_pt_ratio)

#Trigger Mu 50
h_MU50_BCDEF_eta_ratio.Add(h_MU50_GH_eta_ratio)
h_MU50_BCDEF_abseta_pt_ratio.Add(h_MU50_GH_abseta_pt_ratio)
h_MU50_BCDEF_pt_abseta_ratio.Add(h_MU50_GH_pt_abseta_ratio)
h_MU50_BCDEF_pt_ratio.Add(h_MU50_GH_pt_ratio)


###  Save new histogramms as new histogramms
#Trigger Mu 24
new_MU24_eta_ratio = h_MU24_BCDEF_eta_ratio
new_MU24_abseta_pt_ratio = h_MU24_BCDEF_abseta_pt_ratio
new_MU24_pt_abseta_ratio = h_MU24_BCDEF_pt_abseta_ratio
new_MU24_pt_ratio = h_MU24_BCDEF_pt_ratio

#Trigger Mu 50
new_MU50_eta_ratio = h_MU50_BCDEF_eta_ratio
new_MU50_abseta_pt_ratio = h_MU50_BCDEF_abseta_pt_ratio
new_MU50_pt_abseta_ratio = h_MU50_BCDEF_pt_abseta_ratio
new_MU50_pt_ratio = h_MU50_BCDEF_pt_ratio


### Scale new Histogramms to total lumi ##########

#Trigger Mu 24
new_MU24_eta_ratio.Scale(1/lumi_tot) 
new_MU24_abseta_pt_ratio .Scale(1/lumi_tot) 
new_MU24_pt_abseta_ratio.Scale(1/lumi_tot) 
new_MU24_pt_ratio.Scale(1/lumi_tot) 
  
#Trigger Mu 50
new_MU50_eta_ratio.Scale(1/lumi_tot) 
new_MU50_abseta_pt_ratio .Scale(1/lumi_tot) 
new_MU50_pt_abseta_ratio .Scale(1/lumi_tot) 
new_MU50_pt_ratio.Scale(1/lumi_tot)

##### Save new histogramms in new file ###########

#Trigger Mu 24
dir1 = outFile_Trigger.mkdir("IsoMu24_OR_IsoTkMu24_EtaBins")
dir1.cd()
new_MU24_eta_ratio.Write()

dir2 = outFile_Trigger.mkdir("IsoMu24_OR_IsoTkMu24_PtEtaBins")
dir2.cd()
new_MU24_abseta_pt_ratio.Write() 
new_MU24_pt_abseta_ratio.Write() 

dir3 = outFile_Trigger.mkdir("IsoMu24_OR_IsoTkMu24_PtBins")
dir3.cd()
new_MU24_pt_ratio.Write() 
  
#Trigger Mu 50
dir4 = outFile_Trigger.mkdir("Mu50_OR_TkMu50_EtaBins")
dir4.cd()
new_MU50_eta_ratio.Write() 
  
dir5 = outFile_Trigger.mkdir("Mu50_OR_TkMu50_PtEtaBins")
dir5.cd()
new_MU50_abseta_pt_ratio.Write() 
new_MU50_pt_abseta_ratio.Write() 

dir6 = outFile_Trigger.mkdir("Mu50_OR_TkMu50_PtBins")
dir6.cd()
new_MU50_pt_ratio.Write()


outFile_Trigger.Close()
print "Muon Trigger file written:", rootDir+outfile_Name+".root"
muSFTrigger_AtoF.Close()
muSFTrigger_GtoH.Close()
