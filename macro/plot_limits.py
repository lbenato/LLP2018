#! /usr/bin/env python

import optparse
usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('-b', '--batch', action='store_true', default=False, dest='batch')
parser.add_option('-B', '--blind', action='store_true', default=True, dest='blind')
parser.add_option('-c', '--channel', action='store', type='string', dest='channel', default='')
parser.add_option('-t', '--tagvar', action='store', type='string', dest='tagvar', default='')
parser.add_option('-F', '--fom', action='store', type='string', dest='fom', default='')
parser.add_option('-C', '--category', action='store', type='string', dest='category', default='')
parser.add_option('-a', '--abcd', action='store_true', default=False, dest='abcd')
parser.add_option('-v', '--verbose', action='store_true', default=False, dest='verbose')
(options, args) = parser.parse_args()

if "ZH" in options.channel:
    chan = "ZH"
    xs = 1
    from Analyzer.LLP2018.ZH_DNN_setting import *
    from Analyzer.LLP2018.samples import *
if options.channel=="VBFH":
    print "VBFH"
    chan = "VBFH"
    from Analyzer.LLP2018.VBFH_DNN_setting import *    
    isMM = isEE = isComb = False
    xs = 1
    from Analyzer.LLP2018.samples import *
elif options.channel=="ggH":
    print "ggH"
    chan = "ggH"
    isMM = isEE = isComb = False
    xs = 1
    from Analyzer.LLP2018.ggH_DNN_setting import *
    from Analyzer.LLP2018.samples import *
elif options.channel=="SUSY":
    print "SUSY"
    chan = "SUSY"
    isMM = isEE = isComb = False
    xs = 1
    #from Analyzer.LLP2018.SUSY_DNN_setting import *
    #from Analyzer.LLP2018.SUSY_setting_higherpt import *
    #from Analyzer.LLP2018.samplesMINIAOD2018 import *
    from Analyzer.LLP2018.SUSY_DNN_setting_v3 import *
    from Analyzer.LLP2018.samplesAOD2018 import *
elif options.channel=="ggHeavyHiggs":
    print "HeavyHiggs"
    chan = "ggH"
    isMM = isEE = isComb = False
    xs = 1#0.1#1
    #from Analyzer.LLP2018.HeavyHiggs_DNN_setting import *
    #from Analyzer.LLP2018.HeavyHiggs_setting_higherpt import *
    #from Analyzer.LLP2018.samplesMINIAOD2018 import *
    #from Analyzer.LLP2018.HeavyHiggs_setting_AK4AK8 import *
    from Analyzer.LLP2018.HeavyHiggs_DNN_setting_v3 import *
    from Analyzer.LLP2018.samplesAOD2018 import *
else:
    print "Channel not recognized for plotting limits/significance!"

if SIGNAL_SUPPRESSION_FACTOR == 1000:
    unit = "fb"
else:
    unit = "pb"

unit = "pb"

from Analyzer.LLP2018.drawUtils import *

# Combine output with data
# 0 - Observed Limit
# 1 - Expected  2.5%
# 2 - Expected 16.0%
# 3 - Expected 50.0%
# 4 - Expected 84.0%
# 5 - Expected 97.5%
# 6 - Significance
# 7 - p-value
# 8 - Best fit r
# 9 - Best fit r down
#10 - Best fit r up

# Combine output blind
# 0 - Expected  2.5%
# 1 - Expected 16.0%
# 2 - Expected 50.0%
# 3 - Expected 84.0%
# 4 - Expected 97.5%

if options.channel=="SUSY":
    mass_string = "mh"
    ctau_string = "pl"
elif options.channel=="ggHeavyHiggs":
    mass_string = "MH"+str(MH)+"_MS"
    ctau_string = "ctau"
else:
    mass_string = "M"
    ctau_string = "ctau"

def fillValues(filename):
    val = {}
    mass = []
    ctau = []
    for i, s in enumerate(massPoints):
        for j, r in enumerate(ctauPoints):
            try:
                file = open( (filename % (s , r)), 'r')
                card=chan+"_"+mass_string+str(s)+"_"+ctau_string+str(r)
                if isMM:
                    card += "_MM"
                elif isEE:
                    card += "_EE"
                elif isComb:
                    card += "_comb"
                else:
                    card += ""

                val[card] = file.read().splitlines()
                if len(val[card]) == 0:
                           #massPoints.remove(s)#signals.remove(s)
                    continue
                for i, f in enumerate(val[card]): 
                    val[card][i] = float(val[card][i])
                    #if options.channel=="SUSY":#"ggHeavyHiggs":
                        #print "Applied signal suppression, need to reweight the exclusion limit power!!!"
                    	#val[card][i] = float(val[card][i])*xs/SIGNAL_SUPPRESSION_FACTOR
                if not s in mass: mass.append(s)
                if not r in ctau: ctau.append(r)
            except:
                print "File", (filename % (s,r)), "does not exist"
    return mass, ctau,  val

