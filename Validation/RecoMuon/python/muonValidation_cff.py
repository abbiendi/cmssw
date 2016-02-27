#
# introduced BARREL only and ENDCAP only modules  (temporary)
#
# Production configuration for FullSim: muon track validation using MuonAssociatorByHits
#
import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.associators_cff import *
from Validation.RecoMuon.histoParameters_cff import *
import Validation.RecoMuon.MuonTrackValidator_cfi

from SimTracker.TrackAssociation.LhcParametersDefinerForTP_cfi import *
from SimTracker.TrackAssociation.CosmicParametersDefinerForTP_cfi import *

#
# MuonAssociatorByHits used for all track collections
#
trkProbeTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkProbeTrackVMuonAssoc.associatormap = 'tpToTkMuonAssociation' 
#trkProbeTrackVMuonAssoc.label = ('generalTracks',)
trkProbeTrackVMuonAssoc.label = ('probeTracks',)
trkProbeTrackVMuonAssoc.muonHistoParameters = trkMuonHistoParameters

# quickTrackAssociatorByHits on probeTracks used as monitor wrt MuonAssociatorByHits
#
trkMuonTrackVTrackAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkMuonTrackVTrackAssoc.associatormap = 'tpToTkmuTrackAssociation'
trkMuonTrackVTrackAssoc.associators = ('trackAssociatorByHits',)
#trkMuonTrackVTrackAssoc.label = ('generalTracks',)
trkMuonTrackVTrackAssoc.label = ('probeTracks',)
trkMuonTrackVTrackAssoc.muonHistoParameters = trkMuonHistoParameters

staSeedTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staSeedTrackVMuonAssoc.associatormap = 'tpToStaSeedAssociation'
staSeedTrackVMuonAssoc.label = ('seedsOfSTAmuons',)
staSeedTrackVMuonAssoc.muonHistoParameters = staSeedMuonHistoParameters

staMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staMuonTrackVMuonAssoc.associatormap = 'tpToStaMuonAssociation'
staMuonTrackVMuonAssoc.label = ('standAloneMuons',)
staMuonTrackVMuonAssoc.muonHistoParameters = staMuonHistoParameters

staUpdMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staUpdMuonTrackVMuonAssoc.associatormap = 'tpToStaUpdMuonAssociation'
staUpdMuonTrackVMuonAssoc.label = ('standAloneMuons:UpdatedAtVtx',)
staUpdMuonTrackVMuonAssoc.muonHistoParameters = staUpdMuonHistoParameters

glbMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbMuonTrackVMuonAssoc.associatormap = 'tpToGlbMuonAssociation'
glbMuonTrackVMuonAssoc.label = ('globalMuons',)
glbMuonTrackVMuonAssoc.muonHistoParameters = glbMuonHistoParameters

staRefitMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staRefitMuonTrackVMuonAssoc.associatormap = 'tpToStaRefitMuonAssociation'
staRefitMuonTrackVMuonAssoc.label = ('refittedStandAloneMuons',)
staRefitMuonTrackVMuonAssoc.muonHistoParameters = staMuonHistoParameters

staRefitUpdMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staRefitUpdMuonTrackVMuonAssoc.associatormap = 'tpToStaRefitUpdMuonAssociation'
staRefitUpdMuonTrackVMuonAssoc.label = ('refittedStandAloneMuons:UpdatedAtVtx',)
staRefitUpdMuonTrackVMuonAssoc.muonHistoParameters = staUpdMuonHistoParameters

displacedTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedTrackVMuonAssoc.associatormap = 'tpToDisplacedTrkMuonAssociation'
displacedTrackVMuonAssoc.label = ('displacedTracks',)
displacedTrackVMuonAssoc.muonTPSelector = displacedMuonTPSet
displacedTrackVMuonAssoc.muonHistoParameters = displacedTrkMuonHistoParameters

displacedStaSeedTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedStaSeedTrackVMuonAssoc.associatormap = 'tpToDisplacedStaSeedAssociation'
displacedStaSeedTrackVMuonAssoc.label = ('seedsOfDisplacedSTAmuons',)
displacedStaSeedTrackVMuonAssoc.muonTPSelector = displacedMuonTPSet
displacedStaSeedTrackVMuonAssoc.muonHistoParameters = displacedStaSeedMuonHistoParameters

displacedStaMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedStaMuonTrackVMuonAssoc.associatormap = 'tpToDisplacedStaMuonAssociation'
displacedStaMuonTrackVMuonAssoc.label = ('displacedStandAloneMuons',)
displacedStaMuonTrackVMuonAssoc.muonTPSelector = displacedMuonTPSet
displacedStaMuonTrackVMuonAssoc.muonHistoParameters = displacedStaMuonHistoParameters

displacedGlbMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedGlbMuonTrackVMuonAssoc.associatormap = 'tpToDisplacedGlbMuonAssociation'
displacedGlbMuonTrackVMuonAssoc.label = ('displacedGlobalMuons',)
displacedGlbMuonTrackVMuonAssoc.muonTPSelector = displacedMuonTPSet
displacedGlbMuonTrackVMuonAssoc.muonHistoParameters = displacedGlbMuonHistoParameters

staSETMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staSETMuonTrackVMuonAssoc.associatormap = 'tpToStaSETMuonAssociation'
staSETMuonTrackVMuonAssoc.label = ('standAloneSETMuons',)
staSETMuonTrackVMuonAssoc.muonHistoParameters = staMuonHistoParameters

staSETUpdMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staSETUpdMuonTrackVMuonAssoc.associatormap = 'tpToStaSETUpdMuonAssociation'
staSETUpdMuonTrackVMuonAssoc.label = ('standAloneSETMuons:UpdatedAtVtx',)
staSETUpdMuonTrackVMuonAssoc.muonHistoParameters = staUpdMuonHistoParameters

glbSETMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbSETMuonTrackVMuonAssoc.associatormap = 'tpToGlbSETMuonAssociation'
glbSETMuonTrackVMuonAssoc.label = ('globalSETMuons',)
glbSETMuonTrackVMuonAssoc.muonHistoParameters = glbMuonHistoParameters

tevMuonFirstTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
tevMuonFirstTrackVMuonAssoc.associatormap = 'tpToTevFirstMuonAssociation'
tevMuonFirstTrackVMuonAssoc.label = ('tevMuons:firstHit',)
tevMuonFirstTrackVMuonAssoc.muonHistoParameters = glbMuonHistoParameters

tevMuonPickyTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
tevMuonPickyTrackVMuonAssoc.associatormap = 'tpToTevPickyMuonAssociation'
tevMuonPickyTrackVMuonAssoc.label = ('tevMuons:picky',)
tevMuonPickyTrackVMuonAssoc.muonHistoParameters = glbMuonHistoParameters

tevMuonDytTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
tevMuonDytTrackVMuonAssoc.associatormap = 'tpToTevDytMuonAssociation'
tevMuonDytTrackVMuonAssoc.label = ('tevMuons:dyt',)
tevMuonDytTrackVMuonAssoc.muonHistoParameters = glbMuonHistoParameters

# cosmics 2-leg reco
trkCosmicMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkCosmicMuonTrackVSelMuonAssoc.associatormap = 'tpToTkCosmicSelMuonAssociation'
trkCosmicMuonTrackVSelMuonAssoc.label = ('ctfWithMaterialTracksP5LHCNavigation',)
trkCosmicMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
trkCosmicMuonTrackVSelMuonAssoc.muonTPSelector = cosmicMuonTPSet
trkCosmicMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
trkCosmicMuonTrackVSelMuonAssoc.muonHistoParameters = trkCosmicMuonHistoParameters

staCosmicMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staCosmicMuonTrackVSelMuonAssoc.associatormap = 'tpToStaCosmicSelMuonAssociation'
staCosmicMuonTrackVSelMuonAssoc.label = ('cosmicMuons',)
staCosmicMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
staCosmicMuonTrackVSelMuonAssoc.muonTPSelector = cosmicMuonTPSet
staCosmicMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
staCosmicMuonTrackVSelMuonAssoc.muonHistoParameters = staCosmicMuonHistoParameters

glbCosmicMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbCosmicMuonTrackVSelMuonAssoc.associatormap = 'tpToGlbCosmicSelMuonAssociation'
glbCosmicMuonTrackVSelMuonAssoc.label = ('globalCosmicMuons',)
glbCosmicMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
glbCosmicMuonTrackVSelMuonAssoc.muonTPSelector = cosmicMuonTPSet
glbCosmicMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
glbCosmicMuonTrackVSelMuonAssoc.muonHistoParameters = glbCosmicMuonHistoParameters

# cosmics 1-leg reco
trkCosmic1LegMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkCosmic1LegMuonTrackVSelMuonAssoc.associatormap = 'tpToTkCosmic1LegSelMuonAssociation'
trkCosmic1LegMuonTrackVSelMuonAssoc.label = ('ctfWithMaterialTracksP5',)
trkCosmic1LegMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
trkCosmic1LegMuonTrackVSelMuonAssoc.muonTPSelector = cosmicMuonTPSet
trkCosmic1LegMuonTrackVSelMuonAssoc.muonHistoParameters = trkCosmic1LegMuonHistoParameters

staCosmic1LegMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staCosmic1LegMuonTrackVSelMuonAssoc.associatormap = 'tpToStaCosmic1LegSelMuonAssociation'
staCosmic1LegMuonTrackVSelMuonAssoc.label = ('cosmicMuons1Leg',)
staCosmic1LegMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
staCosmic1LegMuonTrackVSelMuonAssoc.muonTPSelector = cosmicMuonTPSet
staCosmic1LegMuonTrackVSelMuonAssoc.muonHistoParameters = staCosmic1LegMuonHistoParameters

glbCosmic1LegMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbCosmic1LegMuonTrackVSelMuonAssoc.associatormap = 'tpToGlbCosmic1LegSelMuonAssociation'
glbCosmic1LegMuonTrackVSelMuonAssoc.label = ('globalCosmicMuons1Leg',)
glbCosmic1LegMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
glbCosmic1LegMuonTrackVSelMuonAssoc.muonTPSelector = cosmicMuonTPSet
glbCosmic1LegMuonTrackVSelMuonAssoc.muonHistoParameters = glbCosmic1LegMuonHistoParameters

##################################################################################
# Muon validation sequences using MuonTrackValidator
#
muonValidation_seq = cms.Sequence(
    probeTracks_seq + tpToTkMuonAssociation + trkProbeTrackVMuonAssoc
    +trackAssociatorByHits + tpToTkmuTrackAssociation + trkMuonTrackVTrackAssoc
    +seedsOfSTAmuons_seq + tpToStaSeedAssociation + staSeedTrackVMuonAssoc
    +tpToStaMuonAssociation + staMuonTrackVMuonAssoc
    +tpToStaUpdMuonAssociation + staUpdMuonTrackVMuonAssoc
    + tpToGlbMuonAssociation + glbMuonTrackVMuonAssoc
)

muonValidationTEV_seq = cms.Sequence(
    tpToTevFirstMuonAssociation + tevMuonFirstTrackVMuonAssoc
    +tpToTevPickyMuonAssociation + tevMuonPickyTrackVMuonAssoc
    +tpToTevDytMuonAssociation + tevMuonDytTrackVMuonAssoc
)

muonValidationRefit_seq = cms.Sequence(
    tpToStaRefitMuonAssociation + staRefitMuonTrackVMuonAssoc
    +tpToStaRefitUpdMuonAssociation + staRefitUpdMuonTrackVMuonAssoc
)

