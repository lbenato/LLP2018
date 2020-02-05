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


from Analyzer.LLP2018.samples import sample, samples
from Analyzer.LLP2018.selections import selection
from Analyzer.LLP2018.variables import *

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

#NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v7_short/SkimBTagCSV/"
#NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v7_short/"
NTUPLEDIR   = "/nfs/dust/cms/group/cms-llp/v0_pfXTag_short/"
#NTUPLEDIR   = "/nfs/dust/cms/user/lbenato/v4/"
#LUMI        = 36814 # in pb-1
LUMI = 35867#36814# in pb-1 Full 2016 with normtag
SIGNAL      = 1.
RATIO       = 4 # 0: No ratio plot; !=0: ratio between the top and bottom pads
BLIND       = True
POISSON     = False
verbose     = False
jobs        = []

########## SAMPLES ##########
sign = [
#'VBFH_M15_ctau0p05','VBFH_M15_ctau0p1','VBFH_M15_ctau1','VBFH_M15_ctau5','VBFH_M15_ctau10','VBFH_M15_ctau25','VBFH_M15_ctau50',
'VBFH_M40_ctau0','VBFH_M40_ctau0p05','VBFH_M40_ctau0p1','VBFH_M40_ctau1','VBFH_M40_ctau5','VBFH_M40_ctau10',#'VBFH_M40_ctau25',#,'VBFH_M40_ctau5','VBFH_M40_ctau50'
#'VBFH_M15_ctau100',#'VBFH_M15_ctau500','VBFH_M15_ctau1000','VBFH_M15_ctau2000','VBFH_M15_ctau5000','VBFH_M15_ctau10000',
#'VBFH_M55_ctau0p05','VBFH_M55_ctau0p1','VBFH_M55_ctau5','VBFH_M55_ctau10','VBFH_M55_ctau25','VBFH_M55_ctau50',#'VBFH_M55_ctau1',
#'VBFH_M55_ctau100','VBFH_M55_ctau500','VBFH_M55_ctau1000','VBFH_M55_ctau2000','VBFH_M55_ctau5000','VBFH_M55_ctau10000',
]
#back = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","DYJetsToQQ","DYJetsToNuNu","ST","TTbar","QCD"]
back = ["QCD_red", "TTbar"]
colors = [4, 410, 856, 2, 634, 1, 881, 798, 602, 921]
########## ######## ##########

#gROOT.SetBatch(True)

def efficiency(cutlist, labellist):

    basecut = ""
    signame = ""
    ncuts = len(cutlist)
    
    file = {}
    nevt = {}
    tree = {}
    effs = {}

    for i, s in enumerate(sign):
        signame = "LLP"
        file[s] = TFile(NTUPLEDIR + samples[s]['files'][0] + ".root", "READ") # Read TFile
#        nevt[s] = (file[s].Get('c_nEvents')).GetBinContent(1) # TODO: add with global variable for skimmed tree
#        tree[s] = file[s].Get("skim") # TODO: add with global variable for skimmed tree
        nevt[s] = (file[s].Get('counter/c_nEvents')).GetBinContent(1)
        tree[s] = file[s].Get("ntuple/tree") # Read TTree
        effs[s] = [0]*(ncuts+1)
        if verbose: print "signal: ", s
        for j, c in enumerate(cutlist):
            if verbose: print "cut: ", c
            br = 1.
            d = nevt[s]#all gen events! ###    tree[s].GetEntries()#nevt[s]#d = sample[samples[s]['files'][0]]['nevents']#tree[s].GetEntries(basecut)
            if verbose: print "den: ", d
            n = tree[s].GetEntries(cutlist[j])
            if verbose: print "num: ", n
            effs[s][j] = float(n)/(d*br)
    
    line = []
    #outFile = TFile("Efficiency/ZhadZinv/Eff_spline.root", "UPDATE")
    #outFile.cd()
    #flagLP = True
    for j, c in enumerate(cutlist):
        line.append( TGraph(ncuts) )
        line[j].SetTitle(";m_{VZ}^{T} (GeV);Efficiency")
        #print labellist[j]
        for i, s in enumerate(sign):
            mass = samples[s]['mass']
            ctau = samples[s]['ctau']
            #mass = int( ''.join(x for x in s if x.isdigit()) )
            line[j].SetPoint(i, ctau, effs[s][j])#mass
            if verbose: print  mass, ctau, effs[s][j]
        line[j].SetMarkerStyle(20)
        line[j].SetMarkerColor(colors[j])
        line[j].SetLineColor(colors[j])
        line[j].SetLineWidth(3)
        line[j].GetXaxis().SetTitleOffset(line[j].GetXaxis().GetTitleOffset()*1.2)
        line[j].GetYaxis().SetTitleOffset(line[j].GetYaxis().GetTitleOffset()*1.2)
    #outFile.Close()
    leg = TLegend(0.6, 0.6, 0.9, 0.9)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0) #1001
    leg.SetFillColor(0)
    for i, c in enumerate(cutlist):
        leg.AddEntry(line[i], labellist[i], "lp")

    leg.AddEntry(line[0], 'VBF H #rightarrow #pi #pi #rightarrow b#bar{b} b#bar{b}', "")
    
    c1 = TCanvas("c1", "Signals", 800, 600)
    c1.cd()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    c1.SetLogx()
    line[0].GetXaxis().SetTitle("m_{#pi} (GeV)")
    line[0].GetYaxis().SetTitle("Efficiency")
    line[0].GetYaxis().SetRangeUser(0., 1.)
    
    for i, s in enumerate(cutlist):
        line[i].Draw("APL" if i==0 else "SAME, PL")
    leg.Draw()
    #drawCMS(-1, "Simulation")
    
    name = ""
    
    c1.Print("$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/Efficiency_" + signame + "_v0_pfXTag.png")
    c1.Print("$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/Efficiency_" + signame + "_v0_pfXTag.pdf")
    #if not options.runBash: raw_input("Press Enter to continue...")

