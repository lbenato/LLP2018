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
#private production test reason
    'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC' : {
        'nevents' : 100000,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
    },

# 2016 campaign
    'VBFH_HToSSTo4b_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },

  # separated samples
    'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-0p1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-5_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },
    'VBFH_HToSSTo4b_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3' : {
        'nevents' : 1,
        'xsec'    : 1.,
        'matcheff': 1.,
        'kfactor' : 1.,
        },


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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-0p1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-25_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-50_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'
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
            'VBFH_HToSSTobbbb_MH-125_MS-15_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0p1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-25_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-50_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
            'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3',
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-0p05_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-0p1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-1_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-5_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-25_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-50_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-500_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-1000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-2000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-5000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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
        'files' : ['VBFH_HToSSTobbbb_MH-125_MS-55_ctauS-10000_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16MiniAODv3'],
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