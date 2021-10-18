import matplotlib.pyplot as plt
from math import cos, sin, pi
import random


def predator_prey():
    # define the starting position of rabbits (x-position and y-position at t=0)
    rabbit_speed = 1

    rabbits_position_x, rabbits_position_y, rabbits_angle = generate_rabbits(25)

    ### LOOP GEVEN MET INHOUD
    # take steps in time t
    for t in range(100):

        # move the rabbits
        rabbits_position_x, rabbits_position_y, rabbits_angle = move_rabbits(rabbits_position_x, rabbits_position_y, rabbits_angle, rabbit_speed)

        # plot the position of the rabbits
        draw_forest(rabbits_position_x, rabbits_position_y)

    return

### MISSCHIEN DEZE FUNCTIE AL GEVEN? 
def generate_rabbits(nr_rabbits):
    rabbits_position_x = []
    rabbits_position_y = []
    rabbits_angle = []

    for _ in range(nr_rabbits):
        rabbits_position_x.append(random.uniform(20, 30))
        rabbits_position_y.append(random.uniform(20, 30))
        rabbits_angle.append(random.uniform(0, 2 * pi))

    return rabbits_position_x, rabbits_position_y, rabbits_angle


def move_rabbits(rabbits_position_x, rabbits_position_y, rabbits_angle, rabbit_speed):
    rabbits_count = len(rabbits_position_x)

    for rabbit_nr in range(rabbits_count):
        if random.random() < 0.05:
            rabbits_angle[rabbit_nr] = random.random() * 2 * pi
            continue

        change_x = cos(rabbits_angle[rabbit_nr]) * rabbit_speed
        change_y = sin(rabbits_angle[rabbit_nr]) * rabbit_speed

        rabbits_position_x[rabbit_nr] += change_x
        rabbits_position_y[rabbit_nr] += change_y

        if not (0 <= rabbits_position_x[rabbit_nr] <= 100):
            rabbits_position_x[rabbit_nr] -= change_x

            rabbits_angle[rabbit_nr] += pi

        if not (0 <= rabbits_position_y[rabbit_nr] <= 100):
            rabbits_position_y[rabbit_nr] -= change_y

            rabbits_angle[rabbit_nr] += pi

    return rabbits_position_x, rabbits_position_y, rabbits_angle


def draw_forest(rabbits_position_x, rabbits_position_y):
    # define the axes of the forest
    plt.axis([0, 100, 0, 100])

    # draw the rabbits as a blue dot
    plt.plot(rabbits_position_x, rabbits_position_y, 'o', color='blue', markersize=6)

    # update the frames for a simple animation
    plt.draw()
    plt.pause(0.1)
    plt.clf()


# run the simulation
predator_prey()
