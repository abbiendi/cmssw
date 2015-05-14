#
# Production configuration for FullSim: muon track validation using MuonAssociatorByHits
#
import FWCore.ParameterSet.Config as cms

from Validation.RecoMuon.selectors_cff import *
from Validation.RecoMuon.associators_cff import *
import Validation.RecoMuon.MuonTrackValidator_cfi

from SimTracker.TrackAssociation.LhcParametersDefinerForTP_cfi import *
from SimTracker.TrackAssociation.CosmicParametersDefinerForTP_cfi import *

#
# quickTrackAssociatorByHits on probeTracks used as monitor wrt MuonAssociatorByHits
#
trkMuonTrackVTrackAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkMuonTrackVTrackAssoc.associatormap = 'tpToTkmuTrackAssociation'
trkMuonTrackVTrackAssoc.associators = ('trackAssociatorByHits',)
#trkMuonTrackVTrackAssoc.label = ('generalTracks',)
trkMuonTrackVTrackAssoc.label = ('probeTracks',)
trkMuonTrackVTrackAssoc.usetracker = True
trkMuonTrackVTrackAssoc.usemuon = False
##
trkMuonTrackVTrackAssoc.nintHit = 41
trkMuonTrackVTrackAssoc.maxHit = 40.5
trkMuonTrackVTrackAssoc.do_MUOhitsPlots = False

#
# MuonAssociatorByHits used for all track collections
#
trkProbeTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkProbeTrackVMuonAssoc.associatormap = 'tpToTkMuonAssociation' 
trkProbeTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
#trkProbeTrackVMuonAssoc.label = ('generalTracks',)
trkProbeTrackVMuonAssoc.label = ('probeTracks',)
trkProbeTrackVMuonAssoc.usetracker = True
trkProbeTrackVMuonAssoc.usemuon = False
##
trkProbeTrackVMuonAssoc.nintHit = 41
trkProbeTrackVMuonAssoc.maxHit = 40.5
trkProbeTrackVMuonAssoc.do_MUOhitsPlots = False

staSeedTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staSeedTrackVMuonAssoc.associatormap = 'tpToStaSeedAssociation'
staSeedTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staSeedTrackVMuonAssoc.label = ('seedsOfSTAmuons',)
staSeedTrackVMuonAssoc.usetracker = False
staSeedTrackVMuonAssoc.usemuon = True
##
staSeedTrackVMuonAssoc.nintHit = 7
staSeedTrackVMuonAssoc.maxHit = 6.5
staSeedTrackVMuonAssoc.nintDTHit = 7
staSeedTrackVMuonAssoc.maxDTHit = 6.5
staSeedTrackVMuonAssoc.nintCSCHit = 7
staSeedTrackVMuonAssoc.maxCSCHit = 6.5
staSeedTrackVMuonAssoc.nintRPCHit = 7
staSeedTrackVMuonAssoc.maxRPCHit = 6.5
staSeedTrackVMuonAssoc.do_TRKhitsPlots = False
##
staSeedTrackVMuonAssoc.minDxy = -10.
staSeedTrackVMuonAssoc.maxDxy = 10.
##
staSeedTrackVMuonAssoc.ptRes_nbin = 120
staSeedTrackVMuonAssoc.ptRes_rangeMin = -3.
staSeedTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staSeedTrackVMuonAssoc.phiRes_nbin = 80
staSeedTrackVMuonAssoc.phiRes_rangeMin = -0.1
staSeedTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staSeedTrackVMuonAssoc.etaRes_nbin = 80
staSeedTrackVMuonAssoc.etaRes_rangeMin = -0.1
staSeedTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staSeedTrackVMuonAssoc.cotThetaRes_nbin = 100
staSeedTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staSeedTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staSeedTrackVMuonAssoc.dxyRes_nbin = 100
staSeedTrackVMuonAssoc.dxyRes_rangeMin = -10.
staSeedTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staSeedTrackVMuonAssoc.dzRes_nbin = 100
staSeedTrackVMuonAssoc.dzRes_rangeMin = -25.
staSeedTrackVMuonAssoc.dzRes_rangeMax = 25.

staMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staMuonTrackVMuonAssoc.associatormap = 'tpToStaMuonAssociation'
staMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staMuonTrackVMuonAssoc.label = ('standAloneMuons',)
staMuonTrackVMuonAssoc.usetracker = False
staMuonTrackVMuonAssoc.usemuon = True
##
staMuonTrackVMuonAssoc.nintHit = 61
staMuonTrackVMuonAssoc.maxHit = 60.5
staMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
staMuonTrackVMuonAssoc.minDxy = -10.
staMuonTrackVMuonAssoc.maxDxy = 10.
##
staMuonTrackVMuonAssoc.ptRes_nbin = 120
staMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
staMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staMuonTrackVMuonAssoc.phiRes_nbin = 80
staMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
staMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staMuonTrackVMuonAssoc.etaRes_nbin = 80
staMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
staMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
staMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staMuonTrackVMuonAssoc.dxyRes_nbin = 100
staMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
staMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staMuonTrackVMuonAssoc.dzRes_nbin = 100
staMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
staMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

staUpdMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staUpdMuonTrackVMuonAssoc.associatormap = 'tpToStaUpdMuonAssociation'
staUpdMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staUpdMuonTrackVMuonAssoc.label = ('standAloneMuons:UpdatedAtVtx',)
staUpdMuonTrackVMuonAssoc.usetracker = False
staUpdMuonTrackVMuonAssoc.usemuon = True
##
staUpdMuonTrackVMuonAssoc.nintHit = 61
staUpdMuonTrackVMuonAssoc.maxHit = 60.5
staUpdMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
staUpdMuonTrackVMuonAssoc.minDxy = -10.
staUpdMuonTrackVMuonAssoc.maxDxy = 10.
##
staUpdMuonTrackVMuonAssoc.ptRes_nbin = 120
staUpdMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
staUpdMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staUpdMuonTrackVMuonAssoc.phiRes_nbin = 80
staUpdMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
staUpdMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staUpdMuonTrackVMuonAssoc.etaRes_nbin = 80
staUpdMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
staUpdMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staUpdMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
staUpdMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staUpdMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staUpdMuonTrackVMuonAssoc.dxyRes_nbin = 100
staUpdMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
staUpdMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staUpdMuonTrackVMuonAssoc.dzRes_nbin = 100
staUpdMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
staUpdMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

glbMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbMuonTrackVMuonAssoc.associatormap = 'tpToGlbMuonAssociation'
glbMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
glbMuonTrackVMuonAssoc.label = ('extractedGlobalMuons',)
glbMuonTrackVMuonAssoc.usetracker = True
glbMuonTrackVMuonAssoc.usemuon = True

staRefitMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staRefitMuonTrackVMuonAssoc.associatormap = 'tpToStaRefitMuonAssociation'
staRefitMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staRefitMuonTrackVMuonAssoc.label = ('refittedStandAloneMuons',)
staRefitMuonTrackVMuonAssoc.usetracker = False
staRefitMuonTrackVMuonAssoc.usemuon = True
##
staRefitMuonTrackVMuonAssoc.nintHit = 61
staRefitMuonTrackVMuonAssoc.maxHit = 60.5
staRefitMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
staRefitMuonTrackVMuonAssoc.minDxy = -10.
staRefitMuonTrackVMuonAssoc.maxDxy = 10.
##
staRefitMuonTrackVMuonAssoc.ptRes_nbin = 120
staRefitMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
staRefitMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staRefitMuonTrackVMuonAssoc.phiRes_nbin = 80
staRefitMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
staRefitMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staRefitMuonTrackVMuonAssoc.etaRes_nbin = 80
staRefitMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
staRefitMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staRefitMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
staRefitMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staRefitMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staRefitMuonTrackVMuonAssoc.dxyRes_nbin = 100
staRefitMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
staRefitMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staRefitMuonTrackVMuonAssoc.dzRes_nbin = 100
staRefitMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
staRefitMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

staRefitUpdMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staRefitUpdMuonTrackVMuonAssoc.associatormap = 'tpToStaRefitUpdMuonAssociation'
staRefitUpdMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staRefitUpdMuonTrackVMuonAssoc.label = ('refittedStandAloneMuons:UpdatedAtVtx',)
staRefitUpdMuonTrackVMuonAssoc.usetracker = False
staRefitUpdMuonTrackVMuonAssoc.usemuon = True
##
staRefitUpdMuonTrackVMuonAssoc.nintHit = 61
staRefitUpdMuonTrackVMuonAssoc.maxHit = 60.5
staRefitUpdMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
staRefitUpdMuonTrackVMuonAssoc.minDxy = -10.
staRefitUpdMuonTrackVMuonAssoc.maxDxy = 10.
##
staRefitUpdMuonTrackVMuonAssoc.ptRes_nbin = 120
staRefitUpdMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
staRefitUpdMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staRefitUpdMuonTrackVMuonAssoc.phiRes_nbin = 80
staRefitUpdMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
staRefitUpdMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staRefitUpdMuonTrackVMuonAssoc.etaRes_nbin = 80
staRefitUpdMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
staRefitUpdMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staRefitUpdMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
staRefitUpdMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staRefitUpdMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staRefitUpdMuonTrackVMuonAssoc.dxyRes_nbin = 100
staRefitUpdMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
staRefitUpdMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staRefitUpdMuonTrackVMuonAssoc.dzRes_nbin = 100
staRefitUpdMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
staRefitUpdMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

displacedTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedTrackVMuonAssoc.associatormap = 'tpToDisplacedTrkMuonAssociation'
displacedTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
displacedTrackVMuonAssoc.label = ('displacedTracks',)
displacedTrackVMuonAssoc.usetracker = True
displacedTrackVMuonAssoc.usemuon = False
displacedTrackVMuonAssoc.tipTP = 85.
displacedTrackVMuonAssoc.lipTP = 210.
#displacedTrackVMuonAssoc.stableOnlyTP = True   (ora default)
##
displacedTrackVMuonAssoc.nintHit = 41
displacedTrackVMuonAssoc.maxHit = 40.5
displacedTrackVMuonAssoc.do_MUOhitsPlots = False
##
displacedTrackVMuonAssoc.nintDxy = 85
displacedTrackVMuonAssoc.minDxy = -85.
displacedTrackVMuonAssoc.maxDxy = 85.
displacedTrackVMuonAssoc.nintDz = 84
displacedTrackVMuonAssoc.minDz = -210.
displacedTrackVMuonAssoc.maxDz = 210.
displacedTrackVMuonAssoc.nintRpos = 85
displacedTrackVMuonAssoc.minRpos = 0.
displacedTrackVMuonAssoc.maxRpos = 85.
displacedTrackVMuonAssoc.nintZpos = 84
displacedTrackVMuonAssoc.minZpos = -210.
displacedTrackVMuonAssoc.maxZpos = 210.

displacedStaSeedTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedStaSeedTrackVMuonAssoc.associatormap = 'tpToDisplacedStaSeedAssociation'
displacedStaSeedTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
displacedStaSeedTrackVMuonAssoc.label = ('seedsOfDisplacedSTAmuons',)
displacedStaSeedTrackVMuonAssoc.usetracker = False
displacedStaSeedTrackVMuonAssoc.usemuon = True
displacedStaSeedTrackVMuonAssoc.tipTP = cms.double(85.)
displacedStaSeedTrackVMuonAssoc.lipTP = cms.double(210.)
#displacedStaSeedTrackVMuonAssoc.stableOnlyTP = cms.bool(True)
#
displacedStaSeedTrackVMuonAssoc.nintHit = 7
displacedStaSeedTrackVMuonAssoc.maxHit = 6.5
displacedStaSeedTrackVMuonAssoc.nintDTHit = 7
displacedStaSeedTrackVMuonAssoc.maxDTHit = 6.5
displacedStaSeedTrackVMuonAssoc.nintCSCHit = 7
displacedStaSeedTrackVMuonAssoc.maxCSCHit = 6.5
displacedStaSeedTrackVMuonAssoc.nintRPCHit = 7
displacedStaSeedTrackVMuonAssoc.maxRPCHit = 6.5
displacedStaSeedTrackVMuonAssoc.do_TRKhitsPlots = False
##
displacedStaSeedTrackVMuonAssoc.nintDxy = 85
displacedStaSeedTrackVMuonAssoc.minDxy = -85.
displacedStaSeedTrackVMuonAssoc.maxDxy = 85.
displacedStaSeedTrackVMuonAssoc.nintDz = 84
displacedStaSeedTrackVMuonAssoc.minDz = -210.
displacedStaSeedTrackVMuonAssoc.maxDz = 210.
displacedStaSeedTrackVMuonAssoc.nintRpos = 85
displacedStaSeedTrackVMuonAssoc.minRpos = 0.
displacedStaSeedTrackVMuonAssoc.maxRpos = 85.
displacedStaSeedTrackVMuonAssoc.nintZpos = 84
displacedStaSeedTrackVMuonAssoc.minZpos = -210.
displacedStaSeedTrackVMuonAssoc.maxZpos = 210.
##
displacedStaSeedTrackVMuonAssoc.ptRes_nbin = 120
displacedStaSeedTrackVMuonAssoc.ptRes_rangeMin = -3.
displacedStaSeedTrackVMuonAssoc.ptRes_rangeMax = 3.
##
displacedStaSeedTrackVMuonAssoc.phiRes_nbin = 80
displacedStaSeedTrackVMuonAssoc.phiRes_rangeMin = -0.1
displacedStaSeedTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
displacedStaSeedTrackVMuonAssoc.etaRes_nbin = 80
displacedStaSeedTrackVMuonAssoc.etaRes_rangeMin = -0.1
displacedStaSeedTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
displacedStaSeedTrackVMuonAssoc.cotThetaRes_nbin = 100
displacedStaSeedTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
displacedStaSeedTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
displacedStaSeedTrackVMuonAssoc.dxyRes_nbin = 100
displacedStaSeedTrackVMuonAssoc.dxyRes_rangeMin = -10.
displacedStaSeedTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
displacedStaSeedTrackVMuonAssoc.dzRes_nbin = 100
displacedStaSeedTrackVMuonAssoc.dzRes_rangeMin = -25.
displacedStaSeedTrackVMuonAssoc.dzRes_rangeMax = 25.

displacedStaMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedStaMuonTrackVMuonAssoc.associatormap = 'tpToDisplacedStaMuonAssociation'
displacedStaMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
displacedStaMuonTrackVMuonAssoc.label = ('displacedStandAloneMuons',)
displacedStaMuonTrackVMuonAssoc.usetracker = False
displacedStaMuonTrackVMuonAssoc.usemuon = True
displacedStaMuonTrackVMuonAssoc.tipTP = cms.double(85.)
displacedStaMuonTrackVMuonAssoc.lipTP = cms.double(210.)
#displacedStaMuonTrackVMuonAssoc.stableOnlyTP = cms.bool(True)
##
displacedStaMuonTrackVMuonAssoc.nintHit = 61
displacedStaMuonTrackVMuonAssoc.maxHit = 60.5
displacedStaMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
displacedStaMuonTrackVMuonAssoc.nintDxy = 85
displacedStaMuonTrackVMuonAssoc.minDxy = -85.
displacedStaMuonTrackVMuonAssoc.maxDxy = 85.
displacedStaMuonTrackVMuonAssoc.nintDz = 84
displacedStaMuonTrackVMuonAssoc.minDz = -210.
displacedStaMuonTrackVMuonAssoc.maxDz = 210.
displacedStaMuonTrackVMuonAssoc.nintRpos = 85
displacedStaMuonTrackVMuonAssoc.minRpos = 0.
displacedStaMuonTrackVMuonAssoc.maxRpos = 85.
displacedStaMuonTrackVMuonAssoc.nintZpos = 84
displacedStaMuonTrackVMuonAssoc.minZpos = -210.
displacedStaMuonTrackVMuonAssoc.maxZpos = 210.
##
displacedStaMuonTrackVMuonAssoc.ptRes_nbin = 120
displacedStaMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
displacedStaMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
displacedStaMuonTrackVMuonAssoc.phiRes_nbin = 80
displacedStaMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
displacedStaMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
displacedStaMuonTrackVMuonAssoc.etaRes_nbin = 80
displacedStaMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
displacedStaMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
displacedStaMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
displacedStaMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
displacedStaMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
displacedStaMuonTrackVMuonAssoc.dxyRes_nbin = 100
displacedStaMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
displacedStaMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
displacedStaMuonTrackVMuonAssoc.dzRes_nbin = 100
displacedStaMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
displacedStaMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

displacedGlbMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
displacedGlbMuonTrackVMuonAssoc.associatormap = 'tpToDisplacedGlbMuonAssociation'
displacedGlbMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
displacedGlbMuonTrackVMuonAssoc.label = ('displacedGlobalMuons',)
displacedGlbMuonTrackVMuonAssoc.usetracker = True
displacedGlbMuonTrackVMuonAssoc.usemuon = True
displacedGlbMuonTrackVMuonAssoc.tipTP = cms.double(85.)
displacedGlbMuonTrackVMuonAssoc.lipTP = cms.double(210.)
#displacedGlbMuonTrackVMuonAssoc.stableOnlyTP = cms.bool(True)
##
displacedGlbMuonTrackVMuonAssoc.nintDxy = 85
displacedGlbMuonTrackVMuonAssoc.minDxy = -85.
displacedGlbMuonTrackVMuonAssoc.maxDxy = 85.
displacedGlbMuonTrackVMuonAssoc.nintDz = 84
displacedGlbMuonTrackVMuonAssoc.minDz = -210.
displacedGlbMuonTrackVMuonAssoc.maxDz = 210.
displacedGlbMuonTrackVMuonAssoc.nintRpos = 85
displacedGlbMuonTrackVMuonAssoc.minRpos = 0.
displacedGlbMuonTrackVMuonAssoc.maxRpos = 85.
displacedGlbMuonTrackVMuonAssoc.nintZpos = 84
displacedGlbMuonTrackVMuonAssoc.minZpos = -210.
displacedGlbMuonTrackVMuonAssoc.maxZpos = 210.

staSETMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staSETMuonTrackVMuonAssoc.associatormap = 'tpToStaSETMuonAssociation'
staSETMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staSETMuonTrackVMuonAssoc.label = ('standAloneSETMuons',)
staSETMuonTrackVMuonAssoc.usetracker = False
staSETMuonTrackVMuonAssoc.usemuon = True
##
staSETMuonTrackVMuonAssoc.nintHit = 61
staSETMuonTrackVMuonAssoc.maxHit = 60.5
staSETMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
staSETMuonTrackVMuonAssoc.minDxy = -10.
staSETMuonTrackVMuonAssoc.maxDxy = 10.
##
staSETMuonTrackVMuonAssoc.ptRes_nbin = 120
staSETMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
staSETMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staSETMuonTrackVMuonAssoc.phiRes_nbin = 80
staSETMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
staSETMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staSETMuonTrackVMuonAssoc.etaRes_nbin = 80
staSETMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
staSETMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staSETMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
staSETMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staSETMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staSETMuonTrackVMuonAssoc.dxyRes_nbin = 100
staSETMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
staSETMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staSETMuonTrackVMuonAssoc.dzRes_nbin = 100
staSETMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
staSETMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

staSETUpdMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staSETUpdMuonTrackVMuonAssoc.associatormap = 'tpToStaSETUpdMuonAssociation'
staSETUpdMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
staSETUpdMuonTrackVMuonAssoc.label = ('standAloneSETMuons:UpdatedAtVtx',)
staSETUpdMuonTrackVMuonAssoc.usetracker = False
staSETUpdMuonTrackVMuonAssoc.usemuon = True
##
staSETUpdMuonTrackVMuonAssoc.nintHit = 61
staSETUpdMuonTrackVMuonAssoc.maxHit = 60.5
staSETUpdMuonTrackVMuonAssoc.do_TRKhitsPlots = False
##
staSETUpdMuonTrackVMuonAssoc.minDxy = -10.
staSETUpdMuonTrackVMuonAssoc.maxDxy = 10.
##
staSETUpdMuonTrackVMuonAssoc.ptRes_nbin = 120
staSETUpdMuonTrackVMuonAssoc.ptRes_rangeMin = -3.
staSETUpdMuonTrackVMuonAssoc.ptRes_rangeMax = 3.
##
staSETUpdMuonTrackVMuonAssoc.phiRes_nbin = 80
staSETUpdMuonTrackVMuonAssoc.phiRes_rangeMin = -0.1
staSETUpdMuonTrackVMuonAssoc.phiRes_rangeMax = 0.1
##
staSETUpdMuonTrackVMuonAssoc.etaRes_nbin = 80
staSETUpdMuonTrackVMuonAssoc.etaRes_rangeMin = -0.1
staSETUpdMuonTrackVMuonAssoc.etaRes_rangeMax = 0.1
##
staSETUpdMuonTrackVMuonAssoc.cotThetaRes_nbin = 100
staSETUpdMuonTrackVMuonAssoc.cotThetaRes_rangeMin = -0.1
staSETUpdMuonTrackVMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staSETUpdMuonTrackVMuonAssoc.dxyRes_nbin = 100
staSETUpdMuonTrackVMuonAssoc.dxyRes_rangeMin = -10.
staSETUpdMuonTrackVMuonAssoc.dxyRes_rangeMax = 10.
##
staSETUpdMuonTrackVMuonAssoc.dzRes_nbin = 100
staSETUpdMuonTrackVMuonAssoc.dzRes_rangeMin = -25.
staSETUpdMuonTrackVMuonAssoc.dzRes_rangeMax = 25.

glbSETMuonTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbSETMuonTrackVMuonAssoc.associatormap = 'tpToGlbSETMuonAssociation'
glbSETMuonTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
glbSETMuonTrackVMuonAssoc.label = ('globalSETMuons',)
glbSETMuonTrackVMuonAssoc.usetracker = True
glbSETMuonTrackVMuonAssoc.usemuon = True

tevMuonFirstTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
tevMuonFirstTrackVMuonAssoc.associatormap = 'tpToTevFirstMuonAssociation'
tevMuonFirstTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
tevMuonFirstTrackVMuonAssoc.label = ('tevMuons:firstHit',)
tevMuonFirstTrackVMuonAssoc.usetracker = True
tevMuonFirstTrackVMuonAssoc.usemuon = True

tevMuonPickyTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
tevMuonPickyTrackVMuonAssoc.associatormap = 'tpToTevPickyMuonAssociation'
tevMuonPickyTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
tevMuonPickyTrackVMuonAssoc.label = ('tevMuons:picky',)
tevMuonPickyTrackVMuonAssoc.usetracker = True
tevMuonPickyTrackVMuonAssoc.usemuon = True

tevMuonDytTrackVMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
tevMuonDytTrackVMuonAssoc.associatormap = 'tpToTevDytMuonAssociation'
tevMuonDytTrackVMuonAssoc.associators = ('MuonAssociationByHits',)
tevMuonDytTrackVMuonAssoc.label = ('tevMuons:dyt',)
tevMuonDytTrackVMuonAssoc.usetracker = True
tevMuonDytTrackVMuonAssoc.usemuon = True

# cosmics 2-leg reco
trkCosmicMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkCosmicMuonTrackVSelMuonAssoc.associatormap = 'tpToTkCosmicSelMuonAssociation'
trkCosmicMuonTrackVSelMuonAssoc.associators = ('MuonAssociationByHits',)
trkCosmicMuonTrackVSelMuonAssoc.label = ('ctfWithMaterialTracksP5LHCNavigation',)
trkCosmicMuonTrackVSelMuonAssoc.usetracker = True
trkCosmicMuonTrackVSelMuonAssoc.usemuon = False
trkCosmicMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
trkCosmicMuonTrackVSelMuonAssoc.ptMinTP = 1.
trkCosmicMuonTrackVSelMuonAssoc.tipTP = 85.
trkCosmicMuonTrackVSelMuonAssoc.lipTP = 210.
trkCosmicMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
##
trkCosmicMuonTrackVSelMuonAssoc.nintHit = 41
trkCosmicMuonTrackVSelMuonAssoc.maxHit = 40.5
trkCosmicMuonTrackVSelMuonAssoc.do_MUOhitsPlots = False
##
trkCosmicMuonTrackVSelMuonAssoc.nintDxy = 40
trkCosmicMuonTrackVSelMuonAssoc.minDxy = -10. 
trkCosmicMuonTrackVSelMuonAssoc.maxDxy = 10.
trkCosmicMuonTrackVSelMuonAssoc.nintDz = 50
trkCosmicMuonTrackVSelMuonAssoc.minDz = -50.
trkCosmicMuonTrackVSelMuonAssoc.maxDz = 50.
trkCosmicMuonTrackVSelMuonAssoc.nintRpos = 40 
trkCosmicMuonTrackVSelMuonAssoc.minRpos = 0.
trkCosmicMuonTrackVSelMuonAssoc.maxRpos = 10.
trkCosmicMuonTrackVSelMuonAssoc.nintZpos = 50
trkCosmicMuonTrackVSelMuonAssoc.minZpos = -50.
trkCosmicMuonTrackVSelMuonAssoc.maxZpos = 50.

staCosmicMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staCosmicMuonTrackVSelMuonAssoc.associatormap = 'tpToStaCosmicSelMuonAssociation'
staCosmicMuonTrackVSelMuonAssoc.associators = ('MuonAssociationByHits',)
staCosmicMuonTrackVSelMuonAssoc.label = ('cosmicMuons',)
staCosmicMuonTrackVSelMuonAssoc.usetracker = False
staCosmicMuonTrackVSelMuonAssoc.usemuon = True
staCosmicMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
staCosmicMuonTrackVSelMuonAssoc.ptMinTP = 1.
staCosmicMuonTrackVSelMuonAssoc.tipTP = 85.
staCosmicMuonTrackVSelMuonAssoc.lipTP = 210.
staCosmicMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
##
staCosmicMuonTrackVSelMuonAssoc.nintHit = 61
staCosmicMuonTrackVSelMuonAssoc.maxHit = 60.5
staCosmicMuonTrackVSelMuonAssoc.do_TRKhitsPlots = False
##
staCosmicMuonTrackVSelMuonAssoc.nintDxy = 40
staCosmicMuonTrackVSelMuonAssoc.minDxy = -10. 
staCosmicMuonTrackVSelMuonAssoc.maxDxy = 10.
staCosmicMuonTrackVSelMuonAssoc.nintDz = 50
staCosmicMuonTrackVSelMuonAssoc.minDz = -50.
staCosmicMuonTrackVSelMuonAssoc.maxDz = 50.
staCosmicMuonTrackVSelMuonAssoc.nintRpos = 40 
staCosmicMuonTrackVSelMuonAssoc.minRpos = 0.
staCosmicMuonTrackVSelMuonAssoc.maxRpos = 10.
staCosmicMuonTrackVSelMuonAssoc.nintZpos = 50
staCosmicMuonTrackVSelMuonAssoc.minZpos = -50.
staCosmicMuonTrackVSelMuonAssoc.maxZpos = 50.
##
staCosmicMuonTrackVSelMuonAssoc.ptRes_nbin = 120
staCosmicMuonTrackVSelMuonAssoc.ptRes_rangeMin = -3.
staCosmicMuonTrackVSelMuonAssoc.ptRes_rangeMax = 3.
##
staCosmicMuonTrackVSelMuonAssoc.phiRes_nbin = 80
staCosmicMuonTrackVSelMuonAssoc.phiRes_rangeMin = -0.1
staCosmicMuonTrackVSelMuonAssoc.phiRes_rangeMax = 0.1
##
staCosmicMuonTrackVSelMuonAssoc.etaRes_nbin = 80
staCosmicMuonTrackVSelMuonAssoc.etaRes_rangeMin = -0.1
staCosmicMuonTrackVSelMuonAssoc.etaRes_rangeMax = 0.1
##
staCosmicMuonTrackVSelMuonAssoc.cotThetaRes_nbin = 100
staCosmicMuonTrackVSelMuonAssoc.cotThetaRes_rangeMin = -0.1
staCosmicMuonTrackVSelMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staCosmicMuonTrackVSelMuonAssoc.dxyRes_nbin = 100
staCosmicMuonTrackVSelMuonAssoc.dxyRes_rangeMin = -10.
staCosmicMuonTrackVSelMuonAssoc.dxyRes_rangeMax = 10.
##
staCosmicMuonTrackVSelMuonAssoc.dzRes_nbin = 100
staCosmicMuonTrackVSelMuonAssoc.dzRes_rangeMin = -25.
staCosmicMuonTrackVSelMuonAssoc.dzRes_rangeMax = 25.

glbCosmicMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbCosmicMuonTrackVSelMuonAssoc.associatormap = 'tpToGlbCosmicSelMuonAssociation'
glbCosmicMuonTrackVSelMuonAssoc.associators = ('MuonAssociationByHits',)
glbCosmicMuonTrackVSelMuonAssoc.label = ('globalCosmicMuons',)
glbCosmicMuonTrackVSelMuonAssoc.usetracker = True
glbCosmicMuonTrackVSelMuonAssoc.usemuon = True
glbCosmicMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
glbCosmicMuonTrackVSelMuonAssoc.ptMinTP = 1.
glbCosmicMuonTrackVSelMuonAssoc.tipTP = 85.
glbCosmicMuonTrackVSelMuonAssoc.lipTP = 210.
glbCosmicMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
##
glbCosmicMuonTrackVSelMuonAssoc.nintDxy = 40
glbCosmicMuonTrackVSelMuonAssoc.minDxy = -10. 
glbCosmicMuonTrackVSelMuonAssoc.maxDxy = 10.
glbCosmicMuonTrackVSelMuonAssoc.nintDz = 50
glbCosmicMuonTrackVSelMuonAssoc.minDz = -50.
glbCosmicMuonTrackVSelMuonAssoc.maxDz = 50.
glbCosmicMuonTrackVSelMuonAssoc.nintRpos = 40 
glbCosmicMuonTrackVSelMuonAssoc.minRpos = 0.
glbCosmicMuonTrackVSelMuonAssoc.maxRpos = 10.
glbCosmicMuonTrackVSelMuonAssoc.nintZpos = 50
glbCosmicMuonTrackVSelMuonAssoc.minZpos = -50.
glbCosmicMuonTrackVSelMuonAssoc.maxZpos = 50.

