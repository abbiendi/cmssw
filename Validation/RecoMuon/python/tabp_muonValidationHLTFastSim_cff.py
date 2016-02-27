import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.tabp_muonValidationHLT_cff import *

# Configurations for MuonTrackValidators

l2MuonTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l2MuonTrackV.clone()
l2MuonTrackFSV.associatormap = 'tpToL2TrackAssociationFS'
l2MuonTrackFSV.label_tp_effic = 'mix:MergedTrackTruth'
l2MuonTrackFSV.label_tp_fake = 'mix:MergedTrackTruth'
l2MuonTrackFSV.beamSpot = 'offlineBeamSpot'

l2UpdMuonTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l2UpdMuonTrackV.clone()
l2UpdMuonTrackFSV.associatormap = 'tpToL2UpdTrackAssociationFS'
l2UpdMuonTrackFSV.label_tp_effic = 'mix:MergedTrackTruth'
l2UpdMuonTrackFSV.label_tp_fake = 'mix:MergedTrackTruth'
l2UpdMuonTrackFSV.beamSpot = 'offlineBeamSpot'

l3TkMuonTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l3TkMuonTrackV.clone()
l3TkMuonTrackFSV.associatormap = 'tpToL3TkTrackTrackAssociationFS'
l3TkMuonTrackFSV.label_tp_effic = 'mix:MergedTrackTruth'
l3TkMuonTrackFSV.label_tp_fake = 'mix:MergedTrackTruth'
l3TkMuonTrackFSV.beamSpot = 'offlineBeamSpot'

l3MuonTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l3MuonTrackV.clone()
l3MuonTrackFSV.associatormap = 'tpToL3TrackAssociationFS'
l3MuonTrackFSV.label_tp_effic = 'mix:MergedTrackTruth'
l3MuonTrackFSV.label_tp_fake = 'mix:MergedTrackTruth'
l3MuonTrackFSV.beamSpot = 'offlineBeamSpot'


# # Muon validation sequence
muonValidationHLTFastSim_seq = cms.Sequence(
    l2MuonMuTrackFSV+l2UpdMuonMuTrackFSV+l3MuonMuTrackFSV+l3TkMuonMuTrackFSV
    )


# The muon HLT association and validation sequence
recoMuonAssociationHLTFastSim_seq = cms.Sequence(muonAssociationHLTFastSim_seq)
recoMuonValidationHLTFastSim_seq = cms.Sequence(muonValidationHLTFastSim_seq)
