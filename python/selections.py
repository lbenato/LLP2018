#! /usr/bin/env python

long_string = "("
long_string += "Jets.Jets[0].isGenMatched" #new version from v3
long_string += ")"

selection = {
    "none" : "",
    "isMC" : "isMC",
    "VBF" : "isVBF",
    ##Comment: including only triggers from BTagCSV, DisplacedJet and MET datasets, as per: https://docs.google.com/spreadsheets/d/1oBxzCCM1XP_dfezelrlamR6sfuAdnWm3cHTcaKbt1xA/edit?usp=sharing
    "METfilters" : "(isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",

    "METfiltersAOD" : "Flag2_globalSuperTightHalo2016Filter && Flag2_goodVertices && Flag2_EcalDeadCellTriggerPrimitiveFilter && Flag2_HBHENoiseFilter && Flag2_HBHEIsoNoiseFilter && Flag2_ecalBadCalibFilter && Flag2_eeBadScFilter && Flag2_BadPFMuonFilter",#https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2

    "PFMETNoMuTrigger" : "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)",
    "PFMETNoMuTriggerAOD" : "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v && Flag2_globalSuperTightHalo2016Filter && Flag2_EcalDeadCellTriggerPrimitiveFilter && Flag2_HBHENoiseFilter && Flag2_HBHEIsoNoiseFilter && Flag2_ecalBadCalibFilter && Flag2_eeBadScFilter && Flag2_BadPFMuonFilter",#&& Flag2_goodVertices 

    "VBFDisplHadTrigger" : "(HLT_VBF_DisplacedJet40_VTightID_Hadronic_v || HLT_VBF_DisplacedJet40_VVTightID_Hadronic_v) && (isMC?1:Flag_EcalDeadCellTriggerPrimitiveFilter) && (isMC?1:Flag_HBHENoiseFilter) && (isMC?1:Flag_HBHENoiseIsoFilter) && (isMC?1:Flag_globalTightHalo2016Filter) && (isMC?1:Flag_goodVertices) && Flag_BadPFMuon && Flag_BadChCand",
    "VetoLeptons" : "nMuons==0 && nElectrons==0 && nPhotons==0 && nTaus==0",#enriches in QCD
    #"L" : "(HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && Flag_HBHENoiseIsoFilter",
}