muonValidationDisplaced_seq = cms.Sequence(
    seedsOfDisplacedSTAmuons_seq + tpToDisplacedStaSeedAssociation + displacedStaSeedTrackVMuonAssoc
    +tpToDisplacedStaMuonAssociation + displacedStaMuonTrackVMuonAssoc
    +tpToDisplacedTrkMuonAssociation + displacedTrackVMuonAssoc
    +tpToDisplacedGlbMuonAssociation + displacedGlbMuonTrackVMuonAssoc
)

muonValidationSET_seq = cms.Sequence(
    tpToStaSETMuonAssociation + staSETMuonTrackVMuonAssoc
    +tpToStaSETUpdMuonAssociation + staSETUpdMuonTrackVMuonAssoc
    +tpToGlbSETMuonAssociation + glbSETMuonTrackVMuonAssoc
)

muonValidationCosmic_seq = cms.Sequence(
    tpToTkCosmicSelMuonAssociation + trkCosmicMuonTrackVSelMuonAssoc
    +tpToTkCosmic1LegSelMuonAssociation + trkCosmic1LegMuonTrackVSelMuonAssoc
    +tpToStaCosmicSelMuonAssociation + staCosmicMuonTrackVSelMuonAssoc
    +tpToStaCosmic1LegSelMuonAssociation + staCosmic1LegMuonTrackVSelMuonAssoc
    +tpToGlbCosmicSelMuonAssociation + glbCosmicMuonTrackVSelMuonAssoc
    +tpToGlbCosmic1LegSelMuonAssociation + glbCosmic1LegMuonTrackVSelMuonAssoc
)
#####################################################################################
# FEW sequences for BARREL and ENDCAPS separately !
#
# probe Tracks
barrelOnlyTrkProbeTrackVMuonAssoc = trkProbeTrackVMuonAssoc.clone()
barrelOnlyTrkProbeTrackVMuonAssoc.muonTPSelector = muonBarrelOnlyTPSet
barrelOnlyTrkProbeTrackVMuonAssoc.label = ('innerTracksBarrelOnly',)
barrelOnlyTrkProbeTrackVMuonAssoc.associatormap = 'tpToTkMuonAssociationBarrelOnly'

minusEndcapOnlyTrkProbeTrackVMuonAssoc = trkProbeTrackVMuonAssoc.clone()
minusEndcapOnlyTrkProbeTrackVMuonAssoc.muonTPSelector = muonMinusEndcapOnlyTPSet
minusEndcapOnlyTrkProbeTrackVMuonAssoc.label = ('innerTracksMinusEndcapOnly',)
minusEndcapOnlyTrkProbeTrackVMuonAssoc.associatormap = 'tpToTkMuonAssociationMinusEndcapOnly'

plusEndcapOnlyTrkProbeTrackVMuonAssoc = trkProbeTrackVMuonAssoc.clone()
plusEndcapOnlyTrkProbeTrackVMuonAssoc.muonTPSelector = muonPlusEndcapOnlyTPSet
plusEndcapOnlyTrkProbeTrackVMuonAssoc.label = ('innerTracksPlusEndcapOnly',)
plusEndcapOnlyTrkProbeTrackVMuonAssoc.associatormap = 'tpToTkMuonAssociationPlusEndcapOnly'

# GLB muons
barrelOnlyGlbMuonTrackVMuonAssoc = glbMuonTrackVMuonAssoc.clone()
barrelOnlyGlbMuonTrackVMuonAssoc.muonTPSelector = muonBarrelOnlyTPSet
barrelOnlyGlbMuonTrackVMuonAssoc.label = ('globalMuonsBarrelOnly',)
barrelOnlyGlbMuonTrackVMuonAssoc.associatormap = 'tpToGlbMuonAssociationBarrelOnly'

minusEndcapOnlyGlbMuonTrackVMuonAssoc = glbMuonTrackVMuonAssoc.clone()
minusEndcapOnlyGlbMuonTrackVMuonAssoc.muonTPSelector = muonMinusEndcapOnlyTPSet
minusEndcapOnlyGlbMuonTrackVMuonAssoc.label = ('globalMuonsMinusEndcapOnly',)
minusEndcapOnlyGlbMuonTrackVMuonAssoc.associatormap = 'tpToGlbMuonAssociationMinusEndcapOnly'

