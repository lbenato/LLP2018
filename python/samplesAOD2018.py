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

    #ZJetsToNuNu
    'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 384.1,
        'matcheff': 1.,
        'kfactor' : 1.37,
    },
    'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 118.1,
        'matcheff': 1.,
        'kfactor' : 1.52,
    },
    'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 14.7,
        'matcheff': 1.,
        'kfactor' : 1.37,
    },
    'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 3.35,
        'matcheff': 1.,
        'kfactor' : 1.04,
    },
    'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 1.68,
        'matcheff': 1.,
        'kfactor' : 1.14,
    },
    'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 0.316,
        'matcheff': 1.,
        'kfactor' : 0.88,
    },
    'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1' : {
        'nevents' : 1,
        'xsec'    : 0.0072,
        'matcheff': 1.,
        'kfactor' : 0.88,
    },

    'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-v2' : {
        'nevents' : 1,
        'xsec'    : 52850.0,#second entry on XSDB, 50260.0,
        'matcheff': 1.,
        'kfactor' : 0.88,
    },


    #WJetsToLNu HT binned
    'WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 1292.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 1395.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 407.9,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 57.48,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 12.87,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 5.366,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 1.074,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1,
        'xsec'    : 0.008001,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    #2017 numbers!!
    'QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8-v1': {
        'nevents' : 93954381,
        #'xsec' : 28060000.0,#pb#2016 numbers
        'xsec'    : 23700000.0,#XSDB for 2018 is empty..
        #'xsec' : 19380000, #mcm, seems completely wrong
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 18722416,
        #'xsec' : 1710000.0,#pb#2016
        'xsec'    : 1547000.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 17035891,
        #'xsec'   : 351300,#pb#B2G-17-005
        'xsec'    : 322600.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 18929951,
        #'xsec'   : 31630,#pb#B2G-17-005
        'xsec'    : 29980.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 15629253,
        #'xsec'   : 6802,#pb#B2G-17-005
        'xsec'    : 6334.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 4767100,
        #'xsec' : 1206,#pb#B2G-17-005
        'xsec'    : 1088.0,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 3970819,
        #'xsec' : 120.4,#pb
        'xsec'    : 99.11,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1' : {
        'nevents' : 1991645,
        #'xsec' : 25.25,#pb
        'xsec'    : 20.23,#XSDB
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    #TTbar
    'TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_ext1-v2' : {
        'nevents' : 1,
        'xsec'    : 722.8,#x-sec DB
        'matcheff': 1.,
        'kfactor' : 1.,
    },

    'n3n2-n1-hbb-hbb_mh400_pl1000' : {
        'nevents' : 1,
        'xsec'    : 88.7325,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'n3n2-n1-hbb-hbb_mh300_pl1000' : {
        'nevents' : 1,
        'xsec'    : 284.855,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'n3n2-n1-hbb-hbb_mh250_pl1000' : {
        'nevents' : 1,
        'xsec'    : 577.314,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'n3n2-n1-hbb-hbb_mh200_pl1000' : {
        'nevents' : 1,
        'xsec'    : 1335.62,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'n3n2-n1-hbb-hbb_mh175_pl1000' : {
        'nevents' : 1,
        'xsec'    : 2583.965,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'n3n2-n1-hbb-hbb_mh150_pl1000' : {
        'nevents' : 1,
        'xsec'    : 3832.31,
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    'n3n2-n1-hbb-hbb_mh127_pl1000' : {
        'nevents' : 1,
        'xsec'    : 10314.755,
        'matcheff': 1.,
        'kfactor' : 1.,
    },    

    ##Dibosons
    ##WW
    #x-sec taken from B2G-17-005
    'WW_TuneCP5_13TeV-pythia8-v2' : {
        'nevents' : 994012,
#        'xsec'    : 75.8,#x-sec DB
        'xsec'    : 118.7,#B2G-17-005
        'matcheff': 1.,
        'kfactor' : 1.,
    },
    ##WZ
    #x-sec taken from B2G-17-005
    'WZ_TuneCP5_13TeV-pythia8-v3' : {
        'nevents' : 1000000,
#        'xsec'    : 27.6,#x-sec DB, fishy....
        'xsec'    : 47.2,#B2G-17-005
        'matcheff': 1.,
        'kfactor' : 1.,
    }, 
    #ZZ
    #x-sec taken from B2G-17-005
    'ZZ_TuneCP5_13TeV-pythia8-v2' : {
        'nevents' : 990064,
#        'xsec'    : 12.14,#x-sec DB, fishy....
        'xsec'    : 16.6,#B2G-17-005
        'matcheff': 1.,
        'kfactor' : 1.,
    },

}



samples = {

    #DATA
    'data_obs' : {
        'order' : 0,
        'files' : ['METRun2018A-17Sep2018-v1'],
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

    #BACKGROUNDS
    #QCD
    'QCD' : {
        'files' : [
             #'QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
             'QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8-v1','QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8-v1','QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8-v1'],
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
        'files' : ['TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_ext1-v2'],
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
        'files' : [],  
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Single t",
        'weight': 1.,
        'plot': True,
    },

    #ZJetsToNuNu
    'ZJetsToNuNu' : {
        'files' : ['ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1'],  
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z #rightarrow #nu #nu + jets",
        'weight': 1.,
        'plot': True,
    },
    'ZJetsToNuNuRed' : {
        'files' : [
            'ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1', 
            #'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1', 
            #'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v1', 
            'ZJetsToNuNu_HT-600To800_13TeV-madgraph-v1', 
            #'ZJetsToNuNu_HT-800To1200_13TeV-madgraph-v1', 
            #'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph-v1', 
            'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph-v1'
            ],  
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z jets to NuNu",
        'weight': 1.,
        'plot': True,
    },

    #WJets
    'WJetsToLNuIncl' : { 
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
    #HT binned
    'WJetsToLNu' : { 
        'files' : [
            ##'WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8-v1',
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
        'label' : "W #rightarrow l #nu + jets",
        'weight': 1.,
        'plot': True,
    },
    #Dibosons
    'VV' : {
        'files' : [
            'WW_TuneCP5_13TeV-pythia8-v2', 
            'WZ_TuneCP5_13TeV-pythia8-v3', 
            'ZZ_TuneCP5_13TeV-pythia8-v2'
        ],  
        'fillcolor' : 602,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "WW, WZ, ZZ",
        'weight': 1.,
        'plot': True,
    },
   
    #SIGNAL
######################################
#
#  JiaJing's AOD
    'SUSY_mh400_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh400_pl1000'],
        'mass' : 400,
        'ctau' : 1000,
        'fillcolor' : 1,
        'fillstyle' : 0,
        'linecolor' : 1,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 400 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

    'SUSY_mh300_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh300_pl1000'],
        'mass' : 300,
        'ctau' : 1000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 300 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

    'SUSY_mh250_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh250_pl1000'],
        'mass' : 250,
        'ctau' : 1000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 250 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

    'SUSY_mh200_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh200_pl1000'],
        'mass' : 200,
        'ctau' : 1000,
        'fillcolor' : 3,
        'fillstyle' : 0,
        'linecolor' : 3,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 200 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

    'SUSY_mh175_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh175_pl1000'],
        'mass' : 175,
        'ctau' : 1000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 175 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

    'SUSY_mh150_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh150_pl1000'],
        'mass' : 150,
        'ctau' : 1000,
        'fillcolor' : 4,
        'fillstyle' : 0,
        'linecolor' : 4,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 150 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

    'SUSY_mh127_pl1000' : {
        'files' : ['n3n2-n1-hbb-hbb_mh127_pl1000'],
        'mass' : 127,
        'ctau' : 1000,
        'fillcolor' : 826,
        'fillstyle' : 0,
        'linecolor' : 826,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{#chi} = 127 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },
######################################
#
#  Heavy Higgs AOD
    #MH 1000, MS 400
    'ggH_MH1000_MS400_ctau500' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-500_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 500,
        'fillcolor' : 9,
        'fillstyle' : 0,
        'linecolor' : 9,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H;S} = 1000;400 GeV, c#tau_{0} = 0.5 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH1000_MS400_ctau1000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 1000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        #'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 1 m",
        'label' : "m_{H/S} = 1 TeV/400 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH1000_MS400_ctau2000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-2000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,        
        'ctau' : 2000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 2 m",
        'weight': 1.,
        'plot': True,
    },    
    'ggH_MH1000_MS400_ctau5000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,        
        'ctau' : 5000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 5 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH1000_MS400_ctau10000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-400_ctauS-10000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 10000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 10 m",
        'weight': 1.,
        'plot': True,
    },

    #MH 1000, MS 150
    'ggH_MH1000_MS150_ctau500' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-500_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 150,
        'ctau' : 500,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 150 GeV, c#tau_{0} = 0.5 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH1000_MS150_ctau1000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 150,
        'ctau' : 1000,
        'fillcolor' : 418,
        'fillstyle' : 0,
        'linecolor' : 418,
        'linewidth' : 3,
        'linestyle' : 1,
        #'label' : "m_{H} = 1 TeV, m_{S} = 150 GeV, c#tau_{0} = 1 m",
        'label' : "m_{H/S} = 1 TeV/150 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH1000_MS150_ctau2000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-2000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 150,
        'ctau' : 2000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 150 GeV, c#tau_{0} = 2 m",
        'weight': 1.,
        'plot': True,
    },    
    'ggH_MH1000_MS150_ctau5000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-5000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 150,
        'ctau' : 5000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 150 GeV, c#tau_{0} = 5 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH1000_MS150_ctau10000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-10000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 150,
        'ctau' : 10000,
        'fillcolor' : 2,
        'fillstyle' : 0,
        'linecolor' : 2,
        'linewidth' : 3,
        'linestyle' : 1,
        'label' : "m_{H} = 1 TeV, m_{S} = 150 GeV, c#tau_{0} = 10 m",
        'weight': 1.,
        'plot': True,
    },

 #MH400
    'ggH_MH400_MS100_ctau1000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-400_MS-100_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 1000,
        'fillcolor' : 801,
        'fillstyle' : 0,
        'linecolor' : 801,
        'linewidth' : 3,
        'linestyle' : 1,
        #'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 1 m",
        'label' : "m_{H/S} = 400/100 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH400_MS50_ctau1000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-400_MS-50_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 1000,
        'fillcolor' : 825,
        'fillstyle' : 0,
        'linecolor' : 825,
        'linewidth' : 3,
        'linestyle' : 1,
        #'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 1 m",
        'label' : "m_{H/S} = 400/50 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },

 #MH200
    'ggH_MH200_MS50_ctau1000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-200_MS-50_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 1000,
        'fillcolor' : 1,
        'fillstyle' : 0,
        'linecolor' : 1,
        'linewidth' : 3,
        'linestyle' : 1,
        #'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 1 m",
        'label' : "m_{H/S} = 200/50 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },
    'ggH_MH200_MS25_ctau1000' : {
        'files' : ['GluGluH2_H2ToSSTobbbb_MH-200_MS-25_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC'],
        'MH' : 1000,
        'MS' : 400,
        'ctau' : 1000,
        'fillcolor' : 7,
        'fillstyle' : 0,
        'linecolor' : 7,
        'linewidth' : 3,
        'linestyle' : 1,
        #'label' : "m_{H} = 1 TeV, m_{S} = 400 GeV, c#tau_{0} = 1 m",
        'label' : "m_{H/S} = 200/25 GeV, c#tau_{0} = 1 m",
        'weight': 1.,
        'plot': True,
    },


}
