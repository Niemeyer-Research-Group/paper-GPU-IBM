#!/usr/bin/env python
#This script makes validation plots for VIV flow

import sys
import os.path
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import brewer2mpl

def main():

    print("-"*80)
    print("Making validaiton plot for VIV.")
    print("-"*80)

    # file with cylinder position
    filename = 'midPosition'

    methods = ['external', 'embedded']
    couplings = ['lc', 'sc']
    # validation data
    Ured_list = [3, 4, 5, 6, 7, 8]
    amplitudes_ak = [0.0714, 0.5616, 0.5234, 0.451, 0.371, 0.0696]
    amplitudes_borazjani = [0.0714, 0.5286, 0.4894, 0.435, 0.381, 0.0696]

    for method in methods:
        for coupling in couplings:
            #name = '{0}_{1}/Ured'.format(i, j) #example: external_lc/Ured

            amplitudes = []
            times = []
            for Ured in Ured_list:
                # example: Ured3/lc_embedded
                name = os.path.join('Ured{:d}'.format(Ured),
                                    '{0}_{1}'.format(coupling, method),
                                    filename
                                    )
                data = np.genfromtxt(name, dtype=float, delimiter='\t', skip_header=1)

                times.append(data[:, 0])
                amplitudes.append(data[:, 2])

            max_amplitudes = [np.max(y) for y in amplitudes]
            # use the median peak because sometimes this one isn't steady state
            max_amplitudes[-1] = viv_median(times[-1], amplitudes[-1])

            plt.plot(Ured_list, amplitudes_ak, 's', label='Ann & Kallindens(2006)')
            plt.plot(Ured_list, amplitudes_borazjani, 'o', label='Borazjani et al.(2008)')
            plt.plot(Ured_list, max_amplitudes, 'x', label='{0}_{1}'.format(method, coupling))
            plt.xlabel('Ured')
            plt.ylabel('Maximum amplitude')
            plt.xlim([2, 9])
            plt.ylim([0, 0.6])
            plt.legend()
            plt.savefig('VIV_{0}_{1}.pdf'.format(method, coupling))
            plt.clf()

    print("\nDone plotting!\n")

def viv_median(x, data):
    peaks = signal.find_peaks_cwt(data, np.arange(1,100))
    peaks_y = [data[i] for i in peaks]
    return np.median(peaks_y)

if __name__ == "__main__":
    main()
