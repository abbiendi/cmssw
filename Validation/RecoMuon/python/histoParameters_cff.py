import FWCore.ParameterSet.Config as cms

defaultMuonHistoParameters = cms.PSet(
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
    #
    # switches to be set according to the input Track collection to properly count the number of hits in Eff vs N(SimHits)
    usetracker = cms.bool(True),
    usemuon = cms.bool(True),
    # here set for GLB tracks, redefined for TRK and STA tracks
    minNHit = cms.double(-0.5),                            
    maxNHit = cms.double(80.5),
    nintNHit = cms.int32(81),
    #
    # select doing TRK/MUO hits plots
    do_TRKhitsPlots = cms.bool(True),
    do_MUOhitsPlots = cms.bool(True),
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

#####################################################################################
# TRK tracks
trkMuonHistoParameters =  defaultMuonHistoParameters.clone()
trkMuonHistoParameters.usetracker = True
trkMuonHistoParameters.usemuon = False
trkMuonHistoParameters.nintNHit = 41
trkMuonHistoParameters.minNHit = -0.5
trkMuonHistoParameters.maxNHit = 40.5
trkMuonHistoParameters.do_TRKhitsPlots = True
trkMuonHistoParameters.do_MUOhitsPlots = False
#####################################################################################
# STA seeds
staSeedMuonHistoParameters = defaultMuonHistoParameters.clone()
staSeedMuonHistoParameters.usetracker = False
staSeedMuonHistoParameters.usemuon = True
staSeedMuonHistoParameters.nintNHit = 7
staSeedMuonHistoParameters.minNHit = -0.5
staSeedMuonHistoParameters.maxNHit = 6.5
staSeedMuonHistoParameters.do_TRKhitsPlots = False
staSeedMuonHistoParameters.do_MUOhitsPlots = True
staSeedMuonHistoParameters.nintDTHit = 7
staSeedMuonHistoParameters.maxDTHit = 6.5
staSeedMuonHistoParameters.nintCSCHit = 7
staSeedMuonHistoParameters.maxCSCHit = 6.5
staSeedMuonHistoParameters.nintRPCHit = 7
staSeedMuonHistoParameters.maxRPCHit = 6.5
##
staSeedMuonHistoParameters.minDxy = -10.
staSeedMuonHistoParameters.maxDxy = 10.
##
staSeedMuonHistoParameters.ptRes_nbin = 120
staSeedMuonHistoParameters.ptRes_rangeMin = -3.
staSeedMuonHistoParameters.ptRes_rangeMax = 3.
##
staSeedMuonHistoParameters.phiRes_nbin = 80
staSeedMuonHistoParameters.phiRes_rangeMin = -0.1
staSeedMuonHistoParameters.phiRes_rangeMax = 0.1
##
staSeedMuonHistoParameters.etaRes_nbin = 80
staSeedMuonHistoParameters.etaRes_rangeMin = -0.1
staSeedMuonHistoParameters.etaRes_rangeMax = 0.1
##
staSeedMuonHistoParameters.cotThetaRes_nbin = 100
staSeedMuonHistoParameters.cotThetaRes_rangeMin = -0.1
staSeedMuonHistoParameters.cotThetaRes_rangeMax = 0.1
##
staSeedMuonHistoParameters.dxyRes_nbin = 100
staSeedMuonHistoParameters.dxyRes_rangeMin = -10.
staSeedMuonHistoParameters.dxyRes_rangeMax = 10.
##
staSeedMuonHistoParameters.dzRes_nbin = 100
staSeedMuonHistoParameters.dzRes_rangeMin = -25.
staSeedMuonHistoParameters.dzRes_rangeMax = 25.
#####################################################################################
# STA tracks
staMuonHistoParameters = defaultMuonHistoParameters.clone()
staMuonHistoParameters.usetracker = False
staMuonHistoParameters.usemuon = True
staMuonHistoParameters.nintNHit = 61
staMuonHistoParameters.minNHit = -0.5
staMuonHistoParameters.maxNHit = 60.5
staMuonHistoParameters.do_TRKhitsPlots = False
staMuonHistoParameters.do_MUOhitsPlots = True
##
staMuonHistoParameters.nintDxy = 40
staMuonHistoParameters.minDxy = -10.
staMuonHistoParameters.maxDxy = 10.
##
staMuonHistoParameters.ptRes_nbin = 120
staMuonHistoParameters.ptRes_rangeMin = -3.
staMuonHistoParameters.ptRes_rangeMax = 3.
##
staMuonHistoParameters.phiRes_nbin = 80
staMuonHistoParameters.phiRes_rangeMin = -0.1
staMuonHistoParameters.phiRes_rangeMax = 0.1
##
staMuonHistoParameters.etaRes_nbin = 80
staMuonHistoParameters.etaRes_rangeMin = -0.1
staMuonHistoParameters.etaRes_rangeMax = 0.1
##
staMuonHistoParameters.cotThetaRes_nbin = 100
staMuonHistoParameters.cotThetaRes_rangeMin = -0.1
staMuonHistoParameters.cotThetaRes_rangeMax = 0.1
##
staMuonHistoParameters.dxyRes_nbin = 100
staMuonHistoParameters.dxyRes_rangeMin = -10.
staMuonHistoParameters.dxyRes_rangeMax = 10.
##
staMuonHistoParameters.dzRes_nbin = 100
staMuonHistoParameters.dzRes_rangeMin = -25.
staMuonHistoParameters.dzRes_rangeMax = 25.
#####################################################################################
# GLB tracks
glbMuonHistoParameters =  defaultMuonHistoParameters.clone()
glbMuonHistoParameters.usetracker = True
glbMuonHistoParameters.usemuon = True
glbMuonHistoParameters.nintNHit = 81
glbMuonHistoParameters.minNHit = -0.5
glbMuonHistoParameters.maxNHit = 80.5
glbMuonHistoParameters.do_TRKhitsPlots = True
glbMuonHistoParameters.do_MUOhitsPlots = True
#####################################################################################
# Displaced TRK tracks
displacedTrkMuonHistoParameters =  defaultMuonHistoParameters.clone()
displacedTrkMuonHistoParameters.usetracker = True
displacedTrkMuonHistoParameters.usemuon = False
displacedTrkMuonHistoParameters.nintNHit = 41
displacedTrkMuonHistoParameters.minNHit = -0.5
displacedTrkMuonHistoParameters.maxNHit = 40.5
displacedTrkMuonHistoParameters.do_TRKhitsPlots = True
displacedTrkMuonHistoParameters.do_MUOhitsPlots = False
##
displacedTrkMuonHistoParameters.nintDxy = 85
displacedTrkMuonHistoParameters.minDxy = -85.
displacedTrkMuonHistoParameters.maxDxy = 85.
displacedTrkMuonHistoParameters.nintDz = 84
displacedTrkMuonHistoParameters.minDz = -210.
displacedTrkMuonHistoParameters.maxDz = 210.
displacedTrkMuonHistoParameters.nintRpos = 85
displacedTrkMuonHistoParameters.minRpos = 0.
displacedTrkMuonHistoParameters.maxRpos = 85.
displacedTrkMuonHistoParameters.nintZpos = 84
displacedTrkMuonHistoParameters.minZpos = -210.
displacedTrkMuonHistoParameters.maxZpos = 210.
#####################################################################################
# Displaced muons: STA seeds
displacedStaSeedMuonHistoParameters = defaultMuonHistoParameters.clone()
displacedStaSeedMuonHistoParameters.usetracker = False
displacedStaSeedMuonHistoParameters.usemuon = True
displacedStaSeedMuonHistoParameters.nintNHit = 7
displacedStaSeedMuonHistoParameters.minNHit = -0.5
displacedStaSeedMuonHistoParameters.maxNHit = 6.5
displacedStaSeedMuonHistoParameters.do_TRKhitsPlots = False
displacedStaSeedMuonHistoParameters.do_MUOhitsPlots = True
displacedStaSeedMuonHistoParameters.nintDTHit = 7
displacedStaSeedMuonHistoParameters.maxDTHit = 6.5
displacedStaSeedMuonHistoParameters.nintCSCHit = 7
displacedStaSeedMuonHistoParameters.maxCSCHit = 6.5
displacedStaSeedMuonHistoParameters.nintRPCHit = 7
displacedStaSeedMuonHistoParameters.maxRPCHit = 6.5
##
displacedStaSeedMuonHistoParameters.nintDxy = 85
displacedStaSeedMuonHistoParameters.minDxy = -85.
displacedStaSeedMuonHistoParameters.maxDxy = 85.
displacedStaSeedMuonHistoParameters.nintDz = 84
displacedStaSeedMuonHistoParameters.minDz = -210.
displacedStaSeedMuonHistoParameters.maxDz = 210.
displacedStaSeedMuonHistoParameters.nintRpos = 85
displacedStaSeedMuonHistoParameters.minRpos = 0.
displacedStaSeedMuonHistoParameters.maxRpos = 85.
displacedStaSeedMuonHistoParameters.nintZpos = 84
displacedStaSeedMuonHistoParameters.minZpos = -210.
displacedStaSeedMuonHistoParameters.maxZpos = 210.
##
displacedStaSeedMuonHistoParameters.ptRes_nbin = 120
displacedStaSeedMuonHistoParameters.ptRes_rangeMin = -3.
displacedStaSeedMuonHistoParameters.ptRes_rangeMax = 3.
##
displacedStaSeedMuonHistoParameters.phiRes_nbin = 80
displacedStaSeedMuonHistoParameters.phiRes_rangeMin = -0.1
displacedStaSeedMuonHistoParameters.phiRes_rangeMax = 0.1
##
displacedStaSeedMuonHistoParameters.etaRes_nbin = 80
displacedStaSeedMuonHistoParameters.etaRes_rangeMin = -0.1
displacedStaSeedMuonHistoParameters.etaRes_rangeMax = 0.1
##
displacedStaSeedMuonHistoParameters.cotThetaRes_nbin = 100
displacedStaSeedMuonHistoParameters.cotThetaRes_rangeMin = -0.1
displacedStaSeedMuonHistoParameters.cotThetaRes_rangeMax = 0.1
##
displacedStaSeedMuonHistoParameters.dxyRes_nbin = 100
displacedStaSeedMuonHistoParameters.dxyRes_rangeMin = -10.
displacedStaSeedMuonHistoParameters.dxyRes_rangeMax = 10.
##
displacedStaSeedMuonHistoParameters.dzRes_nbin = 100
displacedStaSeedMuonHistoParameters.dzRes_rangeMin = -25.
displacedStaSeedMuonHistoParameters.dzRes_rangeMax = 25.
#####################################################################################
# Displaced muons: STA tracks
displacedStaMuonHistoParameters = defaultMuonHistoParameters.clone()
displacedStaMuonHistoParameters.usetracker = False
displacedStaMuonHistoParameters.usemuon = True
displacedStaMuonHistoParameters.nintNHit = 61
displacedStaMuonHistoParameters.minNHit = -0.5
displacedStaMuonHistoParameters.maxNHit = 60.5
displacedStaMuonHistoParameters.do_TRKhitsPlots = False
displacedStaMuonHistoParameters.do_MUOhitsPlots = True
##
displacedStaMuonHistoParameters.nintDxy = 85
displacedStaMuonHistoParameters.minDxy = -85.
displacedStaMuonHistoParameters.maxDxy = 85.
displacedStaMuonHistoParameters.nintDz = 84
displacedStaMuonHistoParameters.minDz = -210.
displacedStaMuonHistoParameters.maxDz = 210.
displacedStaMuonHistoParameters.nintRpos = 85
displacedStaMuonHistoParameters.minRpos = 0.
displacedStaMuonHistoParameters.maxRpos = 85.
displacedStaMuonHistoParameters.nintZpos = 84
displacedStaMuonHistoParameters.minZpos = -210.
displacedStaMuonHistoParameters.maxZpos = 210.
##
displacedStaMuonHistoParameters.ptRes_nbin = 120
displacedStaMuonHistoParameters.ptRes_rangeMin = -3.
displacedStaMuonHistoParameters.ptRes_rangeMax = 3.
##
displacedStaMuonHistoParameters.phiRes_nbin = 80
displacedStaMuonHistoParameters.phiRes_rangeMin = -0.1
displacedStaMuonHistoParameters.phiRes_rangeMax = 0.1
##
displacedStaMuonHistoParameters.etaRes_nbin = 80
displacedStaMuonHistoParameters.etaRes_rangeMin = -0.1
displacedStaMuonHistoParameters.etaRes_rangeMax = 0.1
##
displacedStaMuonHistoParameters.cotThetaRes_nbin = 100
displacedStaMuonHistoParameters.cotThetaRes_rangeMin = -0.1
displacedStaMuonHistoParameters.cotThetaRes_rangeMax = 0.1
##
displacedStaMuonHistoParameters.dxyRes_nbin = 100
displacedStaMuonHistoParameters.dxyRes_rangeMin = -10.
displacedStaMuonHistoParameters.dxyRes_rangeMax = 10.
##
displacedStaMuonHistoParameters.dzRes_nbin = 100
displacedStaMuonHistoParameters.dzRes_rangeMin = -25.
displacedStaMuonHistoParameters.dzRes_rangeMax = 25.
#####################################################################################
# Displaced muons: GLB tracks
displacedGlbMuonHistoParameters = defaultMuonHistoParameters.clone()
displacedGlbMuonHistoParameters.usetracker = True
displacedGlbMuonHistoParameters.usemuon = True
displacedGlbMuonHistoParameters.nintNHit = 81
displacedGlbMuonHistoParameters.minNHit = -0.5
displacedGlbMuonHistoParameters.maxNHit = 80.5
displacedGlbMuonHistoParameters.do_TRKhitsPlots = True
displacedGlbMuonHistoParameters.do_MUOhitsPlots = True
#
displacedGlbMuonHistoParameters.nintDxy = 85
displacedGlbMuonHistoParameters.minDxy = -85.
displacedGlbMuonHistoParameters.maxDxy = 85.
displacedGlbMuonHistoParameters.nintDz = 84
displacedGlbMuonHistoParameters.minDz = -210.
displacedGlbMuonHistoParameters.maxDz = 210.
displacedGlbMuonHistoParameters.nintRpos = 85
displacedGlbMuonHistoParameters.minRpos = 0.
displacedGlbMuonHistoParameters.maxRpos = 85.
displacedGlbMuonHistoParameters.nintZpos = 84
displacedGlbMuonHistoParameters.minZpos = -210.
displacedGlbMuonHistoParameters.maxZpos = 210.

#####################################################################################
# COSMIC muons
#####################################################################################
# cosmics: TRK tracks (2-legs)
trkCosmicMuonHistoParameters = defaultMuonHistoParameters.clone()
trkCosmicMuonHistoParameters.usetracker = True
trkCosmicMuonHistoParameters.usemuon = False
trkCosmicMuonHistoParameters.nintNHit = 41
trkCosmicMuonHistoParameters.minNHit = -0.5
trkCosmicMuonHistoParameters.maxNHit = 40.5
trkCosmicMuonHistoParameters.do_TRKhitsPlots = True
trkCosmicMuonHistoParameters.do_MUOhitsPlots = False
##
trkCosmicMuonHistoParameters.nintDxy = 40
trkCosmicMuonHistoParameters.minDxy = -10. 
trkCosmicMuonHistoParameters.maxDxy = 10.
trkCosmicMuonHistoParameters.nintDz = 50
trkCosmicMuonHistoParameters.minDz = -50.
trkCosmicMuonHistoParameters.maxDz = 50.
trkCosmicMuonHistoParameters.nintRpos = 40 
trkCosmicMuonHistoParameters.minRpos = 0.
trkCosmicMuonHistoParameters.maxRpos = 10.
trkCosmicMuonHistoParameters.nintZpos = 50
trkCosmicMuonHistoParameters.minZpos = -50.
trkCosmicMuonHistoParameters.maxZpos = 50.
#####################################################################################
# cosmics: STA tracks (2-legs)
staCosmicMuonHistoParameters = defaultMuonHistoParameters.clone()
staCosmicMuonHistoParameters.usetracker = False
staCosmicMuonHistoParameters.usemuon = True
staCosmicMuonHistoParameters.nintNHit = 61
staCosmicMuonHistoParameters.minNHit = -0.5
staCosmicMuonHistoParameters.maxNHit = 60.5
staCosmicMuonHistoParameters.do_TRKhitsPlots = False
staCosmicMuonHistoParameters.do_MUOhitsPlots = True
##
staCosmicMuonHistoParameters.nintDxy = 40
staCosmicMuonHistoParameters.minDxy = -10. 
staCosmicMuonHistoParameters.maxDxy = 10.
staCosmicMuonHistoParameters.nintDz = 50
staCosmicMuonHistoParameters.minDz = -50.
staCosmicMuonHistoParameters.maxDz = 50.
staCosmicMuonHistoParameters.nintRpos = 40 
staCosmicMuonHistoParameters.minRpos = 0.
staCosmicMuonHistoParameters.maxRpos = 10.
staCosmicMuonHistoParameters.nintZpos = 50
staCosmicMuonHistoParameters.minZpos = -50.
staCosmicMuonHistoParameters.maxZpos = 50.
##
staCosmicMuonHistoParameters.ptRes_nbin = 120
staCosmicMuonHistoParameters.ptRes_rangeMin = -3.
staCosmicMuonHistoParameters.ptRes_rangeMax = 3.
##
staCosmicMuonHistoParameters.phiRes_nbin = 80
staCosmicMuonHistoParameters.phiRes_rangeMin = -0.1
staCosmicMuonHistoParameters.phiRes_rangeMax = 0.1
##
staCosmicMuonHistoParameters.etaRes_nbin = 80
staCosmicMuonHistoParameters.etaRes_rangeMin = -0.1
staCosmicMuonHistoParameters.etaRes_rangeMax = 0.1
##
staCosmicMuonHistoParameters.cotThetaRes_nbin = 100
staCosmicMuonHistoParameters.cotThetaRes_rangeMin = -0.1
staCosmicMuonHistoParameters.cotThetaRes_rangeMax = 0.1
##
staCosmicMuonHistoParameters.dxyRes_nbin = 100
staCosmicMuonHistoParameters.dxyRes_rangeMin = -10.
staCosmicMuonHistoParameters.dxyRes_rangeMax = 10.
##
staCosmicMuonHistoParameters.dzRes_nbin = 100
staCosmicMuonHistoParameters.dzRes_rangeMin = -25.
staCosmicMuonHistoParameters.dzRes_rangeMax = 25.
#####################################################################################
# cosmics: GLB tracks (2-legs)
glbCosmicMuonHistoParameters = defaultMuonHistoParameters.clone()
glbCosmicMuonHistoParameters.usetracker = True
glbCosmicMuonHistoParameters.usemuon = True
glbCosmicMuonHistoParameters.nintNHit = 81
glbCosmicMuonHistoParameters.minNHit = -0.5
glbCosmicMuonHistoParameters.maxNHit = 80.5
glbCosmicMuonHistoParameters.do_TRKhitsPlots = True
glbCosmicMuonHistoParameters.do_MUOhitsPlots = True
#
glbCosmicMuonHistoParameters.nintDxy = 40
glbCosmicMuonHistoParameters.minDxy = -10. 
glbCosmicMuonHistoParameters.maxDxy = 10.
glbCosmicMuonHistoParameters.nintDz = 50
glbCosmicMuonHistoParameters.minDz = -50.
glbCosmicMuonHistoParameters.maxDz = 50.
glbCosmicMuonHistoParameters.nintRpos = 40 
glbCosmicMuonHistoParameters.minRpos = 0.
glbCosmicMuonHistoParameters.maxRpos = 10.
glbCosmicMuonHistoParameters.nintZpos = 50
glbCosmicMuonHistoParameters.minZpos = -50.
glbCosmicMuonHistoParameters.maxZpos = 50.
#####################################################################################
# cosmics: TRK tracks (1-leg)
trkCosmic1LegMuonHistoParameters = defaultMuonHistoParameters.clone()
trkCosmic1LegMuonHistoParameters.usetracker = True
trkCosmic1LegMuonHistoParameters.usemuon = False
trkCosmic1LegMuonHistoParameters.nintNHit = 81
trkCosmic1LegMuonHistoParameters.minNHit = -0.5
trkCosmic1LegMuonHistoParameters.maxNHit = 80.5
trkCosmic1LegMuonHistoParameters.do_TRKhitsPlots = True
trkCosmic1LegMuonHistoParameters.do_MUOhitsPlots = False
trkCosmic1LegMuonHistoParameters.nintLayers = 31
trkCosmic1LegMuonHistoParameters.maxLayers = 30.5
trkCosmic1LegMuonHistoParameters.nintPixels = 11
trkCosmic1LegMuonHistoParameters.maxPixels = 10.5
##
trkCosmic1LegMuonHistoParameters.nintDxy = 40
trkCosmic1LegMuonHistoParameters.minDxy = -10. 
trkCosmic1LegMuonHistoParameters.maxDxy = 10.
trkCosmic1LegMuonHistoParameters.nintDz = 50
trkCosmic1LegMuonHistoParameters.minDz = -50.
trkCosmic1LegMuonHistoParameters.maxDz = 50.
trkCosmic1LegMuonHistoParameters.nintRpos = 40 
trkCosmic1LegMuonHistoParameters.minRpos = 0.
trkCosmic1LegMuonHistoParameters.maxRpos = 10.
trkCosmic1LegMuonHistoParameters.nintZpos = 50
trkCosmic1LegMuonHistoParameters.minZpos = -50.
trkCosmic1LegMuonHistoParameters.maxZpos = 50.
#####################################################################################
# cosmics: STA tracks (1-leg)
staCosmic1LegMuonHistoParameters = defaultMuonHistoParameters.clone()
staCosmic1LegMuonHistoParameters.usetracker = False
staCosmic1LegMuonHistoParameters.usemuon = True
staCosmic1LegMuonHistoParameters.nintNHit = 121
staCosmic1LegMuonHistoParameters.maxNHit = 120.5
staCosmic1LegMuonHistoParameters.do_TRKhitsPlots = False
staCosmic1LegMuonHistoParameters.do_MUOhitsPlots = True
staCosmic1LegMuonHistoParameters.nintDTHit = 101
staCosmic1LegMuonHistoParameters.maxDTHit = 100.5
staCosmic1LegMuonHistoParameters.nintCSCHit = 101
staCosmic1LegMuonHistoParameters.maxCSCHit = 100.5
staCosmic1LegMuonHistoParameters.nintRPCHit = 21
staCosmic1LegMuonHistoParameters.maxRPCHit = 20.5
##
staCosmic1LegMuonHistoParameters.nintDxy = 40
staCosmic1LegMuonHistoParameters.minDxy = -10. 
staCosmic1LegMuonHistoParameters.maxDxy = 10.
staCosmic1LegMuonHistoParameters.nintDz = 50
staCosmic1LegMuonHistoParameters.minDz = -50.
staCosmic1LegMuonHistoParameters.maxDz = 50.
staCosmic1LegMuonHistoParameters.nintRpos = 40 
staCosmic1LegMuonHistoParameters.minRpos = 0.
staCosmic1LegMuonHistoParameters.maxRpos = 10.
staCosmic1LegMuonHistoParameters.nintZpos = 50
staCosmic1LegMuonHistoParameters.minZpos = -50.
staCosmic1LegMuonHistoParameters.maxZpos = 50.
##
staCosmic1LegMuonHistoParameters.ptRes_nbin = 120
staCosmic1LegMuonHistoParameters.ptRes_rangeMin = -3.
staCosmic1LegMuonHistoParameters.ptRes_rangeMax = 3.
##
staCosmic1LegMuonHistoParameters.phiRes_nbin = 80
staCosmic1LegMuonHistoParameters.phiRes_rangeMin = -0.1
staCosmic1LegMuonHistoParameters.phiRes_rangeMax = 0.1
##
staCosmic1LegMuonHistoParameters.etaRes_nbin = 80
staCosmic1LegMuonHistoParameters.etaRes_rangeMin = -0.1
staCosmic1LegMuonHistoParameters.etaRes_rangeMax = 0.1
##
staCosmic1LegMuonHistoParameters.cotThetaRes_nbin = 100
staCosmic1LegMuonHistoParameters.cotThetaRes_rangeMin = -0.1
staCosmic1LegMuonHistoParameters.cotThetaRes_rangeMax = 0.1
##
staCosmic1LegMuonHistoParameters.dxyRes_nbin = 100
staCosmic1LegMuonHistoParameters.dxyRes_rangeMin = -10.
staCosmic1LegMuonHistoParameters.dxyRes_rangeMax = 10.
##
staCosmic1LegMuonHistoParameters.dzRes_nbin = 100
staCosmic1LegMuonHistoParameters.dzRes_rangeMin = -25.
staCosmic1LegMuonHistoParameters.dzRes_rangeMax = 25.
#####################################################################################
# cosmics: GLB tracks (1-leg)
glbCosmic1LegMuonHistoParameters = defaultMuonHistoParameters.clone()
glbCosmic1LegMuonHistoParameters.usetracker = True
glbCosmic1LegMuonHistoParameters.usemuon = True
glbCosmic1LegMuonHistoParameters.nintNHit = 161
glbCosmic1LegMuonHistoParameters.maxNHit = 160.5
staCosmic1LegMuonHistoParameters.do_TRKhitsPlots = True
staCosmic1LegMuonHistoParameters.do_MUOhitsPlots = True
glbCosmic1LegMuonHistoParameters.nintDTHit = 101
glbCosmic1LegMuonHistoParameters.maxDTHit = 100.5
glbCosmic1LegMuonHistoParameters.nintCSCHit = 101
glbCosmic1LegMuonHistoParameters.maxCSCHit = 100.5
glbCosmic1LegMuonHistoParameters.nintRPCHit = 21
glbCosmic1LegMuonHistoParameters.maxRPCHit = 20.5
glbCosmic1LegMuonHistoParameters.nintLayers = 31 
glbCosmic1LegMuonHistoParameters.maxLayers = 30.5
glbCosmic1LegMuonHistoParameters.nintPixels = 11
glbCosmic1LegMuonHistoParameters.maxPixels = 10.5
##
glbCosmic1LegMuonHistoParameters.nintDxy = 40
glbCosmic1LegMuonHistoParameters.minDxy = -10. 
glbCosmic1LegMuonHistoParameters.maxDxy = 10.
glbCosmic1LegMuonHistoParameters.nintDz = 50
glbCosmic1LegMuonHistoParameters.minDz = -50.
glbCosmic1LegMuonHistoParameters.maxDz = 50.
glbCosmic1LegMuonHistoParameters.nintRpos = 40 
glbCosmic1LegMuonHistoParameters.minRpos = 0.
glbCosmic1LegMuonHistoParameters.maxRpos = 10.
glbCosmic1LegMuonHistoParameters.nintZpos = 50
glbCosmic1LegMuonHistoParameters.minZpos = -50.
glbCosmic1LegMuonHistoParameters.maxZpos = 50.
