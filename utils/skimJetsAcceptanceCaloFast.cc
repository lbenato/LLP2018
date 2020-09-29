#include "TFile.h"
#include "TTree.h"
#include "TMath.h"

#include <vector>
#include <iostream>
#include <map>
#include <chrono>//compute time
#include <ctime>//compute time

#include "Analyzer/LLP2018/plugins/Objects.h"
//#include "Analyzer/LLP2018/plugins/ObjectsFormat.h"
//#include "Analyzer/LLP2018/plugins/ObjectsFormat.cc"
//#include "Objects.h"

//bool pt_sorter(PFCandidateType const& lhs, PFCandidateType const& rhs) {
//    if (lhs.pt != rhs.pt)
//        return lhs.pt > rhs.pt;
//}

bool pt_sorter(const PFCandidateType& x, const PFCandidateType& y) { return x.pt > y.pt; }
/*
double avg ( vector & v )
{
        double return_value = 0.0;
        int n = v.size();
       
        for ( int i=0; i < n; i++)
        {
            return_value += v[i];
        }
       
        return ( return_value / size);
}
*/

double avg ( std::vector<double> & v )
{
        double return_value = 0.0;
        int n = v.size();
       
        for ( int i=0; i < n; i++)
        {
            return_value += v.at(i);
        }
       
        return ( return_value / n);
}

void skimJetsAcceptanceCaloFast(
                 std::string inFilename=
                 "/pnfs/desy.de/cms/tier2/store/user/lbenato/v3_calo_AOD_2018_11June2020/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_ext1-v2/200623_122753/0000/output_10.root",
		 //"output.root",
		 //"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC.root",
                 //"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC.root",
                 //"/nfs/dust/cms/group/cms-llp/test_calo_AOD_pfcand/WW_TuneCP5_13TeV-pythia8-v2.root",//
                 std::string outFilename=
		 //"/nfs/dust/cms/group/cms-llp/test_calo_AOD_pfcand/Skim/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC.root"
		 "output_4ML.root",
		 Long64_t first_event=0,
		 Long64_t last_event=-1,
		 Bool_t doPFCand=true
             )