'''
efficiency([
    '(isVBF)',
    '(isVBF) && nCHSJets>2'
    ],
    [
    'isVBF',
    '+nCHSJets>2'
    ]
)
'''
#raw_input('pausa')

def calc_punzi_FOM_vs_ctau(cutlist, labellist=[],mass_point=40,additional_string="",n_sigma=1,FOM='punzi'):
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
#        tree[s] = file[s].Get("skim") # TODO: add with global variable for skimmed tree 
#        nevt[s] = (file[s].Get('c_nEvents')).GetBinContent(1) # TODO: add with global variable for skimmed tree
        effs[s] = [0]*(ncuts+1)
        if samples[s]['mass'] not in mass_array: mass_array.append(samples[s]['mass'])
        if samples[s]['ctau'] not in ctau_array: ctau_array.append(samples[s]['ctau'])
        for j, c in enumerate(cutlist):
            tot_gen = nevt[s]
            n = tree[s].GetEntries("(" + cutlist[j] + ")")
            if tot_gen==0:
                effs[s][j] = float(0.)
            else:
                effs[s][j] = (float(n)/(tot_gen))
            eff_dict[c][s] = {'mass' : samples[s]['mass'], 'ctau' : samples[s]['ctau'], 'eff' :effs[s][j]}


    #sort mass array
    masses = np.array(mass_array)
    masses.sort()

    ctaus = np.array(ctau_array)
    ctaus.sort()


    #define multigraph
    mg = TMultiGraph()
    leg = TLegend(0.78, 0.7, 0.98, 0.98)
    leg2 = TLegend(0., 0.4, 0.98, 0.98)
    leg.SetTextSize(0.03)
    leg2.SetTextSize(0.03)
    leg.SetBorderSize(0)
    leg2.SetBorderSize(0)
    leg.SetHeader("m_{#pi}=" +str(mass_point)+" GeV")
    leg2.SetHeader("m_{#pi}=" +str(mass_point)+" GeV")

    #for background let's first consider the cut
    for j, c in enumerate(cutlist):
        print "cut: ", c
        #then loop over background
        integral = 0
        weighted_integral = 0
        back_tot_events = 0
        for i, s in enumerate(back):
            chain[s] = TChain("ntuple/tree")
#            chain[s] = TChain("skim") # TODO: add with global variable for skimmed tree
            #print "back: ", s
            back_file = {}
            for p, ss in enumerate(samples[s]['files']):
                back_file[ss] = TFile(NTUPLEDIR + ss + ".root", "READ") # Read TFile                  
                if verbose: print "file: ", ss
                if verbose: print "gen events: ", (back_file[ss].Get('counter/c_nEvents')).GetBinContent(1)
                if verbose: print "tree events: ", (back_file[ss].Get('ntuple/tree')).GetEntries()
                back_tot_events += (back_file[ss].Get('counter/c_nEvents')).GetBinContent(1)
#                back_tot_events += (back_file[ss].Get('c_nEvents')).GetBinContent(1) # TODO: add with global variable for skimmed tree
                chain[s].Add(NTUPLEDIR + ss + ".root")
            weight = "EventWeight"
            var = "nPV"
