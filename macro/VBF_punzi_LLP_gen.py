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
#from Analyzer.LLP2018.skimmed_variables import *

### comment:
### updated Punzi macro according to STATCOM recommendation: https://twiki.cern.ch/twiki/bin/view/CMS/PunziFom


########## SETTINGS ##########

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-v", "--variable", action="store", type="string", dest="variable", default="")
parser.add_option("-c", "--cut", action="store", type="string", dest="cut", default="")
parser.add_option("-r", "--region", action="store", type="string", dest="region", default="")
parser.add_option("-a", "--all", action="store_true", default=False, dest="all")
parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
parser.add_option("-B", "--blind", action="store_true", default=False, dest="blind")
parser.add_option("-f", "--final", action="store_true", default=False, dest="final")
(options, args) = parser.parse_args()
if options.bash:
    gROOT.SetBatch(True)

########## SETTINGS ##########

gStyle.SetOptStat(0)

NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v1_gen_production_calo/"
OUTPUTDIR   = "$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/v1_gen_production_calo/"

LUMI        = 35867 # in pb-1
SIGNAL      = 1.
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
BLIND       = False
POISSON     = False
verbose     = False
verbose_add = False
jobs        = []
CHANNEL     = "ggH"#"VBFH"#
CHANNEL     = "VBFH"

########## SAMPLES ##########
sign = [
#    'VBFH_M15_ctau100','VBFH_M15_ctau500','VBFH_M15_ctau1000','VBFH_M15_ctau2000','VBFH_M15_ctau5000','VBFH_M15_ctau10000',
    'VBFH_M20_ctau100','VBFH_M20_ctau500','VBFH_M20_ctau1000','VBFH_M20_ctau2000','VBFH_M20_ctau5000','VBFH_M20_ctau10000',
#    'VBFH_M40_ctau100','VBFH_M40_ctau500','VBFH_M40_ctau1000','VBFH_M40_ctau2000','VBFH_M40_ctau5000','VBFH_M40_ctau10000',
    ]
back = ["VV","WJetsToLNu","DYJetsToLL","ZJetsToNuNu","ST","TTbar","QCD"]
colors = [4, 410, 856, 2, 634, 1, 881, 798, 602, 921, 870, 906, 838, 420, 398]
markers = [24,26,25,32,28,30,27,24,26,25,32,28,30,27,24,26]
back = []
########## ######## ##########

#gROOT.SetBatch(True)