def limit_vs_mass(channel, ctaupoint, tagvar, save=False):
    particle = "#chi" if "SUSY" in options.channel else "#pi"
    if "HeavyHiggs" in options.channel: particle = "S" 
    #suffix = "_"+method
    drawTheory = False
    
    #print OUTPUTFOLDER
    filename = OUTPUTFOLDER +"/" + chan+"_"+mass_string+"%d_"+ctau_string+"%d"
    if isMM:
       filename += "_MM"
    elif isEE:
       filename += "_EE"
    elif isComb:
       filename += "_comb"
    filename +=".txt"

    mass, ctau, val = fillValues(filename)

    #print mass, ctau, val
    Obs0s = TGraph()
    Exp0s = TGraph()
    Exp1s = TGraphAsymmErrors()
    Exp2s = TGraphAsymmErrors()

    multF = 1.
    #print "----------------"
    #print "Ctau: ", ctaupoint

    #here loop for filling the plots
    n = 0
    for j, m in enumerate(mass):
        #print "mass: ", m
        name = chan+"_"+mass_string+str(m)+"_"+ctau_string+str(ctaupoint)#key index of val
        if isMM:
            name += "_MM"
        elif isEE:
            name += "_EE"
        elif isComb:
            name += "_comb"
        if not name in val:
            print "Key Error:", name, "not in value map"
            continue
        
        if len(val[name])<3: continue
        
        Exp0s.SetPoint(n, m, val[name][2]*multF)
        Exp1s.SetPoint(n, m, val[name][2]*multF)
        #print "Median: ", val[name][2]*multF
        Exp1s.SetPointError(n, 0., 0., val[name][2]*multF-val[name][1]*multF, val[name][3]*multF-val[name][2]*multF)
        #print "-1 sigma: ", val[name][2]*multF-val[name][1]*multF, "+ 1 sigma: ", val[name][4]*multF-val[name][3]*multF
        Exp2s.SetPoint(n, m, val[name][2]*multF)
        Exp2s.SetPointError(n, 0., 0., val[name][2]*multF-val[name][0]*multF, (val[name][4]*multF-val[name][2]*multF))
        #print "-2 sigma: ", val[name][2]*multF-val[name][0]*multF, "+ 2 sigma: ", (val[name][4]*multF-val[name][2]*multF)
        n = n+1

    n = 0
        
    Exp2s.SetLineWidth(2)
    Exp2s.SetLineStyle(1)
    Exp0s.SetLineStyle(2)
    Exp0s.SetLineWidth(3)
    Exp1s.SetFillColor(417) #kGreen
    Exp1s.SetLineColor(417) #kGreen
    Exp2s.SetFillColor(800) #kYellow
    Exp2s.SetLineColor(800) #kYellow
    Exp2s.GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
    #Exp2s.GetXaxis().SetTitleSize(Exp2s.GetXaxis().GetTitleSize()*1.25)
    Exp2s.GetXaxis().SetNoExponent(True)
    Exp2s.GetXaxis().SetMoreLogLabels(True)
    #Exp2s.GetYaxis().SetTitleSize(Exp2s.GetYaxis().GetTitleSize()*1.1)
    Exp2s.GetXaxis().SetTitleSize(0.048)
    Exp2s.GetYaxis().SetTitleSize(0.048)
    Exp2s.GetYaxis().SetTitleOffset(0.8)
    Exp2s.GetXaxis().SetTitleOffset(0.9)

    top = 0.9
    nitems = 4
    leg = TLegend(0.45+0.05, top-nitems*0.3/5., 0.75+0.05, top)
    leg.SetBorderSize(0)
    leg.SetHeader("95% CL limits, c#tau_{"+particle+"}="+str(ctaupoint)+" mm")
    leg.SetTextSize(0.04)

    c1 = TCanvas("c1", "Exclusion Limits", 800, 600)
    c1.cd()
    c1.SetGridx()
    c1.SetGridy()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    c1.GetPad(0).SetLogy()
    #c1.GetPad(0).SetLogx()
        
    leg.AddEntry(Exp0s,  "Expected", "l")
    leg.AddEntry(Exp1s, "#pm 1 std. deviation", "f")
    leg.AddEntry(Exp2s, "#pm 2 std. deviations", "f")

    Exp2s.GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b})/#sigma_{SM}")
    if options.channel=="ggHeavyHiggs": Exp2s.GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b}) ("+unit+")")
    Exp2s.GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
    Exp1s.GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
    Exp0s.GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
    Exp2s.SetMinimum(0.3)
    Exp2s.Draw("A3")
    Exp1s.Draw("SAME, 3")
    Exp0s.Draw("SAME, L")

    lineY = TLine(ctauPoints[0],1.,ctauPoints[len(ctauPoints)-1],1.)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
    lineY.Draw()

    leg.Draw()
    
    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)

    drawRegion(channel,top=0.7)
    drawAnalysis("LL"+chan)
    drawTagVar(tagvar)

    OUTSTRING = PLOTDIR+"/Exclusion_ctau"+str(ctaupoint)+"_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING += "_MM"
    elif isEE:
        OUTSTRING += "_EE"
    elif isComb:
        OUTSTRING += "_comb"
    if save:
        c1.Print(OUTSTRING+".png")
        c1.Print(OUTSTRING+".pdf")       
    c1.Close()
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    return Exp0s, Exp1s

