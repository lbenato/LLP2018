#!/usr/bin/env python
import os

var = [
#"number_of_b_matched_to_CHSJets",
#"nMatchedCHSJets",
#"MEt.pt",
#"MEt.sign",
#"HT",
#"MinJetMetDPhi",
##"nCHSJets",
#"nPFCandidates","nPFCandidatesTrack",

#"Jets[0].pt", 
#"Jets[0].alphaMax",
#"Jets[0].cHadEFrac", 
#"Jets[0].nHadEFrac",
#"Jets[0].nConstituents",
#"Jets[0].nTrackConstituents",
#"Jets[0].nSelectedTracks",
#"Jets[0].nTracks3PixelHits","Jets[0].cMulti","Jets[0].nMulti",
#"Jets[0].pfXWP0p01",
#"Jets[0].pfXWP1",
#"Jets[0].pfXWP10",
#"Jets[0].pfXWP100",
#"Jets[0].pfXWP1000",
#?
#"Jets[0].ecalE/Jets[0].energyRaw",
#"Jets[0].hcalE/Jets[0].energyRaw",

#"Jets[0].ecalE",
#"Jets[0].hcalE",
#"Jets[0].FracCal",
#"Jets[0].nHitsMedian",
#"Jets[0].nPixelHitsMedian",
#"Jets[0].sigIP2DMedian",

#"Jets[0].sigIP2DMedian",
#"Jets[0].theta2DMedian",
#"Jets[0].POCA_theta2DMedian",
#"Jets[0].nVertexTracks",
#"Jets[0].nSVCand",
#"Jets[0].CSV",
#"Jets[0].nSV",
#"Jets[0].dRSVJet",
#"Jets[0].flightDist2d",
#"Jets[0].flightDist3d",
#"Jets[0].nTracksSV",
#"Jets[0].SV_mass",

"Jets[0].nSV",
"Jets[0].nSVCand",
"Jets[0].nVertexTracks",
"Jets[0].nSelectedTracks",
"Jets[0].dRSVJet",
"Jets[0].flightDist2d",
"Jets[0].flightDist2dError",
"Jets[0].flightDist3d",
"Jets[0].flightDist3dError",
"Jets[0].SV_x",
"Jets[0].SV_y",
"Jets[0].SV_z",
"Jets[0].SV_dx",
"Jets[0].SV_dy",
"Jets[0].SV_dz",
"Jets[0].nTracksSV",
"Jets[0].SV_mass",

"Jets[0].alphaMax",
"Jets[0].sigIP2DMedian",
"Jets[0].theta2DMedian",
"Jets[0].POCA_theta2DMedian",
"Jets[0].nPixelHitsMedian",
"Jets[0].nHitsMedian",


"Jets[1].nSV",
"Jets[1].nSVCand",
"Jets[1].nVertexTracks",
"Jets[1].nSelectedTracks",
"Jets[1].dRSVJet",
"Jets[1].flightDist2d",
"Jets[1].flightDist2dError",
"Jets[1].flightDist3d",
"Jets[1].flightDist3dError",
"Jets[1].SV_x",
"Jets[1].SV_y",
"Jets[1].SV_z",
"Jets[1].SV_dx",
"Jets[1].SV_dy",
"Jets[1].SV_dz",
"Jets[1].nTracksSV",
"Jets[1].SV_mass",

"Jets[1].alphaMax",
"Jets[1].sigIP2DMedian",
"Jets[1].theta2DMedian",
"Jets[1].POCA_theta2DMedian",
"Jets[1].nPixelHitsMedian",
"Jets[1].nHitsMedian",
#"Jets[1].CSV",


#"Jets[1].pt",
#"Jets[1].alphaMax",
#"Jets[1].cHadEFrac", 
#"Jets[1].nHadEFrac",
#"Jets[1].nConstituents",
#"Jets[1].nTrackConstituents",
#"Jets[1].nSelectedTracks",
#"Jets[1].nTracks3PixelHits","Jets[1].cMulti","Jets[1].nMulti",
#"Jets[1].pfXWP0p01",
#"Jets[1].pfXWP1",
#"Jets[1].pfXWP10",
#"Jets[1].pfXWP100",
#"Jets[1].pfXWP1000",
#"Jets[2].pfXWP1000",
#"Jets[3].pfXWP1000",
#"Jets[4].pfXWP1000",
#"Jets[2].cHadEFrac",
#"Jets[3].cHadEFrac",
#"Jets[4].cHadEFrac",
#"Jets[2].nHadEFrac",
#"Jets[3].nHadEFrac",
#"Jets[4].nHadEFrac",
#"Jets[2].nTrackConstituents",
#"Jets[3].nTrackConstituents",
#"Jets[4].nTrackConstituents",
#"Jets[2].nSelectedTracks",
#"Jets[3].nSelectedTracks",
#"Jets[4].nSelectedTracks",
]
cuts = [
"METPreSelSUSYAOD",
#"METSR",
]

regs = ["calo"]

for a in var:
    for b in cuts:
        for c in regs:
            os.system('echo python macro/plot_from_tree_SUSY.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            os.system('python macro/plot_from_tree_SUSY.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #if "Jets[0]" in a:
            #    os.system('echo python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+'Signal -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #    os.system('echo +++ Adding matching to Jet[0] requirement in signal +++')
            #    os.system('python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+'Signal -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #else:
            #    os.system('echo python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')
            #    os.system('python macro/plot_from_tree.py -c ' + str(b) + ' -s ' + str(b)+' -v ' + str(a) + ' -r ' + str(c) + ' -B -b \n')

