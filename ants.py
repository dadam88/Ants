import pygame, random, math
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = (0, 0, 0)
white = (255,255,255)
# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ants Sim")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

ants = []

for i in range(1000):
    ants.append([random.randrange(0,400), random.randrange(0, 400   )])
    # ants[i] = [200,200]

balls = []
for i in range(10):
    balls.append([random.randrange(0,400), random.randrange(0,400)])

def move_ant(ant, direction):
    dic = {"left": (-1,0), "right": (1,0), "up": (0,-1), "down": (0,1)}
    rmove = dic[direction]

    ant[0] += rmove[0]
    ant[1] += rmove[1]

def get_distance(origin, destination):
    x = origin[0] - destination[0]
    y = origin[1] - destination[1]
    return math.sqrt(x*x + y*y)

def attract(ant, attract_pos):
    movelist = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    possible_move = []
    # check if up/down/right/left will lead them closer to orb
    # append to list, and pick at random
    for move in movelist:
        if get_distance((move[0] + ant[0], move[1] + ant[1]),(attract_pos[0], attract_pos[1])) < get_distance(ant, (attract_pos[0],attract_pos[1])):
            possible_move.append(move)
        else:
            pass
    k = random.choice(possible_move)
    if len(k) > 0:
        ant[0] += k[0]
        ant[1] += k[1]
    else:
        pass

movelist = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
 
    # Clear the screen and set the screen background
    screen.fill(black)
    # attract
    # pygame.draw.circle(screen, [255,0,0], [200,225], 1)
    
    # repel
    pygame.draw.circle(screen, [255,0,0], [180,180], 1)


    # counts = dict()
    # for ant in ants:
    #     counts[(ant[0], ant[1])] = counts.get((ant[0], ant[1]), 0) + 1

  
    for ant in ants:
        # screen.set_at(ant, 255)
        pygame.draw.circle(screen, [0,255,0], ant, 0)
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    for ant in ants:
        # if ant is less than 10 pixels away from attracting orb...
        # if get_distance(ant, (200, 225)) < 10:
        #     attract(ant, (200,225))

        # Same but for repellings
        if get_distance(ant, (180, 180)) < 50:
            possible_move = []
            
            for move in movelist:
                if get_distance((move[0] + ant[0], move[1] + ant[1]),(180,180)) > get_distance(ant, (180,180)):
                    possible_move.append(move)


            k = random.choice(possible_move)
            ant[0] += k[0]
            ant[1] += k[1]

        for ball in balls:
            if get_distance(ant, ball) < 50 and get_distance(ant, ball) > 0:
                attract(ant, ball)
        # elif get_distance(ant, balls[0]) < 50:
        #     attract(ant, balls[0])

        else:
            #Normal random move sets
            moves = ["left", "up", "down", "right"]
            move_ant(ant, random.choice(moves))


    for ant in ants[:]:
        # if get_distance(ant, (210,210)) < 5:
        #     ant[0] = 210
        #     ant[1] = 210
        # if ant == [200, 225]:
        #     ants.remove(ant)

        for ball in balls:
            if ant == ball:
                ants.remove(ant)
        
    print len(ants)

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick()
 
# Be IDLE friendly
pygame.quit()