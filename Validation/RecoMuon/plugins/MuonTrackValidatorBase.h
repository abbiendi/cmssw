#ifndef MuonTrackValidatorBase_h
#define MuonTrackValidatorBase_h

/** \class MuonTrackValidatorBase
* Base class for analyzers that produces histograms to validate Muon Track Reconstruction performances
*
*/

#include <memory>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticleFwd.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "DQMServices/Core/interface/MonitorElement.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

// #include "CommonTools/RecoAlgos/interface/RecoTrackSelector.h"
#include "SimTracker/Common/interface/TrackingParticleSelector.h"
#include "CommonTools/RecoAlgos/interface/CosmicTrackingParticleSelector.h"

#include <iostream>
#include <sstream>
#include <string>
#include <TH1F.h>
#include <TH2F.h>


class DQMStore;
class MuonTrackValidatorBase {
 public:
  /// Constructor
  MuonTrackValidatorBase(const edm::ParameterSet& pset, edm::ConsumesCollector iC) : MuonTrackValidatorBase(pset)
    {
      bsSrc_Token = iC.consumes<reco::BeamSpot>(bsSrc);
      tp_effic_Token = iC.consumes<TrackingParticleCollection>(label_tp_effic);
      tp_fake_Token = iC.consumes<TrackingParticleCollection>(label_tp_fake);
      pileupinfo_Token = iC.consumes<std::vector<PileupSummaryInfo> >(label_pileupinfo);
      for (unsigned int www=0;www<label.size();www++){
	track_Collection_Token[www] = iC.consumes<edm::View<reco::Track> >(label[www]);
      }
    }

  MuonTrackValidatorBase(const edm::ParameterSet& pset):
    label(pset.getParameter< std::vector<edm::InputTag> >("label")),
    usetracker(pset.getParameter<bool>("usetracker")),
    usemuon(pset.getParameter<bool>("usemuon")),
    bsSrc(pset.getParameter< edm::InputTag >("beamSpot")),
    label_tp_effic(pset.getParameter< edm::InputTag >("label_tp_effic")),
    label_tp_fake(pset.getParameter< edm::InputTag >("label_tp_fake")),
    label_pileupinfo(pset.getParameter< edm::InputTag >("label_pileupinfo")),
    associators(pset.getParameter< std::vector<std::string> >("associators")),
    out(pset.getParameter<std::string>("outputFile")),
    parametersDefiner(pset.getParameter<std::string>("parametersDefiner")),
    //
    minEta(pset.getParameter<double>("minEta")),
    maxEta(pset.getParameter<double>("maxEta")),
    nintEta(pset.getParameter<int>("nintEta")),
    useFabsEta(pset.getParameter<bool>("useFabsEta")),
    minPt(pset.getParameter<double>("minPt")),
    maxPt(pset.getParameter<double>("maxPt")),
    nintPt(pset.getParameter<int>("nintPt")),
    useLogPt(pset.getUntrackedParameter<bool>("useLogPt",false)),
    useInvPt(pset.getParameter<bool>("useInvPt")),
    minHit(pset.getParameter<double>("minHit")),
    maxHit(pset.getParameter<double>("maxHit")),
    nintHit(pset.getParameter<int>("nintHit")),
      //
    minDTHit(pset.getParameter<double>("minDTHit")),
    maxDTHit(pset.getParameter<double>("maxDTHit")),
    nintDTHit(pset.getParameter<int>("nintDTHit")),
      //
    minCSCHit(pset.getParameter<double>("minCSCHit")),
    maxCSCHit(pset.getParameter<double>("maxCSCHit")),
    nintCSCHit(pset.getParameter<int>("nintCSCHit")),
      //
    minRPCHit(pset.getParameter<double>("minRPCHit")),
    maxRPCHit(pset.getParameter<double>("maxRPCHit")),
    nintRPCHit(pset.getParameter<int>("nintRPCHit")),
      //
    minLayers(pset.getParameter<double>("minLayers")),
    maxLayers(pset.getParameter<double>("maxLayers")),
    nintLayers(pset.getParameter<int>("nintLayers")),
    minPixels(pset.getParameter<double>("minPixels")),
    maxPixels(pset.getParameter<double>("maxPixels")),
    nintPixels(pset.getParameter<int>("nintPixels")),
    minPhi(pset.getParameter<double>("minPhi")),
    maxPhi(pset.getParameter<double>("maxPhi")),
    nintPhi(pset.getParameter<int>("nintPhi")),
    minDxy(pset.getParameter<double>("minDxy")),
    maxDxy(pset.getParameter<double>("maxDxy")),
    nintDxy(pset.getParameter<int>("nintDxy")),
    minDz(pset.getParameter<double>("minDz")),
    maxDz(pset.getParameter<double>("maxDz")),
    nintDz(pset.getParameter<int>("nintDz")),
    minRpos(pset.getParameter<double>("minRpos")),
    maxRpos(pset.getParameter<double>("maxRpos")),
    nintRpos(pset.getParameter<int>("nintRpos")),
    minZpos(pset.getParameter<double>("minZpos")),
    maxZpos(pset.getParameter<double>("maxZpos")),
    nintZpos(pset.getParameter<int>("nintZpos")),
    minPU(pset.getParameter<double>("minPU")),
    maxPU(pset.getParameter<double>("maxPU")),
    nintPU(pset.getParameter<int>("nintPU")),
    //
    ptRes_rangeMin(pset.getParameter<double>("ptRes_rangeMin")),
    ptRes_rangeMax(pset.getParameter<double>("ptRes_rangeMax")),
    ptRes_nbin(pset.getParameter<int>("ptRes_nbin")),
    etaRes_rangeMin(pset.getParameter<double>("etaRes_rangeMin")),
    etaRes_rangeMax(pset.getParameter<double>("etaRes_rangeMax")),
    etaRes_nbin(pset.getParameter<int>("etaRes_nbin")),
    phiRes_rangeMin(pset.getParameter<double>("phiRes_rangeMin")),
    phiRes_rangeMax(pset.getParameter<double>("phiRes_rangeMax")),
    phiRes_nbin(pset.getParameter<int>("phiRes_nbin")),
    cotThetaRes_rangeMin(pset.getParameter<double>("cotThetaRes_rangeMin")),
    cotThetaRes_rangeMax(pset.getParameter<double>("cotThetaRes_rangeMax")),
    cotThetaRes_nbin(pset.getParameter<int>("cotThetaRes_nbin")),
    dxyRes_rangeMin(pset.getParameter<double>("dxyRes_rangeMin")),
    dxyRes_rangeMax(pset.getParameter<double>("dxyRes_rangeMax")),
    dxyRes_nbin(pset.getParameter<int>("dxyRes_nbin")),
    dzRes_rangeMin(pset.getParameter<double>("dzRes_rangeMin")),
    dzRes_rangeMax(pset.getParameter<double>("dzRes_rangeMax")),
    dzRes_nbin(pset.getParameter<int>("dzRes_nbin")),
    do_TRKhitsPlots(pset.getParameter<bool>("do_TRKhitsPlots")),
    do_MUOhitsPlots(pset.getParameter<bool>("do_MUOhitsPlots")),
    //
    ignoremissingtkcollection_(pset.getUntrackedParameter<bool>("ignoremissingtrackcollection",false))
    //
    {
      dbe_ = edm::Service<DQMStore>().operator->();

      if (useLogPt) {
        minPt=log10(std::max(0.01,minPt));
	maxPt=log10(maxPt);
      }
    }
  
