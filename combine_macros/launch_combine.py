#!/usr/bin/env python

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
    from Analyzer.LLP2018.ZH_DNN_setting import *
elif "VBFH" in options.channel:
    isMM = isEE = isComb = False
    chan = "VBFH"
    from Analyzer.LLP2018.VBFH_DNN_setting import *
elif "ggH" in options.channel:
    isMM = isEE = isComb = False
    chan = "ggH"
    from Analyzer.LLP2018.ggH_DNN_setting import *
else:
    print "Channel not recognized for calculating limits/significance!"

if options.fom=="Limits":
    print "Calculating limits with asymptotic method over these datacards: "+DATACARDS
elif options.fom=="Significance":
    print "Calculating a-priori expected significance (Asimov dataset) over these datacards: "+DATACARDS
else:
    print "Wrong figure of merit, can't be computed by combine"


for m in massPoints:
    for c in ctauPoints:
        card = chan+"_M"+str(m)+"_ctau"+str(c)
        if isMM: card+="_MM.txt"
        elif isEE: card+="_EE.txt"
        elif isComb: card+="_comb.txt"
        else: card+=".txt"
        print card
        if options.fom=="Limits":
            os.system("combine -M AsymptoticLimits --datacard " + DATACARDS + "/" + card + "  --run blind -m " + str(m) + " | grep -e Observed -e Expected | awk '{print $NF}' > " + OUTPUTFOLDER + "/" + card)
        elif options.fom=="Significance":
            workspace = card[:-3]+"root"
            os.system("text2workspace.py " + DATACARDS + "/" + card + " " + " -o " + DATACARDS + "/" + workspace)
            os.system("combine -M Significance " + DATACARDS + "/" + workspace + "  -t -1 --expectSignal=1 | grep -e Significance: | awk '{print $NF}' > " + OUTPUTFOLDER + "/Significance_" + card)


print "Results written in " + OUTPUTFOLDER
