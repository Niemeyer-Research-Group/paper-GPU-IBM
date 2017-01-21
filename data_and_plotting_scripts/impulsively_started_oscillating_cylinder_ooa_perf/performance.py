#!/usr/bin/env python
#This script plots cylinder performance
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
	print "Plotting error order"
	print "-"*80
	fileid = '/forces'
	grid_osc_750ti = [346, 318, 222, 198, 346, 318, 222, 198]
	time_osc_750ti = [206, 167, 71, 51, 7760, 7171, 1112, 414]
	time_osc_k20 =   [134, 106, 62, 52, 4380,6005,929,387]
	
	for i in xrange(len(grid_osc_750ti)):
		grid_osc_750ti[i] = grid_osc_750ti[i]**2

	plt.loglog(grid_osc_750ti[0:4],time_osc_750ti[0:4],'-.sb', label='External-750ti')
	plt.loglog(grid_osc_750ti[4:8],time_osc_750ti[4:8],'-.^g', label='Embedded-750ti')
	plt.loglog(grid_osc_750ti[0:4],time_osc_k20[0:4],'-sb', label='External-k20')
	plt.loglog(grid_osc_750ti[4:8],time_osc_k20[4:8],'-^g', label='Embedded-k20')
	plt.xlabel('Grid Size (total cell count)')
	plt.ylabel('Run Time (s)')
	plt.axis([30000,200000,10,10000])
	plt.legend(loc='lower right', numpoints=1, fancybox=True)
	plt.savefig('osc_performance.pdf')
	plt.clf()

if __name__ == "__main__":
	main()