def calc_punzi_FOM_vs_ctau(cutlist, labellist=[],mass_point=40,additional_string="",alpha=2,CL=5,FOM='punzi',header=""):
    file = {}
    nevt = {}
    tree = {}
    effs = {}
    chain = {}
    hist = {}
    eff_dict = { k:{} for k in cutlist}
    back_int = { k:{} for k in cutlist}
    back_int_weight = { k:{} for k in cutlist}
    back_eff = { k:{} for k in cutlist}
    punzi_dict = { k:{} for k in cutlist}
    graph = {}
    back_graph = {}
    ncuts = len(cutlist)
    if labellist == []:
        labellist=cutlist
    print NTUPLEDIR
    print "............."
    #prepare ctau ordered array for 1D plot                                                                
    mass_array = []
    ctau_array = []


    #for signal we have the normal efficiency                                                               
    for i, s in enumerate(sign):
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile                  
        tree[s] = file[s].Get("ntuple/tree") # Read TTree       
        nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)# all gen events before cuts!
        #tree[s] = file[s].Get("skim") # Read TTree       
        #nevt[s] = tree[s].GetEntries("")#if the tree is skimmed, this becomes a relative denominator
        #nevt[s] = (file[s].Get('c_nEvents')).GetBinContent(1)# all gen events before cuts!
        filename = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ")
        if verbose_add: print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        if verbose_add: print filename
        if verbose_add: print "x-check: n gen events in counter, first bin:"
        if verbose_add: print (filename.Get('c_nEvents')).GetBinContent(1)
        if verbose_add: print "x-check: n entries in counter:"
        if verbose_add: print (filename.Get('c_nEvents')).GetEntries()
        effs[s] = [0]*(ncuts+1)
        effs[s] = [0]*(ncuts+1)
        weight = "1"#"EventWeight"
        var = "isMC"

        if samples[s]['mass'] not in mass_array:
            mass_array.append(samples[s]['mass'])
        if samples[s]['ctau'] not in ctau_array:
            ctau_array.append(samples[s]['ctau'])
        for j, c in enumerate(cutlist):
            tot_gen = nevt[s]
            n = tree[s].GetEntries("(" + cutlist[j] + ")")

            #wat?#test_op = cutlist[j] + " && number_of_matched_Jets>=1"
            #wat?#n = tree[s].GetEntries("(" + test_op + ")")

            ###BUGFIX: efficiency should be computed w.r.t. histo integral
            #hist[s+"_cut"+str(j)] = TH1F(s+"_cut"+str(j), ";"+variable[var]['title'], variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
            #hist[s+"_cut"+str(j)].Sumw2()
            #cutstring = "("+weight+")" + ("*("+cutlist[j]+")" if len(cutlist[j])>0 else "")
            #tree[s].Project(s+"_cut"+str(j), var, cutstring)
            #hist[s+"_cut"+str(j)].SetOption("%s" % tree[s].GetTree().GetEntriesFast())


            if verbose_add: print '\n'
            if verbose_add: print '**********************************************'
            if verbose_add: print "cut: ", c
            if verbose_add: print 'over signal ', s
            if verbose_add: print '\n'
            if verbose_add: print "signal num: ", n
            if verbose_add: print "signal den: ", tot_gen
            #if verbose_add: print "BUGFIX!!!!!!!!!!!"
            #if verbose: print "BUGFIX!!!!!!!!!!!"
            #if verbose_add: print "signal num from integral: ", hist[s+"_cut"+str(j)].Integral()
            #if verbose_add: print "signal den from generator: ", tot_gen
            #if verbose: print "BUGFIX!!!!!!!!!!!"
            if verbose_add: print ("signal eff %.2f") % (float(n)/(tot_gen)*100)
            if tot_gen==0:
                effs[s][j] = float(0.)
            else:
                effs[s][j] = (float(n)/(tot_gen))
            eff_dict[c][s] = {'mass' : samples[s]['mass'], 'ctau' : samples[s]['ctau'], 'eff' :effs[s][j], 'nevents' : n}


    #sort mass array
    masses = np.array(mass_array)
    masses.sort()

    ctaus = np.array(ctau_array)
    ctaus.sort()


    #define multigraph
    mg = TMultiGraph()
    #leg = TLegend(0.78, 0.7, 0.98, 0.98)
    #leg2 = TLegend(0., 0.4, 0.98, 0.98)
    #leg2 = TLegend(0.3, 0.11, 0.65, 0.45)#DCMS,gen matching
    leg2 = TLegend(0.4, 0.11, 0.85, 0.45)#DCMS,summary plot
    leg2 = TLegend(0.4-0.3, 0.11+0.43, 0.85+0.05-0.3, 0.45+0.43)#EXO,summary plot
    leg2 = TLegend(0.4, 0.11, 0.85+0.05, 0.45)#EXO,summary plot

    leg3 = TLegend(0., 0.5, 0.5, 1.)#2 plots

    leg = TLegend(0., 0.4, 0.98, 0.98)
    leg.SetTextSize(0.03)
    leg2.SetTextSize(0.03)
    leg2.SetTextSize(0.025)
    leg.SetBorderSize(0)
    leg2.SetBorderSize(0)
    leg.SetHeader("Signal: m_{#pi}=" +str(mass_point)+" GeV")
    leg2.SetHeader("Signal: m_{#pi}=" +str(mass_point)+" GeV")

    leg3.SetTextSize(0.03)
    leg3.SetTextSize(0.025)
    leg3.SetBorderSize(0)
    leg3.SetHeader("Signal: m_{#pi}=" +str(mass_point)+" GeV")


    #for background let's first consider the cut
    for j, c in enumerate(cutlist):
        print '\n'
        print "cut: ", c
        print 'over background'
        print '\n'
        #then loop over background
        integral = 0
        weighted_integral = 0
        back_tot_events = 0
        for i, s in enumerate(back):
            chain[s] = TChain("ntuple/tree")
            #chain[s] = TChain("skim")
            #print "back: ", s
            back_file = {}
            for p, ss in enumerate(samples[s]['files']):
                back_file[ss] = TFile(NTUPLEDIR + ss + ".root", "READ") # Read TFile                  
                #?#if verbose: print "file: ", ss
                #?#if verbose: print "gen events: ", (back_file[ss].Get('counter/c_nEvents')).GetBinContent(1)
                #?#if verbose: print "tree events: ", (back_file[ss].Get('ntuple/tree')).GetEntries()
                back_tot_events += (back_file[ss].Get('counter/c_nEvents')).GetBinContent(1)
                #back_tot_events += (back_file[ss].Get('c_nEvents')).GetBinContent(1)
                chain[s].Add(NTUPLEDIR + ss + ".root")
            #print "MODIFIED WEIGHT!!!!!!"
            #weight = ("EventWeight*%s/5000." % str(back_tot_events))
            weight = "EventWeight"
            #var = "nCHSJets"
            var = "isMC"
            hist[s] = TH1F(s, ";"+variable[var]['title'], variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
            hist[s].Sumw2()
            cutstring = "("+weight+")" + ("*("+cutlist[j]+")" if len(cutlist[j])>0 else "")
            chain[s].Project(s, var, "")#"1*"+"("+weight+")")
            hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
            #if verbose: print "Hist content, no cut:"
            #if verbose: print hist[s].Print()
            #?#if verbose: print "events in the histo with get entries with empty project: ", hist[s].GetEntries()
            #?#if verbose: print "area under histo with empty project: ", hist[s].Integral()
            chain[s].Project(s, var, cutstring)#"1*"+"("+weight+")")
            hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
            hist[s].Scale(samples[s]['weight'] if hist[s].Integral() >= 0 else 0)
            #?#if verbose: print "events in the histo with get entries after project: ", hist[s].GetEntries()
            #?#if verbose: print "area under histo after project: ", hist[s].Integral()
            if verbose: print "Hist content, with cut:"
            if verbose: print hist[s].Print()
            integral += hist[s].GetEntries()
            weighted_integral += hist[s].Integral()
        back_int[c] = integral
        back_int_weight[c] = weighted_integral
        if back_tot_events==0:
            back_eff[c] = float(0.)
        else:
            back_eff[c] = float(integral)/float(back_tot_events)
        if verbose: print "cut: ", c
        if verbose: print "back tot events (unweighted):", back_tot_events
        if verbose: print "back integral (unweighted): ", back_int[c]
        if verbose: print "back integral (weighted): ", back_int_weight[c]
        if verbose: print "back eff (unweighted): ", back_eff[c]*100
        if FOM=="signaleff":
            punzi_dict[c]['back'] = {'back' : back_eff[c]*100}
        for i, s in enumerate(sign):
            if verbose: print "signal efficiency: ", eff_dict[c][s]['eff']*100
            if FOM=="punzi":
                punzi_dict[c][s] = {'sign': eff_dict[c][s]['eff']/(CL**2/2. + alpha*math.sqrt(back_int_weight[c]) + (CL/2.)*math.sqrt(CL**2 + 4*alpha*math.sqrt(back_int_weight[c]) + 4*back_int_weight[c]))}
            elif FOM=="signaleff":
                punzi_dict[c][s] = {'sign': eff_dict[c][s]['eff']*100}
            elif FOM=="entries":
                punzi_dict[c][s] = {'sign': eff_dict[c][s]['nevents']}
            else:
                print "not punzi FOM, aborting!"
                exit()

    if FOM=="signaleff":
        dummy = TGraph()#len(ct),ct, np.array(ct))
        dummy.SetMarkerStyle(0)
        dummy.SetLineWidth(2)
        dummy.SetMarkerSize(1.)
        dummy.SetLineColor(15)
        dummy.SetLineStyle(2)
        if header!="":
            leg2.AddEntry(dummy, header,'')
            leg3.AddEntry(dummy, header,'')


    #for each cut, we need a graph                                                                          
    for j, c in enumerate(cutlist):
    #first let's build the ordered punzi vector w.r.t. masses, for a chosen ctau                            
        punzi_array = []
        back_array = []
        for la in ctaus:
            #la = str(a)
            if la== 0.001:
                st = CHANNEL+"_M"+str(mass_point)+"_ctau0"
            elif la==0.05 or la==0.1:
                st = CHANNEL+"_M"+str(mass_point)+"_ctau"+str(str(la).replace("0.","0p"))
            else:
                st = CHANNEL+"_M"+str(mass_point)+"_ctau"+str(int(la))
            #st = "VBFH_M"+str(mass_point)+"_ctau"+str(a)                                                        
            punzi_array.append(punzi_dict[c][st]['sign'])
        mass = array('d', masses)
        ct = array('d', ctaus)
        p_array = array('d',punzi_array)
        #graph[c] = TGraph(len(mass),mass, np.array(p_array))                                                   
        graph[c] = TGraph(len(ct),ct, np.array(p_array))
        graph[c].SetMarkerStyle(markers[j])#21
        graph[c].SetLineWidth(3)
        graph[c].SetMarkerSize(1.2)
        graph[c].SetMarkerColor(colors[j])
        graph[c].SetLineColor(colors[j])
        graph[c].SetFillColor(colors[j])
        #graph[c].SetLogx()                                                                                 

        leg.AddEntry(graph[c],labellist[j],'PL')
        leg2.AddEntry(graph[c],labellist[j],'PL')
        leg3.AddEntry(graph[c],labellist[j],'PL')
        mg.Add(graph[c])

        if FOM=="signaleff":
        #add plot for background                                                                            
            for a in ctaus:
                back_array.append(punzi_dict[c]['back']['back'])
            mass = array('d', masses)
            ct = array('d', ctaus)
            e_array = array('d',back_array)
            #back_graph[c] = TGraph(len(mass),mass, np.array(e_array))
            back_graph[c] = TGraph(len(ct),ct, np.array(e_array))
            back_graph[c].SetMarkerStyle(0)
            back_graph[c].SetLineWidth(2)
            back_graph[c].SetMarkerSize(1.)
            back_graph[c].SetMarkerColor(colors[j])
            back_graph[c].SetLineColor(colors[j])
            back_graph[c].SetLineStyle(2)
            back_graph[c].SetFillColor(colors[j])
            #back_graph[c].SetLogx()                                                                        
            #leg.AddEntry(back_graph[c],labellist[j]+" bkg.",'PL')
            #w#leg2.AddEntry(back_graph[c],labellist[j]+" bkg.",'PL')                                         
            #w#mg.Add(back_graph[c])

    if FOM=="signaleff":
        dummy = TGraph(len(ct),ct, np.array(e_array))
        dummy.SetMarkerStyle(0)
        dummy.SetLineWidth(2)
        dummy.SetMarkerSize(1.)
        dummy.SetLineColor(15)
        dummy.SetLineStyle(2)
        #w#leg2.AddEntry(dummy, 'cuts on bkg.','PL')


    #cmg = TCanvas("cmg", "cmg", 2000, 1400)
    #cmg = TCanvas("cmg", "cmg", 2000, 800)#best
    #cmg = TCanvas("cmg", "cmg", 1200, 1000)
    cmg = TCanvas("cmg", "cmg", 1300, 800)#DCMS
    cmg.cd()
    cmg.SetGrid()
    cmg.SetLogx()
    #if FOM=="signaleff":
    #    cmg.SetLogx()
    #pad1 = TPad("pad1", "pad1", 0, 0., 0.85, 1.0)
    #pad1 = TPad("pad1", "pad1", 0, 0., 0.7, 1.0)
    #pad1.SetGrid()
    #pad1.SetLogx()
    if FOM=="signaleff":
        print "LOL"
        #pad1.SetLogy()
    #pad1.SetLogy()
    #pad1.Draw()
    #pad1.cd()

    #W#if FOM=="signaleff":
        #w#mg.SetMaximum(101)
        #mg.SetMinimum(1.e-50)
    mg.SetMinimum(0.)#!!
    mg.Draw("APL")
    mg.GetXaxis().SetTitleSize(0.05)
    mg.GetYaxis().SetTitleSize(0.05)
    mg.GetXaxis().SetTitle('c#tau_{#pi} (mm)')
    mg.GetYaxis().SetTitleOffset(0.9);
    if FOM=="punzi":
        mg.GetYaxis().SetTitle('Punzi significance @ '+str(alpha)+' #sigma, '+CHANNEL+' cuts')
        #mg.GetYaxis().SetTitleOffset(1.5)
    elif FOM=="signaleff":
        #mg.GetYaxis().SetTitle('Signal efficiency, '+CHANNEL+' cuts (%)')
        mg.GetYaxis().SetTitle('Signal gen-matching efficiency, '+CHANNEL+' (%)')
    elif FOM=="entries":
        mg.GetYaxis().SetTitle('Signal entries surviving cuts')
    else:
        print "not punzi FOM, aborting"

    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.05)
    latex.SetTextColor(1)
    latex.SetTextFont(42)
    latex.SetTextAlign(33)
    latex.SetTextFont(62)
    latex.DrawLatex(0.25, 0.96, "CMS")
    latex.SetTextFont(52)
    latex.DrawLatex(0.66, 0.96, "Simulation Preliminary")
    cmg.Update()

    cmg.cd()
    leg2.SetTextSize(0.04)
    #leg.Clear()#?????????
    #w#leg2.Draw()

    #cmgL = TCanvas("cmgL", "cmgL", 2000, 800)#DCMS
    #cmgL.cd()

    #pad2 = TPad("pad2", "pad2", 0.85, 0., 1, 1.0)
    #pad2 = TPad("pad2", "pad2", 0.7, 0., 1, 1.0)
    #pad2.SetGrid()
    #pad2.SetLogx()macro/VBF_punzi_LLP_AOD.py
    #pad2.Draw()
    #pad2.cd()
    leg3.SetTextSize(0.04)
    #leg.Clear()#?????????
    leg3.Draw()
    #cmgL.Update()


    if FOM=="punzi":
        cmg.Print(OUTPUTDIR + "Punzi_correct_"+CHANNEL+"_m"+str(mass_point)+"_"+str(alpha)+"sigma"+additional_string+".pdf")
        cmg.Print(OUTPUTDIR + "Punzi_correct_"+CHANNEL+"_m"+str(mass_point)+"_"+str(alpha)+"sigma"+additional_string+".png")
        cmgL.Print(OUTPUTDIR + "Punzi_correct_"+CHANNEL+"_m"+str(mass_point)+"_"+str(alpha)+"sigma"+additional_string+"_L.pdf")
        cmgL.Print(OUTPUTDIR + "Punzi_correct_"+CHANNEL+"_m"+str(mass_point)+"_"+str(alpha)+"sigma"+additional_string+"_L.png")
    elif FOM=="signaleff":
        cmg.Print(OUTPUTDIR + "SignalEff_"+CHANNEL+"_m"+str(mass_point)+additional_string+".pdf")
        cmg.Print(OUTPUTDIR + "SignalEff_"+CHANNEL+"_m"+str(mass_point)+additional_string+".png")
        cmgL.Print(OUTPUTDIR + "SignalEff_"+CHANNEL+"_m"+str(mass_point)+additional_string+"_L.pdf")
        cmgL.Print(OUTPUTDIR + "SignalEff_"+CHANNEL+"_m"+str(mass_point)+additional_string+"_L.png")
    elif FOM=="entries":
        cmg.Print(OUTPUTDIR + "SignalEntries_"+CHANNEL+"_m"+str(mass_point)+additional_string+".pdf")
        cmg.Print(OUTPUTDIR + "SignalEntries_"+CHANNEL+"_m"+str(mass_point)+additional_string+".png")
        cmgL.Print(OUTPUTDIR + "SignalEntries_"+CHANNEL+"_m"+str(mass_point)+additional_string+"_L.pdf")
        cmgL.Print(OUTPUTDIR + "SignalEntries_"+CHANNEL+"_m"+str(mass_point)+additional_string+"_L.png")
    else:
        print "not punzi FOM, aborting"

    if not options.bash: raw_input("Press Enter to continue...")
    cmg.Close()