plusEndcapOnlyGlbMuonTrackVMuonAssoc = glbMuonTrackVMuonAssoc.clone()
plusEndcapOnlyGlbMuonTrackVMuonAssoc.muonTPSelector = muonPlusEndcapOnlyTPSet
plusEndcapOnlyGlbMuonTrackVMuonAssoc.label = ('globalMuonsPlusEndcapOnly',)
plusEndcapOnlyGlbMuonTrackVMuonAssoc.associatormap = 'tpToGlbMuonAssociationPlusEndcapOnly'

# TeV picky
barrelOnlyTevMuonPickyTrackVMuonAssoc = tevMuonPickyTrackVMuonAssoc.clone()
barrelOnlyTevMuonPickyTrackVMuonAssoc.muonTPSelector = muonBarrelOnlyTPSet
barrelOnlyTevMuonPickyTrackVMuonAssoc.label = ('pickyMuonsBarrelOnly',)
barrelOnlyTevMuonPickyTrackVMuonAssoc.associatormap = 'tpToTevPickyMuonAssociationBarrelOnly'

minusEndcapOnlyTevMuonPickyTrackVMuonAssoc = tevMuonPickyTrackVMuonAssoc.clone()
minusEndcapOnlyTevMuonPickyTrackVMuonAssoc.muonTPSelector = muonMinusEndcapOnlyTPSet
minusEndcapOnlyTevMuonPickyTrackVMuonAssoc.label = ('pickyMuonsMinusEndcapOnly',)
minusEndcapOnlyTevMuonPickyTrackVMuonAssoc.associatormap = 'tpToTevPickyMuonAssociationMinusEndcapOnly'

plusEndcapOnlyTevMuonPickyTrackVMuonAssoc = tevMuonPickyTrackVMuonAssoc.clone()
plusEndcapOnlyTevMuonPickyTrackVMuonAssoc.muonTPSelector = muonPlusEndcapOnlyTPSet
plusEndcapOnlyTevMuonPickyTrackVMuonAssoc.label = ('pickyMuonsPlusEndcapOnly',)
plusEndcapOnlyTevMuonPickyTrackVMuonAssoc.associatormap = 'tpToTevPickyMuonAssociationPlusEndcapOnly'

# STA muons
staMuonTrackVMuonAssocBarrelOnly = staMuonTrackVMuonAssoc.clone()
staMuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
staMuonTrackVMuonAssocBarrelOnly.label = ('staMuonsBarrelOnly',)
staMuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToStaMuonAssociationBarrelOnly'

staMuonTrackVMuonAssocMinusEndcapOnly = staMuonTrackVMuonAssoc.clone()
staMuonTrackVMuonAssocMinusEndcapOnly.muonTPSelector = muonMinusEndcapOnlyTPSet
staMuonTrackVMuonAssocMinusEndcapOnly.label = ('staMuonsMinusEndcapOnly',)
staMuonTrackVMuonAssocMinusEndcapOnly.associatormap = 'tpToStaMuonAssociationMinusEndcapOnly'

staMuonTrackVMuonAssocPlusEndcapOnly = staMuonTrackVMuonAssoc.clone()
staMuonTrackVMuonAssocPlusEndcapOnly.muonTPSelector = muonPlusEndcapOnlyTPSet
staMuonTrackVMuonAssocPlusEndcapOnly.label = ('staMuonsPlusEndcapOnly',)
staMuonTrackVMuonAssocPlusEndcapOnly.associatormap = 'tpToStaMuonAssociationPlusEndcapOnly'

# STA Upd muons
staUpdMuonTrackVMuonAssocBarrelOnly = staUpdMuonTrackVMuonAssoc.clone()
staUpdMuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
staUpdMuonTrackVMuonAssocBarrelOnly.label = ('staUpdMuonsBarrelOnly',)
staUpdMuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToUpdStaMuonAssociationBarrelOnly'

