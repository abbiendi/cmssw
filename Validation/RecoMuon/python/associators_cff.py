import FWCore.ParameterSet.Config as cms

# Track selector
from Validation.RecoMuon.selectors_cff import *

# TrackAssociation
from SimTracker.TrackAssociatorProducers.trackAssociatorByChi2_cfi import *
import SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi

trackAssociatorByHits = SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi.quickTrackAssociatorByHits.clone()

onlineTrackAssociatorByHits = SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi.quickTrackAssociatorByHits.clone()
onlineTrackAssociatorByHits.ThreeHitTracksAreSpecial = False

# select probeTracks from generalTracks
import PhysicsTools.RecoAlgos.recoTrackSelector_cfi
probeTracks = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
#probeTracks.quality = cms.vstring('highPurity')
#probeTracks.quality = cms.vstring('loose'),
probeTracks.tip = 3.5
probeTracks.lip = 30.
probeTracks.ptMin = 4.0
probeTracks.minRapidity = -2.4
probeTracks.maxRapidity = 2.4
probeTracks_seq = cms.Sequence( probeTracks )

#
# quickTrackAssociatorByHits on probeTracks used as monitor wrt MuonAssociatorByHits
#
tpToTkmuTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.InputTag('trackAssociatorByHits'),
    label_tp = cms.InputTag('mix', 'MergedTrackTruth'),
#    label_tr = cms.InputTag('generalTracks')
    label_tr = cms.InputTag('probeTracks')
)

#
# Configuration for Seed track extractor
#
import SimMuon.MCTruth.SeedToTrackProducer_cfi
seedsOfSTAmuons = SimMuon.MCTruth.SeedToTrackProducer_cfi.SeedToTrackProducer.clone()
seedsOfSTAmuons.L2seedsCollection = cms.InputTag("ancientMuonSeed")
seedsOfSTAmuons_seq = cms.Sequence( seedsOfSTAmuons )

seedsOfDisplacedSTAmuons = SimMuon.MCTruth.SeedToTrackProducer_cfi.SeedToTrackProducer.clone()
seedsOfDisplacedSTAmuons.L2seedsCollection = cms.InputTag("displacedMuonSeeds")
seedsOfDisplacedSTAmuons_seq = cms.Sequence( seedsOfDisplacedSTAmuons )

#
# MuonAssociatorByHits used for all track collections
#
import SimMuon.MCTruth.MuonAssociatorByHits_cfi
MABH = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
# DEFAULTS ###################################
#    EfficiencyCut_track = cms.double(0.),
#    PurityCut_track = cms.double(0.),
#    EfficiencyCut_muon = cms.double(0.),
#    PurityCut_muon = cms.double(0.),
#    includeZeroHitMuons = cms.bool(True),
#    acceptOneStubMatchings = cms.bool(False),
##############################################
MABH.EfficiencyCut_track = 0.5
MABH.PurityCut_track = 0.75
#MABH.EfficiencyCut_muon = 0.5
MABH.EfficiencyCut_muon = 0.     # for high pt muons this should be a better choice
MABH.PurityCut_muon = 0.75
MABH.includeZeroHitMuons = False
#
MABH_hlt = MABH.clone()
MABH_hlt.DTrechitTag = 'hltDt1DRecHits'
MABH_hlt.ignoreMissingTrackCollection = True
################################################

tpToTkMuonAssociation = MABH.clone()
#tpToTkMuonAssociation.tracksTag = 'generalTracks'
tpToTkMuonAssociation.tracksTag ='probeTracks'
tpToTkMuonAssociation.UseTracker = True
tpToTkMuonAssociation.UseMuon = False

tpToStaSeedAssociation = MABH.clone()
tpToStaSeedAssociation.tracksTag = 'seedsOfSTAmuons'
tpToStaSeedAssociation.UseTracker = False
tpToStaSeedAssociation.UseMuon = True

tpToStaMuonAssociation = MABH.clone()
tpToStaMuonAssociation.tracksTag = 'standAloneMuons'
tpToStaMuonAssociation.UseTracker = False
tpToStaMuonAssociation.UseMuon = True

tpToStaUpdMuonAssociation = MABH.clone()
tpToStaUpdMuonAssociation.tracksTag = 'standAloneMuons:UpdatedAtVtx'
tpToStaUpdMuonAssociation.UseTracker = False
tpToStaUpdMuonAssociation.UseMuon = True

tpToGlbMuonAssociation = MABH.clone()
tpToGlbMuonAssociation.tracksTag = 'globalMuons'
tpToGlbMuonAssociation.UseTracker = True
tpToGlbMuonAssociation.UseMuon = True