selection["VBFplusPFMETNoMuTrigger"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && HT>100"
selection["VBFplusPFMETNoMuTriggerPlateau"] = selection["VBF"] + " && " + selection["PFMETNoMuTrigger"] + " && MEt.pt>250 && HT>100"

selection["METCR"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && MEt.pt>250  && HT>200"
selection["METNoVBFCR"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && !isVBF && MEt.pt>250  && HT>200"
selection["METVBFCR"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && isVBF && MEt.pt>250  && HT>200"
selection["METMuCR"] = selection["PFMETNoMuTrigger"] + " && MEt.pt>250  && HT>200 && nTightMuons==1"

selection["DisplHadPreSel"] = selection["VBFDisplHadTrigger"] + " && " + selection["VetoLeptons"] + " && HT>100 && isVBF"

selection["METPreSel"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && HT>100 && isVBF"#No Met cuts
selection["METPreSel200"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && HT>100 && isVBF && MEt.pt>200"

selection["METPreSel120"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && HT>100 && isVBF && MEt.pt>120"
###
selection["METPreSelSUSYAOD"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200"


selection["PreselSkimAK4"] = "MEt.pt>200 && nCHSJets>=1"# && EventNumber%2!=0"
selection["PreselSkimAK4Match"] = "MEt.pt>200 && nCHSJets>=1 && Jets[0].isGenMatchedCaloCorrLLPAccept"# && EventNumber%2!=0"
selection["PreselSkimAK8"] = "MEt.pt>200 && nCHSFatJets>=1"# && EventNumber%2!=0"
selection["PreselSkimAK8Match"] = "MEt.pt>200 && nCHSFatJets>=1 && FatJets[0].isGenMatched"# && EventNumber%2!=0"
selection["PreselTrainDNNSkim"] = "MEt_pt>200 && nCHSJets>=1"# && EventNumber%2!=0"
selection["PreselTrainDNNSkimAK8"] = "MEt_pt>200 && nCHSFatJets>=1"# && EventNumber%2!=0"




selection["METPreSelSUSY"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && HT>100 && MEt.pt>200"

selection["METPreSelSUSYAODAK4"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48"
selection["METPreSelSUSYAODAK4Match"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && Jets.isGenMatchedCaloCorrLLPAccept"

#selection["METPreSelSUSYAODAK8Match"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.isGenMatchedCaloCorrLLPAccept"

selection["METPreSelSUSYAODAK4ECAL"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48"
selection["METPreSelSUSYAODAK4ECALMatch"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && Jets.isGenMatchedCaloCorr && Jets.radiusLLP>129 && Jets.radiusLLP<184 && fabs(Jets.zLLP)<300"

selection["METPreSelSUSYAODAK4HCAL"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48"
selection["METPreSelSUSYAODAK4HCALMatch"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && Jets.isGenMatchedCaloCorr && Jets.radiusLLP>181 && Jets.radiusLLP<290 && fabs(Jets.zLLP)<450"

##
selection["Check"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>100 && MEt.pt>120"
selection["InvestigateTimeAK4ECAL"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && Jets.timeRecHitsEB<0"
selection["InvestigateTimeAK4ECALPos"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && Jets.timeRecHitsEB>=0"

selection["InvestigateTimeAK4ECAL2OrMoreJets"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && nCHSJets>1"
selection["InvestigateTimeAK4ECAL3OrMoreJets"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && nCHSJets>2"
selection["InvestigateTimeAK4ECAL4OrMoreJets"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.48 && nCHSJets>4"

selection["InvestigateTimeAK4ECAL2OrMoreJetsHT500"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>500 && MEt.pt>200 && fabs(Jets.eta)<1.48 && nCHSJets>1"
selection["InvestigateTimeAK4ECAL2OrMoreJetsHT750"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>750 && MEt.pt>200 && fabs(Jets.eta)<1.48 && nCHSJets>1"
selection["InvestigateTimeAK4ECAL3OrMoreJetsHT500"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>500 && MEt.pt>200 && fabs(Jets.eta)<1.48 && nCHSJets>2"


#

##
selection["HCALInvestigationAcceptance"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.3"

selection["HCALInvestigationEta1p3"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<1.3 && fabs(Jets.eta)>0.5"

selection["HCALInvestigationEta0p5"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<0.5 && fabs(Jets.eta)>0.2"

selection["HCALInvestigationEta0p2"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(Jets.eta)<0.2"
##

selection["METPreSelSUSYAODAK8ECAL"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48"
selection["METPreSelSUSYAODAK8ECALMatch"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.isGenMatchedCaloCorrLLPAccept && FatJets.radiusLLP>129 && FatJets.radiusLLP<184 && fabs(FatJets.zLLP)<300"
selection["METPreSelSUSYAODAK8HCAL"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48"
selection["METPreSelSUSYAODAK8HCALMatch"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.isGenMatchedCaloCorrLLPAccept && FatJets.radiusLLP>181 && FatJets.radiusLLP<290 && fabs(FatJets.zLLP)<450"

selection["METPreSelSUSYAODAK8"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48"
selection["METPreSelSUSYAODAK8Match"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.isGenMatchedCaloCorrLLPAccept"

selection["prova0"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.cHadEFrac<0.05 "
selection["prova"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.gammaMaxET<0.05 && FatJets.cHadEFrac<0.05 "

selection["prova2"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.gammaMaxET<0.02 && FatJets.cHadEFrac<0.03 && FatJets.energyRecHitsHB/FatJets.energy>0.03 "



selection["Karla"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.cHadEFrac>-1. && FatJets.cHadEFrac<0.08 && FatJets.gammaMaxET>-1. && FatJets.gammaMaxET<0.08 && FatJets.minDeltaRPVTracks<999 && FatJets.minDeltaRPVTracks>0.3 "

selection["KarlaMatch"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>200 && MEt.pt>200 && fabs(FatJets.eta)<1.48 && FatJets.cHadEFrac>-1. && FatJets.cHadEFrac<0.08 && FatJets.gammaMaxET>-1. && FatJets.gammaMaxET<0.08 && FatJets.minDeltaRPVTracks<999 && FatJets.minDeltaRPVTracks>0.3 && FatJets.isGenMatchedCaloCorrLLPAccept"





selection["CheckLeader"] = "MEt.sign>20 && " + selection["VetoLeptons"] + " && HT>100 && MEt.pt>120"
selection["synch"] = selection["PFMETNoMuTriggerAOD"] + " && " + selection["VetoLeptons"] + " && HT>100 && MEt.pt>120 && Jets[0].pt>30 && Jets[1].pt>30 && nJets>1"


selection["METPreSel120QCDKiller"] = selection["PFMETNoMuTrigger"] + " && " + selection["VetoLeptons"] + " && HT>100 && isVBF && MEt.pt>120 && MinJetMetDPhi>0.5"


selection["METHTLowPt"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>200"
selection["METHTLowMet"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>120"

selection["METHTLowMetHT"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>120"

selection["METHT"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>200 && CHSJets.pt>15"
selection["METHTNoVBF"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>250 && !isVBF"

selection["METHTv0"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>200 && Jets.pt>15"
selection["METHTv0miniAOD"] = selection["PFMETNoMuTrigger"] + " && HT>200 && MEt.pt>200 && (isMC?CHSJets.pt>15:1)"




selection["isZ"] = " (isZtoEE || isZtoMM) && Z.mass>70 && Z.mass<110 "
selection["isZtoEE"] = " (isZtoEE) && Z.mass>70 && Z.mass<110 && Z.pt>50"
selection["isZtoMM"] = " (isZtoMM) && Z.mass>70 && Z.mass<110 && Z.pt>50"
selection["triggerEle"] = "HLT_Ele27_WPTight_Gsf_v"
selection["triggerMu"] = "HLT_IsoMu24_v"

selection["ZHtoEE"] = selection["isZtoEE"] + " && " + selection["triggerEle"]
selection["ZHtoMM"] = selection["isZtoMM"] + " && " + selection["triggerMu"]

selection["ZHtoMMSR"] = selection["isZtoMM"] + " && " + selection["triggerMu"] + " && MEt.pt>120 && MEt.sign>30"
selection["BoostZHtoMMSR"] = selection["isZtoMM"] + " && " + selection["triggerMu"] + " && MEt.pt>120 && MEt.sign>30 && Z.pt>100"

selection["METggH"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>120 && isggH " + " && " + selection["VetoLeptons"]
selection["METggHNotVBF"] = selection["PFMETNoMuTrigger"] + " && HT>100 && MEt.pt>120 && isggH && !isVBF " + " && " + selection["VetoLeptons"]