staUpdMuonTrackVMuonAssocMinusEndcapOnly = staUpdMuonTrackVMuonAssoc.clone()
staUpdMuonTrackVMuonAssocMinusEndcapOnly.muonTPSelector = muonMinusEndcapOnlyTPSet
staUpdMuonTrackVMuonAssocMinusEndcapOnly.label = ('staUpdMuonsMinusEndcapOnly',)
staUpdMuonTrackVMuonAssocMinusEndcapOnly.associatormap = 'tpToUpdStaMuonAssociationMinusEndcapOnly'

staUpdMuonTrackVMuonAssocPlusEndcapOnly = staUpdMuonTrackVMuonAssoc.clone()
staUpdMuonTrackVMuonAssocPlusEndcapOnly.muonTPSelector = muonPlusEndcapOnlyTPSet
staUpdMuonTrackVMuonAssocPlusEndcapOnly.label = ('staUpdMuonsPlusEndcapOnly',)
staUpdMuonTrackVMuonAssocPlusEndcapOnly.associatormap = 'tpToUpdStaMuonAssociationPlusEndcapOnly'

# displaced STA muons
displacedStaMuonTrackVMuonAssocBarrelOnly = displacedStaMuonTrackVMuonAssoc.clone()
displacedStaMuonTrackVMuonAssocBarrelOnly.muonTPSelector = muonBarrelOnlyTPSet
displacedStaMuonTrackVMuonAssocBarrelOnly.label = ('displacedStaMuonsBarrelOnly',)
displacedStaMuonTrackVMuonAssocBarrelOnly.associatormap = 'tpToDisplacedStaMuonAssociationBarrelOnly'


muonValidationBarrelOnly_seq = cms.Sequence(
    innerTracksBarrelOnly + tpToTkMuonAssociationBarrelOnly + barrelOnlyTrkProbeTrackVMuonAssoc
    +globalMuonsBarrelOnly + tpToGlbMuonAssociationBarrelOnly + barrelOnlyGlbMuonTrackVMuonAssoc
    +pickyMuonsBarrelOnly + tpToTevPickyMuonAssociationBarrelOnly + barrelOnlyTevMuonPickyTrackVMuonAssoc
    +staMuonsBarrelOnly + tpToStaMuonAssociationBarrelOnly + staMuonTrackVMuonAssocBarrelOnly
    +staUpdMuonsBarrelOnly + tpToUpdStaMuonAssociationBarrelOnly + staUpdMuonTrackVMuonAssocBarrelOnly
)

muonValidationMinusEndcapOnly_seq = cms.Sequence(
    innerTracksMinusEndcapOnly + tpToTkMuonAssociationMinusEndcapOnly + minusEndcapOnlyTrkProbeTrackVMuonAssoc
    +globalMuonsMinusEndcapOnly + tpToGlbMuonAssociationMinusEndcapOnly + minusEndcapOnlyGlbMuonTrackVMuonAssoc
    +pickyMuonsMinusEndcapOnly + tpToTevPickyMuonAssociationMinusEndcapOnly + minusEndcapOnlyTevMuonPickyTrackVMuonAssoc
    +staMuonsMinusEndcapOnly + tpToStaMuonAssociationMinusEndcapOnly + staMuonTrackVMuonAssocMinusEndcapOnly
    +staUpdMuonsMinusEndcapOnly + tpToUpdStaMuonAssociationMinusEndcapOnly + staUpdMuonTrackVMuonAssocMinusEndcapOnly
)

muonValidationPlusEndcapOnly_seq = cms.Sequence(
    innerTracksPlusEndcapOnly + tpToTkMuonAssociationPlusEndcapOnly + plusEndcapOnlyTrkProbeTrackVMuonAssoc
    +globalMuonsPlusEndcapOnly + tpToGlbMuonAssociationPlusEndcapOnly + plusEndcapOnlyGlbMuonTrackVMuonAssoc
    +pickyMuonsPlusEndcapOnly + tpToTevPickyMuonAssociationPlusEndcapOnly + plusEndcapOnlyTevMuonPickyTrackVMuonAssoc
    +staMuonsPlusEndcapOnly + tpToStaMuonAssociationPlusEndcapOnly + staMuonTrackVMuonAssocPlusEndcapOnly
    +staUpdMuonsPlusEndcapOnly + tpToUpdStaMuonAssociationPlusEndcapOnly + staUpdMuonTrackVMuonAssocPlusEndcapOnly
)

