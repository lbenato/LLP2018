#! /usr/bin/env python

long_string = "("
vec_range = 1
'''
for a in range(vec_range):
    if a!=len(range(vec_range))-1:
        long_string += "(Jets.Jets[" + str(a) +"].pt == MatchedCHSJet1.pt || Jets.Jets[" +str(a)+"].pt == MatchedCHSJet2.pt || Jets.Jets[" +str(a)+"].pt == MatchedCHSJet3.pt || Jets.Jets[" +str(a)+"].pt == MatchedCHSJet4.pt) || "
    else:
        long_string +="(Jets.Jets["+str(a)+"].pt == MatchedCHSJet1.pt || Jets.Jets[" +str(a)+"].pt == MatchedCHSJet2.pt || Jets.Jets[" +str(a)+"].pt == MatchedCHSJet3.pt || Jets.Jets[" +str(a)+"].pt == MatchedCHSJet4.pt)"
'''
long_string += "Jets.Jets[0].isGenMatched" #new version from v3
long_string += ")"
#print long_string
selection = {
    "none" : "",
    "VBF" : "isVBF",
    ##Comment: including only triggers from BTagCSV, DisplacedJet and MET datasets, as per: https://docs.google.com/spreadsheets/d/1oBxzCCM1XP_dfezelrlamR6sfuAdnWm3cHTcaKbt1xA/edit?usp=sharing
    "METfilters" : "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "triggerMu" : "HLT_IsoMu24_v",
    "triggerEle" : "HLT_Ele27_WPTight_Gsf_v",
    "VBFTrigger" : "(HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v || HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v || HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v || HLT_QuadJet45_TripleBTagCSV_p087_v || HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v || HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "DisplacedTrigger" : "(HLT_VBF_DisplacedJet40_DisplacedTrack_v || HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v || HLT_HT350_DisplacedDijet40_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v || HLT_HT650_DisplacedDijet80_Inclusive_v || HLT_HT750_DisplacedDijet80_Inclusive_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "DisplacedDiJetTrigger" : "(HLT_HT350_DisplacedDijet40_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v || HLT_HT650_DisplacedDijet80_Inclusive_v || HLT_HT750_DisplacedDijet80_Inclusive_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "DisplacedSingleJetTrigger" : "(HLT_VBF_DisplacedJet40_DisplacedTrack_v || HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v || HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",

    "DisplacedHadronicTrigger" : "(HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "DisplacedTrackTrigger" : "(HLT_VBF_DisplacedJet40_DisplacedTrack_v || HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v || HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",



    "METTrigger" : "(HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_MET200_v || HLT_MET250_v || HLT_MET75_IsoTrk50_v || HLT_MET90_IsoTrk50_v || HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v || HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_PFMET110_PFMHT110_IDTight_v || HLT_PFMET120_PFMHT120_IDTight_v || HLT_PFMET170_HBHECleaned_v || HLT_PFMET300_v || HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",

    "PFMETNoMuTrigger" : "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "PFMETNoMuTriggerSignal" : "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && Jets.Jets[0].isGenMatched",


    "MatchSignal" : long_string,#"(Jets.Jets.pt == MatchedCHSJet1.pt || Jets.Jets.pt == MatchedCHSJet2.pt || Jets.Jets.pt == MatchedCHSJet3.pt || Jets.Jets.pt == MatchedCHSJet4.pt)",
#    "MatchSignal" : "(Jets.Jets.pt == MatchedCHSJet1.pt || Jets.Jets.pt == MatchedCHSJet2.pt || Jets.Jets.pt == MatchedCHSJet3.pt || Jets.Jets.pt == MatchedCHSJet4.pt)",
#    "NaiveCutBased" : "Jets.Jets.chm<30 && MEt.pt<250 && nCHSJets<12  && Jets.Jets.mass<60",
    "VetoLeptons" : "nMuons==0 && nElectrons==0 && nPhotons==0 && nTaus==0",#enriches in QCD
    "aaa" : "isVBF && (HLT_VBF_DisplacedJet40_DisplacedTrack_v || HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v || HLT_HT350_DisplacedDijet40_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v || HLT_HT650_DisplacedDijet80_Inclusive_v || HLT_HT750_DisplacedDijet80_Inclusive_v) && nCHSJets<6 && nCHSJets>1 && MEt.pt>200",

    #Trigger studies
    "TSG" : "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && HLT_IsoMu24_v && nTightMuons==1",
    "L1seed" : "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && HLT_IsoMu24_v && nTightMuons==1 && hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300",
    "hltTripleJet50" : "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && HLT_IsoMu24_v && nTightMuons==1  && hltL1sTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBFIorHTT300 && hltTripleJet50",
}

selection["VBFplusVBFTrigger"] = selection["VBF"] + " && " + selection["VBFTrigger"] + " && HT>100"
selection["VBFplusMETTrigger"] = selection["VBF"] + " && " + selection["METTrigger"] + " && HT>100"
selection["VBFplusDisplacedTrigger"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && HT>100"

selection["VBFplusVBFTriggerSignal"] = selection["VBFplusVBFTrigger"] + " && " + selection["MatchSignal"] 
selection["VBFplusVBFTriggerSignal1"] = selection["VBFplusVBFTrigger"] + " && Jets.Jets[1].isGenMatched"



#0
selection["VBFplusDisplacedHadronicTrigger"] = selection["VBF"] + " && " + selection["DisplacedHadronicTrigger"] + " && HT>100"
selection["VBFplusDisplacedHadronicTriggerSignal"] = selection["VBF"] + " && " + selection["DisplacedHadronicTrigger"] + " && HT>100" + " && HT>100 && " + selection["MatchSignal"]
selection["VBFplusDisplacedHadronicTriggerSignal1"] = selection["VBF"] + " && " + selection["DisplacedHadronicTrigger"] + " && HT>100" + " && HT>100 && Jets.Jets[1].isGenMatched"
selection["VBFplusDisplacedHadronicTriggerSignal2"] = selection["VBF"] + " && " + selection["DisplacedHadronicTrigger"] + " && HT>100" + " && HT>100 && Jets.Jets[2].isGenMatched"

#1
selection["VBFplusPFMETNoMuTrigger"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && HT>100"
selection["VBFplusPFMETNoMuTriggerSignal"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && HT>100 && " + selection["MatchSignal"]
selection["VBFplusPFMETNoMuTriggerSignal1"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && HT>100 && Jets.Jets[1].isGenMatched"
selection["VBFplusPFMETNoMuTriggerSignal2"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && HT>100 && Jets.Jets[2].isGenMatched"


selection["VBFplusDisplacedHadronicTriggerMatched"] = selection["VBFplusDisplacedHadronicTrigger"]
selection["VBFplusDisplacedHadronicTriggerMatchedSignal"] = selection["VBF"] + " && " + selection["DisplacedHadronicTrigger"] + " && HT>100" + " && " + selection["MatchSignal"]



selection["VBFplusPFMETNoMuTriggerPlateau"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100"
selection["VBFplusPFMETNoMuTriggerPlateau0Jets"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets==0"
selection["VBFplusPFMETNoMuTriggerPlateau1Jet"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets==1"
selection["VBFplusPFMETNoMuTriggerPlateauSignal"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100" + " && Jets.Jets[0].isGenMatched"
selection["VBFplusPFMETNoMuTriggerPlateauAtLeast1Jet"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=1"
selection["VBFplusPFMETNoMuTriggerPlateauAtLeast1JetSignal"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=1 && Jets.Jets[0].isGenMatched"
selection["VBFplusPFMETNoMuTriggerPlateauAtLeast2Jets"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=2"
selection["VBFplusPFMETNoMuTriggerPlateauAtLeast2JetsSignal"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=2 && Jets.Jets[1].isGenMatched"

selection["VBFplusPFMETNoMuTriggerPlateauAtLeast2JetsNoGenMatched"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=2"
selection["VBFplusPFMETNoMuTriggerPlateauAtLeast2JetsNoGenMatchedSignal"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=2"


selection["VBFplusPFMETNoMuTriggerPlateauAtLeast2JetsQCDkiller"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=2 && MinJetMetDPhi>0.5"
selection["VBFplusPFMETNoMuTriggerPlateauAtLeast2JetsQCDkillerSignal"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets>=2 && MinJetMetDPhi>0.5 && Jets.Jets[0].isGenMatched"





selection["test"] = selection["VBFplusPFMETNoMuTriggerPlateau"]
selection["testSignal"] = selection["VBFplusPFMETNoMuTriggerPlateau"]
selection["testMatched"] = selection["VBFplusPFMETNoMuTriggerPlateau"]
selection["testMatchedSignal"] = selection["VBFplusPFMETNoMuTriggerPlateau"] + " && Jets.Jets[0].isGenMatched"



selection["VBFplusPFMETNoMuTriggerANDDisplacedHadronicTrigger"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && HT>100 && " + selection["DisplacedHadronicTrigger"]
selection["VBFplusPFMETNoMuTriggerANDDisplacedHadronicTriggerSignal"] = selection["VBFplusPFMETNoMuTriggerANDDisplacedHadronicTrigger"] + " && Jets.Jets[0].isGenMatched"

selection["VBFplusPFMETNoMuTriggerXORDisplacedHadronicTrigger"] = "((isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && isVBF && HT>100 && ( HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v) && !(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v && (HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v))  )"
selection["VBFplusPFMETNoMuTriggerXORDisplacedHadronicTriggerSignal"] = selection["VBFplusPFMETNoMuTriggerXORDisplacedHadronicTrigger"]  + " && Jets.Jets[0].isGenMatched"

selection["VBFplusPFMETNoMuTriggerNOTDisplacedHadronicTrigger"] = "((isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && isVBF && HT>100 && ( HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && !((HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v))  )"
selection["VBFplusPFMETNoMuTriggerNOTDisplacedHadronicTriggerSignal"] = selection["VBFplusPFMETNoMuTriggerNOTDisplacedHadronicTrigger"] + " && Jets.Jets[0].isGenMatched"

selection["VBFplusNOTPFMETNoMuTriggerDisplacedHadronicTrigger"] = "((isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && isVBF && HT>100 && (HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v) && !(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v)  )"
selection["VBFplusNOTPFMETNoMuTriggerDisplacedHadronicTriggerSignal"] = selection["VBFplusNOTPFMETNoMuTriggerDisplacedHadronicTrigger"] + " && Jets.Jets[0].isGenMatched"



selection["VBFplusPFMETNoMuTriggerPlateau0Jets"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets==0"
selection["VBFplusPFMETNoMuTriggerPlateau1Jets"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100 && nCHSJets==1"






selection["VBFplusMETTriggerSignal"] = selection["VBFplusMETTrigger"] + " && " + selection["MatchSignal"]
selection["VBFplusDisplacedTriggerSignal"] = selection["VBFplusDisplacedTrigger"] + " && " + selection["MatchSignal"]

#selection["DisplacedNaive"] = selection["VBFplusDisplacedTrigger"] + " && " + selection["NaiveCutBased"]
#selection["DisplacedNaiveSignal"] = selection["DisplacedNaive"] + " && " + selection["MatchSignal"]

#selection["VBFNaive"] = selection["VBFplusVBFTrigger"] + " && " + selection["NaiveCutBased"]
#selection["VBFNaiveSignal"] = selection["VBFNaive"] + " && " + selection["MatchSignal"]

#selection["METNaive"] = selection["VBFplusMETTrigger"] + " && " + selection["NaiveCutBased"]
#selection["METNaiveSignal"] = selection["METNaive"] + " && " + selection["MatchSignal"]

selection["isZ"] = " (isZtoEE || isZtoMM) && Z.mass>70 && Z.mass<110 "
selection["isZtoEE"] = " (isZtoEE) && Z.mass>70 && Z.mass<110 "
selection["isZtoMM"] = " (isZtoMM) && Z.mass>70 && Z.mass<110 "

#selection["ZtoMMCR"] = selection["triggerMu"] + " && Lepton1.pt>30 && Lepton2.pt>30 && Lepton1.isTight && Lepton2.isTight && Lepton1.pfIso04<0.15 && Lepton2.pfIso04<0.15 && Z.pt>50 && " + selection["isZtoMM"]#v4
selection["ZtoMMCR"] = selection["triggerMu"] + " && Muon1.pt>30 && Muon2.pt>30 && Muon1.isTight && Muon2.isTight && Muon1.pfIso04<0.15 && Muon2.pfIso04<0.15 && Z.pt>50 && " + selection["isZtoMM"]


#selection["ZtoMMVBFCR"] = selection["triggerMu"] + " && Lepton1.pt>30 && Lepton2.pt>30 && Lepton1.isTight && Lepton2.isTight && Lepton1.pfIso04<0.15 && Lepton2.pfIso04<0.15 && Z.pt>50 && " + selection["isZtoMM"] + " && isVBF"
selection["TopEMCR"] = selection["triggerMu"] + " && isTtoEM && Muon1.pt>30 && " + selection["METfilters"]

selection["WtoMNCR"] = selection["triggerMu"] + " && Muon1.pt>30 && Muon1.isTight && Muon1.pfIso04<0.15 && isWtoMN && " + selection["METfilters"]


selection["ZtoEECR"] = selection["triggerEle"] + " && Lepton1.pt>30 && Lepton2.pt>30 && Lepton1.isTight && Lepton2.isTight && Z.pt>50 && " + selection["isZtoEE"]

selection["DisplacedZCR"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && " + selection["isZ"]
selection["DisplacedZtoEECR"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && " + selection["ZtoEECR"]
selection["DisplacedZtoMMCR"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && " + selection["ZtoMMCR"]
selection["DisplacedWtoMNCR"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && " + selection["WtoMNCR"]
selection["DisplacedTopEMCR"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && isTtoEM"
selection["DisplacedTopEMNoVBFCR"] = selection["DisplacedTrigger"] + " && isTtoEM"

selection["DisplacedCR0Tag"] = selection["VBFplusDisplacedTrigger"] + " && nCaloTagJets==0 && HT>100"
selection["DisplacedCR1Tag"] = selection["VBFplusDisplacedTrigger"] + " && nCaloTagJets==1 "

selection["DisplacedHadronicCR0Tag"] = selection["VBFplusDisplacedHadronicTrigger"] + " && nCaloTagJets==0 && HT>100"


selection["METCR"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && MEt.pt>250  && HT>200"
selection["METNoVBFCR"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && !isVBF && MEt.pt>250  && HT>200"
selection["METVBFCR"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && isVBF && MEt.pt>250  && HT>200"
selection["METMuCR"] = selection["PFMETNoMuTrigger"] + " && MEt.pt>250  && HT>200 && nTightMuons==1"
selection["METDiboson"] = selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && CHSFatJet1.pt>200 && CHSFatJet1.softdropPuppiMassCorr>30 && HT>200 && MinJetMetDPhi>0.5 && CHSFatJet1.isTight" + " && " + selection["VetoLeptons"]


selection["METHTNoVBF"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>250 && !isVBF"
selection["METHTNoVeto"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>250 && !(" + selection["VetoLeptons"]+")"


selection["METHT"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>200"
selection["METHTHighpT"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>200 && Jets.pt>15"
selection["METHTMediumpT"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>200 && Jets.pt>10"

selection["METHTSignal"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>200"
selection["METHTSignalSignal"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>200 && Jets.Jets[0].isGenMatched"
selection["METHTZeroTracksSignal"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>200 && Jets.Jets[0].nTrackConstituents==0"
selection["METHTZeroTracksSignalSignal"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>200 && Jets.Jets[0].nTrackConstituents==0 && Jets.Jets[0].isGenMatched"


selection["ZtoMM"] = "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && HLT_IsoMu24_v && isZtoMM"
selection["ZtoEE"] = "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand) && HLT_Ele27_WPTight_Gsf_v && isZtoEE"


#selection["SimpleCountingDisplaced"] = selection["VBFplusDisplacedTrigger"] + " && nCaloTagJets>1 && nCHSJets<6"


#selection["SimpleCountingMET"] = selection["VBFplusMETTrigger"] + " && nCHSJets<6 && MEt.pt>300"
selection["SimpleCountingMET"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && MEt.pt>250  && HT>100 && Jets.Jets[0].nSelectedTracks<3 && nCHSJets<7 && isVBF"

selection["TriggerStudies"] = selection["VBF"] + " && " + selection["DisplacedTrigger"] + " && HLT_Mu50_v && HT>100"


#for a,b in enumerate(selection):
#    print "'" +b+"',"


#    "VBFTriggerFullOR" : "(HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq240_v || HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq500_v || HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v || HLT_QuadJet45_TripleBTagCSV_p087_v || HLT_HT650_v || HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v || HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v || HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v || HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v || HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v)",
#    "DisplacedTriggerFullOR" : "(HLT_VBF_DisplacedJet40_DisplacedTrack_v || HLT_VBF_DisplacedJet40_DisplacedTrack_2TrackIP2DSig5_v || HLT_HT350_DisplacedDijet40_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VVTightID_DisplacedTrack_v || HLT_HT350_DisplacedDijet80_Tight_DisplacedTrack_v || HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v || HLT_HT650_DisplacedDijet80_Inclusive_v || HLT_Mu38NoFiltersNoVtx_DisplacedJet60_Loose_v || HLT_HT750_DisplacedDijet80_Inclusive_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Loose_v || HLT_Mu38NoFiltersNoVtxDisplaced_DisplacedJet60_Tight_v)",
#    "METTriggerFullOR" : "(HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v || HLT_PFMET110_PFMHT110_IDTight_v || HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_PFMET120_PFMHT120_IDTight_v || HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v || HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v || HLT_PFMET170_HBHECleaned_v || HLT_PFHT300_PFMET110_v || HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV_p067_v || HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v || HLT_MET200_v || HLT_RsqMR270_Rsq0p09_MR200_v || HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v || HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v || HLT_MET250_v || HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v  || HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v || HLT_PFMET300_v || HLT_MET75_IsoTrk50_v || HLT_MET90_IsoTrk50_v )",
