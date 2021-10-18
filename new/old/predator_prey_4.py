import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, pi, sqrt

import random


def average_half_life():
    avg_list = []
    for i in range(500):
        if not i % 25:
            print(i)
        avg_list.append(calculate_half_life())

    print(f'A simulated world with: N_rabbits=25 (v=1), N_fox=2 (v=2), N_simulations = 500:\n Average half-life of rabbits = {np.mean(avg_list)} seconds')


def calculate_half_life():
    nr_rabbits = predator_prey(show_vis=False)

    for i, nr in enumerate(nr_rabbits):
        if nr < 13:
            return i

    return i


def predator_prey(seconds=1000, show_vis=True):
    # define the starting position of rabbits (x-position and y-position at t=0)
    rabbit_speed = 0.5

    rabbits_position_x, rabbits_position_y, rabbits_angle = generate_rabbits(25)

    foxes_position_x = [70, 80]
    foxes_position_y = [70, 80]
    foxes_angle = [pi, 0]
    fox_speed = 2

    nr_rabbits = []

    # take steps in time t
    for t in range(seconds):

        # move the rabbits
        rabbits_position_x, rabbits_position_y, rabbits_angle = move_rabbits(rabbits_position_x, rabbits_position_y, rabbits_angle, rabbit_speed)

        # move the foxes
        foxes_position_x, foxes_position_y, foxes_angle = move_foxes(foxes_position_x, foxes_position_y, foxes_angle, fox_speed)

        rabbits_position_x, rabbits_position_y, rabbits_angle = dinnertime(rabbits_position_x, rabbits_position_y, foxes_position_x, foxes_position_y, rabbits_angle)

        if t > 200:
            rabbits_position_x, rabbits_position_y, rabbits_angle = reproduction(rabbits_position_x, rabbits_position_y, rabbits_angle)

            rabbits_position_x, rabbits_position_y, rabbits_angle = overpopulation(rabbits_position_x, rabbits_position_y, rabbits_angle)

        # plot the position of the rabbits
        if show_vis:
            draw_forest(rabbits_position_x, rabbits_position_y, foxes_position_x, foxes_position_y)

        nr_rabbits.append(len(rabbits_position_x))

    return nr_rabbits

### GEVEN?
def overpopulation(rabbits_position_x, rabbits_position_y, rabbits_angle):
    return rabbits_position_x[:50], rabbits_position_y[:50], rabbits_angle[:50]

### DEZE IS BEHOORLIJK INGEWIKKELD
def reproduction(rabbits_position_x, rabbits_position_y, rabbits_angle):
    nr_rabbits = len(rabbits_position_x)

    taken = []

    for rabbit1 in range(nr_rabbits):
        for rabbit2 in range(rabbit1 + 1, nr_rabbits):
            distance = calc_dist(rabbits_position_x[rabbit1], rabbits_position_y[rabbit1], rabbits_position_x[rabbit2], rabbits_position_y[rabbit2])

            if distance <= 1 and rabbit2 not in taken and rabbit1 not in taken:
                taken.append(rabbit2)
                break

    child_x, child_y, child_angle = generate_rabbits(len(taken) * 4, 0, 100)

    return rabbits_position_x + child_x, rabbits_position_y + child_y, rabbits_angle + child_angle


def generate_rabbits(nr_rabbits, pos_min=20, pos_max=20):
    rabbits_position_x = []
    rabbits_position_y = []
    rabbits_angle = []

    for _ in range(nr_rabbits):
        rabbits_position_x.append(random.uniform(pos_min, pos_max))
        rabbits_position_y.append(random.uniform(pos_min, pos_max))
        rabbits_angle.append(random.uniform(0, 2 * pi))

    return rabbits_position_x, rabbits_position_y, rabbits_angle


def calc_dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dinnertime(rabbits_position_x, rabbits_position_y, foxes_position_x, foxes_position_y, rabbits_angle):
    rabbits_count = len(rabbits_position_x)
    foxes_count = len(foxes_position_x)

    new_rabbits_position_x = []
    new_rabbits_position_y = []
    new_rabbits_angle = []

    for rabbit_nr in range(rabbits_count):
        eaten = False

        for fox_nr in range(foxes_count):
            distance = calc_dist(rabbits_position_x[rabbit_nr], rabbits_position_y[rabbit_nr], foxes_position_x[fox_nr], foxes_position_y[fox_nr])

            if distance < 5:
                eaten = True

        if not eaten:
            new_rabbits_position_x.append(rabbits_position_x[rabbit_nr])
            new_rabbits_position_y.append(rabbits_position_y[rabbit_nr])
            new_rabbits_angle.append(rabbits_angle[rabbit_nr])

    return new_rabbits_position_x, new_rabbits_position_y, new_rabbits_angle


def move_foxes(foxes_position_x, foxes_position_y, foxes_angle, fox_speed):
    foxes_count = len(foxes_position_x)

    for fox_nr in range(foxes_count):
        change_x = cos(foxes_angle[fox_nr]) * fox_speed
        change_y = sin(foxes_angle[fox_nr]) * fox_speed

        foxes_position_x[fox_nr] += change_x
        foxes_position_y[fox_nr] += change_y

        if not(0 <= foxes_position_x[fox_nr] <= 100):
            foxes_position_x[fox_nr] -= change_x

            foxes_angle[fox_nr] += pi

        if not(0 <= foxes_position_y[fox_nr] <= 100):
            foxes_position_y[fox_nr] -= change_y

            foxes_angle[fox_nr] += pi

        foxes_angle[fox_nr] = np.random.normal(foxes_angle[fox_nr], 0.2)

    return foxes_position_x, foxes_position_y, foxes_angle


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


def draw_forest(rabbits_position_x, rabbits_position_y, foxes_position_x, foxes_position_y):
    # define the axes of the forest
    plt.axis([0, 100, 0, 100])

    # draw the rabbits as a blue dot
    plt.plot(rabbits_position_x, rabbits_position_y, 'o', color='blue', markersize=6)

    # draw the foxes as a red dot
    plt.plot(foxes_position_x, foxes_position_y, 'o', color='red')

    # update the frames for a simple animation
    plt.draw()
    plt.pause(0.1)
    plt.clf()


def success_chance_rabbits(simulations=200):
    if simulations == 1:
        numbers = predator_prey(show_vis=False)

        plt.ylim([0, 60])
        plt.plot(numbers)
        plt.ylabel('Number of rabbits')
        plt.xlabel('Time (seconds)')
        plt.axhline(24.9, linestyle='dashed', color='r')
        plt.show()

        print(f'The number of rabbits after t=1000 steps was {numbers[-1]}')
        if numbers[-1] < 5:
            print(f'This means that the foxes have won')
        else:
            print(f'This means that the rabbits have won')
    else:
        total = 0
        for i in range(simulations):
            if i % 25 == 0:
                print(i)
            numbers = predator_prey(show_vis=False)
            if numbers[-1] >= 5:
                total += 1
        print(f'A simulated world with: N_rabbits=25 (v=1), N_fox=2 (v=2), N_simulations = {simulations}:')
        print(f'In {(total / simulations) * 100} percent of the cases the rabbits win')


# run the simulation
# predator_prey(show_vis=False)

success_chance_rabbits()

# print(f'After {calculate_half_life()} seconds more than half the rabbits have been eaten')
#
# average_half_life()