tpToStaRefitMuonAssociation = MABH.clone()
tpToStaRefitMuonAssociation.tracksTag = 'refittedStandAloneMuons'
tpToStaRefitMuonAssociation.UseTracker = False
tpToStaRefitMuonAssociation.UseMuon = True

tpToStaRefitUpdMuonAssociation = MABH.clone()
tpToStaRefitUpdMuonAssociation.tracksTag = 'refittedStandAloneMuons:UpdatedAtVtx'
tpToStaRefitUpdMuonAssociation.UseTracker = False
tpToStaRefitUpdMuonAssociation.UseMuon = True

tpToDisplacedTrkMuonAssociation = MABH.clone()
tpToDisplacedTrkMuonAssociation.tracksTag = 'displacedTracks'
tpToDisplacedTrkMuonAssociation.UseTracker = True
tpToDisplacedTrkMuonAssociation.UseMuon = False

tpToDisplacedStaSeedAssociation = MABH.clone()
tpToDisplacedStaSeedAssociation.tracksTag = 'seedsOfDisplacedSTAmuons'
tpToDisplacedStaSeedAssociation.UseTracker = False
tpToDisplacedStaSeedAssociation.UseMuon = True

tpToDisplacedStaMuonAssociation = MABH.clone()
tpToDisplacedStaMuonAssociation.tracksTag = 'displacedStandAloneMuons'
tpToDisplacedStaMuonAssociation.UseTracker = False
tpToDisplacedStaMuonAssociation.UseMuon = True

tpToDisplacedGlbMuonAssociation = MABH.clone()
tpToDisplacedGlbMuonAssociation.tracksTag = 'displacedGlobalMuons'
tpToDisplacedGlbMuonAssociation.UseTracker = True
tpToDisplacedGlbMuonAssociation.UseMuon = True

tpToStaSETMuonAssociation = MABH.clone()
tpToStaSETMuonAssociation.tracksTag = 'standAloneSETMuons'
tpToStaSETMuonAssociation.UseTracker = False
tpToStaSETMuonAssociation.UseMuon = True

tpToStaSETUpdMuonAssociation = MABH.clone()
tpToStaSETUpdMuonAssociation.tracksTag = 'standAloneSETMuons:UpdatedAtVtx'
tpToStaSETUpdMuonAssociation.UseTracker = False
tpToStaSETUpdMuonAssociation.UseMuon = True

tpToGlbSETMuonAssociation = MABH.clone()
tpToGlbSETMuonAssociation.tracksTag = 'globalSETMuons'
tpToGlbSETMuonAssociation.UseTracker = True
tpToGlbSETMuonAssociation.UseMuon = True

tpToTevFirstMuonAssociation = MABH.clone()
tpToTevFirstMuonAssociation.tracksTag = 'tevMuons:firstHit'
tpToTevFirstMuonAssociation.UseTracker = True
tpToTevFirstMuonAssociation.UseMuon = True

tpToTevPickyMuonAssociation = MABH.clone()
tpToTevPickyMuonAssociation.tracksTag = 'tevMuons:picky'
tpToTevPickyMuonAssociation.UseTracker = True
tpToTevPickyMuonAssociation.UseMuon = True

tpToTevDytMuonAssociation = MABH.clone()
tpToTevDytMuonAssociation.tracksTag = 'tevMuons:dyt'
tpToTevDytMuonAssociation.UseTracker = True
tpToTevDytMuonAssociation.UseMuon = True

tpToL3TkMuonAssociation = MABH_hlt.clone()
tpToL3TkMuonAssociation.tracksTag = 'hltL3TkTracksFromL2'
tpToL3TkMuonAssociation.UseTracker = True
tpToL3TkMuonAssociation.UseMuon = False

tpToL2MuonAssociation = MABH_hlt.clone()
tpToL2MuonAssociation.tracksTag = 'hltL2Muons'
tpToL2MuonAssociation.UseTracker = False
tpToL2MuonAssociation.UseMuon = True

tpToL2UpdMuonAssociation = MABH_hlt.clone()
tpToL2UpdMuonAssociation.tracksTag = 'hltL2Muons:UpdatedAtVtx'
tpToL2UpdMuonAssociation.UseTracker = False
tpToL2UpdMuonAssociation.UseMuon = True

tpToL3MuonAssociation = MABH_hlt.clone()
tpToL3MuonAssociation.tracksTag = 'hltL3Muons'
tpToL3MuonAssociation.UseTracker = True
tpToL3MuonAssociation.UseMuon = True

