import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.associatorsFastSim_cff import *
from Validation.RecoMuon.muonValidationHLT_cff import *

# Configurations for MuonTrackValidators

l2MuonMuTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l2MuonMuTrackV.clone()
l2MuonMuTrackFSV.associatormap = 'tpToL2MuonAssociationFS'

l2UpdMuonMuTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l2UpdMuonMuTrackV.clone()
l2UpdMuonMuTrackFSV.associatormap = 'tpToL2UpdMuonAssociationFS'

l3TkMuonMuTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l3TkMuonMuTrackV.clone()
l3TkMuonMuTrackFSV.associatormap = 'tpToL3TkMuonAssociationFS'

l3MuonMuTrackFSV = Validation.RecoMuon.muonValidationHLT_cff.l3MuonMuTrackV.clone()
l3MuonMuTrackFSV.associatormap = 'tpToL3MuonAssociationFS'

# # Muon validation sequence
#muonValidationHLTFastSim_seq = cms.Sequence(
#    l2MuonMuTrackFSV+l2UpdMuonMuTrackFSV+l3MuonMuTrackFSV+l3TkMuonMuTrackFSV
#    )

muonValidationHLTFastSim_seq = cms.Sequence(
    tpToL2MuonAssociationFS + l2MuonMuTrackFSV
    +tpToL2UpdMuonAssociationFS + l2UpdMuonMuTrackFSV
    +tpToL3TkMuonAssociationFS + l3TkMuonMuTrackFSV
    +tpToL3MuonAssociationFS + l3MuonMuTrackFSV
    )

# The muon HLT association and validation sequence
#### recoMuonAssociationHLTFastSim_seq = cms.Sequence(muonAssociationHLTFastSim_seq)
recoMuonValidationHLTFastSim_seq = cms.Sequence(muonValidationHLTFastSim_seq)


#recoMuonValidationHLT_seq = cms.Sequence(
#    muonValidationHLT_seq
#    )
