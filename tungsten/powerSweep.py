#!/usr/bin/python
# -*- coding: utf-8 -*-
from pylab import *
from connectClient import CEE
CEE = CEE()
ion()

setAndGet = lambda x:  CEE.getInput('a', .1, 1, CEE.setOutput('a', 'i', x)['startSample']+100)


voltages = []
currents = []


for mA in arange(5, 130):
	[v, i] = setAndGet(mA)
	voltages.append(v)
	currents.append(i)

voltage = array(voltages)
current = array(currents)
resistance = voltages/(current/1000)
power = voltages*(current/1000)
temperature = [((r/resistance[0])-1)/.004403+20 for r in resistance]

subplot(221)
plot(resistance, temperature, '.')
xlabel(u"resistance (Ω)")
ylabel(u"temperature (ºC)")

subplot(223)
semilogx(power[1::], diff(resistance), '.')
ylabel(u"∂Ω/∂W")
xlabel("power (W)")

subplot(222)
loglog(power, temperature, '.')
ylabel(u"temperature (ºC)")
xlabel("power (W)")

subplot(224)
loglog(power[1::], diff(temperature), '.')
ylabel(u"∂ºC/∂W")
xlabel("power (W)")

CEE.setOutput()
show()
