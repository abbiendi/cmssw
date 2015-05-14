import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.associators_cff import *
import Validation.RecoMuon.MuonTrackValidator_cfi

l2MuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l2MuonMuTrackV.associatormap = 'tpToL2MuonAssociation'
l2MuonMuTrackV.label = ('hltL2Muons',)
l2MuonMuTrackV.associators = ('MuonAssociationByHits',)
l2MuonMuTrackV.dirName = 'HLT/Muon/MultiTrack/'
#l2MuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l2MuonMuTrackV.ignoremissingtrackcollection=True
l2MuonMuTrackV.usetracker = False
l2MuonMuTrackV.usemuon = True

l2UpdMuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l2UpdMuonMuTrackV.associatormap = 'tpToL2UpdMuonAssociation'
l2UpdMuonMuTrackV.label = ('hltL2Muons:UpdatedAtVtx',)
l2UpdMuonMuTrackV.associators = ('MuonAssociationByHits',)
l2UpdMuonMuTrackV.dirName = 'HLT/Muon/MultiTrack/'
#l2UpdMuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l2UpdMuonMuTrackV.ignoremissingtrackcollection=True
l2UpdMuonMuTrackV.usetracker = False
l2UpdMuonMuTrackV.usemuon = True

l3TkMuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l3TkMuonMuTrackV.associatormap = 'tpToL3TkMuonAssociation'
l3TkMuonMuTrackV.label = ('hltL3TkTracksFromL2:',)
l3TkMuonMuTrackV.associators = ('MuonAssociationByHits',)
l3TkMuonMuTrackV.dirName = 'HLT/Muon/MultiTrack/'
#l3TkMuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l3TkMuonMuTrackV.ignoremissingtrackcollection=True
l3TkMuonMuTrackV.usetracker = True
l3TkMuonMuTrackV.usemuon = False

l3MuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l3MuonMuTrackV.associatormap = 'tpToL3MuonAssociation'
l3MuonMuTrackV.label = ('hltL3Muons:',)
l3MuonMuTrackV.associators = ('MuonAssociationByHits',)
l3MuonMuTrackV.dirName = 'HLT/Muon/MultiTrack/'
#l3MuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l3MuonMuTrackV.ignoremissingtrackcollection=True
l3MuonMuTrackV.usetracker = True
l3MuonMuTrackV.usemuon = True

#
# The full Muon HLT validation sequence
#
muonValidationHLT_seq = cms.Sequence(
    tpToL2MuonAssociation + l2MuonMuTrackV
    +tpToL2UpdMuonAssociation + l2UpdMuonMuTrackV
    +tpToL3TkMuonAssociation + l3TkMuonMuTrackV
    +tpToL3MuonAssociation + l3MuonMuTrackV
    )

recoMuonValidationHLT_seq = cms.Sequence(
    muonValidationHLT_seq
    )