#            var = "nCHSJets" # TODO: add with global variable for skimmed tree
            hist[s] = TH1F(s, ";"+variable[var]['title'], variable[var]['nbins'], variable[var]['min'], variable[var]['max'])
            hist[s].Sumw2()
            cutstring = "("+weight+")" + ("*("+cutlist[j]+")" if len(cutlist[j])>0 else "")
            chain[s].Project(s, var, "")#"1*"+"("+weight+")")
            hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
            if verbose: print "events in the histo with get entries with empty project: ", hist[s].GetEntries()
            if verbose: print "area under histo with empty project: ", hist[s].Integral()
            chain[s].Project(s, var, cutstring)#"1*"+"("+weight+")")
            hist[s].SetOption("%s" % chain[s].GetTree().GetEntriesFast())
            hist[s].Scale(samples[s]['weight'] if hist[s].Integral() >= 0 else 0)
            if verbose: print "events in the histo with get entries after project: ", hist[s].GetEntries()
            if verbose: print "area under histo after project: ", hist[s].Integral()
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
            if FOM=="punzi":
                punzi_dict[c][s] = {'sign': eff_dict[c][s]['eff']/(n_sigma*0.5 + math.sqrt(back_int_weight[c]))}
            elif FOM=="signaleff":
                punzi_dict[c][s] = {'sign': eff_dict[c][s]['eff']*100}
            else:
                print "not punzi FOM, aborting!"
                exit()



    #for each cut, we need a graph                                                                          
    for j, c in enumerate(cutlist):
    #first let's build the ordered punzi vector w.r.t. masses, for a chosen ctau                            
        punzi_array = []
        back_array = []
        for la in ctaus:
            #la = str(a)
            if la== 0.001:
                st = "VBFH_M"+str(mass_point)+"_ctau0"
            elif la==0.05 or la==0.1:
                st = "VBFH_M"+str(mass_point)+"_ctau"+str(str(la).replace("0.","0p"))
            else:
                st = "VBFH_M"+str(mass_point)+"_ctau"+str(int(la))
            #st = "VBFH_M"+str(mass_point)+"_ctau"+str(a)                                                        
            punzi_array.append(punzi_dict[c][st]['sign'])
        mass = array('d', masses)
        ct = array('d', ctaus)
        p_array = array('d',punzi_array)
        #graph[c] = TGraph(len(mass),mass, np.array(p_array))                                                   
        graph[c] = TGraph(len(ct),ct, np.array(p_array))
        graph[c].SetMarkerStyle(21)
        graph[c].SetLineWidth(2)
        graph[c].SetMarkerSize(1.)
        graph[c].SetMarkerColor(colors[j])
        graph[c].SetLineColor(colors[j])
        graph[c].SetFillColor(colors[j])
        #graph[c].SetLogx()                                                                                 
        leg.AddEntry(graph[c],labellist[j],'PL')
        leg2.AddEntry(graph[c],labellist[j],'PL')
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
            leg.AddEntry(back_graph[c],labellist[j]+" bkg.",'PL')
            #leg2.AddEntry(back_graph[c],labellist[j]+" bkg.",'PL')                                         
            mg.Add(back_graph[c])

    if FOM=="signaleff":
        dummy = TGraph(len(ct),ct, np.array(e_array))
        dummy.SetMarkerStyle(0)
        dummy.SetLineWidth(2)
        dummy.SetMarkerSize(1.)
        dummy.SetLineColor(15)
        dummy.SetLineStyle(2)
        leg2.AddEntry(dummy, 'cuts on bkg.','PL')


    cmg = TCanvas("cmg", "cmg", 2000, 800)
    cmg.cd()
    cmg.SetGrid()
    if FOM=="signaleff":
        cmg.SetLogx()
    pad1 = TPad("pad1", "pad1", 0, 0., 0.75, 1.0)
    pad1.SetGrid()
    pad1.SetLogx()
    if FOM=="signaleff":
        #print "LOL"
        pad1.SetLogy()
    pad1.Draw()
    pad1.cd()

    if FOM=="signaleff":
        mg.SetMaximum(101)
        #mg.SetMinimum(1.e-50)
    mg.Draw("APL")
    mg.GetXaxis().SetTitle('c#tau_{#pi} (mm)')
    mg.GetYaxis().SetTitleOffset(1.2);
    if FOM=="punzi":
        mg.GetYaxis().SetTitle('Punzi significance @ '+str(n_sigma)+' #sigma, VBF cuts')
        mg.GetYaxis().SetTitleOffset(1.5)
    elif FOM=="signaleff":
        mg.GetYaxis().SetTitle('Signal (background) efficiency, VBF cuts (%)')
    else:
        print "not punzi FOM, aborting"

    cmg.cd()
    pad2 = TPad("pad2", "pad2", 0.75, 0., 1, 1.0)
    pad2.SetGrid()
    pad2.SetLogx()
    pad2.Draw()
    pad2.cd()
    leg2.SetTextSize(0.07)
    leg.Clear()#?????????
    leg2.Draw()
    cmg.Update()

    if FOM=="punzi":
        cmg.Print("$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/Punzi_m"+str(mass_point)+"_"+str(n_sigma)+"sigma"+additional_string+"_v0_pfXTag.pdf")
        cmg.Print("$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/Punzi_m"+str(mass_point)+"_"+str(n_sigma)+"sigma"+additional_string+"_v0_pfXTag.png")
    elif FOM=="signaleff":
        cmg.Print("$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/SignalEff_m"+str(mass_point)+additional_string+"_v0_pfXTag.pdf")
        cmg.Print("$CMSSW_BASE/src/Analyzer/LLP2018/macro/Efficiency/SignalEff_m"+str(mass_point)+additional_string+"_v0_pfXTag.png")
    else:
        print "not punzi FOM, aborting"

    if not options.bash: raw_input("Press Enter to continue...")
    cmg.Close()


fom = ["signaleff","punzi"]

#cut_val = [["0.","999.9"],["80.","180."],["100.","160."], ["110.","140."]]
#cut = "mjjAK8"

cut_val = ["0.", "0.6", "0.8", "0.9", "0.95"]
#cut = "pfXWP1"
cut = "CSV"

#cut_val = ["1.", "0.8", "0.85", "0.7", "0.75", "0.6", "0.65", "0.5"]
#cut = "tau21"

select = []
legend = []

#select.append(selection["VBFplusVBFTrigger"],)
#legend.append("Trigger",)

