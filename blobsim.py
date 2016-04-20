'''
Create Blobs.
Bigger Blobs eat smaller blobs.
Smaller Blobs run from bigger blobs.
'''
import pygame, random, math

class Blob():
    moves = {"left": [-1,0], "right": [1,0], 
    "up": [0,-1], "down": [0,1], 
    "upleft": [-1,-1], "downleft": [-1,1], 
    "upright": [1,-1], "bottomright": [1,1]}

    def __init__(self):
        self.pos = [random.randrange(0,400),random.randrange(0,400)]
        self.powerlevel = random.randrange(1,3)

    def move_blob(self, new_position):
        self.pos[0] = new_position[0]
        self.pos[1] = new_position[1]

    def add_xys(self, xy):
        self.pos[0] += xy[0]
        self.pos[1] += xy[1]

    def get_closer(self, move, new_position):
        current_delta = get_distance(self.pos, new_position)
        z = [x + y for x, y in zip(self.pos, move)]

        delta = get_distance(z, new_position)
        return delta < current_delta

def fight(blobA, blobB):
	if blobA.pos == blobB.pos and blobA != blobB:
		if blobA.powerlevel > blobB.powerlevel:
			return blobB
		elif blobA.powerlevel == blobB.powerlevel:
			return blobB
		else:
			return blobA



def get_distance(origin, destination):
    '''(x,y), (x,y) -> returns float
    Calculates distance from (x,y) to (x,y)
    '''
    x = origin[0] - destination[0]
    y = origin[1] - destination[1]
    return math.sqrt(x*x + y*y)

def within_distance(origin, destination, distance):
    '''(x,y) , (x,y), int -> returns bool
    Checks if origin to destination is within a distance
    '''
    return get_distance(origin, destination) <= distance

def main(): 
    # Initialize the game engine
    pygame.init()
     
    # Define the colors we will use in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    # Set the height and width of the SCREEN
    SIZE = [400, 400]
    SCREEN = pygame.display.set_mode(SIZE)
     
    pygame.display.set_caption("blobs Sim")
    clock = pygame.time.Clock() 

    # Create list of blobs
    blobs = []   
    for i in range(100):
        blobs.append(Blob())
    
    # Loop until the user clicks the close button.
    done = False
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        deaths = []
        

        for blob in blobs:
        	
        	scanned = []
        	# Accounts for scanning self until I have a better fix
        	for target in blobs:
        		if target == blob:
        			continue

        		# scan surroudning of blob
        		if within_distance(blob.pos, target.pos, 100):
        			scanned.append(target)

	        if len(scanned) > 0:
	        
	        	'''
	        	# If any blobs in radius have power level greater
	        	if any(x.powerlevel > blob.powerlevel for x in scanned):
	        		# Move away from from greatest
		        	newlist = sorted(scanned, key=lambda x: x.powerlevel, reverse=True)

	        		# Flee time

	        	else:
	        		'''
	        	# Move towards weaker blob
     			for scan in scanned:
     				
	        		loser = fight(blob,target)
	        		
	        		if loser != None:
	        			if loser not in deaths:
		        			deaths.append(loser)
		        			blob.powerlevel += 1
	    	
        		weaker_blob = scanned[0]

        		possible_moves = []
        		for move in blob.moves.keys():
        			if blob.get_closer(blob.moves[move], weaker_blob.pos):
        				possible_moves.append(blob.moves[move])

        		if possible_moves:
	      			chosen_move = random.choice(possible_moves)
	      			blob.add_xys(chosen_move)


	        else:
	        	# move randomly
	        	rng_move = random.choice(blob.moves.values())
	        	blob.add_xys(rng_move)

    	for death in deaths:
    		
    		blobs.remove(death)
        # Draw blobs
        for blob in blobs:
            pygame.draw.rect(SCREEN, [0,255,0], [blob.pos[0], blob.pos[1],blob.powerlevel,blob.powerlevel], 0)

        pygame.display.flip()
        # Clear the SCREEN and set the SCREEN background
        SCREEN.fill(BLACK)

        clock.tick(60)
     
    # Can't use X on window withou this command
    pygame.quit()


if __name__ == '__main__':
  main()
