#
# Production configuration for FastSim: muon track validation using MuonAssociatorByHits
#
import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.associatorsFastSim_cff import *
#from Validation.RecoMuon.muonValidation_cff import *

# Configurations for MuonTrackValidators

from Validation.RecoMuon.muonValidation_cff import trkMuonTrackVTrackAssoc
trkMuonTrackVTrackAssocFS = trkMuonTrackVTrackAssoc.clone()
trkMuonTrackVTrackAssocFS.associatormap = 'tpToTkmuTrackAssociationFS'

from Validation.RecoMuon.muonValidation_cff import trkProbeTrackVMuonAssoc 
trkProbeTrackVMuonAssocFS = trkProbeTrackVMuonAssoc.clone()
trkProbeTrackVMuonAssocFS.associatormap = 'tpToTkMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import staSeedTrackVMuonAssoc
staSeedTrackVMuonAssocFS = staSeedTrackVMuonAssoc.clone() 
staSeedTrackVMuonAssocFS.associatormap = 'tpToStaSeedAssociationFS' 

from Validation.RecoMuon.muonValidation_cff import staMuonTrackVMuonAssoc
staMuonTrackVMuonAssocFS = staMuonTrackVMuonAssoc.clone()
staMuonTrackVMuonAssocFS.associatormap = 'tpToStaMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import staUpdMuonTrackVMuonAssoc
staUpdMuonTrackVMuonAssocFS = staUpdMuonTrackVMuonAssoc.clone()
staUpdMuonTrackVMuonAssocFS.associatormap = 'tpToStaUpdMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import staRefitMuonTrackVMuonAssoc
staRefitMuonTrackVMuonAssocFS = staRefitMuonTrackVMuonAssoc.clone()
staRefitMuonTrackVMuonAssocFS.associatormap = 'tpToStaRefitMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import staRefitUpdMuonTrackVMuonAssoc
staRefitUpdMuonTrackVMuonAssocFS = staRefitUpdMuonTrackVMuonAssoc.clone()
staRefitUpdMuonTrackVMuonAssocFS.associatormap = 'tpToStaRefitUpdMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import glbMuonTrackVMuonAssoc
glbMuonTrackVMuonAssocFS = glbMuonTrackVMuonAssoc.clone()
glbMuonTrackVMuonAssocFS.associatormap = 'tpToGlbMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import tevMuonFirstTrackVMuonAssoc
tevMuonFirstTrackVMuonAssocFS = tevMuonFirstTrackVMuonAssoc.clone()
tevMuonFirstTrackVMuonAssocFS.associatormap = 'tpToTevFirstMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import tevMuonPickyTrackVMuonAssoc
tevMuonPickyTrackVMuonAssocFS = tevMuonPickyTrackVMuonAssoc.clone()
tevMuonPickyTrackVMuonAssocFS.associatormap = 'tpToTevPickyMuonAssociationFS'

from Validation.RecoMuon.muonValidation_cff import tevMuonDytTrackVMuonAssoc
tevMuonDytTrackVMuonAssocFS = tevMuonDytTrackVMuonAssoc.clone()
tevMuonDytTrackVMuonAssocFS.associatormap = 'tpToTevDytMuonAssociationFS'

# Configurations for RecoMuonValidator
from Validation.RecoMuon.muonValidation_cff import *