for b in cut_val:
    if b < len(cut_val):
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets.FatJets[0].pfBoostedDoubleSVAK8 > 0.9 " + " && " + "FatJets.FatJets[1].pfBoostedDoubleSVAK8 > 0.9 ",)
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets[0].pfBoostedDoubleSVAK8 > "+ b,)
#        select.append( b[0] + "< mjjAK8 " + " && "+ " mjjAK8 < " + b[1], )
#        legend.append(b[0]+" < " + cut+" < "+ b[1],)
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets.FatJets[0].pfBoostedDoubleSVAK8 > " + b + " && " + "FatJets.FatJets[1].pfBoostedDoubleSVAK8 > " + b,)
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets.FatJets[0].pfBoostedDoubleSVAK8 > " + b ,)
#        select.append(selection["VBFplusVBFTrigger"] + " && " +  "nCHSFatJets == 1" + " && " + "FatJets.FatJets[0].chsTau21 < " + b ,)
#        select.append(selection["VBFplusVBFTrigger"] + " && (" + " (nCHSFatJets == 2 && FatJets.FatJets[0].pfBoostedDoubleSVAK8 > 0.9 && FatJets.FatJets[1].pfBoostedDoubleSVAK8 > 0.9) "+" || " + "(nCHSFatJets == 1" + " && " + "FatJets.FatJets[0].chsTau21 < " + b + "))",)
#        select.append(selection["VBFplusVBFTrigger"] + " && (" + "nCHSJets > 1 && " + "Jets.Jets[0].pfXWP1 > " + b + ")",) #" && Jets.Jets[1].pfXWP1 > " + b + ")",)
        select.append(selection["VBFplusVBFTrigger"] + " && (" + "nCHSJets > 1 && " + "Jets.Jets[0].CSV > " + b + " && Jets.Jets[1].CSV > " + b + ")",)
        legend.append(cut+" > "+ b,)
    else:
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets.FatJets[0].pfBoostedDoubleSVAK8 > 0.9 " + " && " + "FatJets.FatJets[1].pfBoostedDoubleSVAK8 > 0.9 ")
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets[0].pfBoostedDoubleBSVAK8 > " + b)
#        select.append( b[0] + "< mjjAK8 " + " && "+ " mjjAK8 < " + b[1])
#        legend.append(b[0]+" < " + cut+" < "+ b[1])
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets.FatJets[0].pfBoostedDoubleSVAK8 > " + b + " && " + "FatJets.FatJets[1].pfBoostedDoubleSVAK8 > " + b)
#        select.append(selection["VBFplusVBFTrigger"] + " && " + "FatJets.FatJets[0].pfBoostedDoubleSVAK8 > " + b )
#        select.append(selection["VBFplusVBFTrigger"] + " && " +  "nCHSFatJets == 1" + " && " + "FatJets.FatJets[0].chsTau21 < " + b )
#        select.append(selection["VBFplusVBFTrigger"] + " && (" + " (nCHSFatJets == 2 && FatJets.FatJets[0].pfBoostedDoubleSVAK8 > 0.9 && FatJets.FatJets[1].pfBoostedDoubleSVAK8 > 0.9) "+" || " + "(nCHSFatJets == 1" + " && " + "FatJets.FatJets[0].chsTau21 < " + b + "))")
#        select.append(selection["VBFplusVBFTrigger"] + " && (" + "nCHSJets > 1 && " + "Jets.Jets[0].pfXWP1 > " + b + ")") #" && Jets.Jets[1].pfXWP1 > " + b + ")")
        select.append(selection["VBFplusVBFTrigger"] + " && (" + "nCHSJets > 1 && " + "Jets.Jets[0].CSV > " + b + " && Jets.Jets[1].CSV > " + b + ")")
        legend.append(cut+" > "+ b)

print select
print legend
for a in fom:

    calc_punzi_FOM_vs_ctau(
        select,
        legend,
        mass_point=40,
        additional_string = "_CSV_twoJet_"+cut,
        n_sigma = 5,
        FOM = a
)



