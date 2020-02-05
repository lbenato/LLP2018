#! /usr/bin/env python

import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory, gPad
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH2F, THStack, TGraph, TGraphAsymmErrors
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TBox, TGaxis

#### IMPORT SAMPLES AND VARIABLES DICTIONARIES ####

from Analyzer.LLP2018.samples import sample, samples
from Analyzer.LLP2018.variables import *
from Analyzer.LLP2018.selections import *
from Analyzer.LLP2018.drawUtils import *
#selections as string in different file?
#project and draw functions in different files?


#### PARSER ####

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
parser.add_option("-s", "--cut_s", action="store", type="string", dest="cut_s", default="")
parser.add_option("-r", "--region", action="store", type="string", dest="region", default="")
parser.add_option("-f", "--formula", action="store", type="string", dest="formula", default="")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
(options, args) = parser.parse_args()
if options.bash: gROOT.SetBatch(True)
gStyle.SetOptStat(0)

#### NTUPLE, PLOT DIRECTORIES ####

#NTUPLEDIR   = "/nfs/dust/cms/user/lbenato/v2/"
#PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v2_15Oct/"
#v3
#NTUPLEDIR   = "/nfs/dust/cms/user/lbenato/v3_b/"
#PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v3_06Nov/"
#LUMI        = 35867# in pb-1
#SIGNAL      = 10000#1#10000#10000
#POISSON     = False

# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v4/"#"DisplacedJet/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v4_14Nov/DisplacedJet/"
# #SingleMuon v4
# #LUMI        = 7478.896# in pb-1
# #LUMI        = 7380.269# in pb-1#DisplacedJet v4

# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v5/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v5_18Dec/SingleMuon/"
# LUMI        = 7533.496# in pb-1#SingleMuon v5
# #LUMI        = 7419.796# in pb-1#DisplacedJet v5

# #TRIGGER!
# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v6_trigger/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v6_trigger/SingleMuonRunG/"#RunC/"
# LUMI        = 7570.852545674# in pb-1#SingleMuonRunG v6_trigger
# #LUMI        = 2391.657804102# in pb-1#SingleMuonRunC v6_trigger

# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v6/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v6_21Mar/"#RunC/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v6_29Jul/"#RunC/"
# LUMI        = 7419.796# in pb-1#DisplacedJet v5

# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v0_met/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v0_met/"#RunC/"
# LUMI        = 5750.126252897# in pb-1#DisplacedJet v5



# #NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v0_ZH_recluster_CHS/"
# #PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v0_ZH_recluster_CHS/"
# #LUMI        = 35867#v0_ZH_recluster_CHS

# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v1_met_recluster_CHS/"
# PLOTDIR     = "/nfs/dust/cms/user/lbenato/plots/v1_met_recluster_CHS/"#RunC/"
# LUMI        = 35867#v1_met_recluster_CHS

# NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v7_short/"
# PLOTDIR     = "/nfs/dust/cms/user/eichm/plots/v7_short/"
# LUMI        = 35867#

NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v0_pfXTag_short/"
PLOTDIR     = "/nfs/dust/cms/user/eichm/plots/v0_pfXTag_short/"
LUMI        = 35867#


#SIGNAL      = 10000######LLL
SIGNAL = 100#good for met
#SIGNAL = 100000#good for ZH
#SIGNAL = 10
POISSON     = False

#### SAMPLES ####

data = ["data_obs"]
#back = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","QCD_red"]
#back = ["VV","WJetsToQQ","WJetsToLNu","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","QCD_red"]
#back = ["VV","WJetsToQQ","WJetsToLNu","DYJetsToQQ","ZJetsToNuNu","DYJetsToLL","ST","TTbar","QCD"]

#back = ["VV","ST","TTbar","QCD","WJets","DYJets"]#MET
#back = ["VV","WJets","ZJetsToNuNu","DYJetsToQQ","ST","TTbar","DYJetsToLL"]#ZH
back = [ "TTbar","QCD_red"]
sign = []
#back = data = []

