#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#This script plots drag around an inline oscillating cylinder for re 200 kc 10 against dutsch et als work at cycle 14

import sys
import os.path
import numpy
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import brewer2mpl

plt.ion()

home_dir = os.path.join(sys.path[0], '../../')
home_dir = os.path.realpath(home_dir)
d = os.path.join(home_dir, 'figures')

validationData = 'osc_Re200_KC10_Dutsch.txt'

print("\n"+"-"*100)
print("Plotting validation for flow around inline oscillating cylinder with Re200 and KC10\n")
print("-"*100+"\n")

colors = brewer2mpl.get_map('Dark2', 'qualitative', 3).mpl_colors

experiment = numpy.genfromtxt(validationData, delimiter=',')
external = numpy.genfromtxt('external/forces.csv', delimiter=',')
embedded = numpy.genfromtxt('embedded/forces.csv', delimiter=',')
cite = u'Dütsch et al.'

plt.plot(external[:,0]-13, 5.*external[:,1], '-', color=colors[0], linewidth=2, label='External')
plt.plot(embedded[:,0]-13, 5.*embedded[:,1], '--', color=colors[1], linewidth=2, label='Embedded')
plt.plot(experiment[:,0], experiment[:,1], 'o', color=colors[2], markersize=8, label=cite)
plt.legend(loc='lower right', numpoints=1)
plt.xlabel('Nondimensional time')
plt.ylabel('Drag force')
plt.ylim([-6, 6])
plt.xlim([0, 1])
pp = PdfPages(os.path.join(d, 'static_kc10.pdf'))
pp.savefig()
pp.close()
plt.clf()

#external
# plt.plot([i-13 for i in zip(*external)[0]],[i*5 for i in zip(*external)[1]],'-',color='blue',linewidth=2,label='External')
# plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label=cite)
# plt.legend(loc='lower right',numpoints=1, fancybox=True)
# plt.xlabel('t/T')
# plt.ylabel('Fd')
# plt.ylim([-6,6])
# plt.xlim([0,1])
# plt.savefig('External_static_kc10.pdf')
# plt.clf()
#
# #emb
# plt.plot([i-13 for i in zip(*embedded)[0]],[i*5 for i in zip(*embedded)[1]],'-',color='blue',linewidth=2,label='Embedded')
# plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label=cite)
# plt.legend(loc='lower right',numpoints=1, fancybox=True)
# plt.xlabel('t/T')
# plt.ylabel('Fd')
# plt.ylim([-6,6])
# plt.xlim([0,1])
# plt.savefig('Embedded_static_kc10.pdf')
# plt.clf()

print '\nDone plotting!'