muonValidationSTABarrelOnly_seq = cms.Sequence(
    staMuonsBarrelOnly + tpToStaMuonAssociationBarrelOnly + staMuonTrackVMuonAssocBarrelOnly
    +staUpdMuonsBarrelOnly + tpToUpdStaMuonAssociationBarrelOnly + staUpdMuonTrackVMuonAssocBarrelOnly
    +displacedStaMuonsBarrelOnly + tpToDisplacedStaMuonAssociationBarrelOnly + displacedStaMuonTrackVMuonAssocBarrelOnly
)

#####################################################################################
# Configurations for RecoMuonValidator
#
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
from Validation.RecoMuon.RecoMuonValidator_cfi import *

#import SimGeneral.MixingModule.mixNoPU_cfi
from SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi import *
from SimMuon.MCTruth.MuonAssociatorByHits_cfi import muonAssociatorByHitsCommonParameters

#tracker
muonAssociatorByHitsNoSimHitsHelperTrk = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperTrk.UseTracker = True
muonAssociatorByHitsNoSimHitsHelperTrk.UseMuon  = False
recoMuonVMuAssoc_trk = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_trk.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_Trk'
recoMuonVMuAssoc_trk.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperTrk'
recoMuonVMuAssoc_trk.trackType = 'inner'
recoMuonVMuAssoc_trk.selection = "isTrackerMuon"

#tracker and PF
muonAssociatorByHitsNoSimHitsHelperTrkPF = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperTrkPF.UseTracker = True
muonAssociatorByHitsNoSimHitsHelperTrkPF.UseMuon  = False
recoMuonVMuAssoc_trkPF = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_trkPF.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_TrkPF'
recoMuonVMuAssoc_trkPF.usePFMuon = True
recoMuonVMuAssoc_trkPF.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperTrkPF'
recoMuonVMuAssoc_trkPF.trackType = 'inner'
recoMuonVMuAssoc_trkPF.selection = "isTrackerMuon & isPFMuon"

#standalone
muonAssociatorByHitsNoSimHitsHelperStandalone = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperStandalone.UseTracker = False
muonAssociatorByHitsNoSimHitsHelperStandalone.UseMuon  = True
recoMuonVMuAssoc_sta = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_sta.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_Sta'
recoMuonVMuAssoc_sta.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperStandalone'
recoMuonVMuAssoc_sta.trackType = 'outer'
recoMuonVMuAssoc_sta.selection = "isStandAloneMuon"

#seed of StandAlone
muonAssociatorByHitsNoSimHitsHelperSeedStandalone = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperSeedStandalone.UseTracker = False
muonAssociatorByHitsNoSimHitsHelperSeedStandalone.UseMuon  = True
recoMuonVMuAssoc_seedSta = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_seedSta.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_SeedSta'
recoMuonVMuAssoc_seedSta.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperStandalone'
recoMuonVMuAssoc_seedSta.trackType = 'outer'
recoMuonVMuAssoc_seedSta.selection = ""

#standalone and PF
muonAssociatorByHitsNoSimHitsHelperStandalonePF = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperStandalonePF.UseTracker = False
muonAssociatorByHitsNoSimHitsHelperStandalonePF.UseMuon  = True
recoMuonVMuAssoc_staPF = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_staPF.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_StaPF'
recoMuonVMuAssoc_staPF.usePFMuon = True
recoMuonVMuAssoc_staPF.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperStandalonePF'
recoMuonVMuAssoc_staPF.trackType = 'outer'
recoMuonVMuAssoc_staPF.selection = "isStandAloneMuon & isPFMuon"