#
# COSMICS reco
#
# 2-legs cosmics reco: simhits can be twice the reconstructed ones in any single leg
# (Quality cut have to be set at 0.25, purity cuts can stay at default value 0.75)
# T.B.D. upper and lower leg should be analyzed separately 
#
tpToTkCosmicSelMuonAssociation = MABH.clone()
tpToTkCosmicSelMuonAssociation.tracksTag = 'ctfWithMaterialTracksP5LHCNavigation'
tpToTkCosmicSelMuonAssociation.UseTracker = True
tpToTkCosmicSelMuonAssociation.UseMuon = False
tpToTkCosmicSelMuonAssociation.EfficiencyCut_track = 0.25

tpToStaCosmicSelMuonAssociation = MABH.clone()
tpToStaCosmicSelMuonAssociation.tracksTag = 'cosmicMuons'
tpToStaCosmicSelMuonAssociation.UseTracker = False
tpToStaCosmicSelMuonAssociation.UseMuon = True
tpToStaCosmicSelMuonAssociation.EfficiencyCut_muon = 0.25

tpToGlbCosmicSelMuonAssociation = MABH.clone()
tpToGlbCosmicSelMuonAssociation.tracksTag = 'globalCosmicMuons'
tpToGlbCosmicSelMuonAssociation.UseTracker = True
tpToGlbCosmicSelMuonAssociation.UseMuon = True
tpToGlbCosmicSelMuonAssociation.EfficiencyCut_track = 0.25
tpToGlbCosmicSelMuonAssociation.EfficiencyCut_muon = 0.25

# 1-leg cosmics reco
tpToTkCosmic1LegSelMuonAssociation = MABH.clone()
tpToTkCosmic1LegSelMuonAssociation.tracksTag = 'ctfWithMaterialTracksP5'
tpToTkCosmic1LegSelMuonAssociation.UseTracker = True
tpToTkCosmic1LegSelMuonAssociation.UseMuon = False

tpToStaCosmic1LegSelMuonAssociation = MABH.clone()
tpToStaCosmic1LegSelMuonAssociation.tracksTag = 'cosmicMuons1Leg'
tpToStaCosmic1LegSelMuonAssociation.UseTracker = False
tpToStaCosmic1LegSelMuonAssociation.UseMuon = True

tpToGlbCosmic1LegSelMuonAssociation = MABH.clone()
tpToGlbCosmic1LegSelMuonAssociation.tracksTag = 'globalCosmicMuons1Leg'
tpToGlbCosmic1LegSelMuonAssociation.UseTracker = True
tpToGlbCosmic1LegSelMuonAssociation.UseMuon = True

#
# The full-sim association sequences
#

muonAssociation_seq = cms.Sequence(
    probeTracks_seq+tpToTkMuonAssociation
    +trackAssociatorByHits+tpToTkmuTrackAssociation
    +seedsOfSTAmuons_seq+tpToStaSeedAssociation+tpToStaMuonAssociation+tpToStaUpdMuonAssociation
    +tpToGlbMuonAssociation
    )

muonAssociationTEV_seq = cms.Sequence(
    tpToTevFirstMuonAssociation+tpToTevPickyMuonAssociation+tpToTevDytMuonAssociation
    )

muonAssociationDisplaced_seq = cms.Sequence(
    seedsOfDisplacedSTAmuons_seq+tpToDisplacedStaSeedAssociation+tpToDisplacedStaMuonAssociation
    +tpToDisplacedTrkMuonAssociation+tpToDisplacedGlbMuonAssociation
    )

muonAssociationRefit_seq = cms.Sequence(
    tpToStaRefitMuonAssociation+tpToStaRefitUpdMuonAssociation
    )

muonAssociationSET_seq = cms.Sequence(
    tpToStaSETMuonAssociation+tpToStaSETUpdMuonAssociation+tpToGlbSETMuonAssociation
    )

muonAssociationCosmic_seq = cms.Sequence(
    tpToTkCosmicSelMuonAssociation+ tpToTkCosmic1LegSelMuonAssociation
    +tpToStaCosmicSelMuonAssociation+tpToStaCosmic1LegSelMuonAssociation
    +tpToGlbCosmicSelMuonAssociation+tpToGlbCosmic1LegSelMuonAssociation
    )

muonAssociationHLT_seq = cms.Sequence(
    tpToL2MuonAssociation+tpToL2UpdMuonAssociation+tpToL3TkMuonAssociation+tpToL3MuonAssociation
    )