def limit_vs_ctau(channel, masspoint, tagvar, save=False):
    particle = "#chi" if "SUSY" in options.channel else "#pi"
    if "HeavyHiggs" in options.channel: particle = "S"
    #suffix = "_"+method
    drawTheory = False
    
    #print OUTPUTFOLDER
    filename = OUTPUTFOLDER +"/" + chan+"_"+mass_string+"%d_"+ctau_string+"%d"
    if isMM:
       filename += "_MM"
    elif isEE:
       filename += "_EE"
    elif isComb:
       filename += "_comb"
    filename +=".txt"

    mass, ctau, val = fillValues(filename)

    #print mass, ctau, val
    Obs0s = TGraph()
    Exp0s = TGraph()
    Exp1s = TGraphAsymmErrors()
    Exp2s = TGraphAsymmErrors()

    multF = 1.
    #print "----------------"
    #print "Mass: ", masspoint

    #here loop for filling the plots
    n = 0
    for j, c in enumerate(ctau):
        #print "ctau: ", c
        name = chan+"_"+mass_string+str(masspoint)+"_"+ctau_string+str(c)#key index of val
        if isMM:
            name += "_MM"
        elif isEE:
            name += "_EE"
        elif isComb:
            name += "_comb"
        if not name in val:
            print "Key Error:", name, "not in value map"
            continue
        
        if len(val[name])<3: continue
        
        Exp0s.SetPoint(n, c, val[name][2]*multF)
        Exp1s.SetPoint(n, c, val[name][2]*multF)
        #print "Median: ", val[name][2]*multF
        Exp1s.SetPointError(n, 0., 0., val[name][2]*multF-val[name][1]*multF, val[name][3]*multF-val[name][2]*multF)
        #print "-1 sigma: ", val[name][2]*multF-val[name][1]*multF, "+ 1 sigma: ", val[name][4]*multF-val[name][3]*multF
        Exp2s.SetPoint(n, c, val[name][2]*multF)
        Exp2s.SetPointError(n, 0., 0., val[name][2]*multF-val[name][0]*multF, (val[name][4]*multF-val[name][2]*multF))
        #print "-2 sigma: ", val[name][2]*multF-val[name][0]*multF, "+ 2 sigma: ", (val[name][4]*multF-val[name][2]*multF)
        n = n+1

    n = 0
        
    Exp2s.SetLineWidth(2)
    Exp2s.SetLineStyle(1)
    Exp0s.SetLineStyle(2)
    Exp0s.SetLineWidth(3)
    Exp1s.SetFillColor(417) #kGreen
    Exp1s.SetLineColor(417) #kGreen
    Exp2s.SetFillColor(800) #kYellow
    Exp2s.SetLineColor(800) #kYellow
    Exp2s.GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
    #Exp2s.GetXaxis().SetTitleSize(Exp2s.GetXaxis().GetTitleSize()*1.25)
    Exp2s.GetXaxis().SetNoExponent(True)
    Exp2s.GetXaxis().SetMoreLogLabels(True)
    #Exp2s.GetYaxis().SetTitleSize(Exp2s.GetYaxis().GetTitleSize()*1.1)
    Exp2s.GetXaxis().SetTitleSize(0.048)
    Exp2s.GetYaxis().SetTitleSize(0.048)
    Exp2s.GetYaxis().SetTitleOffset(0.8)
    Exp2s.GetXaxis().SetTitleOffset(0.9)

    top = 0.9
    nitems = 4
    leg = TLegend(0.45+0.05, top-nitems*0.3/5., 0.75+0.05, top)
    leg.SetBorderSize(0)
    leg.SetHeader("95% CL limits, m_{"+particle+"}="+str(masspoint)+"GeV")
    leg.SetTextSize(0.04)

    c1 = TCanvas("c1", "Exclusion Limits", 800, 600)
    c1.cd()
    c1.SetGridx()
    c1.SetGridy()
    c1.GetPad(0).SetTopMargin(0.06)
    c1.GetPad(0).SetRightMargin(0.05)
    c1.GetPad(0).SetTicks(1, 1)
    c1.GetPad(0).SetLogy()
    c1.GetPad(0).SetLogx()
        
    leg.AddEntry(Exp0s,  "Expected", "l")
    leg.AddEntry(Exp1s, "#pm 1 std. deviation", "f")
    leg.AddEntry(Exp2s, "#pm 2 std. deviations", "f")

    Exp2s.GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b})/#sigma_{SM}")
    if options.channel=="ggHeavyHiggs": Exp2s.GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b}) ("+unit+")")
    Exp2s.GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
    Exp1s.GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
    Exp0s.GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
    Exp2s.SetMinimum(0.3)
    Exp2s.Draw("A3")
    Exp1s.Draw("SAME, 3")
    Exp0s.Draw("SAME, L")

    lineY = TLine(massPoints[0],1.,massPoints[len(massPoints)-1],1.)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
    lineY.Draw()

    leg.Draw()
    
    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)

    drawRegion(channel,top=0.7)
    drawAnalysis("LL"+chan)
    drawTagVar(tagvar)

    OUTSTRING = PLOTDIR+"/Exclusion_m"+str(masspoint)+"_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING += "_MM"
    elif isEE:
        OUTSTRING += "_EE"
    elif isComb:
        OUTSTRING += "_comb"
    if save:
        c1.Print(OUTSTRING+".png")
        c1.Print(OUTSTRING+".pdf")
    c1.Close()
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    return Exp0s, Exp1s

