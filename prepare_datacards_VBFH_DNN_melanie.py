#! /usr/bin/env python

from Analyzer.LLP2018.VBFH_DNN_setting import *
from Analyzer.LLP2018.drawUtils import *

########## ######## ##########
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetPadTopMargin(0.06)
gStyle.SetPadRightMargin(0.05)

h2 = {}
h2_profX = {}
tree = {}
c2 = {}
n_A = {}
n_B = {}
n_C = {}
n_D = {}
error_A = {}
error_B = {}
error_C = {}
error_D = {}

#back = ["VV","WJetsToLNu","ZJetsToNuNu","TTbar","QCD"]#some are missing
back = ["TTbar","QCD"]

def write_datacard_2D(channel,tag_variable,tree_name="",cut="",draw_all=False,add_string="",j0_crmin=0,j0_crmax=0,j0_sigmin=0,j0_sigmax=0,j1_crmin=0,j1_crmax=0,j1_sigmin=0,j1_sigmax=0,title='',rebin=False):

    #treeName  = 'skim'
    treeName  = tree_name#'ntuple/tree'
    #!# modify if your tree has a different name
    #cut       = ''
    #!# modify if your tree has a different name; this should be a base cut applied to everything
    #trigger   = 'HLT_VBF_DisplacedJet'
    #!# modify if trigger in your tree has a different name
    binFact   = 1
    signalMultFactor = SIGMULTFAC * ENHANCEMENT
    tagVar    = tag_variable
    MAXVAL = 0.
    trigger_short_name   = 'HLT_MET'
    if tag_variable == 'nHadEFrac':
        j0Var = "Jets[0].nHadEFrac"
        j1Var = "Jets[1].nHadEFrac"
        wp = "nHadEFrac"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min
    elif tag_variable == 'nTrackConstituents':
        j0Var = "Jets[0].nTrackConstituents" if not is_array2root_tree else "Jets0_nTrackConstituents"
        j1Var = "Jets[1].nTrackConstituents" if not is_array2root_tree else "Jets1_nTrackConstituents"
        wp = "nTrackConstituents"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min if not is_array2root_tree else "Jets0_pt>"+jet_pt_min
        jet_pt_cut+= " && Jets[1].pt>"+jet_pt_min if not is_array2root_tree else " && Jets1_pt>"+jet_pt_min
#####################################
    elif tag_variable == 'pfXWP1000':
        j0Var = "j0_pfXWP1000"if tree_name=="skim" else "Jets[0].pfXWP1000"
        j1Var = "j1_pfXWP1000"if tree_name=="skim" else "Jets[1].pfXWP1000"
        wp = "pfXWP1000"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min

    elif tag_variable == 'one_pfXWP1000':
        j0Var = "j0_pfXWP1000"if tree_name=="skim" else "Jets[0].pfXWP1000"
        j1Var = "j1_pfXWP1000"if tree_name=="skim" else "Jets[1].pfXWP1000"
        wp = "pfXWP1000"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min


    elif tag_variable == 'ORpfXWP1000':
        j0Var = "j0_pfXWP1000"if tree_name=="skim" else "Jets[0].pfXWP1000"
        j1Var = "j1_pfXWP1000"if tree_name=="skim" else "Jets[1].pfXWP1000"
        wp = "ORpfXWP1000"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min


    elif tag_variable == 'OR3pfXWP1000':
        j0Var = "j0_pfXWP1000"if tree_name=="skim" else "Jets[0].pfXWP1000"
        j1Var = "j1_pfXWP1000"if tree_name=="skim" else "Jets[1].pfXWP1000"
        wp = "ORpfXWP1000"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min


    elif tag_variable == 'OR4pfXWP1000':
        j0Var = "j0_pfXWP1000"if tree_name=="skim" else "Jets[0].pfXWP1000"
        j1Var = "j1_pfXWP1000"if tree_name=="skim" else "Jets[1].pfXWP1000"
        wp = "ORpfXWP1000"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min


    elif tag_variable == 'OR5pfXWP1000':
        j0Var = "j0_pfXWP1000"if tree_name=="skim" else "Jets[0].pfXWP1000"
        j1Var = "j1_pfXWP1000"if tree_name=="skim" else "Jets[1].pfXWP1000"
        wp = "ORpfXWP1000"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min