# fastsim has no hlt specific dt hit collection
from Configuration.StandardSequences.Eras import eras
if eras.fastSim.isChosen():
    _DTrechitTag = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.DTrechitTag
    tpToL3TkMuonAssociation.DTrechitTag = _DTrechitTag
    tpToL2MuonAssociation.DTrechitTag = _DTrechitTag
    tpToL2UpdMuonAssociation.DTrechitTag = _DTrechitTag
    tpToL3MuonAssociation.DTrechitTag = _DTrechitTag


### special sequences for BarrelOnly and EndcapOnly
#
innerTracksBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
innerTracksBarrelOnly.src = "generalTracks"
innerTracksBarrelOnly.ptMin = 4.
innerTracksBarrelOnly.minRapidity = -0.9
innerTracksBarrelOnly.maxRapidity = 0.9

innerTracksMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
innerTracksMinusEndcapOnly.src = "generalTracks"
innerTracksMinusEndcapOnly.ptMin = 4.
innerTracksMinusEndcapOnly.minRapidity = -2.4
innerTracksMinusEndcapOnly.maxRapidity = -1.2

innerTracksPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
innerTracksPlusEndcapOnly.src = "generalTracks"
innerTracksPlusEndcapOnly.ptMin = 4.
innerTracksPlusEndcapOnly.minRapidity = 1.2
innerTracksPlusEndcapOnly.maxRapidity = 2.4

globalMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
globalMuonsBarrelOnly.src = "globalMuons"
globalMuonsBarrelOnly.ptMin = 0.
globalMuonsBarrelOnly.minRapidity = -0.9
globalMuonsBarrelOnly.maxRapidity = 0.9
globalMuonsBarrelOnly.quality = cms.vstring('')
globalMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)

globalMuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
globalMuonsMinusEndcapOnly.src = "globalMuons"
globalMuonsMinusEndcapOnly.ptMin = 0.
globalMuonsMinusEndcapOnly.minRapidity = -2.4
globalMuonsMinusEndcapOnly.maxRapidity = -1.2
globalMuonsMinusEndcapOnly.quality = cms.vstring('')
globalMuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)

globalMuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
globalMuonsPlusEndcapOnly.src = "globalMuons"
globalMuonsPlusEndcapOnly.ptMin = 0.
globalMuonsPlusEndcapOnly.minRapidity = 1.2
globalMuonsPlusEndcapOnly.maxRapidity = 2.4
globalMuonsPlusEndcapOnly.quality = cms.vstring('')
globalMuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)

pickyMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
pickyMuonsBarrelOnly.src = "tevMuons:picky"
pickyMuonsBarrelOnly.ptMin = 0.
pickyMuonsBarrelOnly.minRapidity = -0.9
pickyMuonsBarrelOnly.maxRapidity = 0.9
pickyMuonsBarrelOnly.quality = cms.vstring('')
pickyMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)

pickyMuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
pickyMuonsMinusEndcapOnly.src = "tevMuons:picky"
pickyMuonsMinusEndcapOnly.ptMin = 0.
pickyMuonsMinusEndcapOnly.minRapidity = -2.4
pickyMuonsMinusEndcapOnly.maxRapidity = -1.2
pickyMuonsMinusEndcapOnly.quality = cms.vstring('')
pickyMuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)

pickyMuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
pickyMuonsPlusEndcapOnly.src = "tevMuons:picky"
pickyMuonsPlusEndcapOnly.ptMin = 0.
pickyMuonsPlusEndcapOnly.minRapidity = 1.2
pickyMuonsPlusEndcapOnly.maxRapidity = 2.4
pickyMuonsPlusEndcapOnly.quality = cms.vstring('')
pickyMuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)

staMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
staMuonsBarrelOnly.src = "standAloneMuons"
staMuonsBarrelOnly.ptMin = 0.
staMuonsBarrelOnly.minRapidity = -0.9 
staMuonsBarrelOnly.maxRapidity = 0.9
staMuonsBarrelOnly.quality = cms.vstring('')
staMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
staMuonsBarrelOnly.minHit = 0

staMuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
staMuonsMinusEndcapOnly.src = "standAloneMuons"
staMuonsMinusEndcapOnly.ptMin = 0.
staMuonsMinusEndcapOnly.minRapidity = -2.4
staMuonsMinusEndcapOnly.maxRapidity = -1.2
staMuonsMinusEndcapOnly.quality = cms.vstring('')
staMuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
staMuonsMinusEndcapOnly.minHit = 0

staMuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
staMuonsPlusEndcapOnly.src = "standAloneMuons"
staMuonsPlusEndcapOnly.ptMin = 0.
staMuonsPlusEndcapOnly.minRapidity = 1.2
staMuonsPlusEndcapOnly.maxRapidity = 2.4
staMuonsPlusEndcapOnly.quality = cms.vstring('')
staMuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
staMuonsPlusEndcapOnly.minHit = 0

staUpdMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
staUpdMuonsBarrelOnly.src = "standAloneMuons:UpdatedAtVtx"
staUpdMuonsBarrelOnly.ptMin = 0.
staUpdMuonsBarrelOnly.minRapidity = -0.9 
staUpdMuonsBarrelOnly.maxRapidity = 0.9
staUpdMuonsBarrelOnly.quality = cms.vstring('')
staUpdMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
staUpdMuonsBarrelOnly.minHit = 0

staUpdMuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
staUpdMuonsMinusEndcapOnly.src = "standAloneMuons:UpdatedAtVtx"
staUpdMuonsMinusEndcapOnly.ptMin = 0.
staUpdMuonsMinusEndcapOnly.minRapidity = -2.4
staUpdMuonsMinusEndcapOnly.maxRapidity = -1.2
staUpdMuonsMinusEndcapOnly.quality = cms.vstring('')
staUpdMuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
staUpdMuonsMinusEndcapOnly.minHit = 0

staUpdMuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
staUpdMuonsPlusEndcapOnly.src = "standAloneMuons:UpdatedAtVtx"
staUpdMuonsPlusEndcapOnly.ptMin = 0.
staUpdMuonsPlusEndcapOnly.minRapidity = 1.2 
staUpdMuonsPlusEndcapOnly.maxRapidity = 2.4
staUpdMuonsPlusEndcapOnly.quality = cms.vstring('')
staUpdMuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
staUpdMuonsPlusEndcapOnly.minHit = 0

#--- HLT
L2MuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L2MuonsBarrelOnly.src = "hltL2Muons"
L2MuonsBarrelOnly.ptMin = 0.
L2MuonsBarrelOnly.minRapidity = -0.9 
L2MuonsBarrelOnly.maxRapidity = 0.9
L2MuonsBarrelOnly.quality = cms.vstring('')
L2MuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L2MuonsBarrelOnly.minHit = 0

L2MuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L2MuonsMinusEndcapOnly.src = "hltL2Muons"
L2MuonsMinusEndcapOnly.ptMin = 0.
L2MuonsMinusEndcapOnly.minRapidity = -2.4
L2MuonsMinusEndcapOnly.maxRapidity = -1.2
L2MuonsMinusEndcapOnly.quality = cms.vstring('')
L2MuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L2MuonsMinusEndcapOnly.minHit = 0

L2MuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L2MuonsPlusEndcapOnly.src = "hltL2Muons"
L2MuonsPlusEndcapOnly.ptMin = 0.
L2MuonsPlusEndcapOnly.minRapidity = 1.2
L2MuonsPlusEndcapOnly.maxRapidity = 2.4
L2MuonsPlusEndcapOnly.quality = cms.vstring('')
L2MuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L2MuonsPlusEndcapOnly.minHit = 0

L2UpdMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L2UpdMuonsBarrelOnly.src = "hltL2Muons:UpdatedAtVtx"
L2UpdMuonsBarrelOnly.ptMin = 0.
L2UpdMuonsBarrelOnly.minRapidity = -0.9 
L2UpdMuonsBarrelOnly.maxRapidity = 0.9
L2UpdMuonsBarrelOnly.quality = cms.vstring('')
L2UpdMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L2UpdMuonsBarrelOnly.minHit = 0

L2UpdMuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L2UpdMuonsMinusEndcapOnly.src = "hltL2Muons:UpdatedAtVtx"
L2UpdMuonsMinusEndcapOnly.ptMin = 0.
L2UpdMuonsMinusEndcapOnly.minRapidity = -2.4
L2UpdMuonsMinusEndcapOnly.maxRapidity = -1.2
L2UpdMuonsMinusEndcapOnly.quality = cms.vstring('')
L2UpdMuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L2UpdMuonsMinusEndcapOnly.minHit = 0

L2UpdMuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L2UpdMuonsPlusEndcapOnly.src = "hltL2Muons:UpdatedAtVtx"
L2UpdMuonsPlusEndcapOnly.ptMin = 0.
L2UpdMuonsPlusEndcapOnly.minRapidity = 1.2
L2UpdMuonsPlusEndcapOnly.maxRapidity = 2.4
L2UpdMuonsPlusEndcapOnly.quality = cms.vstring('')
L2UpdMuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L2UpdMuonsPlusEndcapOnly.minHit = 0

