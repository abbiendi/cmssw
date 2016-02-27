# configuration for FastSim: muon track validation using TrackAssociatorByPosition
#  (backup solution, incomplete, not run by default)
#
import FWCore.ParameterSet.Config as cms

# Configurations for MuonTrackValidators

from Validation.RecoMuon.muonValidation_cff import trkMuonTrackVTrackAssoc
trkMuonTrackVTrackAssocFS = trkMuonTrackVTrackAssoc.clone()
trkMuonTrackVTrackAssocFS.associatormap = 'tpToTkmuTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import staMuonTrackVTrackAssoc
staMuonTrackVTrackAssocFS = staMuonTrackVTrackAssoc.clone()
staMuonTrackVTrackAssocFS.associatormap = 'tpToStaTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import staUpdMuonTrackVTrackAssoc
staUpdMuonTrackVTrackAssocFS = staUpdMuonTrackVTrackAssoc.clone()
staUpdMuonTrackVTrackAssocFS.associatormap = 'tpToStaUpdTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import glbMuonTrackVTrackAssoc
glbMuonTrackVTrackAssocFS = glbMuonTrackVTrackAssoc.clone()
glbMuonTrackVTrackAssocFS.associatormap = 'tpToGlbTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import tevMuonFirstTrackVTrackAssoc
tevMuonFirstTrackVTrackAssocFS = tevMuonFirstTrackVTrackAssoc.clone()
tevMuonFirstTrackVTrackAssocFS.associatormap = 'tpToTevFirstTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import tevMuonPickyTrackVTrackAssoc
tevMuonPickyTrackVTrackAssocFS = tevMuonPickyTrackVTrackAssoc.clone()
tevMuonPickyTrackVTrackAssocFS.associatormap = 'tpToTevPickyTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import tevMuonDytTrackVTrackAssoc
tevMuonDytTrackVTrackAssocFS = tevMuonDytTrackVTrackAssoc.clone()
tevMuonDytTrackVTrackAssocFS.associatormap = 'tpToTevDytTrackAssociationFS'


# Muon validation sequence
muonValidationFastSim_seq = cms.Sequence(
    trkMuonTrackVTrackAssocFS
    +staMuonTrackVTrackAssocFS+staUpdMuonTrackVTrackAssocFS+glbMuonTrackVTrackAssocFS
    +tevMuonFirstTrackVTrackAssocFS+tevMuonPickyTrackVTrackAssocFS+tevMuonDytTrackVTrackAssocFS
    )

# The muon association and validation sequence
from Validation.RecoMuon.tabp_associatorsFastSim_cff import muonAssociationFastSim_seq
recoMuonAssociationFastSim = cms.Sequence(muonAssociationFastSim_seq)
recoMuonValidationFastSim = cms.Sequence(muonValidationFastSim_seq)

