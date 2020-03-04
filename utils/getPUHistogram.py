#! /usr/bin/env python

import os
from array import array
from ROOT import gStyle, TFile, TH1F, TCanvas, TLegend, ROOT, gROOT
import numpy as np

gStyle.SetOptStat(0)

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
#parser.add_option("-d", "--dataFile", action="store", type="string", default=False, dest="dataFileName")
#parser.add_option("-m", "--mcFile", action="store", type="string", default=False, dest="mcFileName")
#parser.add_option("-r", "--mcReweightedFile", action="store", type="string", default=False, dest="mcReweightedFileName")
#parser.add_option("-p", "--plot", action="store_true", default=False, dest="doPlot")
parser.add_option("-r", "--runera", action="store", type="string", default="", dest="runera")
parser.add_option("-s", "--save", action="store_true", default=False, dest="save")
parser.add_option("-b", "--batch", action="store_true", default=False, dest="batch")
(options, args) = parser.parse_args()
if options.batch: gROOT.SetBatch(True)

#scp lxplus.cern.ch:/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt data/JSON/
#pileupCalc.py -i data/JSON/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt --inputLumiJSON data/JSON/pileup_latest.txt --calcMode true --minBiasXsec 71300 --maxPileupBin 60 --numPileupBins 60 data/PU_71300.root

#Older scenarios
#https://github.com/cms-sw/cmssw/blob/CMSSW_8_1_X/SimGeneral/MixingModule/python/mix_2016_25ns_Moriond17MC_PoissonOOTPU_cfi.py
scenarioMoriond2016 = "2016_25ns_Moriond17MC_PoissonOOTPU"
probValueMoriond2016 = [1.78653e-05 ,2.56602e-05 ,5.27857e-05 ,8.88954e-05 ,0.000109362 ,0.000140973 ,0.000240998 ,0.00071209 ,0.00130121 ,0.00245255 ,0.00502589 ,0.00919534 ,0.0146697 ,0.0204126 ,0.0267586 ,0.0337697 ,0.0401478 ,0.0450159 ,0.0490577 ,0.0524855 ,0.0548159 ,0.0559937 ,0.0554468 ,0.0537687 ,0.0512055 ,0.0476713 ,0.0435312 ,0.0393107 ,0.0349812 ,0.0307413 ,0.0272425 ,0.0237115 ,0.0208329 ,0.0182459 ,0.0160712 ,0.0142498 ,0.012804 ,0.011571 ,0.010547 ,0.00959489 ,0.00891718 ,0.00829292 ,0.0076195 ,0.0069806 ,0.0062025 ,0.00546581 ,0.00484127 ,0.00407168 ,0.00337681 ,0.00269893 ,0.00212473 ,0.00160208 ,0.00117884 ,0.000859662 ,0.000569085 ,0.000365431 ,0.000243565 ,0.00015688 ,9.88128e-05 ,6.53783e-05 ,3.73924e-05 ,2.61382e-05 ,2.0307e-05 ,1.73032e-05 ,1.435e-05 ,1.36486e-05 ,1.35555e-05 ,1.37491e-05 ,1.34255e-05 ,1.33987e-05 ,1.34061e-05 ,1.34211e-05 ,1.34177e-05 ,1.32959e-05 ,1.33287e-05]

#https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2016_25ns_UltraLegacy_PoissonOOTPU_cfi.py
scenario2016 = "2016_25ns_UltraLegacy_PoissonOOTPU"
probValue2016 = [
    8.89374611122e-07, 1.1777062868e-05, 3.99725585118e-05, 0.000129888015252, 0.000265224848687,
    0.000313088635109, 0.000353781668514, 0.000508787237162, 0.000873670065767, 0.00147166880932,
    0.00228230649018, 0.00330375581273, 0.00466047608406, 0.00624959203029, 0.00810375867901,
    0.010306521821, 0.0129512453978, 0.0160303925502, 0.0192913204592, 0.0223108613632,
    0.0249798930986, 0.0273973789867, 0.0294402350483, 0.031029854302, 0.0324583524255,
    0.0338264469857, 0.0351267479019, 0.0360320204259, 0.0367489568401, 0.0374133183052,
    0.0380352633799, 0.0386200967002, 0.039124376968, 0.0394201612616, 0.0394673457109,
    0.0391705388069, 0.0384758587461, 0.0372984548399, 0.0356497876549, 0.0334655175178,
    0.030823567063, 0.0278340752408, 0.0246009685048, 0.0212676009273, 0.0180250593982,
    0.0149129830776, 0.0120582333486, 0.00953400069415, 0.00738546929512, 0.00563442079939,
    0.00422052915668, 0.00312446316347, 0.00228717533955, 0.00164064894334, 0.00118425084792,
    0.000847785826565, 0.000603466454784, 0.000419347268964, 0.000291768785963, 0.000199761337863,
    0.000136624574661, 9.46855200945e-05, 6.80243180179e-05, 4.94806013765e-05, 3.53122628249e-05,
    2.556765786e-05, 1.75845711623e-05, 1.23828210848e-05, 9.31669724108e-06, 6.0713272037e-06,
    3.95387384933e-06, 2.02760874107e-06, 1.22535149516e-06, 9.79612472109e-07, 7.61730246474e-07,
    4.2748847738e-07, 2.41170461205e-07, 1.38701083552e-07, 3.37678010922e-08, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0]