L3MuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L3MuonsBarrelOnly.src = "hltL3Muons"
L3MuonsBarrelOnly.ptMin = 0.
L3MuonsBarrelOnly.minRapidity = -0.9 
L3MuonsBarrelOnly.maxRapidity = 0.9
L3MuonsBarrelOnly.quality = cms.vstring('')
L3MuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L3MuonsBarrelOnly.minHit = 0

L3MuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L3MuonsMinusEndcapOnly.src = "hltL3Muons"
L3MuonsMinusEndcapOnly.ptMin = 0.
L3MuonsMinusEndcapOnly.minRapidity = -2.4
L3MuonsMinusEndcapOnly.maxRapidity = -1.2
L3MuonsMinusEndcapOnly.quality = cms.vstring('')
L3MuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L3MuonsMinusEndcapOnly.minHit = 0

L3MuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L3MuonsPlusEndcapOnly.src = "hltL3Muons"
L3MuonsPlusEndcapOnly.ptMin = 0.
L3MuonsPlusEndcapOnly.minRapidity = 1.2
L3MuonsPlusEndcapOnly.maxRapidity = 2.4
L3MuonsPlusEndcapOnly.quality = cms.vstring('')
L3MuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L3MuonsPlusEndcapOnly.minHit = 0

L3TkMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L3TkMuonsBarrelOnly.src = "hltL3TkTracksFromL2"
L3TkMuonsBarrelOnly.ptMin = 0.
L3TkMuonsBarrelOnly.minRapidity = -0.9 
L3TkMuonsBarrelOnly.maxRapidity = 0.9
L3TkMuonsBarrelOnly.quality = cms.vstring('')
L3TkMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L3TkMuonsBarrelOnly.minHit = 0

L3TkMuonsMinusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L3TkMuonsMinusEndcapOnly.src = "hltL3TkTracksFromL2"
L3TkMuonsMinusEndcapOnly.ptMin = 0.
L3TkMuonsMinusEndcapOnly.minRapidity = -2.4
L3TkMuonsMinusEndcapOnly.maxRapidity = -1.2
L3TkMuonsMinusEndcapOnly.quality = cms.vstring('')
L3TkMuonsMinusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L3TkMuonsMinusEndcapOnly.minHit = 0

L3TkMuonsPlusEndcapOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
L3TkMuonsPlusEndcapOnly.src = "hltL3TkTracksFromL2"
L3TkMuonsPlusEndcapOnly.ptMin = 0.
L3TkMuonsPlusEndcapOnly.minRapidity = 1.2
L3TkMuonsPlusEndcapOnly.maxRapidity = 2.4
L3TkMuonsPlusEndcapOnly.quality = cms.vstring('')
L3TkMuonsPlusEndcapOnly.maxChi2 = 1e38  # def cms.double(10000.0)
L3TkMuonsPlusEndcapOnly.minHit = 0
#--- HLT

displacedStaMuonsBarrelOnly = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
displacedStaMuonsBarrelOnly.src = "displacedStandAloneMuons"
displacedStaMuonsBarrelOnly.ptMin = 0.
displacedStaMuonsBarrelOnly.minRapidity = -0.9 
displacedStaMuonsBarrelOnly.maxRapidity = 0.9
displacedStaMuonsBarrelOnly.quality = cms.vstring('')
displacedStaMuonsBarrelOnly.maxChi2 = 1e38  # def cms.double(10000.0)
displacedStaMuonsBarrelOnly.minHit = 0

tpToTkMuonAssociationBarrelOnly = MABH.clone()
tpToTkMuonAssociationBarrelOnly.tracksTag ='innerTracksBarrelOnly'
tpToTkMuonAssociationBarrelOnly.UseTracker = True
tpToTkMuonAssociationBarrelOnly.UseMuon = False

tpToGlbMuonAssociationBarrelOnly = MABH.clone()
tpToGlbMuonAssociationBarrelOnly.tracksTag = 'globalMuonsBarrelOnly'
tpToGlbMuonAssociationBarrelOnly.UseTracker = True
tpToGlbMuonAssociationBarrelOnly.UseMuon = True

tpToTevPickyMuonAssociationBarrelOnly = MABH.clone()
tpToTevPickyMuonAssociationBarrelOnly.tracksTag = 'pickyMuonsBarrelOnly'
tpToTevPickyMuonAssociationBarrelOnly.UseTracker = True
tpToTevPickyMuonAssociationBarrelOnly.UseMuon = True

