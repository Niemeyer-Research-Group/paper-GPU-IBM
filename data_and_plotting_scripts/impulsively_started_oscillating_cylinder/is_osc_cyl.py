#!/usr/bin/env python
#This script makes the validation plot for an impulsivly started oscillating oscilatting cylinder

import sys
import os.path
import numpy
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import brewer2mpl

plt.ion()

home_dir = os.path.join(sys.path[0], '../../')
home_dir = os.path.realpath(home_dir)
direct = os.path.join(home_dir, 'figures')

print("-"*100)
print("Plotting kc5\n")
print("-"*100)

a = numpy.genfromtxt('forces_ext_cfl0p35_h0625', delimiter=',')
b = numpy.genfromtxt('forces_emb_cfl0p35_h0625', delimiter=',')
c = numpy.genfromtxt('forces_ext_cfl0p35_h03125', delimiter=',')
d = numpy.genfromtxt('forces_emb_cfl0p35_h03125', delimiter=',')
e = numpy.genfromtxt('forces_ext_cfl0p7_h03125', delimiter=',')
f = numpy.genfromtxt('forces_emb_cfl0p7_h03125', delimiter=',')
g = numpy.genfromtxt('forces_ext_cfl1p0_h03125', delimiter=',')
h = numpy.genfromtxt('forces_emb_cfl1p0_h03125', delimiter=',')

fig, ((axa,axb), (axc,axd), (axe,axf), (axg,axh)) = plt.subplots(4, 2, sharex='col', sharey='row')
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
plt.grid(False)

axa.plot(a[:,0], a[:,1], '-', color='black', linewidth=1)
axb.plot(b[:,0], b[:,1], '-', color='black', linewidth=1)

axc.plot(c[:,0], c[:,1], '-', color='black', linewidth=1)
axd.plot(d[:,0], d[:,1], '-', color='black', linewidth=1)

axe.plot(e[:,0], e[:,1], '-', color='black', linewidth=1)
axf.plot(f[:,0], f[:,1], '-', color='black', linewidth=1)

axg.plot(g[:,0], g[:,1], '-', color='black', linewidth=1)
axh.plot(h[:,0], h[:,1], '-', color='black', linewidth=1)

#set axes
axg.set_xlim(0,10)
axh.set_xlim(0,10)
axa.set_ylim(0,2)
axc.set_ylim(0,2)
axe.set_ylim(0,2)
axg.set_ylim(0,2)

#labels
axa.set_title('External')
axb.set_title('Embedded')
axg.set_xlabel('Time')
axh.set_xlabel('Time')

#run info
axa.set_ylabel('h: 0.0625\nCFL: 0.35')
axc.set_ylabel('h: 0.03125\nCFL: 0.35')
axe.set_ylabel('h: 0.03125\nCFL: 0.7')
axg.set_ylabel('h: 0.03125\nCFL: 1.0')

plt.ylabel('Drag force', labelpad=25)

plt.tight_layout()
pp = PdfPages(os.path.join(direct, 'osc_cylinder.pdf'))
pp.savefig(bbox_inches='tight')
pp.close()
plt.clf()

print("\nDone plotting!\n")