######################################
    elif tag_variable == 'nDTSegments':
        j0Var = "nDTSegments"
        j1Var = "nDTSegments"
        wp = "nDTSegments"
        MAXVAL=1.
    elif tag_variable == 'nTrackConstituents_nDTSegments':
        j0Var = "Jets[0].nTrackConstituents" if not is_array2root_tree else "Jets0_nTrackConstituents"
        j1Var = "nDTSegments"
        wp = "nTrackConstituents_nDTSegments"
        MAXVAL=1.        
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min if not is_array2root_tree else "Jets0_pt>"+jet_pt_min
    elif tag_variable == 'DNN_nDTSegments':
        j0Var = "sigprob"
        j1Var = "nDTSegments"
        wp = "DNN_nDTSegments"
        MAXVAL=1.
        jet_pt_cut = ""
######################################
    elif tag_variable == "CSV":
        j0Var = "Jets[0].CSV"
        j1Var = "Jets[1].CSV"
        wp = "CSV_0p9"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min
    elif tag_variable == "pfXWP1":
        j0Var = "Jets[0].pfXWP1"
        j1Var = "Jets[0].pfXWP1"
        wp = "pfXWP1_0p9"
        MAXVAL=1.
        jet_pt_cut = "Jets[0].pt>"+jet_pt_min+" && Jets[1].pt>"+jet_pt_min


    if isMM:
        channel += "_MM"
    elif isEE:
        channel += "_EE"

    if jet_pt_cut!="":
        cut += " && " + jet_pt_cut


    print '--- Channel   : ', channel, ' ---'
    print '  ntuples     : ', NTUPLEDIR
    print '  read tree   : ', treeName
    print '  applied base cut : ', cut
    print '  signal      : ', signName
    print '  j0 SR min:     : ', j0_sigmin
    print '  j0 SR max:     : ', j0_sigmax
    print '  j1 SR min:     : ', j1_sigmin
    print '  j1 SR max:     : ', j1_sigmax
    if useABCD:
        print '  Using ABCD prediction! '
    else:
        print '  Counting MC events in SR! '
    if signalMultFactor == 0.001:
        print '  x-sec calculated in fb '
    elif (signalMultFactor >= 1 and signalMultFactor < 1000):
        print '  x-sec calculated in pb '
    else:
        print 'Wrong signal mult. factor, aborting...'
        exit()
    print '-'*11*2

    #*******************************************************#
    #                                                       #
    #              Variables and selections                 #
    #                                                       #
    #*******************************************************#
    # Add here interesting variables for your SR definition
    j0Tag                   = RooRealVar( j0Var,    '',  0,      1       )
    j1Tag                   = RooRealVar( j1Var,    '',  0,      1       )
    tagVar                  = RooRealVar( tag_variable,  ' n. calo tagged jets',      0,    10    )
    weight                  = RooRealVar( WEIGHT,  '',                      -1.e9,  1.e9    )

    tagVarArg = RooArgSet(tagVar)

    # Define the selection for the various categories (base + SR / LSBcut / HSBcut )
    baseCut = '{0}'.format(cut)
    print 'base cut', baseCut

    #*******************************************************#
    #                                                       #
    #                      Input files                      #
    #                                                       #
    #*******************************************************#
    
    # Import the files using TChains (example here, QCD)
    #treeData    = TChain(treeName)
    #treeQCD     = TChain(treeName)
    #treeVjet    = TChain(treeName)
    #treeTTbar     = TChain(treeName)
    #treeVV      = TChain(treeName)
    #treeSMHiggs = TChain(treeName)
    #treeMC      = TChain(treeName)

    #!# Commenting out stuffs for simplicity

    # Read data
    pd = getPrimaryDataset(trigger_short_name)
    if len(pd)==0: raw_input('Warning: Primary Dataset not recognized, continue?')
    #for i, s in enumerate(pd): 
    #    treeData.Add(NTUPLEDIR + s + '.root')

    # Read QCD backgrounds
    #for i, s in enumerate(['QCD']):
    #    for j, ss in enumerate(samples[s]['files']): 
    #        treeQCD.Add(NTUPLEDIR + ss + '.root')

    # Read V+jets backgrounds
    #for i, s in enumerate(['ZJetsToNuNu', 'WJetsToLNu', 'WJetsToQQ', 'DYJetsToQQ','DYJetsToLL']):
    #    for j, ss in enumerate(samples[s]['files']): 
    #        treeVjet.Add(NTUPLEDIR + ss + '.root')
    
    # Read TTbar backgrounds
    #for i, s in enumerate(['TTbar','ST']):
    #    for j, ss in enumerate(samples[s]['files']): 
    #        treeTTbar.Add(NTUPLEDIR + ss + '.root')

    # Read VV backgrounds
    #for i, s in enumerate(['VV']):
    #    for j, ss in enumerate(samples[s]['files']): 
    #        treeVV.Add(NTUPLEDIR + ss + '.root')
    
    # Read SM Higgs backgrounds
    #for i, s in enumerate(['SM_Higgs']):
    #    for j, ss in enumerate(samples[s]['files']): 
    #        treeSMHiggs.Add(NTUPLEDIR +


    for b in back:
        tree[b] = TChain(treeName)
        for i, ss in enumerate(samples[b]['files']):
            tree[b].Add(NTUPLEDIR + ss + '.root')
        print '  %s tree entries: %.2f' % (b,tree[b].GetEntries())

    #print '  QCD tree entries: %.2f' % treeQCD.GetEntries()
    #print '  V+jets tree entries: %.2f' % treeVjet.GetEntries()
    #print '  TTbar,ST tree entries: %.2f' % treeTTbar.GetEntries()
    #print '  VV tree entries: %.2f' % treeVV.GetEntries()
    #print '  SM Higgs tree entries: %.2f' % treeSMHiggs.GetEntries()


    label = TLatex()
    label.SetNDC()
    label.SetTextSize(0.04)
    label.SetTextColor(1)


    #*******************************************************#
    #                                                       #
    #                    ABCD   method                      #
    #                                                       #
    #*******************************************************# 

    if tag_variable=="nTracks3PixelHits":
        Acut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_crmin,j1_crmax)
        Bcut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_crmin,j1_crmax)
        Ccut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_sigmin,j1_sigmax)
        Dcut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_sigmin,j1_sigmax)
    elif tag_variable=="nHadEFrac":
        Acut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_crmin,j1_crmax)
        Bcut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_crmin,j1_crmax)
        Ccut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_sigmin,j1_sigmax)
        Dcut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_sigmin,j1_sigmax)
    elif tag_variable=="pfXWP1000":
        Acut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_crmin,j1_crmax)
        Bcut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_crmin,j1_crmax)
        Ccut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_sigmin,j1_sigmax)
        Dcut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_sigmin,j1_sigmax)


    elif tag_variable=="DNN":
        Acut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_crmin,j1_crmax)
        Bcut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_crmin,j1_crmax)
        Ccut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_sigmin,j1_sigmax)
        Dcut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_sigmin,j1_sigmax)
    else:
        Acut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_crmin,j1_crmax)
        Bcut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>{4} && {1}<{5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_crmin,j1_crmax)
        Ccut  = baseCut + ' && {0}>{2} && {0}<{3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_crmin,j0_crmax,j1_sigmin,j1_sigmax)
        Dcut  = baseCut + ' && {0}>={2} && {0}<={3} && {1}>={4} && {1}<={5}'.format(j0Tag.GetName(),j1Tag.GetName(),j0_sigmin,j0_sigmax,j1_sigmin,j1_sigmax)


    print "Acut:",Acut
    print "Bcut:",Bcut
    print "Ccut:",Ccut
    print "Dcut:",Dcut

    j0Var2D = j0Var
    j1Var2D = j1Var

    lineX = TLine(j0_sigmin if j0_sigmin>j0_crmin else j0_sigmax, min(j1_crmin,j1_sigmin), j0_sigmin if j0_sigmin>j0_crmin else j0_sigmax, max(j1_crmax,j1_sigmax))
    lineX.SetLineColor(2)
    lineX.SetLineWidth(2)
    lineX.SetLineStyle(2)


    lineY = TLine(min(j0_crmin,j0_sigmin),j1_sigmin if j1_sigmin>j1_crmin else j1_sigmax, max(j0_crmax,j0_sigmax), j1_sigmin if j1_sigmin>j1_crmin else j1_sigmax)
    lineY.SetLineColor(2)
    lineY.SetLineWidth(2)
    lineY.SetLineStyle(2)
                                                                                                                                     
 
    ###########
    # 2D plots
    ########### 

 
    for b in back:

        c2[b] = TCanvas('c2_'+str(b), 'plot', 1200, 800)
        c2[b].cd(1)
        c2[b].GetPad(0).SetRightMargin(1.)
        c2[b].GetPad(0).SetTicks(1, 1)
        c2[b].SetGrid()
        #c2[b].SetLogx()                                                                                                                                        
        c2[b].SetLogy()
        #c2[b].SetLogz()
        h2[b] = TH1F(str(b)+wp,str(b),NBINS_X,min(j0_crmin,j0_sigmin),max(j0_crmax,j0_sigmax,MAXVAL))
        print "\n"
        print "histo name: ", str(b)+wp
        print "cut: ", baseCut
        print "\n"
        h2[b].Sumw2()
        tree[b].Project(str(b)+wp,j0Var,"("+baseCut+")*"+WEIGHT)#eventweight?

        h2[b].GetXaxis().SetTitle(variables[j0Var]['label'])
        h2[b].GetYaxis().SetTitle("Events")
        h2[b].SetOption("%s" % tree[b].GetTree().GetEntriesFast())
        h2[b].SetLineColor(samples[b]['fillcolor'])
        h2[b].SetLineWidth(2)
        h2[b].SetFillColor(samples[b]['fillcolor'])
        h2[b].Draw("HISTO")

        lineX.Draw()

        leg = TLegend(0.15, 0.75+0.05, 0.25+0.03, 0.88)
        leg.SetTextSize(0.025)
        leg.AddEntry(h2[b],"MC background","PL")
        leg.SetBorderSize(0)
        leg.Draw()
        drawCMS(LUMI, "Preliminary",pd)
        label.DrawLatex(0.6, 0.8,str(b))

        if not WEIGHT=="isMC":
            c2[b].SetLogz()
        if draw_all:
            c2[b].Print(OUTPUTDIR_CHAN+wp+"_"+str(b)+weight_label+"_datacards"+add_string+".pdf")
            c2[b].Print(OUTPUTDIR_CHAN+wp+"_"+str(b)+weight_label+"_datacards"+add_string+".png")
        c2[b].Close()

        leg.Clear()


        error_A[b] = Double()
        error_B[b] = Double()
        error_C[b] = Double()
        error_D[b] = Double()


        n_B[b]   = RooRealVar('n_B_'+str(b),  str(b)+' B normalization',   h2[b].IntegralAndError(h2[b].GetXaxis().FindBin(j0_crmin), h2[b].GetXaxis().FindBin(j0_sigmin)-1,error_B[b],""),   0., 1.e50)

        n_D[b]   = RooRealVar('n_D_'+str(b),  str(b)+' D normalization',   h2[b].IntegralAndError(h2[b].GetXaxis().FindBin(j0_sigmin), h2[b].GetXaxis().FindBin(j0_sigmax),error_D[b],""),   0., 1.e50)

        if WEIGHT=="isMC":
            #print str(b)+ " in A: %.1f +- %.1f" % (n_A[b].getVal(), error_A[b])
            print str(b)+ " in B: %.1f +- %.1f" % (n_B[b].getVal(), error_B[b])
            #print str(b)+ " in C: %.1f +- %.1f" % (n_C[b].getVal(), error_C[b])
            print str(b)+ " in D: %.1f +- %.1f" % (n_D[b].getVal(), error_D[b])
        else:
            #print str(b)+ " in A: %.2e +- %.2e" % (n_A[b].getVal(), error_A[b])
            print str(b)+ " in B: %.2e +- %.2e" % (n_B[b].getVal(), error_B[b])
            #print str(b)+ " in C: %.2e +- %.2e" % (n_C[b].getVal(), error_C[b])
            print str(b)+ " in D: %.2e +- %.2e" % (n_D[b].getVal(), error_D[b])


    print "Create a stack!"
    bkg = THStack("Bkg", ";"+h2[back[0]].GetXaxis().GetTitle()+";Events")
    bkg_err = h2[back[0]].Clone("bkg_err")
    bkg_err.Reset("MICES")
    bkg_err.SetMarkerStyle(0)
    bkg_err.SetFillStyle(3003)
    bkg_err.SetFillColor(1)
    for i, s in enumerate(back):
        bkg.Add(h2[s])
        bkg_err.Add(h2[s])

    # --- Display ---
    c1 = TCanvas("c1", "all", 1000, 800)
    c1.cd()
    # Draw
    #c1.SetLogy()
    c1.SetGrid()
    bkg.Draw("HIST") # stack
    bkg_err.Draw("SAME, E2") # sum of bkg
    c1.SetGrid()
    c1.SetLogy()
    c1.Update()
    c1.Print(OUTPUTDIR_CHAN+"j0tagVar_"+wp+"_all_bkg"+".pdf")

    print "And here Signal w/o ABCD"

    #*******************************************************#
    #                                                       #
    #                    Signal                             #
    #                                                       #
    #*******************************************************#
    # One datacard per signal!
    # .....

    treeSignal = {}
    hSignal = {}
    hSignal_profX = {}
    nSignalSR = {}
    SignalYieldSR = {}
    SignalYieldErrSR = {}
    cSign = {}
    for m in massPoints:
        for c in ctauPoints:
            name = "VBFH_M"+str(m)+"_ctau"+str(c)
            treeSignal[name] = TChain(treeName)
            for j, ss in enumerate(samples[name]['files']): 
                treeSignal[name].Add(NTUPLEDIR + ss + '.root')
            if(options.verbose):
                print name, treeSignal[name].GetEntries()


            cSign[name] = TCanvas(name, name, 1200, 800)
            cSign[name].cd(1)
            cSign[name].GetPad(0).SetRightMargin(1.)
            cSign[name].GetPad(0).SetTicks(1, 1)
            cSign[name].SetGrid()
            hSignal[name] = TH1F("j0tagVar_"+wp+name,tag_variable+name,NBINS_X,min(j0_crmin,j0_sigmin,j1_crmin,j1_sigmin),max(j0_crmax,j0_sigmax,j1_crmax,j1_sigmax,MAXVAL))
            hSignal[name].Sumw2()
            treeSignal[name].Project("j0tagVar_"+wp+name,j0Var,"("+baseCut+")*"+WEIGHT)#eventweight?
            hSignal[name].GetXaxis().SetTitle(variables[j0Var]['label'])
            hSignal[name].GetYaxis().SetTitle("Events")
            hSignal[name].SetOption("%s" % treeSignal[name].GetTree().GetEntriesFast())
            hSignal[name].SetLineColor(samples[name]['fillcolor'])
            hSignal[name].SetLineWidth(2)
            hSignal[name].SetFillColor(samples[name]['fillcolor'])
            hSignal[name].Draw("HISTO")

            lineX.Draw()


            leg = TLegend(0.15, 0.75+0.05, 0.25+0.03, 0.88)
            leg.SetTextSize(0.025)
            leg.AddEntry(hSignal[name],name,'PLF')
            leg.SetBorderSize(0)
            leg.Draw()

            drawCMS(LUMI, "Preliminary",pd)
            label.DrawLatex(0.6, 0.8,name)
            cSign[name].SetLogy()

            #QUI
            if log_plot:
                cSign[name].SetLogy()

            if draw_all:
                cSign[name].Print(OUTPUTDIR_CHAN+tag_variable+"_"+name+".pdf")
                cSign[name].Print(OUTPUTDIR_CHAN+tag_variable+"_"+name+".png")
            cSign[name].Close()


            #!# Perform integral and error
            SignalYieldErrSR[name]  = Double()
            SignalYieldSR[name]     = RooRealVar('SignalYield'+name,  'Signal ' + name + ' normalization',   hSignal[name].IntegralAndError(hSignal[name].GetXaxis().FindBin(j0_sigmin), hSignal[name].GetXaxis().FindBin(j0_sigmax),SignalYieldErrSR[name],""),   0., 1.e10)
            nSignalSR[name] = SignalYieldSR[name].getVal()*signalMultFactor
            print name + " in SR: %.1f +- %.1f" % (nSignalSR[name], SignalYieldErrSR[name])

            if nSignalSR[name]==0:
                print "No signal left for sample: ", name
                print "Skip to next sample!"
                continue
    
            
            #*******************************************************#
            #                                                       #
            #                      Datacard                         #
            #                                                       #
            #*******************************************************#
            # now let's wrap things up and put together a datacard

            card  = 'imax 1\n'#n of bins
            card += 'jmax *\n'#n of backgrounds
            card += 'kmax *\n'#n of nuisance parmeters
            card += '-----------------------------------------------------------------------------------\n'
            card += 'bin               %s\n' % channel
            card += 'observation       %s\n' % '-1.0'
            card += '-----------------------------------------------------------------------------------\n'


