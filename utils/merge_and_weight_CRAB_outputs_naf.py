#!/usr/bin/env python
import os, re
import multiprocessing
import logging
import commands
import math, time
import sys
from ROOT import TObject, TFile, TH1, TH1F
#from Analyzer.LLP2018.samples import sample
from array import array

print "*****************************************************************************"
print "\n"
print "Please input the correct lumi!!! Taking lumi for prod v5, SingleMuon dataset"
print "\n"
#LUMI = 5750.126252897#met_v0_19Aug2019, RunB v2 ver 2
LUMI        =  35867# full Run 2016 with normtag#36814# in pb-1
print LUMI, " fb -1"
print "*****************************************************************************"


# use the following lists to include/exclude samples to be merged

blacklist = []
whitelist = []

#TIP = "/pnfs/desy.de/cms/tier2/store/user/lbenato/"
#DEST = "/nfs/dust/cms/user/lbenato/v1/"


########## DO NOT TOUCH BELOW THIS POINT ##########

###argparse
#import argparse

#parser = argparse.ArgumentParser(description='combine the CRAB outputs into one file')
#parser.add_argument('folder', help='the folder containing the CRAB outputs')
#args = parser.parse_args()

#if not os.path.exists(os.path.expandvars(args.folder)):
#    print '--- ERROR ---'
#    print '  \''+args.folder+'\' path not found'
#    print '  please point to the correct path to the folder containing the CRAB output'
#    print '  example on NAF: '
#    print TIP
#    print
#    exit()

###optparse
import optparse

usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-l", "--lists", action="store", type="string", dest="lists", default="")
parser.add_option("-i", "--input_folder", action="store", type="string", dest="input_folder", default="", help='the input folder containing the CRAB outputs')
parser.add_option("-o", "--output_folder", action="store", type="string", dest="output_folder", default="", help='the output folder containing the hadd of CRAB outputs')
parser.add_option("-g", "--groupofsamples", action="store", type="string", dest="groupofsamples", default="")
(options, args) = parser.parse_args()


if options.lists == "v0_pfXTag_calo":
    from Analyzer.LLP2018.samples import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v1_gen_production_calo":
    from Analyzer.LLP2018.samples import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v1_pfXTag_puppi_calo":
    from Analyzer.LLP2018.samples import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v2_pfXTag_puppi_calo":
    from Analyzer.LLP2018.samples import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v2_pfXTag_puppi_calo":
    from Analyzer.LLP2018.samples import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v0_SUSY_calo_AOD_2018":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v0_SUSY_calo_MINIAOD_2018":
    from Analyzer.LLP2018.samplesMINIAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_MINIAOD_2018 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v0_ggHeavyHiggs_calo_AOD_2018":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v0_gen_studies_calo_AOD_HeavyHiggsSUSY":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "synch_exercise_caltech":
    from Analyzer.LLP2018.samplesAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "synch_exercise_caltech_v2":
    from Analyzer.LLP2018.samplesAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "synch_exercise_caltech_v3":
    from Analyzer.LLP2018.samplesAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "synch_exercise_caltech_v4":
    from Analyzer.LLP2018.samplesAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "test_calo_AOD_pfcand":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v2_calo_AOD_2017":
    from Analyzer.LLP2018.samplesAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
    LUMI = 41557#2017 lumi with normtag, from pdvm2017 twiki
elif options.lists == "v3_calo_AOD_2018":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    #LUMI = 6.815605990*1000.# METRun2018A-17Sep2018-v1 partial # 59690 #2018 from ppd
    #LUMI = 11.816443876*1000.
    LUMI = 13.906390984*1000.# METRun2018A-17Sep2018-v1 all done, 28 Jul 2020
    #LUMI = 59690#2018 lumi with normtag, from pdvm2018 twiki
elif options.lists == "v4_calo_AOD_2018":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    #LUMI = 6.815605990*1000.# METRun2018A-17Sep2018-v1 partial # 59690 #2018 from ppd
    #LUMI = 11.816443876*1000.
    #LUMI = 13.906390984*1000.# METRun2018A-17Sep2018-v1 all done, 28 Jul 2020
    LUMI = 59690#2018 lumi with normtag, from pdvm2018 twiki
elif options.lists == "v5_calo_AOD_2018":
    from Analyzer.LLP2018.samplesAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
    LUMI = 59690#2018 lumi with normtag, from pdvm2018 twiki
elif options.lists == "v1_central_miniAOD_2017_17Nov2020":
    from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2017 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_2017MINIAOD_centrallyProduced import *
    LUMI = 41557#2017 lumi with normtag, from pdvm2017 twiki
elif options.lists == "v5_central_miniAOD_2018_12Mar2021":
    from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_2018MINIAOD_centrallyProduced import *
    LUMI = 59690#2018 lumi with normtag, from pdvm2018 twiki
