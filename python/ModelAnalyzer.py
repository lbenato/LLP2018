import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')

process = cms.Process("Test")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# process.options = cms.untracked.PSet(
#     wantSummary = cms.untracked.bool(True)
# )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/02CABFEC-61A6-924D-A3E9-B3B41B5AD1C7.root',
        # 'file:/pnfs/desy.de/cms/tier2/store/mc/RunIIAutumn18MiniAOD/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/100000/02DCC1DD-1EEF-2A4D-9641-8703D1D025FB.root',
        ############
        # WminusH v1
        ############
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/EF478A1A-E17C-D14A-8D8B-3C6507B8476D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/E2A90339-5939-7E41-A940-7D10FC083762.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/08A5B142-88B7-A347-904C-88B76D909E96.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/26E463F4-547C-1D4B-8A7E-27E570F60B88.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/E251DEF2-68D9-F246-9C7B-FB06876DA192.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/7F6D1399-C42B-724F-ABBD-BD2714B2F40F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/0F154FC3-DFDD-664E-95DF-B53E38204556.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/C23329A9-2E0B-4043-96CF-7468431269A4.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/4C128918-1D25-7D4D-BE73-895D1CBECDDB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/065EF921-67D6-2E44-853F-31661440FB47.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/A75700B9-22A4-B140-8A06-7578F36F3DE8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/6403B279-F944-F848-937E-3CB11AB610A2.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/40C48B52-AF79-904B-BF0F-007A2FB6F3BB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/F6A657DC-5F5B-4F4B-B563-775B7353470A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/E88611DE-8BEC-9E47-ACD2-5D40E793242A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/F062C55F-5B49-7847-8F62-2FB5E377FC49.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/70000/3FB3088C-C6A0-BD4F-926E-438EFA88DCE3.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/0593B7B4-8B8C-A649-9271-5F0DC1884391.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/201C8DA8-C053-6649-AC31-668310F252C3.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/8BD3A7D9-91B4-DB4C-8AB2-DABC156DAC59.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/2F33057E-C543-D142-BA50-87A0E5B3B9E5.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/8E86D07A-1BE7-6E47-A32B-22C0A2047545.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/7C90593F-C0BF-254B-926B-74E73B75FED7.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/60ED4D31-D1CC-9342-B235-D4F52AE840BB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/E89A9558-23FF-8348-B8ED-DA55ECF3B3B9.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/C5AC9E61-CD3A-1E44-A721-91FC99C2066F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/3304B40F-3B29-0C4E-A4A9-1B69320E90B6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/67BF7C43-B881-5645-93DB-9EDCE71C0726.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/1078F336-A409-5746-9A21-5D6AF3A83DB0.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/7A6AD360-3E25-214B-9158-A1F3A730A16B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/34033982-CECA-924D-902B-FAFB3A00225C.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/6A200E22-4600-0145-981F-D4BEE7D48740.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/5EC7594E-28B2-2E49-907C-87B6E17B9932.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/609417FB-9E69-6947-8ACF-993DE8351627.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/100000/FC0D087F-E24D-D940-BB23-3AA091B849EC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/91A2DD51-060D-8B41-B9F7-0BB3D8C7776C.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/6BA2E163-220C-C14D-8114-145757C75222.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/5BB4E3D6-DD78-1747-9BF1-78BF87E6AEEB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/81CC1755-9A7E-7B45-8491-AE3B18C3F218.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/F236F5C9-D85E-8B44-B487-BE283733FCE8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/60192047-6577-8C48-94C6-68C937B50C98.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/C45AA53E-043D-B04D-9C58-E606C4015F76.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/0F571013-693A-554C-B05C-96A177162E9A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/466CB543-1283-044D-9391-11CE980994F1.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/BD1DDE78-CC1D-2A4A-9A09-83B10895DE14.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/6958F220-9FA0-6946-92AD-2186D9E2B280.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/B178E5D5-6CA8-B34B-A265-AAFE99D80027.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/A17EE685-ED1D-E740-91C0-A8C0114EA903.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/280000/83865C5A-6BFA-524B-B427-A4BC862C1C04.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/5A798016-CA42-3C43-8A90-A17D78EC7440.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/C7F08E47-9EEA-B845-84A2-109EF136DE71.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/5B53B0AE-B936-AB46-91C8-FE9E671FF75F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/DFE5461A-0798-D34B-958C-0205B6543325.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/96F739D9-8079-1342-870B-AC9DE315B309.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/BCCF0CFB-6557-0240-88FC-EF587E771212.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/DCE7784A-E0F0-A841-921A-C18229655F61.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/915CCE56-842D-634B-90E7-7B1CB443F2D6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/C5D5813E-A2DD-5B49-840D-2A2592B7A4CD.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/10000/024D2B08-80B4-CB45-A6C4-6D314C42F192.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/500A142B-D207-7F4F-B2DF-C6BCAE638929.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/B62C3D1D-1CBD-DC47-8672-FB4C707B3396.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/4F222AE9-05F9-F147-A112-94E18AD4B5E8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/FE4606FE-F5CA-A24B-BC13-72C2C98E63D4.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/10000/28032329-2988-0F4D-8B6E-7B6AD7B705E2.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/110000/18D3C85A-D85A-1443-B624-20A494C82E68.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/F8D5720F-C31F-6D4B-9D1C-7991FF7F9C22.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/D76D8F6A-E1CA-6A44-A99F-B8D45C595B6C.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/270000/8C7EE10B-5406-B345-9AFB-09D81297F808.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/10000/E5EBE018-2440-2040-B514-B2BF739C596B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/10000/7DD680A4-ADA0-AB4C-9B57-F95989A26E55.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/10000/F3219BC6-33A8-0D41-AC64-D4D5F297E79F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v2/10000/360B7037-ECCD-6343-8183-8031F9E95E94.root',

        #################
        # WminusH ext1-v1
        #################
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/CB80742F-1683-CB48-B779-EF66E09CED62.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/9392A403-7A73-AB43-8E08-9B7BA69AB87A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/FAD0F6EB-FD77-664F-8845-BB86915B66D7.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/5E4CC706-4175-CB45-A0B7-4C3291F7B46A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/54C2BA4D-D6C5-A544-96E7-521160F538CA.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/E2C7F2D8-950F-C445-A3BC-1358218135AD.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/59B9A366-4E57-C04C-930E-E88EABF6CBFC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/334163F6-B220-044C-B94D-5D3ABEADC2C6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/38DBE284-D03A-024D-88D6-4B209D7A477B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/4F26CACF-BCA9-584A-BCF6-71B9BE02DB14.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/D13EBDBE-F891-E846-B876-D01FC6B4B746.root',

        ############
        # WplusH v1
        ############
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/51C830B8-7819-4240-9D29-50819378D410.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/005C3B82-B384-A54F-B104-A57B57B52C41.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/78D47F8D-03A3-5542-A50D-B631E86E7D94.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/97980529-8AC6-D04A-B298-76E4E04E58B8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/DAD30224-7A2B-5B46-8ECD-293DD81117B1.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/38E9B74F-0FDE-7348-8FE1-6660C69CBA32.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/5325C4FF-35E0-D648-855E-3D6822FA2EAC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/06278C26-8E39-C542-BD01-1FC3D6E858B5.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/98E2C30F-795F-B946-A66A-00A957C6E56B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/B9790644-55E9-C945-8D87-2A54E7F405B8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/94DF3305-BB70-024F-8A6A-652F8DC56DEF.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/E9387105-A184-BE41-A363-77A7DE7C3C2E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/03270A5D-8653-DA4F-8AB8-E07E5BEC22BC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/B259DC2F-5403-5940-98F9-E821DE0AEE82.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/2494A88E-F8BF-DF48-A740-BA9A1130EE8B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/4B9568BE-C301-E14E-A671-557CF0DF6AA1.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/B26435F9-F0EF-384F-9A47-B8DE34711EA4.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/AEA33FA9-5B1C-284A-8BA6-BE38D230A285.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/29DB493C-DB79-8B4B-9326-4FB84A299D7A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/E5A8D25E-0CE5-2249-BA63-0510F7AF9DB0.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/502DA9E6-4FB9-4149-ADD1-63D4DC5943FB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/5FAB4AFD-C1D7-6A42-AB2D-CE4774D692BF.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/0929E6FE-F18B-8441-AF7C-2B87DAF77DDE.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/B9FC2348-2EFD-1240-B258-7533A78A0877.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/4A84A50E-AAAF-F14E-898B-6691EE58D0D2.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/98A4EFA0-D65E-1546-BA34-9FE3D39654DE.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/7BA16F37-BDF1-8E47-BB0E-50F09617C161.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/5FFC38EA-AE55-B84D-83F0-76C7E2F063AC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/0A495A60-D3C1-8B45-AC36-82517C0E151F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/B0B38545-5A8F-AC48-8414-861157190425.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/230000/64C73D92-491A-F244-B426-EC505EACECA9.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/3194E733-EFC3-2044-8F54-77968BB03255.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/A0C5FEEC-4F24-AC40-944E-2308975B91BE.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/F43C28AC-687B-4843-B0FE-FEE59E72B17E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/A47539C9-F405-0540-ABD5-DD5C8522FE56.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/B496E4E0-B9EA-EE48-9988-8548FFF276AA.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/5ECA1B8C-C2E9-7840-9271-3325258A0334.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/29D7992E-504E-5D44-A610-3A26255AA22D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/127D7094-1299-F743-8CD5-118C9C40A94D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/B4E0E427-61A5-0E44-BADA-D900635A01D4.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/EDE0051C-F07E-E44A-9A78-56B1C4E5B239.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/4DC8C8D8-A6AA-8E4D-A800-9CD0B69F8E7E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/B9DC971B-D4D9-DF4B-9E96-9B46DACECBAD.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/87C26B59-A2EC-1E48-BA62-30FF468DE11E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/AEBD9857-94BC-BD48-BAE6-1965550FC09F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/F5A94064-549E-9C47-B09D-000B3911FAB4.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/D5620AF9-8205-2746-AD64-909C7980B7D1.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/7BBE39CE-8725-6D4C-9FA4-FE5DBAA35F1D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/B3BE974E-433B-324E-A113-2275EC41820B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/18A94F28-F36B-5B42-A427-358316B28B6E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/240000/74A7CBB9-66CF-7C43-AB0F-1CBB86CC6A7B.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/7A770AD8-1B68-514D-910B-EDF0AFF6A6A6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/FFE35C38-EA67-8041-A5CD-437B90301A2D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/CA820DA3-7566-B047-BB30-002C07B1084C.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/149E2F28-473F-B74A-8D97-D1A273A30DE7.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/66DA1935-7033-F549-89EF-5E581D931C3A.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/5DD3BEBB-E04E-904B-8A1C-AE2CCBCA5DF6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/C913515A-D68C-7742-BB0F-7F92EB68FAA1.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/710000/ABBBD9FB-14F0-124C-9A9F-5EBFF40D48A6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/710000/ADC715F1-5F59-B447-98A0-6B04D2B7B237.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/AC7AC1B5-5324-F34A-8787-CBADF55D6186.root',
        # '/store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/70000/560EB90A-C0B6-C345-A557-7CCE81DD6370.root',

        ################
        # WplusH ext1-v1
        ################
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/701F451C-B478-AA46-8FE4-D6FE22D79AE2.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/7D0D8E61-8884-1945-A23E-9C74E7BD5984.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/B41C9F56-9B70-234A-915E-EF9F899338DD.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/0288323A-E5F8-F841-AF31-522490FE8A21.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/9038B911-8BA6-5A4F-9354-9A1932F6C075.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/633A1F4B-0312-D24A-B895-8FE5D447B81B.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/FFDB3E85-2DCE-C94A-BC84-2810E148AB6E.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/16839631-2937-8045-B3AC-4F3CEEB8D299.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/1EF814E3-3B4D-1246-9033-A7C241ACE23C.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/40BD5501-A870-4841-B605-0EA1B40DBD87.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/3912874D-DD17-6540-9CE5-783DE048BBC4.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/5FFB6C31-ABC1-A344-BC26-8EC1A671B9C5.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/535A4183-9491-C34F-B8DA-D6D520D6B63F.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/11037DE8-1C27-114E-BEAE-85C22C4CCADA.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/0AAAABF6-C344-6942-92A8-1779ACD9E901.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/A60973D0-CA01-2A4D-81DA-AE205655D95E.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/3CF94F01-1AC3-4A41-8D46-0A55B76FE669.root',
        'root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/260000/CD0C3E13-74F6-0C47-8785-74BF09B95268.root',

        ################
        # ZH v1
        ################
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/2921539A-9EEE-3040-B2C2-A7C27BE3DCAD.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/8B46AE16-692F-4A4E-85FF-6172D73F1834.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/FC4E2FDB-4ED3-7A4F-A7C2-BE4E2E30AFC7.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/02CABFEC-61A6-924D-A3E9-B3B41B5AD1C7.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/AEF58991-8300-964E-A355-436D9CE23059.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/F6AC23DF-20FF-6144-AEFF-BFEBCC783C0E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/1CE247F5-CF07-834E-A89D-911F17AED19F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/36AA9654-A1C6-6D42-A6B3-26DCA8DBDF79.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/AE2E2F08-F57D-C540-90F1-58A4BEC401ED.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/9BA58AEB-E3DA-FB43-8F9C-4CEDB9BA1D90.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/2D56432B-A019-9749-AD69-3543755B89FE.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/04AD4110-83BC-E141-8D90-EFD657C37EC4.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/2F62162C-2862-E241-BACF-11AF9AD4B837.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/C9426028-7775-DB43-B38C-3980FE835493.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/24B2BEEC-8E47-3945-A16C-787D40E944C5.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/6B723ECE-ED5B-DB4C-B343-3742FACEAFEA.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/3431DC9F-AC03-A140-A317-BD84774745A8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/F0A89398-3C75-F74D-A5CD-FBFC7E5948FB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/5CA750DA-8C52-6048-BDE8-B8C4332BDB57.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/CFAAB41A-CB3E-B047-8979-05915AE33423.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/377275D8-7890-9D41-A6FC-CBEEC964239D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/300478DA-2471-3847-80A2-90556A22E59D.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/F945C891-0E0E-4449-89E4-98BCB8C9B555.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/F92EC5C0-A17C-994F-9956-12F99B2AE154.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/266BAE7F-5359-2740-912A-037243671470.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/7601DF80-5C24-A84B-B0C1-80C8205A46FB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/2B8942E5-EB74-4E4A-8445-B86419FB5FE8.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/270000/0E4F8890-A3E4-1540-AAA5-94CA60190178.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/260000/DA3BE598-ED1E-3D45-94DC-2CC545205EEB.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/270000/487DC856-2E70-7345-BB3B-A240474E3319.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/B63C593C-D8A1-1443-8EF6-7299A1B346BC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/89E37F43-67F4-8F47-BBA5-FAA300279471.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/9D90A568-4833-F749-ACC2-6A740566BD02.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/350E7310-8A29-894C-8F4D-4BA4D63A7F54.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/5B566FC4-B42E-D64E-9DB0-43BE5DA254EA.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/0973BFA9-73C3-F744-8D59-B59D23BEA750.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15-v1/20000/3AF285C7-BA93-104C-B9F2-79CFDB3A32EA.root',

        ################
        # ZH ext1-v1
        ################
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/53C107FC-638B-C145-BF8D-A0DA86B45528.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/9FC0727D-B21C-DF4E-ACC6-0B633A9B9F76.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/1C467C0C-D2B1-2546-81D2-4A7FC75722AE.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/772B9D2D-9AC8-9F45-AC08-736CF1C854D1.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/8B17552A-39CF-B246-A932-6D2F0BF1B6BD.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/4CC836A8-EE8C-B044-A43E-8C72C66B566C.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/0A56D1B2-6FA2-B742-829B-231BAA7ADC25.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/77AA5B71-7529-124C-B691-485CF8A72BD0.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/B066883C-D449-C141-B2CF-49F4B2BAFB4E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/2F3226F3-7FC1-B844-88E5-130561744F1F.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/54EBA52C-C138-3B4E-9D71-8F8C541B23BC.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/B1E173D3-525F-6B48-8DF7-A948ACFFDEF6.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/21F4A11F-E88F-9541-A12D-B7303C65D913.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/D3E33365-ECCD-E147-B793-229BA6880E7E.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/AB261A4E-5F58-5A4B-ADFC-EC5DE28077FA.root',
        # '/store/mc/RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/rp_102X_upgrade2018_realistic_v15_ext1-v1/130000/0E5C757E-7AAF-7A44-ABF2-46B704D24EE2.root',
    )
)

