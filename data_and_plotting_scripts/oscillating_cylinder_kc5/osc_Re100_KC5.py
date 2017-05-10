#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#This script makes the validation plot for an in-line oscilatting cylinder driven flow with Re100 KC5

import sys
import os.path
import numpy
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import brewer2mpl

plt.ion()

validationData = 'osc_Re100_KC5_Dutsch.txt'

home_dir = os.path.join(sys.path[0], '../../')
home_dir = os.path.realpath(home_dir)
d = os.path.join(home_dir, 'figures')

print("-"*100)
print("Plotting kc5\n")
print("-"*100)

colors = brewer2mpl.get_map('Dark2', 'qualitative', 3).mpl_colors

experiment = numpy.genfromtxt(validationData, delimiter=',')
external = numpy.genfromtxt('external/forces_init.csv', delimiter=',')
embedded = numpy.genfromtxt('embedded/forces_init.csv', delimiter=',')
cite = u'Dütsch et al.'
print(cite)

#Initial external and embedded
#multiply by 5 because the diameter is 0.2
plt.plot(external[:,0], 5.*external[:,1], '-', color=colors[1], linewidth=2, label='External')
plt.plot(embedded[:,0], 5.*embedded[:,1], '--', color=colors[2], linewidth=2, label='Embedded')
plt.plot(experiment[:,0], experiment[:,1], 'o', color=colors[0], markersize=8, label=cite)
plt.legend(loc='lower right', numpoints=1)
plt.xlabel('Nondimensional time')
plt.ylabel('Drag force')
plt.ylim([-2, 2])
pp = PdfPages(os.path.join(d, 'static_init.pdf'))
pp.savefig()
pp.close()
plt.clf()

#emb init
# plt.plot(external[:,0], 5.*external[:,1], '-', color='blue', linewidth=2, label='External')
# plt.plot(embedded[:,0], 5.*embedded[:,1], '--', color='green', linewidth=2, label='Embedded')
# plt.plot(experiment[:,0], experiment[:,1], 'o', color='red', markersize=8, label=cite)
# plt.legend(loc='lower right', numpoints=1)
# plt.xlabel('Nondimensional time')
# plt.ylabel('Drag force')
# plt.ylim([-2,2])
# pp = PdfPages(os.path.join(d, 'static_em_init.pdf'))
# pp.savefig()
# pp.close()
# plt.clf()

external = numpy.genfromtxt('external/forces_ss.csv',delimiter=',')
embedded = numpy.genfromtxt('embedded/forces_ss.csv',delimiter=',')

# steady state
#multiply by 5 because the diameter is 0.2
plt.plot(external[:,0], 5.*external[:,1], '-', color=colors[1], linewidth=2, label='External')
plt.plot(embedded[:,0], 5.*embedded[:,1], '--', color=colors[2], linewidth=2, label='Embedded')
plt.plot(experiment[:,0], experiment[:,1], 'o', color=colors[0], markersize=8, label=cite)
plt.legend(loc='lower right', numpoints=1)
plt.xlabel('Nondimensional time')
plt.ylabel('Drag force')
plt.ylim([-2,2])
pp = PdfPages(os.path.join(d, 'static_ss.pdf'))
pp.savefig()
pp.close()
plt.clf()

# #ss external
# plt.plot(zip(*external)[0],[i*5 for i in zip(*external)[1]],'-',color='blue',linewidth=2,label='External')
# plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = cite)
# plt.legend(loc='lower right', numpoints=1)
# plt.xlabel('Nondimensional time')
# plt.ylabel('Drag force')
# plt.ylim([-2,2])
# pp = PdfPages(os.path.join(d, 'static_ex_ss.pdf'))
# pp.savefig()
# pp.close()
# plt.clf()
#
# #ss emb
# plt.plot(zip(*embedded)[0],[i*5 for i in zip(*embedded)[1]],'-',color='blue',linewidth=2,label='Embedded')
# plt.plot(zip(*experiment)[0],zip(*experiment)[1],'o', color = 'red', markersize = 8, label = cite)
# plt.legend(loc='lower right', numpoints=1)
# plt.xlabel('Nondimensional time')
# plt.ylabel('Drag force')
# plt.ylim([-2,2])
# pp = PdfPages(os.path.join(d, 'static_em_ss.pdf'))
# pp.savefig()
# pp.close()
# plt.clf()

print("\nDone plotting!\n")
