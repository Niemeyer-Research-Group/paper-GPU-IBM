#!/usr/bin/env python
#This script makes the validation plot for an impulsivly started oscillating oscilatting cylinder

import csv
from matplotlib import pyplot as plt
import numpy

print "-"*100
print "Plotting kc5\n"
print "-"*100

a = numpy.genfromtxt('a/forces',delimiter='\t')
b = numpy.genfromtxt('b/forces',delimiter='\t')
c = numpy.genfromtxt('c/forces',delimiter='\t')
d = numpy.genfromtxt('d/forces',delimiter='\t')
e = numpy.genfromtxt('e/forces',delimiter='\t')
f_ = numpy.genfromtxt('f/forces',delimiter='\t')
g = numpy.genfromtxt('g/forces',delimiter='\t')
h = numpy.genfromtxt('h/forces',delimiter='\t')

f, ((axa,axb),(axc, axd),(axe,axf),(axg,axh)) = plt.subplots(4,2,sharex='col', sharey='row')
axa.plot(zip(*a)[0],zip(*a)[1],'-',color='black',linewidth=1)
axb.plot(zip(*b)[0],zip(*b)[1],'-',color='black',linewidth=1)

axc.plot(zip(*c)[0],zip(*c)[1],'-',color='black',linewidth=1)
axd.plot(zip(*d)[0],zip(*d)[1],'-',color='black',linewidth=1)

axe.plot(zip(*e)[0],zip(*e)[1],'-',color='black',linewidth=1)
axf.plot(zip(*f_)[0],zip(*f_)[1],'-',color='black',linewidth=1)

axg.plot(zip(*g)[0],zip(*g)[1],'-',color='black',linewidth=1)
axh.plot(zip(*h)[0],zip(*h)[1],'-',color='black',linewidth=1)

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
axa.set_ylabel('Fd\n(h: 0.0625\n CFL: 0.35)')
axc.set_ylabel('Fd\n(h: 0.03125\n CFL: 0.35)')
axe.set_ylabel('Fd\n(h: 0.03125\n CFL: 0.7)')
axg.set_ylabel('Fd\n(h: 0.03125\n CFL: 1.0)')

plt.tight_layout()
plt.savefig('osc_cylinder.pdf')
plt.clf()

print "\nDone plotting!\n"