{//"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC_ML.root") {

    auto start = std::chrono::system_clock::now();//time!
    // =================
    // Input
    // =================
    TFile *inFile = TFile::Open(inFilename.data(),"READ"); if (!inFile) return;
    TTree *inTree = (TTree*)inFile->Get("ntuple/tree");
    TH1F  *counter = (TH1F*)inFile->Get("counter/c_nEvents");
    Float_t tree_weight = inTree->GetWeight();
    std::cout << "Tree weight: " << tree_weight << std::endl;

    // Input variables
    Long64_t EventNumber;
    Long64_t RunNumber;
    Long64_t LumiNumber;
    Float_t  EventWeight;
    Bool_t   isMC;
    Bool_t   isVBF;
    Bool_t   HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v;
    Bool_t   HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v;
    Bool_t   Flag2_globalSuperTightHalo2016Filter;
    Bool_t   Flag2_goodVertices;
    Bool_t   Flag2_EcalDeadCellTriggerPrimitiveFilter;
    Bool_t   Flag2_HBHENoiseFilter;
    Bool_t   Flag2_HBHEIsoNoiseFilter;
    Bool_t   Flag2_ecalBadCalibFilter;
    Bool_t   Flag2_eeBadScFilter;
    Bool_t   Flag2_BadPFMuonFilter;

    //Bool_t   HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v;
    //Bool_t   HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v;
    Float_t  HT;
    Float_t  MinJetMetDPhi;
    Long64_t nCHSJets;
    Long64_t nCHSFatJets;
    Int_t    nElectrons;
    Int_t    nMuons;
    Int_t    nPhotons;
    Int_t    nTaus;
    Int_t    nPFCandidates;
    Int_t    nPFCandidatesTrack;
    //Int_t    nLLPInCalo;

    std::vector<JetType>         *Jets = 0;
    std::vector<FatJetType>      *FatJets = 0;
    std::vector<PFCandidateType> *PFCandidates = 0;
    MEtType                      *MEt = 0;

    // Input branches
    TBranch        *b_Jets = 0;
    TBranch        *b_FatJets = 0;
    TBranch        *b_PFCandidates = 0;
    TBranch        *b_MEt = 0;
    //TBranch        *b_Jet_0_PFCandidates = 0;
    TBranch        *b_EventNumber;
    TBranch        *b_RunNumber;
    TBranch        *b_LumiNumber;
    TBranch        *b_metpt;
    TBranch        *b_EventWeight;
    TBranch        *b_isMC;
    TBranch        *b_isVBF;
    TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v;
    TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v;
    TBranch        *b_Flag2_globalSuperTightHalo2016Filter;
    TBranch        *b_Flag2_goodVertices;
    TBranch        *b_Flag2_EcalDeadCellTriggerPrimitiveFilter;
    TBranch        *b_Flag2_HBHENoiseFilter;
    TBranch        *b_Flag2_HBHEIsoNoiseFilter;
    TBranch        *b_Flag2_ecalBadCalibFilter;
    TBranch        *b_Flag2_eeBadScFilter;
    TBranch        *b_Flag2_BadPFMuonFilter;
    //TBranch        *b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v;
    //TBranch        *b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v;
    TBranch        *b_HT;
    TBranch        *b_MinJetMetDPhi;
    TBranch        *b_nCHSJets;
    TBranch        *b_nCHSFatJets;
    TBranch        *b_nElectrons;
    TBranch        *b_nMuons;
    TBranch        *b_nPhotons;
    TBranch        *b_nTaus;
    TBranch        *b_nPFCandidates;
    TBranch        *b_nPFCandidatesTrack;  
    //TBranch        *b_nLLPInCalo;

    inTree->SetBranchAddress("Jets",              &Jets,              &b_Jets);
    inTree->SetBranchAddress("FatJets",           &FatJets,           &b_FatJets);
    inTree->SetBranchAddress("PFCandidates"   ,   &PFCandidates,      &b_PFCandidates);
    inTree->SetBranchAddress("MEt",&MEt, &b_MEt);//the branch part seems kinda useless
    inTree->SetBranchAddress("EventNumber",       &EventNumber,       &b_EventNumber);
    inTree->SetBranchAddress("RunNumber",         &RunNumber,         &b_RunNumber);
    inTree->SetBranchAddress("LumiNumber",        &LumiNumber,        &b_LumiNumber);
    inTree->SetBranchAddress("EventWeight",       &EventWeight,       &b_EventWeight);
    inTree->SetBranchAddress("isMC",              &isMC,              &b_isMC);
    inTree->SetBranchAddress("isVBF",             &isVBF,             &b_isVBF);
    inTree->SetBranchAddress("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v, &b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v);
    inTree->SetBranchAddress("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v, &b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v);
    inTree->SetBranchAddress("Flag2_globalSuperTightHalo2016Filter", &Flag2_globalSuperTightHalo2016Filter, &b_Flag2_globalSuperTightHalo2016Filter);
    inTree->SetBranchAddress("Flag2_goodVertices", &Flag2_goodVertices, &b_Flag2_goodVertices);
    inTree->SetBranchAddress("Flag2_EcalDeadCellTriggerPrimitiveFilter", &Flag2_EcalDeadCellTriggerPrimitiveFilter, &b_Flag2_EcalDeadCellTriggerPrimitiveFilter);
    inTree->SetBranchAddress("Flag2_HBHENoiseFilter", &Flag2_HBHENoiseFilter, &b_Flag2_HBHENoiseFilter);
    inTree->SetBranchAddress("Flag2_HBHEIsoNoiseFilter", &Flag2_HBHEIsoNoiseFilter, &b_Flag2_HBHEIsoNoiseFilter);
    inTree->SetBranchAddress("Flag2_ecalBadCalibFilter", &Flag2_ecalBadCalibFilter, &b_Flag2_ecalBadCalibFilter);
    inTree->SetBranchAddress("Flag2_eeBadScFilter", &Flag2_eeBadScFilter, &b_Flag2_eeBadScFilter);
    inTree->SetBranchAddress("Flag2_BadPFMuonFilter", &Flag2_BadPFMuonFilter, &b_Flag2_BadPFMuonFilter);

    //inTree->SetBranchAddress(b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v);
    //inTree->SetBranchAddress(b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v);
    inTree->SetBranchAddress("HT",                &HT,                &b_HT);
    inTree->SetBranchAddress("MinJetMetDPhi",     &MinJetMetDPhi,     &b_MinJetMetDPhi);
    inTree->SetBranchAddress("nCHSJets",          &nCHSJets,          &b_nCHSJets);
    inTree->SetBranchAddress("nCHSFatJets",       &nCHSFatJets,       &b_nCHSFatJets);
    inTree->SetBranchAddress("nElectrons",        &nElectrons,        &b_nElectrons);
    inTree->SetBranchAddress("nMuons",            &nMuons,            &b_nMuons);
    inTree->SetBranchAddress("nPhotons",          &nPhotons,          &b_nPhotons);
    inTree->SetBranchAddress("nTaus",             &nTaus,             &b_nTaus);
    inTree->SetBranchAddress("nPFCandidates",     &nPFCandidates,     &b_nPFCandidates);
    inTree->SetBranchAddress("nPFCandidatesTrack", &nPFCandidatesTrack, &b_nPFCandidatesTrack);
    //inTree->SetBranchAddress("nLLPInCalo", &nLLPInCalo, &b_nLLPInCalo);

    
    


    // =================
    // Output
    // =================

    TFile *outFile = TFile::Open(outFilename.data(),"RECREATE", "", 207);
    TTree *outTree = new TTree("skim", "skim");
    

    // Output variables
    //std::map<int, JetType> JetMap;
    //std::map<std::pair<int,int>, PFCandidateType> PFCandidateMap;
    std::vector<PFCandidateType> Jet_0_PFCandidates;
    std::vector<PFCandidateType> Jet_1_PFCandidates;
    std::vector<PFCandidateType> Jet_2_PFCandidates;
    std::vector<PFCandidateType> Jet_3_PFCandidates;
    std::vector<PFCandidateType> Jet_4_PFCandidates;
    std::vector<PFCandidateType> Jet_5_PFCandidates;
    std::vector<PFCandidateType> Jet_6_PFCandidates;
    std::vector<PFCandidateType> Jet_7_PFCandidates;
    std::vector<PFCandidateType> Jet_8_PFCandidates;
    std::vector<PFCandidateType> Jet_9_PFCandidates;

    std::vector<JetType>    skimmedJets;
    std::vector<FatJetType> skimmedFatJets;

    std::vector<double> timeJets;
    std::vector<double> timeFatJets;
    std::vector<double> timePF;
    double averageTimeJets;
    double averageTimeFatJets;
    double averageTimePF;

    //int MaxNumJets = 10;
    //int MaxNumPFCandidates = 100;
    int nCHSJetsAcceptanceCalo;
    int nCHSFatJetsAcceptanceCalo;
        
    // Output branches    
    outTree->Branch("EventNumber",       &EventNumber,       "EventNumber/I");
    outTree->Branch("RunNumber",         &RunNumber,         "RunNumber/I");
    outTree->Branch("LumiNumber",        &LumiNumber,        "LumiNumber/I");
    outTree->Branch("EventWeight",       &EventWeight,       "EventWeight/F");
    outTree->Branch("isMC",              &isMC,              "isMC/O");
    outTree->Branch("isVBF",             &isVBF,             "isVBF/O");
    outTree->Branch("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v/O");
    outTree->Branch("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v/O");
    //outTree->Branch("Flag2_globalSuperTightHalo2016Filter", &Flag2_globalSuperTightHalo2016Filter, "Flag2_globalSuperTightHalo2016Filter/O");
    //outTree->Branch("Flag2_goodVertices", &Flag2_goodVertices, "Flag2_goodVertices/O");
    //outTree->Branch("Flag2_EcalDeadCellTriggerPrimitiveFilter", &Flag2_EcalDeadCellTriggerPrimitiveFilter, "Flag2_EcalDeadCellTriggerPrimitiveFilter/O");
    //outTree->Branch("Flag2_HBHENoiseFilter", &Flag2_HBHENoiseFilter, "Flag2_HBHENoiseFilter/O");
    //outTree->Branch("Flag2_HBHEIsoNoiseFilter", &Flag2_HBHEIsoNoiseFilter, "Flag2_HBHEIsoNoiseFilter/O");
    //outTree->Branch("Flag2_ecalBadCalibFilter", &Flag2_ecalBadCalibFilter, "Flag2_ecalBadCalibFilter/O");
    //outTree->Branch("Flag2_eeBadScFilter", &Flag2_eeBadScFilter, "Flag2_eeBadScFilter/O");
    //outTree->Branch("Flag2_BadPFMuonFilter", &Flag2_BadPFMuonFilter, "Flag2_BadPFMuonFilter/O");
    outTree->Branch("HT",                &HT,                "HT/F");
    outTree->Branch("MinJetMetDPhi",     &MinJetMetDPhi,     "MinJetMetDPhi/F");
    outTree->Branch("nCHSJets",          &nCHSJets,          "nCHSJets/I");
    outTree->Branch("nCHSFatJets",       &nCHSFatJets,       "nCHSFatJets/I");
    outTree->Branch("nCHSJetsAcceptanceCalo",          &nCHSJetsAcceptanceCalo,          "nCHSJetsAcceptanceCalo/I");
    outTree->Branch("nCHSFatJetsAcceptanceCalo",       &nCHSFatJetsAcceptanceCalo,       "nCHSFatJetsAcceptanceCalo/I");
    outTree->Branch("nElectrons",        &nElectrons,        "nElectrons/I");
    outTree->Branch("nMuons",            &nMuons,            "nMuons/I");
    outTree->Branch("nPhotons",          &nPhotons,          "nPhotons/I");
    outTree->Branch("nTaus",             &nTaus,             "nTaus/I");
    outTree->Branch("nPFCandidates",     &nPFCandidates,     "nPFCandidates/I");
    outTree->Branch("nPFCandidatesTrack", &nPFCandidatesTrack, "nPFCandidatesTrack/I");
    //outTree->Branch("nLLPInCalo",        &nLLPInCalo,        "nLLPInCalo/I");
    
    //outTree->Branch("PFCandidates", &PFCandidates);
    outTree->Branch("Jets", &skimmedJets);
    outTree->Branch("FatJets", &skimmedFatJets);
    if(doPFCand) outTree->Branch("Jet_0_PFCandidates", &Jet_0_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_1_PFCandidates", &Jet_1_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_2_PFCandidates", &Jet_2_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_3_PFCandidates", &Jet_3_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_4_PFCandidates", &Jet_4_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_5_PFCandidates", &Jet_5_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_6_PFCandidates", &Jet_6_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_7_PFCandidates", &Jet_7_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_8_PFCandidates", &Jet_8_PFCandidates);
    if(doPFCand) outTree->Branch("Jet_9_PFCandidates", &Jet_9_PFCandidates);
    outTree->Branch("MEt", &MEt);
    
    // =================
    // Event loop
    // =================


    Long64_t start_loop;
    Long64_t stop_loop;
    start_loop = first_event>-1 ? first_event : 0;
    stop_loop = last_event>-1  ? last_event : inTree->GetEntriesFast();
    //for (Long64_t entry=0; entry<inTree->GetEntriesFast(); entry++) {
    std::cout << "Events in tree: " << inTree->GetEntriesFast() << std::endl;
    for (Long64_t entry=start_loop; entry<inTree->GetEntriesFast() && entry<stop_loop; entry++) {
    //std::cout << inTree->GetEntriesFast() << std::endl;
    //for (Long64_t entry=0; entry<10; entry++) {

	//Default values
        nCHSJetsAcceptanceCalo = 0;
        nCHSFatJetsAcceptanceCalo = 0;

        inTree->GetEntry(entry);

        //std::cout << "======== " << std::endl;
        //std::cout << "Event " << entry << std::endl;
        //std::cout << "======== " << std::endl;
        if(!HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) continue;
        if(nCHSJets<1 and nCHSFatJets<1) continue;
        if(nElectrons>0) continue;
        if(nPhotons>0) continue;
        if(nMuons>0) continue;
        if(nTaus>0) continue;
	//MET filters v2
	if(!Flag2_globalSuperTightHalo2016Filter) continue;
	if(!Flag2_EcalDeadCellTriggerPrimitiveFilter) continue;
	if(!Flag2_HBHENoiseFilter) continue;
	if(!Flag2_HBHEIsoNoiseFilter) continue;
	if(!Flag2_ecalBadCalibFilter) continue;
	if(!Flag2_eeBadScFilter) continue;
	if(!Flag2_BadPFMuonFilter) continue;
	if(HT<100) continue;
	if(MEt->pt<200) continue;
      
        if(entry % 1000 == 0) 
          {
            std::cout << "======== " << std::endl;
            std::cout << "Entry n. " << entry << " passed pre-selections"  << std::endl;
            std::cout << "======== " << std::endl;
          }

	//Here: apply acceptance cuts to calo jets and fat jets
        auto befJets = std::chrono::system_clock::now();
        std::vector<int> validJetIndex;
	for (Int_t j=0; j<Jets->size(); j++)
	  {
	    if( fabs(Jets->at(j).eta)<1.48 and Jets->at(j).timeRecHitsEB>-100. and Jets->at(j).timeRecHitsHB>-100.)
	      {
                nCHSJetsAcceptanceCalo++;
		skimmedJets.push_back(Jets->at(j));
                validJetIndex.push_back(j);
	      }
          }
        auto befFatJets = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_jets = befFatJets-befJets;
        timeJets.push_back(elapsed_jets.count());

	for (Int_t j=0; j<FatJets->size(); j++)
	  {
	    if( fabs(FatJets->at(j).eta)<1.48 and FatJets->at(j).timeRecHitsEB>-100. and FatJets->at(j).timeRecHitsHB>-100.)
	      {
                nCHSFatJetsAcceptanceCalo++;
		skimmedFatJets.push_back(FatJets->at(j));
	      }
          }

        auto befPF = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_Fatjets = befPF-befFatJets;
        timeFatJets.push_back(elapsed_Fatjets.count());

	if(nCHSJetsAcceptanceCalo==0 and nCHSFatJetsAcceptanceCalo==0) continue;

        //Sort PF candidates by their pt
	if(doPFCand and nCHSJetsAcceptanceCalo>0)
	  {
	    std::sort(PFCandidates->begin(), PFCandidates->end(), pt_sorter);

            //New jet loop

            
	    for(Int_t p=0; p<PFCandidates->size(); p++)
               {

                 for (Int_t j=0; j<validJetIndex.size(); j++)
                  {                
                      if(PFCandidates->at(p).jetIndex==validJetIndex.at(j))
		        {
		          //pf_index++;
		          if(validJetIndex.at(j)==0)
		            {
			      //std::cout << PFCandidates->at(p).pt << std::endl;
			      Jet_0_PFCandidates.push_back(PFCandidates->at(p));
		            }
		          else if(validJetIndex.at(j)==1) Jet_1_PFCandidates.push_back(PFCandidates->at(p));
		          else if(validJetIndex.at(j)==2) Jet_2_PFCandidates.push_back(PFCandidates->at(p));
  		          else if(validJetIndex.at(j)==3) Jet_3_PFCandidates.push_back(PFCandidates->at(p));
  		          else if(validJetIndex.at(j)==4) Jet_4_PFCandidates.push_back(PFCandidates->at(p));
		          else if(validJetIndex.at(j)==5) Jet_5_PFCandidates.push_back(PFCandidates->at(p));
		          else if(validJetIndex.at(j)==6) Jet_6_PFCandidates.push_back(PFCandidates->at(p));
		          else if(validJetIndex.at(j)==7) Jet_7_PFCandidates.push_back(PFCandidates->at(p));
		          else if(validJetIndex.at(j)==8) Jet_8_PFCandidates.push_back(PFCandidates->at(p));
		          else if(validJetIndex.at(j)==9) Jet_9_PFCandidates.push_back(PFCandidates->at(p));
		        }//check pf cand and jet indices
	            }//loop on jet indices 


            }//loop on pf candidates
            


	    // Jet loop
            /*
	    for (Int_t j=0; j<Jets->size(); j++)
            {
        
	      //Here: jet in acceptance condition missing before moving to pf matching!
              if( fabs(Jets->at(j).eta)<1.48 and Jets->at(j).timeRecHitsEB>-100. and Jets->at(j).timeRecHitsHB>-100.)
                {
                  //std::cout << "Jet index: " << j << std::endl;

    	          //JetMap[j] = skimmedJets->at(j);
	          //int pf_index = -1;
	          for(Int_t p=0; p<PFCandidates->size(); p++)
                    {
                
                      if(PFCandidates->at(p).jetIndex==j)
		        {
		          //pf_index++;
		          if(j==0)
		            {
			      //std::cout << PFCandidates->at(p).pt << std::endl;
			      Jet_0_PFCandidates.push_back(PFCandidates->at(p));
		            }
		          else if(j==1) Jet_1_PFCandidates.push_back(PFCandidates->at(p));
		          else if(j==2) Jet_2_PFCandidates.push_back(PFCandidates->at(p));
  		          else if(j==3) Jet_3_PFCandidates.push_back(PFCandidates->at(p));
  		          else if(j==4) Jet_4_PFCandidates.push_back(PFCandidates->at(p));
		          else if(j==5) Jet_5_PFCandidates.push_back(PFCandidates->at(p));
		          else if(j==6) Jet_6_PFCandidates.push_back(PFCandidates->at(p));
		          else if(j==7) Jet_7_PFCandidates.push_back(PFCandidates->at(p));
		          else if(j==8) Jet_8_PFCandidates.push_back(PFCandidates->at(p));
		          else if(j==9) Jet_9_PFCandidates.push_back(PFCandidates->at(p));
		        }//check pf cand and jet indices
	            }//loop on pf cand   
	        }//jet selection

            }//loop on jets
            */
            

	  }//doPfCandidates


        auto befFill = std::chrono::system_clock::now();
        std::chrono::duration<double> elapsed_PF = befFill-befPF;
        timePF.push_back(elapsed_PF.count());

	outTree->Fill();

	skimmedJets.clear();
	skimmedFatJets.clear();
	Jet_0_PFCandidates.clear();
	Jet_1_PFCandidates.clear();
	Jet_2_PFCandidates.clear();
	Jet_3_PFCandidates.clear();
	Jet_4_PFCandidates.clear();
	Jet_5_PFCandidates.clear();
	Jet_6_PFCandidates.clear();
	Jet_7_PFCandidates.clear();
	Jet_8_PFCandidates.clear();
	Jet_9_PFCandidates.clear();        
        
	    
    } // End of event loop


    outTree->SetWeight(tree_weight);
    counter->Write();
    outFile->Write();
    auto end = std::chrono::system_clock::now();//time!
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    averageTimeJets = avg(timeJets);
    averageTimeFatJets = avg(timeFatJets);
    averageTimePF = avg(timePF);

    std::cout << "**************************************************" << std::endl;
    std::cout << "finished  computations at " << std::ctime(&end_time)
		  << "jet average time: " << averageTimeJets << "\n"
		  << "fat jet average time: " << averageTimeFatJets << "\n"
		  << "PF average time: " << averageTimePF << "\n"
		  << "elapsed time: " << elapsed_seconds.count() << "s\n";
    std::cout << "**************************************************" << std::endl;

}
