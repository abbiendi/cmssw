import FWCore.ParameterSet.Config as cms


#RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
#        mix = cms.PSet(initialSeed = cms.untracked.uint32(12345),
#                       engineName = cms.untracked.string('HepJamesRandom')
#        ),
#        restoreStateLabel = cms.untracked.string("randomEngineStateProducer"),
#)

from Validation.Configuration.globalValidation_cff import *

from Validation.RecoMuon.muonValidation_cff import *

prevalidation = cms.Sequence(globalPrevalidationCosmics)

validation = cms.Sequence(cms.SequencePlaceholder("mix")
                          *globalValidationCosmics
                          )