#https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2017_25ns_UltraLegacy_PoissonOOTPU_cfi.py
scenario2017 = "2017_25ns_UltraLegacy_PoissonOOTPU"
probValue2017 = [
    1.1840841518e-05, 3.46661037703e-05, 8.98772521472e-05, 7.47400487733e-05, 0.000123005176624,
    0.000156501700614, 0.000154660478659, 0.000177496185603, 0.000324149805611, 0.000737524009713,
    0.00140432980253, 0.00244424508696, 0.00380027898037, 0.00541093042612, 0.00768803501793,
    0.010828224552, 0.0146608623707, 0.01887739113, 0.0228418813823, 0.0264817796874,
    0.0294637401336, 0.0317960986171, 0.0336645950831, 0.0352638818387, 0.036869429333,
    0.0382797316998, 0.039386705577, 0.0398389681346, 0.039646211131, 0.0388392805703,
    0.0374195678161, 0.0355377892706, 0.0333383902828, 0.0308286549265, 0.0282914440969,
    0.0257860718304, 0.02341635055, 0.0213126338243, 0.0195035612803, 0.0181079838989,
    0.0171991315458, 0.0166377598339, 0.0166445341361, 0.0171943735369, 0.0181980997278,
    0.0191339792146, 0.0198518804356, 0.0199714909193, 0.0194616474094, 0.0178626975229,
    0.0153296785464, 0.0126789254325, 0.0100766041988, 0.00773867100481, 0.00592386091874,
    0.00434706240169, 0.00310217013427, 0.00213213401899, 0.0013996000761, 0.000879148859271,
    0.000540866009427, 0.000326115560156, 0.000193965828516, 0.000114607606623, 6.74262828734e-05,
    3.97805301078e-05, 2.19948704638e-05, 9.72007976207e-06, 4.26179259146e-06, 2.80015581327e-06,
    1.14675436465e-06, 2.52452411995e-07, 9.08394910044e-08, 1.14291987912e-08, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0]

#https://github.com/cms-sw/cmssw/blob/master/SimGeneral/MixingModule/python/mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi.py
scenario2018 = "2018_25ns_UltraLegacy_PoissonOOTPU"
probValue2018 = [
    8.89374611122e-07, 1.1777062868e-05, 3.99725585118e-05, 0.000129888015252, 0.000265224848687,
    0.000313088635109, 0.000353781668514, 0.000508787237162, 0.000873670065767, 0.00147166880932,
    0.00228230649018, 0.00330375581273, 0.00466047608406, 0.00624959203029, 0.00810375867901,
    0.010306521821, 0.0129512453978, 0.0160303925502, 0.0192913204592, 0.0223108613632,
    0.0249798930986, 0.0273973789867, 0.0294402350483, 0.031029854302, 0.0324583524255,
    0.0338264469857, 0.0351267479019, 0.0360320204259, 0.0367489568401, 0.0374133183052,
    0.0380352633799, 0.0386200967002, 0.039124376968, 0.0394201612616, 0.0394673457109,
    0.0391705388069, 0.0384758587461, 0.0372984548399, 0.0356497876549, 0.0334655175178,
    0.030823567063, 0.0278340752408, 0.0246009685048, 0.0212676009273, 0.0180250593982,
    0.0149129830776, 0.0120582333486, 0.00953400069415, 0.00738546929512, 0.00563442079939,
    0.00422052915668, 0.00312446316347, 0.00228717533955, 0.00164064894334, 0.00118425084792,
    0.000847785826565, 0.000603466454784, 0.000419347268964, 0.000291768785963, 0.000199761337863,
    0.000136624574661, 9.46855200945e-05, 6.80243180179e-05, 4.94806013765e-05, 3.53122628249e-05,
    2.556765786e-05, 1.75845711623e-05, 1.23828210848e-05, 9.31669724108e-06, 6.0713272037e-06,
    3.95387384933e-06, 2.02760874107e-06, 1.22535149516e-06, 9.79612472109e-07, 7.61730246474e-07,
    4.2748847738e-07, 2.41170461205e-07, 1.38701083552e-07, 3.37678010922e-08, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0]

