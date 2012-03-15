from pylab import *

ion()

import json
import smooth

from connectClient import CEE
CEE = CEE()

calData = json.loads(open("137423432303FFFF91FF1100C100_1327702983256.json").read())

calI = smooth.smooth(calData['sweep']['a_i'], 50)

calV = calData['sweep']['a_v']

calI = calI[0:len(calI)/5]
calV = calV[0:len(calV)/5]

plot(calV, calI)
figure()

indexes = []

findNearest = lambda lst, value: abs(array(lst)-value).argmin()

resistance = lambda vi: vi[0]/(vi[1]/1000)

def getCaldValues(voltage):
	v, i = CEE.getInput('a', .1, 1, CEE.setOutput('a', 'v', voltage)['startSample']+100)
	idx = findNearest(calV, v)
	indexes.append(idx)
	i = i - calI[idx]
	return [v, i]

spread=linspace(1.7,2.3,200)
#plot(spread, [resistance(getCaldValues(v)) for v in spread])
plot(spread, [getCaldValues(v)[1] for v in spread])
