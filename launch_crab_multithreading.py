#Here: standard crab config file

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

config.User.voGroup='dcms'

config.General.workArea = 'crab_projects_LLP'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'python/Ntuplizer2018.py'
config.JobType.inputFiles = ['data']

#config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod, string_isPromptReco,string_noLHEinfo, string_isbbH, string_GT, string_JECstring, string_jsonName, string_triggerTag, string_filterString]

config.General.requestName = 'VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_Summer16_MINIAOD'

config.Data.inputDataset =  '/VBFH_HToSSTobbbb_MH-125_MS-40_ctauS-0_TuneCUETP8M1_13TeV-powheg-pythia8_PRIVATE-MC/lbenato-RunIISummer16-PU_standard_mixing-Moriond17_80X_mcRun2_2016_MINIAOD-28028af67189b3de7224b79195bd0e1d/USER'
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 10000
#config.Data.splitting = 'Automatic'

config.Data.outLFNDirBase = '/store/user/lbenato/choose_a_folder_name'
config.Data.publication = False

config.Site.storageSite = 'T2_DE_DESY'
#config.Site.whitelist   = ['T2_DE_DESY']
#config.Site.blacklist   = ['T2_FR_IPHC']
            
#enable multi-threading
config.JobType.maxMemoryMB = 9000#15900 #more memory
config.JobType.numCores = 8

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    # Selection of samples via python lists
    import os

    list_of_samples = ["SM_Higgs","VV","WJetsToQQ","WJetsToLNu","WJetsToLNu_Pt","DYJetsToQQ","DYJetsToNuNu","DYJetsToLL","ST","TTbar","QCD","signal_VBF","signal_ggH","all","data_obs","ZJetsToNuNu", "DYJets", "WJets", "signal_ZH", "SUSY", "TTbarSemiLep","TTbarNu","ggHeavyHiggs"]#,"data_obs"
    print "Possible subgroups of samples:"
    for a in list_of_samples:
        print a
    print "---------------"

    ########parser#######
    import optparse
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-a", "--crabaction", action="store", type="string", dest="crabaction", default="test")
    parser.add_option("-l", "--lists", action="store", type="string", dest="lists", default="v0_SUSY_calo_AOD_gen")
    parser.add_option("-g", "--groupofsamples", action="store", type="string", dest="groupofsamples", default="")
    parser.add_option("-c", "--calo", action="store_true", dest="calo", default=False)
    parser.add_option("-d", "--datatier", action="store", type="string", dest="datatier", default="AOD")
    parser.add_option("-r", "--runera", action="store", type="string", dest="runera", default="2018")
    parser.add_option("-m", "--mode", action="store", type="string", dest="mode", default="")
    parser.add_option("-M", "--model", action="store", type="string", dest="model", default="SUSY")
    (options, args) = parser.parse_args()


    ####################
    #crabConfig = ''
    if options.calo:
       isCalo=True
    else:
       isCalo=False

    if options.mode=="VBF":
        isVBF = True
        isggH = False
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
    elif options.mode=="ggH":
        isVBF = False
        isggH = True
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
    if options.model=="TwinHiggs":
        isTwinHiggs = True
        isHeavyHiggs = False
        isSUSY = False
    elif options.model=="HeavyHiggs":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        isSUSY = False
    elif options.model=="SUSY":
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = False
        isSUSY = True

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
        isVBF = False
        isggH = False
        isTwinHiggs = False
        isHeavyHiggs = True
        isSUSY = False
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
    else:
        print "No list indicated, aborting!"
        exit()

    selected_requests = {}
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
            if "n3n2-n1-hbb-hbb" in k:
                print k
                selected_requests[k] = requests[k]
        elif options.groupofsamples=="ggHeavyHiggs":
            if "GluGluH2_H2ToSSTobb" in k:
                print k
                selected_requests[k] = requests[k]
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

    if(int(isTwinHiggs) + int(isHeavyHiggs) + int(isSUSY)>1):
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
        isData = True if ('SingleMuon' in j or 'SingleElectron' in j or 'JetHT' in j or 'BTagCSV' in j or 'DisplacedJet' in j or 'MET' in j) else False
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
        isSignal = True if ('HToSSTobbbb_MH-125' in j) else False
        GT = ''

        if isMINIAOD:
            if isData:
                if is2016:
                    if isReMiniAod and any(s in j for s in theRunH2016): GT = '80X_dataRun2_Prompt_v16' 
                    else: GT = '94X_dataRun2_v10'
                elif is2017:
                    GT = '94X_dataRun2_v11'
                elif is2018:
                    if theRun2018ABC: GT = '102X_dataRun2_v12'
                    if theRun2018D:   GT = '102X_dataRun2_Prompt_v15'
            elif not(isData):
                if is2016:
                   GT = '94X_mcRun2_asymptotic_v3'
                elif is2017:
                   GT = '94X_mc2017_realistic_v17'
                elif is2018:
                   GT = '102X_upgrade2018_realistic_v20'

        if isAOD:
            if isData:
                if is2016:
                    GT = '80X_dataRun2_2016SeptRepro_v7'
                elif is2017:
                    GT = '94X_dataRun2_v11'
                elif is2018:
                    if theRun2018ABC: GT = '102X_dataRun2_v12'
                    if theRun2018D:   GT = '102X_dataRun2_Prompt_v15'
            elif not(isData):
                if is2016:
                    GT = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
                elif is2017:
                    GT = '94X_mc2017_realistic_v17'
                elif is2018:
                    GT = '102X_upgrade2018_realistic_v20'

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
        else:#dummy!
           print "WARNING! Dummy JEC for other run eras!!!!!!!!!!!"
           JECstring = "Summer16_23Sep2016HV3_DATA"

        print "JEC ->",JECstring

        # JSON filter
        if is2016:
            jsonName = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON"
        elif is2017:
            jsonName = "Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON"
        elif is2018:
            jsonName = "Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON"

        # Trigger filter
        triggerTag = 'HLT2' if isReHLT else 'HLT'

        if isData:
            filterString = "RECO"
        else:
            if isMINIAOD: filterString = "PAT"
            if isAOD: filterString = "RECO"

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
        string_GT = 'PGT='+str(GT)
        string_JECstring = 'PJECstring='+str(JECstring)
        string_jsonName = 'PjsonName='+str(jsonName)
        string_triggerTag = 'PtriggerTag='+str(triggerTag)
        string_filterString = 'PfilterString='+str(filterString)
        string_calo = 'Pcalo=True' if isCalo else 'Pcalo=False'
        string_VBF = 'PVBF=True' if isVBF else 'PVBF=False'
        string_ggH = 'PggH=True' if isggH else 'PggH=False'
        string_TwinHiggs = 'PTwinHiggs=True' if isTwinHiggs else 'PTwinHiggs=False'
        string_HeavyHiggs = 'PHeavyHiggs=True' if isHeavyHiggs else 'PHeavyHiggs=False'
        string_SUSY = 'PSUSY=True' if isSUSY else 'PSUSY=False'

        # submission of the python config
        if options.crabaction=="submit":
            if "VBFH_HToSS" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "GluGluH_HToSS" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "n3n2-n1-hbb-hbb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "GluGluH2_H2ToSSTobb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            else:
                config.Data.inputDBS = "global"

            os.system('echo submitting this config...\n')
            #modify parameters here
            config.General.requestName = j
            config.Data.inputDataset = selected_requests[j]
            config.JobType.psetName = "python/" + pset
            config.Data.outLFNDirBase = outLFNDirBase
            config.General.workArea= workarea
            if isData:
                if is2016:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
                elif is2017:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
                elif is2018:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                #config.Data.splitting = 'Automatic'
                config.Data.unitsPerJob = 100000
            #config.JobType.pyCfgParams = ['runLocal=False']
            config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod, string_is2016, string_is2017, string_is2018, string_isPromptReco,string_noLHEinfo, string_isbbH, string_isSignal, string_GT, string_JECstring, string_jsonName, string_triggerTag, string_filterString, string_calo, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY]
            print config
            submit(config)

        elif options.crabaction=="status":
            os.system('echo status -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab status -d ' + workarea + '/crab_'+j+'\n')
            os.system('echo ----------------------------------------------------\n') 
        elif options.crabaction=="resubmit":
            os.system('echo resubmit -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab resubmit -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="getoutput":
            os.system('echo getoutput -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab getoutput -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="kill":
            os.system('echo kill -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab kill -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="report":
            os.system('echo report -d ' + workarea + '/crab_'+j+'\n')
            os.system('crab report -d ' + workarea + '/crab_'+j+'\n')
        elif options.crabaction=="test":
            if "VBFH_HToSS" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "GluGluH_HToSS" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "n3n2-n1-hbb-hbb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            elif "GluGluH2_H2ToSSTobb" in j:
                #automatic implementation of the choice bewteen inputDBS global/phys03
                config.Data.inputDBS = "phys03"
            else:
                config.Data.inputDBS = "global"

            os.system('echo submitting this config...\n')
            #modify parameters here
            config.General.requestName = j
            config.Data.inputDataset = selected_requests[j]
            config.JobType.psetName = "python/" + pset
            config.Data.outLFNDirBase = outLFNDirBase
            config.General.workArea= workarea
            if isData:
                if is2016:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
                elif is2017:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
                elif is2018:
                    config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
                #config.Data.splitting = 'Automatic'
                config.Data.unitsPerJob = 100000
            config.JobType.pyCfgParams = [string_runLocal, string_isData, string_isREHLT, string_isReReco, string_isReMiniAod, string_is2016, string_is2017, string_is2018, string_isPromptReco,string_noLHEinfo, string_isbbH, string_isSignal, string_GT, string_JECstring, string_jsonName, string_triggerTag, string_filterString, string_calo, string_VBF, string_ggH, string_TwinHiggs, string_HeavyHiggs, string_SUSY]
            print config
        else:
            print "Invalid crab action. Please type: -a submit/status/resubmit/getoutput/kill"
            exit()
    os.system('echo -%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-%-\n') 





