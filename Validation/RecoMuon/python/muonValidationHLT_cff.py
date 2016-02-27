import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.associators_cff import *
from Validation.RecoMuon.histoParameters_cff import *
import Validation.RecoMuon.MuonTrackValidator_cfi

l2MuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l2MuonMuTrackV.associatormap = 'tpToL2MuonAssociation'
l2MuonMuTrackV.label = ('hltL2Muons',)
l2MuonMuTrackV.dirName = 'HLT/Muon/MuonTrack/'
#l2MuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l2MuonMuTrackV.ignoremissingtrackcollection=True
l2MuonMuTrackV.muonHistoParameters = staMuonHistoParameters

l2UpdMuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l2UpdMuonMuTrackV.associatormap = 'tpToL2UpdMuonAssociation'
l2UpdMuonMuTrackV.label = ('hltL2Muons:UpdatedAtVtx',)
l2UpdMuonMuTrackV.dirName = 'HLT/Muon/MuonTrack/'
#l2UpdMuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l2UpdMuonMuTrackV.ignoremissingtrackcollection=True
l2UpdMuonMuTrackV.muonHistoParameters = staUpdMuonHistoParameters

l3TkMuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l3TkMuonMuTrackV.associatormap = 'tpToL3TkMuonAssociation'
l3TkMuonMuTrackV.label = ('hltL3TkTracksFromL2:',)
l3TkMuonMuTrackV.dirName = 'HLT/Muon/MuonTrack/'
#l3TkMuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l3TkMuonMuTrackV.ignoremissingtrackcollection=True
l3TkMuonMuTrackV.muonHistoParameters = trkMuonHistoParameters

l3MuonMuTrackV = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
l3MuonMuTrackV.associatormap = 'tpToL3MuonAssociation'
l3MuonMuTrackV.label = ('hltL3Muons:',)
l3MuonMuTrackV.dirName = 'HLT/Muon/MuonTrack/'
#l3MuonMuTrackV.beamSpot = 'hltOfflineBeamSpot'
l3MuonMuTrackV.ignoremissingtrackcollection=True
l3MuonMuTrackV.muonHistoParameters = glbMuonHistoParameters
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

#####################################################################################
# FEW sequences for BARREL and ENDCAPS separately !
#
# L2 muons
L2MuonTrackVMuonAssocBarrelOnly = l2MuonMuTrackV.clone()
L2MuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
L2MuonTrackVMuonAssocBarrelOnly.label = ('L2MuonsBarrelOnly',)
L2MuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToL2MuonAssociationBarrelOnly'

L2MuonTrackVMuonAssocMinusEndcapOnly = l2MuonMuTrackV.clone()
L2MuonTrackVMuonAssocMinusEndcapOnly.muonTPSelector = muonMinusEndcapOnlyTPSet
L2MuonTrackVMuonAssocMinusEndcapOnly.label = ('L2MuonsMinusEndcapOnly',)
L2MuonTrackVMuonAssocMinusEndcapOnly.associatormap = 'tpToL2MuonAssociationMinusEndcapOnly'

L2MuonTrackVMuonAssocPlusEndcapOnly = l2MuonMuTrackV.clone()
L2MuonTrackVMuonAssocPlusEndcapOnly.muonTPSelector = muonPlusEndcapOnlyTPSet
L2MuonTrackVMuonAssocPlusEndcapOnly.label = ('L2MuonsPlusEndcapOnly',)
L2MuonTrackVMuonAssocPlusEndcapOnly.associatormap = 'tpToL2MuonAssociationPlusEndcapOnly'

# L2 Upd muons
L2UpdMuonTrackVMuonAssocBarrelOnly = l2MuonMuTrackV.clone()
L2UpdMuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
L2UpdMuonTrackVMuonAssocBarrelOnly.label = ('L2UpdMuonsBarrelOnly',)
L2UpdMuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToL2UpdMuonAssociationBarrelOnly'

L2UpdMuonTrackVMuonAssocMinusEndcapOnly = l2MuonMuTrackV.clone()
L2UpdMuonTrackVMuonAssocMinusEndcapOnly.muonTPSelector = muonMinusEndcapOnlyTPSet
L2UpdMuonTrackVMuonAssocMinusEndcapOnly.label = ('L2UpdMuonsMinusEndcapOnly',)
L2UpdMuonTrackVMuonAssocMinusEndcapOnly.associatormap = 'tpToL2UpdMuonAssociationMinusEndcapOnly'

L2UpdMuonTrackVMuonAssocPlusEndcapOnly = l2MuonMuTrackV.clone()
L2UpdMuonTrackVMuonAssocPlusEndcapOnly.muonTPSelector = muonPlusEndcapOnlyTPSet
L2UpdMuonTrackVMuonAssocPlusEndcapOnly.label = ('L2UpdMuonsPlusEndcapOnly',)
L2UpdMuonTrackVMuonAssocPlusEndcapOnly.associatormap = 'tpToL2UpdMuonAssociationPlusEndcapOnly'

# L3 muons
L3MuonTrackVMuonAssocBarrelOnly = l3MuonMuTrackV.clone()
L3MuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
L3MuonTrackVMuonAssocBarrelOnly.label = ('L3MuonsBarrelOnly',)
L3MuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToL3MuonAssociationBarrelOnly'

