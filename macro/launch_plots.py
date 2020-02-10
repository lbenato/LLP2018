#!/usr/bin/env python
import os

var = [
#"MEt.pt",
#"MEt.sign",
#"HT",
#"MinJetMetDPhi",
#"nCHSJets",
#"nPFCandidates","nPFCandidatesTrack",
#"Jets[0].pt", 
"Jets[0].alphaMax",
#"Jets[0].cHadEFrac", 
#"Jets[0].nHadEFrac",
#"Jets[0].nConstituents",
#"Jets[0].nTrackConstituents",
#"Jets[0].nSelectedTracks",
#"Jets[0].nTracks3PixelHits","Jets[0].cMulti","Jets[0].nMulti",
#"Jets[0].pfXWP0p01",
#"Jets[0].pfXWP1",
#"Jets[0].pfXWP1000",
#"Jets[1].pt",
"Jets[1].alphaMax",
"Jets[1].cHadEFrac", 
"Jets[1].nHadEFrac",
"Jets[1].nConstituents",
"Jets[1].nTrackConstituents",
"Jets[1].nSelectedTracks",
"Jets[1].nTracks3PixelHits","Jets[1].cMulti","Jets[1].nMulti",
"Jets[1].pfXWP0p01",
"Jets[1].pfXWP1",
"Jets[1].pfXWP1000",
#"Jets[2].pfXWP1000",
#"Jets[3].pfXWP1000",
]
cuts = [
#"METPreSel120",
"METSR",
]

regs = ["calo"]

for a in var:
    for b in cuts:
        for c in regs:
            os.system('echo python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            os.system('python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #if "Jets[0]" in a:
            #    os.system('echo python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+'Signal -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #    os.system('echo +++ Adding matching to Jet[0] requirement in signal +++')
            #    os.system('python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+'Signal -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #else:
            #    os.system('echo python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #    os.system('python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')

