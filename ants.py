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

balls = []
for i in range(10):
    balls.append([random.randrange(0,400), random.randrange(0,400)])

def move_ant_to(ant, pos):
    ant[0] += pos[0]
    ant[1] += pos[1]

def get_distance(origin, destination):
    x = origin[0] - destination[0]
    y = origin[1] - destination[1]
    return math.sqrt(x*x + y*y)

def attract(ant, attract_pos):
    k = random.choice(legit_moves(ant, attract_pos))
    if len(k) > 0:
        ant[0] += k[0]
        ant[1] += k[1]
    else:
        pass

def legit_moves(ant, attract_pos):
    movelist = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    possible_moves = list()

    for move in movelist:
        if get_distance((move[0] + ant[0], move[1] + ant[1]),(attract_pos[0], attract_pos[1])) < get_distance(ant, (attract_pos[0],attract_pos[1])):
            possible_moves.append(move)
        else:
            pass
    return possible_moves



while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for ant in ants:
        # If in proximity of 50 pixels, attract towards ball
        for ball in balls:
            if get_distance(ant, ball) < 50 and get_distance(ant, ball) > 0:
                attracting_moves = legit_moves(ant, ball)
                move_ant_to(ant, random.choice(attracting_moves))

        else:
            # Choose random direction and move
            dic = {"left": (-1,0), "right": (1,0), "up": (0,-1), "down": (0,1)}
            moves = ["left", "up", "down", "right"]
            random_pick = random.choice(moves)
            move_ant_to(ant, dic[random_pick])
         

    # Can't remove from iterating list so we make a copy using ants[:]
    for ant in ants[:]:
        # If ant is at same coordinate as ball, remove ant from screen
        for ball in balls:
            if ant == ball:
                ants.remove(ant)

    # Draw ants
    for ant in ants:
        pygame.draw.circle(screen, [0,255,0], ant, 0)

    pygame.display.flip()
    # Clear the screen and set the screen background
    screen.fill(black)

    clock.tick()
 
# Can't use X on window withou this command
pygame.quit()