  /// Destructor
  virtual ~MuonTrackValidatorBase(){ }
 
  template<typename T> void fillPlotNoFlow (MonitorElement* h, T val) {
    h->Fill(std::min(std::max(val,((T) h->getTH1()->GetXaxis()->GetXmin())),((T) h->getTH1()->GetXaxis()->GetXmax())));
  }
  
  void doProfileX(TH2 * th2, MonitorElement* me){
    if (th2->GetNbinsX()==me->getNbinsX()){
      TProfile * p1 = (TProfile*) th2->ProfileX();
      p1->Copy(*me->getTProfile());
      delete p1;
    } else {
      throw cms::Exception("MuonTrackValidator") << "Different number of bins!";
    }
  }

  void doProfileX(MonitorElement * th2m, MonitorElement* me) {
    doProfileX(th2m->getTH2F(), me);
  }

  //  virtual double getEta(double eta) {
  double getEta(double eta) {
    if (useFabsEta) return fabs(eta);
    else return eta;
  }

  //  virtual double getPt(double pt) {
  double getPt(double pt) {
    if (useInvPt && pt!=0) return 1/pt;
    else return pt;
  }
  
  void fillPlotFromVector(MonitorElement* h, std::vector<int>& vec) {
    for (unsigned int j=0; j<vec.size(); j++){
      h->setBinContent(j+1, vec[j]);
    }
  }