def significance_vs_ctau(channel, masspoint, tagvar, save=False):
    particle = "#chi" if "SUSY" in options.channel else "#pi"
    if "HeavyHiggs" in options.channel: particle = "S"
    drawTheory = False
    
    #print OUTPUTFOLDER
    filename = OUTPUTFOLDER +"/Significance_" + chan+"_"+mass_string+"%d_"+ctau_string+"%d"
    if isMM:
       filename += "_MM"
    elif isEE:
       filename += "_EE"
    elif isComb:
       filename += "_comb"
    filename +=".txt"

    mass, ctau, val = fillValues(filename)

    #print mass, ctau, val
    Sign  = TGraph()

    multF = 1.
    #print "----------------"
    #print "Mass: ", masspoint

    #here loop for filling the plots
    n = 0
    for j, c in enumerate(ctau):
        #print "ctau: ", c
        name = chan+"_"+mass_string+str(masspoint)+"_"+ctau_string+str(c)#key index of val
        if isMM:
            name += "_MM"
        elif isEE:
            name += "_EE"
        elif isComb:
            name += "_comb"
        if not name in val:
            print "Key Error:", name, "not in value map"
            continue
        
        if len(val[name])<1: continue      
        Sign.SetPoint(n, c, val[name][0]*multF)
        n = n+1

    n = 0

    # ---------- Significance ----------
    c2 = TCanvas("c2", "Significance", 800, 600)
    c2.cd()
    c2.SetGrid()
    c2.GetPad(0).SetTopMargin(0.06)
    c2.GetPad(0).SetRightMargin(0.05)
    c2.GetPad(0).SetTicks(1, 1)
    c2.GetPad(0).SetGridx()
    c2.GetPad(0).SetGridy()
    c2.GetPad(0).SetLogx()
    #Sign.GetYaxis().SetRangeUser(0., 5.)
    Sign.SetLineWidth(3)
    Sign.SetLineColor(2)

    Sign.GetYaxis().SetTitle("Significance; H #rightarrow "+particle+particle+" #rightarrow b #bar{b} b #bar{b}")
    Sign.GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
    Sign.GetXaxis().SetNoExponent(True)
    Sign.GetXaxis().SetMoreLogLabels(True)
    #Sign.GetYaxis().SetTitleSize(Exp2s.GetYaxis().GetTitleSize()*1.1)
    Sign.GetXaxis().SetTitleSize(0.048)
    Sign.GetYaxis().SetTitleSize(0.048)
    Sign.GetYaxis().SetTitleOffset(0.8)
    Sign.GetXaxis().SetTitleOffset(0.9)

    Sign.Draw("AL3")
    top = 0.9
    nitems = 1
    leg = TLegend(0.5, 0.2, 0.8, 0.35)
    leg.SetBorderSize(0)
    leg.SetHeader("Significance, m_{"+particle+"}="+str(masspoint)+"GeV")
    leg.SetTextSize(0.04)
    leg.AddEntry(Sign,  "Expected significance", "l")
    leg.Draw()

    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)

    drawRegion(channel,top=0.6)
    drawAnalysis("LL"+chan)
    drawTagVar(tagvar)

    OUTSTRING = PLOTDIR+"/Significance_m"+str(masspoint)+"_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING += "_MM"
    elif isEE:
        OUTSTRING += "_EE"
    elif isComb:
        OUTSTRING += "_comb"
    if save:
        c2.Print(OUTSTRING+".png")
        c2.Print(OUTSTRING+".pdf")       
    c2.Close()

    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    return Sign

