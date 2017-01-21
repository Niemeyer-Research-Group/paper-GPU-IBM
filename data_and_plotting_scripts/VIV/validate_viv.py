#!/usr/bin/env python
#This script makes validation plots for VIV flow
#import csv
#import argparse
import numpy as np
from numpy import genfromtxt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy import signal
#import os
#import os.path
#import sys

def main():

	print "-"*80
	print "Making validaiton plot for VIV."
	print "-"*80
	fileid = '/midPosition'
	method = ["external", "embedded"]
	coupling = ["lc","sc"]
	#validation data
	x = [3, 4, 5, 6, 7, 8] 
	y_ak = [0.0714, 0.5616, 0.5234, 0.451, 0.371, 0.0696]
	y_b = [0.0714, 0.5286, 0.4894, 0.435, 0.381, 0.0696]
	for i in method:
		for j in coupling:
			name = '{0}_{1}/Ured'.format(i,j) #example: external_lc/Ured
			d3 = genfromtxt(name + '3' + fileid,dtype=float,delimiter='\t',skip_header=1)
			d4 = genfromtxt(name + '4' + fileid,dtype=float,delimiter='\t',skip_header=1)
			d5 = genfromtxt(name + '5' + fileid,dtype=float,delimiter='\t',skip_header=1)
			d6 = genfromtxt(name + '6' + fileid,dtype=float,delimiter='\t',skip_header=1)
			d7 = genfromtxt(name + '7' + fileid,dtype=float,delimiter='\t',skip_header=1)
			d8 = genfromtxt(name + '8' + fileid,dtype=float,delimiter='\t',skip_header=1)

			t3 = [d3[i][0] for i in xrange(1,len(d3))]#(1,len) skips headers
			t4 = [d4[i][0] for i in xrange(1,len(d4))]
			t5 = [d5[i][0] for i in xrange(1,len(d5))]
			t6 = [d6[i][0] for i in xrange(1,len(d6))]
			t7 = [d7[i][0] for i in xrange(1,len(d7))]
			t8 = [d8[i][0] for i in xrange(1,len(d8))]

			y3 = [d3[i][2] for i in xrange(1,len(d3))]
			y4 = [d4[i][2] for i in xrange(1,len(d4))]
			y5 = [d5[i][2] for i in xrange(1,len(d5))]
			y6 = [d6[i][2] for i in xrange(1,len(d6))]
			y7 = [d7[i][2] for i in xrange(1,len(d7))]
			y8 = [d8[i][2] for i in xrange(1,len(d8))]

			max3 = max(y3);
			max4 = max(y4);
			max5 = max(y5);
			max6 = max(y6);
			max7 = max(y7);
			max8 = viv_median(t8,y8); #use the median peak because sometimes this one isn't steady state

			y = [max3, max4, max5, max6, max7, max8]

			plt.plot(x,y_ak,'s',label='Ann & Kallindens(2006)')
			plt.plot(x,y_b,'o',label='Borazjani et al.(2008)')
			plt.plot(x,y,'x',label='{0}_{1}'.format(i,j))
			plt.xlabel('Ured')
			plt.ylabel('Max Amplitude')
			plt.xlim([2,9])
			plt.ylim([0,0.6])
			plt.legend()
			plt.savefig('VIV_{0}_{1}.pdf'.format(i,j))
			plt.clf()
	
	print "\nDone plotting!\n"

def viv_median(x,data):
	peaks = signal.find_peaks_cwt(data, np.arange(1,100))
	peaks_y = [data[i] for i in peaks]
	return np.median(peaks_y)

if __name__ == "__main__":
	main()