#Check if sample was produced with randomized parameter approach:
randomizedParameterSamples = [
    # ggH
    'ggH_HToSSTobbbb_MH-125',
    # 2017 & 2018 VH
    'RunIIFall17MiniAODv2/ZH_HToSSTobbbb_ZToLL_MH-125',
    'RunIIFall17MiniAODv2/WminusH_HToSSTobbbb_WToLNu_MH-125',
    'RunIIFall17MiniAODv2/WplusH_HToSSTobbbb_WToLNu_MH-125',
    'RunIIFall17MiniAODv2/ggZH_HToSSTobbbb_ZToLL_MH-125',
    'RunIIAutumn18MiniAOD/ZH_HToSSTobbbb_ZToLL_MH-125',
    'RunIIAutumn18MiniAOD/WminusH_HToSSTobbbb_WToLNu_MH-125',
    'RunIIAutumn18MiniAOD/WplusH_HToSSTobbbb_WToLNu_MH-125',
    # VBF
    'VBFH_HToSSTo4b_MH-125',
]

hasModelInfo = any(i in process.source.fileNames[0] for i in randomizedParameterSamples)

#Model analyzer:
process.model = cms.EDAnalyzer('ModelAnalyzer',
    # genLumi = cms.InputTag('generator'),
    hasModelInfo = cms.bool(hasModelInfo),
)