######
#fom = ["entries","signaleff", "punzi"]
#fom = ["punzi","signaleff"]
#fom = ["entries","punzi"]
#fom = ["entries","signaleff","punzi"]
fom = ["punzi"]
#fom = ["signaleff"]

colors = [856, 2, 881, 798, 602, 921, 870, 906, 838, 420,]
colors = [856, 2, 881, 798, 602, 921, 870, 906, 838, 801, 4, 410, 634, 1, 398, 6,7,8,9,10,11]

n_matches = 0

#CHANNEL     = "ggH"
CHANNEL     = "VBFH"

#NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v1_pfXTag_puppi_calo/"
#OUTPUTDIR   = "$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/v1_pfXTag_puppi_calo/"
#available on v1:
#back = ["VV","WJetsToLNu","ZJetsToNuNu","TTbar","QCD"]

#NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v2_pfXTag_puppi_calo/"
#OUTPUTDIR   = "$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/v2_pfXTag_puppi_calo/"
#available on v2:
back = ["VV","WJetsToLNu","ZJetsToNuNu","TTbar","QCD"]
back = []


fom = ["signaleff"]
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",
            "HLT_VBF_DisplacedJet40_VTightID_Hadronic_v",
            ],
        [
#            'Leading jet p_{T}>5 GeV',
#            'Leading jet p_{T}>10 GeV',
#            'Leading jet p_{T}>15 GeV',
#            'Sub-leading jet p_{T}>5 GeV',
#            'Sub-leading jet p_{T}>10 GeV',
#            'Sub-leading jet p_{T}>15 GeV',
            ],
        header = "",#"CHS",#str(n_matches)+" VBF jets gen matched",
        mass_point=20,#15,#50
        additional_string = "_", 
        alpha = 2,
        CL = 5,
        FOM = a
        )