'''
######

fom = ["signaleff","punzi"]
#fom = ["punzi"]
#fom = ["signaleff"]

#v3
#Ultra Loose WP
#this works okay
#uloose_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.3 && Jets.Jets[0].nHadEFrac>0.7"
#uloose_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.3 && Jets.Jets[1].nHadEFrac>0.7"

#second try
uloose_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.4 && Jets.Jets[0].nHadEFrac>0.6"
uloose_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.4 && Jets.Jets[1].nHadEFrac>0.6"


#this is better than loose alone!
#uloose_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.2 && Jets.Jets[0].nHadEFrac>0.8"
#uloose_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.3 && Jets.Jets[1].nHadEFrac>0.7"

#only one var per time
n_uloose_cut_Jet0 = "Jets.Jets[0].nHadEFrac>0.6"
n_uloose_cut_Jet1 = "Jets.Jets[1].nHadEFrac>0.6"

c_uloose_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.4"
c_uloose_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.4"


#Loose WP
cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.2 && Jets.Jets[0].cMulti<10 && Jets.Jets[0].nEmEFrac<0.15 && Jets.Jets[0].nHadEFrac>0.8 && Jets.Jets[0].photonEFrac < 0.1"
cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.2 && Jets.Jets[1].cMulti<10 && Jets.Jets[1].nEmEFrac<0.15 && Jets.Jets[1].nHadEFrac>0.8 && Jets.Jets[1].photonEFrac < 0.1"
cut_Jet2 = "Jets.Jets[2].cHadEFrac<0.2 && Jets.Jets[2].cMulti<10 && Jets.Jets[2].nEmEFrac<0.15 && Jets.Jets[2].nHadEFrac>0.8 && Jets.Jets[2].photonEFrac < 0.1"
cut_Jet3 = "Jets.Jets[3].cHadEFrac<0.2 && Jets.Jets[3].cMulti<10 && Jets.Jets[3].nEmEFrac<0.15 && Jets.Jets[3].nHadEFrac>0.8 && Jets.Jets[3].photonEFrac < 0.1"

#BEST WP
best_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.09 && Jets.Jets[0].nEmEFrac<0.1 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.1 && Jets.Jets[0].ecalE<10"#THE BEST SO FAR!!!
best_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.09 && Jets.Jets[1].nEmEFrac<0.1 && Jets.Jets[1].nHadEFrac>0.9 && Jets.Jets[1].photonEFrac < 0.1 && Jets.Jets[1].ecalE<10"#THE BEST SO FAR!!!

#this is going worse than tight
#medium_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.09 && Jets.Jets[0].nEmEFrac<0.09 && Jets.Jets[0].nHadEFrac>0.92 && Jets.Jets[0].ecalE<10"#
#medium_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.09 && Jets.Jets[1].nEmEFrac<0.09 && Jets.Jets[1].nHadEFrac>0.92 && Jets.Jets[1].ecalE<10"

#this is better than best!
#medium_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.1 && Jets.Jets[0].nEmEFrac<0.09 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].ecalE<10"#
#medium_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.1 && Jets.Jets[1].nEmEFrac<0.09 && Jets.Jets[1].nHadEFrac>0.9 && Jets.Jets[1].ecalE<10"

medium_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.11 && Jets.Jets[0].nEmEFrac<0.099 && Jets.Jets[0].nHadEFrac>0.9"#
medium_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.11 && Jets.Jets[1].nEmEFrac<0.099 && Jets.Jets[1].nHadEFrac>0.9"

#Calo WP
hard_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10"
hard_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.08 && Jets.Jets[1].cMulti<8 && Jets.Jets[1].nEmEFrac<0.08 && Jets.Jets[1].nHadEFrac>0.9 && Jets.Jets[1].photonEFrac < 0.08 && Jets.Jets[1].ecalE<10"
hard_cut_Jet2 = "Jets.Jets[2].cHadEFrac<0.08 && Jets.Jets[2].cMulti<8 && Jets.Jets[2].nEmEFrac<0.08 && Jets.Jets[2].nHadEFrac>0.9 && Jets.Jets[2].photonEFrac < 0.08 && Jets.Jets[2].ecalE<10"

more_hard_cut_Jet0 = "Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && Jets.Jets[0].cEmEFrac<0.05"
more_hard_cut_Jet1 = "Jets.Jets[1].cHadEFrac<0.08 && Jets.Jets[1].cMulti<8 && Jets.Jets[1].nEmEFrac<0.08 && Jets.Jets[1].nHadEFrac>0.9 && Jets.Jets[1].photonEFrac < 0.08 && Jets.Jets[1].ecalE<10 && Jets.Jets[1].cEmEFrac<0.05"
more_hard_cut_Jet2 = "Jets.Jets[2].cHadEFrac<0.08 && Jets.Jets[2].cMulti<8 && Jets.Jets[2].nEmEFrac<0.08 && Jets.Jets[2].nHadEFrac>0.9 && Jets.Jets[2].photonEFrac < 0.08 && Jets.Jets[2].ecalE<10 && Jets.Jets[2].cEmEFrac<0.05"


##LISA
#just to test trigger
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
#            selection['DisplacedTrigger'] + " && isVBF",
            selection['DisplacedHadronicTrigger'] + " && isVBF",
#            selection['DisplacedTrackTrigger'] + " && isVBF",
#            selection['DisplacedDiJetTrigger'] + " && isVBF",
#            selection['DisplacedTrigger'] + " && isVBF && " + cut_Jet0 + " && " + cut_Jet1,
#            selection['DisplacedTrigger'] + " && isVBF && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + cut_Jet0 + " && " + cut_Jet1,
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + cut_Jet0 + " && " + cut_Jet1 + "&& Jets.Jets[0].pt>20 && Jets.Jets[1].pt>20",
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + hard_cut_Jet0 + " && " + hard_cut_Jet1 + "&& Jets.Jets[0].pt>20 && Jets.Jets[1].pt>20",
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + cut_Jet0 + " && " + cut_Jet1 + "&& Jets.Jets[0].pt>30 && Jets.Jets[1].pt>30",
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + hard_cut_Jet0 + " && " + hard_cut_Jet1 + "&& Jets.Jets[0].pt>30 && Jets.Jets[1].pt>30",
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + cut_Jet0 + " && " + cut_Jet1 + "&& Jets.Jets[0].pt>40 && Jets.Jets[1].pt>40",
            selection['DisplacedHadronicTrigger'] + " && isVBF && " + hard_cut_Jet0 + " && " + hard_cut_Jet1 + "&& Jets.Jets[0].pt>40 && Jets.Jets[1].pt>40",
            ],
        [
#            'DisplacedTrigger && VBF',
            'DisplacedHadronic && VBF',
#            'DisplacedTrack && VBF',
#            'DisplacedDiJet && VBF',
#            'j_{0} j_{1} LooseCaloTag',
#            'j_{0} j_{1} TightCaloTag',
            'HadTr + j_{0} j_{1} LooseCaloTag',
            'HadTr + j_{0} j_{1} TightCaloTag',
            'HadTr + pt20 + j_{0} j_{1} LooseCaloTag',
            'HadTr + pt20 + j_{0} j_{1} TightCaloTag',
            'HadTr + pt30 + j_{0} j_{1} LooseCaloTag',
            'HadTr + pt30 + j_{0} j_{1} TightCaloTag',
            'HadTr + pt40 + j_{0} j_{1} LooseCaloTag',
            'HadTr + pt40 + j_{0} j_{1} TightCaloTag',
            ],
        mass_point=55,#20
        #additional_string = "_TestDisplacedTriggers",#"_LMT", 
        additional_string = "_LT_HadronicTrigger_pt20_30_40",#"_LMT", 
        n_sigma = 5,
        FOM = a
        )


exit()
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            selection['DisplacedTrigger'] + " && isVBF",
#            selection['DisplacedTrigger'] + " && isVBF && " + n_uloose_cut_Jet0 + " && " + n_uloose_cut_Jet1,
            selection['DisplacedTrigger'] + " && isVBF && " + c_uloose_cut_Jet0 + " && " + c_uloose_cut_Jet1,
#            selection['DisplacedTrigger'] + " && isVBF && " + uloose_cut_Jet0 + " && " + uloose_cut_Jet1,
            selection['DisplacedTrigger'] + " && isVBF && " + cut_Jet0 + " && " + cut_Jet1,
#            selection['DisplacedTrigger'] + " && isVBF && " + medium_cut_Jet0 + " && " + medium_cut_Jet1,
            selection['DisplacedTrigger'] + " && isVBF && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
#            selection['DisplacedTrigger'] + " && isVBF && " + best_cut_Jet0 + " && " + best_cut_Jet1,

#            selection['DisplacedTrigger'],
#            selection['DisplacedTrigger'] + " && isVBF && Jets.Jets[0].cHadEFrac<0.2",
#            selection['DisplacedTrigger'] + " && isVBF && Jets.Jets[0].cMulti<10",
#            selection['DisplacedTrigger'] + " && isVBF && Jets.Jets[0].nEmEFrac<0.15",
#            selection['DisplacedTrigger'] + " && isVBF && Jets.Jets[0].nHadEFrac>0.8",
#            selection['DisplacedTrigger'] + " && isVBF && Jets.Jets[0].photonEFrac < 0.1",
#            selection['DisplacedTrigger'] + " && isVBF && Jets.Jets[0].nSelectedTracks < 5",
##            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.2 && Jets.Jets[0].cMulti<10 && Jets.Jets[0].nEmEFrac<0.15 && Jets.Jets[0].nHadEFrac>0.8 && Jets.Jets[0].photonEFrac < 0.1",
##            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10",#npr<30?20?15
##            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && Jets.Jets[0].nSelectedTracks <5",#npr<30?20?15
##            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && Jets.Jets[0].nSelectedTracks <4",#npr<30?20?15
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && Jets.Jets[0].npr<20",#npr<30?20?15
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && nElectrons==0 && nMuons==0 && nPhotons==0", 
#            selection['DisplacedTrigger'] + " && nCaloTagJets>=1",
###            selection['DisplacedTrigger'] + " && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
###            selection['DisplacedTrigger'] + " && " + hard_cut_Jet0 + " && " + hard_cut_Jet1 + " && " + hard_cut_Jet2,
###            selection['DisplacedTrigger'] + " && nCaloTagJets>=2",
#            selection['DisplacedTrigger'] + " && nCaloTagJets>=2 && nCHSJets>0",
#            selection['DisplacedTrigger'] + " && nCaloTagJets>=3",
            ],
        [
            'DisplacedTrigger && VBF',
#            'j_{0} j_{1} n_UltraLooseCaloTag',
            'j_{0} j_{1} c_UltraLooseCaloTag',
#            'j_{0} j_{1} UltraLooseCaloTag',
            'j_{0} j_{1} LooseCaloTag',
#            'j_{0} j_{1} MediumCaloTag',
            'j_{0} j_{1} TightCaloTag',
#            'j_{0} j_{1} BestCaloTag',

#            '+ Jet[0] cHadEFrac<0.2',
#            '+ Jet[0] cMulti<10',
#            '+ Jet[0] nEmEFrac<0.15',
#            '+ Jet[0] nHadEFrac>0.8',
#            '+ Jet[0] photonEFrac<0.1',
#            '+ Jet[0] tracks<5',
##            '+ all Jet[0]',
##            ' harder J0',
##            ' +tracks<5',
##            ' +tracks<4',
#            ' even harder ',
#            ' harder + lep veto',
#            'calo jet tag >= 1',
###            ' harder J01',
###            ' harder J012',
###            'calo jet tag >= 2',
#            'calo jet tag >= 2 && nJets>0',
#            'calo jet tag >= 3',
            ],
        mass_point=55,
        additional_string = "_LT_wp",#"_LMT", 
        #additional_string = "_LMTB_bis_check",#"_LMT", 
        n_sigma = 5,
        FOM = a
        )
'''

