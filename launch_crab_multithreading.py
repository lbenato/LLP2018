#Here: standard crab config file

import CRABClient
from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
import sys
from multiprocessing import Process
config = config()

config.User.voGroup='dcms'

config.General.workArea = 'crab_projects_LLP'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'python/Ntuplizer2018.py'
config.JobType.inputFiles = ['data']
config.JobType.allowUndistributedCMSSW = True # To use CMSSW_10_2_18 with SL7 (might not be available at some sites)
#config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod, string_isPromptReco,string_noLHEinfo, string_isbbH, string_GT, string_JECstring, string_JERstring, string_jsonName, string_triggerTag, string_filterString]
# config.JobType.priority = 1

config.General.requestName = 'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_Summer16_MINIAOD'

config.Data.inputDataset =  '/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC/lbenato-RunIISummer16-PU_standard_mixing-Moriond17_80X_mcRun2_2016_MINIAOD-28028af67189b3de7224b79195bd0e1d/USER'
config.Data.inputDBS = 'global'

config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 20000#15000
# config.Data.totalUnits = 10000000#15000

#config.Data.splitting = 'Automatic'#Note: Not working with submit --dryrun. Use e.g. 'EventAwareLumiBased'
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1
#config.Data.totalUnits = 20


config.Data.outLFNDirBase = '/store/user/lbenato/choose_a_folder_name'
config.Data.publication = False

config.Site.storageSite = 'T2_DE_DESY'

#Workaround when crab complains that this release+arch isn't supported; running on SL7 machines
config.JobType.allowUndistributedCMSSW = True

#config.Site.ignoreGlobalBlacklist   = True #Set to true if e.g. your dataset is in a blacklisted site
#config.Site.whitelist   = ['T1_US_FNAL'] #Add your preferred site here if setting ignoreGlobalBlacklist to True

#config.Site.blacklist   = ['T2_FR_IPHC']

## Use this for central production 2016 signal as long as in status 'production'
#config.Data.allowNonValidInputDataset = True