#global
muonAssociatorByHitsNoSimHitsHelperGlobal = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperGlobal.UseTracker = True
muonAssociatorByHitsNoSimHitsHelperGlobal.UseMuon  = True
recoMuonVMuAssoc_glb = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_glb.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_Glb'
recoMuonVMuAssoc_glb.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperGlobal'
recoMuonVMuAssoc_glb.trackType = 'global'
recoMuonVMuAssoc_glb.selection = "isGlobalMuon"

#global and PF
muonAssociatorByHitsNoSimHitsHelperGlobalPF = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperGlobalPF.UseTracker = True
muonAssociatorByHitsNoSimHitsHelperGlobalPF.UseMuon  = True
recoMuonVMuAssoc_glbPF = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_glbPF.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_GlbPF'
recoMuonVMuAssoc_glbPF.usePFMuon = True
recoMuonVMuAssoc_glbPF.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperGlobalPF'
recoMuonVMuAssoc_glbPF.trackType = 'global'
recoMuonVMuAssoc_glbPF.selection = "isGlobalMuon & isPFMuon"

#tight
muonAssociatorByHitsNoSimHitsHelperTight = SimMuon.MCTruth.muonAssociatorByHitsNoSimHitsHelper_cfi.muonAssociatorByHitsNoSimHitsHelper.clone()
muonAssociatorByHitsNoSimHitsHelperTight.UseTracker = True
muonAssociatorByHitsNoSimHitsHelperTight.UseMuon  = True
recoMuonVMuAssoc_tgt = Validation.RecoMuon.RecoMuonValidator_cfi.recoMuonValidator.clone()
recoMuonVMuAssoc_tgt.subDir = 'Muons/RecoMuonV/RecoMuon_MuonAssoc_Tgt'
recoMuonVMuAssoc_tgt.muAssocLabel = 'muonAssociatorByHitsNoSimHitsHelperTight'
recoMuonVMuAssoc_tgt.trackType = 'global'
recoMuonVMuAssoc_tgt.selection = 'isGlobalMuon'
recoMuonVMuAssoc_tgt.wantTightMuon = True
recoMuonVMuAssoc_tgt.beamSpot = 'offlineBeamSpot'
recoMuonVMuAssoc_tgt.primaryVertex = 'offlinePrimaryVertices'

##########################################################################
# Muon validation sequence using RecoMuonValidator
#
muonValidationRMV_seq = cms.Sequence(
    muonAssociatorByHitsNoSimHitsHelperTrk +recoMuonVMuAssoc_trk
    +muonAssociatorByHitsNoSimHitsHelperStandalone +recoMuonVMuAssoc_sta
    +muonAssociatorByHitsNoSimHitsHelperGlobal +recoMuonVMuAssoc_glb
    +muonAssociatorByHitsNoSimHitsHelperTight +recoMuonVMuAssoc_tgt
    # 
    #    +muonAssociatorByHitsNoSimHitsHelperTrkPF +recoMuonVMuAssoc_trkPF
    #    +muonAssociatorByHitsNoSimHitsHelperStandalonePF +recoMuonVMuAssoc_staPF
    #    +muonAssociatorByHitsNoSimHitsHelperGlobalPF +recoMuonVMuAssoc_glbPF
    )

##########################################################################
# The full offline muon validation sequence
#
recoMuonValidation = cms.Sequence(
    muonValidation_seq + muonValidationTEV_seq + muonValidationRefit_seq + muonValidationDisplaced_seq + muonValidationSET_seq
    + muonValidationRMV_seq
    )

from Configuration.StandardSequences.Eras import eras
# no displaces or SET muons in fastsim
if eras.fastSim.isChosen():
    recoMuonValidation = cms.Sequence(muonValidation_seq + muonValidationTEV_seq + muonValidationRefit_seq)

# sequence for cosmic muons
recoCosmicMuonValidation = cms.Sequence(
    muonValidationCosmic_seq
    )