#MET is VERY difficult so far
'''

other = "MEt.pt<700"

for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
#            selection['DisplacedTrigger'] + " && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
#            selection['METTrigger'] + " && MEt.pt > 200",
            selection['METTrigger'] + " && nCHSJets<6 && nCHSJets>=1",
            selection['METTrigger'] + " && MEt.pt > 200 && nCHSJets<6 && nCHSJets>=1",
            selection['METTrigger'] + " && " + other,
#            selection['METTrigger'] + " && MEt.pt > 200 && nCHSJets<6 && nCHSJets>=1" + " && " + other + " && Jets.Jets[0].cHadMulti<15 && Jets.Jets[0].cmuEFrac<0.05 && Jets.Jets[0].eleMulti<1",
            ],
        [
#            'DJ manual hard_cut Jet01',
            'MET jet multi',
            'MET MET>200 jet multi',
            'MET<700',
#            'MET MET>200 no lept',
#            'MET MET>200 jet multi',
#            'MET MET>200 plus things',
#            'etc',
            ],
        mass_point=55,
        additional_string = "_METvsDispl_n_calo_jet_tags_mult_v3_b", 
        n_sigma = 5,
        FOM = a
        )
'''

##LISA
###Try categories
'''
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            selection['DisplacedTrigger'] + " && nCaloTagJets>=2",
            selection['DisplacedTrigger'] + " && nCHSJets>0 && nCaloTagJets==1",
            selection['DisplacedTrigger'] + " && nCHSJets==2 && nCaloTagJets>=2",
            selection['DisplacedTrigger'] + " && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
            selection['DisplacedTrigger'] + " && nCHSJets>2 && nCaloTagJets>=2",
            selection['DisplacedTrigger'] + " && nCHSJets>2 && nCaloTagJets>=2 && nCHSJets<6",
            ],
        [
            '>= 2 CaloTagJets',
            '=1 CaloTagJets',
            '=2 jets, >=2 CaloTag',
            'SubLeading category',
            '>2 jets, >=2 CaloTag',
            '2<jets<6, >=2 CaloTag',
            ],
        mass_point=55,
        additional_string = "_calo_jet_categories", 
        n_sigma = 5,
        FOM = a
        )

'''

