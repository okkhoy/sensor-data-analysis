import sys, re

datafile = open(sys.argv[1])

positionfile = open('position.csv', 'w')
laserfile = open('laser.csv','w')

position = re.compile(r'\b(position)\b', flags=re.IGNORECASE)
laser = re.compile(r'\b(laser)\b', flags=re.IGNORECASE)


def mean(a):
	return sum(a)/float(len(a))
	
def chunk(l, n):
	for i in range(0, len(l), n):
		yield l[i:i+n]
		
		
for line in datafile:
	line = line.strip()
	if position.search(line):
		words = line.split()
		strg = words[0] + ',' + ','.join(words[6:]) + '\n'
		positionfile.write(strg)
	if laser.search(line):
		words = line.split()
		ts = words[0]
		words = words[6:]
		words = [float(w) for w in words]
		#print words
		#laserd = [words[i:i+3] for i in range(0, len(words), 3)]
		laserd = chunk(words, 3)
		laserd_avg = map(mean, zip(*laserd))
		laserd_avg = [str(w) for w in laserd_avg]
		strg = str(ts) + ',' + ','.join(laserd_avg) + '\n'
		laserfile.write(strg)
		
		


		