def significance_vs_mass(channel, ctaupoint, tagvar, save=False):
    particle = "#chi" if "SUSY" in options.channel else "#pi"
    if "HeavyHiggs" in options.channel: particle = "S"
    drawTheory = False
    
    #print OUTPUTFOLDER
    filename = OUTPUTFOLDER +"/Significance_" + chan+"_"+mass_string+"%d_"+ctau_string+"%d"
    if isMM:
       filename += "_MM"
    elif isEE:
       filename += "_EE"
    elif isComb:
       filename += "_comb"
    filename +=".txt"

    mass, ctau, val = fillValues(filename)

    #print mass, ctau, val
    Sign  = TGraph()

    multF = 1.
    #print "----------------"
    #print "Ctau: ", ctaupoint

    #here loop for filling the plots
    n = 0
    for j, m in enumerate(mass):
        #print "mass: ", m
        name = chan+"_"+mass_string+str(m)+"_"+ctau_string+str(ctaupoint)#key index of val
        if isMM:
            name += "_MM"
        elif isEE:
            name += "_EE"
        elif isComb:
            name += "_comb"
        if not name in val:
            print "Key Error:", name, "not in value map"
            continue
        
        if len(val[name])<1: continue      
        Sign.SetPoint(n, m, val[name][0]*multF)
        n = n+1

    n = 0

    # ---------- Significance ----------
    c2 = TCanvas("c2", "Significance", 800, 600)
    c2.cd()
    c2.SetGrid()
    c2.GetPad(0).SetTopMargin(0.06)
    c2.GetPad(0).SetRightMargin(0.05)
    c2.GetPad(0).SetTicks(1, 1)
    c2.GetPad(0).SetGridx()
    c2.GetPad(0).SetGridy()
    #c2.GetPad(0).SetLogx()
    #Sign.GetYaxis().SetRangeUser(0., 5.)
    Sign.SetLineWidth(3)
    Sign.SetLineColor(2)

    Sign.GetYaxis().SetTitle("Significance; H #rightarrow "+particle+particle+" #rightarrow b #bar{b} b #bar{b}")
    Sign.GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
    Sign.GetXaxis().SetNoExponent(True)
    #Sign.GetXaxis().SetMoreLogLabels(True)
    #Sign.GetYaxis().SetTitleSize(Exp2s.GetYaxis().GetTitleSize()*1.1)
    Sign.GetXaxis().SetTitleSize(0.048)
    Sign.GetYaxis().SetTitleSize(0.048)
    Sign.GetYaxis().SetTitleOffset(0.8)
    Sign.GetXaxis().SetTitleOffset(0.9)

    Sign.Draw("AL3")
    top = 0.9
    nitems = 1
    leg = TLegend(0.5, 0.2, 0.8, 0.35)
    leg.SetBorderSize(0)
    leg.SetHeader("Significance, c#tau_{"+particle+"}="+str(ctaupoint)+" mm")
    leg.SetTextSize(0.04)
    leg.AddEntry(Sign,  "Expected significance", "l")
    leg.Draw()

    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)

    drawRegion(channel,top=0.6)
    drawAnalysis("LL"+chan)
    drawTagVar(tagvar)

    OUTSTRING = PLOTDIR+"/Significance_ctau"+str(ctaupoint)+"_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING += "_MM"
    elif isEE:
        OUTSTRING += "_EE"
    elif isComb:
        OUTSTRING += "_comb"
    if save:
        c2.Print(OUTSTRING+".png")
        c2.Print(OUTSTRING+".pdf")       
    c2.Close()

    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    return Sign



