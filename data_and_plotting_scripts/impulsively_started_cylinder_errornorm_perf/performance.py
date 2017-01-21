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
	grid_cylinder_750ti = [170,208,450,890,135,208,450,890,162,352,372,462]
	time_cylinder_750ti = [117,236,1017,3820,81,127,364,1487,390,894,1099,2880]
	time_cylinder_k20 = [43,61,151,563,20,26,51,174,122,206,281,762]

	for i in xrange(len(grid_cylinder_750ti)):
		grid_cylinder_750ti[i] = grid_cylinder_750ti[i]**2

	plt.loglog(grid_cylinder_750ti[4:8], time_cylinder_750ti[4:8] ,'-.sb', label='External-750ti')
	plt.loglog(grid_cylinder_750ti[8:12],time_cylinder_750ti[8:12],'-.^g', label='Embedded-750ti')
	plt.loglog(grid_cylinder_750ti[4:8], time_cylinder_k20[4:8]   ,'-sb' , label='External-k20')
	plt.loglog(grid_cylinder_750ti[8:12],time_cylinder_k20[8:12]  ,'-^g' , label='Embedded-k20')
	plt.xlabel('Grid Size (total cell count)')
	plt.ylabel('Run Time (s)')
	plt.legend(loc='upper left', numpoints=1, fancybox=True)
	plt.savefig('cylinder_performance.pdf')
	plt.clf()

if __name__ == "__main__":
	main()