#sign_b = ["VBFH_M20_ctau0","VBFH_M20_ctau0p1", "VBFH_M20_ctau1"]#
#sign_b = ["VBFH_M15_ctau0","VBFH_M15_ctau0p1", "VBFH_M15_ctau1"]
sign_b = ["VBFH_M40_ctau0","VBFH_M40_ctau0p05","VBFH_M40_ctau0p1", "VBFH_M40_ctau1"]
#sign_b = ["VBFH_M55_ctau0","VBFH_M55_ctau0p1"]
sign_track = ["VBFH_M20_ctau5","VBFH_M20_ctau10", "VBFH_M20_ctau100"]#
sign_calo = ["VBFH_M20_ctau500","VBFH_M20_ctau1000", "VBFH_M20_ctau2000"]#, "VBFH_M20_ctau5000","VBFH_M20_ctau10000",]#
sign_calo += ["VBFH_M50_ctau500"]#
#sign_calo = ["VBFH_M55_ctau500","VBFH_M55_ctau1000", "VBFH_M55_ctau2000"]#
#sign_calo = []
#MET
sign_calo = ["VBFH_M20_ctau5000","VBFH_M20_ctau1000", "VBFH_M20_ctau2000"]#, "VBFH_M20_ctau5000","VBFH_M20_ctau10000",]#
sign_calo += ["VBFH_M50_ctau5000"]#
sign_calo = ["VBFH_M20_ctau2000","ggH_M20_ctau2000","VBFH_M20_ctau5000","ggH_M20_ctau5000"]
#back = data = []
sign_calo = ["VBFH_M20_ctau2000","VBFH_M20_ctau5000"]
#sign_calo_ggH = ["ggH_M20_ctau2000","ggH_M20_ctau5000"]

#sign_calo = ["ZH_M15_ctau1000","ZH_M55_ctau10000"]#ZH

if options.region == "b":
    sign = sign_b
    SIGNAL      = 100
elif options.region == "track":
    sign = sign_track
elif options.region == "calo":
    sign = sign_calo
#    if "METTrigger" in options.cut:
#        SIGNAL = SIGNAL/10
elif options.region == "calo_ggH":
    sign = sign_calo_ggH
elif options.region == "all":#pick all signals
    for a in samples.keys():
        if "VBFH_M" in a and a!="VBFH_M25_ctau5":
            #print a
            sign.append(a)
    SIGNAL      = 100
else:
    print "No region specified, plotting without signal!"
    print "Aborting!"
    exit()


#SIGNAL = SIGNAL*10

#print sign
#exit()

#### Function not working!
#def signal_matching_string(var):
#    signal_cut_additional_string = ""
#    if "Jets.Jets" in var:
#        rest = var[0:var.index(']')+1]
#        signal_cut_additional_string = " && ( " + rest + ".pt==MatchedCHSJet1.pt || " + rest + ".pt==MatchedCHSJet2.pt || " + rest + ".pt==MatchedCHSJet3.pt || " + rest + ".pt==MatchedCHSJet4.pt ) "
#    return signal_cut_additional_string
####