exit()


#Effect of pT on gen-level matching
'''
fom = ["signaleff"]
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            "isVBF && Jets[0].pt>5 && Jets[0].isGenMatched"+" && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0  && "+selection["PFMETNoMuTrigger"],
            #"Jets.Jets[0].pt>10 && Jets.Jets[0].isGenMatched",
            "isVBF && Jets[0].pt>10 && Jets[0].isGenMatched"+" && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0  && "+selection["PFMETNoMuTrigger"],
            "isVBF && Jets[0].pt>15 && Jets[0].isGenMatched"+" && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0  && "+selection["PFMETNoMuTrigger"],
            "isVBF && Jets[1].pt>5 && Jets[1].isGenMatched"+" && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0  && "+selection["PFMETNoMuTrigger"],
            #"Jets[1].pt>10 && Jets[1].isGenMatched",
            "isVBF && Jets[1].pt>10 && Jets[1].isGenMatched"+" && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && "+selection["PFMETNoMuTrigger"],
            "isVBF && Jets[1].pt>15 && Jets[1].isGenMatched"+"  && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && "+selection["PFMETNoMuTrigger"],
            ],
        [
            'Leading jet p_{T}>5 GeV',
            'Leading jet p_{T}>10 GeV',
            'Leading jet p_{T}>15 GeV',
            'Sub-leading jet p_{T}>5 GeV',
            'Sub-leading jet p_{T}>10 GeV',
            'Sub-leading jet p_{T}>15 GeV',
            ],
        header = "CHS",#str(n_matches)+" VBF jets gen matched",
        mass_point=40,#15,#50
        additional_string = "_gen_matching_vs_pt", 
        alpha = 2,
        CL = 5,
        FOM = a
        )
'''
#exit()

