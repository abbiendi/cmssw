import FWCore.ParameterSet.Config as cms

from SimTracker.TrackAssociation.LhcParametersDefinerForTP_cfi import *
from SimTracker.TrackAssociation.CosmicParametersDefinerForTP_cfi import *
from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.histoParameters_cff import *

muonTrackValidator = cms.EDAnalyzer("MuonTrackValidator",
    # define the TrackingParticleSelector for evaluation of efficiency
    muonTPSelector = cms.PSet(muonTPSet),
    # input TrackingParticle collections
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    #
    # input reco::Track collection
    label = cms.VInputTag(cms.InputTag("globalMuons")),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    #
    # set true if you do not want that MTV launch an exception
    # if the track collection is missing (e.g. HLT):
    ignoremissingtrackcollection=cms.untracked.bool(False),
    #
    # collision-like tracks
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    # cosmics tracks
    # parametersDefiner = cms.string('CosmicParametersDefinerForTP'), 
    #
    # map linking SimHits to TrackingParticles, needed for cosmics validation`
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"), 
    #
    # if !UseAssociators the association map has to be given in input 
    associators = cms.vstring('a_MuonAssociator'),
    UseAssociators = cms.bool(False),
    useGEMs = cms.bool(False),
    associatormap = cms.InputTag("tpToMuonTrackAssociation"),
    #
    # BiDirectional Logic for RecoToSim association corrects the Fake rates (counting ghosts and split tracks as fakes)
    #  setting it to False the ghost and split tracks are counted as good ones
    #  the default setting is True: should NOT be changed !
    BiDirectional_RecoToSim_association = cms.bool(True),
    #
    # Output File / Directory
    outputFile = cms.string(''),
    dirName = cms.string('Muons/RecoMuonV/MuonTrack/'),
    #
    # Parameters defining which histograms to make and their attributes (nbins, range: min, max...)
    muonHistoParameters = cms.PSet(defaultMuonHistoParameters)
)

from Configuration.StandardSequences.Eras import eras
eras.run3_GEM.toModify( muonTrackValidator, useGEMs = cms.bool(True) )
