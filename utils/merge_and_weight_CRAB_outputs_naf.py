#!/usr/bin/env python
import os, re
import multiprocessing
import logging
import commands
import math, time
import sys
from ROOT import TObject, TFile, TH1, TH1F
from Analyzer.LLP2018.samples import sample, samples
from array import array

#LUMI        =  35867#36814# in pb-1

#print "Please input the correct lumi!!! Taking lumi for prod v4, SingleMuon dataset"
#print "Please input the correct lumi!!! Taking lumi for prod v4, displaced jet dataset"

#LUMI = 7478.896#v4, SingleMuonRunG
#LUMI = 7380.269#v4, DisplacedJetRunG

print "*****************************************************************************"
print "\n"
print "Please input the correct lumi!!! Taking lumi for prod v5, SingleMuon dataset"
#print "Please input the correct lumi!!! Taking lumi for prod v5, displaced jet dataset"
print "\n"
#LUMI = 7533.496#v5, SingleMuonRunG
#LUMI = 7419.796#v5, DisplacedJetRunG

LUMI = 5750.126252897#met_v0_19Aug2019, RunB v2 ver 2

#LUMI        =  35867# full Run 2016#36814# in pb-1
#LUMI = 0
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


if options.lists == "VBF":
    from Analyzer.LLP.crab_requests_lists import *
elif options.lists == "ttbar":
    from Analyzer.LLP.crab_requests_lists_ttbar import *
elif options.lists == "additional":
    from Analyzer.LLP.crab_requests_lists_additional_backgrounds import *
elif options.lists == "missing":
    from Analyzer.LLP.crab_requests_lists_missing import *
elif options.lists == "v2":
    from Analyzer.LLP.crab_requests_lists_v2 import *
elif options.lists == "v3":
    from Analyzer.LLP.crab_requests_lists_v3 import *
elif options.lists == "DYJetsToLL":
    from Analyzer.LLP.crab_requests_lists_DYJetsToLL import *
elif options.lists == "DisplacedJets":
    from Analyzer.LLP.crab_requests_lists_DisplacedJets import *
elif options.lists == "v4":
    from Analyzer.LLP.crab_requests_lists_v4 import *
elif options.lists == "v5":
    from Analyzer.LLP.crab_requests_lists_v5 import *
elif options.lists == "triggerv0":
    from Analyzer.LLP.crab_requests_lists_v5 import *
elif options.lists == "triggerv1":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
elif options.lists == "triggerv2":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
elif options.lists == "triggerv3":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
elif options.lists == "triggerv4":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
elif options.lists == "triggerv5":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
elif options.lists == "triggerv6":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
    LUMI = 7570.852545674#SingleMuonRunG
    #LUMI = 2391.657804102#SingleMuonRunC
elif options.lists == "v6":
    from Analyzer.LLP.crab_requests_lists_v5 import *
    LUMI = 7419.796#WARNING! Lumi from v5, since v6 fails
elif options.lists == "VBFH_ext":
    from Analyzer.LLP.crab_requests_lists_VBFH_Tranche2 import *
    LUMI = 7419.796#WARNING! Lumi from v5, since v6 fails
elif options.lists == "triggerv7":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
    LUMI = 7552.828525093#SingleMuonRunG
elif options.lists == "triggerv8":
    from Analyzer.LLP.crab_requests_lists_triggerv1 import *
    LUMI = 7543.233758#SingleMuonRunG
elif options.lists == "calo_signal":
    from Analyzer.LLP.crab_requests_lists_calo_signal import *
    LUMI = 35867#36814# in pb-1 Full 2016
elif options.lists == "met":
    from Analyzer.LLP.crab_requests_lists_met import *
    #LUMI = 35867#36814# in pb-1 Full 2016
    LUMI = 5750.126252897#met_v0_19Aug2019, RunB v2 ver 2
elif options.lists == "met_recluster":
    from Analyzer.LLP.crab_requests_lists_met import *
    LUMI = 35867#36814# in pb-1 Full 2016
    #LUMI = 5750.126252897#met_v0_19Aug2019, RunB v2 ver 2
elif options.lists == "zh":
    from Analyzer.LLP.crab_requests_lists_zh import *
    LUMI = 35867#36814# in pb-1 Full 2016