#            card += 'bin                                     %-33s%-33s%-33s%-33s%-33s%-33s\n' % (channel, channel, channel, channel, channel, channel)
            card += 'bin                                     %-33s%-33s%-33s\n' % (channel, channel, channel)
            #a bit hardcoded, but okay for now
#            card += 'process                                 %-33s%-33s%-33s%-33s%-33s%-33s\n' % (name, 'ZJetsToNuNu_'+channel, 'WJetsToLNu_'+channel, 'TTbar_'+channel, 'QCD_'+channel, 'VV_'+channel, ) 
            card += 'process                                 %-33s%-33s%-33s\n' % (name,'TTbar_'+channel, 'QCD_'+channel, )
#            card += 'process                                 %-33s%-33s%-33s%-33s%-33s%-33s\n' % ('0', '1', '2', '3', '4', '5',)
            card += 'process                                 %-33s%-33s%-33s\n' % ('0', '1', '2',)

#            card += 'rate                                    %-23f%-23f%-23f%-23f%-23f%-23f\n' % (nSignalSR[name], n_D['ZJetsToNuNu'].getVal() if n_D['ZJetsToNuNu'].getVal()>0 else 0.1, n_D['WJetsToLNu'].getVal(), n_D['TTbar'].getVal(), n_D['QCD'].getVal(), n_D['VV'].getVal())
            card += 'rate                                    %-23f%-23f%-23f\n' % (nSignalSR[name],n_D['TTbar'].getVal(), n_D['QCD'].getVal())

            #if useABCD:
            #    if nQCD_ABCD == 0: #!# 0 background leads to failures in combine
            #        card += 'rate                                    %-23f%-23f\n' % (nSignalSR[name], 0.0001)
            #    else:
            #        card += 'rate                                    %-23f%-23f\n' % (nSignalSR[name], nQCD_ABCD)
            #if not useABCD:
            #    if n_D['QCD'].getVal() == 0: #!# 0 background leads to failures in combine
            #        card += 'rate                                    %-23f%-23f\n' % (nSignalSR[name], 0.0001)
            #    else:
            #        card += 'rate                                    %-23f%-23f\n' % (nSignalSR[name], nQCD_D.getVal())
                    

            card += '-----------------------------------------------------------------------------------\n'

            #Syst uncertainties
            #luminosity