def plot(var, cut, cut_s, norm=False):
    ### Preliminary Operations ###
    
    # Substitute cut
    pd = ""
    channel = ""
    plotdir = ""
    shortcut = cut
    shortcut_s = cut_s
    longcut = longcut_s = ""
    if cut in selection:
        plotdir = cut
        longcut = selection[cut]
    if cut_s in selection:
        #The function does not work.
        ################longcut_s = "Jets.Jets[0].pt>30 && Jets.Jets[0].eta<2 && Jets.Jets[0].isGenMatched>-5 && Jets.Jets[0].isMatchedToMatchedCHSJet>-2 && Jets.Jets[0].isMatchedToMatchedCHSJet<=1 "#Jets.Jets[0].isMatchedToMatchedCHSJet"#selection[cut_s] #+ " && Jets.Jets[0].isMatchedToMatchedCHSJet "# + signal_matching_string(var)
        #longcut_s = selection[cut_s] + signal_matching_string(var)
        #print "VERIFY: " , longcut_s
        longcut_s = selection[cut_s]

    # Determine Primary Dataset
    pd = getPrimaryDataset(longcut)
    if len(data)>0 and len(pd)==0: raw_input("Warning: Primary Dataset not recognized, continue?")
    
    # Determine weight
    weight = "EventWeight"
    print weight

    print "Considered ntuples: ", NTUPLEDIR
    print "Plotting", var#, "in", channel, "channel with:"
    print "  dataset:", pd
    print "  weight :", weight
    print "  cut    :", longcut
    print "  cut on signal    :", longcut_s
    suffix = ""

    for i, s in enumerate(back):
        print "back sample: ", s


    ### Create and fill MC histograms ###
    print "doing project . . . "
    hist = project(var, longcut, longcut_s, weight, data+back+sign, pd, NTUPLEDIR, formula=options.formula)
    
    # Background sum
    if len(back)>0:
        if options.blind: RATIO = False
        else: RATIO = 4
        hist['BkgSum'] = hist['data_obs'].Clone("BkgSum") if 'data_obs' in hist else hist[back[0]].Clone("BkgSum")
        hist['BkgSum'].Reset("MICES")
        hist['BkgSum'].SetFillStyle(3003)
        hist['BkgSum'].SetFillColor(1)
        for i, s in enumerate(back):
            hist['BkgSum'].Add(hist[s])
    
    if len(back)==0 and len(data)==0:
        suffix = ''
        RATIO = False
        for i, s in enumerate(sign):
            print "I won't scale signal!"
            #hist[s].Scale(1./hist[s].Integral())
            hist[s].SetFillStyle(0)
    
    if norm:
        sfnorm = hist['data_obs'].Integral()/hist['BkgSum'].Integral()
        for i, s in enumerate(back+['BkgSum']): hist[s].Scale(sfnorm)
        
    ### Plot ###

    if len(data+back)>0:
        if options.blind: RATIO = 0
        else: RATIO = 4
        out = draw(hist, data if not options.blind else [], back, sign, SIGNAL, RATIO, POISSON, variable[var]['log'])
    else:
        out = drawSignal(hist, sign,variable[var]['log'])
        out[0].SetGrid()

    # Other plot operations
    out[0].cd(1)
    drawCMS(LUMI, "Preliminary" if len(data+back)>0 else "Simulation",onTop=True,data_obs=data)
    #drawCMS(LUMI, "Work in Progress",data_obs=data)
    drawRegion(shortcut)
    drawAnalysis("LL")
    #drawAnalysis("LLZH")
    out[0].Update()
    
    # Save
    SAVE = True
    pathname = PLOTDIR+plotdir
    #if gROOT.IsBatch() and SAVE:
    if SAVE:
        if not os.path.exists(pathname): os.makedirs(pathname)
        suffix+= "_"+str(options.region)
        if len(data+back)>0:
            out[0].Print(pathname+"/"+var.replace('.', '_')+suffix+".png")
            out[0].Print(pathname+"/"+var.replace('.', '_')+suffix+".pdf")
        else:
            out[0].Print(pathname+"/"+var.replace('.', '_')+suffix+"_signal.png")
            out[0].Print(pathname+"/"+var.replace('.', '_')+suffix+"_signal.pdf")    
    ### Other operations ###
    # Print table
    if len(data+back)>0: printTable(hist, sign, SIGNAL)
    
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")