#enable multi-threading
#remove from being default!
config.JobType.maxMemoryMB = 3000#15900 #more memory
config.JobType.numCores = 8

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

    list_of_samples = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","WJetsToLNu_Pt","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","TTbarGenMET","TTJets","QCD","QCD_HT","QCD_MuEnriched","signal_VBF","signal_ggH","all","data_obs","MET","SingleMuon","SingleElectron","SinglePhoton","EGamma","JetHT","MuonEG","ZJetsToNuNu", "DYJets", "WJets", "signal_ZH", "SUSY", "TTbarSemiLep","TTbarNu","ggHeavyHiggs","WJetsToLNu_HT", "VBFH_MH-125_2016","VBFH_MH-125_2017", "VBFH_MH-125_2018","ggH_MH-125_2016","ggH_MH-125_2017","ggH_MH-125_2018","gluinoGMSB","Others","data_BTagCSV","WH_MH-125_2016","WH_MH-125_2018","ZH_MH-125_2018","data_ParkingBPH", "data_ParkingBPH_Run2018A", "data_ParkingBPH_test","splitSUSY","JetJet","RPVstopBL"]

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
        isSUSY = False
        isRPV = False
    elif options.mode=="ggH":
        isVBF = False
        isggH = True
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
        isRPV = False
    if options.model=="TwinHiggs":
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
        isRPV = False
    elif options.model=="HeavyHiggs":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        isSUSY = False
        isRPV = False
    elif options.model=="SUSY":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.model=="gluinoGMSB":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.model=="RPV":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = False
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



    folder = ''
    pset = ''
    workarea = ''
    if options.lists == "v7_calo":
        from Analyzer.LLP2018.crab_requests_lists_v7_calo import *
        from Analyzer.LLP2018.samples import sample, samples
        pset = "Ntuplizer_multithreading.py"
        folder = "v7_calo_24Oct2019_multithreading"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        isCalo=True
    elif options.lists == "v0_pfXTag_calo":
        from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
        from Analyzer.LLP2018.samples import sample, samples
        pset = "Ntuplizer2018.py"
        folder = "v0_pfXTag_calo_15Jan2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        isCalo = True
        isVBF = True
    elif options.lists == "v1_gen_production_calo":
        from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
        from Analyzer.LLP2018.samples import sample, samples
        pset = "GenNtuplizer.py"
        folder = "v1_gen_production_calo_17Jan2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        isCalo=True
        config.JobType.inputFiles = ['data_gen']
    elif options.lists == "v1_pfXTag_puppi_calo":
        from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
        from Analyzer.LLP2018.samples import sample, samples
        pset = "Ntuplizer_puppi.py"
        folder = "v1_pfXTag_puppi_calo_21Jan2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        isCalo = True
        isVBF = True
        isggH = False
    elif options.lists == "v2_pfXTag_puppi_calo":
        from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
        from Analyzer.LLP2018.samples import sample, samples
        pset = "Ntuplizer_puppi.py"
        folder = "v2_pfXTag_puppi_calo_23Jan2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        isCalo = True
        isVBF = True
        isggH = False
    elif options.lists == "v2_pfXTag_puppi_calo_signal_fixed":
        from Analyzer.LLP2018.crab_requests_lists_v0_pfXTag_calo import *
        from Analyzer.LLP2018.samples import sample, samples
        pset = "Ntuplizer_puppi.py"
        folder = "v2_pfXTag_puppi_calo_signal_fixed_24Jan2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        isCalo = True
        isVBF = True
        isggH = False
    elif options.lists == "v0_SUSY_calo_MINIAOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_MINIAOD_2018 import *
        from Analyzer.LLP2018.samplesMINIAOD2018 import samples, sample
        config.Data.totalUnits = 2000000 #maximum amount of processed events
        pset = "Ntuplizer2018.py"
        folder = "v0_SUSY_calo_MINIAOD_2018_11Mar2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        is2018 = True
        isMINIAOD = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "v0_SUSY_calo_AOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v0_SUSY_calo_AOD_2018_10Mar2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        is2018 = True
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "v0_ggHeavyHiggs_calo_AOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v0_ggHeavyHiggs_calo_AOD_2018_18Mar2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        is2018 = True
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        isSUSY = False
        isRPV = False
    elif options.lists == "v0_ggHeavyHiggs_calo_AOD_gen":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "TriggerGenNtuplizer.py"
        folder = "v0_ggHeavyHiggs_calo_AOD_gen_19Mar2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data_gen']
        is2018 = True
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        isSUSY = False
        isRPV = False
    elif options.lists == "v0_SUSY_calo_AOD_gen":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "TriggerGenNtuplizer.py"
        folder = "v0_SUSY_calo_AOD_gen_20Mar2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data_gen']
        is2018 = True
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "synch_exercise_caltech":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "Synch.py"
        folder = "synch_exercise_caltech_v2_31Mar2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "v1_SUSY_calo_AOD_2017":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v1_SUSY_calo_AOD_2017_21Apr2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        is2017 = True
        is2016 = False
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "synch_exercise_caltech_v2":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "Synch.py"
        folder = "synch_exercise_caltech_v2_21Apr2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        is2017 = True
        is2016 = False
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "synch_exercise_caltech_v3":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "Synch.py"
        folder = "synch_exercise_caltech_v3_22Apr2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        is2017 = True
        is2016 = False
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False
    elif options.lists == "synch_exercise_caltech_v4":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "synch_exercise_caltech_v4_29Apr2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 5000 #more memory
        is2017 = True
        is2016 = False
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True
        isRPV = False

    elif options.lists == "test_calo_AOD_pfcand":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "test_calo_AOD_pfcand_22Apr2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 15900 #more memory
        is2018 = True
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        isSUSY = False
        isRPV = False
    elif options.lists == "v1_calo_AOD_2017":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v1_calo_AOD_2017_24Apr2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 5000#15900 #more memory
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#only for heavy higgs
        isSUSY = True
        isRPV = False
    elif options.lists == "v2_calo_AOD_2017":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        #folder = "v2_calo_AOD_2017_01May2020"#CHANGE here your crab folder name
        folder = "v2_calo_AOD_2017_genstudies_30May2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 3000#15900 #more memory
        config.JobType.numCores = 4
        is2016 = False
        is2017 = True#!!!
        is2018 = False#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#False#only for heavy higgs
        isSUSY = True#!!!
        isRPV = False
    elif options.lists == "v3_calo_AOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v3_calo_AOD_2018_11June2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 5000#15900 #more memory
        config.JobType.numCores = 8
        config.Data.splitting = 'Automatic'
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
    elif options.lists == "v4_calo_AOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        #pset = "AODNtuplizer2018.py"
        pset = "V4AODNtuplizer.py"
        folder = "v4_calo_AOD_2018_18October2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 5000#15900 #more memory
        config.JobType.numCores = 8
        config.Data.splitting = 'Automatic'
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
        isHeavyHiggs = True#False#only for heavy higgs
        isSUSY = False#!!!
        isRPV = False
    elif options.lists == "v4_taperecall":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v4_taperecall_05Oct2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 4000#5000#15900 #more memory
        config.JobType.numCores = 8
        config.Data.splitting = 'Automatic'
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = True#False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = False#True#!!!
        isRPV = False
    elif options.lists == "v0_2016miniAOD_centrallyProduced":
        from Analyzer.LLP2018.crab_requests_lists_2016MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2016 import sample, samples
        pset = "Ntuplizer2018.py"
        folder = "v0_production_centrallyProduced_LumiMask_full2016/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/meich/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/eichm/" + folder #CHANGE here according to your username!
        config.Data.totalUnits = 200
        isCalo=False
        isShort = True
        isVBF = True
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#True#only for heavy higgs
        isSUSY = False
        isRPV = False
        isCentralProd = True if ("VBFH_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        isAOD  = False
        is2016 = True
        is2017 = False
        is2018 = False
        config.JobType.inputFiles = ['data']
    elif options.lists == "v1_2016miniAOD_centrallyProduced_controlRegion":
        from Analyzer.LLP2018.crab_requests_lists_2016MINIAOD_centrallyProduced_short import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2016_modified import sample, samples
        pset = "Ntuplizer2018.py"
        folder = "v1_production_centrallyProduced_full2016_controlRegion/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/meich/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/eichm/" + folder #CHANGE here according to your username!
#        config.Data.totalUnits = 200
        isCalo=False
        isShort = True
        isTracking = True
        isControl = True
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#True#only for heavy higgs
        isSUSY = False
        isRPV = False
        isCentralProd = True if ("VBFH_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        is2016 = True
        is2017 = False
        is2018 = False
        isAOD  = False
        config.JobType.inputFiles = ['data']
    elif options.lists == "v0_2017miniAOD_centrallyProduced":
        from Analyzer.LLP2018.crab_requests_lists_2017MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2017 import sample, samples
        pset = "Ntuplizer2018.py"
        folder = "v0_production_centrallyProduced_LumiMask_full2017/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/meich/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/eichm/" + folder #CHANGE here according to your username!
        config.Data.totalUnits = 200
        isCalo=False
        isShort = True
        isVBF = True
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#True#only for heavy higgs
        isSUSY = False
        isRPV = False
        isCentralProd = True  if ("VBFH_MH-125_201" in options.groupofsamples) else False
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = True
        isAOD  = False
        config.JobType.inputFiles = ['data']
    elif options.lists == "v0_2018miniAOD_centrallyProduced":
        from Analyzer.LLP2018.crab_requests_lists_2018MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
        pset = "Ntuplizer2018.py"
        folder = "v0_production_centrallyProduced_LumiMask_full2018/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/meich/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/eichm/" + folder #CHANGE here according to your username!
        config.Data.totalUnits = 200
        isCalo=False
        isShort = True
        isVBF = True
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False#True#only for heavy higgs
        isSUSY = False
        isRPV = False
        isCentralProd = True if ("VBFH_MH-125_201" in options.groupofsamples) else False
        is2016 = False
        is2017 = False
        is2018 = True
        isMINIAOD = True
        isAOD  = False
        config.JobType.inputFiles = ['data']
    elif options.lists == "test_calo_AOD_METRun2018A":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "test_calo_AOD_METRun2018A_21Jul2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/kjpena/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/penaka/crabProjects/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['data']
        config.JobType.maxMemoryMB = 3000#15900 #more memory
        config.JobType.numCores = 8
        is2016 = False
        is2017 = False#!!!
        is2018 = True#!!!
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True#False#only for heavy higgs
        isSUSY = False#!!!
        isRPV = False

    elif options.lists == "v5_calo_AOD_2018":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v5_calo_AOD_2018_31December2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 2
        config.Data.ignoreLocality = True
        config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 85
        #config.Data.unitsPerJob = 2
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
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
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = False#True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = True

    elif options.lists == "v5_calo_AOD_2018_resubmission_1":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2018_31December2020"
        folder = "v5_calo_AOD_2018_31December2020_resubmission_1"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 2
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 2
        ##config.Data.totalUnits = 1
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
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
    elif options.lists == "v5_calo_AOD_2018_resubmission_2":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2018_31December2020_resubmission_1"
        folder = "v5_calo_AOD_2018_31December2020_resubmission_2"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 2
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 1
        ##config.Data.totalUnits = 1
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
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
    elif options.lists == "v5_calo_AOD_2018_resubmission_3":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2018 import *
        from Analyzer.LLP2018.samplesAOD2018 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2018_31December2020_resubmission_2"
        folder = "v5_calo_AOD_2018_31December2020_resubmission_3"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4500#15900 #more memory
        #config.JobType.numCores = 2
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 2
        ##config.Data.totalUnits = 1
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
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
    elif options.lists == "v5_calo_AOD_2017":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v5_calo_AOD_2017_31December2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 5
        #config.Data.unitsPerJob = 6
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v5_calo_AOD_2017_resubmission_1":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2017_31December2020"
        folder = "v5_calo_AOD_2017_31December2020_resubmission_1"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 2
        #config.Data.unitsPerJob = 6
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v5_calo_AOD_2017_resubmission_2":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2017_31December2020_resubmission_1"
        folder = "v5_calo_AOD_2017_31December2020_resubmission_2"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 1
        #config.Data.unitsPerJob = 6
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v5_calo_AOD_2017_resubmission_3":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2017 import *
        from Analyzer.LLP2018.samplesAOD2017 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2017_31December2020_resubmission_2"
        folder = "v5_calo_AOD_2017_31December2020_resubmission_3"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 1
        #config.Data.unitsPerJob = 6
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = False
        is2017 = True
        is2018 = False
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v5_calo_AOD_2016":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        folder = "v5_calo_AOD_2016_31December2020"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 5
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = True
        is2017 = False#
        is2018 = False#
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False
    elif options.lists == "v5_calo_AOD_2016_resubmission_1":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2016_31December2020"
        folder = "v5_calo_AOD_2016_31December2020_resubmission_1"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 3000#4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 1
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = True
        is2017 = False#
        is2018 = False#
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False

    elif options.lists == "v5_calo_AOD_2016_resubmission_2":
        from Analyzer.LLP2018.crab_requests_lists_calo_AOD_2016 import *
        from Analyzer.LLP2018.samplesAOD2016 import samples, sample
        pset = "AODNtuplizer2018.py"
        prev_folder = "v5_calo_AOD_2016_31December2020_resubmission_1"
        folder = "v5_calo_AOD_2016_31December2020_resubmission_2"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/lbenato/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/lbenato/" + folder #CHANGE here according to your username!
        config.JobType.inputFiles = ['dataAOD']
        config.JobType.maxMemoryMB = 4000#15900 #more memory
        #config.JobType.numCores = 8
        #config.Data.splitting = 'Automatic'
        #config.Data.ignoreLocality = True
        #config.Site.whitelist   = ['T2_DE_DESY'] #Add your preferred site here if setting ignoreGlobalBlacklist to True
        config.Data.splitting = 'LumiBased'
        config.Data.unitsPerJob = 1
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        is2016 = True
        is2017 = False#
        is2018 = False#
        isMINIAOD = False
        isAOD  = True
        isCalo = True
        isShort = False
        isTracking = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False#True#False#only for heavy higgs
        isSUSY = True#False#!!!
        isRPV = False
        isJetJet = False
        isSplit = False
    elif options.lists == "v1_central_miniAOD_2016_17Nov2020":
        from Analyzer.LLP2018.crab_requests_lists_2016MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2016 import sample, samples
        if ("H_MH-125_2017" in options.groupofsamples or "H_MH-125_2018" in options.groupofsamples):
            print("Error: Using wrong group of samples for 2016 list")
            exit()
        if ("2017" in options.runera or "2018" in options.runera):
            print("Error: Using wrong run era for 2016 list")
            exit()
        pset = "Ntuplizer2018.py"
        folder = "v0_central_miniAOD_2016_17Nov2020/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/kjpena/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/penaka/crabProjects/" + folder #CHANGE here according to your username!
        isCalo = False
        isTracking = True
        isShort = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        isRPV = False
        isSUSY = False
        isCentralProd = True if ("VBFH_MH-125_201" in options.groupofsamples or "ggH_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        isAOD  = False
        is2016 = True
        is2017 = False
        is2018 = False
        config.JobType.inputFiles = ['data']
    elif options.lists == "v1_central_miniAOD_2017_17Nov2020":
        from Analyzer.LLP2018.crab_requests_lists_2017MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2017 import sample, samples
        if ("H_MH-125_2016" in options.groupofsamples or "H_MH-125_2018" in options.groupofsamples):
            print("Error: Using wrong group of samples for 2017 list")
            exit()
        if ("2016" in options.runera or "2018" in options.runera):
            print("Error: Using wrong run era for 2017 list")
            exit()
        pset = "Ntuplizer2018.py"
        folder = "v0_central_miniAOD_2017_17Nov2020/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/kjpena/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/penaka/crabProjects/" + folder #CHANGE here according to your username!
        isCalo = False
        isTracking = True
        isShort = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
        isRPV = False
        isCentralProd = True if ("VBFH_MH-125_201" in options.groupofsamples or "ggH_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        isAOD  = False
        is2016 = False
        is2017 = True
        is2018 = False
        config.JobType.inputFiles = ['data']
    elif options.lists == "v5_central_miniAOD_2018_12Mar2021":
        os.system('tput bold && tput setab 1') #Print bold text in red background. Format is reset in the next line
        os.system('echo "     REMINDER: Make sure PU weight file is updated for this production\'s ParkingBPH data!     $(tput sgr0)"')
        from Analyzer.LLP2018.crab_requests_lists_2018MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
        if ("H_MH-125_2016" in options.groupofsamples or "H_MH-125_2017" in options.groupofsamples):
            print("Error: Using wrong group of samples for 2018 list")
            exit()
        if ("2016" in options.runera or "2017" in options.runera):
            print("Error: Using wrong run era for 2018 list")
            exit()
        pset = "Ntuplizer2018.py"
        folder = "v5_central_miniAOD_2018_12Mar2021/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/kjpena/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/penaka/crabProjects/" + folder #CHANGE here according to your username!
        isCalo = False
        isTracking = True
        isShort = False
        isControl = False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
        isRPV = False
        isCentralProd = True if ("VBFH_MH-125_201" in options.groupofsamples or "ggH_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        isAOD  = False
        is2016 = False
        is2017 = False
        is2018 = True
        config.JobType.inputFiles = ['data']
    elif options.lists == "v6_central_miniAOD_2018_14Mar2022" or options.lists == "v6_central_miniAOD_2018_28Mar2022":
        os.system('tput bold && tput setab 1') #Print bold text in red background. Format is reset in the next line
        os.system('echo "     REMINDER: Make sure PU weight file is updated for this production\'s ParkingBPH data!     $(tput sgr0)"')
        from Analyzer.LLP2018.crab_requests_lists_2018MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
        if ("H_MH-125_2016" in options.groupofsamples or "H_MH-125_2017" in options.groupofsamples):
            print("Error: Using wrong group of samples for 2018 list")
            exit()
        if ("2016" in options.runera or "2017" in options.runera):
            print("Error: Using wrong run era for 2018 list")
            exit()
        pset = "Ntuplizer2018.py"
        folder = options.lists + "/"#CHANGE here your crab folder name
        outLFNDirBase = "/store/user/kjpena/"+folder #CHANGE here according to your username!
        workarea = "/nfs/dust/cms/user/penaka/crabProjects/" + folder #CHANGE here according to your username!
        isCalo = False
        isTracking = True
        isShort = False
        isControl = True if ("14Mar" in options.lists) else False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
        isCentralProd = True if ("H_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        isAOD  = False
        is2016 = False
        is2017 = False
        is2018 = True
        config.JobType.inputFiles = ['data',os.environ['CMSSW_BASE']+'/src/HiggsLongLived/DeepSets/data/']
        # config.Data.splitting = 'Automatic'
        # config.Data.splitting = 'FileBased'
        # config.Data.unitsPerJob = 1
        # if "ParkingBPH" in options.groupofsamples: config.Data.totalUnits = 5000 #Use w/ FileBased splitting for data
    elif options.lists == "v7_central_miniAOD_2018_ControlRegion_21Mar2023" or "v7_central_miniAOD_2018_SignalRegion_21Mar2023":
        os.system('tput bold && tput setab 1') #Print bold text in red background. Format is reset in the next line
        os.system('echo "     REMINDER: Make sure PU weight file is updated for this production\'s ParkingBPH data!     $(tput sgr0)"')
        from Analyzer.LLP2018.crab_requests_lists_2018MINIAOD_centrallyProduced import *
        from Analyzer.LLP2018.crab_lumiMask_lists_gen_centrallyProduced import *
        from Analyzer.LLP2018.samples_centrallyProduced_MINIAOD2018 import sample, samples
        if ("H_MH-125_2016" in options.groupofsamples or "H_MH-125_2017" in options.groupofsamples):
            print("Error: Using wrong group of samples for 2018 list")
            exit()
        if ("2016" in options.runera or "2017" in options.runera):
            print("Error: Using wrong run era for 2018 list")
            exit()
        pset = "Ntuplizer2018.py"
        folder = options.lists + "/"
        outLFNDirBase = "/store/user/kjpena/"+folder
        workarea = "/nfs/dust/cms/user/penaka/crabProjects/" + folder
        isCalo = False
        isTracking = True
        isShort = False
        isControl = True if ("ControlRegion" in options.lists) else False
        isVBF = False
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
        isCentralProd = True if ("H_MH-125_201" in options.groupofsamples) else False
        isMINIAOD = True
        isAOD  = False
        is2016 = False
        is2017 = False
        is2018 = True
        config.JobType.inputFiles = ['data',os.environ['CMSSW_BASE']+'/src/HiggsLongLived/DeepSets/data/']
        config.Data.splitting = 'Automatic'
        # config.Data.splitting = 'FileBased'
        # config.Data.unitsPerJob = 1
        # if "ParkingBPH" in options.groupofsamples: config.Data.totalUnits = 5000 #Use w/ FileBased splitting for data
    else:
        print "No list indicated, aborting!"
        exit()

    if options.crabaction == "dryrun":
        config.Data.splitting = 'LumiBased'
        #config.Data.unitsPerJob = 30
        #if isData:
        #    config.Data.unitsPerJob = 30
        #else:
        #    config.Data.unitsPerJob = 20
        #config.Data.splitting = 'EventAwareLumiBased'
        #config.Data.unitsPerJob = 2500#15000

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
        elif options.groupofsamples=="SUSY":
            if ("n3n2-n1-hbb-hbb" in k) or ("TChiHH" in k):
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
        # Separate datasets for centrally-produced 2016 WH signal
        elif "WH_MH-125_2016" in options.groupofsamples:
            if "WminusH_HToSSTobbbb_" in k or "WplusH_HToSSTobbbb_" in k:
                print k
                selected_requests[k] = requests[k]
        # Randomized-parameter dataset for centrally-produced 2018 WH signal
        elif "WH_MH-125_2018" in options.groupofsamples:
            if "WminusH_HToSSTobbbb_" in k or "WplusH_HToSSTobbbb_" in k:
                print k
                selected_requests[k] = requests[k]
                if k in masks.keys():
                    selected_lumiMasks[k] = masks[k]
                    print "lumi mask:", masks[k]
                else:
                    print "no mask available"
                    exit()
        elif "ZH_MH-125_2018" in options.groupofsamples:
            if "ZH_HToSSTobbbb_" in k:
                print k
                selected_requests[k] = requests[k]
                if k in masks.keys():
                    selected_lumiMasks[k] = masks[k]
                    print "lumi mask:", masks[k]
                else:
                    print "no mask available"
                    exit()
        elif "ggH_MH-125_201" in options.groupofsamples:
            if "ggH_HToSSTobbbb" in k and "MS-" in k:
                print k
                selected_requests[k] = requests[k]
                if k in masks.keys():
                    selected_lumiMasks[k] = masks[k]
                    print "lumi mask:", masks[k]
                elif "MS-15_ctauS-1_" in k: #First signal point: Privately produced
                    print "Signal point missing from central production: Privately produced, no lumi mask needed"
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
        print "Running CONTROL REGION!"
        print "\n"
        print "***************************************"
        print "***************************************"
        print "***************************************"
        print "\n"

    if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSY) + int(isRPV) + int(isSplit) + int(isJetJet)>1):
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

    if isSUSY:
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
        isData = True if ('SingleMuon' in j or 'SingleElectron' in j or 'JetHT' in j or 'BTagCSV' in j or 'DisplacedJet' in j or 'ParkingBPH' in j or 'METRun' in j or 'EGamma' in j or 'MuonEG' in j or 'SinglePhoton' in j) else False
        print "isData?", isData
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
        isSignal = True if ('HToSSTobbbb_MH-125' in j or 'HToSSTo4b_MH-125' in j or 'HToSSTobbbb_WToLNu' in j or 'HToSSTobbbb_ZToLL' in j or 'SMS-T1tbs_RPV' in j or 'H2ToSSTobbbb' in j or 'n3n2-n1-hbb-hbb' in j or 'TChiHH' in j or 'GluinoGluino' in j or 'DisplacedSUSY_StopToBL' in j or 'XXTo4J' in j) else False #FIXME: Update with other signal modes & models?
        isCentralProd = ("H_MH-125_201" in options.groupofsamples) and not (is2018 and "ggH_HToSSTobbbb_MH-125_MS-15_ctauS-1_" in j) #First signal point: Privately produced
        GT = ''

        if isMINIAOD:
        #from https://indico.cern.ch/event/920726/contributions/3868370/attachments/2055396/3446379/20-06-11_News_PPD.pdf
            if isData:
                if is2016:
                    GT = '102X_dataRun2_v14'
                elif is2017:
                    GT = '102X_dataRun2_v14'
                elif is2018:
                    if any(s in j for s in theRun2018ABC): GT = '102X_dataRun2_v14'
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
            # print "To ignore this warning, add the option 'isControl = False' to your list"
            # if isControl: exit()
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

        # JSON filter (Note: Parameter not used in miniAOD ntuplizer. Update directly there for local jobs (and below for crab jobs)!)
        jsonName = ""
        if is2016:
            #jsonName = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON"
            jsonName = "Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt"
        elif is2017:
            jsonName = "Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt"
        elif is2018:
            if isTracking:
                jsonName = "Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"
            else:
                jsonName = "Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
        if "resubmission" in options.lists:
            jsonName = prev_folder+"/"+j+"/notFinishedLumis.json"
            print "Resubmission! JSON: ", jsonName

        if isCentralProd and (is2016 or is2017 or is2018):
            jsonName = selected_lumiMasks[j]+'.txt'

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
        string_RPV = 'PRPV=True' if isRPV else 'PRPV=False'
        string_Split = 'PSplit=True' if isSplit else 'PSplit=False'
        string_JetJet = 'PJetJet=True' if isJetJet else 'PJetJet=False'
        #string_outName = 'POutName=output'

        # Set parameters and print python config
        if options.crabaction=="submit" or options.crabaction=="dryrun" or options.crabaction=="recover" or options.crabaction=="test":
            if "VBFH_HToSS" in j and not isCentralProd:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "ggH_HToSS" in j and not isCentralProd:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "GluGluH_HToSS" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "n3n2-n1-hbb-hbb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "TChiHH" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "GluGluH2_H2ToSSTobb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            else:
                config.Data.inputDBS = "global"

            # Some sample-specific settings:
            if isTracking and is2018 and isData:
                config.Data.splitting = 'FileBased'
                config.Data.unitsPerJob = 1

            elif isTracking and is2018 and isSignal:
                config.Data.splitting = 'EventAwareLumiBased'
                config.Data.unitsPerJob = 150000

            elif isTracking and is2018 and "ST_t-channel_top" in j:
                config.Data.splitting = 'FileBased'
                config.Data.unitsPerJob = 10

            elif isTracking and is2018 and "DYJetsToLL_M-50" in j and "ext2-v1" in j:
                config.Data.splitting = 'FileBased'
                config.Data.unitsPerJob = 10

            elif isTracking and is2018:
                config.Data.splitting = 'EventAwareLumiBased'
                config.Data.unitsPerJob = 250000

            os.system('echo submitting this config...\n')
            #modify parameters here
            config.General.requestName = j# + "_01Jun2022"
            config.Data.inputDataset = selected_requests[j]
            config.JobType.psetName = "python/" + pset
            config.Data.outLFNDirBase = outLFNDirBase
            config.General.workArea= workarea
            config.Data.lumiMask = ""
            if isData:
                if is2016:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
                elif is2017:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
                elif is2018:
                    if isTracking:
                        if options.groupofsamples == "data_ParkingBPH_test":
                            if isControl:
                                config.Data.lumiMask = '/nfs/dust/cms/user/penaka/crabProjects/v6_central_miniAOD_2018_14Mar2022/crab_ParkingBPH1_Run2018D-05May2019promptD-v1/results/processedLumis.json'
                            else:
                                config.Data.lumiMask = '/nfs/dust/cms/user/penaka/crabProjects/v6_central_miniAOD_2018_28Mar2022/crab_ParkingBPH1_Run2018D-05May2019promptD-v1/results/processedLumis.json'
                        else:
                            config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'
                    else:
                        # config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                        config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                if "resubmission" in options.lists:
                    config.Data.lumiMask = os.environ['CMSSW_BASE']+"/src/Analyzer/LLP2018/dataAOD/JSON/"+prev_folder+"/"+j+"/notFinishedLumis.json"

                #config.Data.splitting = 'Automatic'
                #config.Data.unitsPerJob = 100000#comment, giving errors with new crab
            elif isCentralProd:
                if isSignal and selected_lumiMasks[j] != '':
                    config.Data.lumiMask = os.environ['CMSSW_BASE']+'/src/Analyzer/LLP2018/data_gen/JSON/'+selected_lumiMasks[j]+'.txt'
                    print "Use lumiMask: "+os.environ['CMSSW_BASE']+"/src/Analyzer/LLP2018/data_gen/JSON/"+selected_lumiMasks[j]+".txt"
            if options.crabaction=="recover":
                # JSON file with "not processed" lumis, obtained with 'crab report' (default is notFinished)
                recoveryJSON = workarea + '/crab_'+j+"/results/notFinishedLumis.json"
                print "Using recovery lumiMask: " + recoveryJSON
                # recoveryJSON = workarea + '/crab_'+j+"/report/results/notPublishedLumis.json"
                # recoveryJSON = workarea + '/crab_'+j+"/report/results/failedLumis.json"
                if not (os.path.exists(recoveryJSON)):
                    print "Recovery JSON file does not exist. Please check!"
                    print "Use 'crab report' to get the list of non-processed lumis"
                    exit()
                config.General.requestName = j + "_recoveryTask"
                config.Data.lumiMask = recoveryJSON
            #config.JobType.pyCfgParams = ['runLocal=False']
            #FIXME JERstring should not be needed anymore. Test miniAOD ntuplizer without this parameter!
            #FIXME isCentralProd is not yet implemented in AOD ntuplizer. Add!
            #FIXME Once those two parameters work similarly for AOD and miniAOD, remove the if...else below
            if isAOD:
                config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod,string_isPromptReco, string_is2016, string_is2017, string_is2018, string_noLHEinfo, string_isbbH, string_isSignal, string_isCentralProd, string_GT, string_JECstring, string_JERstring, string_MuonSFIDstring, string_MuonSFISOstring, string_MuonSFTriggerstring, string_jsonName, string_eleVetoIDstring, string_eleLooseIdstring, string_eleMediumIdstring, string_eleTightIdstring, string_eleMVA90noISOstring, string_eleMVA80noISOstring, string_phoLooseIdFilestring, string_phoMediumIdFilestring, string_phoTightIdFilestring, string_phoMVANonTrigMediumIdFilestring, string_btagSFstring, string_triggerTag, string_triggerString, string_filterString, string_calo, string_tracking, string_short, string_control, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY, string_RPV, string_Split, string_JetJet]
            else:
                config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod,string_isPromptReco, string_is2016, string_is2017, string_is2018, string_noLHEinfo, string_isbbH, string_isSignal, string_isCentralProd, string_GT, string_JECstring, string_JERstring, string_MuonSFIDstring, string_MuonSFISOstring, string_MuonSFTriggerstring, string_jsonName, string_eleVetoIDstring, string_eleLooseIdstring, string_eleMediumIdstring, string_eleTightIdstring, string_eleMVA90noISOstring, string_eleMVA80noISOstring, string_phoLooseIdFilestring, string_phoMediumIdFilestring, string_phoTightIdFilestring, string_phoMVANonTrigMediumIdFilestring, string_btagSFstring, string_triggerTag, string_triggerString, string_filterString, string_calo, string_tracking, string_short, string_control, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY]
            print config
            # Submit config file
            if options.crabaction=="submit" or options.crabaction=="recover":
                if not isCentralProd or not isSignal:
                    submit(config)
                else:
                    p = Process(target=submit, args=(config,))
                    p.start()
                    p.join()
            if options.crabaction=="dryrun":
                if not isCentralProd or not isSignal:
                    submit(config, dryrun = True)
                else:
                    p = Process(target=submit, args=(config, True))
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
            #os.system('echo resubmit -d ' + workarea + '/crab_'+j+'\n')
            #os.system('crab resubmit -d ' + workarea + '/crab_'+j+'\n')
            # To request more memory for failed jobs:
            os.system('echo resubmit --maxmemory 5000 -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab resubmit --maxmemory 5000 -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="getoutput":
            os.system('echo getoutput -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab getoutput -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="kill":
            os.system('echo kill -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab kill -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="report":
            os.system('echo report -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab report -d ' + workarea + '/crab_'+j+'\n')
#        elif options.crabaction=="test":
#            if "VBFH_HToSS" in j and not isCentralProd:
#                #automatic implementation of the choice bewteen inputDBS global/phys03
#                config.Data.inputDBS = "phys03"
#            elif "GluGluH_HToSS" in j:
#                #automatic implementation of the choice bewteen inputDBS global/phys03
#                config.Data.inputDBS = "phys03"
#            elif "n3n2-n1-hbb-hbb" in j:
#                #automatic implementation of the choice bewteen inputDBS global/phys03
#                config.Data.inputDBS = "phys03"
#            elif "GluGluH2_H2ToSSTobb" in j:
#                #automatic implementation of the choice bewteen inputDBS global/phys03
#                config.Data.inputDBS = "phys03"
#            else:
#                config.Data.inputDBS = "global"
#
#            os.system('echo submitting this config...\n')
#            #modify parameters here
#            config.General.requestName = j
#            config.Data.inputDataset = selected_requests[j]
#            config.JobType.psetName = "python/" + pset
#            config.Data.outLFNDirBase = outLFNDirBase
#            config.General.workArea= workarea
#            if isData:
#                if is2016:
#                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
#                elif is2017:
#                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
#                elif is2018:
#                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
#                #config.Data.splitting = 'Automatic'
#                config.Data.unitsPerJob = 100000
#            elif isCentralProd:
#                if isSignal:
#                    config.Data.lumiMask = '/afs/desy.de/user/e/eichm/xxl/af-cms/CMSSW_10_2_18/src/Analyzer/LLP2018/data_gen/JSON/'+selected_lumiMasks[j]+'.txt'
#                    print "Use lumiMask: /afs/desy.de/user/e/eichm/xxl/af-cms/CMSSW_10_2_18/src/Analyzer/LLP2018/data_gen/JSON/"+selected_lumiMasks[j]+".txt"
#            config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod, string_is2016, string_is2017, string_is2018, string_isPromptReco,string_noLHEinfo, string_isbbH, string_isSignal, string_isCentralProd, string_GT, string_JECstring, string_JERstring, string_jsonName, string_triggerTag, string_filterString, string_calo, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY]
#            print config
        else:
            print "Invalid crab action. Please type: -a submit/status/proceed/resubmit/dryrun/getoutput/kill"
            exit()
    os.system('echo -%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-\n')