elif options.lists == "v7_short":
    from Analyzer.LLP.crab_requests_lists_v7_short import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v7_calo":
    from Analyzer.LLP.crab_requests_lists_v7_calo import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
elif options.lists == "v10":
    from Analyzer.LLP2018.crab_requests_lists_v10 import *
    LUMI = 35867#36814# in pb-1 Full 2016 with normtag
else:
    print "No sample list indicated, aborting!"
    exit()

from Analyzer.LLP2018.samples import sample, samples
list_of_samples = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","WJetsToLNu_Pt","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","QCD","signal_VBF","signal_ggH","all","data_obs","ZJetsToNuNu","DYJets","WJets","signal_ZH", "QCD_HT50to100","QCD_HT100to200","QCD_HT200to300","QCD_HT300to500","QCD_HT500to700","QCD_HT700to1000","QCD_HT1000to1500","QCD_HT1500to2000","QCD_HT2000toInf"]
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
    elif options.groupofsamples=="signal_ggH":
        if "GluGluH_HToSSTobb" in k:
            print k
            selected_requests[k] = requests[k]
    elif options.groupofsamples=="signal_ZH":
        if "ZH_HToSSTobb" in k:
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
#    os.system('hadd -k -f '+DEST+name+'.root '+fold+'/*/*/*/output_7*.root')# + ' ' +name+'/*/*/*/*_1.root') # work around for full ttbar sample, which is too large
#    os.system('hadd -k -f '+DEST+name+'.root '+fold+'/*/*/*/output_7*.root'+ ' ' +fold+'/*/*/*/*_1*.root'+ ' ' +fold+'/*/*/*/*_2*.root'+ ' ' +fold+'/*/*/*/*_3*.root'+ ' ' +fold+'/*/*/*/*_4*.root'+ ' ' +fold+'/*/*/*/*_5*.root')#+ ' ' +fold+'/*/*/*/*_6*.root') # for ttbar sample; trigger study v9
    #os.system('hadd -k -f -O '+DEST+name+'.root ' + fold + "/*/*/*/*.root")#work around if TTree is too large
    os.system('hadd -k -f '+DEST+name+'.root ' + fold + "/*/*/*/*.root")
pass

def weight(name):
    weight = 1.
    filename = TFile(DEST+name+'.root', "UPDATE")
    if ('Run2016') in name: weight = 1.
    ###
    # If you want to weight only one sample, specify
    #elif ('TT_TuneCUETP8M2T4_13TeV') in name:
    ###
    else:
        nevents = filename.Get("counter/c_nEvents").GetBinContent(1)
#        nevents = filename.Get("counter/c_nEvents").GetEntries()#try?!
        if ('VBFH_HToSSTobbbb') in name:
            #We take into account VBF Higgs production x-sec
            xs = 3.782
        elif('GluGluH_HToSSTobbbb') in name:
            #We take into account ggH Higgs production x-sec
            xs = 48.58
        elif('ZH_HToSSTobbbb') in name:
            #We take into account ZH Higgs production x-sec times branching fraction into leptons
            xs = 0.8839*(3.3658/100.)
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

#for naming purposes, we have to include v1, etc. Additional loop###
#print os.listdir(args.folder)
os.chdir(options.input_folder)

crab_subdirs = []
for l in subdirs:
    crab_subdirs += [x[5:] for x in os.listdir(l) if os.path.isdir(os.path.join(l, x))]
#here they have the proper names, including v1

os.chdir(options.input_folder)

for l in subdirs:
    fold = ""
    name = ""
    for a in crab_subdirs:
        #if l in a:
        if l in a and a in selected_requests.keys():
            fold = l
            name = a
            #print fold
            print "Being added...."
            print name
            #print "Not being added...."
            hadd_outputs(fold,name)
            print "##################################"

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


onlyfiles = [f for f in os.listdir(DEST) if (os.path.isfile(os.path.join(DEST, f)))]
os.chdir(DEST)

for b in onlyfiles:
    #print b
    if b[:-5] in selected_requests.keys():
        print "I am going to weight:"
        #print b
        weight(b[:-5])
        ##q = multiprocessing.Process(target=weight, args=(b[:-5],))
        ##jobs.append(q)
        ##q.start()                                                                                                                                                                         
print "Ntuples weighted in ", DEST
