# LLP2018

Ntuplizer compatible with LLPDNNX tagger (https://github.com/LLPDNNX/LLPReco)

## Login to naf SLC7 and setup CMSSW release
```
ssh naf-cms-el7
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

## Checkout LLPDNNX
```
cd CMSSW_10_2_18/src
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