elif options.lists == "v6_central_miniAOD_2018_14Mar2022" or options.lists == "v6_central_miniAOD_2018_28Mar2022":
    from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
    from Analyzer.LLP2018.crab_requests_lists_2018MINIAOD_centrallyProduced import *
    LUMI = 59690#2018 lumi with normtag, from pdvm2018 twiki
else:
    print "No sample list indicated, aborting!"
    exit()

list_of_samples = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","WJetsToLNu_Pt","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","TTJets","QCD","QCD_HT","QCD_MuEnriched","signal_VBF","signal_ggH", "centralSignal_VBF", "centralSignal_ggH", "centralSignal_ZH", "centralSignal_WH", "all","data_obs","ZJetsToNuNu","DYJets","WJets","signal_ZH","ZJetsToNuNuRed","SUSY","TTbarSemiLep","TTbarNu","ggHeavyHiggs","WJetsToLNu_HT","data_DisplacedJet2018"]
print "Possible subgroups of samples:"
for a in list_of_samples:
    print a
    print "---------------"

#print requests.keys()


selected_requests = {}
if options.groupofsamples not in list_of_samples:
    print "Invalid subgroup of samples, aborting!"
    exit()

for b, k in enumerate(requests.keys()):
    if options.groupofsamples=="signal_VBF":
        if "VBFH_HToSSTobb" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="centralSignal_VBF":
            if "VBFH_HToSSTo4b" in k:
                print k
                selected_requests[k] = requests[k]
    elif options.groupofsamples=="signal_ggH":
        if "GluGluH_HToSSTobb" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="centralSignal_ggH":
            if "ggH_HToSSTobbbb" in k:
                print k
                selected_requests[k] = requests[k]
    elif options.groupofsamples=="signal_ZH":
        if "ZH_HToSSTobb" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="centralSignal_ZH":
            if "ZH_HToSSTobbbb" in k:
                print k
                selected_requests[k] = requests[k]
    elif options.groupofsamples=="centralSignal_WH":
            if "WplusH_HToSSTobbbb" in k or "WminusH_HToSSTobbbb" in k:
                print k
                selected_requests[k] = requests[k]
    elif options.groupofsamples=="JetJet":
        if "XXTo4J" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="splitSUSY":
        if "GluinoGluinoToNeutralinoNeutralinoTo2T2B2S" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="SUSY":
        if "n3n2-n1-hbb-hbb" in k:
            print k
            selected_requests[k] = requests[k]
        elif "TChi" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="ggHeavyHiggs":
        if "GluGluH2_H2ToSSTobb" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="all":
        print "All samples considered"
        selected_requests[k] = requests[k]
    else:
        if k in samples[options.groupofsamples]["files"]:
            print k
            selected_requests[k] = requests[k]


if options.output_folder == "":
    DEST = "/nfs/dust/cms/user/lbenato/v3/"
else:
    DEST = options.output_folder+'/'

if not os.path.exists(os.path.expandvars(options.input_folder)):
    print '--- ERROR: INPUT FOLDER ---'
    print '  \''+options.input_folder+'\' path not found'
    print '  please point to the correct path to the folder containing the CRAB output'
    exit()

if not os.path.exists(os.path.expandvars(DEST)):
    print '--- ERROR: OUTPUT FOLDER ---'
    print '  \''+DEST+'\' path not found'
    print '  please point to the correct output path'
    exit()


#########

jobs = []
names = []

def hadd_outputs(fold,name):
    if "_PRIVATE-MC" in name:
        short_name = name[:-11]
    else:
        short_name = name

######################This blocks naf machines
    #print name
    #os.system('hadd -k -f '+DEST+name+'.root '+fold+'/*/*/*/output_2*.root')# + ' ' +name+'/*/*/*/*_1.root')
    # os.system('hadd -fk207 '+DEST+name+'_0.root ' + fold + "/crab_" + name+"/*/*/*00.root " + fold + "/crab_" + name+"/*/*/*20.root " + fold + "/crab_" + name+"/*/*/*40.root "+ fold + "/crab_" + name+"/*/*/*60.root " + fold + "/crab_" + name+"/*/*/*80.root")##For tracking lifetimes & central production
    # os.system('hadd -fk207 '+DEST+name+'_0p1.root ' + fold + "/crab_" + name+"/*/*/*0.root")##For tracking lifetimes & central production
    # os.system('hadd -fk207 '+DEST+name+'.root ' + fold + "/crab_" + name+"/*/*/*.root")##For tracking lifetimes & central production
    # os.system('hadd -fk207 '+DEST+name+'.root ' + fold + "/*/*/*/*.root")#timestamp for calo_signal!
pass

def weight(name):
    weight = 1.
    filename = TFile(DEST+name+'.root', "UPDATE")
    if ('Run201') in name: weight = 1.
    ###
    # If you want to weight only one sample, specify
    #elif ('TT_TuneCUETP8M2T4_13TeV') in name:
    ###
    else:
        print "********************************"
        nevents = filename.Get("counter/c_nEvents").GetBinContent(1)
