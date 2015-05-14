import FWCore.ParameterSet.Config as cms

from SimTracker.TrackAssociation.LhcParametersDefinerForTP_cfi import *
from SimTracker.TrackAssociation.CosmicParametersDefinerForTP_cfi import *

muonTrackValidator = cms.EDAnalyzer("MuonTrackValidator",
    # input TrackingParticle collections
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    # input reco::Track collection
    label = cms.VInputTag(cms.InputTag("globalMuons")),
    # switches to be set according to the input Track collection to properly count SimHits
    usetracker = cms.bool(True),
    usemuon = cms.bool(True),
    #
    beamSpot = cms.InputTag("offlineBeamSpot"),
    # set true if you do not want that MTV launch an exception
    # if the track collection is missing (e.g. HLT):
    ignoremissingtrackcollection=cms.untracked.bool(False),
    #
    # select doing TRK/MUO hits plots
    do_TRKhitsPlots = cms.bool(True),
    do_MUOhitsPlots = cms.bool(True),
    #
    # define the TrackingParticleSelector for evaluation of efficiency
    signalOnlyTP = cms.bool(True),
    stableOnlyTP = cms.bool(True),   # era sempre stato false, ma a noi non interessano i decadimenti in volo !!! 
    chargedOnlyTP = cms.bool(True),
    pdgIdTP = cms.vint32(13,-13),
    minHitTP = cms.int32(0),
    ptMinTP = cms.double(0.9),
    minRapidityTP = cms.double(-2.4),
    maxRapidityTP = cms.double(2.4),
    tipTP = cms.double(3.5),
    lipTP = cms.double(30.0),
    # collision-like tracks
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    # cosmics tracks
    # parametersDefiner = cms.string('CosmicParametersDefinerForTP'), 
    #
    # map linking SimHits to TrackingParticles, needed for cosmics validation`
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"), 
    #
    # if !UseAssociators the association map has to be given in input 
    associators = cms.vstring('a_MuonAssociator'),
    UseAssociators = cms.bool(False),
    associatormap = cms.InputTag("tpToMuonTrackAssociation"),
    #
    # BiDirectional Logic for RecoToSim association corrects the Fake rates (counting ghosts and split tracks as fakes)
    #  setting it to False the ghost and split tracks are counted as good ones (old setting of Muon Validation up to CMSSW_3_6_0_pre4)
    #  the default setting is True: should NOT be changed !
    BiDirectional_RecoToSim_association = cms.bool(True),
    #
    # Output File / Directory
    outputFile = cms.string(''),           
    dirName = cms.string('Muons/RecoMuonV/MultiTrack/'),
    #
    # Parameters for plots                                    
    useFabsEta = cms.bool(False),
    minEta = cms.double(-2.5),
    maxEta = cms.double(2.5),
    nintEta = cms.int32(50),
    #
    minPt = cms.double(0.9),
    maxPt = cms.double(2000.),
    nintPt = cms.int32(50),      # TRK ha 40 con scala LOG da 0.05 a 1 TeV - e' ok con scala LOG (vd trk)
    useLogPt=cms.untracked.bool(True),
    useInvPt = cms.bool(False),
    #
    # here set for GLB tracks, redefined for TRK and STA tracks
    minHit = cms.double(-0.5),                            
    maxHit = cms.double(80.5),
    nintHit = cms.int32(81),
    #
    minDTHit = cms.double(-0.5),                            
    maxDTHit = cms.double(50.5),
    nintDTHit = cms.int32(51),
    #
    minCSCHit = cms.double(-0.5),                            
    maxCSCHit = cms.double(50.5),
    nintCSCHit = cms.int32(51),
    #
    minRPCHit = cms.double(-0.5),                            
    maxRPCHit = cms.double(10.5),
    nintRPCHit = cms.int32(11),
    #
    minPhi = cms.double(-3.1416),
    maxPhi = cms.double(3.1416),
    nintPhi = cms.int32(36),
    #
    minDxy = cms.double(-2.),  # per prompt particles e' ok cosi', per displaced muons vanno cambiati !
    maxDxy = cms.double(2.),   # metto 40 bins da -10. a 10.
    nintDxy = cms.int32(40),   # TRK ha 100 bins da -25. a +25 cm !!!
    #
    minDz = cms.double(-30.),  # come TRK e' rispetto al beamspot !!!  
    maxDz = cms.double(30.),
    nintDz = cms.int32(60),
    # TP production Radius        # per non disdpalced  muons ok cosi ' ??
    minRpos = cms.double(0.),     # per displaced per es. da 0. a 85. e 85 bins
    maxRpos = cms.double(4.),    # TRK ha 60 \bins da 0. a 60cm
    nintRpos = cms.int32(40),
    # TP production Z position    # cosi' e \' il TRK (il select per displaced va fino a 210cm in Z !)
    minZpos = cms.double(-30.),    # TRK ha 60 bins da --30 a 30cm   (e' rispetto al BeamSPot -> bunch length !!
    maxZpos = cms.double(30.),     # per diaplced fino a -210 - +210 cm -> 105 bins ?
    nintZpos = cms.int32(60),
    # Number of vertices (PU summary info)
    minPU = cms.double(-0.5),                            
    maxPU = cms.double(199.5),
    nintPU = cms.int32(100),
    # n TRK layers
    minLayers = cms.double(-0.5),                            
    maxLayers = cms.double(20.5),
    nintLayers = cms.int32(21),
    # n Pixel layers
    minPixels = cms.double(-0.5),                            
    maxPixels = cms.double(5.5),
    nintPixels = cms.int32(6),
    #
    ptRes_nbin = cms.int32(120),       # passo da 100 a 120   # forse ne bastano 60 direi !!!                       
    ptRes_rangeMin = cms.double(-0.3),    # TRK ha -0.1 / 0.1   con 100 bins 
    ptRes_rangeMax = cms.double(0.3),    # provo con 120 tra -3. e 3. x STA  n.b. x pt=1000 e' ancora poco...
    #
    # TRK ha 300 bins da -0.01 a +0.01    # muo aveva 100 bins da -0.05 a 0.05
    phiRes_nbin = cms.int32(100),         # devo allargarla per STA tracks tipo 100 bins da -0.1 a 0.1
    phiRes_rangeMin = cms.double(-0.01),
    phiRes_rangeMax = cms.double(0.01),
    #
    etaRes_rangeMin = cms.double(-0.02),     # ok per GLB e TRK limitare a 0.02 !!!  STA invece -0.1 - 0.1
    etaRes_rangeMax = cms.double(0.02),      # TRK ha 200 bins da -0.1 a 0.1 
    etaRes_nbin = cms.int32(80),               
    #
    #     TRK ha 300 bins  da -0.02 a +0.02     // MUO aveva 120 bins tra -0.01 e 0.01
    cotThetaRes_nbin = cms.int32(100),           # per STA allargo a -0.05 - 0.05  e 80- bins -> allargo a -0.1 +0.1 e 100 bins                       
    cotThetaRes_rangeMin = cms.double(-0.01),
    cotThetaRes_rangeMax = cms.double(0.01),
    #
    # TRK ha 500 bins tra -0.1 e +0.1     // MUO ora aveva 100 bins da -0.02 a 0.02
    dxyRes_nbin = cms.int32(100),         # faccio 100 bins tra -0.1 e 0.1 per TRK e GLB   (20 um)
    dxyRes_rangeMin = cms.double(-0.1),   # per STA provo 100 bins tra -4. e 4.  (400 um) -> non copre -> allargo tra -10 e 10.
    dxyRes_rangeMax = cms.double(0.1),    
    # TRK ha 150 bins tra -0.05  e +0.05  // MUO aveva lo stesso ora
    dzRes_nbin = cms.int32(100),          # cambio: 100 bins tra -0.1 e 0.1   (20 um)                         
    dzRes_rangeMin = cms.double(-0.1),    # per STA faccio 100 bins tra -4. e 4. -> non copre -> allargo tra -25 e 25.
    dzRes_rangeMax = cms.double(0.1)
)
