#!/usr/bin/env python
#This script calculates and plots the order of accuracy for an oscillating cylinder
#import csv
#import argparse
import numpy as np
from numpy import genfromtxt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from scipy import signal
from math import log
from math import exp
#import os
#import os.path
#import sys

def main():
	print "-"*80
	print "Plotting error order"
	print "-"*80
	fileid = '/forces'
	typeid = ['external', 'embedded']
	val=[0]*2
	place = 0
	for methodtype in typeid:
		d1 = genfromtxt(methodtype + '015625' + fileid,dtype=float,delimiter='\t',skip_header=1)
		d2 = genfromtxt(methodtype + '02' + fileid,dtype=float,delimiter='\t',skip_header=1)
		d3 = genfromtxt(methodtype + '03125' + fileid,dtype=float,delimiter='\t',skip_header=1)
		d4 = genfromtxt(methodtype + '0625' + fileid,dtype=float,delimiter='\t',skip_header=1)

		t1 = [d1[i][0] for i in xrange(1,len(d1))]
		t2 = [d2[i][0] for i in xrange(1,len(d2))]
		t3 = [d3[i][0] for i in xrange(1,len(d3))]
		t4 = [d4[i][0] for i in xrange(1,len(d4))]

		y1 = [d1[i][1] for i in xrange(1,len(d1))]
		y2  = [d2[i][1] for i in xrange(1,len(d2))]
		y3  = [d3[i][1] for i in xrange(1,len(d3))]
		y4 = [d4[i][1] for i in xrange(1,len(d4))]

		error = [0]*3
		error[0] = find_error(t1,t4,y1,y4)
		error[1] = find_error(t1,t3,y1,y3)
		error[2] = find_error(t1,t2,y1,y2)
		
		val[place] = error
		place +=1

	

	h=[0.0625, 0.03125, 0.02]
	x_plus = 0.1
	x_minus = 0.01
	y_plus = 1
	y_minus = 0.01
	#calculate reference lines
	ooa_shal = ooa(val[1][:-1],h[:-1])
	ooa_ste = ooa(val[1][1:],h[1:])
	e2_shallow = e2(ooa_shal, val[1][0], h[0], x_plus)
	h1_shallow = h1(ooa_shal, y_minus, val[1][1], h[1])
	e2_steep = e2(ooa_ste, val[1][1], h[1], x_plus)
	h1_steep = h1(ooa_ste, y_minus, val[1][2], h[2])
	ref_h_shallow = [h1_shallow,x_plus]
	ref_err_shallow = [y_minus,e2_shallow]
	ref_h_steep = [h1_steep,x_plus]
	ref_err_steep = [y_minus,e2_steep]

	#plot
	plt.loglog(h,val[0],'-s',label='External')
	plt.loglog(h,val[1],'-^',label='Embedded')
	plt.loglog(ref_h_steep, ref_err_steep,'--k', label='Order of Accuracy = {0}'.format(round(ooa_ste,2)))
	plt.loglog(ref_h_shallow,ref_err_shallow,':k',label='Order of Accuracy = {0}'.format(round(ooa_shal,2)))
	plt.xlabel('Uniform Area Grid Spacing')
	plt.ylabel('Average Error')
	plt.legend(loc='upper left', numpoints=1, fancybox=True)
	plt.savefig('error_oscflow.pdf')
	plt.clf()

	print "\nDone plotting!\n"

def find_error(tfine, tcourse, yfine, ycourse):
	error=[0]*len(tcourse)
	for i in xrange(len(tcourse)-1):
		j = 0
		if tfine[j]>10 or j>=len(tfine):
			pass
		else:
			while tfine[j] <= tcourse[i]:
				j+=1
			if tfine[j] == tcourse[i]:
				error[i]=abs(yfine[j]-ycourse[i])/abs(yfine[j])
			else:
				yf = (yfine[j]-yfine[j-1])/(tfine[j]-tfine[j-1])*(tcourse[i]-tfine[j-1])+yfine[j]
				error[i]=abs(yfine[j]-ycourse[i])/abs(yfine[j])
	errorsum = sum(error)
	return errorsum/len(error)

def ooa(err,h):
	return log(err[1]/err[0]) / log(h[1]/h[0])

def e2(ooa, e1, h1, h2):
	return e1*exp(ooa*log(h2/h1))

def h1(ooa, e1, e2, h2):
	return h2/exp(log(e2/e1)/ooa)
if __name__ == "__main__":
	main()