'''
##################
#    PROJECT     #
##################


def project(var, cut, cut_s, weight, samplelist, pd, ntupledir, treename="ntuple/tree"):
    # Create dict
    file = {}
    tree = {}
    chain = {}
    hist = {}
    
    ### Create and fill MC histograms ###
    for i, s in enumerate(samplelist):
        if "HIST" in cut: # Histogram written to file
            for j, ss in enumerate(samples[s]['files']):
                file[ss] = TFile(ntupledir + ss + ".root", "READ")
                hist[s] = file[ss].Get("ntuple/" + histDir[var[0:2]] + "/" + var) if not s in hist else hist[s].Add(file[ss].Get("ntuple/" + histDir[var[0:2]] + "/" + var))
        else: # Project from tree
            chain[s] = TChain(treename)
            for j, ss in enumerate(samples[s]['files']):
                if not 'data' in s or ('data' in s and ss in pd):
                    chain[s].Add(ntupledir + ss + ".root")
            if variable[var]['nbins']>0: hist[s] = TH1F(s, ";"+variable[var]['title'], variable[var]['nbins'], variable[var]['min'], variable[var]['max']) # Init histogram
            else: hist[s] = TH1F(s, ";"+variable[var]['title'], len(variable[var]['bins'])-1, array('f', variable[var]['bins']))
            hist[s].Sumw2()
            tmpcut = cut
            tmpcut_s = cut_s
            if not 'data' in s:
                if s.endswith('_0b'): tmpcut += " && nBJets==0"
                elif s.endswith('_1b'): tmpcut += " && nBJets==1"
                elif s.endswith('_2b'): tmpcut += " && nBJets>=2"
                if s.endswith('_0l'): tmpcut += " && genNl==0"
                elif s.endswith('_1l'): tmpcut += " && genNl==1"
                elif s.endswith('_2l'): tmpcut += " && genNl>=2"
            cutstring = "("+weight+")" + ("*("+tmpcut+")" if len(tmpcut)>0 else "")
            cutstring_s = "("+weight+")" + ("*("+tmpcut_s+")" if len(tmpcut_s)>0 else "")
            if s in sign:#important bugfix! Not applying jet matching to signal!
                chain[s].Project(s, var, cutstring_s)
            else:
                chain[s].Project(s, var, cutstring)
            hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
            hist[s].Scale(samples[s]['weight'] if hist[s].Integral() >= 0 else 0)
            #if s in sign:
                #print "Is it empty?"
                #print s, hist[s].Integral()

        hist[s].SetFillColor(samples[s]['fillcolor'])
        hist[s].SetFillStyle(samples[s]['fillstyle'])
        hist[s].SetLineColor(samples[s]['linecolor'])
        hist[s].SetLineStyle(samples[s]['linestyle'])
    
    if "HIST" in cut: hist["files"] = file
    return hist


##################
#      DRAW      #
##################

def draw(hist, data, back, sign, snorm=1, ratio=0, poisson=False, log=False):
    # If not present, create BkgSum
    if not 'BkgSum' in hist.keys():
        hist['BkgSum'] = hist['data_obs'].Clone("BkgSum") if 'data_obs' in hist else hist[back[0]].Clone("BkgSum")
        hist['BkgSum'].Reset("MICES")
        for i, s in enumerate(back): hist['BkgSum'].Add(hist[s])
    hist['BkgSum'].SetMarkerStyle(0)
    
    # Some style
    for i, s in enumerate(data):
        hist[s].SetMarkerStyle(21)
        hist[s].SetMarkerSize(1.25)
    for i, s in enumerate(sign):
        hist[s].SetLineWidth(3)
        
    for i, s in enumerate(data+back+sign+['BkgSum']):
        addOverflow(hist[s], False) # Add overflow
    
    # Set Poisson error bars
    #if len(data) > 0: hist['data_obs'].SetBinErrorOption(1) # doesn't work
    
    # Poisson error bars for data
    if poisson:
        alpha = 1 - 0.6827
        hist['data_obs'].SetBinErrorOption(TH1.kPoisson)
        data_graph = TGraphAsymmErrors(hist['data_obs'].GetNbinsX())
        data_graph.SetMarkerStyle(hist['data_obs'].GetMarkerStyle())
        data_graph.SetMarkerSize(hist['data_obs'].GetMarkerSize())
        res_graph = data_graph.Clone()
        for i in range(hist['data_obs'].GetNbinsX()):
            N = hist['data_obs'].GetBinContent(i+1)
            B = hist['BkgSum'].GetBinContent(i+1)
            L =  0 if N==0 else ROOT.Math.gamma_quantile(alpha/2,N,1.)
            U =  ROOT.Math.gamma_quantile_c(alpha/2,N+1,1)
            data_graph.SetPoint(i, hist['data_obs'].GetXaxis().GetBinCenter(i+1), N if not N==0 else -1.e99)
            data_graph.SetPointError(i, hist['data_obs'].GetXaxis().GetBinWidth(i+1)/2., hist['data_obs'].GetXaxis().GetBinWidth(i+1)/2., N-L, U-N)
            res_graph.SetPoint(i, hist['data_obs'].GetXaxis().GetBinCenter(i+1), N/B if not B==0 and not N==0 else -1.e99)
            res_graph.SetPointError(i, hist['data_obs'].GetXaxis().GetBinWidth(i+1)/2., hist['data_obs'].GetXaxis().GetBinWidth(i+1)/2., (N-L)/B if not B==0 else -1.e99, (U-N)/B if not B==0 else -1.e99)
    
    
    # Create stack
    bkg = THStack("Bkg", ";"+hist['BkgSum'].GetXaxis().GetTitle()+";Events")
    for i, s in enumerate(back): bkg.Add(hist[s])
    
    # Legend
    n = len([x for x in data+back+['BkgSum']+sign if samples[x]['plot']])
    for i, s in enumerate(sign):
        if 'sublabel' in samples[s]: n+=1
        if 'subsublabel' in samples[s]: n+=1
    leg = TLegend(0.68, 0.9-0.05*n, 0.93, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    if len(data) > 0:
        leg.AddEntry(hist[data[0]], samples[data[0]]['label'], "ple1")
    for i, s in reversed(list(enumerate(['BkgSum']+back))):
        leg.AddEntry(hist[s], samples[s]['label'], "f")    
    for i, s in enumerate(sign):
        leg.AddEntry(hist[s], samples[s]['label'], "f")

    
    # --- Display ---
    c1 = TCanvas("c1", hist.values()[-1].GetXaxis().GetTitle(), 1000, 800 if ratio else 700)
    
    if ratio:
        c1.Divide(1, 2)
        setTopPad(c1.GetPad(1), ratio)
        setBotPad(c1.GetPad(2), ratio)
    c1.cd(1)
    c1.GetPad(bool(ratio)).SetTopMargin(0.06)
    c1.GetPad(bool(ratio)).SetRightMargin(0.05)
    c1.GetPad(bool(ratio)).SetTicks(1, 1)
    if log:
        c1.GetPad(bool(ratio)).SetLogy()
        #c1.GetPad(bool(ratio)).SetLogx()
        
    # Draw
    bkg.Draw("HIST") # stack
    hist['BkgSum'].Draw("SAME, E2") # sum of bkg
    if poisson: data_graph.Draw("SAME, PE")
    elif len(data) > 0: hist['data_obs'].Draw("SAME, PE")
    for i, s in enumerate(sign):
        if samples[s]['plot']:
            hist[s].DrawNormalized("SAME, HIST", hist[s].Integral()*snorm) # signals

    bkg.GetYaxis().SetTitleOffset(bkg.GetYaxis().GetTitleOffset()*1.075)

    # Determine range
    if 'data_obs' in hist:
        bkg.SetMaximum((2.5 if log else 1.2)*max(bkg.GetMaximum(), hist['data_obs'].GetBinContent(hist['data_obs'].GetMaximumBin())+hist['data_obs'].GetBinError(hist['data_obs'].GetMaximumBin())))
        bkg.SetMinimum(max(min(hist['BkgSum'].GetBinContent(hist['BkgSum'].GetMinimumBin()), hist['data_obs'].GetMinimum()), 5.e-1)  if log else 0.)
    else:
        bkg.SetMaximum(bkg.GetMaximum()*(2.5 if log else 1.2))
        bkg.SetMinimum(5.e-1 if log else 0.)
    if log:
        bkg.GetYaxis().SetNoExponent(bkg.GetMaximum() < 1.e4)
        bkg.GetYaxis().SetMoreLogLabels(True)
    
    leg.Draw()
    drawCMS(LUMI, "Preliminary")
    #drawRegion(channel)
    drawAnalysis("LL")
    
    setHistStyle(bkg, 1.2 if ratio else 1.1)
    setHistStyle(hist['BkgSum'], 1.2 if ratio else 1.1)

    if ratio:
        c1.cd(2)
        err = hist['BkgSum'].Clone("BkgErr;")
        err.SetTitle("")
        err.GetYaxis().SetTitle("Data / Bkg")
        for i in range(1, err.GetNbinsX()+1):
            err.SetBinContent(i, 1)
            if hist['BkgSum'].GetBinContent(i) > 0:
                err.SetBinError(i, hist['BkgSum'].GetBinError(i)/hist['BkgSum'].GetBinContent(i))
        setBotStyle(err)
        errLine = err.Clone("errLine")
        errLine.SetLineWidth(2)
        errLine.SetFillStyle(0)
        errLine.SetLineColor(2)#L#
        errLine.SetLineStyle(2)#L#
        #err.GetXaxis().SetLabelOffset(err.GetXaxis().GetLabelOffset()*5)
        #err.GetXaxis().SetTitleOffset(err.GetXaxis().GetTitleOffset()*2)
        err.Draw("E2")
        errLine.Draw("SAME, HIST")
        if 'data_obs' in hist:
            res = hist['data_obs'].Clone("Residues")
            for i in range(0, res.GetNbinsX()+1):
                if hist['BkgSum'].GetBinContent(i) > 0: 
                    res.SetBinContent(i, res.GetBinContent(i)/hist['BkgSum'].GetBinContent(i))
                    res.SetBinError(i, res.GetBinError(i)/hist['BkgSum'].GetBinContent(i))
            setBotStyle(res)
            if poisson: res_graph.Draw("SAME, PE0")
            else: res.Draw("SAME, PE0")
            if len(err.GetXaxis().GetBinLabel(1))==0: # Bin labels: not a ordinary plot
                drawRatio(hist['data_obs'], hist['BkgSum'])
                drawKolmogorov(hist['data_obs'], hist['BkgSum'])
        else: res = None
    c1.Update()
    
    # return list of objects created by the draw() function
    return [c1, bkg, leg, err if ratio else None, errLine if ratio else None, res if ratio else None, data_graph if poisson else None, res_graph if poisson else None]




def drawSignal(hist, sign, log=False):
    
    # Legend
    n = len(sign)
    leg = TLegend(0.7, 0.9-0.05*n, 0.95, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for i, s in enumerate(sign): leg.AddEntry(hist[s], samples[s]['label'], "fl")
    
    
    # --- Display ---
    c1 = TCanvas("c1", hist.values()[-1].GetXaxis().GetTitle(), 800, 600)
    
    c1.cd(1)
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    if log:
        c1.GetPad(0).SetLogy()
        
    # Draw
    for i, s in enumerate(sign): 
        hist[s].SetLineWidth(3)
        hist[s].Draw("SAME, HIST" if i>0 else "HIST") # signals
    
    #hist[sign[0]].GetXaxis().SetRangeUser(0., 1500)
    hist[sign[0]].GetYaxis().SetTitleOffset(hist[sign[-1]].GetYaxis().GetTitleOffset()*1.075)
    hist[sign[0]].SetMaximum(max(hist[sign[0]].GetMaximum(), hist[sign[-1]].GetMaximum())*1.25)
    hist[sign[0]].SetMinimum(0.)
    
    if log:
        hist[sign[0]].GetYaxis().SetNoExponent(hist[sign[0]].GetMaximum() < 1.e4)
        hist[sign[0]].GetYaxis().SetMoreLogLabels(True)
    
    leg.Draw()
    drawCMS(LUMI, "Preliminary")
    
    c1.Update()
    
    # return list of objects created by the draw() function
    return [c1, leg]

def drawRatio(data, bkg):
    errData = array('d', [1.0])
    errBkg = array('d', [1.0])
    intData = data.IntegralAndError(1, data.GetNbinsX(), errData)
    intBkg = bkg.IntegralAndError(1, bkg.GetNbinsX(), errBkg)
    ratio = intData / intBkg if intBkg!=0 else 0.
    error = math.hypot(errData[0]*ratio/intData,  errBkg[0]*ratio/intBkg) if intData>0 and intBkg>0 else 0
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextColor(1)
    latex.SetTextFont(62)
    latex.SetTextSize(0.08)
    latex.DrawLatex(0.25, 0.85, "Data/Bkg = %.3f #pm %.3f" % (ratio, error))
    print "  Ratio:\t%.3f +- %.3f" % (ratio, error)
    #return [ratio, error]

def drawKolmogorov(data, bkg):
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextColor(1)
    latex.SetTextFont(62)
    latex.SetTextSize(0.08)
    latex.DrawLatex(0.55, 0.85, "#chi^{2}/ndf = %.2f,   K-S = %.3f" % (data.Chi2Test(bkg, "CHI2/NDF"), data.KolmogorovTest(bkg)))

def printTable(hist, sign=[]):
    samplelist = [x for x in hist.keys() if not 'data' in x and not 'BkgSum' in x and not x in sign and not x=="files"]
    print "Sample                  Events          Entries         %"
    print "-"*80
    for i, s in enumerate(['data_obs']+samplelist+['BkgSum']):
        if i==1 or i==len(samplelist)+1: print "-"*80
        print "%-20s" % s, "\t%-10.2f" % hist[s].Integral(), "\t%-10.0f" % (hist[s].GetEntries()-2), "\t%-10.2f" % (100.*hist[s].Integral()/hist['BkgSum'].Integral()) if hist['BkgSum'].Integral() > 0 else 0, "%"
    print "-"*80
    #for i, s in enumerate(sign):
    for s in sorted(sign):
        if not samples[s]['plot']: continue
        print "%-20s" % s, "\t%-10.2f" % (hist[s].Integral()*SIGNAL), "\t%-10.0f" % (hist[s].GetEntries()-2), "\t%-10.2f" % (100.*hist[s].GetEntries()/float(hist[s].GetOption())) if float(hist[s].GetOption()) > 0 else 0, "%"    
    print "-"*80




##################
#     OTHERS     #
##################

def getPrimaryDataset(cut):
    pd = []
#    if 'HLT_PFMET' in cut: pd += [x for x in samples['data_obs']['files'] if "MET" in x]
#    if 'HLT_' in cut: pd += [x for x in samples['data_obs']['files'] if "MET" in x]
    pd += [x for x in samples['data_obs']['files'] if "MET" in x]
    return pd


def addOverflow(hist, addUnder=True):
    n = hist.GetNbinsX()
    hist.SetBinContent(n, hist.GetBinContent(n) + hist.GetBinContent(n+1))
    hist.SetBinError(n, math.sqrt( hist.GetBinError(n)**2 + hist.GetBinError(n+1)**2 ) )
    hist.SetBinContent(n+1, 0.)
    hist.SetBinError(n+1, 0.)
    if addUnder:
        hist.SetBinContent(1, hist.GetBinContent(0) + hist.GetBinContent(1))
        hist.SetBinError(1, math.sqrt( hist.GetBinError(0)**2 + hist.GetBinError(1)**2 ) )
        hist.SetBinContent(0, 0.)
        hist.SetBinError(0, 0.)

def setTopPad(TopPad, r=4):
    TopPad.SetPad("TopPad", "", 0., 1./r, 1.0, 1.0, 0, -1, 0)
    TopPad.SetTopMargin(0.24/r)
    TopPad.SetBottomMargin(0.04/r)
    TopPad.SetRightMargin(0.05)
    TopPad.SetTicks(1, 1)

def setBotPad(BotPad, r=4):
    BotPad.SetPad("BotPad", "", 0., 0., 1.0, 1./r, 0, -1, 0)
    BotPad.SetTopMargin(r/100.)
    BotPad.SetBottomMargin(r/10.)
    BotPad.SetRightMargin(0.05)
    BotPad.SetTicks(1, 1)

def setHistStyle(hist, r=1.1):
    hist.GetXaxis().SetTitleSize(hist.GetXaxis().GetTitleSize()*r*r)
    hist.GetYaxis().SetTitleSize(hist.GetYaxis().GetTitleSize()*r*r)
    hist.GetXaxis().SetLabelSize(hist.GetXaxis().GetLabelSize()*r)
    hist.GetYaxis().SetLabelSize(hist.GetYaxis().GetLabelSize()*r)
    hist.GetXaxis().SetLabelOffset(hist.GetXaxis().GetLabelOffset()*r*r*r*r)
    hist.GetXaxis().SetTitleOffset(hist.GetXaxis().GetTitleOffset()*r)
    hist.GetYaxis().SetTitleOffset(hist.GetYaxis().GetTitleOffset())
    if hist.GetXaxis().GetTitle().find("GeV") != -1: # and not hist.GetXaxis().IsVariableBinSize()
        div = (hist.GetXaxis().GetXmax() - hist.GetXaxis().GetXmin()) / hist.GetXaxis().GetNbins()
        hist.GetYaxis().SetTitle("Events / %.1f GeV" % div)

def setBotStyle(h, r=4, fixRange=True):
    h.GetXaxis().SetLabelSize(h.GetXaxis().GetLabelSize()*(r-1));
    h.GetXaxis().SetLabelOffset(h.GetXaxis().GetLabelOffset()*(r-1));
    h.GetXaxis().SetTitleSize(h.GetXaxis().GetTitleSize()*(r-1));
    h.GetYaxis().SetLabelSize(h.GetYaxis().GetLabelSize()*(r-1));
    h.GetYaxis().SetNdivisions(505);
    h.GetYaxis().SetTitleSize(h.GetYaxis().GetTitleSize()*(r-1));
    h.GetYaxis().SetTitleOffset(h.GetYaxis().GetTitleOffset()/(r-1));
    if fixRange:
        h.GetYaxis().SetRangeUser(0., 2.)
        for i in range(1, h.GetNbinsX()+1):
            if h.GetBinContent(i)<1.e-6:
                h.SetBinContent(i, -1.e-6)

##################
### DRAW UTILS ###
##################

def drawCMS(LUMI, text, onTop=False, left_marg_CMS=0.15):
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    if (type(LUMI) is float or type(LUMI) is int) and float(LUMI) > 0: latex.DrawLatex(0.95, 0.985, "%.1f fb^{-1}  (13 TeV)" % (float(LUMI)/1000.))
    elif type(LUMI) is str: latex.DrawLatex(0.95, 0.985, "%s fb^{-1}  (13 TeV)" % LUMI)
    if not onTop: latex.SetTextAlign(11)
    latex.SetTextFont(62)
    latex.SetTextSize(0.05 if len(text)>0 else 0.06)
    if not onTop: latex.DrawLatex(left_marg_CMS, 0.87 if len(text)>0 else 0.84, "CMS")
    else: latex.DrawLatex(0.20, 0.99, "CMS")
    latex.SetTextSize(0.04)
    latex.SetTextFont(52)
    if not onTop: latex.DrawLatex(left_marg_CMS, 0.83, text)
    else: latex.DrawLatex(0.40, 0.98, text)

def drawAnalysis(s, center=False):
    analyses = {"LL" : "VBF H #rightarrow #pi #pi #rightarrow b#bar{b} b#bar{b}",}
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.SetTextFont(42)
    #latex.SetTextAlign(33)
    latex.DrawLatex(0.15 if not center else 0.3, 0.95, s if not s in analyses else analyses[s])

def drawRegion(channel, left=False, left_marg_CMS=0.15):
    region = {"VBFtrigger": "VBF triggers","VBF": "VBF"}
    
    text = ""
    if channel in region:
        text = region[channel]
#    #not set yet..
#    #else:
#        # leptons
#        if 'ee' in channel: text += "2e"
    else:
        #return False
        text = ""
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextFont(72) #52
    latex.SetTextSize(0.035)
    if left: latex.DrawLatex(left_marg_CMS, 0.75, text)
    else:
        latex.SetTextAlign(22)
        latex.DrawLatex(0.5, 0.85, text)


def drawBox(x1, y1, x2, y2, t="", fillstyle=3005):
    box = TBox(x1, y1, x2, y2)
    box.SetFillColor(1)
    box.SetFillStyle(fillstyle)
    box.Draw()
    if not t=="":
        text = TLatex()
        text.SetTextColor(1)
        text.SetTextFont(42)
        text.SetTextAlign(23)
        text.SetTextSize(0.04)
        text.DrawLatex((x1+x2)/2., y2/1.15, t)
        text.Draw()
    return box

def drawLine(x1, y1, x2, y2,color=1):
    line = TLine(x1, y1, x2, y2)
    line.SetLineStyle(2)
    line.SetLineWidth(2)
    line.SetLineColor(color)
    line.Draw()
    return line

def drawText(x, y, t, col=1):
    text = TLatex()
    text.SetTextColor(col)
    text.SetTextFont(42)
    text.SetTextAlign(23)
    text.SetTextSize(0.04)
    text.DrawLatex(x, y, t)
    text.Draw()
    return text
'''


plot(options.variable, options.cut, options.cut_s)