###PLOTTED, v3
'''
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
#            selection['DisplacedTrigger'],
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.2",
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].cMulti<10",
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].nEmEFrac<0.15",
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].nHadEFrac>0.8",
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].photonEFrac < 0.1",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.2 && Jets.Jets[0].cMulti<10 && Jets.Jets[0].nEmEFrac<0.15 && Jets.Jets[0].nHadEFrac>0.8 && Jets.Jets[0].photonEFrac < 0.1",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10",#npr<30?20?15
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && Jets.Jets[0].npr<20",#npr<30?20?15
#            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.08 && Jets.Jets[0].cMulti<8 && Jets.Jets[0].nEmEFrac<0.08 && Jets.Jets[0].nHadEFrac>0.9 && Jets.Jets[0].photonEFrac < 0.08 && Jets.Jets[0].ecalE<10 && nElectrons==0 && nMuons==0 && nPhotons==0", 
#            selection['DisplacedTrigger'] + " && nCaloTagJets>=1",
            selection['DisplacedTrigger'] + " && " + hard_cut_Jet0 + " && " + hard_cut_Jet1,
            selection['DisplacedTrigger'] + " && " + hard_cut_Jet0 + " && " + hard_cut_Jet1 + " && " + hard_cut_Jet2,
            selection['DisplacedTrigger'] + " && nCaloTagJets>=2",
#            selection['DisplacedTrigger'] + " && nCaloTagJets>=2 && nCHSJets>0",
#            selection['DisplacedTrigger'] + " && nCaloTagJets>=3",
            ],
        [
#            'DisplacedTrigger && VBF',
#            '+ Jet[0] cHadEFrac<0.2',
#            '+ Jet[0] cMulti<10',
#            '+ Jet[0] nEmEFrac<0.15',
#            '+ Jet[0] nHadEFrac>0.8',
#            '+ Jet[0] photonEFrac<0.1',
            '+ all Jet[0]',
            ' harder J0',
#            ' even harder ',
#            ' harder + lep veto',
#            'calo jet tag >= 1',
            ' harder J01',
            ' harder J012',
            'calo jet tag >= 2',
#            'calo jet tag >= 2 && nJets>0',
#            'calo jet tag >= 3',
            ],
        mass_point=55,
        additional_string = "_allbkg_n_calo_jet_tags_improve", 
        n_sigma = 5,
        FOM = a
        )
'''

