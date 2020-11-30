# LLP2018

Ntuplizer compatible with LLPDNNX tagger (https://github.com/LLPDNNX/LLPReco)

## Login to naf SL7 and setup CMSSW release
```
ssh naf-cms.desy.de
bash #if you like bash
source /etc/profile.d/modules.sh #if you like bash
export SCRAM_ARCH=slc7_amd64_gcc700
module use -a /afs/desy.de/group/cms/modulefiles/
module load cmssw
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src
cmsenv
git cms-init
scram b -j 10
```

## Set grid environment on SL7 and CRAB3 client API
```
source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh
source /cvmfs/cms.cern.ch/common/crab-setup.sh
```

## EGAMMA modules
Recipe: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#2018_MiniAOD

```
cd $CMSSW_BASE/src
git cms-merge-topic cms-egamma:EgammaPostRecoTools #just adds in an extra file to have a setup function to make things easier 
git cms-merge-topic cms-egamma:PhotonIDValueMapSpeedup1029 #optional but speeds up the photon ID value module so things fun faster
git cms-merge-topic cms-egamma:slava77-btvDictFix_10210 #fixes the Run2018D dictionary issue, see https://github.com/cms-sw/cmssw/issues/26182, may not be necessary for later releases, try it first and see if it works
# now to add the scale and smearing for 2018 (eventually this will not be necessary in later releases but is harmless to do regardless)
git cms-addpkg EgammaAnalysis/ElectronTools
rm EgammaAnalysis/ElectronTools/data -rf
git clone git@github.com:cms-data/EgammaAnalysis-ElectronTools.git EgammaAnalysis/ElectronTools/data
# now build everything
scram b -j 32
```

## Jet Toolbox
Recipe: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetToolbox
```
cd $CMSSW_BASE/src
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_102X_v2
scram b -j 32
```

## PU Jet ID
Recipe:
```
git clone -b 94X_weights_DYJets_inc_v2 git@github.com:cms-jet/PUjetID.git PUJetIDWeights/
git cms-merge-topic singh-ramanpreet:PUID_102_15_v2
cp PUJetIDWeights/weights/pileupJetId_102X_Eta* $CMSSW_BASE/src/RecoJets/JetProducers/data/
##rm -rf PUJetIDWeights/  ### If needed
```


## Checkout LLPDNNX
```
cd $CMSSW_BASE/src
git clone https://github.com/LLPDNNX/LLPReco.git LLPReco
scram b
```

## Clone LLP2018
```
cd $CMSSW_BASE/src
mkdir Analyzer
cd Analyzer
git clone https://github.com/lbenato/LLP2018.git
cd LLP2018
scram b -j 32
```

## Install combine
```
cd $CMSSW_BASE/src
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
scram b
```

## How to produce limits/significance with combine
Datacards must first be prepared in LLP2018 working area.

This script will set all the needed folders for writing datacards and combine results. Copy and edit your own script, choosing the variables for defining your signal region, your mass and ctau points.

```
python python/VBFH_DNN_setting.py -c XXX -t YYY -F ZZZ
```
where XXX is your channel (i.e. VBFH), YYY is your tag variable (i.e. nTrackConstituents), and YYY is the figure of merit you want to calculate (Limits or Significance).

For writing datacards, adapt the following macro (background, cuts, variables can be different):

```
python prepare_datacards_VBFH_DNN.py -c XXX -t YYY -F ZZZ -b
```

Once datacards are written, copy the relevant launching macro and move to combine area:

```
cp combine_macros/launch_combine.py $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/.
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
python launch_combine.py -c XXX -t YYY -F ZZZ
```

You can finally plot your results:

```
cd $CMSSW_BASE/src/Analyzer/LLP2018
python macro/plot_limits.py -c XXX -t YYY -F ZZZ -b
```