# cosmics 1-leg reco
trkCosmic1LegMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
trkCosmic1LegMuonTrackVSelMuonAssoc.associatormap = 'tpToTkCosmic1LegSelMuonAssociation'
trkCosmic1LegMuonTrackVSelMuonAssoc.associators = ('MuonAssociationByHits',)
trkCosmic1LegMuonTrackVSelMuonAssoc.label = ('ctfWithMaterialTracksP5',)
trkCosmic1LegMuonTrackVSelMuonAssoc.usetracker = True
trkCosmic1LegMuonTrackVSelMuonAssoc.usemuon = False
trkCosmic1LegMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
trkCosmic1LegMuonTrackVSelMuonAssoc.ptMinTP = 1.
trkCosmic1LegMuonTrackVSelMuonAssoc.tipTP = 85.
trkCosmic1LegMuonTrackVSelMuonAssoc.lipTP = 210.
trkCosmic1LegMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
##
trkCosmic1LegMuonTrackVSelMuonAssoc.nintLayers = 31
trkCosmic1LegMuonTrackVSelMuonAssoc.maxLayers = 30.5
trkCosmic1LegMuonTrackVSelMuonAssoc.nintPixels = 11
trkCosmic1LegMuonTrackVSelMuonAssoc.maxPixels = 10.5
trkCosmic1LegMuonTrackVSelMuonAssoc.do_MUOhitsPlots = False
##
trkCosmic1LegMuonTrackVSelMuonAssoc.nintDxy = 40
trkCosmic1LegMuonTrackVSelMuonAssoc.minDxy = -10. 
trkCosmic1LegMuonTrackVSelMuonAssoc.maxDxy = 10.
trkCosmic1LegMuonTrackVSelMuonAssoc.nintDz = 50
trkCosmic1LegMuonTrackVSelMuonAssoc.minDz = -50.
trkCosmic1LegMuonTrackVSelMuonAssoc.maxDz = 50.
trkCosmic1LegMuonTrackVSelMuonAssoc.nintRpos = 40 
trkCosmic1LegMuonTrackVSelMuonAssoc.minRpos = 0.
trkCosmic1LegMuonTrackVSelMuonAssoc.maxRpos = 10.
trkCosmic1LegMuonTrackVSelMuonAssoc.nintZpos = 50
trkCosmic1LegMuonTrackVSelMuonAssoc.minZpos = -50.
trkCosmic1LegMuonTrackVSelMuonAssoc.maxZpos = 50.

staCosmic1LegMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
staCosmic1LegMuonTrackVSelMuonAssoc.associatormap = 'tpToStaCosmic1LegSelMuonAssociation'
staCosmic1LegMuonTrackVSelMuonAssoc.associators = ('MuonAssociationByHits',)
staCosmic1LegMuonTrackVSelMuonAssoc.label = ('cosmicMuons1Leg',)
staCosmic1LegMuonTrackVSelMuonAssoc.usetracker = False
staCosmic1LegMuonTrackVSelMuonAssoc.usemuon = True
staCosmic1LegMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
staCosmic1LegMuonTrackVSelMuonAssoc.ptMinTP = 1.
staCosmic1LegMuonTrackVSelMuonAssoc.tipTP = 85.
staCosmic1LegMuonTrackVSelMuonAssoc.lipTP = 210.
staCosmic1LegMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
##
staCosmic1LegMuonTrackVSelMuonAssoc.nintHit = 121
staCosmic1LegMuonTrackVSelMuonAssoc.maxHit = 120.5
staCosmic1LegMuonTrackVSelMuonAssoc.nintDTHit = 101
staCosmic1LegMuonTrackVSelMuonAssoc.maxDTHit = 100.5
staCosmic1LegMuonTrackVSelMuonAssoc.nintCSCHit = 101
staCosmic1LegMuonTrackVSelMuonAssoc.maxCSCHit = 100.5
staCosmic1LegMuonTrackVSelMuonAssoc.nintRPCHit = 21
staCosmic1LegMuonTrackVSelMuonAssoc.maxRPCHit = 20.5
staCosmic1LegMuonTrackVSelMuonAssoc.do_TRKhitsPlots = False
##
staCosmic1LegMuonTrackVSelMuonAssoc.nintDxy = 40
staCosmic1LegMuonTrackVSelMuonAssoc.minDxy = -10. 
staCosmic1LegMuonTrackVSelMuonAssoc.maxDxy = 10.
staCosmic1LegMuonTrackVSelMuonAssoc.nintDz = 50
staCosmic1LegMuonTrackVSelMuonAssoc.minDz = -50.
staCosmic1LegMuonTrackVSelMuonAssoc.maxDz = 50.
staCosmic1LegMuonTrackVSelMuonAssoc.nintRpos = 40 
staCosmic1LegMuonTrackVSelMuonAssoc.minRpos = 0.
staCosmic1LegMuonTrackVSelMuonAssoc.maxRpos = 10.
staCosmic1LegMuonTrackVSelMuonAssoc.nintZpos = 50
staCosmic1LegMuonTrackVSelMuonAssoc.minZpos = -50.
staCosmic1LegMuonTrackVSelMuonAssoc.maxZpos = 50.
##
staCosmic1LegMuonTrackVSelMuonAssoc.ptRes_nbin = 120
staCosmic1LegMuonTrackVSelMuonAssoc.ptRes_rangeMin = -3.
staCosmic1LegMuonTrackVSelMuonAssoc.ptRes_rangeMax = 3.
##
staCosmic1LegMuonTrackVSelMuonAssoc.phiRes_nbin = 80
staCosmic1LegMuonTrackVSelMuonAssoc.phiRes_rangeMin = -0.1
staCosmic1LegMuonTrackVSelMuonAssoc.phiRes_rangeMax = 0.1
##
staCosmic1LegMuonTrackVSelMuonAssoc.etaRes_nbin = 80
staCosmic1LegMuonTrackVSelMuonAssoc.etaRes_rangeMin = -0.1
staCosmic1LegMuonTrackVSelMuonAssoc.etaRes_rangeMax = 0.1
##
staCosmic1LegMuonTrackVSelMuonAssoc.cotThetaRes_nbin = 100
staCosmic1LegMuonTrackVSelMuonAssoc.cotThetaRes_rangeMin = -0.1
staCosmic1LegMuonTrackVSelMuonAssoc.cotThetaRes_rangeMax = 0.1
##
staCosmic1LegMuonTrackVSelMuonAssoc.dxyRes_nbin = 100
staCosmic1LegMuonTrackVSelMuonAssoc.dxyRes_rangeMin = -10.
staCosmic1LegMuonTrackVSelMuonAssoc.dxyRes_rangeMax = 10.
##
staCosmic1LegMuonTrackVSelMuonAssoc.dzRes_nbin = 100
staCosmic1LegMuonTrackVSelMuonAssoc.dzRes_rangeMin = -25.
staCosmic1LegMuonTrackVSelMuonAssoc.dzRes_rangeMax = 25.