##LISA
##PLOTTED ALREADY, v2
'''


for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            selection['DisplacedTrigger'],
            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.2",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].cMulti<10",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].nEmEFrac<0.15",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].nHadEFrac>0.8",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].photonEFrac < 0.1",
            selection['DisplacedTrigger'] + " && Jets.Jets[0].cHadEFrac<0.2 && Jets.Jets[0].cMulti<10 && Jets.Jets[0].nEmEFrac<0.15 && Jets.Jets[0].nHadEFrac>0.8 && Jets.Jets[0].photonEFrac < 0.1",
            ],
        [
            'DisplacedTrigger && VBF',
            '+ Jet[0] cHadEFrac<0.2',
            '+ Jet[0] cMulti<10',
            '+ Jet[0] nEmEFrac<0.15',
            '+ Jet[0] nHadEFrac>0.8',
            '+ Jet[0] photonEFrac<0.1',
            '+ all Jet[0]',
            ],
        mass_point=20,
        additional_string = "_test", 
        n_sigma = 5,
        FOM = a
        )


for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            selection['DisplacedTrigger'],
            selection['DisplacedTrigger'] + " && " + cut_Jet0,
            selection['DisplacedTrigger'] + " && " + cut_Jet0 + " && " + cut_Jet1,
            selection['DisplacedTrigger'] + " && " + cut_Jet0 + " && " + cut_Jet1 + " && " + cut_Jet2,
            selection['DisplacedTrigger'] + " && " + cut_Jet0 + " && " + cut_Jet1 + " && " + cut_Jet2 + " && " + cut_Jet3,
            ],
        [
            'DisplacedTrigger && VBF',
            '+ all Jet[0]',
            '+ all Jet[0]&[1]',
            '+ all Jet[0]&[1]&[2]',
            '+ all Jet[0]&[1]&[2]&[3]',
            ],
        mass_point=55,#20,
#        additional_string = "_calo_cuts_Jet01", 
#        additional_string = "_calo_cuts_Jet012", 
        additional_string = "_calo_cuts_Jet0123", 
        n_sigma = 5,
        FOM = a
        )

'''


'''
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            selection['VBFTrigger'],
            selection['DisplacedTrigger'],
            selection['METTrigger'],
            selection['DisplacedSingleJetTrigger'],
            selection['DisplacedDiJetTrigger'],
            ],
        [
            'VBFTrigger',
            'DisplacedTrigger',
            'METTrigger',
            'DisplacedSingleJetTrigger',
            'DisplacedDiJetTrigger',
            ],
        mass_point=55,
        additional_string = "_displaced_trigger", 
        n_sigma = 5,
        FOM = a
        )
exit()

for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
            selection['VBFTrigger'],
            selection['DisplacedTrigger'],
            selection['METTrigger'],
            selection['VBFTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1)",
            selection['DisplacedTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1)",
            selection['METTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1)",
            ],
        [
            'VBFTrigger',
            'DisplacedTrigger',
            'METTrigger',
            'VBFTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1)",
            'DisplacedTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1)",
            'METTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1)",
            ],
        mass_point=20,
        additional_string = "_trigger_plus_mult", 
        n_sigma = 5,
        FOM = a
        )

exit()
 
'''

##LISA
###ALREADY PLOTTED:

'''

#v2
for a in fom:

    calc_punzi_FOM_vs_ctau(
        [
#            selection['VBFTrigger'],
#            selection['DisplacedTrigger'],
#            selection['METTrigger'],

#            selection['VBFTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1)",
#            selection['DisplacedTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1)",
#            selection['METTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1)",
#            selection['VBFTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1) && Jets.Jets[0].mass < 50",
#            selection['DisplacedTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1) && Jets.Jets[0].mass < 50",
#            selection['METTrigger'] + " && " + "(nCHSJets==2 || nCHSJets==1) && Jets.Jets[0].mass < 50",




#            selection['VBFTrigger'] + " && HT<200",
#            selection['DisplacedTrigger'] + " && HT<200",
#            selection['METTrigger'] + " && HT<200",
#            'nCHSJets==1',
#            'nCHSJets==2',
#            'nCHSJets==2 || nCHSJets==1',
#            'nCHSJets==3',
#            'nCHSJets==4',
#            'nCHSJets>4',
#            'HT<300',
#            'HT<300 && nCHSJets==2',
#            '(nCHSJets==2 || nCHSJets==1) && HT<300',
#            'Jets.Jets[0].cm<35',
#            'Jets.Jets[0].chf<0.7 && Jets.Jets[0].nhf>0.3 && (nCHSJets==2 || nCHSJets==1) && HT<300',
#            'Jets.Jets[0].nhf>0.3',
            ],
        [
            'VBFTrigger',
            'DisplacedTrigger',
            'METTrigger',

            'VBFTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1)",
            'DisplacedTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1)",
            'METTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1)",
#            'VBFTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1) && Jets.Jets[0].mass < 50",
#            'DisplacedTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1) && Jets.Jets[0].mass < 50",
#            'METTrigger' + " && " + "(nCHSJets==2 || nCHSJets==1) && Jets.Jets[0].mass < 50",




#            'VBFTrigger' + " && HT<200",
#            'DisplacedTrigger' + " && HT<200",
#            'METTrigger' + " && HT<200",
#            'nCHSJets==1',
#            'nCHSJets==2',
#            'nCHSJets==2 || nCHSJets==1',
#            'nCHSJets==3',
#            'nCHSJets==4',
#            'nCHSJets>4',
#            'HT<300',
#            'HT<300 && nCHSJets==2',
#            '(nCHSJets==2 || nCHSJets==1) && HT<300',
#            'Jets.Jets[0].cm<35',
#            'Jets.Jets[0].chf<0.7 && Jets.Jets[0].nhf<0.3 && (nCHSJets==2 || nCHSJets==1) && HT<300',
#            'Jets.Jets[0].nhf>0.3',
            ],
        mass_point=20,
        additional_string = "_test", 
        n_sigma = 5,
        FOM = a
        )


'''

