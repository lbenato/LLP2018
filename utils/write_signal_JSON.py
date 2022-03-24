#! /usr/bin/env python
import json
import os, multiprocessing
import copy
import math
from array import array
from ROOT import ROOT, gROOT, gStyle, gRandom, TSystemDirectory, gPad
from ROOT import TFile, TChain, TTree, TCut, TH1, TH1F, TH1D, TH2F, THStack, TGraph, TGraphAsymmErrors
from ROOT import TStyle, TCanvas, TPad, gDirectory
from ROOT import TLegend, TLatex, TText, TLine, TBox, TGaxis
import uproot
import root_numpy
import numpy as np


#### IMPORT SAMPLES AND VARIABLES DICTIONARIES ####
import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-l", "--lists", action="store", type="string", dest="lists", default="")
parser.add_option("-i", "--input_folder", action="store", type="string", dest="input_folder", default="", help='the input folder containing the CRAB outputs')
parser.add_option("-o", "--output_folder", action="store", type="string", dest="output_folder", default="", help='the output folder containing the hadd of CRAB outputs')
parser.add_option("-g", "--groupofsamples", action="store", type="string", dest="groupofsamples", default="")
parser.add_option("-c", "--channel", action="store", type="string", dest="channel", default="", help='decay channel of neutralinos')
(options, args) = parser.parse_args()


if options.lists == "v6_calo_AOD_2016":
    from Analyzer.LLP2018.samplesAOD2016 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
    RUN_ERA = 2016
elif options.lists == "v6_calo_AOD_2017":
    from Analyzer.LLP2018.samplesAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
    RUN_ERA = 2017
elif options.lists == "v6_calo_AOD_2018":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    RUN_ERA = 2018
else:
    print "Invalid list, aborting"
    RUN_ERA = 0
    exit()

chan = ""
if "HZ" in options.channel:
    INPUTDIR = ("/pnfs/desy.de/cms/tier2/store/user/lbenato/v6_calo_AOD_%s_gen_SUSY_HZ_08December2021/")% str(RUN_ERA)
    chan = "HZ"

elif "ZZ" in options.channel:
    INPUTDIR = ("/pnfs/desy.de/cms/tier2/store/user/lbenato/v6_calo_AOD_%s_gen_SUSY_ZZ_08December2021/")% str(RUN_ERA)
    chan = "ZZ"

else:
    #First version, HH only
    INPUTDIR = ("/pnfs/desy.de/cms/tier2/store/user/lbenato/v6_calo_AOD_%s_07October2021/")% str(RUN_ERA)
    chan = "HH"

sample_list = ["SUSY_central"]
dicty = {}
for s in sample_list:
    for ss in samples[s]["files"]:
        #print ss
        #print requests[ss]
        s1 = requests[ss][1:].split('/')[0]
        #print s1
        dicty[ss] = s1+'/crab_'+ss+'/'
        if s=="DYJetsToLL" and RUN_ERA==2018:
            new_ss = ss.replace('pythia8','pythia')
            dicty[ss] = s1+'8/crab_'+new_ss+'/'

#print dicty
sample_to_loop = dicty.keys()

list_of_variables = ["EventNumber","LumiNumber","RunNumber","m_chi","is_central","ctau"]
for s in sample_to_loop:
    print s
    #read input files in crab folder
    IN = INPUTDIR + dicty[s]
    #print(IN)
    if not(os.path.exists(IN)):
        print IN , " : empty dir, go to next..."
        continue

    date_subdirs = [x for x in os.listdir(IN) if os.path.isdir(os.path.join(IN, x))]
    if(len(date_subdirs)>1):
        print("Multiple date/time subdirs, aborting...")
        exit()
    IN += date_subdirs[0]
    num_subdirs = [x for x in os.listdir(IN) if os.path.isdir(os.path.join(IN, x))]

    m_chi       = np.array([])
    ctau        = np.array([])
    #is_central  = np.array([])
    #RunNumber   = np.array([])
    LumiNumber  = np.array([])
    #EventNumber = np.array([])

    for subd in num_subdirs:
        INPS = IN + "/"+subd+"/"
        root_files = [INPS+x for x in os.listdir(INPS) if os.path.isfile(os.path.join(INPS, x))]
        print "Loading files in ", INPS, " . . . "
        gen = uproot.iterate(root_files,"ntuple/tree",list_of_variables)
        n_arr = 0
        for arrays in gen:
            m_chi = np.concatenate((m_chi,np.array(arrays["m_chi"])))
            ctau = np.concatenate((ctau,np.array(arrays["ctau"])))
            #is_central = np.concatenate((is_central,np.array(arrays["is_central"])))
            #RunNumber = np.concatenate((RunNumber,np.array(arrays["RunNumber"])))
            LumiNumber = np.concatenate((LumiNumber,np.array(arrays["LumiNumber"])))
            #EventNumber = np.concatenate((EventNumber,np.array(arrays["EventNumber"])))
            n_arr+=1
            if n_arr%10==0:
                print "Loading array n. ", n_arr
            del arrays
            ##if n_arr>10: break

    #I have loaded all the crab outputs
    masses = np.unique(m_chi)
    ctaus = np.unique(ctau)
    for m in masses:
        for c in ctaus:
            sample_name = s+"_m"+str(int(m))+"_ctau"+str(int(c))
            print sample_name
            mask = np.logical_and(m_chi==m, ctau==c)
            #print m_chi[mask]
            #print ctau[mask]
            #print RunNumber[mask]
            #print LumiNumber[mask]
            #print EventNumber[mask]
            lumis =  np.unique(LumiNumber[mask].astype(int))
            lumi_format = np.repeat(lumis,2).reshape(lumis.shape[0],2).tolist()
            content = '{"1" :'+str(lumi_format)+'}'
            lumi_filename = "/afs/desy.de/user/l/lbenato/LLP_code_slc7/CMSSW_10_2_18/src/Analyzer/LLP2018/dataAOD/JSON/"+str(RUN_ERA)+"/"+chan+"/"
            if not os.path.isdir(lumi_filename):
                os.mkdir(lumi_filename)
            lumi_filename+=sample_name+"_"+chan+"_JSON.txt"
            print content
            print "Open: ",lumi_filename
            with open(lumi_filename,"w") as js:
                js.write(content)
            print "Written: ", lumi_filename

#Usage example
#python utils/write_signal_JSON.py -l v6_calo_AOD_2018 -c HZ