def plot_all_limits_vs_ctau(vector_expected, vector_1sigma, channel, tagvar):
    particle = "#chi" if "SUSY" in options.channel else "#pi"
    if "HeavyHiggs" in options.channel: particle = "S"
    colors = [881,801,856,920,825,2,602,880,798,5]#920 is grey
    colors = [881,801,856,825,2,602,880,798,5]#920 is grey
    c2 = TCanvas("c2", "Significance", 800, 600)
    c2.cd()
    c2.SetGrid()
    c2.GetPad(0).SetTopMargin(0.06)
    c2.GetPad(0).SetRightMargin(0.05)
    c2.GetPad(0).SetTicks(1, 1)
    c2.GetPad(0).SetGridx()
    c2.GetPad(0).SetGridy()
    c2.GetPad(0).SetLogy()
    c2.GetPad(0).SetLogx()
    top = 0.9
    nitems = len(vector_expected)
    leg = TLegend(0.45+0.05, top-nitems*0.3/5., 0.75+0.05, top)
    leg.SetBorderSize(0)
    leg.SetHeader("95% CL expected limits")
    leg.SetTextSize(0.04)

    for i, b in enumerate(vector_1sigma):
        vector_1sigma[b].SetLineColor(colors[i])
        vector_1sigma[b].SetLineStyle(2)
        vector_1sigma[b].SetLineWidth(3)
        vector_1sigma[b].SetFillStyle(3002)
        vector_1sigma[b].SetFillColorAlpha(colors[i],0.3)
        vector_1sigma[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b})/#sigma_{SM}")
        if (options.channel=="ggHeavyHiggs" or options.channel=="SUSY"): vector_1sigma[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b}) ("+unit+")")
        vector_1sigma[b].GetXaxis().SetNoExponent(True)
        vector_1sigma[b].GetXaxis().SetMoreLogLabels(True)
        vector_1sigma[b].GetXaxis().SetTitleSize(0.048)
        vector_1sigma[b].GetYaxis().SetTitleSize(0.048)
        vector_1sigma[b].GetYaxis().SetTitleOffset(0.8)
        vector_1sigma[b].GetXaxis().SetTitleOffset(0.9)
        vector_1sigma[b].GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
        if i == 0:
            vector_1sigma[b].SetMinimum(0.1)
            vector_1sigma[b].SetMaximum(50.)
            if options.channel=="ggHeavyHiggs":
            	vector_1sigma[b].SetMinimum(0.0001)
            	vector_1sigma[b].SetMaximum(1.)            
            vector_1sigma[b].Draw("A3")
        else:
            vector_1sigma[b].SetMinimum(0.1)
            vector_1sigma[b].SetMaximum(50.)
            if options.channel=="ggHeavyHiggs":
            	vector_1sigma[b].SetMinimum(0.0001)
            	vector_1sigma[b].SetMaximum(1.)            
            vector_1sigma[b].Draw("SAME,3")

    for i, b in enumerate(vector_expected):
        vector_expected[b].SetLineColor(colors[i])
        vector_expected[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b})/#sigma_{SM}")
        if (options.channel=="ggHeavyHiggs" or options.channel=="SUSY"): vector_expected[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b}) ("+unit+")")
        vector_expected[b].GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
        vector_expected[b].GetXaxis().SetNoExponent(True)
        vector_expected[b].GetXaxis().SetMoreLogLabels(True)
        vector_expected[b].GetXaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleOffset(0.8)
        vector_expected[b].GetXaxis().SetTitleOffset(0.9)
        vector_expected[b].Draw("SAME,L3")

    for b in sorted(vector_expected.keys()):
        leg.AddEntry(vector_expected[b],  "m_{"+particle+"} = "+str(b)+" GeV", "l")

    lineY = TLine(ctauPoints[0],1.,ctauPoints[len(ctauPoints)-1],1.)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
    lineY.Draw()

    leg.Draw()
    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)
    drawAnalysis("LL"+chan)
    drawRegion(channel)
    drawTagVar(tagvar)

    OUTSTRING = PLOTDIR+"/Exclusion_vs_ctau_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING +"_MM"
    elif isEE:
        OUTSTRING +"_EE"
    elif isComb:
        OUTSTRING +"_comb"
    if xs<1.:
        OUTSTRING+="_BR"+str(xs).replace('.','p')          
    c2.Print(OUTSTRING + ".png")
    c2.Print(OUTSTRING + ".pdf")

    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    #return