glbCosmic1LegMuonTrackVSelMuonAssoc = Validation.RecoMuon.MuonTrackValidator_cfi.muonTrackValidator.clone()
glbCosmic1LegMuonTrackVSelMuonAssoc.associatormap = 'tpToGlbCosmic1LegSelMuonAssociation'
glbCosmic1LegMuonTrackVSelMuonAssoc.associators = ('MuonAssociationByHits',)
glbCosmic1LegMuonTrackVSelMuonAssoc.label = ('globalCosmicMuons1Leg',)
glbCosmic1LegMuonTrackVSelMuonAssoc.usetracker = True
glbCosmic1LegMuonTrackVSelMuonAssoc.usemuon = True
glbCosmic1LegMuonTrackVSelMuonAssoc.parametersDefiner = cms.string('CosmicParametersDefinerForTP')
glbCosmic1LegMuonTrackVSelMuonAssoc.ptMinTP = 1.
glbCosmic1LegMuonTrackVSelMuonAssoc.tipTP = 85.
glbCosmic1LegMuonTrackVSelMuonAssoc.lipTP = 210.
glbCosmic1LegMuonTrackVSelMuonAssoc.BiDirectional_RecoToSim_association = False
##
glbCosmic1LegMuonTrackVSelMuonAssoc.nintHit = 161
glbCosmic1LegMuonTrackVSelMuonAssoc.maxHit = 160.5
glbCosmic1LegMuonTrackVSelMuonAssoc.nintDTHit = 101
glbCosmic1LegMuonTrackVSelMuonAssoc.maxDTHit = 100.5
glbCosmic1LegMuonTrackVSelMuonAssoc.nintCSCHit = 101
glbCosmic1LegMuonTrackVSelMuonAssoc.maxCSCHit = 100.5
glbCosmic1LegMuonTrackVSelMuonAssoc.nintRPCHit = 21
glbCosmic1LegMuonTrackVSelMuonAssoc.maxRPCHit = 20.5
glbCosmic1LegMuonTrackVSelMuonAssoc.nintLayers = 31 
glbCosmic1LegMuonTrackVSelMuonAssoc.maxLayers = 30.5
glbCosmic1LegMuonTrackVSelMuonAssoc.nintPixels = 11
glbCosmic1LegMuonTrackVSelMuonAssoc.maxPixels = 10.5
##
glbCosmic1LegMuonTrackVSelMuonAssoc.nintDxy = 40
glbCosmic1LegMuonTrackVSelMuonAssoc.minDxy = -10. 
glbCosmic1LegMuonTrackVSelMuonAssoc.maxDxy = 10.
glbCosmic1LegMuonTrackVSelMuonAssoc.nintDz = 50
glbCosmic1LegMuonTrackVSelMuonAssoc.minDz = -50.
glbCosmic1LegMuonTrackVSelMuonAssoc.maxDz = 50.
glbCosmic1LegMuonTrackVSelMuonAssoc.nintRpos = 40 
glbCosmic1LegMuonTrackVSelMuonAssoc.minRpos = 0.
glbCosmic1LegMuonTrackVSelMuonAssoc.maxRpos = 10.
glbCosmic1LegMuonTrackVSelMuonAssoc.nintZpos = 50
glbCosmic1LegMuonTrackVSelMuonAssoc.minZpos = -50.
glbCosmic1LegMuonTrackVSelMuonAssoc.maxZpos = 50.

##################################################################################
# Muon validation sequences using MuonTrackValidator
#
muonValidation_seq = cms.Sequence(
    probeTracks_seq + tpToTkMuonAssociation + trkProbeTrackVMuonAssoc
    +trackAssociatorByHits + tpToTkmuTrackAssociation + trkMuonTrackVTrackAssoc
    +seedsOfSTAmuons_seq + tpToStaSeedAssociation + staSeedTrackVMuonAssoc
    +tpToStaMuonAssociation + staMuonTrackVMuonAssoc
    +tpToStaUpdMuonAssociation + staUpdMuonTrackVMuonAssoc
    +extractedMuonTracks_seq + tpToGlbMuonAssociation + glbMuonTrackVMuonAssoc
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

# sequence for cosmic muons
recoCosmicMuonValidation = cms.Sequence(
    muonValidationCosmic_seq
    )