#            card += '%-25s     lnN       %-23f%-23s%-23s%-23s%-23s%-23s\n' % ('sig_norm', 1.+SignalYieldErrSR[name]/nSignalSR[name], '-', '-', '-', '-', '-')
            card += '%-25s     lnN       %-23f%-23s%-23s\n' % ('sig_norm', 1.+SignalYieldErrSR[name]/nSignalSR[name], '-', '-')
            #if useABCD:
            #    card += '%-25s     lnN       %-23s%-23f\n' % ('QCD_norm', '-', 1.+math.sqrt( eQCD_ABCD**2 + (nQCD_ABCD*20./100.)**2 )/nQCD_ABCD)
            #else:
            #    card += '%-25s     lnN       %-23s%-23f\n' % ('QCD_norm', '-', 1.+ error_QCD_D/nQCD_D.getVal() if nQCD_D.getVal()>0 else 1. + 1.)#100% uncertainty!

#            card += '%-25s     lnN       %-23s%-23f%-23s%-23s%-23s%-23s\n' % ('ZJetsToNuNu_norm' , '-', 1. + error_D['ZJetsToNuNu']/n_D['ZJetsToNuNu'].getVal() if n_D['ZJetsToNuNu'].getVal()>0 else 1. + 1., '-', '-', '-', '-')
#            card += '%-25s     lnN       %-23s%-23s%-23f%-23s%-23s%-23s\n' % ('WJetsToLNu_norm' ,  '-', '-', 1. + error_D['WJetsToLNu']/n_D['WJetsToLNu'].getVal() if n_D['WJetsToLNu'].getVal()>0 else 1. + 1., '-', '-', '-')
#            card += '%-25s     lnN       %-23s%-23s%-23s%-23f%-23s%-23s\n' % ('TTbar_norm' ,    '-', '-', '-', 1. + error_D['TTbar']/n_D['TTbar'].getVal() if n_D['TTbar'].getVal()>0 else 1. + 1., '-', '-')
#            card += '%-25s     lnN       %-23s%-23s%-23s%-23s%-23f%-23s\n' % ('QCD_norm' ,    '-', '-', '-', '-', 1. + error_D['QCD']/n_D['QCD'].getVal() if n_D['QCD'].getVal()>0 else 1. + 1., '-')
            card += '%-25s     lnN       %-23s%-23s%-23s\n' % ('TTbar_norm' ,    1. + error_D['TTbar']/n_D['TTbar'].getVal() if n_D['TTbar'].getVal()>0 else 1. + 1., '-', '-')
            card += '%-25s     lnN       %-23s%-23s%-23s\n' % ('QCD_norm' ,    '-',1. + error_D['QCD']/n_D['QCD'].getVal() if n_D['QCD'].getVal()>0 else 1. + 1., '-')
