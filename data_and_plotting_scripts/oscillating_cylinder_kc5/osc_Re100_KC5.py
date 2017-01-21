#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#This script makes the validation plot for an in-line oscilatting cylinder driven flow with Re100 KC5

import argparse
import os
import os.path
import sys
import csv
import matplotlib
from matplotlib import pyplot as plt
import numpy

validationData = 'osc_Re100_KC5_Dutsch.txt'

print "-"*100
print "Plotting kc5\n"
print "-"*100

experiment = numpy.genfromtxt(validationData,delimiter='\t')
external = numpy.genfromtxt('external/forces_init',delimiter='\t')
embedded = numpy.genfromtxt('embedded/forces_init',delimiter=',')
cite = u'Dütsch et al.'
print cite

#mult by 5 because the diameter is 0.2
#Initial external
plt.plot(zip(*external)[0],[i*5 for i in zip(*external)[1]],'-',color='blue',linewidth=2,label='External')
plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = cite)
plt.legend(loc='lower right',numpoints=1, fancybox=True)
plt.xlabel('t/T')
plt.ylabel('Fd')
plt.ylim([-2,2])
plt.savefig('staticexinit.pdf')
plt.clf()

#emb init
plt.plot(zip(*embedded)[0],[i*5 for i in zip(*embedded)[1]],'-',color='blue',linewidth=2,label='Embedded')
plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = cite)
plt.legend(loc='lower right',numpoints=1, fancybox=True)
plt.xlabel('t/T')
plt.ylabel('Fd')
plt.ylim([-2,2])
plt.savefig('staticeminit.pdf')
plt.clf()

external = numpy.genfromtxt('external/forces_ss',delimiter=',')
embedded = numpy.genfromtxt('embedded/forces_ss',delimiter=',')

#ss external
plt.plot(zip(*external)[0],[i*5 for i in zip(*external)[1]],'-',color='blue',linewidth=2,label='External')
plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = cite)
plt.legend(loc='lower right',numpoints=1, fancybox=True)
plt.xlabel('t/T')
plt.ylabel('Fd')
plt.ylim([-2,2])
plt.savefig('staticexss.pdf')
plt.clf()

#ss emb
plt.plot(zip(*embedded)[0],[i*5 for i in zip(*embedded)[1]],'-',color='blue',linewidth=2,label='Embedded')
plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = cite)
plt.legend(loc='lower right',numpoints=1, fancybox=True)
plt.xlabel('t/T')
plt.ylabel('Fd')
plt.ylim([-2,2])
plt.savefig('staticemss.pdf')
plt.clf()

print "\nDone plotting!\n"
