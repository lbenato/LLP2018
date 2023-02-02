#! /usr/bin/env python                                                                                                                  
import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory
from ROOT import TFile, TChain, TTree, TCut, TH1F, TH2F, THStack, TGraph, TH3F
from ROOT import TStyle, TCanvas, TPad
from ROOT import TLegend, TLatex, TText, TLine, TProfile

from Analyzer.LLP2018.drawUtils import *

#import optparse
#usage = "usage: %prog [options]"
#parser = optparse.OptionParser(usage)
#parser.add_option("-b", "--bash", action="store_true", default=False, dest="bash")
#(options, args) = parser.parse_args()
gROOT.SetBatch(True)
gStyle.SetOptStat(0000)

data = [
    "pickevents_275309_875415530","pickevents_277096_153555117","pickevents_279931_4073593513","pickevents_319910_457404349","pickevents_276811_244034371","pickevents_279029_387083289",
    "pickevents_302485_987393715"]
MAIN = "/afs/desy.de/user/l/lbenato/LLP_code_slc7/CMSSW_10_2_18/src/Analyzer/LLP2018/"

for d in data:
    chain = TChain("ntuple/tree")
    chain.Add(MAIN+d+".root")

    h_xy_dt   = TH2F("h_xy_dt","",     100, -10, 10, 100, -10, 10)
    h_xy_ecal = TH2F("h_xy_ecal","",   100, -10, 10, 100, -10, 10)
    h_yz_dt   = TH2F("h_yz_dt","",     100, -10, 10, 100, -10, 10)
    h_yz_ecal = TH2F("h_yz_ecal","",   100, -10, 10, 100, -10, 10)
    h_xz_dt   = TH2F("h_xz_dt","",     100, -10, 10, 100, -10, 10)
    h_xz_ecal = TH2F("h_xz_ecal","",   100, -10, 10, 100, -10, 10)

    h_xyz_dt   = TH3F("h_xyz_dt","",   100, -10, 10, 100, -10, 10, 100, -10, 10)
    h_xyz_ecal = TH3F("h_xyz_ecal","", 100, -10, 10, 100, -10, 10, 100, -10, 10)

    #h_3D = TH1F("rh","", 300, 0, 3000)
    #gh.Sumw2()
    #rh.Sumw2()

    chain.Project("h_xy_dt", "DTSegments.y/100.:DTSegments.x/100.", "")
    chain.Project("h_xy_ecal", "EcalRecHitsAK4.y/100.:EcalRecHitsAK4.x/100.", "")
    chain.Project("h_xyz_dt", "DTSegments.y/100.:DTSegments.x/100.:DTSegments.z/100.", "")
    chain.Project("h_xyz_ecal", "EcalRecHitsAK4.y/100.:EcalRecHitsAK4.x/100.:EcalRecHitsAK4.z/100.", "")
    chain.Project("h_xz_dt", "DTSegments.x/100.:DTSegments.z/100.", "")
    chain.Project("h_xz_ecal", "EcalRecHitsAK4.x/100.:EcalRecHitsAK4.z/100.", "")
    chain.Project("h_yz_dt", "DTSegments.y/100.:DTSegments.z/100.", "")
    chain.Project("h_yz_ecal", "EcalRecHitsAK4.y/100.:EcalRecHitsAK4.z/100.", "")
    #chain.Project("rh", "RecHigMass", "")

    h_xy_dt.SetMarkerColor(4)
    h_xy_dt.SetMarkerStyle(20)
    h_xy_ecal.SetMarkerColor(2)
    h_xy_ecal.SetMarkerStyle(20)

    h_xy_dt.Fit("pol1")

    h_xyz_dt.SetMarkerColor(4)
    h_xyz_dt.SetMarkerStyle(20)
    h_xyz_ecal.SetMarkerColor(2)
    h_xyz_ecal.SetMarkerStyle(20)

    h_xz_dt.SetMarkerColor(4)
    h_xz_dt.SetMarkerStyle(20)
    h_xz_ecal.SetMarkerColor(2)
    h_xz_ecal.SetMarkerStyle(20)

    h_xz_dt.Fit("pol1")

    h_yz_dt.SetMarkerColor(4)
    h_yz_dt.SetMarkerStyle(20)
    h_yz_ecal.SetMarkerColor(2)
    h_yz_ecal.SetMarkerStyle(20)

    h_yz_dt.Fit("pol1")

    leg = TLegend(0.75, 0.8, 1., 1.)
    #leg.SetHeader(d)
    leg.AddEntry(h_xy_dt,"DT segments","P")
    leg.AddEntry(h_xy_ecal,"EB rec hits","P")

    can_xy = TCanvas("can_xy","can_xy",900,800)
    can_xy.cd()
    can_xy.SetRightMargin(0.05)
    #can_xy.SetLogy()
    h_xy_dt.Draw("")
    h_xy_ecal.Draw("sames")

    h_xy_dt.GetXaxis().SetTitle("x (m)")
    h_xy_dt.GetYaxis().SetTitle("y (m)")
    h_xy_dt.GetYaxis().SetTitleOffset(1.4)
    h_xy_ecal.GetXaxis().SetTitle("x (m)")
    h_xy_ecal.GetYaxis().SetTitle("y (m)")

    leg.Draw()
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextAlign(33)
    latex.SetTextSize(0.04)
    latex.SetTextFont(62)
    latex.DrawLatex(0.20, 0.96, "CMS")
    latex.SetTextFont(52)
    latex.DrawLatex(0.36, 0.96, "Simulation")
    can_xy.Update()
    can_xy.Print(MAIN+d+'_xy.png')
    can_xy.Print(MAIN+d+'_xy.pdf')
    can_xy.Close()
    h_xy_dt.Delete()
    h_xy_ecal.Delete()
    leg.Delete()


    can_xz = TCanvas("can_xz","can_xz",900,800)
    can_xz.cd()
    can_xz.SetRightMargin(0.05)
    #can_xz.SetLogy()
    h_xz_dt.Draw("")
    h_xz_ecal.Draw("sames")
    h_xz_dt.GetXaxis().SetTitle("z (m)")
    h_xz_dt.GetYaxis().SetTitle("x (m)")
    h_xz_ecal.GetXaxis().SetTitle("z (m)")
    h_xz_ecal.GetYaxis().SetTitle("x (m)")
    h_xz_dt.GetYaxis().SetTitleOffset(1.4)
    leg = TLegend(0.75, 0.8, 1., 1.)
    #leg.SetHeader(d)
    leg.AddEntry(h_xz_dt,"DT segments","P")
    leg.AddEntry(h_xz_ecal,"EB rec hits","P")
    leg.Draw()
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextAlign(33)
    latex.SetTextSize(0.04)
    latex.SetTextFont(62)
    latex.DrawLatex(0.20, 0.96, "CMS")
    latex.SetTextFont(52)
    latex.DrawLatex(0.36, 0.96, "Simulation")
    can_xz.Update()
    can_xz.Print(MAIN+d+'_xz.png')
    can_xz.Print(MAIN+d+'_xz.pdf')
    can_xz.Close()
    h_xz_dt.Delete()
    h_xz_ecal.Delete()
    leg.Delete()

    can_yz = TCanvas("can_yz","can_yz",900,800)
    can_yz.cd()
    can_yz.SetRightMargin(0.05)
    #can_yz.SetLogy()
    h_yz_dt.Draw("")
    h_yz_ecal.Draw("sames")
    h_yz_dt.GetXaxis().SetTitle("z (m)")
    h_yz_dt.GetYaxis().SetTitle("y (m)")
    h_yz_ecal.GetXaxis().SetTitle("z (m)")
    h_yz_ecal.GetYaxis().SetTitle("y (m)")
    h_yz_dt.GetYaxis().SetTitleOffset(1.4)
    leg = TLegend(0.75, 0.8, 1., 1.)
    #leg.SetHeader(d)
    leg.AddEntry(h_yz_dt,"DT segments","P")
    leg.AddEntry(h_yz_ecal,"EB rec hits","P")
    leg.Draw()
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextAlign(33)
    latex.SetTextSize(0.04)
    latex.SetTextFont(62)
    latex.DrawLatex(0.20, 0.96, "CMS")
    latex.SetTextFont(52)
    latex.DrawLatex(0.36, 0.96, "Simulation")
    can_yz.Update()
    can_yz.Print(MAIN+d+'_yz.png')
    can_yz.Print(MAIN+d+'_yz.pdf')
    can_yz.Close()
    h_yz_dt.Delete()
    h_yz_ecal.Delete()
    leg.Delete()


    can_xyz = TCanvas("can_xyz","can_xyz",900,800)
    can_xyz.cd()
    #can_xyz.SetRightMargin(0.05)
    #can_xyz.SetLogy()
    h_xyz_dt.Draw("")
    h_xyz_ecal.Draw("sames")
    h_xyz_dt.GetXaxis().SetTitle("z (m)")
    h_xyz_dt.GetYaxis().SetTitle("x (m)")
    h_xyz_dt.GetZaxis().SetTitle("y (m)")
    h_xyz_ecal.GetXaxis().SetTitle("z (m)")
    h_xyz_ecal.GetYaxis().SetTitle("x (m)")
    h_xyz_ecal.GetZaxis().SetTitle("y (m)")
    h_xyz_dt.GetXaxis().SetTitleOffset(1.4)
    h_xyz_dt.GetYaxis().SetTitleOffset(1.8)
    h_xyz_dt.GetZaxis().SetTitleOffset(1.4)
    leg = TLegend(0.75, 0.8, 1., 1.)
    #leg.SetHeader(d)
    leg.AddEntry(h_xyz_dt,"DT segments","P")
    leg.AddEntry(h_xyz_ecal,"EB rec hits","P")
    leg.Draw()
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextAlign(33)
    latex.SetTextSize(0.04)
    latex.SetTextFont(62)
    latex.DrawLatex(0.20, 0.96, "CMS")
    latex.SetTextFont(52)
    latex.DrawLatex(0.36, 0.96, "Simulation")
    can_xyz.Update()
    can_xyz.Print(MAIN+d+'_xyz.png')
    can_xyz.Print(MAIN+d+'_xyz.pdf')
    can_xyz.Close()
    h_xyz_dt.Delete()
    h_xyz_ecal.Delete()
    #raw_input("Press Enter to continue...")
    leg.Delete()