  /*
  void fillPlotFromVectors(MonitorElement* h, std::vector<int>& numerator, std::vector<int>& denominator,std::string type){
    double value,err;
    for (unsigned int j=0; j<numerator.size(); j++){
      if (denominator[j]!=0){
	if (type=="effic")
	  value = ((double) numerator[j])/((double) denominator[j]);
	else if (type=="fakerate")
	  value = 1-((double) numerator[j])/((double) denominator[j]);
	//else if (type=="pileup"){
	//	value = ((double) numerator[j])*1./((double) denominator[j]);
	//        err = sqrt( value*(1+value)/(double) denominator[j] );
	//      }
	else return;
	err = sqrt( value*(1-value)/(double) denominator[j] );
	h->setBinContent(j+1, value);
	h->setBinError(j+1,err);
      }
      else {
	h->setBinContent(j+1, 0);
	h->setBinError(j+1, 0.);
      }
    }
  }
  */

  void BinLogX(TH1*h) {
    
    TAxis *axis = h->GetXaxis();
    int bins = axis->GetNbins();
    
    float from = axis->GetXmin();
    float to = axis->GetXmax();
    float width = (to - from) / bins;
    float *new_bins = new float[bins + 1];
    
    for (int i = 0; i <= bins; i++) {
      new_bins[i] = TMath::Power(10, from + i * width);
      
    }
    axis->Set(bins, new_bins);
    delete[] new_bins;
  }

 protected:

  DQMStore* dbe_;

  std::vector<edm::InputTag> label;
  bool usetracker;
  bool usemuon;
  edm::InputTag bsSrc;
  edm::InputTag label_tp_effic;
  edm::InputTag label_tp_fake;
  edm::InputTag label_pileupinfo;
  std::vector<std::string> associators;
  std::string out;
  std::string parametersDefiner;
  std::vector<edm::EDGetTokenT<edm::View<reco::Track> > > track_Collection_Token;
  edm::EDGetTokenT<reco::BeamSpot> bsSrc_Token;
  edm::EDGetTokenT<TrackingParticleCollection> tp_effic_Token;
  edm::EDGetTokenT<TrackingParticleCollection> tp_fake_Token;
  edm::EDGetTokenT<std::vector<PileupSummaryInfo> > pileupinfo_Token;
  edm::ESHandle<MagneticField> theMF;

  double minEta, maxEta;  int nintEta;  bool useFabsEta;
  double minPt, maxPt;  int nintPt;  bool useLogPt;  bool useInvPt; 
  double minHit, maxHit;  int nintHit;
  double minDTHit, maxDTHit; int nintDTHit;
  double minCSCHit, maxCSCHit;  int nintCSCHit;
  double minRPCHit, maxRPCHit;  int nintRPCHit;
  double minLayers, maxLayers;  int nintLayers;
  double minPixels, maxPixels;  int nintPixels;
  double minPhi, maxPhi;  int nintPhi;
  double minDxy, maxDxy;  int nintDxy;
  double minDz, maxDz;  int nintDz;
  double minRpos, maxRpos;  int nintRpos;
  double minZpos, maxZpos;  int nintZpos;
  double minPU, maxPU;  int nintPU;
  //
  double ptRes_rangeMin,ptRes_rangeMax; int ptRes_nbin;
  double etaRes_rangeMin,etaRes_rangeMax; int etaRes_nbin;
  double phiRes_rangeMin,phiRes_rangeMax; int phiRes_nbin;
  double cotThetaRes_rangeMin,cotThetaRes_rangeMax; int cotThetaRes_nbin;
  double dxyRes_rangeMin,dxyRes_rangeMax; int dxyRes_nbin;
  double dzRes_rangeMin,dzRes_rangeMax; int dzRes_nbin;
      
  bool do_TRKhitsPlots, do_MUOhitsPlots;
  bool ignoremissingtkcollection_;

  //1D
  std::vector<MonitorElement*> h_tracks, h_fakes, h_nhits, h_charge;
  //trk
  //  std::vector<MonitorElement*> h_effic,  h_fakerate, h_recoeta, h_assoceta, h_assoc2eta, h_simuleta, h_loopereta, h_misideta, h_looprate, h_misidrate;
  std::vector<MonitorElement*> h_recoeta, h_assoceta, h_assoc2eta, h_simuleta, h_misideta;
  std::vector<MonitorElement*> h_recopT, h_assocpT, h_assoc2pT, h_simulpT, h_misidpT;
  std::vector<MonitorElement*> h_recohit, h_assochit, h_assoc2hit, h_simulhit, h_misidhit;
  std::vector<MonitorElement*> h_recophi, h_assocphi, h_assoc2phi, h_simulphi, h_misidphi;
  std::vector<MonitorElement*> h_recodxy, h_assocdxy, h_assoc2dxy, h_simuldxy, h_misiddxy;
  std::vector<MonitorElement*> h_recodz, h_assocdz, h_assoc2dz, h_simuldz, h_misiddz;
  std::vector<MonitorElement*> h_recopu, h_assocpu, h_assoc2pu, h_simulpu, h_misidpu;