def plot_all_limits_vs_mass(vector_expected, vector_1sigma, channel, tagvar):
    particle = "#chi" if "SUSY" in options.channel else "#pi"
    if "HeavyHiggs" in options.channel: particle = "S"
    colors = [881,801,856,920,825,2,602,880,798,5]#920 is grey
    colors = [881,801,856,825,2,602,880,798,5]#920 is grey
    c2 = TCanvas("c2", "Significance", 800, 600)
    c2.cd()
    c2.SetGrid()
    c2.GetPad(0).SetTopMargin(0.06)
    c2.GetPad(0).SetRightMargin(0.05)
    c2.GetPad(0).SetTicks(1, 1)
    c2.GetPad(0).SetGridx()
    c2.GetPad(0).SetGridy()
    c2.GetPad(0).SetLogy()
    #c2.GetPad(0).SetLogx()
    top = 0.9
    nitems = len(vector_expected)
    leg = TLegend(0.45+0.05, top-nitems*0.3/5., 0.75+0.05, top)
    leg.SetBorderSize(0)
    leg.SetHeader("95% CL expected limits")
    leg.SetTextSize(0.04)

    for i, b in enumerate(vector_1sigma):
        vector_1sigma[b].SetLineColor(colors[i])
        vector_1sigma[b].SetLineStyle(2)
        vector_1sigma[b].SetLineWidth(3)
        vector_1sigma[b].SetFillStyle(3002)
        vector_1sigma[b].SetFillColorAlpha(colors[i],0.3)
        vector_1sigma[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b})/#sigma_{SM}")
        if (options.channel=="ggHeavyHiggs" or options.channel=="SUSY"): vector_1sigma[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b}) ("+unit+")")
        vector_1sigma[b].GetXaxis().SetNoExponent(True)
        vector_1sigma[b].GetXaxis().SetMoreLogLabels(True)
        vector_1sigma[b].GetXaxis().SetTitleSize(0.048)
        vector_1sigma[b].GetYaxis().SetTitleSize(0.048)
        vector_1sigma[b].GetYaxis().SetTitleOffset(0.8)
        vector_1sigma[b].GetXaxis().SetTitleOffset(0.9)
        vector_1sigma[b].GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
        if i == 0:
            vector_1sigma[b].SetMinimum(0.0005)
            vector_1sigma[b].SetMaximum(50.)
            vector_1sigma[b].Draw("A3")
        else:
            vector_1sigma[b].SetMinimum(0.0005)
            vector_1sigma[b].SetMaximum(50.)
            vector_1sigma[b].Draw("SAME,3")

    for i, b in enumerate(vector_expected):
        vector_expected[b].SetLineColor(colors[i])
        vector_expected[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b})/#sigma_{SM}")
        if (options.channel=="ggHeavyHiggs" or options.channel=="SUSY"): vector_expected[b].GetYaxis().SetTitle("#sigma(H) B("+particle+particle+" #rightarrow b #bar{b} b #bar{b}) ("+unit+")")
        vector_expected[b].GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
        vector_expected[b].GetXaxis().SetNoExponent(True)
        vector_expected[b].GetXaxis().SetMoreLogLabels(True)
        vector_expected[b].GetXaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleOffset(0.8)
        vector_expected[b].GetXaxis().SetTitleOffset(0.9)
        vector_expected[b].Draw("SAME,L3")

    for b in sorted(vector_expected.keys()):
        leg.AddEntry(vector_expected[b],  "c#tau_{"+particle+"} = "+str(b)+" mm", "l")

    lineY = TLine(massPoints[0],1.,massPoints[len(massPoints)-1],1.)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
    lineY.Draw()
    leg.Draw()

    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)
    drawAnalysis("LL"+chan)
    drawRegion(channel)
    drawTagVar(tagvar)

    OUTSTRING = PLOTDIR+"/Exclusion_vs_mass_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING +"_MM"
    elif isEE:
        OUTSTRING +"_EE"
    elif isComb:
        OUTSTRING +"_comb"
    if xs<1.:
        OUTSTRING+="_BR"+str(xs).replace('.','p')
    c2.Print(OUTSTRING + ".png")
    c2.Print(OUTSTRING + ".pdf")
    newFile = TFile(OUTSTRING+".root", "RECREATE")
    newFile.cd()
    for i, b in enumerate(vector_expected):
        vector_expected[b].Write(tagvar+"_exp")
    for i, b in enumerate(vector_1sigma):
        vector_1sigma[b].Write(tagvar+"_1sigma")
    c2.Write()
    newFile.Close()

    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    
def plot_all_significance_vs_ctau(vector_expected, channel, tagvar):
    particle = "#pi"
    if "HeavyHiggs" in options.channel: particle = "S"
    colors = [881,801,856,920,825,2,602,880,798,5]#920 is grey
    colors = [881,801,856,825,2,602,880,798,5]#920 is grey
    c2 = TCanvas("c2", "Significance", 800, 600)
    c2.cd()
    c2.SetGrid()
    c2.GetPad(0).SetTopMargin(0.06)
    c2.GetPad(0).SetRightMargin(0.05)
    c2.GetPad(0).SetTicks(1, 1)
    c2.GetPad(0).SetGridx()
    c2.GetPad(0).SetGridy()
    #c2.GetPad(0).SetLogy()
    c2.GetPad(0).SetLogx()
    top = 0.7
    nitems = len(vector_expected)
    leg = TLegend(0.45+0.25, top-nitems*0.3/5.-0.1, 0.75+0.2, top-0.1)
    leg.SetBorderSize(0)
    leg.SetHeader("Significance")
    leg.SetTextSize(0.04)

    for i, b in enumerate(vector_expected):
##    for b in vector_name:
        vector_expected[b].SetLineColor(colors[i])
        vector_expected[b].GetYaxis().SetTitle("Significance; H #rightarrow "+particle+particle+" #rightarrow b #bar{b} b #bar{b}")
        vector_expected[b].GetXaxis().SetTitle("c#tau_{"+particle+"} (mm)")
        vector_expected[b].GetXaxis().SetNoExponent(True)
        vector_expected[b].GetXaxis().SetMoreLogLabels(True)
        vector_expected[b].GetXaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleOffset(0.8)
        vector_expected[b].GetXaxis().SetTitleOffset(0.9)
        if i==0:
            vector_expected[b].SetMinimum(0.00005)
            vector_expected[b].SetMaximum(0.01)
            vector_expected[b].Draw("AL3")
        else:
            vector_expected[b].SetMinimum(0.00005)
            vector_expected[b].SetMaximum(0.01)
            vector_expected[b].Draw("SAME,L3")


    for b in sorted(vector_expected.keys()):
        leg.AddEntry(vector_expected[b],  "m_{"+particle+"} = "+str(b)+" GeV", "l")

    lineY = TLine(ctauPoints[0],1.,ctauPoints[len(ctauPoints)-1],1.)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
    lineY.Draw()

    leg.Draw()
    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)
    drawAnalysis("LL"+chan)
    drawRegion(channel)
    drawTagVar(tagvar)
    
    OUTSTRING = PLOTDIR+"/Significance_vs_ctau_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING += "_MM"
    elif isEE:
        OUTSTRING += "_EE"
    elif isComb:
        OUTSTRING += "_comb"
    if xs<1.:
        OUTSTRING+="_BR"+str(xs).replace('.','p')
    c2.Print(OUTSTRING+".png")
    c2.Print(OUTSTRING+".pdf")
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    #return

