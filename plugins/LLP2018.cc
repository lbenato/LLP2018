// -*- C++ -*-
//
// Package:    Analyzer/LLP2018
// Class:      LLP2018
//
/**\class LLP2018 LLP2018.cc Analyzer/LLP2018/plugins/LLP2018.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Lisa Benato
//         Created:  Thu, 19 Dec 2019 18:29:45 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/PatCandidates/interface/Conversion.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/PatCandidates/interface/VIDCutFlowResult.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"


//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.


using reco::TrackCollection;

class LLP2018 : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit LLP2018(const edm::ParameterSet&);
      ~LLP2018();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      //edm::EDGetTokenT<TrackCollection> tracksToken_;  //used to select what tracks to read from configuration file
      edm::EDGetTokenT<std::vector<pat::Electron>> electronToken_;  //used to select what tracks to read from configuration file
      std::string EleVetoIdMapToken;
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
LLP2018::LLP2018(const edm::ParameterSet& iConfig)
 :
  //tracksToken_(consumes<TrackCollection>(iConfig.getUntrackedParameter<edm::InputTag>("tracks"))),
  electronToken_(consumes< std::vector<pat::Electron> >(iConfig.getUntrackedParameter<edm::InputTag>("electrons"))),
  EleVetoIdMapToken(iConfig.getUntrackedParameter<std::string>("eleVetoIdMap"))
{
   //now do what ever initialization is needed

}


LLP2018::~LLP2018()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
LLP2018::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   /*
    Handle<TrackCollection> tracks;
    iEvent.getByToken(tracksToken_, tracks);
    for(TrackCollection::const_iterator itTrack = tracks->begin();
        itTrack != tracks->end();
        ++itTrack) {
      // do something with track parameters, e.g, plot the charge.
      // int charge = itTrack->charge();
    }
   */

    std::vector<pat::Electron> Vect;
    // Declare and open collection                                                                                                                                         
    edm::Handle<std::vector<pat::Electron> > EleCollection;
    iEvent.getByToken(electronToken_, EleCollection);

    //edm::Handle<edm::ValueMap<bool> > VetoIdDecisions;
    //iEvent.getByToken(EleVetoIdMapToken, VetoIdDecisions);

    //unsigned int elIdx = 0;

    for(std::vector<pat::Electron>::const_iterator it=EleCollection->begin(); it!=EleCollection->end(); ++it) {
      pat::Electron el=*it;
      //pat::ElectronRef elRef(EleCollection, elIdx);
      //bool isPassVeto = (*VetoIdDecisions)[elRef];
      //el.addUserInt("isVeto", isPassVeto ? 1 : 0);
      std::cout<<"el is veto: " << el.electronID(EleVetoIdMapToken) << std::endl;
    }


#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif

#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void
LLP2018::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
LLP2018::endJob()
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LLP2018::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(LLP2018);