L3MuonTrackVMuonAssocMinusEndcapOnly = l3MuonMuTrackV.clone()
L3MuonTrackVMuonAssocMinusEndcapOnly.muonTPSelector = muonMinusEndcapOnlyTPSet
L3MuonTrackVMuonAssocMinusEndcapOnly.label = ('L3MuonsMinusEndcapOnly',)
L3MuonTrackVMuonAssocMinusEndcapOnly.associatormap = 'tpToL3MuonAssociationMinusEndcapOnly'

L3MuonTrackVMuonAssocPlusEndcapOnly = l3MuonMuTrackV.clone()
L3MuonTrackVMuonAssocPlusEndcapOnly.muonTPSelector = muonPlusEndcapOnlyTPSet
L3MuonTrackVMuonAssocPlusEndcapOnly.label = ('L3MuonsPlusEndcapOnly',)
L3MuonTrackVMuonAssocPlusEndcapOnly.associatormap = 'tpToL3MuonAssociationPlusEndcapOnly'

# L3 tracker Tracks from L2 muons
L3TkMuonTrackVMuonAssocBarrelOnly = l3TkMuonMuTrackV.clone()
L3TkMuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
L3TkMuonTrackVMuonAssocBarrelOnly.label = ('L3TkMuonsBarrelOnly',)
L3TkMuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToL3TkMuonAssociationBarrelOnly'

L3TkMuonTrackVMuonAssocMinusEndcapOnly = l3TkMuonMuTrackV.clone()
L3TkMuonTrackVMuonAssocMinusEndcapOnly.muonTPSelector = muonMinusEndcapOnlyTPSet
L3TkMuonTrackVMuonAssocMinusEndcapOnly.label = ('L3TkMuonsMinusEndcapOnly',)
L3TkMuonTrackVMuonAssocMinusEndcapOnly.associatormap = 'tpToL3TkMuonAssociationMinusEndcapOnly'

L3TkMuonTrackVMuonAssocPlusEndcapOnly = l3TkMuonMuTrackV.clone()
L3TkMuonTrackVMuonAssocPlusEndcapOnly.muonTPSelector = muonPlusEndcapOnlyTPSet
L3TkMuonTrackVMuonAssocPlusEndcapOnly.label = ('L3TkMuonsPlusEndcapOnly',)
L3TkMuonTrackVMuonAssocPlusEndcapOnly.associatormap = 'tpToL3TkMuonAssociationPlusEndcapOnly'

#
muonValidationHLTBarrelOnly_seq = cms.Sequence(
    L2MuonsBarrelOnly + tpToL2MuonAssociationBarrelOnly + L2MuonTrackVMuonAssocBarrelOnly
    + L2UpdMuonsBarrelOnly + tpToL2UpdMuonAssociationBarrelOnly + L2UpdMuonTrackVMuonAssocBarrelOnly
    + L3MuonsBarrelOnly + tpToL3MuonAssociationBarrelOnly + L3MuonTrackVMuonAssocBarrelOnly
    + L3TkMuonsBarrelOnly + tpToL3TkMuonAssociationBarrelOnly + L3TkMuonTrackVMuonAssocBarrelOnly
    )

recoMuonValidationHLTBarrelOnly_seq = cms.Sequence(
    muonValidationHLTBarrelOnly_seq
    )

muonValidationHLTMinusEndcapOnly_seq = cms.Sequence(
    L2MuonsMinusEndcapOnly + tpToL2MuonAssociationMinusEndcapOnly + L2MuonTrackVMuonAssocMinusEndcapOnly
    + L2UpdMuonsMinusEndcapOnly + tpToL2UpdMuonAssociationMinusEndcapOnly + L2UpdMuonTrackVMuonAssocMinusEndcapOnly
    + L3MuonsMinusEndcapOnly + tpToL3MuonAssociationMinusEndcapOnly + L3MuonTrackVMuonAssocMinusEndcapOnly
    + L3TkMuonsMinusEndcapOnly + tpToL3TkMuonAssociationMinusEndcapOnly + L3TkMuonTrackVMuonAssocMinusEndcapOnly
    )

recoMuonValidationHLTMinusEndcapOnly_seq = cms.Sequence(
    muonValidationHLTMinusEndcapOnly_seq
    )

muonValidationHLTPlusEndcapOnly_seq = cms.Sequence(
    L2MuonsPlusEndcapOnly + tpToL2MuonAssociationPlusEndcapOnly + L2MuonTrackVMuonAssocPlusEndcapOnly
    + L2UpdMuonsPlusEndcapOnly + tpToL2UpdMuonAssociationPlusEndcapOnly + L2UpdMuonTrackVMuonAssocPlusEndcapOnly
    + L3MuonsPlusEndcapOnly + tpToL3MuonAssociationPlusEndcapOnly + L3MuonTrackVMuonAssocPlusEndcapOnly
    + L3TkMuonsPlusEndcapOnly + tpToL3TkMuonAssociationPlusEndcapOnly + L3TkMuonTrackVMuonAssocPlusEndcapOnly
    )

recoMuonValidationHLTPlusEndcapOnly_seq = cms.Sequence(
    muonValidationHLTPlusEndcapOnly_seq
    )