def plot_all_significance_vs_mass(vector_expected, channel, tagvar):
    particle = "#pi" 
    if "HeavyHiggs" in options.channel: particle = "S"
    colors = [881,801,856,920,825,2,602,880,798,5]#920 is grey
    colors = [881,801,856,825,2,602,880,798,5]#920 is grey
    c2 = TCanvas("c2", "Significance", 800, 600)
    c2.cd()
    c2.SetGrid()
    c2.GetPad(0).SetTopMargin(0.06)
    c2.GetPad(0).SetRightMargin(0.05)
    c2.GetPad(0).SetTicks(1, 1)
    c2.GetPad(0).SetGridx()
    c2.GetPad(0).SetGridy()
    #c2.GetPad(0).SetLogy()
    #c2.GetPad(0).SetLogx()
    top = 0.9
    nitems = len(vector_expected)
    leg = TLegend(0.45+0.25, top-nitems*0.3/5.-0.1, 0.75+0.2, top-0.1)
    leg.SetBorderSize(0)
    leg.SetHeader("Significance")
    leg.SetTextSize(0.04)

    for i, b in enumerate(vector_expected):
##    for b in vector_name:
        vector_expected[b].SetLineColor(colors[i])
        vector_expected[b].GetYaxis().SetTitle("Significance; H #rightarrow "+particle+particle+" #rightarrow b #bar{b} b #bar{b}")
        vector_expected[b].GetXaxis().SetTitle("m_{"+particle+"} (GeV)")
        vector_expected[b].GetXaxis().SetNoExponent(True)
        vector_expected[b].GetXaxis().SetMoreLogLabels(True)
        vector_expected[b].GetXaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleSize(0.048)
        vector_expected[b].GetYaxis().SetTitleOffset(0.8)
        vector_expected[b].GetXaxis().SetTitleOffset(0.9)
        if i==0:
            vector_expected[b].SetMinimum(0.0005)
            #vector_expected[b].SetMaximum(40)
            vector_expected[b].Draw("AL3")
        else:
            vector_expected[b].SetMinimum(0.0005)
            #vector_expected[b].SetMaximum(40)
            vector_expected[b].Draw("SAME,L3")


    for b in sorted(vector_expected.keys()):
        leg.AddEntry(vector_expected[b],  "c#tau_{#pi} = "+str(b)+" mm", "l")

    lineY = TLine(massPoints[0],1.,massPoints[len(massPoints)-1],1.)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
    lineY.Draw()

    leg.Draw()
    if PRELIMINARY:
        drawCMS(samples, LUMI, "Preliminary",left_marg_CMS=0.3)
    else:
        drawCMS(samples, LUMI, "",left_marg_CMS=0.32)
    drawAnalysis("LL"+chan)
    drawRegion(channel)
    drawTagVar(tagvar)
    
    OUTSTRING = PLOTDIR+"/Significance_vs_mass_"+tagvar+"_"+chan
    if isMM:
        OUTSTRING += "_MM"
    elif isEE:
        OUTSTRING += "_EE"
    elif isComb:
        OUTSTRING += "_comb"
    if xs<1.:
        OUTSTRING+="_BR"+str(xs).replace('.','p')
    c2.Print(OUTSTRING+".png")
    c2.Print(OUTSTRING+".pdf")
    if not gROOT.IsBatch(): raw_input("Press Enter to continue...")
    #return




vect_exp = vect_1sigma = dummy = {}
vect_exp_m = vect_1sigma_m = dummy = {}

if options.fom=="Limits":
    if "SUSY" not in options.channel:
        for a in massPoints:
            vect_exp[a], vect_1sigma[a] = limit_vs_ctau(options.channel,a,options.tagvar)
        plot_all_limits_vs_ctau(vect_exp,vect_1sigma,options.channel,options.tagvar)
    for c in ctauPoints:
        vect_exp_m[c], vect_1sigma_m[c] = limit_vs_mass(options.channel,c,options.tagvar)
    plot_all_limits_vs_mass(vect_exp_m,vect_1sigma_m,options.channel,options.tagvar)

elif options.fom=="Significance":
    if "SUSY" not in options.channel:
        for a in massPoints:
            vect_exp[a] = significance_vs_ctau(options.channel,a,options.tagvar)
        plot_all_significance_vs_ctau(vect_exp,options.channel,options.tagvar)
    for c in ctauPoints:
        vect_exp_m[c] = significance_vs_mass(options.channel,c,options.tagvar)
    plot_all_significance_vs_mass(vect_exp_m,options.channel,options.tagvar)