#
# Muon validation sequence
#
#muonValidationFastSim_seq = cms.Sequence(
#### validator modules (associators included in another sequence: why can't this be done as in FullSim?)
#    trkMuonTrackVTrackAssocFS+trkProbeTrackVMuonAssocFS
#    +staSeedTrackVMuonAssocFS+staMuonTrackVMuonAssocFS+staUpdMuonTrackVMuonAssocFS+glbMuonTrackVMuonAssocFS
#    +staRefitMuonTrackVMuonAssocFS+staRefitUpdMuonTrackVMuonAssocFS
#    +tevMuonFirstTrackVMuonAssocFS+tevMuonPickyTrackVMuonAssocFS+tevMuonDytTrackVMuonAssocFS
#####    # associator + validator module
#    +muonAssociatorByHitsNoSimHitsHelperTrk + recoMuonVMuAssoc_trk
#    +muonAssociatorByHitsNoSimHitsHelperStandalone + recoMuonVMuAssoc_sta
#    +muonAssociatorByHitsNoSimHitsHelperGlobal + recoMuonVMuAssoc_glb
#    +muonAssociatorByHitsNoSimHitsHelperTrkPF + recoMuonVMuAssoc_trkPF
#    +muonAssociatorByHitsNoSimHitsHelperStandalonePF + recoMuonVMuAssoc_staPF
#    +muonAssociatorByHitsNoSimHitsHelperGlobalPF + recoMuonVMuAssoc_glbPF
#    +muonAssociatorByHitsNoSimHitsHelperTight + recoMuonVMuAssoc_tgt
#    )

muonValidationFastSimBase_seq = cms.Sequence(
    probeTracks_seq + tpToTkMuonAssociationFS + trkProbeTrackVMuonAssocFS
    +trackAssociatorByHits + tpToTkmuTrackAssociationFS + trkMuonTrackVTrackAssocFS
    +seedsOfSTAmuons_seq + tpToStaSeedAssociationFS + staSeedTrackVMuonAssocFS
    +tpToStaMuonAssociationFS + staMuonTrackVMuonAssocFS
    +tpToStaUpdMuonAssociationFS + staUpdMuonTrackVMuonAssocFS
    +extractedMuonTracks_seq + tpToGlbMuonAssociationFS + glbMuonTrackVMuonAssocFS
)

muonValidationFastSimTEV_seq = cms.Sequence(
    tpToTevFirstMuonAssociationFS + tevMuonFirstTrackVMuonAssocFS
    +tpToTevPickyMuonAssociationFS + tevMuonPickyTrackVMuonAssocFS
    +tpToTevDytMuonAssociationFS + tevMuonDytTrackVMuonAssocFS
)

muonValidationFastSimRefit_seq = cms.Sequence(
    tpToStaRefitMuonAssociationFS + staRefitMuonTrackVMuonAssocFS
    +tpToStaRefitUpdMuonAssociationFS + staRefitUpdMuonTrackVMuonAssocFS
)

muonValidationFastSimRMV_seq = cms.Sequence(
    muonAssociatorByHitsNoSimHitsHelperTrk +recoMuonVMuAssoc_trk
    +muonAssociatorByHitsNoSimHitsHelperStandalone +recoMuonVMuAssoc_sta
    +muonAssociatorByHitsNoSimHitsHelperGlobal +recoMuonVMuAssoc_glb
    +muonAssociatorByHitsNoSimHitsHelperTight +recoMuonVMuAssoc_tgt 
    +muonAssociatorByHitsNoSimHitsHelperTrkPF +recoMuonVMuAssoc_trkPF
    +muonAssociatorByHitsNoSimHitsHelperStandalonePF +recoMuonVMuAssoc_staPF
    +muonAssociatorByHitsNoSimHitsHelperGlobalPF +recoMuonVMuAssoc_glbPF
)

# The muon association and validation sequence
#from Validation.RecoMuon.associatorsFastSim_cff import muonAssociationFastSim_seq

#from Validation.RecoMuon.associatorsFastSim_cff import *
######from Validation.RecoMuon.associators_cff import *

#recoMuonAssociationFastSim = cms.Sequence(muonAssociationFastSim_seq
#                                          + muonAssociationRefitFastSim_seq + muonAssociationTEVFastSim_seq
#                                          )

#recoMuonValidationFastSim = cms.Sequence(muonValidationFastSim_seq)

recoMuonValidationFastSim = cms.Sequence(
    muonValidationFastSimBase_seq 
    + muonValidationFastSimTEV_seq 
    + muonValidationFastSimRefit_seq
    + muonValidationFastSimRMV_seq
    )

