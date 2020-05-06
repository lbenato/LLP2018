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

void skimJets(
                 std::string inFilename=
		 "output.root",
		 //"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC.root",
                 //"GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC.root",
                 //"/nfs/dust/cms/group/cms-llp/test_calo_AOD_pfcand/WW_TuneCP5_13TeV-pythia8-v2.root",//
                 std::string outFilename=
		 //"/nfs/dust/cms/group/cms-llp/test_calo_AOD_pfcand/Skim/GluGluH2_H2ToSSTobbbb_MH-1000_MS-150_ctauS-1000_TuneCP5_13TeV-pythia8_PRIVATE-MC.root"
		 "output_4ML.root"
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
    //Bool_t   HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v;
    //Bool_t   HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v;
    Float_t  HT;
    Float_t  MinJetMetDPhi;
    Long64_t nCHSJets;
    Int_t    nElectrons;
    Int_t    nMuons;
    Int_t    nPhotons;
    Int_t    nTaus;
    Int_t    nPFCandidates;
    Int_t    nPFCandidatesTrack;

    std::vector<JetType>         *Jets = 0;
    std::vector<PFCandidateType> *PFCandidates = 0;
    MEtType                      *MEt = 0;

    // Input branches
    TBranch        *b_Jets = 0;
    TBranch        *b_PFCandidates = 0;
    TBranch        *b_MEt = 0;
    TBranch        *b_EventNumber;
    TBranch        *b_RunNumber;
    TBranch        *b_LumiNumber;
    TBranch        *b_metpt;
    TBranch        *b_EventWeight;
    TBranch        *b_isMC;
    TBranch        *b_isVBF;
    TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v;
    TBranch        *b_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v;
    //TBranch        *b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v;
    //TBranch        *b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v;
    TBranch        *b_HT;
    TBranch        *b_MinJetMetDPhi;
    TBranch        *b_nCHSJets;
    TBranch        *b_nElectrons;
    TBranch        *b_nMuons;
    TBranch        *b_nPhotons;
    TBranch        *b_nTaus;
    TBranch        *b_nPFCandidates;
    TBranch        *b_nPFCandidatesTrack;  

    inTree->SetBranchAddress("Jets",              &Jets,              &b_Jets);
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
    //inTree->SetBranchAddress(b_HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v);
    //inTree->SetBranchAddress(b_HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v);
    inTree->SetBranchAddress("HT",                &HT,                &b_HT);
    inTree->SetBranchAddress("MinJetMetDPhi",     &MinJetMetDPhi,     &b_MinJetMetDPhi);
    inTree->SetBranchAddress("nCHSJets",          &nCHSJets,          &b_nCHSJets);
    inTree->SetBranchAddress("nElectrons",        &nElectrons,        &b_nElectrons);
    inTree->SetBranchAddress("nMuons",            &nMuons,            &b_nMuons);
    inTree->SetBranchAddress("nPhotons",          &nPhotons,          &b_nPhotons);
    inTree->SetBranchAddress("nTaus",             &nTaus,             &b_nTaus);
    inTree->SetBranchAddress("nPFCandidates",     &nPFCandidates,     &b_nPFCandidates);
    inTree->SetBranchAddress("nPFCandidatesTrack", &nPFCandidatesTrack, &b_nPFCandidatesTrack);
    
    


    // =================
    // Output
    // =================

    TFile *outFile = TFile::Open(outFilename.data(),"RECREATE");
    TTree *outTree = new TTree("skim", "skim");
    

    // Output variables
    std::map<int, JetType> JetMap;
    std::map<std::pair<int,int>, PFCandidateType> PFCandidateMap;
    //std::vector<PFCandidateType> *SortedPFCandidates;
    int MaxNumJets = 10;
    int MaxNumPFCandidates = 100;
    
    //initialize maps
    for(int j = 0; j < MaxNumJets; j++) JetMap[j] = JetType();
    //initialize a large map
    for(int j = 0; j < MaxNumJets; j++)
    {
        for(int p = 0; p < MaxNumPFCandidates; p++) PFCandidateMap[std::make_pair(j,p)] = PFCandidateType();
    }
    
    // Output branches    
    outTree->Branch("EventNumber",       &EventNumber,       "EventNumber/I");
    outTree->Branch("RunNumber",         &RunNumber,         "RunNumber/I");
    outTree->Branch("LumiNumber",        &LumiNumber,        "LumiNumber/I");
    outTree->Branch("EventWeight",       &EventWeight,       "EventWeight/F");
    outTree->Branch("isMC",              &isMC,              "isMC/O");
    outTree->Branch("isVBF",             &isVBF,             "isVBF/O");
    outTree->Branch("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v/O");
    outTree->Branch("HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v", &HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v, "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v/O");
    outTree->Branch("HT",                &HT,                "HT/F");
    outTree->Branch("MinJetMetDPhi",     &MinJetMetDPhi,     "MinJetMetDPhi/F");
    outTree->Branch("nCHSJets",          &nCHSJets,          "nCHSJets/I");
    outTree->Branch("nElectrons",        &nElectrons,        "nElectrons/I");
    outTree->Branch("nMuons",            &nMuons,            "nMuons/I");
    outTree->Branch("nPhotons",          &nPhotons,          "nPhotons/I");
    outTree->Branch("nTaus",             &nTaus,             "nTaus/I");
    outTree->Branch("nPFCandidates",     &nPFCandidates,     "nPFCandidates/I");
    outTree->Branch("nPFCandidatesTrack", &nPFCandidatesTrack, "nPFCandidatesTrack/I");
    
    //outTree->Branch("PFCandidates", &PFCandidates);
    //outTree->Branch("Jets", &Jets);
    outTree->Branch("MEt", &MEt);
    
    for(auto it = JetMap.begin(); it != JetMap.end(); it++)
    {
        outTree->Branch( ("Jet_"+std::to_string(it->first)).c_str(), &it->second);
    }
    for(int j = 0; j < MaxNumJets; j++)
    {
        for(int p = 0; p < MaxNumPFCandidates; p++)
        {
            outTree->Branch( ("Jet_"+std::to_string(j)+"_PFCandidate_"+std::to_string(p)).c_str(), &PFCandidateMap[std::make_pair(j,p)] );
        }
    }
    // =================
    // Event loop
    // =================

    for (Long64_t entry=0; entry<inTree->GetEntriesFast(); entry++) {
    //std::cout << inTree->GetEntriesFast() << std::endl;
    //for (Long64_t entry=0; entry<10; entry++) {
        inTree->GetEntry(entry);

        //std::cout << "======== " << std::endl;
        //std::cout << "Event " << entry << std::endl;
        //std::cout << "======== " << std::endl;
        if(!HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) continue;
        if(nCHSJets<1) continue;
        if(nElectrons>0) continue;
        if(nPhotons>0) continue;
        if(nMuons>0) continue;
        if(nTaus>0) continue;
      
        //Sort PF candidates by their pt
        std::sort(PFCandidates->begin(), PFCandidates->end(), pt_sorter);
             
        // Jet loop
        for (Int_t j=0; j<Jets->size(); j++) {
        
            JetMap[j] = Jets->at(j);
            int pf_index = -1;
            for(Int_t p=0; p<PFCandidates->size(); p++) {
                
                if(PFCandidates->at(p).jetIndex==j)
                {
                   pf_index++;
                   PFCandidateMap[std::make_pair(j,pf_index)] = PFCandidates->at(p);
                }
            }            
        }
        
        
        //check jet map
        /*
        for (auto& x: JetMap) {
            std::cout << "Jet map: " << x.first << ", nconst: " << x.second.nConstituents << ", pt: " << x.second.pt <<'\n';
        }
        
        for (auto& x: PFCandidateMap) {
            std::cout << "PFCandidate map: [" << (x.first).first <<  "," << (x.first).second << "] pt: " << x.second.pt << '\n';
        }   
        */
        
        outTree->Fill();
        
        //Clear maps
        for(int j = 0; j < MaxNumJets; j++) JetMap[j] = JetType();
        for(int j = 0; j < MaxNumJets; j++)
        {
            for(int p = 0; p < MaxNumPFCandidates; p++) PFCandidateMap[std::make_pair(j,p)] = PFCandidateType();
        }
        

    } // End of event loop


    outTree->SetWeight(tree_weight);
    counter->Write();
    outFile->Write();
    auto end = std::chrono::system_clock::now();//time!
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    std::cout << "**************************************************" << std::endl;
    std::cout << "finished  computations at " << std::ctime(&end_time)
		  << "elapsed time: " << elapsed_seconds.count() << "s\n";
    std::cout << "**************************************************" << std::endl;

}
