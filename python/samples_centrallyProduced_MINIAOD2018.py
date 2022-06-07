#! /usr/bin/env python

#voms-proxy-init -voms cms
#

#Higgs production cross sections: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHXSWG#Production_cross_sections_and_de
#mH = 125 GeV (check if it' better 125.09!)
    #ggH xsec: 48.58
    #VBF xsec: 3.782
    #WH xsec: 1.373
    #ZH xsec: 0.8839

sample = {

    # ------------
    # VBF signal
    # ------------

    #2016 campaign
    'VBFH_HToSSTo4b_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    #2017 campaign
    'VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAODv2' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    #2018 campaign
    'VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    # ------------
    # ggH signal
    # ------------

    #2016 campaign
    'ggH_HToSSTobbbb_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    #2017 campaign
    'ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAODv2' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    #2018 campaign
    'ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    # ------------
    # QCD
    # ------------
    # From twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
    # and 50-100 HT bin from: https://gitlab.cern.ch/DasAnalysisSystem/workarea/-/blob/master/tables/MCxsections/README.md
    'QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8-v1': {
        'nevents' : 1,
        'xsec' : 2.464e+08, #XSDB 185300000.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8-v1': {
        'nevents' : 1,
        'xsec' : 27990000.0, #XSDB 23590000.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 1712000.0, #XSDB 1551000.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 347700.0, #XSDB 323400.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'  : 32100.0, #XSDB 30140.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 6831, #XSDB 6344.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 1207, #XSDB 1092.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 119.9, #XSDB 99.76
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 25.24, #XSDB 20.35
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # --------------
    # QCD MuEnriched
    # --------------
    # Had taken values from XSDB - Seemed off
    # From MCM fragment - Same as twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
    'QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3' : {
        'nevents' : 1,
        'xsec' : 1.27319e+09, #XSDB: 2799000.0
        'filtereff' : 0.00300, #xsec*filtereff: 3819570.0
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v4' : {
        'nevents' : 1,
        'xsec' : 5.58528e+08, #XSDB: 2526000.0
        'filtereff' : 0.00530,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3' : {
        'nevents' : 1,
        'xsec' : 1.39803e+08, #XSDB: 1362000.0
        'filtereff' : 0.01182,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3' : {
        'nevents' : 1,
        'xsec' : 1.92225e+07, #XSDB: 376600.0
        'filtereff' : 0.02276,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # 'QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1' : {
    #     'nevents' : 1,
    #     'xsec' : 2.75842e+06, #XSDB: 88930.0
    #     'filtereff' : 0.03844,
    #     'matcheff': 1.,
    #     'kfactor' : 1.,
    #     'ext' : 'QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2',
    # },

    'QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2' : {
        'nevents' : 1,
        'xsec' : 2.75842e+06, #XSDB: 88930.0
        'filtereff' : 0.03844,
        'matcheff': 1.,
        'kfactor' : 1.,
        # 'ext' : 'QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
    },

    # 'QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1' : {
    #     'nevents' : 1,
    #     'xsec' : 469797, #XSDB: 21230.0
    #     'filtereff' : 0.05362,
    #     'matcheff': 1.,
    #     'kfactor' : 1.,
    #     'ext' : 'QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2',
    # },

    'QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2' : {
        'nevents' : 1,
        'xsec' : 469797, #XSDB: 21230.0
        'filtereff' : 0.05362,
        'matcheff': 1.,
        'kfactor' : 1.,
        # 'ext' : 'QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
    },

    'QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3' : {
        'nevents' : 1,
        'xsec' : 117989, #XSDB: 7055.0,#pb
        'filtereff' : 0.07335,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # 'QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3' : {
    #     'nevents' : 1,
    #     'xsec' : 7820.25, #XSDB: 619.3
    #     'filtereff' : 0.10196,
    #     'matcheff': 1.,
    #     'kfactor' : 1.,
    #     'ext' : 'QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext3-v1',
    # },

    'QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext3-v1' : {
        'nevents' : 1,
        'xsec' : 7820.25, #XSDB: 619.3
        'filtereff' : 0.10196,
        'matcheff': 1.,
        'kfactor' : 1.,
        # 'ext' : 'QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3',
    },

    # 'QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1' : {
    #     'nevents' : 1,
    #     'xsec' : 645.528, #XSDB: 59.24
    #     'filtereff' : 0.12242,
    #     'matcheff': 1.,
    #     'kfactor' : 1.,
    #     'ext' : 'QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2',
    # },

    'QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2' : {
        'nevents' : 1,
        'xsec' : 645.528, #XSDB: 59.24
        'filtereff' : 0.12242,
        'matcheff': 1.,
        'kfactor' : 1.,
        # 'ext' : 'QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
    },

    'QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 187.109, #XSDB: 18.21
        'filtereff' : 0.13412,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext3-v2' : {
        'nevents' : 1,
        'xsec' : 32.3486, #XSDB: 3.275
        'filtereff' : 0.14552,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1' : {
        'nevents' : 1,
        'xsec' : 10.4305, #XSDB: 1.078
        'filtereff' : 0.15544,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # ------------
    # TTbar
    # ------------
    # Had taken values from MCM - Likely before parton-shower matching!
    # XSDB has two different values - First value ~consistent with: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (Top mass: 172.5 GeV)
    'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v1' : { #
        'nevents' : 1,
        'xsec'    : 365.34, #MCM: 300.9 #Also 687.1 on XSDB?
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v1' : { #NOTE: Merged only 10% of crab outputs!
        'nevents' : 1,
        'xsec'    : 377.96, #MCM: 313.9 #Also 687.1 on XSDB?
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v1' : { #NOTE: Merged only 10% of crab outputs!
        'nevents' : 1,
        'xsec'    : 88.29, #MCM: 72.1 #Also 687.1 on XSDB?
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # ------------
    # Single top
    # ------------
    # Had taken values from XSDB
    # Now: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec (same values as B2G-17-005)
    'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1-v1' : {
        'nevents' : 1,
        'xsec'    : 35.85, #XSDB: 34.97
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1-v1' : {
        'nevents' : 1,
        'xsec'    : 35.85, #XSDB: 34.97
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8_ext1-v4' : {
        'nevents' : 1,
        'xsec'    : 3.46, #Twiki & PDG 2020: 10.32*(1.0-0.665) #XSDB: 3.74 #B2G-17-005: 10.32*(1.-0.6760)
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 80.95, #XSDB: 69.09
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 136.02, #XSDB: 115.3,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # ------------
    # Diboson
    # ------------
    # Had taken values from XSDB
    # Now: https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
    'WW_TuneCP5_13TeV-pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 118.7, #XSDB: 75.8
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WZ_TuneCP5_13TeV-pythia8-v3' : {
        'nevents' : 1,
        'xsec'    : 47.13, #XSDB: 27.6 #B2G-17-005: 47.2
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZZ_TuneCP5_13TeV-pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 16.523, #XSDB: 12.14 #B2G-17-005: 16.6
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # ------------
    # DY+Jets
    # ------------
    # From twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns?rev=153
    # AOD samples: https://github.com/lbenato/LLP_NN_Inference/blob/master/python/samplesAOD2018.py#L22-L71
    # Where are the values used for the AOD samples actually coming from?
    'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 280.35, #AOD: 384.1 #MCM: 307.7 #XSDB: 302.8
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 1.37,
    },
    'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 77.67, #AOD: 118.1, #MCM: 92.95 #XSDB: 92.59
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 1.52,
    },
    'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v2' : {
        'nevents' : 1,
        'xsec'    : 10.73, #AOD: 14.7, #MCM: 13.21 #XSDB: 13.18
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 1.37,
    },
    'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 2.559, #AOD: 3.35, #MCM: 3.24 #XSDB: 3.257
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 1.04,
    },
    'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 1.1796, #AOD: 1.68, #MCM: 1.5 #XSDB: 1.49
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 1.14,
    },
    'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 0.28833, #AOD: 0.316, #MCM: 0.346 #XSDB: 0.3419
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 0.88,
    },
    'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 0.006945, #AOD: 0.0072, #MCM: 0.0053 #XSDB: 0.005146
        'matcheff': 1.,
        'kfactor' : 1.23, #AOD: 0.88,
    },

    # Twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns?rev=153
    'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 18610.0,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # Twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns?rev=153
    'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 6077.22, #XSDB: 6529.0 #MCM: 7181.0 #AOD(LO): 5321.0 #6025.2
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-ext2-v1' : {
        'nevents' : 1,
        'xsec'    : 6077.22, #XSDB: 6529.0 #MCM: 7181.0 #AOD(LO): 5321.0 #6025.2
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # From XSDB
    'ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 145.3,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 34.29,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 18.57,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # ------------
    # W+Jets
    # ------------
    # Twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns?rev=153#W_jets
    'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 61526.7, #XSDB: 52850.0 #mcm: 121700
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # Values below from twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns?rev=153#W_jets
    # and 70-100 HT bin from XSDB with CUETP8M1 tune (similar to twiki values for other bins)
    'WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 1353.0, #XSDB CP5: 1292.0
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 1345.0, #XSDB CP5: 1395.0 #XSDB CUETP8M1: 1346.0
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 359.7, #XSDB CP5: 407.9 #XSDB CUETP8M1: 360.1
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 48.91, #XSDB CP5: 57.48 #XSDB CUETP8M1: 48.8
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 12.05, #XSDB CP5: 12.87 #XSDB CUETP8M1: 12.07
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 5.501, #XSDB CP5: 5.366 #XSDB CUETP8M1: 5.497
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 1.329, #XSDB 1.074 #XSDB CUETP8M1: 1.329
        'matcheff': 1.,
        'kfactor' : 1.21,
    },
    'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.03216, #XSDB 0.008001 #XSDB CUETP8M1: 0.03209
        'matcheff': 1.,
        'kfactor' : 1.21,
    },

    # From XSDB 2017
    'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 315.2,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 68.58,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 34.69,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    # ------------
    # SM Higgs
    # ------------

    'GluGluHToBB_M125_13TeV_powheg_pythia8-1' : {
        'nevents' : 1,
        'xsec'    : 30.52,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'VBFHToBB_M-125_13TeV_powheg_pythia8-v3' : {
        'nevents' : 1,
        'xsec'    : 3.861,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.554,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.1565,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 0.07924,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.04884,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.01222,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.006185,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.3654,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.585,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 0.176,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 0.2819,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8-v3' : {
        'nevents' : 1,
        'xsec'    : 0.5269,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    }


samples = {

    #DATA
    'data_obs' : {
        'order' : 0,
        'files' : [
                   # 'DisplacedJet_Run2018A-17Sep2018-v1', #4,657,376 events
                   # 'DisplacedJet_Run2018B-17Sep2018-v1', #2,207,166 events
                   # 'DisplacedJet_Run2018C-17Sep2018-v1', #2,072,089 events
                   # 'DisplacedJet_Run2018D-PromptReco-v2', #11,025,759 events
                   # 'ParkingBPH1_Run2018D-05May2019promptD-v1',
                   # -------------------
                   # ParkingBPH_Run2018A
                   # -------------------
                   'ParkingBPH1_Run2018A-05May2019-v1',# files: 4919 # events: 205,952,869
                   'ParkingBPH2_Run2018A-05May2019-v1',# files: 4837
                   'ParkingBPH3_Run2018A-05May2019-v1',# files: 4934
                   'ParkingBPH4_Run2018A-05May2019-v1',# files: 4903
                   'ParkingBPH5_Run2018A-05May2019-v1',# files: 4902
                   'ParkingBPH6_Run2018A-05May2019-v1',# files: 5019
                  ],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
        },

    #DATA
    'data_DisplacedJet2018' : {
        'order' : 0,
        'files' : ['DisplacedJet_Run2018A-17Sep2018-v1', #4,657,376 events
                   'DisplacedJet_Run2018B-17Sep2018-v1', #2,207,166 events
                   'DisplacedJet_Run2018C-17Sep2018-v1', #2,072,089 events
                   'DisplacedJet_Run2018D-PromptReco-v2', #11,025,759 events
                  ],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
        },

    'data_ParkingBPH' : {
        'order' : 0,
        'files' : [# #RunA
                   'ParkingBPH1_Run2018A-05May2019-v1',# files: 4919 # events: 205,952,869
                   'ParkingBPH2_Run2018A-05May2019-v1',# files: 4837
                   'ParkingBPH3_Run2018A-05May2019-v1',# files: 4934
                   'ParkingBPH4_Run2018A-05May2019-v1',# files: 4903
                   'ParkingBPH5_Run2018A-05May2019-v1',# files: 4902
                   'ParkingBPH6_Run2018A-05May2019-v1',# files: 5019
                   # #RunB
                   # 'ParkingBPH1_Run2018B-05May2019-v2', #251,658,697 events
                   # 'ParkingBPH2_Run2018B-05May2019-v2',
                   # 'ParkingBPH3_Run2018B-05May2019-v2',
                   # 'ParkingBPH4_Run2018B-05May2019-v2',
                   # 'ParkingBPH5_Run2018B-05May2019-v2',
                   # 'ParkingBPH6_Run2018B-05May2019-v2',
                   # #RunC
                   # 'ParkingBPH1_Run2018C-05May2019-v1', #226,677,260 events
                   # 'ParkingBPH2_Run2018C-05May2019-v1',
                   # 'ParkingBPH3_Run2018C-05May2019-v1',
                   # 'ParkingBPH4_Run2018C-05May2019-v1',
                   # 'ParkingBPH5_Run2018C-05May2019-v1',
                   # #RunD
                   # 'ParkingBPH1_Run2018D-05May2019promptD-v1', #1,619,434,372 events
                   # 'ParkingBPH2_Run2018D-05May2019promptD-v1',
                   # 'ParkingBPH3_Run2018D-05May2019promptD-v1',
                   # 'ParkingBPH4_Run2018D-05May2019promptD-v1',
                   # 'ParkingBPH5_Run2018D-05May2019promptD-v1',
                  ],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
        },

    # Dummy entry for background sum
    'BkgSum' : {
        'order' : 0,
        'files' : [],
        'fillcolor' : 1,
        'fillstyle' : 3003,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Bkg stat.",
        'weight': 1.,
        'plot': True,
        },

    ########################################################

    #QCD combined
    'QCD_HT' : {
        'files' : [
             'QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             # ----  Older productions ----
             # 'QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
             # 'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
             # 'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
             # 'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
             ],
        'fillcolor' : 920,
        'fillstyle' : 1001,
        'linecolor' : 920,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : 'QCD',
        'title' : 'QCD',
        'weight': 1.,
        'plot': True,
    },

    'QCD_MuEnriched' : {
        'files' : [
            'QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3',
            'QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v4',
            'QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3',
            'QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3',
            'QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2',
            'QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2',
            'QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3',
            'QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext3-v1',
            'QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext1-v2',
            'QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
            'QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8-ext3-v2',
            'QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
            # ---- Non-ext samples (invalid?) ----
            # 'QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
            # 'QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',
            # 'QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v3',
            # 'QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8-v1',

             ],
        'fillcolor' : 920,
        'fillstyle' : 1001,
        'linecolor' : 920,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : 'QCD',
        'title' : 'QCD',
        'weight': 1.,
        'plot': True,
    },

    #TTbar
    'TTbar' : {
        'files' : [
            'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v1',
            'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v1',
            'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v1',
            # ----  Older productions ----
            # 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
            # 'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
            # 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
            # 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v1_0', #NOTE for v3: Merged only 5% of crab outputs!
            # 'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v1_0', #NOTE for v3: Merged only 10% of crab outputs!
            # 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v1_0', #NOTE for v3: Merged only 10% of crab outputs!
            ],
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",
        'weight': 1.,
        'plot': True,
    },

    #Single top
    'ST' : {
        'files' : [
            'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1-v1',
            'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1-v1',
            'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8_ext1-v4',
            'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1',
            'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1',
            # ----  Older productions ----
            # 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
            # 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1_0p1', #NOTE for v5: Merged only 5% of crab outputs!
            # 'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8_ext1-v4_0', #NOTE for v3: Merged only 10% of crab outputs!
            # 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1_0', #NOTE for v3: Merged only 10% of crab outputs!
            # 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1_0', #NOTE for v3: Merged only 10% of crab outputs!
            ],
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Single t",
        'weight': 1.,
        'plot': True,
    },

    'Top' : {
        'files' : [
            'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v1',
            'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v1',
            'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v1'
            'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1-v1',
            'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_ext1-v1',
            'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8_ext1-v4',
            'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1',
            'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8-v1',
            ],
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Single t",
        'weight': 1.,
        'plot': True,
    },

    #Diboson
    'VV' : {
        'files' : [
            'WW_TuneCP5_13TeV-pythia8-v2',
            'WZ_TuneCP5_13TeV-pythia8-v3',
            'ZZ_TuneCP5_13TeV-pythia8-v2'],
        'fillcolor' : 856,#602,
        'fillstyle' : 1001,
        'linecolor' : 856,#602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "VV",
        'weight': 1.,
        'plot': True,
    },

    #DYJets
    'ZJetsToNuNu' : {
        'files' : [
            'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v2',
            'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z + jets",
        'weight': 1.,
        'plot': True,
    },

    'DYJetsToLL' : {
        'files' : [
            'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            # 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-v1',
            'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-ext2-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z + jets",
        'weight': 1.,
        'plot': True,
    },

    'ZJetsToQQ' : {
        'files' : [
            'ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z + jets",
        'weight': 1.,
        'plot': True,
    },

    'DYJets' : {
        'files' : [
            'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v2',
            'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1',
            'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            # 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-v1',
            'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-ext2-v1',
            'ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z + jets",
        'weight': 1.,
        'plot': True,
    },

    'WJetsToLNu_inclusive' : {
        'files' : [
            'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W + jets",
        'weight': 1.,
        'plot': True,
    },

    'WJetsToLNu_HT' : {
        'files' : [
            'WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W + jets",
        'weight': 1.,
        'plot': True,
    },

    'WJetsToQQ' : {
        'files' : [
            'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W + jets",
        'weight': 1.,
        'plot': True,
    },

    'WJets' : {
        'files' : [
            # --- WJetsToLNu inclusive ---
            # 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            # --- WJetsToLNu HT-binned ---
            'WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            # -------   WJetsToQQ  -------
            'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            # ----  Older productions ----
            # 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2_withVertices',
            # 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2_0p1', #NOTE for v5: Merged only 5% of crab outputs!
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W + jets",
        'weight': 1.,
        'plot': True,
    },

    'VJets' : {
        'files' : [
            'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v2',
            'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1',
            'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1',
            'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            # 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-v1',
            'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8-ext2-v1',
            'ZJetsToQQ_HT400to600_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'ZJetsToQQ_HT600to800_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'ZJetsToQQ_HT-800toInf_qc19_4j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            # 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            'WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            'WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
            ],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W/Z + jets",
        'weight': 1.,
        'plot': True,
    },

    'SM_Higgs' : {
        'files' : [
            'GluGluHToBB_M125_13TeV_powheg_pythia8-1',
            'VBFHToBB_M-125_13TeV_powheg_pythia8-v3',
            'ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v1',
            'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-v1',
            'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8-v2',
            'WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v1',
            'WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v1',
            'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2',
            'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2',
            'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8-v3'
            # ----  Older productions ----
            # 'ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v1',
            # 'ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-v1',
            # 'ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8-v1',
            # 'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8-v3_0', #NOTE for v3: Merged only 10% of crab outputs!
            ],
        'fillcolor' : 825,
        'fillstyle' : 1001,
        'linecolor' : 825,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "SM Higgs",
        'weight': 1.,
        'plot': True,
    },

    ########################################################

    #VBF, m15
    'VBFH_M15_ctau0' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-0_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 15,
        'ctau' : 0.001,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 0 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau0p05' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-0p05_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 15,
        'ctau' : 0.05,
        'fillcolor' : 417,
        'fillstyle' : 0,
        'linecolor' : 417,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 0.05 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau0p1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-0p1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 15,
        'ctau' : 0.1,
        'fillcolor' : 802,
        'fillstyle' : 0,
        'linecolor' : 802,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 0.1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m15 c #tau 1',
        'mass' : 15,
        'ctau' : 1,
        'fillcolor' : 602,
        'fillstyle' : 0,
        'linecolor' : 602,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau5' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-5_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 15,
        'ctau' : 5,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 5 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau10' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m15 c #tau 10',
        'mass' : 15,
        'ctau' : 10,
        'fillcolor' : 601,
        'fillstyle' : 3004,
        'linecolor' : 601,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV",#"VBFH",#"c#tau_{0} = 10 mm",#
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau25' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-25_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 15,
        'ctau' : 25,
        'fillcolor' : 826,
        'fillstyle' : 3004,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 25 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau50' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-15_ctauS-50_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m15 c #tau 50',
        'mass' : 15,
        'ctau' : 50,
        'fillcolor' : 634,
        'fillstyle' : 3004,
        'linecolor' : 634,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "c#tau_{0} = 50 mm",#m_{#pi} = 15 GeV,
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau100' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'mass' : 15,
        'ctau' : 100,
        'fillcolor' : 635,
        'fillstyle' : 3004,
        'linecolor' : 635,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "c#tau_{0} = 100 mm",#m_{#pi} = 15 GeV,
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau500' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-500_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'
            ],
        'mass' : 15,
        'ctau' : 500,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 500 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau1000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
                ],
        'title' : 'VBFH m15 c #tau 1000',
        'mass' : 15,
        'ctau' : 1000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 1000 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau2000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-2000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'mass' : 15,
        'ctau' : 2000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 2000 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau5000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-5000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'
            ],
        'mass' : 15,
        'ctau' : 5000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 5000 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau10000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m15 c #tau 10000',
        'mass' : 15,
        'ctau' : 10000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 10000 mm",
        'weight': 1.,
        'plot': True,
    },


#VBF, m40
    'VBFH_M40_ctau0' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-0_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 0',
        'mass' : 40,
        'ctau' : 0.001,
        'fillcolor' : 632,
        'fillstyle' : 0,
        'linecolor' : 632,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = 0 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau0p05' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-0p05_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 0.05',
        'mass' : 40,
        'ctau' : 0.05,
        'fillcolor' : 635,
        'fillstyle' : 0,
        'linecolor' : 635,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = 0.05 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau0p1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-0p1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 0.1',
        'mass' : 40,
        'ctau' : 0.1,
        'fillcolor' : 600,
        'fillstyle' : 0,
        'linecolor' : 600,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = 0.1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 1',
        'mass' : 40,
        'ctau' : 1,
        'fillcolor' : 433,
        'fillstyle' : 0,
        'linecolor' : 433,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = 1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau5' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-5_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 5',
        'mass' : 40,
        'ctau' : 5,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau10' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 10',
        'mass' : 40,
        'ctau' : 10,
        'fillcolor' : 618,
        'fillstyle' : 3004,
        'linecolor' : 618,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV",#"c#tau_{0} = 10 mm",#
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau25' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-25_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 25',
        'mass' : 40,
        'ctau' : 25,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau50' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-40_ctauS-50_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m40 c #tau 50',
        'mass' : 40,
        'ctau' : 50,
        'fillcolor' : 634,
        'fillstyle' : 3004,
        'linecolor' : 634,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "c#tau_{0} = 50 mm",#m_{#pi} = 40 GeV,
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau100' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-40_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 100',
        'mass' : 40,
        'ctau' : 100,
        'fillcolor' : 635,
        'fillstyle' : 3004,
        'linecolor' : 635,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "c#tau_{0} = 100 mm",#m_{#pi} = 40 GeV,
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau500' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-40_ctauS-500_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 500',
        'mass' : 40,
        'ctau' : 500,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = 500 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau1000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-40_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 1000',
        'mass' : 40,
        'ctau' : 1000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = 1000 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau2000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-40_ctauS-2000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 2000',
        'mass' : 40,
        'ctau' : 2000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau5000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-40_ctauS-5000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 5000',
        'mass' : 40,
        'ctau' : 5000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau10000' : {
        'files' : [
            'VBFH_HToSSTo4b_MH-125_MS-40_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 10000',
        'mass' : 40,
        'ctau' : 10000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },


    #VBF, m55
    'VBFH_M55_ctau0' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-0_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 0.001,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 0 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau0p05' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-0p05_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 0.05,
        'fillcolor' : 824,
        'fillstyle' : 0,
        'linecolor' : 824,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 0.05 mm",
        'weight': 1.,
        'plot': True,
    },
        'VBFH_M55_ctau0p1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-0p1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 0.1,
        'fillcolor' : 824,
        'fillstyle' : 0,
        'linecolor' : 824,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 0.1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m55 c #tau 1',
        'mass' : 55,
        'ctau' : 1,
        'fillcolor' : 813,
        'fillstyle' : 0,
        'linecolor' : 813,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau1' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m55 c #tau 1',
        'mass' : 55,
        'ctau' : 1,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 1 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau5' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-5_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 5,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 5 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau10' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m55 c #tau 10',
        'mass' : 55,
        'ctau' : 10,
        'fillcolor' : 633,
        'fillstyle' : 3004,
        'linecolor' : 633,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV",#"c#tau_{0} = 10 mm",#
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau25' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-25_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 25,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 25 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau50' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-50_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m55 c #tau 50',
        'mass' : 55,
        'ctau' : 50,
        'fillcolor' : 634,
        'fillstyle' : 3004,
        'linecolor' : 634,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "c#tau_{0} = 50 mm",#m_{#pi} = 55 GeV,
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau100' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 100,
        'fillcolor' : 635,
        'fillstyle' : 3004,
        'linecolor' : 635,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "c#tau_{0} = 100 mm",#m_{#pi} = 55 GeV,
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau500' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-500_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 500,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = 500 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau1000' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m55 c #tau 1000',
        'mass' : 55,
        'ctau' : 1000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau2000' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-2000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 2000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau5000' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-5000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'mass' : 55,
        'ctau' : 5000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau10000' : {
        'files' : ['VBFH_HToSSTo4b_MH-125_MS-55_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'VBFH m55 c #tau 10000',
        'mass' : 55,
        'ctau' : 10000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },

    # Missing signal point in central production:
    # 'ggH_M15_ctau1' : {
    #     'files' : ['ggH_HToSSTobbbb_MH-125_MS-15_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
    #     'title' : 'ggH m15 c #tau 1',
    #     'mass' : 15,
    #     'ctau' : 1,
    #     'fillcolor' : 632,
    #     'fillstyle' : 3004,
    #     'linecolor' : 632,
    #     'linewidth' : 3,
    #     'linestyle' : 1,
    #     'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 1 mm",
    #     'weight': 1.,
    #     'plot': True,
    # },

    'ggH_M15_ctau10' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-15_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m15 c #tau 10',
        'mass' : 15,
        'ctau' : 10,
        'fillcolor' : 600,
        'fillstyle' : 3004,
        'linecolor' : 600,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "ggH #rightarrow #pi#pi #rightarrow b#bar{b}b#bar{b}, m_{#pi} = 15 GeV, c#tau_{0} = 10 mm",#",#"ggH",#"
        # 'label' : "m_{#pi} = 15 GeV",#, c#tau_{0} = 10 mm",#",#"ggH",#"
        # 'label' : "c#tau_{0} = 10 mm",#",#"ggH",#"
        'weight': 1.,
        'plot': True,
    },

    'ggH_M15_ctau100' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-15_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m15 c #tau 100',
        'mass' : 15,
        'ctau' : 100,
        'fillcolor' : 601,
        'fillstyle' : 3004,
        'linecolor' : 601,
        'linewidth' : 3,
        'linestyle' : 1,
        # 'label' : "m_{#pi} = 15 GeV",#, c#tau_{0} = 100 mm",#
        'label' : "c#tau_{0} = 100 mm",#
        'weight': 1.,
        'plot': True,
    },

    'ggH_M15_ctau1000' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-15_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m15 c #tau 1000',
        'mass' : 15,
        'ctau' : 1000,
        'fillcolor' : 602,
        'fillstyle' : 3004,
        'linecolor' : 602,
        'linewidth' : 3,
        'linestyle' : 1,
        # 'label' : "m_{#pi} = 15 GeV",#, c#tau_{0} = 1000 mm",
        'label' : "c#tau_{0} = 1000 mm",
        'weight': 1.,
        'plot': True,
    },

    'ggH_M15_ctau10000' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-15_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m15 c #tau 10000',
        'mass' : 15,
        'ctau' : 10000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV",#, c#tau_{0} = 10000 mm",
        'weight': 1.,
        'plot': True,
    },

    'ggH_M40_ctau1' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-40_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m40 c #tau 1',
        'mass' : 40,
        'ctau' : 1,
        'fillcolor' : 617,
        'fillstyle' : 3004,
        'linecolor' : 617,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV",#, c#tau_{0} = 1 mm",#
        'weight': 1.,
        'plot': True,
    },

    'ggH_M40_ctau10' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-40_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m40 c #tau 10',
        'mass' : 40,
        'ctau' : 10,
        'fillcolor' : 618,
        'fillstyle' : 3004,
        'linecolor' : 618,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV",#, c#tau_{0} = 10 mm",#
        'weight': 1.,
        'plot': True,
    },

    'ggH_M40_ctau100' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-40_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m40 c #tau 100',
        'mass' : 40,
        'ctau' : 100,
        'fillcolor' : 619,
        'fillstyle' : 3004,
        'linecolor' : 619,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV",#, c#tau_{0} = 100 mm",#
        'weight': 1.,
        'plot': True,
    },

    'ggH_M40_ctau1000' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-40_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m40 c #tau 1000',
        'mass' : 40,
        'ctau' : 1000,
        'fillcolor' : 635,
        'fillstyle' : 3004,
        'linecolor' : 635,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV",#, c#tau_{0} = 1000 mm",
        'weight': 1.,
        'plot': True,
    },

    'ggH_M40_ctau10000' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-40_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m40 c #tau 10000',
        'mass' : 40,
        'ctau' : 10000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV",#, c#tau_{0} = 10000 mm",
        'weight': 1.,
        'plot': True,
    },

    'ggH_M55_ctau1' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-55_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m55 c #tau 1',
        'mass' : 55,
        'ctau' : 1,
        'fillcolor' : 632,
        'fillstyle' : 3004,
        'linecolor' : 632,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV",#, c#tau_{0} = 1 mm",#
        'weight': 1.,
        'plot': True,
    },

    'ggH_M55_ctau10' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-55_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m55 c #tau 10',
        'mass' : 55,
        'ctau' : 10,
        'fillcolor' : 633,
        'fillstyle' : 3004,
        'linecolor' : 633,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV",#, c#tau_{0} = 10 mm",#
        'weight': 1.,
        'plot': True,
    },

    'ggH_M55_ctau100' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-55_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m55 c #tau 100',
        'mass' : 55,
        'ctau' : 100,
        'fillcolor' : 634,
        'fillstyle' : 3004,
        'linecolor' : 634,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV",#, c#tau_{0} = 100 mm",#
        'weight': 1.,
        'plot': True,
        },

    'ggH_M55_ctau1000' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-55_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m55 c #tau 1000',
        'mass' : 55,
        'ctau' : 1000,
        'fillcolor' : 635,
        'fillstyle' : 3004,
        'linecolor' : 635,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV",#, c#tau_{0} = 1000 mm",
        'weight': 1.,
        'plot': True,
    },

    'ggH_M55_ctau10000' : {
        'files' : ['ggH_HToSSTobbbb_MH-125_MS-55_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD'],
        'title' : 'ggH m55 c #tau 10000',
        'mass' : 55,
        'ctau' : 10000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV",#, c#tau_{0} = 10000 mm",
        'weight': 1.,
        'plot': True,
    },

    }
