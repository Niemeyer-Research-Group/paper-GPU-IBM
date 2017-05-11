#!/usr/bin/env python
#This script makes the plot for all four VIVs results on the same plot

import sys
import os.path
import numpy
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import brewer2mpl

def main():

    plt.ion()

    home_dir = os.path.join(sys.path[0], '../../')
    home_dir = os.path.realpath(home_dir)
    d = os.path.join(home_dir, 'figures')

    print("-"*80)
    print("Making validaiton plot for an oscillating cylinder in flow.")
    print("-"*80)

    colors = brewer2mpl.get_map('Dark2', 'qualitative', 6).mpl_colors

    ys = [0.0714, 0.5616, 0.5234, 0.451, 0.371, 0.0696]
    yc = [0.0714, 0.5286, 0.4894, 0.435, 0.381, 0.0696]
    em_lc = [0.07161494006079072,0.5717792720930622,0.5344207235887237, 0.46769951947874355, 0.38874337573979395, 0.14012940247913452] #data output from embedded loose coupling
    em_sc = [0.07406970331657958, 0.5443322122816592, 0.48226014304124076, 0.3941003346010647, 0.310016601470416, 0.0881615228777407] #data output from embeded strong coupling
    ex_lc = [0.07041599084467354, 0.5675364513644794, 0.5202419621998599, 0.4533280558268404, 0.38804988964561826, 0.12004663709542096] #data output from external loose coupling
    ex_sc = [0.0742857142857144, 0.5599999999999999, 0.5069387755102042, 0.4342857142857142, 0.35346938775510206, 0.10448979591836749] #data output from external strong coupling
    x = [3, 4, 5, 6, 7, 8]

    labels = ['Ann & Kallindens (2006)', 'Borazjani et al. (2008)', 'External, loose',
              'External, strong', 'Embedded, loose', 'Embedded, strong'
              ]
    markers = ['s', 'o', '^', 'd', 'x', '+']

    for idx, data in enumerate([ys, yc, ex_lc, ex_sc, em_lc, em_sc]):
        plt.plot(x, data, marker=markers[idx], color=colors[idx], label=labels[idx], markersize=8, linestyle='')

    plt.xlabel(r'$U_{\mathrm{red}}$')
    plt.ylabel('Maximum amplitude')
    plt.xlim([2, 9])
    plt.ylim([0, 0.6])
    plt.legend(loc='best', numpoints=1)

    pp = PdfPages(os.path.join(d, 'VIV_combine.pdf'))
    pp.savefig()
    pp.close()

    plt.clf()

#run
main()