#            card += '%-25s     lnN       %-23s%-23s%-23s%-23s%-23s%-23f\n' % ('VV_norm' ,     '-', '-', '-', '-', '-', 1. + error_D['VV']/n_D['VV'].getVal() if n_D['VV'].getVal()>0 else 1. + 1.)

#            card += '%-25s     lnN       %-23f%-23f%-23f%-23f%-23f%-23f\n' % ('lumi_13TeV', 1.025, 1.025, 1.025, 1.025, 1.025, 1.025)
            card += '%-25s     lnN       %-23f%-23f%-23f\n' % ('lumi_13TeV', 1.025, 1.025, 1.025)

            outname = DATACARDS+ name + '.txt'
            cardfile = open(outname, 'w')
            cardfile.write(card)
            cardfile.close()
            print card
            print 'Datacard for mass', m, 'and ctau', c,  'in channel', channel, 'saved in', outname
            


'''
from v1_met
cut_sel = "HT>100 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && MEt_sign>30"
#cut_sel = "j0_isGenMatched"
write_datacard(options.channel,options.tagvar,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)
'''

#from v0_calo_VBF
if is_array2root_tree:
    tree_name = 'tree'
    #if options.tagvar=="DNN":
    #    cut_sel = "isVBF"
    #else:
#    cut_sel = "MEt_sign>30 && MEt_pt>120 && isVBF && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0"
    cut_sel = "isVBF && HT > 100"
