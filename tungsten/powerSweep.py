#!/usr/bin/python
# -*- coding: utf-8 -*-
from pylab import linspace, subplot, plot, title, xlabel, ylabel, show, diff

from connectClient import CEE
CEE = CEE()

resistance = lambda vi: vi[0]/(vi[1]/1000)

setAndGet = lambda i:  CEE.getInput('a', .1, 1, CEE.setOutput('a', 'i', i)['startSample']+100)

spread = linspace(10, 130, 300)

def WR(i):
	v, i = setAndGet(i)
	return v*i, resistance([v, i])


values = [WR(i) for i in spread] 
values = zip(*values)

subplot(211)
plot(values[0], values[1], '.')
title("exploring the temperature-dependent resistance of a tungsten filament")
ylabel(u"resistance (Ω)")

subplot(212)
plot(values[0][1::], diff(values[1]), '.')
ylabel(u"∂Ω/∂W")
xlabel(u"power (mW)")

CEE.setOutput()
show()
