from connectClient import CEE
CEE = CEE()

while True:
	if CEE.getInput('a', .1, 1, CEE.setOutput('a', 'i', 0)['startSample'])[0][0] < 3.7:
		break
		# if open-cell voltage is less than 3.7 then exit
	else:
		print CEE.getInput('a', 2, 1, CEE.setOutput('a', 'i', -100)['startSample'])
		# otherwise, draw a 100mA load
