// -*- C++ -*-
//
// Package:    test/ModelAnalyzer
// Class:      ModelAnalyzer
//
/**\class ModelAnalyzer ModelAnalyzer.cc test/ModelAnalyzer/plugins/ModelAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Karla Josefina Pena Rodriguez
//         Created:  Thu, 24 Mar 2022 19:59:55 GMT
//
//


// system include files
#include <memory>
#include <string>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TTree.h"

#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"


//
// class declaration
//

class ModelAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit ModelAnalyzer(const edm::ParameterSet&);
      ~ModelAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<GenLumiInfoHeader> genLumiHeaderToken_;
      edm::Service<TFileService> fs;
      TTree* tree;

      bool hasModelInfo_;
      long int EventNumber, LumiNumber, RunNumber;//
      float mass, ctau;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
ModelAnalyzer::ModelAnalyzer(const edm::ParameterSet& iConfig):
  genLumiHeaderToken_(consumes<GenLumiInfoHeader,edm::InLumi>(iConfig.getParameter<edm::InputTag>("genLumi"))),
  hasModelInfo_(iConfig.getParameter<bool>("hasModelInfo"))
{
  if (!hasModelInfo_) throw cms::Exception("ModelAnalyzer") << "Sample splitting needed only for samples produced with randomized parameter approach. Please check input dataset!";
   //now do what ever initialization is needed
   usesResource("TFileService");
}


ModelAnalyzer::~ModelAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void ModelAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

  // Get model name
  edm::Handle<GenLumiInfoHeader> gen_header;
  iEvent.getLuminosityBlock().getByToken(genLumiHeaderToken_,gen_header);
  std::string model = gen_header->configDescription();

  // Get LLP mass
  std::size_t start = model.find("MS-")+3;//Make string configurable (and add its length)
  std::size_t length = model.find("_", start) - start;
  std::string mass_string = model.substr(start, length);

  // Get LLP lifetime
  start = model.find("ctauS-")+6;//Make string configurable (and add its length)
  length = model.find("_", start) - start;
  std::string ctau_string = model.substr(start, length);

  // Replace lifetime decimal point ("p" with ".")
  start = ctau_string.find("p");
  if (start != std::string::npos) ctau_string.replace(start, 1, ".");

  // Event info
  EventNumber = iEvent.id().event();
  LumiNumber = iEvent.luminosityBlock();
  RunNumber = iEvent.id().run();

  // Signal point
  mass = std::stof(mass_string);
  ctau = std::stof(ctau_string);

  // Debugging:
  // if (start != std::string::npos) std::cout << "Model: " << model << ", mass: " << mass << ", ctau: " << ctau << std::endl;
  // if (start != std::string::npos) throw cms::Exception("ModelAnalyzer") << "Found p!";

  // Fill!
  tree->Fill();

}


// ------------ method called once each job just before starting event loop  ------------
void ModelAnalyzer::beginJob() {
  tree = fs->make<TTree>("tree", "tree");

  tree->Branch("EventNumber", &EventNumber, "EventNumber/L");
  tree->Branch("LumiNumber", &LumiNumber, "LumiNumber/L");
  tree->Branch("RunNumber", &RunNumber, "RunNumber/L");

  tree->Branch("mass" , &mass , "mass/F");
  tree->Branch("ctau" , &ctau , "ctau/F");
}

// ------------ method called once each job just after ending the event loop  ------------
void ModelAnalyzer::endJob() {
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void ModelAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("genLumi",edm::InputTag("generator"));
  desc.add<bool>("hasModelInfo", true);
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ModelAnalyzer);
