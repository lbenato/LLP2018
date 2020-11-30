import json
import os

# Input directory
jsonDir = os.environ['CMSSW_BASE']+'/src/Analyzer/LLP2018/data_gen/JSON/'

# Loop over year subdirectories
for yearDir in os.listdir(jsonDir):
    
    # Create backup directory
    if not os.path.exists(jsonDir + yearDir + '/ggH_oldFiles/'):
        os.makedirs(jsonDir + yearDir + '/ggH_oldFiles/')

    # Loop over signal points
    for file in os.listdir(jsonDir + yearDir):
        if ('ggH_HToSSTobbbb' in file):

            # Input filename
            jsonFilename = jsonDir + yearDir + '/' + file
            print("Processing: " + jsonFilename + '\n')
            
            # Create backup
            jsonFilenameOld = jsonDir + yearDir + '/ggH_oldFiles/' + file
            if not os.path.exists(jsonFilenameOld):
                os.system('cp %s %s'%(jsonFilename, jsonFilenameOld))

            # Open input json file
            with open(jsonFilenameOld,'r') as jsonFileOld:
                
                # Get dict
                lumisPerRun = json.load(jsonFileOld)
                if not lumisPerRun: continue

                # Get lumi array [lumi1, lumi2, ...]
                oldLumis = lumisPerRun["1"]
                newLumis = []

                # Create an array with lumi "ranges" [[lumi1,lumi1], [lumi2,lumi2], ...]
                for lumi in oldLumis:
                    newLumis.append([lumi,lumi])

                # Replace lumi array  
                lumisPerRun["1"] = newLumis
                #print(lumisPerRun)

                # Save new json file
                with open(jsonFilename,'w') as jsonFile:
                    json.dump(lumisPerRun, jsonFile) 
