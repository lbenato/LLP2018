variable = {}

var_template = {
    "EventNumber": {
      "title" : "event number",
      "nbins" : 10000000,
      "min" : 0,
      "max" : 1.e7,
      "log" : False,
    },
    "LumiNumber": {
      "title" : "lumisection number",
      "nbins" : 2000,
      "min" : 0,
      "max" : 2000,
      "log" : False,
    },
    "RunNumber": {
      "title" : "run number",
      "nbins" : 7000,
      "min" : 254000,
      "max" : 261000,
      "log" : False,
    },
    "nPV": {
      "title" : "number of reconstructed Primary Vertices",
      "nbins" : 50,
      "min" : -0.5,
      "max" : 49.5,
      "log" : False,
    },
    "isVBF": {
      "title" : "isVBF",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
    "nCHSJets": {
      "title" : "number of CHS jets",
      "nbins" : 50,
      "min" : -0.5,
      "max" : 49.5,
      "log" : True,
    },
    "nAllJets": {
      "title" : "number of CHS jets up to |#eta|=5.2",
      "nbins" : 17,
      "min" : -0.5,
      "max" : 16.5,
      "log" : True,
    },
    "nCaloJets": {
      "title" : "number of calo jets",
      "nbins" : 17,
      "min" : -0.5,
      "max" : 16.5,
      "log" : True,
    },
    "nJets": {
      "title" : "number of jets",
      "nbins" : 17,
      "min" : -0.5,
      "max" : 16.5,
      "log" : True,
    },
    "nCaloTagJets": {
      "title" : "number of calo tagged jets",#from v3
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "nCHSFatJets": {
      "title" : "number of AK8 jets",
      "nbins" : 10,
      "min" : 0.5,
      "max" : 10.5,
      "log" : True,
    },
    "MEt_pt": {
      "title" : "E^{T}_{miss} (GeV)",
      "nbins" : 100,#45,
      "min" : 200,#100,
      "max" : 2200,
      "log" : True,
    },
    "met_pt_nomu": {
      "title" : "E_{T}^{miss} no #mu (GeV)",
      "nbins" : 50,#45,
      "min" : 0,#100,
      "max" : 1000,
      "log" : True,
    },
    "HT": {
      "title" : "H_{T} (GeV)",
      "nbins" : 50,#45,
      "min" : 0,#100,
      "max" : 2000,
      "log" : True,
    },
    "MinJetMetDPhi": {
      "title" : "MinJetMetDPhi",
      "nbins" : 64,#10,
      "min" : 0,
      "max" : 3.14,
      "log" : True,
    },
    "MinJetMetDPhiAllJets": {
      "title" : "MinJetMetDPhi all jets up to |#eta|=5.2",
      "nbins" : 64,#10,
      "min" : 0,
      "max" : 3.14,
      "log" : True,
    },


    # Jets vector
    #all jets together
    "Jets.pt": {
      "title" : "all jets p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },
    "Jets.CSV": {
      "title" : "all jets CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.alphaMax": {
      "title" : "all jets #alpha_{max}",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.sigIP2DMedian": {
      "title" : "all jets sigIP2DMedian",
      "nbins" : 100,
      "min" : -50,
      "max" : 50,
      "log" : True,
    },

    "Jets.eta": {
      "title" : "all jets #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : True,
    },
    "Jets.phi": {
      "title" : "all jets #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : True,
    },
    "Jets.mass": {
      "title" : "all jets mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : True,
    },
    "Jets.nSV": {
        "title" : "Number of SV per jet",
        "nbins" : 10,
        "min" : 0,
        "max" : 9,
        "log" :True,
        },
    "Jets.nSVCand": {
        "title" : "Number of SV candidates per jet",
        "nbins" : 10,
        "min" : 0,
        "max" : 9,
        "log" : False,
        },
    "Jets.nVertexTracks": {
        "title" : "Number of tracks per vertex",
        "nbins" : 21,
        "min" : 0,
        "max" : 20,
        "log" : False,
        },
    "Jets.nSelectedTracks": {
        "title" : "Number of selected tracks per jet",
        "nbins" : 51,"min" : 0,
        "max" : 50,
        "log" : True,
        },
    "Jets.dRSVJet": {
        "title" : "dR between SV and jet",
        "nbins" : 51,
        "min" : 0,
        "max" : 1,
        "log" : True,
        },
    "Jets.flightDist2d": {
        "title" : "Flight distance vertex [0] 2D",
        "nbins" : 51,
        "min" : 0,
        "max" : 50,
        "log" : True,
        },
    "Jets.flightDist2dsig": {
        "title" : "Significance of flight distance vertex [0] 2D",
        "nbins" : 31,
        "min" : 0,
        "max" : 30,
        "log" : False,
        },
    "Jets.flightDist3d": {
        "title" : "Flight distance vertex [0] 3D",
        "nbins" : 61,
        "min" : 0,
        "max" : 60,
        "log" : False,
        },
    "Jets.flightDist3dsig": {
        "title" : "Significance of flight distance vertex [0] 2D",
        "nbins" : 81,
        "min" : 0,
        "max" : 80,
        "log" : False,
        },
    "Jets.SV_x": {
        "title" : "vertex [0] x",
        "nbins" : 81,
        "min" : -40,
        "max" : 40,
        "log" : False,
        },
    "Jets.SV_y": {
        "title" : "vertex [0] y",
        "nbins" : 81,
        "min" : -40,"max" : 40,
        "log" : False,
        },
    "Jets.SV_z": {
        "title" : "vertex [0] z",
        "nbins" : 81,
        "min" : -40,
        "max" : 40,
        "log" : False,
        },
    "Jets.nTracksSV": {
        "title" : "Number of selected tracks per vertex [0]",
        "nbins" : 21,
        "min" : 0,
        "max" : 20,
        "log" : False,
        },
    "Jets.SV_mass": {
        "title" : "Mass of vertex [0] (GeV)",
        "nbins" : 31,
        "min" : 0,
        "max" : 30,
        "log" : False,
        },
    

    "Jets.ptMin": {
      "title" : "6 jets min p_{T} (GeV)",
      "nbins" : 40,#40
      "min" : 0,
      "max" : 400,
      "log" : True,
    },
    "Jets.CSVmax": {
      "title" : "6 jets max CSV",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "maxCSV6Jets": {
      "title" : "6 jets max CSV",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "maxSecondCSV6Jets": {
      "title" : "6 jets second max CSV",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "nCSVgr0p84": {
      "title" : "Number of jets with CSV > 0.84",
      "nbins" : 10,
      "min" : -0.5,
      "max" : 9.5,
      "log" : True,
    },
    

    #1 jet at a time
    "Jets.Jets[[N]].pt": {
      "title" : "jet [[N]] p_{T} (GeV)",
      "nbins" : 40,#40
      "min" : 0,
      "max" : 400,
      "log" : True,
    },
    "Jets.Jets[[N]].energy": {
      "title" : "jet [[N]] energy (GeV)",
      "nbins" : 40,#40
      "min" : 0,
      "max" : 400,
      "log" : True,
    },
    "TripleJet50TriggerObjects.TripleJet50TriggerObjects[[N]].pt": {
      "title" : "trigger object firing hltTripleJet50 [[N]] p_{T} (GeV)",
      "nbins" : 40,#40
      "min" : 0,
      "max" : 400,
      "log" : True,
    },

    "Jets.Jets[[N]].eta": {
      "title" : "jet [[N]] #eta",
      "nbins" : 50,
      "min" : -5.2,#-3,
      "max" : 5.2,#3,
      "log" : True,
    },
    "Jets.Jets[[N]].phi": {
      "title" : "jet [[N]] #varphi",
      "nbins" : 60,
      "min" : -3.2,
      "max" : 3.2,
      "log" : True,
    },
    "Jets.Jets[[N]].mass": {
      "title" : "jet [[N]] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 100,
      "log" : True,
    },
    "Jets.Jets[[N]].CSV": {
      "title" : "jet [[N]] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].pfXWP0p01": {
      "title" : "jet [[N]] pfXWP0p01",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].pfXWP1": {
      "title" : "jet [[N]] pfXWP1",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].pfXWP1000": {
      "title" : "jet [[N]] pfXWP1000",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },

    "Jets.Jets[[N]].isMatchedToMatchedCHSJet": {
      "title" : "jet [[N]] matched to signal jet n...",
      "nbins" : 6,
      "min" : -1.5,
      "max" : 4.5,
      "log" : False,
    },
    "Jets.Jets[[N]].alphaMax": {
      "title" : "jet [[N]] #alpha_{max}",
      "nbins" : 50,
      "min" : 0.,
      "max" : 1.,
      "log" : True,
    },
    "Jets.Jets[[N]].sigIP2DMedian": {
      "title" : "jet [[N]] sigIP2DMedian",
      "nbins" : 50,
      "min" : -5,#-50,
      "max" : 7,#50,
      "log" : True,
    },

    "-log(abs(Jets.Jets[[N]].sigIP2DMedian))": {
      "title" : "jet [[N]] sigIP2DMedian",
      "nbins" : 100,
      "min" : -50,
      "max" : 50,
      "log" : True,
    },


    "Jets.Jets[[N]].theta2DMedian": {
      "title" : "jet [[N]] theta2DMedian",
      "nbins" : 100,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].flavour": {
      "title" : "jet [[N]] flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "Jets.Jets[[N]].FracCal": {
      "title" : "jet [[N]] ECAL energy/HCAL energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },
    "Jets.Jets[[N]].hcalE": {
      "title" : "jet [[N]] HCAL energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 500,
      "log" : True,
    },
    "Jets.Jets[[N]].ecalE": {
      "title" : "jet [[N]] ECAL energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },
    "Jets.Jets[[N]].cHadE": {
      "title" : "jet [[N]] charged hadron energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },
    "Jets.Jets[[N]].nHadE": {
      "title" : "jet [[N]] neutral hadron energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },
    "Jets.Jets[[N]].cHadEFrac": {
      "title" : "jet [[N]] charged hadron energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].nHadEFrac": {
      "title" : "jet [[N]] neutral hadron energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.nHadEFrac": {
      "title" : "all jets neutral hadron energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },

    "Jets.Jets[[N]].nEmE": {
      "title" : "jet [[N]] neutral ECAL energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },
    "Jets.Jets[[N]].nEmEFrac": {
      "title" : "jet [[N]] neutral ECAL energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].cEmE": {
      "title" : "jet [[N]] charged ECAL energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 20,
      "log" : True,
    },
    "Jets.Jets[[N]].cEmEFrac": {
      "title" : "jet [[N]] charged ECAL energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "Jets.Jets[[N]].cmuE": {
      "title" : "jet [[N]] charged #mu energy",
      "nbins" : 20,
      "min" : 0,
      "max" : 20,
      "log" : True,
    },
    "Jets.Jets[[N]].cmuEFrac": {
      "title" : "jet [[N]] charged #mu energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "Jets.Jets[[N]].muE": {
      "title" : "jet [[N]] #mu energy",
      "nbins" : 20,
      "min" : 0,
      "max" : 20,
      "log" : True,
    },
    "Jets.Jets[[N]].muEFrac": {
      "title" : "jet [[N]] #mu energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "Jets.Jets[[N]].eleE": {
      "title" : "jet [[N]] electron energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : True,
    },
    "Jets.Jets[[N]].eleEFrac": {
      "title" : "jet [[N]] electron energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 0.1,
      "log" : True,
    },
    "Jets.Jets[[N]].eleMulti": {
      "title" : "jet [[N]] electron multiplicity",
      "nbins" : 20,
      "min" : 0,
      "max" : 20,
      "log" : True,
    },
    "Jets.Jets[[N]].photonE": {
      "title" : "jet [[N]] photon energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },
    "Jets.Jets[[N]].photonEFrac": {
      "title" : "jet [[N]] photon energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "Jets.Jets[[N]].photonMulti": {
      "title" : "jet [[N]] photon multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : True,
    },
    "Jets.Jets[[N]].cHadMulti": {
      "title" : "jet [[N]] charged hadron multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : True,
    },
    "Jets.Jets[[N]].nHadMulti": {
      "title" : "jet [[N]] neutral hadron multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : True,
    },
    "Jets.Jets[[N]].cMulti": {
      "title" : "jet [[N]] charged multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : True,
    },
    "Jets.Jets[[N]].nMulti": {
      "title" : "jet [[N]] neutral multiplicity",
      "nbins" : 50,
      "min" : 0,
      "max" : 50,
      "log" : True,
    },
    "Jets.Jets[[N]].npr": {
      "title" : "jet [[N]] number of components",
      "nbins" : 100,
      "min" : 0,
      "max" : 100,
      "log" : True,
    },

    "Jets.Jets[[N]].isCaloTag": {
      "title" : "jet [[N]] calo tag",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : False,
    },
#####################
# jet substructure

    "Jets.Jets[[N]].tau1": {
      "title" : "jet [[N]] #tau_{1}",
      "nbins" : 50,
      "min" : 0.,
      "max" : 1.,
      "log" : False,
    },

    "Jets.Jets[[N]].tau2": {
      "title" : "jet [[N]] #tau_{2}",
      "nbins" : 50,
      "min" : 0.,
      "max" : 1.,
      "log" : False,
    },

    "Jets.Jets[[N]].tau21": {
      "title" : "jet [[N]] #tau_{2}/#tau_{1}",
      "nbins" : 50,
      "min" : 0.,
      "max" : 1.,
      "log" : False,
    },



#####################

    "Jets.Jets[[N]].nConstituents": {
      "title" : "jet [[N]] number of jet constituents",
      "nbins" : 100,
      "min" : -0.5,
      "max" : 99.5,
      "log" : True,
    },

    "Jets.Jets[[N]].nTrackConstituents": {
      #"title" : "jet [[N]] number of jet constituents with tracks",
      "title" : "Leading jet: n. of constituents with tracks",
      "nbins" : 50+40,
      "min" : -0.5,
      "max" : 49.5+40,
      "log" : True,
    },

    "(Jets.Jets[[N]].nTrackConstituents)/(Jets.Jets[[N]].nConstituents)": {
      "title" : "percentage of jet [[N]] constituents with tracks",
      "nbins" : 50,
      "min" : 0.,
      "max" : 1.,
      "log" : True,
    },


    "Jets.nTrackConstituents": {
      "title" : "number of jet constituents with tracks",
      "nbins" : 50,
      "min" : -0.5,
      "max" : 49.5,
      "log" : True,
    },
    "Jets.nConstituents": {
      "title" : "number of jet constituents",
      "nbins" : 50,
      "min" : -0.5,
      "max" : 49.5,
      "log" : True,
    },
    "Jets.FracCal": {
      "title" : "jets ECAL energy/HCAL energy",
      "nbins" : 50,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },
    "Jets.nTracks3PixelHits": {
      "title" : "jets number of tracks with 3 pixel hits",
      #"title" : "Leading jet: n. of tracks with 3 pixel hits",
      "nbins" : 40,#+30,
      "min" : -0.5,
      "max" : 39.5,#+30,
      "log" : True,
    },


    "Jets.Jets[[N]].nTracks0PixelHits": {
      "title" : "jet [[N]] number of tracks with 0 pixel hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks1PixelHits": {
      "title" : "jet [[N]] number of tracks with 1 pixel hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks2PixelHits": {
      "title" : "jet [[N]] number of tracks with 2 pixel hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks3PixelHits": {
      #"title" : "jet [[N]] number of tracks with 3 pixel hits",
      "title" : "Leading jet: n. of tracks with 3 pixel hits",
      "nbins" : 40+10,
      "min" : -0.5,
      "max" : 39.5+10,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks4PixelHits": {
      "title" : "jet [[N]] number of tracks with 4 pixel hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks5PixelHits": {
      "title" : "jet [[N]] number of tracks with 5 pixel hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracksLarger5PixelHits": {
      "title" : "jet [[N]] number of tracks with more than 5 pixel hits",
      "nbins" : 10,
      "min" : -0.5,
      "max" : 9.5,
      "log" : True,
    },

    "Jets.Jets[[N]].nTracks0LostInnerHits": {
      "title" : "jet [[N]] number of tracks with 0 lost inner hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks1LostInnerHits": {
      "title" : "jet [[N]] number of tracks with 1 lost inner hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracks2LostInnerHits": {
      "title" : "jet [[N]] number of tracks with 2 lost inner hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.Jets[[N]].nTracksLarger2LostInnerHits": {
      "title" : "jet [[N]] number of tracks with more than 2 lost inner hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },
    "Jets.nTracksLarger2LostInnerHits": {
      "title" : "number of tracks in all jets with more than 2 lost inner hits",
      "nbins" : 40,
      "min" : -0.5,
      "max" : 39.5,
      "log" : True,
    },


#######################
#Higgs masses
    "HDiCHS": {
      "title" : "dijet mass CHS (GeV)",
      "nbins" : 20,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HTriCHS": {
      "title" : "trijet mass CHS (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HQuadCHS": {
      "title" : "quadjet mass CHS (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HDiCHSMatched": {
      "title" : "Matched dijet mass CHS (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HTriCHSMatched": {
      "title" : "Matched trijet mass CHS (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HQuadCHSMatched": {
      "title" : "Matched quadjet mass CHS (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },

    "HDiCalo": {
      "title" : "dijet mass Calo (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HTriCalo": {
      "title" : "trijet mass Calo (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HQuadCalo": {
      "title" : "quadjet mass Calo (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HDiCaloMatched": {
      "title" : "Matched dijet mass Calo (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HTriCaloMatched": {
      "title" : "Matched trijet mass Calo (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },
    "HQuadCaloMatched": {
      "title" : "Matched quadjet mass Calo (GeV)",
      "nbins" : 100,
      "min" : 0.5,
      "max" : 500.5,
      "log" : True,
    },

    "CaloJets.emEnergyFraction": {
      "title" : "calo jet ECAL energy fraction",
      "nbins" : 100,
      "min" : 0.,
      "max" : 1.,
      "log" : True,
    },
    "CaloJets.energyFractionHadronic": {
      "title" : "calo jet HCAL energy fraction",
      "nbins" : 100,
      "min" : 0.,
      "max" : 1.,
      "log" : True,
    },
#######################




    # Trigger variables
    "VBFPairJets.VBFPairJets[[N]].pt": {
      "title" : "VBF pair jet [[N]] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },
    "DisplacedJets.DisplacedJets[[N]].nHadEFrac": {
      "title" : "displaced jet [[N]] neutral hadron energy fraction",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "DisplacedJets.DisplacedJets[[N]].pt": {
      "title" : "displaced jet [[N]] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },
    "DisplacedJets.DisplacedJets[[N]].nTrackConstituents": {
      "title" : "Number of constituents with tracks per displaced jet [[N]]",
      "nbins" : 50,
      "min" : 0,
      "max" : 49,
      "log" : False,
    },

    # b-tagging variables
    "Jets.Jets[[N]].nSV": {
        "title" : "Number of SV per jet",
        "nbins" : 10,
        "min" : -0.5,
        "max" : 9.5,
        "log" : False,
    },
    "Jets.Jets[[N]].nSVCand": {
        "title" : "Number of SV candidates per jet [[N]]",
        "nbins" : 10,
        "min" : 0,
        "max" : 9,
        "log" : False,
    },
    "Jets.Jets[[N]].nVertexTracks": {
        "title" : "Number of tracks per vertex",
        "nbins" : 21,
        "min" : 0,"max" : 20,
        "log" : False,
    },
    "Jets.Jets[[N]].nSelectedTracks": {
        "title" : "Number of selected tracks per jet [[N]]",
        "nbins" : 51,
        "min" : 0,
        "max" : 50,
        "log" : False,
    },
    "Jets.Jets[[N]].dRSVJet": {
        "title" : "dR between SV and jet",
        "nbins" : 51,
        "min" : 0,
        "max" : 1,
        "log" : False,
    },
    "Jets.Jets[[N]].flightDist2d": {
        "title" : "Flight distance vertex [[N]] 2D (cm)",
        "nbins" : 150,
        "min" : 0,
        "max" : 10,
        "log" : False,
    },
    "Jets.Jets[[N]].flightDist3d": {
        "title" : "Flight distance vertex [[N]] 3D (cm)",
        "nbins" : 150,
        "min" : 0,
        "max" : 10,
        "log" : False,
    },
    "Jets.Jets[[N]].nTracksSV": {
        "title" : "Number of selected tracks per vertex [[N]]",
        "nbins" : 21,
        "min" : 0,
        "max" : 20,
        "log" : False,
    },
    "Jets.Jets[[N]].SV_mass": {
        "title" : "Mass of vertex [[N]] (GeV)",
        "nbins" : 31,
        "min" : 0,
        "max" : 30,
        "log" : False,
    },

    #VBF Pair jets
    "VBFPairJets.VBFPairJets[[N]].pt": {
      "title" : "VBF pair jet [[N]] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },


    # JetConstits vector
    "JetConstits.JetConstits.pt": {
      "title" : "jet constituents p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },
    "JetConstits.JetConstits[[N]].pt": {
      "title" : "jet constituent [[N]] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 200,
      "log" : True,
    },


    # MatchedCHSJets
    "MatchedCHSJet[N].pt": {
      "title" : "jet [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },
    "MatchedCHSJet[N].eta": {
      "title" : "jet [N] #eta",
      "nbins" : 30,
      "min" : -3,
      "max" : 3,
      "log" : False,
    },
    "MatchedCHSJet[N].phi": {
      "title" : "jet [N] #varphi",
      "nbins" : 60,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },
    "MatchedCHSJet[N].mass": {
      "title" : "jet [N] mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 150,
      "log" : False,
    },
    "MatchedCHSJet[N].CSV": {
      "title" : "jet [N] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "MatchedCHSJet[N].flavour": {
      "title" : "jet [N] flavour",
      "nbins" : 25,
      "min" : -0.5,
      "max" : 24.5,
      "log" : False,
    },
    "MatchedCHSJet[N].chf": {
      "title" : "jet [N] charged hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "MatchedCHSJet[N].nhf": {
      "title" : "jet [N] neutral hadron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "MatchedCHSJet[N].phf": {
      "title" : "jet [N] photon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "MatchedCHSJet[N].elf": {
      "title" : "jet [N] electron fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "MatchedCHSJet[N].muf": {
      "title" : "jet [N] muon fraction",
      "nbins" : 20,
      "min" : 0,
      "max" : 1,
      "log" : False,
    },
    "MatchedCHSJet[N].chm": {
      "title" : "jet [N] charged multiplicity",
      "nbins" : 20,
      "min" : 0,
      "max" : 50,
      "log" : False,
    },
    
    # Z Control Region
    "Z.mass": {
      "title" : "Z->ll mass (GeV)",
      "nbins" : 40,
      "min" : 69.5,
      "max" : 109.5,
      "log" : True,
    },
    "Z.pt": {
      "title" : "Z p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },

    # VBFPair
    "VBFPair.mass": {
      "title" : "VBF pair mass (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 2000,
      "log" : True,
    },
    "VBFPair.dEta": {
      "title" : "VBF pair #Delta #eta",
      "nbins" : 50,
      "min" : 0,
      "max" : 10,
      "log" : True,
    },

    "Lepton[N].pt": {
      "title" : "lepton[N] p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },

    "Muon1_pt": {
      "title" : "#mu_{1} p_{T} (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "Muon1_phi": {
      "title" : "#mu_{1} #varphi",
      "nbins" : 60,
      "min" : -3.2,#15,
      "max" : 3.2,#15,
      "log" : True,
    },
    "Muon1_eta": {
      "title" : "#mu_{1} #eta",
      "nbins" : 50,
      "min" : -2.5,#-3,
      "max" : 2.5,#3,
      "log" : True,
    },

    "isZtoEE": {
      "title" : "is Z->ee",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : True,
    },

    "isZtoMM": {
      "title" : "is Z->#mu #mu",
      "nbins" : 2,
      "min" : -0.5,
      "max" : 1.5,
      "log" : True,
    },


    # Fatjets
    "FatJets.CSV": {
      "title" : "all fat jets CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.CSV1": {
      "title" : "all fat jets subjet 1 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.CSV2": {
      "title" : "all fat jets subjet 2 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.CMVA1": {
      "title" : "all fat jets subjet 1 CMVA",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.CMVA2": {
      "title" : "all fat jets subjet 2 CMVA",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.pfBoostedDoubleSVAK8": {
      "title" : "all jets boosted double SV discriminator",
      "nbins" : 30,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    # .....
    "FatJets.CHSsoftdropMass": {
      "title" : "AK8 jet CHS soft drop mass  (GeV)",
      "nbins" : 90,
      "min" : 0,
      "max" : 150,
      "log" : True,
    },
    "FatJets.dR": {
      "title" : "AK8 jets dR ",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.muMulti": {
      "title" : "AK8 jets muon multiplicity ",
      "nbins" : 15,
      "min" : 0,
      "max" : 15,
      "log" : True,
    },
    "FatJets.chsTau21": {
      "title" : "AK8 jets #tau_{2}/#tau_{1} ",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },

    "FatJets.FatJets[[N]].pt": {
      "title" : "AK8 jet [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 200,
      "max" : 1000,
      "log" : True,
    },
    "FatJets.FatJets[[N]].nMatchedGenBquarks": {
      "title" : "AK8 jet [N] number of matched b quarks",
      "nbins" : 5,
      "min" : -0.5,
      "max" : 4.5,
      "log" : True,
    },
    "FatJets.FatJets[[N]].CSV": {
      "title" : "all fat jet [N] CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].CSV1": {
      "title" : "all fat jet [N] subjet 1 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].CSV2": {
      "title" : "all fat jet [N] subjet 2 CSV",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].CMVA1": {
      "title" : "all fat jet [N] subjet 1 CMVA",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].CMVA2": {
      "title" : "all fat jet [N] subjet 2 CMVA",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].pfBoostedDoubleSVAK8": {
      "title" : "fat jet [N] boosted double SV discriminator",
      "nbins" : 30,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    # .....
    "FatJets.FatJets[[N]].CHSsoftdropMass": {
      "title" : "AK8 jet [N] CHS soft drop mass  (GeV)",
      "nbins" : 90,
      "min" : 0,
      "max" : 150,
      "log" : True,
    },
    "FatJets.FatJets[[N]].dR": {
      "title" : "AK8 jet [N] dR ",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].muMulti": {
      "title" : "AK8 jet [N] muon multiplicity ",
      "nbins" : 15,
      "min" : 0,
      "max" : 15,
      "log" : True,
    },
    "FatJets.FatJets[[N]].chsTau21": {
      "title" : "AK8 jet [N] #tau_{2}/#tau_{1} ",
      "nbins" : 50,
      "min" : 0,
      "max" : 1,
      "log" : True,
    },
    "FatJets.FatJets[[N]].nSV1": {
        "title" : "Number of SV of subjet 1 of fat jet [N]",
        "nbins" : 10,
        "min" : -0.5,
        "max" : 9.5,
        "log" : True,
    },
    "FatJets.FatJets[[N]].nVertexTracks1": {
        "title" : "Number of tracks per vertex of subjet 1 in fat jet [N]",
        "nbins" : 21,
        "min" : 0,
        "max" : 20,
        "log" : True,
    },

    "FatJets.FatJets[[N]].nSV2": {
        "title" : "Number of SV of subjet 2 of fat jet [N]",
        "nbins" : 10,
        "min" : -0.5,
        "max" : 9.5,
        "log" : True,
    },
    "FatJets.FatJets[[N]].nVertexTracks2": {
        "title" : "Number of tracks per vertex of subjet 2 in fat jet [N]",
        "nbins" : 21,
        "min" : 0,
        "max" : 20,
        "log" : True,
    },



    # Vertices
    # .....
    "BTagVertices.chi2": {
       "title" : "Chi^2 of vertex",
       "nbins" : 100,
        "min" : 0,
        "max" : 100,
        "log" : True, 
},
    "BTagVertices.ndof": {
       "title" : "Number degrees of freedom of vertex",
       "nbins" : 20,
        "min" : 0,
        "max" : 20,
        "log" : True, 
},    "BTagVertices.mass": {
       "title" : "Mass of vertex",
       "nbins" : 50,
        "min" : 0,
        "max" : 10,
        "log" : True,
},    "BTagVertices.pt": {
       "title" : "p_{T} of vertex",
       "nbins" : 100,
        "min" : 0,
        "max" : 100,
        "log" : True,
},    "BTagVertices.flightDist2D": {
       "title" : "Flight distance 2D of vertex (cm)",
       "nbins" : 30,
        "min" : 0,
        "max" : 3,
        "log" : True,
},    "BTagVertices.flightDist2DErr": {
       "title" : "Error flight distance 2D of vertex (cm)",
       "nbins" : 20,
        "min" : 0,
        "max" : 10,
        "log" : True,
},    "BTagVertices.flightDist2DSig": {
       "title" : "Significance flight distance 2D of vertex",
       "nbins" : 30,
        "min" : 0,
        "max" : 150,
        "log" : True,
},    "BTagVertices.flightDist3D": {
       "title" : "Flight distance 3D of vertex (cm)",
       "nbins" : 30,
        "min" : 0,
        "max" : 3,
        "log" : True,
},    "BTagVertices.flightDist3DErr": {
       "title" : "Error flight distance 3D of vertex (cm)",
       "nbins" : 20,
        "min" : 0,
        "max" : 10,
        "log" : True,
},    "BTagVertices.flightDist3DSig": {
       "title" : "Significance flight distance 3D of vertex",
       "nbins" : 30,
        "min" : 0,
        "max" : 150,
        "log" : True,
},
    "BTagVertices.BTagVertices[[N]].nVertexTracks": {
        "title" : "Number of tracks per vertex",
        "nbins" : 21,
        "min" : 0,
        "max" : 20,
        "log" : False,
    },


    "BTagVertices.BTagVertices[[N]].chi2": {
       "title" : "Chi^2 of vertex [N]",
       "nbins" : 100,
        "min" : 0,
        "max" : 100,
        "log" : True, 
},





    # Tracks
    # .....

    # Leptons
    "nMuons": {
      "title" : "number of loose muons",
      "nbins" : 6,
      "min" : -0.5,
      "max" : 5.5,
      "log" : True,
    },
    "nTightMuons": {
      "title" : "number of tight muons",
      "nbins" : 6,
      "min" : -0.5,
      "max" : 5.5,
      "log" : True,
    },
    "nElectrons": {
      "title" : "number of veto electrons",
      "nbins" : 6,
      "min" : -0.5,
      "max" : 5.5,
      "log" : True,
    },
    "nTaus": {
      "title" : "number of loose taus",
      "nbins" : 6,
      "min" : -0.5,
      "max" : 5.5,
      "log" : True,
    },
    "nPhotons": {
      "title" : "number of loose photons",
      "nbins" : 6,
      "min" : -0.5,
      "max" : 5.5,
      "log" : True,
    },


    # MET
    "MEt.pt": {
      "title" : "E_{T}^{miss} (GeV)",
      "nbins" : 50,
      "min" : 200,
      "max" : 1200,
      "log" : True,
    },
    "MEt.sign": {
      "title" : "#slash{E}_{T} significance (GeV)",
      "nbins" : 50,
      "min" : 0,
      "max" : 1000,
      "log" : True,
    },
    "MEt.phi": {
      "title" : "#slash{E}_{T} #varphi",
      "nbins" : 50,
      "min" : -3.15,
      "max" : 3.15,
      "log" : False,
    },

    # GenBquarks
    "GenBquark[N].pt": {
      "title" : "gen b-quark [N] p_{T} (GeV)",
      "nbins" : 40,
      "min" : 0,
      "max" : 800,
      "log" : True,
    },
    "GenBquark[N].radius": {
      "title" : "gen b-quark [N] radius (mm)",
      "bins" : [0,0.0001,0.001,0.01,0.1,0.5,1,2,5,10,25,50,100,200,300,500,700,1000,2000,3000,5000,7000,10000,20000,50000],
      "nbins" : 100,
      "min" : 0.000001,
      "max" : 100000,
      "log" : True,
      "logx" : True,
    },
}


for n, v in var_template.iteritems():
    if '[N]' in n:
        for i in range(0, 5):
            ni = n.replace('[N]', "%d" % i)
            variable[ni] = v.copy()
            variable[ni]['title'] = variable[ni]['title'].replace('[N]', "%d" % i)
    else:
        variable[n] = v

# Custom settings
#variable['Jets.Jets[2].pt']['max'] = 500
#variable['Jets.Jets[3].pt']['max'] = 400
#variable['CHSJet2.pt']['max'] = 400
#variable['CHSJet3.pt']['max'] = 200
#variable['CHSJet4.pt']['max'] = 200



