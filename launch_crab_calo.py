#Here: standard crab config file

import CRABClient
from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
import sys
from multiprocessing import Process

#First: set all the parameters
#Then call a new config at every loop

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config, dryrun = False):
        try:
            crabCommand('submit', config = config, dryrun = dryrun)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    # Selection of samples via python lists
    import os

    list_of_samples = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","WJetsToLNu_Pt","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","TTbarGenMET","TTJets","QCD","signal_VBF","signal_ggH","all","data_obs","MET","SingleMuon","SingleElectron","SinglePhoton","EGamma","JetHT","MuonEG","ZJetsToNuNu", "DYJets", "WJets", "signal_ZH", "SUSY", "SUSY_HH", "SUSY_HZ", "SUSY_ZZ", "TTbarSemiLep","TTbarNu","ggHeavyHiggs","WJetsToLNu_HT", "VBFH_MH-125_2016","VBFH_MH-125_2017", "VBFH_MH-125_2018","ggH_MH-125_2016","ggH_MH-125_2017", "ggH_MH-125_2018", "gluinoGMSB", "Others","data_BTagCSV", "WH_MH-125_2016","splitSUSY","JetJet","RPVstopBL","HighMET","Cosmics","ggH","VBFH"]#,"data_obs"
    print "Possible subgroups of samples:"
    for a in list_of_samples:
        print a
    print "---------------"

    ########parser#######
    import optparse
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-a", "--crabaction", action="store", type="string", dest="crabaction", default="test")
    parser.add_option("-l", "--lists", action="store", type="string", dest="lists", default="v1_SUSY_calo_AOD_2017")
    parser.add_option("-g", "--groupofsamples", action="store", type="string", dest="groupofsamples", default="")
    parser.add_option("-c", "--calo", action="store_true", dest="calo", default=False)
    parser.add_option("-d", "--datatier", action="store", type="string", dest="datatier", default="AOD")
    parser.add_option("-r", "--runera", action="store", type="string", dest="runera", default="2017")
    parser.add_option("-m", "--mode", action="store", type="string", dest="mode", default="")
    parser.add_option("-M", "--model", action="store", type="string", dest="model", default="SUSY")
    parser.add_option("-C", "--centralproduction", action="store_true", dest="centralProd", default=False)
    (options, args) = parser.parse_args()


    ####################
    #crabConfig = ''
    if options.calo:
       isCalo=True
    else:
       isCalo=False

    isRPV = False
    isJetJet = False
    isSplit = False
    if options.mode=="VBF":
        isVBF = True
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        #isSUSY = False
        isRPV = False
    elif options.mode=="ggH":
        isVBF = False
        isggH = True
        isTwinHiggs = True
        isHeavyHiggs = False
        #isSUSY = False
        isRPV = False
    if options.model=="TwinHiggs":
        isTwinHiggs = True
        isHeavyHiggs = False
        #isSUSY = False
        isRPV = False
    elif options.model=="HeavyHiggs":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        #isSUSY = False
        isRPV = False
    elif options.model=="SUSY":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        #isSUSY = True
        isRPV = False
    elif options.model=="gluinoGMSB":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        #isSUSY = True
        isRPV = False
    elif options.model=="RPV":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        #isSUSY = False
        isRPV = True

    #DATA TIER
    if options.datatier=="MINIAOD":
        isMINIAOD = True
        isAOD     = False
    elif options.datatier=="AOD":
        isMINIAOD = False
        isAOD     = True
    else:
        print "Wrong data tier! Aborting . . ."
        exit()

    #DATA ERA
    if options.runera=="2016":
        is2016 = True
        is2017 = False
        is2018 = False
    elif options.runera=="2017":
        is2016 = False
        is2017 = True
        is2018 = False
    elif options.runera=="2018":
        is2016 = False
        is2017 = False
        is2018 = True
    else:
        print "Data era not recognized! Aborting . . ."
        exit()

    if options.centralProd:
        isCentralProd=True
    else:
        isCentralProd=False

    isGenProd = False


    folder = ''
    pset = ''
    workarea = ''

    if options.lists == "v6_calo_AOD_2018_gen_TwinHiggs":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2018_gen_TwinHiggs_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 2500#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2017_gen_TwinHiggs":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2017_gen_TwinHiggs_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 2500#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2016_gen_TwinHiggs":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2016_gen_TwinHiggs_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 2500#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2018_gen_SUSY_HZ":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2018_gen_SUSY_HZ_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = True#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2017_gen_SUSY_HZ":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2017_gen_SUSY_HZ_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = True#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2016_gen_SUSY_HZ":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2016_gen_SUSY_HZ_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = True#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True


    elif options.lists == "v6_calo_AOD_2018_gen_SUSY_ZZ":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2018_gen_SUSY_ZZ_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True


    elif options.lists == "v7_calo_AOD_2018_reinterpretation":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        #folder = "v7_calo_AOD_2018_reinterpretation_25July2022"#CHANGE here your crab folder name
        #folder = "v7_calo_AOD_2018_reinterpretation_04August2022"#CHANGE here your crab folder name
        #november accident: ntuples lost in tier 2
        folder = "v7_calo_AOD_2018_reinterpretation_25November2022"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 40#25#20#10
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False
        isGenProd = False

    elif options.lists == "v7_calo_AOD_2017_reinterpretation":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        #folder = "v7_calo_AOD_2017_reinterpretation_25July2022"#CHANGE here your crab folder name
        #folder = "v7_calo_AOD_2017_reinterpretation_04August2022"#CHANGE here your crab folder name
        #november accident: ntuples lost in tier 2
        folder = "v7_calo_AOD_2017_reinterpretation_25November2022"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 20#10
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = False


    elif options.lists == "v7_calo_AOD_2016_reinterpretation":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        #folder = "v7_calo_AOD_2016_reinterpretation_25July2022"#CHANGE here your crab folder name
        #folder = "v7_calo_AOD_2016_reinterpretation_04August2022"#CHANGE here your crab folder name
        #november accident: ntuples lost in tier 2
        folder = "v7_calo_AOD_2016_reinterpretation_25November2022"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 20#10
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = False




    elif options.lists == "v6_calo_AOD_2017_gen_SUSY_ZZ":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2017_gen_SUSY_ZZ_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2016_gen_SUSY_ZZ":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "GenNtuplizerCalo.py"
        folder = "v6_calo_AOD_2016_gen_SUSY_ZZ_08December2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 4000#15900 #more memory 
        inputFiles = ['data_gen']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 50
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

        isGenProd = True

    elif options.lists == "v6_calo_AOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2018_07October2021_HEM"#CHANGE here your crab folder name
        #folder = "v6_calo_AOD_2018_15November2021_slimmedJets_HEM"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 10
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v6_calo_AOD_2018_split":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2018_07October2021_HEM"#CHANGE here your crab folder name
        #folder = "v6_calo_AOD_2018_15November2021_slimmedJets_HEM"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 10
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = True

    elif options.lists == "v6_calo_AOD_2017":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2017_07October2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        ignoreLocality = False
        whitelist   = False
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        ##isCentralProd = True if ("SMS-TChiHZ_ZToQQ" in options.groupofsamples) else False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v6_calo_AOD_2017_split":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2017_07October2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        ignoreLocality = False
        whitelist   = False
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        ##isCentralProd = True if ("SMS-TChiHZ_ZToQQ" in options.groupofsamples) else False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = True

    elif options.lists == "v5_calo_AOD_2016":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v5_calo_AOD_2016_31December2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        inputFiles = ['dataAOD']
        maxMemoryMB = 3000#4000#15900 #more memory 
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 100#10#20
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False


    elif options.lists == "v6_calo_AOD_2016":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2016_07October2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        inputFiles = ['dataAOD']
        maxMemoryMB = 3000#4000#15900 #more memory 
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = True#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False


    elif options.lists == "v6_calo_AOD_2016_split":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2016_07October2021"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        inputFiles = ['dataAOD']
        maxMemoryMB = 3000#4000#15900 #more memory 
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = False#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = True

    #JER Up
    elif options.lists == "v6_calo_AOD_2018_JERUp":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2018_07October2021_HEM_JERUp"#CHANGE here your crab folder name
        #folder = "v6_calo_AOD_2018_15November2021_slimmedJets_HEM"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 15
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = True#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v6_calo_AOD_2017_JERUp":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2017_07October2021_JERUp"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        ignoreLocality = False
        whitelist   = False
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        ##isCentralProd = True if ("SMS-TChiHZ_ZToQQ" in options.groupofsamples) else False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = True#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v6_calo_AOD_2016_JERUp":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2016_07October2021_JERUp"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        inputFiles = ['dataAOD']
        maxMemoryMB = 3000#4000#15900 #more memory 
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = True#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False
    #JER Down
    elif options.lists == "v6_calo_AOD_2018_JERDown":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2018_07October2021_HEM_JERDown"#CHANGE here your crab folder name
        #folder = "v6_calo_AOD_2018_15November2021_slimmedJets_HEM"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        #numCores = 2
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 15
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = True#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v6_calo_AOD_2017_JERDown":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2017_07October2021_JERDown"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        maxMemoryMB = 3000#4000#15900 #more memory 
        inputFiles = ['dataAOD']
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        ignoreLocality = False
        whitelist   = False
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        ##isCentralProd = True if ("SMS-TChiHZ_ZToQQ" in options.groupofsamples) else False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = True#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v6_calo_AOD_2016_JERDown":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v6_calo_AOD_2016_07October2021_JERDown"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        inputFiles = ['dataAOD']
        maxMemoryMB = 3000#4000#15900 #more memory 
        ignoreLocality = False
        whitelist   = False
        splitting = 'LumiBased'
        unitsPerJob = 15#10#20
        is2016 = True
        is2017 = False#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = False
        isSUSYHH = True#True#False#!!!
        isSUSYHZ = False#True#False#!!!
        isSUSYZZ = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    else:
        print "No list indicated, aborting!"
        exit()

    if options.crabaction == "dryrun":
        splitting = 'LumiBased'

    selected_requests = {}
    selected_lumiMasks = {}
    if options.groupofsamples not in list_of_samples:
        print "Invalid subgroup of samples, aborting!"
        exit()

    for b, k in enumerate(requests.keys()):
        if options.groupofsamples=="signal_VBF":
            if "VBFH_HToSSTobb" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="signal_ggH":
            if "GluGluH_HToSSTobb" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="signal_ZH":
            if "ZH_HToSSTobb" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="ggH":
            if ("ggH_HToSSTo" in k):
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="VBFH":
            if ("VBFH_HToSSTo" in k):
                print k
                selected_requests[k] = requests[k]

        elif options.groupofsamples=="SUSY":
            if ("n3n2-n1-hbb-hbb" in k) or ("TChiH" in k):
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="SUSY_HH":
            if ("_HH" in k) and ("TChiH" in k):
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="SUSY_HZ":
            if ("_HZ" in k) and ("TChiH" in k):
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="SUSY_ZZ":
            if ("_ZZ" in k) and ("TChiH" in k):
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="ggHeavyHiggs":
            if "GluGluH2_H2ToSSTobb" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="gluinoGMSB":
            if "gluinoGMSB" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="splitSUSY":
            if "GluinoGluinoToNeutralinoNeutralinoTo2T2B2S" in k:
                print k
                selected_requests[k] = requests[k]
            if "splitSUSY" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="JetJet":
            if "XXTo4J" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="RPVstopBL":
            if "DisplacedSUSY_StopToBL" in k:
                print k
                selected_requests[k] = requests[k]
        elif "VBFH_MH-125_201" in options.groupofsamples:
            if "VBFH_HToSSTo4b" in k and "MS-" in k:
                print k
                selected_requests[k] = requests[k]
                if k in masks.keys():
                    selected_lumiMasks[k] = masks[k]
                    print "lumi mask:", masks[k]
                else:
                    print "no mask available"
                    exit()
        elif "WH_MH-125_2016" in options.groupofsamples:
            if "WminusH_HToSSTobbbb_" in k or "WplusH_HToSSTobbbb_" in k:
                print k
                selected_requests[k] = requests[k]
        elif "ggH_MH-125_201" in options.groupofsamples:
            if "ggH_HToSSTobbbb" in k and "MS-" in k:
                print k
                selected_requests[k] = requests[k]
                if k in masks.keys():
                    selected_lumiMasks[k] = masks[k]
                    print "lumi mask:", masks[k]
                else:
                    print "no mask available"
                    exit()
        elif options.groupofsamples=="all":
            print "All samples considered"
            selected_requests[k] = requests[k]
        else:
            if k in samples[options.groupofsamples]["files"]:
                print k
                selected_requests[k] = requests[k]

    if isCalo:
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"
        print "Performing analysis for CALO LIFETIMES!"
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"

    if isTracking:
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"
        print "Performing TRACKING LIFETIMES analysis!"
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"

    if isShort:
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"
        print "Performing analysis for SHORT LIFETIMES!"
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"

    if isControl:
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"
        print "Performing control region for SHORT LIFETIMES!"
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"

    if isGenProd:
        if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSYHH) + int(isSUSYHZ) + int(isSUSYZZ) >1):
            print "More than one theoretical model selected! Aborting...."
            exit()
    else:
        if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSY) + int(isSUSYHH) + int(isSUSYHZ) + int(isSUSYZZ) + int(isRPV) + int(isSplit) + int(isJetJet)>1):
            print "More than one theoretical model selected! Aborting...."
            exit()

    if isTwinHiggs:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing TWIN HIGGS analysis!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isHeavyHiggs:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing HEAVY HIGGS analysis!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isSUSYHZ or isSUSYHH or isSUSYZZ:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing SUSY analysis!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isRPV:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing RPV stop->bl analysis!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isSplit:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing split susy analysis!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isJetJet:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing XX->4J analysis!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isVBF:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing analysis for VBF!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"

    if isggH:
        print "\n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Performing analysis for ggH!"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n"


    for a, j in enumerate(selected_requests):
        print "#"*65
	print "Dataset: ", j
        # Here: determines every needed parameter as per config file
        isData = True if ('SingleMuon' in j or 'SingleElectron' in j or 'JetHT' in j or 'BTagCSV' in j or 'DisplacedJet' in j or 'METRun' in j or 'EGamma' in j or 'MuonEG' in j or 'SinglePhoton' in j or 'Cosmics' in j) else False
        print "isData?", isData
        isCosmics = True if 'Cosmics' in j else False
        isReHLT = False
        isReReco          = True if ('23Sep2016' in j) else False
        isReMiniAod       = True if ('03Feb2017' in j) else False
        #is2017            = True if ('RunIIFall17MiniAODv2' in j) else False
        isPromptReco      = True if ('PromptReco' in j) else False
        theRunBCD2016 = ['Run2016B','Run2016C','Run2016D']
        theRunEF2016  = ['Run2016E','Run2016F']
        theRunG2016   = ['Run2016G']
        theRunH2016   = ['Run2016H']

        theRun2018ABC = ['Run2018A','Run2018B','Run2018C']
        theRun2018D   = ['Run2018D']

        noLHEinfo = True if ('WW_TuneCUETP8M1_13TeV-pythia8' in j or 'WZ_TuneCUETP8M1_13TeV-pythia8' in j or 'ZZ_TuneCUETP8M1_13TeV-pythia8' in j or 'WW_TuneCP5_13TeV-pythia8' in j or 'WZ_TuneCP5_13TeV-pythia8' in j or 'ZZ_TuneCP5_13TeV-pythia8' in j) else False #check for PythiaLO samples
        isbbH = True if ('bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo' in j) else False #bbH has a different label in LHEEventProduct
        isSignal = True if ('HToSSTobbbb_MH-125' in j  or 'HToSSTo4b_MH-125' in j or 'HToSSTobbbb_WToLNu' in j or 'SMS-T1tbs_RPV' in j or 'H2ToSSTobbbb' in j or 'n3n2-n1-hbb-hbb' in j or 'TChiH' in j or 'GluinoGluino' in j or 'DisplacedSUSY_StopToBL' in j or 'XXTo4J' in j or 'SMS' in j) else False #FIXME: Update with other signal modes & models?
        isSUSYCentral = True if ('SMS-TChiHZ' in j) else False
        ##isSignalCentral = True if ('TChiHZ' in j) else False #FIXME: Update with other signal modes & models?
        GT = ''

        if isMINIAOD:
        #from https://indico.cern.ch/event/920726/contributions/3868370/attachments/2055396/3446379/20-06-11_News_PPD.pdf
            if isData:
                if is2016:
                    GT = '102X_dataRun2_v13'
                elif is2017:
                    GT = '102X_dataRun2_v13'
                elif is2018:
                    if any(s in j for s in theRun2018ABC): GT = '102X_dataRun2_v13'
                    if any(s in j for s in theRun2018D):   GT = '102X_dataRun2_Prompt_v16'
            elif not(isData):
                if is2016:
                   GT = '102X_mcRun2_asymptotic_v8'
                elif is2017:
                   GT = '102X_mc2017_realistic_v8'
                elif is2018:
                   GT = '102X_upgrade2018_realistic_v21'

        if isAOD:
            if isData:
                if is2016:
                    GT = '102X_dataRun2_v13'#'80X_dataRun2_2016SeptRepro_v7'
                elif is2017:
                    GT = '102X_dataRun2_v13'#'94X_dataRun2_v11'
                elif is2018:
                    if any(s in j for s in theRun2018ABC): GT = '102X_dataRun2_v13'
                    if any(s in j for s in theRun2018D):   GT = '102X_dataRun2_Prompt_v16'
            elif not(isData):
                if is2016:
                    GT = '102X_mcRun2_asymptotic_v8'#'80X_mcRun2_asymptotic_2016_TrancheIV_v8'
                elif is2017:
                    GT = '102X_mc2017_realistic_v8'
                elif is2018:
                    GT = '102X_upgrade2018_realistic_v21'

        print "GT ->", GT

        JECstring = ''
        if isData and (isReReco or isReMiniAod):
          if any(s in j for s in theRunBCD2016):
            JECstring = "Summer16_23Sep2016BCDV3_DATA" #if isReMiniAod else "Summer16_23Sep2016BCDV3_DATA"
          if any(s in j for s in theRunEF2016):
            JECstring = "Summer16_23Sep2016EFV3_DATA" #if isReMiniAod else "Summer16_23Sep2016EFV3_DATA"
          if any(s in j for s in theRunG2016):
            JECstring = "Summer16_23Sep2016GV3_DATA" #if isReMiniAod else "Summer16_23Sep2016GV3_DATA"
          if any(s in j for s in theRunH2016):
            JECstring = "Summer16_23Sep2016HV3_DATA" #if isReMiniAod else "Summer16_23Sep2016HV3_DATA"
        elif isData and isPromptReco:
           JECstring = "Spring16_25nsV6_DATA"
        elif not isData:
           JECstring = "Summer16_23Sep2016V3_MC"
        else:#dummy!#FIXME Update JEC after current production is done?
           print "WARNING! Dummy JEC for other run eras!!!!!!!!!!!"
           JECstring = "Summer16_23Sep2016HV3_DATA"

        print "JEC ->",JECstring

        #FIXME JERstring should not be needed anymore. Test miniAOD ntuplizer without this parameter!
        JERstring = ''
        MuonSFTriggerstring = ''
        MuonSFISOstring = ''
        MuonSFIDstring = ''
        eleVetoIDstring = ''
        eleLooseIdstring = ''
        eleMediumIdstring = ''
        eleTightIdstring = ''
        eleMVA90noISOstring = ''
        eleMVA80noISOstring = ''
        phoLooseIdFilestring = ''
        phoMediumIdFilestring = ''
        phoTightIdFilestring = ''
        phoMVANonTrigMediumIdFilestring = ''
        btagSFstring = ''
        if is2016:
            JERstring = 'Summer16_25nsV1b_MC'
            #WARNING! Muon SF should not be here applied for 2016! It needed to be a lumi weighted SF and hence only calculated after full run and brilcalc procedure! Needed to be done after ntuplizer process!
            #==> hardcoded in Ntuplizer that SF for Muons are not applied!
            MuonSFTriggerstring = 'MuonTrigger_average_RunBtoH_SF_Run2_2016'
            MuonSFISOstring = 'MuonISO_average_RunBtoH_SF_Run2_2016'
            MuonSFIDstring = 'MuonID_average_RunBtoH_SF_Run2_2016'
            eleVetoIDstring = '2016_ElectronWPVeto_Fall17V2'
            eleLooseIdstring = '2016LegacyReReco_ElectronLoose_Fall17V2'
            eleMediumIdstring = '2016LegacyReReco_ElectronMedium_Fall17V2'
            eleTightIdstring = '2016LegacyReReco_ElectronTight_Fall17V2'
            eleMVA90noISOstring = '2016LegacyReReco_ElectronMVA90noiso_Fall17V2'
            eleMVA80noISOstring = '2016LegacyReReco_ElectronMVA80noiso_Fall17V2'
            phoLooseIdFilestring = 'Fall17V2_2016_Loose_photons'
            phoMediumIdFilestring = 'egammaPlots_MWP_PhoSFs_2016_LegacyReReco_New'
            phoTightIdFilestring = 'Fall17V2_2016_Tight_photons'
            phoMVANonTrigMediumIdFilestring = 'Fall17V2_2016_MVAwp90_photons'
            btagSFstring = 'DeepJet_2016LegacySF_V1'
        elif is2017:
            JERstring = 'Fall17_V3b_MC'
            MuonSFTriggerstring = 'MuonTrigger_EfficienciesAndSF_RunBtoF_Nov17Nov2017'
            MuonSFISOstring = 'MuonISO_2017_RunBCDEF_SF_ISO_Nov17'
            MuonSFIDstring = 'MuonID_2017_RunBCDEF_SF_ID_Nov17'
            eleVetoIDstring = '2017_ElectronWPVeto_Fall17V2'
            eleLooseIdstring = '2017_ElectronLoose_Fall17V2'
            eleMediumIdstring = '2017_ElectronMedium_Fall17V2'
            eleTightIdstring = '2017_ElectronTight_Fall17V2'
            eleMVA90noISOstring = '2017_ElectronMVA90noiso_Fall17V2'
            eleMVA80noISOstring = '2017_ElectronMVA80noiso_Fall17V2'
            phoLooseIdFilestring = '2017_PhotonsLoose'
            phoMediumIdFilestring = '2017_PhotonsMedium'
            phoTightIdFilestring = '2017_PhotonsTight'
            phoMVANonTrigMediumIdFilestring = '2017_PhotonsMVAwp90'
            btagSFstring = 'DeepFlavour_94XSF_V4_B_F_Run2017'
        elif is2018:
            JERstring = 'Autumn18_V7b_MC'
            MuonSFTriggerstring = 'MuonTrigger_EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_AfterMuonHLTUpdate'
            print "WARNING! There is another SF root file for single muon triggers for Run A: run < 316361 it is called: MuonTrigger_EfficienciesStudies_2018_trigger_EfficienciesAndSF_2018Data_BeforeMuonHLTUpdate. TO BE IMPLEMENTED SOMEHOW!"
            print "To ignore this warning, add the option 'isControl = False' to your list"
            if isControl: exit()
            MuonSFISOstring = 'MuonISO_EfficienciesStudies_2018_rootfiles_RunABCD_SF_ISO'
            MuonSFIDstring = 'MuonID_EfficienciesStudies_2018_rootfiles_RunABCD_SF_ID'
            eleVetoIDstring = '2018_ElectronWPVeto_Fall17V2'
            eleLooseIdstring = '2018_ElectronLoose_Fall17V2'
            eleMediumIdstring = '2018_ElectronMedium_Fall17V2'
            eleTightIdstring = '2018_ElectronTight_Fall17V2'
            eleMVA90noISOstring = '2018_ElectronMVA90noiso_Fall17V2'
            eleMVA80noISOstring = '2018_ElectronMVA80noiso_Fall17V2'
            phoLooseIdFilestring = '2018_PhotonsLoose'
            phoMediumIdFilestring = '2018_PhotonsMedium'
            phoTightIdFilestring = '2018_PhotonsTight'
            phoMVANonTrigMediumIdFilestring = '2018_PhotonsMVAwp90'
            btagSFstring = 'DeepJet_102XSF_V2_Run2018'
        print "JER ->", JERstring

        # JSON filter
        jsonName = ""
        if is2016:
            #jsonName = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON"
            jsonName = "Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt"
        elif is2017:
            jsonName = "Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
        elif is2018 and "Cosmics" not in options.groupofsamples:
            jsonName = "Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
        if "resubmission" in options.lists:
            jsonName = prev_folder+"/"+j+"/notFinishedLumis.json"
            print "Resubmission! JSON: ", jsonName

        if isCentralProd and (is2016 or is2017 or is2018):
            jsonName = selected_lumiMasks[j]+'.txt'

        #if isSUSYCentral:
        #    print "SUSY central!!"
        #    jsonName = ""
        #    if is2016:
        #        jsonName += "2016/"
        #    if is2017:
        #        jsonName += "2017/"
        #    if is2018:
        #        jsonName += "2018/"
        #    jsonName += j+"_JSON.txt"

        # Trigger filter
        triggerTag = 'HLT2' if isReHLT else 'HLT'

        if isData:
            filterString = "RECO"
            triggerString = "DQM"
        else:
            if isMINIAOD:
                filterString = "PAT"
                triggerString = "PAT"
            if isAOD:
                filterString = "RECO"
                triggerString = ""#dummy, not used

        #Prepare inputstrings for pyCfg
        string_runLocal = 'runLocal=False'
        string_isData = 'PisData='+str(isData)
        string_isCosmics = 'PisCosmics='+str(isCosmics)
        string_isREHLT = 'PisReHLT='+str(isReHLT)
        string_isReReco = 'PisReReco='+str(isReReco)
        string_isReMiniAod = 'PisReMiniAod='+str(isReMiniAod)
        string_is2016 = 'Pis2016='+str(is2016)
        string_is2017 = 'Pis2017='+str(is2017)
        string_is2018 = 'Pis2018='+str(is2018)
        string_isPromptReco = 'PisPromptReco='+str(isPromptReco)
        string_noLHEinfo = 'PnoLHEinfo='+str(noLHEinfo)
        string_isbbH = 'PisbbH='+str(isbbH)
        string_isSignal = 'PisSignal='+str(isSignal)
        string_isCentralProd = 'PisCentralProd='+str(isCentralProd)
        string_isSUSYCentral = 'PisSUSYCentral='+str(isSUSYCentral)
        string_GT = 'PGT='+str(GT)
        string_JECstring = 'PJECstring='+str(JECstring)
        string_JERstring = 'PJERstring='+str(JERstring)
        string_MuonSFIDstring = 'PMuonSFIDstring='+str(MuonSFIDstring)
        string_MuonSFISOstring = 'PMuonSFISOstring='+str(MuonSFISOstring)
        string_MuonSFTriggerstring = 'PMuonSFTriggerstring='+str(MuonSFTriggerstring)
        string_eleVetoIDstring = 'PeleVetoIDstring='+str(eleVetoIDstring)
        string_eleLooseIdstring = 'PeleLooseIdstring='+str(eleLooseIdstring)
        string_eleMediumIdstring = 'PeleMediumIdstring='+str(eleMediumIdstring)
        string_eleTightIdstring = 'PeleTightIdstring='+str(eleTightIdstring)
        string_eleMVA90noISOstring = 'PeleMVA90noISOstring='+str(eleMVA90noISOstring)
        string_eleMVA80noISOstring = 'PeleMVA80noISOstring='+str(eleMVA80noISOstring)
        string_phoLooseIdFilestring = 'PphoLooseIdFilestring='+str(phoLooseIdFilestring)
        string_phoMediumIdFilestring = 'PphoMediumIdFilestring='+str(phoMediumIdFilestring)
        string_phoTightIdFilestring = 'PphoTightIdFilestring='+str(phoTightIdFilestring)
        string_phoMVANonTrigMediumIdFilestring = 'PphoMVANonTrigMediumIdFilestring='+str(phoMVANonTrigMediumIdFilestring)
        string_btagSFstring = 'PbtagSFstring='+str(btagSFstring)
        string_jsonName = 'PjsonName='+str(jsonName)
        string_triggerTag = 'PtriggerTag='+str(triggerTag)
        string_triggerString = 'PtriggerString='+str(triggerString)
        string_filterString = 'PfilterString='+str(filterString)
        string_calo = 'Pcalo=True' if isCalo else 'Pcalo=False'
        string_tracking = 'Ptracking=True' if isTracking else 'Ptracking=False'
        string_short = 'Pshort=True' if isShort else 'Pshort=False'
        string_control = 'Pcontrol=True' if isControl else 'Pcontrol=False'
        string_VBF = 'PVBF=True' if isVBF else 'PVBF=False'
        string_ggH = 'PggH=True' if isggH else 'PggH=False'
        string_TwinHiggs = 'PTwinHiggs=True' if isTwinHiggs else 'PTwinHiggs=False'
        string_HeavyHiggs = 'PHeavyHiggs=True' if isHeavyHiggs else 'PHeavyHiggs=False'
        string_SUSY = 'PSUSY=True' if isSUSY else 'PSUSY=False'

        string_SUSYHH = 'PSUSYHH=True' if isSUSYHH else 'PSUSYHH=False'
        string_SUSYHZ = 'PSUSYHZ=True' if isSUSYHZ else 'PSUSYHZ=False'
        string_SUSYZZ = 'PSUSYZZ=True' if isSUSYZZ else 'PSUSYZZ=False'

        string_RPV = 'PRPV=True' if isRPV else 'PRPV=False'
        string_Split = 'PSplit=True' if isSplit else 'PSplit=False'
        string_JetJet = 'PJetJet=True' if isJetJet else 'PJetJet=False'
        #string_outName = 'POutName=output'

        ## Set parameters and print python config
        if options.crabaction=="submit" or options.crabaction=="dryrun" or options.crabaction=="test":
            confcalo = config()
            os.system('echo submitting this confcalo...\n')
            confcalo.User.voGroup='dcms'

            confcalo.General.workArea= workarea
            confcalo.General.transferOutputs = True
            confcalo.General.transferLogs = True
            confcalo.General.requestName = j

            confcalo.JobType.pluginName = 'Analysis'
            confcalo.JobType.psetName = "python/" + pset
            confcalo.JobType.inputFiles = inputFiles#['dataAOD']
            confcalo.JobType.maxMemoryMB = maxMemoryMB
            confcalo.JobType.allowUndistributedCMSSW = True

            confcalo.Site.storageSite = 'T2_DE_DESY'
            if whitelist:
                confcalo.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
                #confcalo.Site.whitelist   = ['T2_US_Caltech']
            #confcalo.Site.ignoreGlobalBlacklist   = True #Set to true if e.g. your dataset is in a blacklisted site

            if not (isSplit and "splitSUSY" in j):
                confcalo.Data.inputDataset = selected_requests[j]
            confcalo.Data.splitting = splitting
            confcalo.Data.unitsPerJob = unitsPerJob
            confcalo.Data.publication = False
            confcalo.Data.ignoreLocality = ignoreLocality
            confcalo.Data.outLFNDirBase = outLFNDirBase
            #if "VBFH_HToSS" in j and not isCentralProd:
            #    #automatic implementation of the choice bewteen inputDBS global/phys03
            #    confcalo.Data.inputDBS = "phys03"
            #el
            if "GluGluH_HToSS" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                confcalo.Data.inputDBS = "phys03"
            elif "n3n2-n1-hbb-hbb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                confcalo.Data.inputDBS = "phys03"
            elif "TChiHH" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                confcalo.Data.inputDBS = "phys03"
            elif "GluGluH2_H2ToSSTobb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                confcalo.Data.inputDBS = "phys03"
            else:
                if not (isSplit and "splitSUSY" in j):
                    confcalo.Data.inputDBS = "global"
            if isData:
                if is2016:
                    #confcalo.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
                    print  "Lumi mask link not working, workaround!"
                    confcalo.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
                elif is2017:
                    #confcalo.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
                    print  "Lumi mask link not working, workaround!"
                    confcalo.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
                elif is2018:
                    print  "Lumi mask link not working, workaround!"
                    confcalo.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                    #confcalo.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                if "resubmission" in options.lists:
                    confcalo.Data.lumiMask = os.environ['CMSSW_BASE']+"/src/Analyzer/LLP2018/dataAOD/JSON/"+prev_folder+"/"+j+"/notFinishedLumis.json"

                #confcalo.Data.splitting = 'Automatic'
                #confcalo.Data.unitsPerJob = 100000#comment, giving errors with new crab
            elif isCentralProd:
                if isSignal:
                    confcalo.Data.lumiMask = os.environ['CMSSW_BASE']+'/src/Analyzer/LLP2018/data_gen/JSON/'+selected_lumiMasks[j]+'.txt'
                    print "Use lumiMask: "+os.environ['CMSSW_BASE']+"/src/Analyzer/LLP2018/data_gen/JSON/"+selected_lumiMasks[j]+".txt"

            #This changes the confcalo and forces manual submission one by one, avoid
            if isSUSYCentral:
                if not isGenProd:
                    print "Second check susy central"
                    jsonNameMask = ""
                    if is2016:
                        jsonNameMask += "2016/"
                    if is2017:
                        jsonNameMask += "2017/"
                    if is2018:
                        jsonNameMask += "2018/"
                    if isSUSYHH:
                        jsonNameMask += "HH/"
                    if isSUSYHZ:
                        jsonNameMask += "HZ/"
                    if isSUSYZZ:
                        jsonNameMask += "ZZ/"
                    jsonNameMask += j+"_JSON"
                    confcalo.Data.lumiMask = os.environ['CMSSW_BASE']+'/src/Analyzer/LLP2018/dataAOD/JSON/'+jsonNameMask+'.txt'
                    print "Use lumiMask: "+os.environ['CMSSW_BASE']+"/src/Analyzer/LLP2018/dataAOD/JSON/"+jsonNameMask+".txt"
            
            #wait!!!
            if ( (not isData) and (not isCentralProd) and (not isSUSYCentral) ):
                confcalo.Data.lumiMask = ""
            if isCosmics:
                confcalo.Data.lumiMask = ""


            if isSplit and "splitSUSY" in j:
                #confcalo.Data.outputPrimaryDataset = selected_requests[j]#"/splitSUSY_M2400_100_ctau0p1_TuneCP2_13TeV_pythia8/RunIIAutumn18DRPremix-102X_upgrade2018_realistic_v15-v1/AODSIM"
                list_name = 'dataAOD/list_'+j
                if is2018:
                    list_name+= "_RunIIAutumn18.txt"
                if is2017:
                    list_name+= "_RunIIFall17.txt"
                if is2016:
                    list_name+= "_RunIISummer16.txt"
                confcalo.Data.userInputFiles = open(list_name).readlines()
                confcalo.Data.splitting = 'FileBased'
                confcalo.Data.unitsPerJob = 5


            #confcalo.JobType.pyCfgParams = ['runLocal=False']
            #FIXME JERstring should not be needed anymore. Test miniAOD ntuplizer without this parameter!
            #FIXME isCentralProd is not yet implemented in AOD ntuplizer. Add!
            #FIXME Once those two parameters work similarly for AOD and miniAOD, remove the if...else below
            if isAOD:
                if isGenProd:
                    print "FIXMEEEE"
                    confcalo.JobType.pyCfgParams = [string_runLocal, string_isData, string_is2016, string_is2017, string_is2018, string_noLHEinfo, string_isSignal, string_GT, string_calo, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSYHH, string_SUSYHZ, string_SUSYZZ]

                else:
                    confcalo.JobType.pyCfgParams = [string_runLocal, string_isData, string_isCosmics, string_isREHLT, string_isReReco, string_isReMiniAod,string_isPromptReco, string_is2016, string_is2017, string_is2018, string_noLHEinfo, string_isbbH, string_isSignal, string_isCentralProd, string_isSUSYCentral, string_GT, string_JECstring, string_JERstring, string_MuonSFIDstring, string_MuonSFISOstring, string_MuonSFTriggerstring, string_jsonName, string_eleVetoIDstring, string_eleLooseIdstring, string_eleMediumIdstring, string_eleTightIdstring, string_eleMVA90noISOstring, string_eleMVA80noISOstring, string_phoLooseIdFilestring, string_phoMediumIdFilestring, string_phoTightIdFilestring, string_phoMVANonTrigMediumIdFilestring, string_btagSFstring, string_triggerTag, string_triggerString, string_filterString, string_calo, string_tracking, string_short, string_control, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY, string_SUSYHH, string_SUSYHZ, string_SUSYZZ, string_RPV, string_Split, string_JetJet]


            else:
                confcalo.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod,string_isPromptReco, string_is2016, string_is2017, string_is2018, string_noLHEinfo, string_isbbH, string_isSignal, string_isCentralProd, string_GT, string_JECstring, string_JERstring, string_MuonSFIDstring, string_MuonSFISOstring, string_MuonSFTriggerstring, string_jsonName, string_eleVetoIDstring, string_eleLooseIdstring, string_eleMediumIdstring, string_eleTightIdstring, string_eleMVA90noISOstring, string_eleMVA80noISOstring, string_phoLooseIdFilestring, string_phoMediumIdFilestring, string_phoTightIdFilestring, string_phoMVANonTrigMediumIdFilestring, string_btagSFstring, string_triggerTag, string_triggerString, string_filterString, string_calo, string_tracking, string_short, string_control, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY]

            #Other settings:
            ## Use this for central production 2016 signal as long as in status 'production'
            #confcalo.Data.allowNonValidInputDataset = True
            #enable multi-threading
            #confcalo.JobType.maxMemoryMB = 3000#15900 #more memory
            #deactivate
            #confcalo.JobType.numCores = 8
            ##
            #modify parameters here
            print confcalo

            # Submit confcalo file
            if options.crabaction=="submit":
                if not isCentralProd or not isSignal or not isSUSYCentral:
                    submit(confcalo)
                else:
                    p = Process(target=submit, args=(confcalo,))
                    p.start()
                    p.join()
            if options.crabaction=="dryrun":
                if not isCentralProd or not isSignal or not isSUSYCentral:
                    submit(confcalo, dryrun = True)
                else:
                    p = Process(target=submit, args=(confcalo, True))
                    p.start()
                    p.join()

        elif options.crabaction=="status":
            os.system('echo status -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab status -d ' + workarea + '/crab_'+j+'\n')
            os.system('echo ----------------------------------------------------\n')
        elif options.crabaction=="proceed":
            os.system('echo proceed -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab proceed -d ' + workarea + '/crab_'+j+'\n')
            os.system('echo ----------------------------------------------------\n')
        elif options.crabaction=="resubmit":
            #print "Force resubmission to caltech"
            #os.system('echo resubmit --sitewhitelist=T2_US_Caltech -d ' + workarea + '/crab_'+j+'\n')
            #os.system('crab resubmit --sitewhitelist=T2_US_Caltech -d ' + workarea + '/crab_'+j+'\n')

            #print "Force resubmission to site"
            #os.system('echo resubmit --sitewhitelist=T2_FR_GRIF_IRFU -d ' + workarea + '/crab_'+j+'\n')
            #os.system('crab resubmit --sitewhitelist=T2_FR_GRIF_IRFU -d ' + workarea + '/crab_'+j+'\n')

            os.system('echo resubmit -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab resubmit -d ' + workarea + '/crab_'+j+'\n')

            # To request more memory for failed jobs:
            #os.system('echo resubmit --maxmemory 5000 -d ' + workarea + '/crab_'+j+'\n')
            #os.system('crab resubmit --maxmemory 5000 -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="getoutput":
            os.system('echo getoutput -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab getoutput -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="kill":
            os.system('echo kill -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab kill -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="report":
            os.system('echo report -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab report -d ' + workarea + '/crab_'+j+'\n')
        else:
            print "Invalid crab action. Please type: -a submit/status/proceed/resubmit/dryrun/getoutput/kill"
            exit()
    os.system('echo -%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-\n')
