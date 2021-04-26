#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"

#include "DataFormats/Common/interface/EDProductfwd.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticleFwd.h"


class TrackingParticleMuonRefSelector : public edm::stream::EDProducer<> {
public:
  TrackingParticleMuonRefSelector(const edm::ParameterSet &iConfig);

  //  static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  void produce(edm::Event &iEvent, const edm::EventSetup &iSetup) override;

private:
  edm::EDGetTokenT<TrackingParticleCollection> tpToken_;

};

TrackingParticleMuonRefSelector::TrackingParticleMuonRefSelector(const edm::ParameterSet &iConfig)
    : tpToken_(consumes<TrackingParticleCollection>(iConfig.getParameter<edm::InputTag>("src"))) {

  produces<TrackingParticleRefVector>();
}

//void TrackingParticleMuonRefSelector::fillDescriptions(edm::ConfigurationDescriptions &descriptions) {
//  edm::ParameterSetDescription desc;
//  desc.add<edm::InputTag>("src", edm::InputTag("mix", "MergedTrackTruth"));
//  descriptions.add("trackingParticleMuonRefSelectorDefault", desc);
//}

void TrackingParticleMuonRefSelector::produce(edm::Event &iEvent, const edm::EventSetup &iSetup) {
  edm::Handle<TrackingParticleCollection> h_tps;
  iEvent.getByToken(tpToken_, h_tps);

  auto ret = std::make_unique<TrackingParticleRefVector>();

  for (size_t i = 0, end = h_tps->size(); i < end; ++i) {
    auto tpRef = TrackingParticleRef(h_tps, i);

    // test if the TP has muon hits
    int n_hits = tpRef->numberOfHits();
    int n_tracker_hits = tpRef->numberOfTrackerHits();
    int n_muon_hits = n_hits - n_tracker_hits;

    if (n_muon_hits > 0) ret->push_back(tpRef);
  }

  iEvent.put(std::move(ret));
}

DEFINE_FWK_MODULE(TrackingParticleMuonRefSelector);