tpToTkMuonAssociationMinusEndcapOnly = MABH.clone()
tpToTkMuonAssociationMinusEndcapOnly.tracksTag ='innerTracksMinusEndcapOnly'
tpToTkMuonAssociationMinusEndcapOnly.UseTracker = True
tpToTkMuonAssociationMinusEndcapOnly.UseMuon = False

tpToGlbMuonAssociationMinusEndcapOnly = MABH.clone()
tpToGlbMuonAssociationMinusEndcapOnly.tracksTag = 'globalMuonsMinusEndcapOnly'
tpToGlbMuonAssociationMinusEndcapOnly.UseTracker = True
tpToGlbMuonAssociationMinusEndcapOnly.UseMuon = True

tpToTevPickyMuonAssociationMinusEndcapOnly = MABH.clone()
tpToTevPickyMuonAssociationMinusEndcapOnly.tracksTag = 'pickyMuonsMinusEndcapOnly'
tpToTevPickyMuonAssociationMinusEndcapOnly.UseTracker = True
tpToTevPickyMuonAssociationMinusEndcapOnly.UseMuon = True

tpToTkMuonAssociationPlusEndcapOnly = MABH.clone()
tpToTkMuonAssociationPlusEndcapOnly.tracksTag ='innerTracksPlusEndcapOnly'
tpToTkMuonAssociationPlusEndcapOnly.UseTracker = True
tpToTkMuonAssociationPlusEndcapOnly.UseMuon = False

tpToGlbMuonAssociationPlusEndcapOnly = MABH.clone()
tpToGlbMuonAssociationPlusEndcapOnly.tracksTag = 'globalMuonsPlusEndcapOnly'
tpToGlbMuonAssociationPlusEndcapOnly.UseTracker = True
tpToGlbMuonAssociationPlusEndcapOnly.UseMuon = True

tpToTevPickyMuonAssociationPlusEndcapOnly = MABH.clone()
tpToTevPickyMuonAssociationPlusEndcapOnly.tracksTag = 'pickyMuonsPlusEndcapOnly'
tpToTevPickyMuonAssociationPlusEndcapOnly.UseTracker = True
tpToTevPickyMuonAssociationPlusEndcapOnly.UseMuon = True

tpToStaMuonAssociationBarrelOnly = MABH.clone() 
tpToStaMuonAssociationBarrelOnly.tracksTag = 'staMuonsBarrelOnly'
tpToStaMuonAssociationBarrelOnly.UseTracker = False
tpToStaMuonAssociationBarrelOnly.UseMuon = True

tpToUpdStaMuonAssociationBarrelOnly = MABH.clone() 
tpToUpdStaMuonAssociationBarrelOnly.tracksTag = 'staUpdMuonsBarrelOnly'
tpToUpdStaMuonAssociationBarrelOnly.UseTracker = False
tpToUpdStaMuonAssociationBarrelOnly.UseMuon = True

tpToStaMuonAssociationMinusEndcapOnly = MABH.clone() 
tpToStaMuonAssociationMinusEndcapOnly.tracksTag = 'staMuonsMinusEndcapOnly'
tpToStaMuonAssociationMinusEndcapOnly.UseTracker = False
tpToStaMuonAssociationMinusEndcapOnly.UseMuon = True

tpToUpdStaMuonAssociationMinusEndcapOnly = MABH.clone() 
tpToUpdStaMuonAssociationMinusEndcapOnly.tracksTag = 'staUpdMuonsMinusEndcapOnly'
tpToUpdStaMuonAssociationMinusEndcapOnly.UseTracker = False
tpToUpdStaMuonAssociationMinusEndcapOnly.UseMuon = True

tpToStaMuonAssociationPlusEndcapOnly = MABH.clone() 
tpToStaMuonAssociationPlusEndcapOnly.tracksTag = 'staMuonsPlusEndcapOnly'
tpToStaMuonAssociationPlusEndcapOnly.UseTracker = False
tpToStaMuonAssociationPlusEndcapOnly.UseMuon = True

tpToUpdStaMuonAssociationPlusEndcapOnly = MABH.clone() 
tpToUpdStaMuonAssociationPlusEndcapOnly.tracksTag = 'staUpdMuonsPlusEndcapOnly'
tpToUpdStaMuonAssociationPlusEndcapOnly.UseTracker = False
tpToUpdStaMuonAssociationPlusEndcapOnly.UseMuon = True

tpToL2MuonAssociationBarrelOnly = MABH_hlt.clone() 
tpToL2MuonAssociationBarrelOnly.tracksTag = 'L2MuonsBarrelOnly'
tpToL2MuonAssociationBarrelOnly.UseTracker = False
tpToL2MuonAssociationBarrelOnly.UseMuon = True

