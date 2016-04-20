import random

class Blob():
	def __init__(self):
		self.powerlevel = random.randrange(1,100)

def fight(alpha, beta):
	if alpha.powerlevel > beta.powerlevel:
		return beta
	else:
		return alpha

blobs = []
deaths = []

for i in range(100):
	blobs.append(Blob())

print len(blobs)

for blob in blobs:
	for i in range(len(blobs)):
		loser = fight(blob, blobs[i])
		print loser.powerlevel
	
		deaths.append(loser)


print len(blobs)

for death in deaths:
	if death in blobs:
		blobs.remove(death)

print len(blobs)