else:
    tree_name = 'ntuple/tree'
#    cut_sel = "MEt.sign>30 && MEt.pt>120 && nPhotons==0 && nMuons==0 && nElectrons==0 && nTaus==0 && isVBF && (HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)"
    cut_sel = "isVBF && HT > 100 && (HLT_DoubleJetsC112_DoubleBTagCSV_p026_DoublePFJetsC172_v || HLT_DoubleJetsC112_DoubleBTagCSV_p014_DoublePFJetsC112MaxDeta1p6_v || HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v || HLT_QuadJet45_TripleBTagCSV_p087_v) && (isMC?Flag_eeBadScFilter:1) && (Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_globalTightHalo2016Filter && Flag_goodVertices && Flag_BadPFMuon && Flag_BadChCand)"

print "AAAH"

if options.tagvar=="DNN":
    write_datacard_1D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)

elif options.tagvar=="nDTSegments":
    write_datacard_1D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)

elif options.tagvar=="ORpfXWP1000":
    print "1D datacards!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    write_datacard_1D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)


elif options.tagvar=="one_pfXWP1000":
    write_datacard_2D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)


elif options.tagvar=="OR3pfXWP1000":
    write_datacard_1D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)
elif options.tagvar=="OR4pfXWP1000":
    write_datacard_1D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)
elif options.tagvar=="OR5pfXWP1000":
    print "1D datacards!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    write_datacard_1D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)


else:
    write_datacard_2D(options.channel,options.tagvar,tree_name=tree_name,cut=cut_sel,draw_all=True,add_string="",j0_crmin=j0_CRMIN,j0_crmax=j0_CRMAX,j0_sigmin=j0_SIGMIN,j0_sigmax=j0_SIGMAX,j1_crmin=j1_CRMIN,j1_crmax=j1_CRMAX,j1_sigmin=j1_SIGMIN,j1_sigmax=j1_SIGMAX,title='',rebin=False)
