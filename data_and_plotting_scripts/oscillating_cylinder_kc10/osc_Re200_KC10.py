#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#This script plots drag around an inline oscillating cylinder for re 200 kc 10 against dutsch et als work at cycle 14
import argparse
import os
import os.path
import sys
import csv
import matplotlib
from matplotlib import pyplot as plt
import numpy


validationData = 'osc_Re200_KC10_Dutsch.txt'

print "\n"+"-"*100
print "Plotting validation for flow around inline oscillating cylinder with Re200 and KC10\n"
print "-"*100+"\n"

experiment = numpy.genfromtxt(validationData,delimiter='\t')
external = numpy.genfromtxt('external/forces',delimiter='\t')
embedded = numpy.genfromtxt('embedded/forces',delimiter='\t')

#external
plt.plot([i-13 for i in zip(*external)[0]],[i*5 for i in zip(*external)[1]],'-',color='blue',linewidth=2,label='External')
plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = u'Dütsch et al.')
plt.legend(loc='lower right',numpoints=1, fancybox=True)
plt.xlabel('t/T')
plt.ylabel('Fd')
plt.ylim([-6,6])
plt.xlim([0,1])
plt.savefig('External_static_kc10.pdf')
plt.clf()

#emb
plt.plot([i-13 for i in zip(*embedded)[0]],[i*5 for i in zip(*embedded)[1]],'-',color='blue',linewidth=2,label='Embedded')
plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = u'Dütsch et al.')
plt.legend(loc='lower right',numpoints=1, fancybox=True)
plt.xlabel('t/T')
plt.ylabel('Fd')
plt.ylim([-6,6])
plt.xlim([0,1])
plt.savefig('Embedded_static_kc10.pdf')
plt.clf()

print '\nDone plotting!'
