'''
Ant colony simulator or BLACK holes and stars
'''
import pygame, random, math
from collections import deque

class Ant():

    moves = {"left": (-1,0), "right": (1,0), "up": (0,-1), "down": (0,1), "upleft": (-1,-1), "downleft": (-1,1), "upright": (1,-1), "bottomright": (1,1)}
    move_stack = 0

    def __init__(self):
        self.pos = [random.randrange(0,400),random.randrange(0,400)]


    def move_ant(self, new_position):
        self.pos[0] = new_position[0]
        self.pos[1] = new_position[1]

    def add_xys(self, xy):
        self.pos[0] += xy[0]
        self.pos[1] += xy[1]

    def get_closer(self, move, new_position):
        current_delta = get_distance(self.pos, new_position)
        self.add_xys(move)
        delta = get_distance(self.pos, new_position)
        return delta < current_delta



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

def get_angle(origin, destination):
    """Returns angle in radians from origin to destination.
    This is the angle that you would get if the points were
    on a cartesian grid. Arguments of (0,0), (1, -1)
    return .25pi(45 deg) rather than 1.75pi(315 deg).
    """
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return math.atan2(-y_dist, x_dist) % (2 * math.pi)

def project(pos, angle, distance):
    """Returns tuple of pos projected distance at angle
    adjusted for pygame's y-axis.
    """
    return (pos[0] + (math.cos(angle) * distance),
            pos[1] - (math.sin(angle) * distance))

def main(): 
    # Initialize the game engine
    pygame.init()
     
    # Define the colors we will use in RGB format
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    # Set the height and width of the SCREEN
    SIZE = [400, 400]
    SCREEN = pygame.display.set_mode(SIZE)
     
    pygame.display.set_caption("Ants Sim")
    clock = pygame.time.Clock() 

    # Create list of ants
    ants = []   
    for i in range(1000):
        ants.append(Ant())
        
    # Create list of balls (attracting balls)
    balls = deque([],3)
    
    # Loop until the user clicks the close button.
    done = False
    while not done: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Stack - keep no more than 3 balls on screen and get rid of oldest one in "deque"  
                balls.append(pos)

        # Grab mouse coordinates every cycle
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        


        for ant in ants:
            # If in proximity of 50 pixels, attract towards ball
            if len (balls) > 0:
                angle = get_angle(ant.pos, balls[ant.move_stack])
                distance = get_distance(ant.pos, balls[ant.move_stack])
                movecoords = project(ant.pos, angle, 1)
                ant.move_ant(movecoords)

                if distance < 1 and len(balls) == 3:

                    ant.move_stack += 1
                    if ant.move_stack == 3:
                        ant.move_stack = 0
            
            # for ball in balls:
                
            #     if within_distance(ant.pos, ball, 50):
            #         possible_moves = []
            #         # If within range of attracting orb...
            #         for move in ant.moves.keys():
            #             if ant.get_closer(ant.moves[move], ball):
            #                 possible_moves.append(ant.moves[move])

            #         ant.add_xys(random.choice(possible_moves))

        # Draw ants
        for ant in ants:
            pygame.draw.rect(SCREEN, [0,255,0], [ant.pos[0], ant.pos[1],1,1], 1)

        for ball in balls:  
            pygame.draw.circle(SCREEN, [255,0,0], ball, 2)

        pygame.display.flip()
        # Clear the SCREEN and set the SCREEN background
        SCREEN.fill(BLACK)

        clock.tick(60)
     
    # Can't use X on window withou this command
    pygame.quit()


if __name__ == '__main__':
  main()