tpToL2UpdMuonAssociationBarrelOnly = MABH_hlt.clone() 
tpToL2UpdMuonAssociationBarrelOnly.tracksTag = 'L2UpdMuonsBarrelOnly'
tpToL2UpdMuonAssociationBarrelOnly.UseTracker = False
tpToL2UpdMuonAssociationBarrelOnly.UseMuon = True

tpToL2MuonAssociationMinusEndcapOnly = MABH_hlt.clone() 
tpToL2MuonAssociationMinusEndcapOnly.tracksTag = 'L2MuonsMinusEndcapOnly'
tpToL2MuonAssociationMinusEndcapOnly.UseTracker = False
tpToL2MuonAssociationMinusEndcapOnly.UseMuon = True

tpToL2UpdMuonAssociationMinusEndcapOnly = MABH_hlt.clone() 
tpToL2UpdMuonAssociationMinusEndcapOnly.tracksTag = 'L2UpdMuonsMinusEndcapOnly'
tpToL2UpdMuonAssociationMinusEndcapOnly.UseTracker = False
tpToL2UpdMuonAssociationMinusEndcapOnly.UseMuon = True

tpToL2MuonAssociationPlusEndcapOnly = MABH_hlt.clone() 
tpToL2MuonAssociationPlusEndcapOnly.tracksTag = 'L2MuonsPlusEndcapOnly'
tpToL2MuonAssociationPlusEndcapOnly.UseTracker = False
tpToL2MuonAssociationPlusEndcapOnly.UseMuon = True

tpToL2UpdMuonAssociationPlusEndcapOnly = MABH_hlt.clone() 
tpToL2UpdMuonAssociationPlusEndcapOnly.tracksTag = 'L2UpdMuonsPlusEndcapOnly'
tpToL2UpdMuonAssociationPlusEndcapOnly.UseTracker = False
tpToL2UpdMuonAssociationPlusEndcapOnly.UseMuon = True

tpToL3MuonAssociationBarrelOnly = MABH_hlt.clone() 
tpToL3MuonAssociationBarrelOnly.tracksTag = 'L3MuonsBarrelOnly'
tpToL3MuonAssociationBarrelOnly.UseTracker = True
tpToL3MuonAssociationBarrelOnly.UseMuon = True

tpToL3MuonAssociationMinusEndcapOnly = MABH_hlt.clone() 
tpToL3MuonAssociationMinusEndcapOnly.tracksTag = 'L3MuonsMinusEndcapOnly'
tpToL3MuonAssociationMinusEndcapOnly.UseTracker = True
tpToL3MuonAssociationMinusEndcapOnly.UseMuon = True

tpToL3MuonAssociationPlusEndcapOnly = MABH_hlt.clone() 
tpToL3MuonAssociationPlusEndcapOnly.tracksTag = 'L3MuonsPlusEndcapOnly'
tpToL3MuonAssociationPlusEndcapOnly.UseTracker = True
tpToL3MuonAssociationPlusEndcapOnly.UseMuon = True

tpToL3TkMuonAssociationBarrelOnly = MABH_hlt.clone() 
tpToL3TkMuonAssociationBarrelOnly.tracksTag = 'L3TkMuonsBarrelOnly'
tpToL3TkMuonAssociationBarrelOnly.UseTracker = True
tpToL3TkMuonAssociationBarrelOnly.UseMuon = False

tpToL3TkMuonAssociationMinusEndcapOnly = MABH_hlt.clone() 
tpToL3TkMuonAssociationMinusEndcapOnly.tracksTag = 'L3TkMuonsMinusEndcapOnly'
tpToL3TkMuonAssociationMinusEndcapOnly.UseTracker = True
tpToL3TkMuonAssociationMinusEndcapOnly.UseMuon = False

tpToL3TkMuonAssociationPlusEndcapOnly = MABH_hlt.clone() 
tpToL3TkMuonAssociationPlusEndcapOnly.tracksTag = 'L3TkMuonsPlusEndcapOnly'
tpToL3TkMuonAssociationPlusEndcapOnly.UseTracker = True
tpToL3TkMuonAssociationPlusEndcapOnly.UseMuon = False

tpToDisplacedStaMuonAssociationBarrelOnly = MABH.clone() 
tpToDisplacedStaMuonAssociationBarrelOnly.tracksTag = 'displacedStaMuonsBarrelOnly'
tpToDisplacedStaMuonAssociationBarrelOnly.UseTracker = False
tpToDisplacedStaMuonAssociationBarrelOnly.UseMuon = True
