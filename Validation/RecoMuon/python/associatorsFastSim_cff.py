import FWCore.ParameterSet.Config as cms

#Track selector
from Validation.RecoMuon.selectors_cff import *

#TrackAssociation
from SimTracker.TrackAssociatorProducers.trackAssociatorByChi2_cfi import *
import SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi

trackAssociatorByHits = SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi.quickTrackAssociatorByHits.clone()

onlineTrackAssociatorByHits = SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi.quickTrackAssociatorByHits.clone()
onlineTrackAssociatorByHits.ThreeHitTracksAreSpecial = False

# select probeTracks from generalTracks
import PhysicsTools.RecoAlgos.recoTrackSelector_cfi
probeTracks = PhysicsTools.RecoAlgos.recoTrackSelector_cfi.recoTrackSelector.clone()
probeTracks.quality = cms.vstring('highPurity')
probeTracks.tip = 3.5
probeTracks.lip = 30.
probeTracks.ptMin = 4.0
probeTracks.minRapidity = -2.4
probeTracks.maxRapidity = 2.4
probeTracks_seq = cms.Sequence( probeTracks )

#
# quickTrackAssociatorByHits on probeTracks used as monitor wrt MuonAssociatorByHits
#
tpToTkmuTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.InputTag('trackAssociatorByHits'),
    label_tp = cms.InputTag('mix', 'MergedTrackTruth'),
#    label_tr = cms.InputTag('generalTracks')
    label_tr = cms.InputTag('probeTracks')
)

#
# Configuration for Muon track extractor
#
import SimMuon.MCTruth.MuonTrackProducer_cfi
extractedGlobalMuons = SimMuon.MCTruth.MuonTrackProducer_cfi.muonTrackProducer.clone()
extractedGlobalMuons.selectionTags = ('AllGlobalMuons',)
extractedGlobalMuons.trackType = "globalTrack"
extractedMuonTracks_seq = cms.Sequence( extractedGlobalMuons )

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

baseMuonAssociatorFS = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
baseMuonAssociatorFS.EfficiencyCut_track = 0.5
baseMuonAssociatorFS.PurityCut_track = 0.75
baseMuonAssociatorFS.EfficiencyCut_muon = 0.5
baseMuonAssociatorFS.PurityCut_muon = 0.75
baseMuonAssociatorFS.includeZeroHitMuons = False
baseMuonAssociatorFS.simtracksTag = "famosSimHits"
baseMuonAssociatorFS.DTsimhitsTag  = "MuonSimHits:MuonDTHits"
baseMuonAssociatorFS.CSCsimHitsTag = "MuonSimHits:MuonCSCHits"
baseMuonAssociatorFS.RPCsimhitsTag = "MuonSimHits:MuonRPCHits"
baseMuonAssociatorFS.simtracksXFTag = "mix:famosSimHits"
baseMuonAssociatorFS.DTsimhitsXFTag  = "mix:MuonSimHitsMuonDTHits"
baseMuonAssociatorFS.CSCsimHitsXFTag = "mix:MuonSimHitsMuonCSCHits"
baseMuonAssociatorFS.RPCsimhitsXFTag = "mix:MuonSimHitsMuonRPCHits"
baseMuonAssociatorFS.ROUList = ['famosSimHitsTrackerHits']

tpToTkMuonAssociationFS = baseMuonAssociatorFS.clone()
#tpToTkMuonAssociationFS.tracksTag = 'generalTracks'
tpToTkMuonAssociationFS.tracksTag = 'probeTracks'
tpToTkMuonAssociationFS.UseTracker = True
tpToTkMuonAssociationFS.UseMuon = False

tpToStaSeedAssociationFS = baseMuonAssociatorFS.clone()
tpToStaSeedAssociationFS.tracksTag = 'seedsOfSTAmuons'
tpToStaSeedAssociationFS.UseTracker = False
tpToStaSeedAssociationFS.UseMuon = True

tpToStaMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToStaMuonAssociationFS.tracksTag = 'standAloneMuons'
tpToStaMuonAssociationFS.UseTracker = False
tpToStaMuonAssociationFS.UseMuon = True

tpToStaUpdMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToStaUpdMuonAssociationFS.tracksTag = 'standAloneMuons:UpdatedAtVtx'
tpToStaUpdMuonAssociationFS.UseTracker = False
tpToStaUpdMuonAssociationFS.UseMuon = True

tpToStaRefitMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToStaRefitMuonAssociationFS.tracksTag = 'refittedStandAloneMuons'
tpToStaRefitMuonAssociationFS.UseTracker = False
tpToStaRefitMuonAssociationFS.UseMuon = True

tpToStaRefitUpdMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToStaRefitUpdMuonAssociationFS.tracksTag = 'refittedStandAloneMuons:UpdatedAtVtx'
tpToStaRefitUpdMuonAssociationFS.UseTracker = False
tpToStaRefitUpdMuonAssociationFS.UseMuon = True

tpToDisplacedTrkMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToDisplacedTrkMuonAssociationFS.tracksTag = 'displacedTracks'
tpToDisplacedTrkMuonAssociationFS.UseTracker = True
tpToDisplacedTrkMuonAssociationFS.UseMuon = False

tpToDisplacedStaSeedAssociationFS = baseMuonAssociatorFS.clone()
tpToDisplacedStaSeedAssociationFS.tracksTag = 'seedsOfDisplacedSTAmuons'
tpToDisplacedStaSeedAssociationFS.UseTracker = False
tpToDisplacedStaSeedAssociationFS.UseMuon = True

tpToDisplacedStaMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToDisplacedStaMuonAssociationFS.tracksTag = 'displacedStandAloneMuons'
tpToDisplacedStaMuonAssociationFS.UseTracker = False
tpToDisplacedStaMuonAssociationFS.UseMuon = True

tpToDisplacedGlbMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToDisplacedGlbMuonAssociationFS.tracksTag = 'displacedGlobalMuons'
tpToDisplacedGlbMuonAssociationFS.UseTracker = True
tpToDisplacedGlbMuonAssociationFS.UseMuon = True

tpToGlbMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToGlbMuonAssociationFS.tracksTag = 'extractedGlobalMuons'
tpToGlbMuonAssociationFS.UseTracker = True
tpToGlbMuonAssociationFS.UseMuon = True

tpToTevFirstMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToTevFirstMuonAssociationFS.tracksTag = 'tevMuons:firstHit'
tpToTevFirstMuonAssociationFS.UseTracker = True
tpToTevFirstMuonAssociationFS.UseMuon = True

tpToTevPickyMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToTevPickyMuonAssociationFS.tracksTag = 'tevMuons:picky'
tpToTevPickyMuonAssociationFS.UseTracker = True
tpToTevPickyMuonAssociationFS.UseMuon = True

tpToTevDytMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToTevDytMuonAssociationFS.tracksTag = 'tevMuons:dyt'
tpToTevDytMuonAssociationFS.UseTracker = True
tpToTevDytMuonAssociationFS.UseMuon = True

tpToL3TkMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToL3TkMuonAssociationFS.tracksTag = 'hltL3TkTracksFromL2'
tpToL3TkMuonAssociationFS.UseTracker = True
tpToL3TkMuonAssociationFS.UseMuon = False
tpToL3TkMuonAssociationFS.ignoreMissingTrackCollection = True

tpToL2MuonAssociationFS = baseMuonAssociatorFS.clone()
tpToL2MuonAssociationFS.tracksTag = 'hltL2Muons'
tpToL2MuonAssociationFS.UseTracker = False
tpToL2MuonAssociationFS.UseMuon = True
tpToL2MuonAssociationFS.ignoreMissingTrackCollection = True

tpToL2UpdMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToL2UpdMuonAssociationFS.tracksTag = 'hltL2Muons:UpdatedAtVtx'
tpToL2UpdMuonAssociationFS.UseTracker = False
tpToL2UpdMuonAssociationFS.UseMuon = True
tpToL2UpdMuonAssociationFS.ignoreMissingTrackCollection = True

tpToL3MuonAssociationFS = baseMuonAssociatorFS.clone()
tpToL3MuonAssociationFS.tracksTag = 'hltL3Muons'
tpToL3MuonAssociationFS.UseTracker = True
tpToL3MuonAssociationFS.UseMuon = True
tpToL3MuonAssociationFS.ignoreMissingTrackCollection = True

#
# The FastSim association sequences
#

#muonAssociationFastSim_seq = cms.Sequence(
#    probeTracks_seq+tpToTkMuonAssociationFS
#    +trackAssociatorByHits+tpToTkmuTrackAssociationFS 
#    +seedsOfSTAmuons_seq+tpToStaSeedAssociationFS
#    +tpToStaMuonAssociationFS+tpToStaUpdMuonAssociationFS
#    +extractedMuonTracks_seq+tpToGlbMuonAssociationFS
#    )

#muonAssociationTEVFastSim_seq = cms.Sequence(
#    tpToTevFirstMuonAssociationFS+tpToTevPickyMuonAssociationFS+tpToTevDytMuonAssociationFS
#    )

#muonAssociationDisplacedFastSim_seq = cms.Sequence(
#    seedsOfDisplacedSTAmuons_seq+tpToDisplacedStaSeedAssociationFS+tpToDisplacedStaMuonAssociationFS
#    +tpToDisplacedTrkMuonAssociationFS+tpToDisplacedGlbMuonAssociationFS
#    )

#muonAssociationRefitFastSim_seq = cms.Sequence(
#    tpToStaRefitMuonAssociationFS+tpToStaRefitUpdMuonAssociationFS
#    )

#muonAssociationHLTFastSim_seq = cms.Sequence(
#    tpToL2MuonAssociationFS+tpToL2UpdMuonAssociationFS+tpToL3MuonAssociationFS+tpToL3TkMuonAssociationFS
#    )

