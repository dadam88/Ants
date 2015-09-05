import pygame, random, math
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = (0, 0, 0)
white = (255,255,255)
# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

ants = []
for i in range(1000):
    ants.append([random.randrange(195,205), random.randrange(195, 205   )])
    ants[i] = [200,200]

def move_ant(ant, direction):
    dic = {"left": (-1,0), "right": (1,0), "up": (0,-1), "down": (0,1)}
    rmove = dic[direction]

    ant[0] += rmove[0]
    ant[1] += rmove[1]

def movesmart(ant):
    for newmove in smartmoves:
        if get_distance((newmove[0] + ant[0], newmove[1] + ant[1]),(200,225)) < get_distance(ant, (200,225)):
            return newmove

def moverepel(ant):
    for newmove in smartmoves:
        if get_distance((newmove[0] + ant[0], newmove[1] + ant[1]),(180,180)) > get_distance(ant, (180,180)):
            return newmove

smartmoves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def get_distance(origin, destination):
    x = origin[0] - destination[0]
    y = origin[1] - destination[1]
    return math.sqrt(x*x + y*y)

while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
 
    # Clear the screen and set the screen background
    screen.fill(white)
 
    # Draw on the screen a green line from (0,0) to (50.75)
    # 5 pixels wide.

    pygame.draw.circle(screen, [255,0,0], [200,225], 1)
    pygame.draw.circle(screen, [255,0,0], [180,180], 1)
    
    # Draw a circle
    for ant in ants:
        pygame.draw.circle(screen, black, ant, 0)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    for ant in ants:
        if get_distance(ant,(200,225)) < 10:
            k = movesmart(ant)
            ant[0] += k[0]
            ant[1] += k[1]
            
        elif get_distance(ant, (180, 180)) < 10:
            k = moverepel(ant)
            ant[0] += k[0]
            ant[1] += k[1]

        else:
			moves = ["left", "up", "down", "right"]
			move_ant(ant, random.choice(moves))


    for ant in ants[:]:
        # if get_distance(ant, (210,210)) < 5:
        #     ant[0] = 210
        #     ant[1] = 210
        if ant == [200, 225]:
            ants.remove(ant)
        


    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick()
 
# Be IDLE friendly
pygame.quit()