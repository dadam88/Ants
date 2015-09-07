'''
Ant colony simulator or black holes and stars
'''
import pygame, random, math


def main(): 
    # Initialize the game engine
    pygame.init()
     
    # Define the colors we will use in RGB format
    black = (0, 0, 0)
    white = (255,255,255)
    # Set the height and width of the screen
    size = [400, 400]
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Ants Sim")
    clock = pygame.time.Clock() 

    # Create list of ants
    ants = []   
    for i in range(1000):
        ants.append([random.randrange(0,400), random.randrange(0, 400   )])

    # Create list of balls (attracting balls)
    balls = []
    
    def move_ant_to(ant, pos):
        '''(x,y), (x,y) -> None

        Modifies ant position by adding pos to it.
        '''
        ant[0] += pos[0]
        ant[1] += pos[1]

    def get_distance(origin, destination):
        '''(x,y), (x,y) -> returns float
        Calculates distance from (x,y) to (x,y)
        '''
        x = origin[0] - destination[0]
        y = origin[1] - destination[1]
        return math.sqrt(x*x + y*y)


    def legit_moves(ant, attract_pos):
        '''
        (x,y), (x,y) -> list of possible moves

        Generates a list of possible moves that takes the intial x,y closer to the second x,y
        '''
        movelist = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        possible_moves = list()
        for move in movelist:

            if get_distance((move[0] + ant[0], move[1] + ant[1]),(attract_pos[0], attract_pos[1])) < get_distance(ant, (attract_pos[0],attract_pos[1])):
                possible_moves.append(move)
            else:
                pass

        return possible_moves

    queue = 0
    # Loop until the user clicks the close button.
    done = False
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(balls) < 3:
                    balls.append(pos)
                else:
                    # Queue which only puts 3 balls on screen at once
                    balls.remove(balls[queue])
                    balls.insert(queue, pos)
                    queue += 1
                    if queue == 3:
                        queue = 0

        # Grab mouse coordinates every cycle
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]


        for ant in ants:
            # If in proximity of 50 pixels, attract towards ball
            for ball in balls:
                
                if get_distance(ant, ball) < 50 and get_distance(ant, ball) >= 0:
                    attracting_moves = legit_moves(ant, ball)

                    # If there is moves left to attract to ball...
                    if attracting_moves:
                        move_ant_to(ant, random.choice(attracting_moves))


                else:
                    # Choose random direction and move
                    dic = {"left": (-1,0), "right": (1,0), "up": (0,-1), "down": (0,1), "upleft": (-1,-1), "downleft": (-1,1), "upright": (1,-1), "bottomright": (1,1)}
                    moves = ["left", "up", "down", "right"]
                    random_pick = random.choice(moves)
                    move_ant_to(ant, dic[random_pick])
        '''
        # Set kill = True to remove ants from game when sucked into balls
        # Can't remove from iterating list so we make a copy using ants[:]
        kill = False
        if kill:
            for ant in ants[:]:
                # If ant is at same coordinate as ball, remove ant from screen
                for ball in balls:

                    if ant[0] == ball[0] and ant[1] == ball[1]:
                        ants.remove(ant)
        '''
        # Draw ants
        for ant in ants:
            pygame.draw.rect(screen, [0,255,0], [ant[0], ant[1],1,1], 1)

        for ball in balls:
            pygame.draw.circle(screen, [255,0,0], ball, 2)

        pygame.display.flip()
        # Clear the screen and set the screen background
        screen.fill(black)

        clock.tick()
     
    # Can't use X on window withou this command
    pygame.quit()


if __name__ == '__main__':
  main()