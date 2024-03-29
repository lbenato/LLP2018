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
#### VBF

# 2017 campaign
    'VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAODv2' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },


    # 2018 campaign
    'VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18MiniAOD' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    

#### gg Fusion
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

    '': {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    '': {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    '': {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 23700000.0,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 1547000.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 322600.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 29980.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 6334.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 1088.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 99.11,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 20.23,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    # 'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-v2': {
    #     'nevents' : 1,
    #     'xsec'    : 1, #TODO: no xsec in mcm for /TT_TuneCH3_13TeV-powheg-herwig7/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM
    #     'matcheff': 1.,
    #     'kfactor' : 1.,
    #     },

    'TTJets_TuneCP5_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 496.1,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 377.96,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 365.34,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 88.29,
        'matcheff': 1.,
        'kfactor' : 1.,
        },


    'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v2': {
        'nevents' : 1,
        'xsec'    : 34.97,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v2': {
        'nevents' : 1,
        'xsec'    : 34.91,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v2': {
        'nevents' : 1,
        'xsec'    : 3.74,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2': {
        'nevents' : 1,
        'xsec'    : 67.91,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2': {
        'nevents' : 1,
        'xsec'    : 113.3,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'VBFHToBB_M-125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 3.861,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'WW_TuneCP5_13TeV-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 75.8,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'WZ_TuneCP5_13TeV-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 27.6,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ZZ_TuneCP5_13TeV-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 12.14,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1-v2': {
        'nevents' : 1,
        'xsec'    : 5343.0,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 1728.0,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 50380.0,
        'matcheff': 1.,
        'kfactor' : 1.,
        },


    'ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.554,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8_ext1-v2': {
        'nevents' : 1,
        'xsec'    : 0.1565,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.07924,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.585,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.3654,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.176,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.2819,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'GluGluToHHTo4B_node_SM_13TeV-madgraph-v2': {
        'nevents' : 1,
        'xsec'    : 1.,# not in mcm
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8-v2': {
        'nevents' : 1,
        'xsec'    : 0.5269,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

    'VBFHHTo4B_CV_1_C2V_1_C3_1_13TeV-madgraph-v2': {
        'nevents' : 1,
        'xsec'    : 0.00162,
        'matcheff': 1.,
        'kfactor' : 1.,
        },


   #ZJetsToNuNu
    #x-sec taken from DAS/mcm
    'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 302.8,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 92.59,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 13.18,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 3.257,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 1.49,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 0.3419,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 0.005146,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    }


samples = {

    #DATA
    'data_obs' : {
        'order' : 0,
        'files' : ['METRun2016B-03Feb2017_ver2-v2'],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
        },

    ########################################################

    #QCD combined
    'QCD' : {
        'files' : [
            #'QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8-v2',
            'QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8-v2', 'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8-v2'],
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

    #TTJets
    'TTJets' : {
        'files' : ['TTJets_TuneCP5_13TeV-madgraphMLM-pythia8-v2',],
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "tt jets",
        'weight': 1.,
        'plot': True,
    },

    #TTbar
    'TTbar' : {
        'files' : ['TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v2', 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v2', 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v2'],
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
        'files' : ['ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v2', 'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v2', 'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v2', 'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2', 'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2'],
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Single t",
        'weight': 1.,
        'plot': True,
    },


    #Nice plotting
    'Top' : {
        'files' : ['TTJets_TuneCP5_13TeV-madgraphMLM-pythia8-v2','ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v2', 'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v2', 'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v2', 'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2', 'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2'
                   #'TTToHadronic_TuneCP5_13TeV-powheg-pythia8-v2', 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8-v2', 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8-v2', 'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext1-v2', 'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v2', 'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v2', 'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2', 'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1-v2'
                   ],
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}, single-t",
        'weight': 1.,
        'plot': True,
    },

    #ZJetsToNuNu
    'ZJetsToNuNu' : {
        'files' : ['ZJetsToNuNu_HT-100To200_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v2',],
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z jets to NuNu",
        'weight': 1.,
        'plot': True,
    },


    'DYJetsToQQ' : {
        'files' : ['DYJetsToQQ_HT180_13TeV-madgraphMLM-pythia8-v2'],
        'fillcolor' : 858,
        'fillstyle' : 1001,
        'linecolor' : 858,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "DY jets to QQ",
        'weight': 1.,
        'plot': True,
    },

    'DYJetsToLL' : {
        'files' : ['DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1-v2'],
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
},


    #Nice plotting
    'DYJets' : {
        'files' : ['ZJetsToNuNu_HT-100To200_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v2', 'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v2','DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1-v2'],
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "DY + jets",
        'weight': 1.,
        'plot': True,
    },


    #WJets
    'WJetsToLNu' : {
        'files' : ['WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2'],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W jets to LNu",
        'weight': 1.,
        'plot': True,
    },

    'WJetsToQQ' : {
        'files' : ['WJetsToQQ_HT180_13TeV-madgraphMLM-pythia8-v2'],
        'fillcolor' : 880,
        'fillstyle' : 1001,
        'linecolor' : 880,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W jets to QQ",
        'weight': 1.,
        'plot': True,
    },

    #Nice plotting
    'WJets' : {
        'files' : ['WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2',],# 'WJetsToQQ_HT180_13TeV-madgraphMLM-pythia8-v2'],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W + jets",
        'weight': 1.,
        'plot': True,
    },


    #Dibosons
    'VV' : {
        'files' : ['WW_TuneCP5_13TeV-pythia8-v2', 'WZ_TuneCP5_13TeV-pythia8-v2', 'ZZ_TuneCP5_13TeV-pythia8-v2'],
        'fillcolor' : 602,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "WW, WZ, ZZ",
        'weight': 1.,
        'plot': True,
    },

    #VBF true higgs
    'VBF_Higgs' : {
        'files' : ['VBFHToBB_M-125_13TeV_powheg_pythia8-v2'],
        'mass' : 40,
        'ctau' : 0.005,
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "VBF H #rightarrow b#bar{b}",
        'weight': 1.,
        'plot': True,
    },

    'VH' : {
        'files' : ['ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v2', 'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-v2', 'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1-v2', 'WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v2', 'WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v2', 'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2', 'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2',],
        'fillcolor' : 420,
        'fillstyle' : 1001,
        'linecolor' : 420,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "VH",
        'weight': 1.,
        'plot': True,
    },

    'ggH' : {
        'files' : ['GluGluHToBB_M125_TuneCP5_13TeV-powheg-pythia8-v2'],
        'fillcolor' : 635,
        'fillstyle' : 1001,
        'linecolor' : 635,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ggH",
        'weight': 1.,
        'plot': True,
    },

    'ttH' : {
        'files' : ['ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8-v2',],# 'bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo-v2'],
        'fillcolor' : 821,
        'fillstyle' : 1001,
        'linecolor' : 821,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ttH",# bbH",
        'weight': 1.,
        'plot': True,
    },

    'HH' : {
        'files' : ['VBFHHTo4B_CV_1_C2V_1_C3_1_13TeV-madgraph-v2'],
        'fillcolor' : 825,
        'fillstyle' : 1001,
        'linecolor' : 825,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "VBF HH",
        'weight': 1.,
        'plot': True,
    },

    'SM_Higgs' : {
        'files' : ['VBFHToBB_M-125_13TeV_powheg_pythia8-v2', 'ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8-v2', 'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8-v2', 'ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8_ext1-v2', 'WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v2', 'WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8-v2', 'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2', 'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8-v2',],# 'GluGluHToBB_M125_TuneCP5_13TeV-powheg-pythia8-v2', 'bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo-v2'],
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

    'ggH_MH-125_2016': {
        'files' : ['ggH_HToSSTobbbb_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
        'fillcolor' : 801,
        'fillstyle' : 0,
        'linecolor' : 801,
        'linewidth' : 4,
        'linestyle' : 2,
        'label' : "ggH 2016 campaign",
        'weight': 1.,
        'plot': True,
        },


    ########################################################

    #VBF, m15
    'VBFH_M15_ctau0' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0p05_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0p1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m15 c #tau 10',
        'mass' : 15,
        'ctau' : 10,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 10 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau25' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-25_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'mass' : 15,
        'ctau' : 25,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 25 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau50' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-50_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m15 c #tau 50',
        'mass' : 15,
        'ctau' : 50,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 50 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau100' : {
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
            ],
        'mass' : 15,
        'ctau' : 100,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 15 GeV, c#tau_{0} = 100 mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M15_ctau500' : {
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-500_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-2000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p05_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m40 c #tau 10',
        'mass' : 40,
        'ctau' : 10,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau25' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-25_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-50_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m40 c #tau 50',
        'mass' : 40,
        'ctau' : 50,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau100' : {
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
            ],
        'title' : 'VBFH m40 c #tau 100',
        'mass' : 40,
        'ctau' : 100,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 40 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M40_ctau500' : {
        'files' : [
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-500_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-2000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD',
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-0_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-0p05_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-0p1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-1_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m55 c #tau 1',
        'mass' : 55,
        'ctau' : 1,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau5' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-5_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'mass' : 55,
        'ctau' : 5,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau10' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-10_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m55 c #tau 10',
        'mass' : 55,
        'ctau' : 10,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau25' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-25_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'mass' : 55,
        'ctau' : 25,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau50' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-50_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'title' : 'VBFH m55 c #tau 50',
        'mass' : 55,
        'ctau' : 50,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau100' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-100_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
        'mass' : 55,
        'ctau' : 100,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#pi} = 55 GeV, c#tau_{0} = ... mm",
        'weight': 1.,
        'plot': True,
    },
    'VBFH_M55_ctau500' : {
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-500_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-1000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-2000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-5000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-10000_TuneCP5_13TeV-powheg-pythia8_RunIIFall17MiniAOD'],
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





    }
