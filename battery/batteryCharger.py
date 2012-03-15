from connectClient import CEE
CEE = CEE()

samples = []

while True:
	if CEE.getInput()[0] < 4.2:
		sample = CEE.getInput('a', 2, 1, CEE.setOutput('a', 'i', 200)['startSample'])
		# constant current
	else:
		sample = CEE.getInput('a', 2, 1, CEE.setOutput('a', 'v', 4.2)['startSample'])
		# constant voltage
		if sample[1] < 10:
			break
		# if in CV mode, current drops below 10mA, exit
	samples.append(sample)
	print samples[-1]