if options.runera=="Moriond2016":
    scenario  = scenarioMoriond2016
    probValue = np.array(probValueMoriond2016)
    bins = 100
elif options.runera=="2016":
    scenario  = scenario2016
    probValue = np.array(probValue2016)
    bins = 200
elif options.runera=="2017":
    scenario  = scenario2017
    probValue = np.array(probValue2017)
    bins = 200
elif options.runera=="2018":
    scenario  = scenario2018
    probValue = np.array(probValue2018)
    bins = 200
else:
    print "Wrong data era! Aborting..."
    exit()

mc = TH1F(scenario, "True nPV distribution", bins, 0, bins)
mc.Sumw2()
for i in range(len(probValue)): mc.SetBinContent(i+1, probValue[i])
mc.SetLineWidth(3)
mc.SetLineColor(1)
mc.SetLineStyle(2)
mc.Scale(1./mc.Integral())

if options.save:
    outFile = TFile("data/PU_MC_"+scenario+".root", "RECREATE")
    outFile.cd()
    mc.Write()
    outFile.Close()

    print "Histograms written to data/PU_MC_"+scenario+".root file"
    exit()
   

puFile = TFile("data/PU_69200_"+str(options.runera)+".root", "READ")
data = puFile.Get("pileup")
data.SetLineWidth(2)
data.SetLineColor(1)
data.Scale(1./data.Integral())


puUpFile = TFile("data/PU_72380_"+str(options.runera)+".root", "READ")
dataUp = puUpFile.Get("pileup")
dataUp.SetLineWidth(2)
dataUp.SetLineColor(634)
dataUp.Scale(1./dataUp.Integral())


puDownFile = TFile("data/PU_66020_"+str(options.runera)+".root", "READ")
dataDown = puDownFile.Get("pileup")
dataDown.SetLineWidth(2)
dataDown.SetLineColor(598)
dataDown.Scale(1./dataDown.Integral())

ratio = data.Clone("ratio")
ratioUp = dataUp.Clone("ratioUp")
ratioDown = dataDown.Clone("ratioDown")

ratio.Divide(mc)
ratioUp.Divide(mc)
ratioDown.Divide(mc)

#outFile = TFile("../data/PU.root", "RECREATE")
#outFile.cd()
#mc.Write()
#data.Write()
#dataUp.Write()
#dataDown.Write()
#ratio.Write()
#ratioUp.Write()
#ratioDown.Write()
#outFile.Close()
#print "Histograms written to ../data/PU.root file"

leg = TLegend(0.5, 0.7, 0.98, 0.9)
leg.SetBorderSize(0)
leg.SetFillStyle(0) #1001
leg.SetFillColor(0)
leg.SetHeader("Pile-up reweighting")
leg.AddEntry(dataUp, "Up", "pl")
leg.AddEntry(data, "Central", "pl")
leg.AddEntry(dataDown, "Down", "pl")
#leg.AddEntry(mc, "MC 25ns", "pl")
leg.AddEntry(mc, scenario, "pl")

c1 = TCanvas("c1", "PileUp reweighting", 800, 800)
c1.cd()
c1.GetPad(0).SetTopMargin(0.06)
c1.GetPad(0).SetRightMargin(0.05)
c1.GetPad(0).SetTicks(1, 1)
dataDown.SetTitle(";number of true interactions")
dataDown.GetXaxis().SetRangeUser(0., 100)
dataDown.Draw("HIST")
dataUp.Draw("SAME, HIST")
data.Draw("SAME, HIST")
mc.Draw("SAME, L")
leg.Draw()
c1.Print("PU/PU_%s.pdf"%scenario)
c1.Print("PU/PU_%s.png"%scenario)