process.TFileService = cms.Service( "TFileService",
    fileName = cms.string(
        # 'output.root' if len(options.outputFile)==0 else options.outputFile
        # '/nfs/dust/cms/group/cms-llp/v6_central_miniAOD_2018_14Mar2022/forVHLumiMasks/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8-v1.root' #Done!
        # '/nfs/dust/cms/group/cms-llp/v6_central_miniAOD_2018_14Mar2022/forVHLumiMasks/WminusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8-ext1-v1.root' #Done!
        # '/nfs/dust/cms/group/cms-llp/v6_central_miniAOD_2018_14Mar2022/forVHLumiMasks/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8-v1.root'#Done
        '/nfs/dust/cms/group/cms-llp/v6_central_miniAOD_2018_14Mar2022/forVHLumiMasks/WplusH_HToSSTobbbb_WToLNu_MH-125_TuneCP5_13TeV-powheg-pythia8-ext1-v1.root'#XROOTD issue
        # '/nfs/dust/cms/group/cms-llp/v6_central_miniAOD_2018_14Mar2022/forVHLumiMasks/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8-v1.root'#Done
        # '/nfs/dust/cms/group/cms-llp/v6_central_miniAOD_2018_14Mar2022/forVHLumiMasks/ZH_HToSSTobbbb_ZToLL_MH-125_TuneCP5_13TeV-powheg-pythia8-ext1-v1.root'#Done
    ),
    closeFileFast = cms.untracked.bool(True),
)

process.p = cms.Path(process.model)