  std::vector<MonitorElement*> h_assocRpos, h_simulRpos, h_assocZpos, h_simulZpos;
  std::vector<MonitorElement*> h_etaRes;
  
  //  std::vector<MonitorElement*> h_assoceta_Quality05, h_assoceta_Quality075;
  //  std::vector<MonitorElement*> h_assocpT_Quality05, h_assocpT_Quality075;
  //  std::vector<MonitorElement*> h_assocphi_Quality05, h_assocphi_Quality075;

  //2D
  //  std::vector<MonitorElement*> nrecHit_vs_nsimHit_sim2rec;
  //  std::vector<MonitorElement*> nrecHit_vs_nsimHit_rec2sim;
  std::vector<MonitorElement*> nRecHits_vs_nSimHits;

  //assoc hits
  std::vector<MonitorElement*> h_assocFraction, h_assocSharedHit;

  //#hit vs eta: to be used with doProfileX
  std::vector<MonitorElement*> nhits_vs_eta,nDThits_vs_eta,nCSChits_vs_eta,nRPChits_vs_eta;
  // NON SERVE, lo fa il Postprocessor
  //  std::vector<MonitorElement*> nhitsMean_vs_eta,nDThitsMean_vs_eta, nCSChitsMean_vs_eta,nRPChitsMean_vs_eta;
 
  ////////////////////////////////////////////////////////////////////////////////////////
  // copiati da MuonTrackValidator.h : non piace neanche cosi' ma almeno sono tutti nello stesso posto
  //1D
  std::vector<MonitorElement*> h_nchi2, h_nchi2_prob, h_losthits;
  std::vector<MonitorElement*> h_nmisslayers_inner,h_nmisslayers_outer,h_nlosthits;

  //2D
  std::vector<MonitorElement*> chi2_vs_nhits, etares_vs_eta;
  // NON SERVE ? Lo fa il PostProcessor  std::vector<MonitorElement*> h_ptshifteta;
  std::vector<MonitorElement*> ptres_vs_phi, chi2_vs_phi, nhits_vs_phi, phires_vs_phi;

  //Profile2D
  // NON LI USIAMO !!!
  //  std::vector<MonitorElement*> ptmean_vs_eta_phi, phimean_vs_eta_phi;

  //assoc chi2
  std::vector<MonitorElement*> h_assochi2, h_assochi2_prob;

  //chi2 and # lost hits vs eta: to be used with doProfileX
  std::vector<MonitorElement*> chi2_vs_eta, nlosthits_vs_eta;
  //  PostPorcessor ?  std::vector<MonitorElement*> nlosthits_vs_eta_prof;
  //  PostPorcessor ?   std::vector<MonitorElement*> nhits_vs_phi_prof;
  //  PostPorcessor ?   std::vector<MonitorElement*> chi2mean_vs_nhits, chi2mean_vs_eta, chi2mean_vs_phi;
  std::vector<MonitorElement*> nTRK_LayersWithMeas_vs_eta,nPixel_LayersWithMeas_vs_eta;

  //resolution of track params: to be used with fitslicesytool
  std::vector<MonitorElement*> dxyres_vs_eta, ptres_vs_eta, dzres_vs_eta, phires_vs_eta, thetaCotres_vs_eta;
  std::vector<MonitorElement*> dxyres_vs_pt, ptres_vs_pt, dzres_vs_pt, phires_vs_pt, thetaCotres_vs_pt;
  std::vector<MonitorElement*> dxyres_vs_pttrue, ptres_vs_pttrue, dzres_vs_pttrue, phires_vs_pttrue, thetaCotres_vs_pttrue;

  //pulls of track params vs eta: to be used with fitslicesytool
  std::vector<MonitorElement*> dxypull_vs_eta, ptpull_vs_eta, dzpull_vs_eta, phipull_vs_eta, thetapull_vs_eta;
  std::vector<MonitorElement*> ptpull_vs_phi, phipull_vs_phi, thetapull_vs_phi;
  std::vector<MonitorElement*> h_dxypulleta, h_ptpulleta, h_dzpulleta, h_phipulleta, h_thetapulleta;
  std::vector<MonitorElement*> h_ptpullphi, h_phipullphi, h_thetapullphi;
  std::vector<MonitorElement*> h_ptpull, h_qoverppull, h_thetapull, h_phipull, h_dxypull, h_dzpull;
  
  // for muon Validation (SimToReco distributions for Quality > 0.5, 0.75)
  std::vector<MonitorElement*> h_PurityVsQuality;

};


#endif