#more fundamental cuts:
#increase Etmiss?
#increae met significance?
#increase min jet met d phi?
#category without puppi jets? 0 or 1?
#increase VBFPair.dEta?
#number of selected tracks?
#number of track const?
#pfXWP1000?


fom = ["punzi"]


for a in fom:
    calc_punzi_FOM_vs_ctau(
        [
            "MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],#the best at the moment
            "Jets[0].nHadEFrac>0.8 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nTrackConstituents<5 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            ],
        [
            "Pre-selections",
            "+ lead. jet nHadEFrac>0.8",
            "+ lead. jet nTracKConstituents<10",
#            "+ lead. jet nHadEFrac>0.8",
#            "+ lead. jet pfXWP1000>0.7",
#            "+ lead. jet pfXWP1000>0.8",
#            "+ lead. jet pfXWP1000>0.85",
#            "+ lead. jet pfXWP1000>0.9",
#            "+ lead. jet pfXWP1000>0.95",
            ],
        header = "",
        mass_point=15,#40#50                               
        additional_string = "_fundamental_cuts",
        alpha = 2,
        CL = 5,
        FOM = a
        )

exit()


for a in fom:
    calc_punzi_FOM_vs_ctau(
        [
            #"MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],#the best at the moment
            "MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.3 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.4 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.5 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.6 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.7 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.8 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.9 && VBFPair.dEta>3. && MinJetMetDPhi>0.3 && MEt.sign>40 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            ],
        [
#            "Pre-selections",
#            "+ 2 CHS jets nTracKConstituents<10",
#            "+ lead. jet nHadEFrac>0.8",
#            "+ lead. jet pfXWP1000>0.7",
#            "+ lead. jet pfXWP1000>0.8",
#            "+ lead. jet pfXWP1000>0.85",
#            "+ lead. jet pfXWP1000>0.9",
#            "+ lead. jet pfXWP1000>0.95",
            ],
        header = "",
        mass_point=15,#40#50                               
        additional_string = "_fundamental_cuts_pfXWP1000",
        alpha = 2,
        CL = 5,
        FOM = a
        )

exit()
###################


#back = ["VVRed","WJetsToLNu","ZJetsToNuNuRed","STRed","QCDRed"]

fom = ["punzi"]
for a in fom:
    calc_punzi_FOM_vs_ctau(
        [
            #"MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nTrackConstituents<10 && Jets[1].nTrackConstituents<10 && Jets[0].nTrackConstituents>-1 && Jets[1].nTrackConstituents>-1 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nHadEFrac>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.7 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.85 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.9 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.95 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            #"Jets[1].nHadEFrac>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[1].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[1].pfXWP1000>0.85 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[1].pfXWP1000>0.9 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[1].pfXWP1000>0.95 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            #"(Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"(Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8 || Jets[2].pfXWP1000>0.8 || Jets[3].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"(Jets[0].pfXWP1000>0.5 && Jets[1].pfXWP1000>0.5) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            ],
        [
            "Pre-selections",
            "+ 2 CHS jets nTracKConstituents<10",
            "+ lead. jet nHadEFrac>0.8",
            "+ lead. jet pfXWP1000>0.7",
            "+ lead. jet pfXWP1000>0.8",
            "+ lead. jet pfXWP1000>0.85",
            "+ lead. jet pfXWP1000>0.9",
            "+ lead. jet pfXWP1000>0.95",
            ],
        header = "",
        mass_point=15,#40#50                               
        additional_string = "_pfXWP1000_jet0_red_back",
        alpha = 2,
        CL = 5,
        FOM = a
        )



for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            #"MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nTrackConstituents<10 && Jets[1].nTrackConstituents<10 && Jets[0].nTrackConstituents>-1 && Jets[1].nTrackConstituents>-1 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nHadEFrac>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[0].pfXWP1000>0.85 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[0].pfXWP1000>0.9 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"Jets[0].pfXWP1000>0.95 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            "Jets[1].nHadEFrac>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.85 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.9 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.95 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            #"(Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"(Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8 || Jets[2].pfXWP1000>0.8 || Jets[3].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #"(Jets[0].pfXWP1000>0.5 && Jets[1].pfXWP1000>0.5) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            ],
        [
            "Pre-selections",
            "+ 2 CHS jets nTracKConstituents<10",
            "+ lead. jet nHadEFrac>0.8",
            "+ lead. jet pfXWP1000>0.8",
            #"+ lead. jet pfXWP1000>0.85",
            #"+ lead. jet pfXWP1000>0.9",
            #"+ lead. jet pfXWP1000>0.95",
            "+ sub-lead. jet nHadEFrac>0.8",
            "+ sub-lead. jet pfXWP1000>0.8",
            "+ sub-lead. jet pfXWP1000>0.85",
            "+ sub-lead. jet pfXWP1000>0.9",
            "+ sub-lead. jet pfXWP1000>0.95",
            ],
        header = "",
        mass_point=15,#40#50                               
        additional_string = "_pfXWP1000_jet0_jet1_red_back",
        alpha = 2,
        CL = 5,
        FOM = a
        )


for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            "MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nTrackConstituents<10 && Jets[1].nTrackConstituents<10 && Jets[0].nTrackConstituents>-1 && Jets[1].nTrackConstituents>-1 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            #asymm cuts
            "Jets[0].pfXWP1000>0.8 && Jets[1].pfXWP1000>0.6 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.9 && Jets[1].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],


            "(Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            ],
        [
            "Pre-selections",
            "+ 2 CHS jets nTracKConstituents<10",
            "+ lead. jet pfXWP1000>0.8",
            "+ sub-lead. jet pfXWP1000>0.8",
            
            "+ j0 pfXWP1000>0.8, j1>0.6",
            "+ j0 pfXWP1000>0.9, j1>0.8",

            "+ lead. or sub-lead jet pfXWP1000>0.8",
            ],
        header = "",
        mass_point=15,#40#50                               
        additional_string = "_combination_pfXWP1000_asymmetric_red_back",
        alpha = 2,
        CL = 5,
        FOM = a
        )

#exit()




for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            "MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nTrackConstituents<10 && Jets[1].nTrackConstituents<10 && Jets[0].nTrackConstituents>-1 && Jets[1].nTrackConstituents>-1 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.8 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            "Jets[0].pfXWP1000>0.8 && Jets[0].nTrackConstituents<10 && Jets[0].nTrackConstituents>-1 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[1].pfXWP1000>0.8 && Jets[1].nTrackConstituents<10 && Jets[1].nTrackConstituents>-1 && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            "(Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],
            "Jets[0].nTrackConstituents<10 && Jets[1].nTrackConstituents<10 && Jets[0].nTrackConstituents>-1 && Jets[1].nTrackConstituents>-1 &&  (Jets[0].pfXWP1000>0.8 || Jets[1].pfXWP1000>0.8) && MEt.sign>30 && MEt.pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF" + " && " + selection["PFMETNoMuTrigger"],

            ],
        [
            "Pre-selections",
            "+ 2 CHS jets nTracKConstituents<10",
            "+ lead. jet pfXWP1000>0.8",
            "+ sub-lead. jet pfXWP1000>0.8",

            "+ lead. jet pfXWP1000>0.8 & nTracKConstituents<10",
            "+ sub-lead. jet pfXWP1000>0.8 & nTracKConstituents<10",

            "+ lead. or sub-lead jet pfXWP1000>0.8",
            "+ lead. or sub-lead jet pfXWP1000>0.8 and nTracKConstituents<10",
            ],
        header = "",
        mass_point=15,#40#50                               
        additional_string = "_combination_pfXWP1000_and_nTracksConst_red_back",
        alpha = 2,
        CL = 5,
        FOM = a
        )

exit()