#        nevents = filename.Get("counter/c_nEvents").GetEntries()#try?!
        # print "File: ", filename.GetName()
        # print "nevents_sample", nevents
        if name in sample and 'ext' in sample[name]:
            filename = TFile(DEST+sample[name]['ext']+'.root', "UPDATE")
            nevents += filename.Get("counter/c_nEvents").GetBinContent(1)
            # print filename.GetName()
            # print "nevents_ext", filename.Get("counter/c_nEvents").GetBinContent(1)
        if 'VBFH_HToSSTobbbb' in name or 'VBFH_HToSSTo4b' in name:
            #We take into account VBF Higgs production x-sec
            xs = 3.782
        elif 'GluGluH_HToSSTobbbb' in name or 'ggH_HToSSTobbbb' in name:
            #We take into account ggH Higgs production x-sec
            xs = 48.58
        elif 'ZH_HToSSTobbbb' in name:
            #We take into account ZH Higgs production x-sec times branching fraction into leptons
            xs = 0.8839*(3*3.3658/100.)
        elif 'WplusH_HToSSTobbbb' in name:
            xs = 0.8400*(3*10.86/100.)
        elif 'WminusH_HToSSTobbbb' in name:
            xs = 0.5328*(3*10.86/100.)
        #elif('n3n2-n1-hbb-hbb') in name:
        #    #Don't know this x-sec actually...
        #    print "This is susy name: ", name
        #    xs = 1.
        elif('GluGluH2_H2ToSSTobbbb') in name:
            #We do not take into account ggH Higgs production x-sec! Absolute x-sec needed!
            xs = 1.#48.58
        elif('XXTo4J') in name:
            xs = 1.
        elif('GluinoGluinoToNeutralinoNeutralinoTo2T2B2S') in name:
            xs = 1.
        else:
            if 'filtereff' in sample[name]:
                xs = sample[name]['xsec'] * sample[name]['kfactor'] * sample[name]['filtereff']
            else:
                xs = sample[name]['xsec'] * sample[name]['kfactor']#to correct MET phase-space
        weight = LUMI * xs / nevents
        tree = filename.Get("ntuple/tree")
        #tree = filename.Get("trigger/tree")
        print name
        print "LUMI ", LUMI
        print "xs ", xs
        print "nevents ", nevents
        print "weight ", weight
        tree.SetWeight(weight)
        tree.AutoSave()


subdirs = [x for x in os.listdir(options.input_folder) if os.path.isdir(os.path.join(options.input_folder, x))]
#subdirs have the names of the samples without v1, etc

print "PRE: ", selected_requests.keys()

#for naming purposes, we have to include v1, etc. Additional loop###
os.chdir(options.input_folder)

crab_subdirs = []
for l in subdirs:
    crab_subdirs += [x[5:] for x in os.listdir(l) if os.path.isdir(os.path.join(l, x))]

print subdirs
print crab_subdirs
#exit()
#here they have the proper names, including v1

os.chdir(options.input_folder)

for l in subdirs:
    fold = ""
    name = ""
    for a in crab_subdirs:
        #if l in a:
        #if (l in a or a in l) and a in selected_requests.keys():
        if os.path.exists(os.path.join(l, "crab_"+a)) and a in selected_requests.keys(): #For tracking lifetimes & central production
            fold = l
            name = a
            #print fold
            # print "Being added...."
            print name
            print "not being added...."
            hadd_outputs(fold,name)
            print "##################################"
        #if a=="WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2" and l=="WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8":
        #    print "NAMING MISTAKE!!!"
        #    fold = l
        #    name = a
        #    #print fold
        #    print "Being added...."
        #    print name
        #    #print "Not being added...."
        #    hadd_outputs(fold,name)
        #    print "##################################"

######################
#
#    Multiprocessing stucked naf machines, avoid - also, not tested with optparse
#
#    p = multiprocessing.Process(target=hadd_outputs, args=(fold,name))
#    jobs.append(p)
#    p.start()
######################

    #hadd_outputs(fold,name)

print "Ntuples ready in ", DEST
os.system('cd '+DEST+".. ")

if options.lists=="synch_exercise_caltech":
    exit()
if options.lists=="synch_exercise_caltech_v2":
    exit()
if options.lists=="synch_exercise_caltech_v3":
    exit()
if options.lists=="synch_exercise_caltech_v4":
    exit()

#exit()

onlyfiles = [f for f in os.listdir(DEST) if (os.path.isfile(os.path.join(DEST, f)))]
os.chdir(DEST)

for b in onlyfiles:
    #print b
    if b[:-5] in selected_requests.keys():
        # print "I am going to weight:"
        # print b
        weight(b[:-5])
        ##q = multiprocessing.Process(target=weight, args=(b[:-5],))
        ##jobs.append(q)
        ##q.start()
print "Ntuples weighted in ", DEST
