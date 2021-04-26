import FWCore.ParameterSet.Config as cms

trackingParticlesMuon = cms.EDProducer("TrackingParticleMuonRefSelector",
   mightGet = cms.optional.untracked.vstring,
   src = cms.InputTag("mix","MergedTrackTruth")
)
