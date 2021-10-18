import random
import math

import matplotlib.pyplot as plt
import numpy as np


def distance(creature1, creature2):
    return math.sqrt((creature1.pos_x - creature2.pos_x) ** 2 + (creature1.pos_y - creature2.pos_y) ** 2)


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.creatures = []

    def add_creatures(self, creature_type, number, speed=1, sight=10):
        for _ in range(number):
            rand_pos_x = random.uniform(0, self.width)
            rand_pos_y = random.uniform(0, self.height)
            rand_angle = random.uniform(0, 2 * math.pi)

            creature = creature_type(rand_pos_x, rand_pos_y, rand_angle, speed, sight)

            self.creatures.append(creature)

    def step(self):
        for creature in self.creatures:
            creature.move()

        self.handle_collisions()

        for creature in self.creatures[:]:
            if not creature.alive:
                self.creatures.remove(creature)

    def handle_collisions(self):
        for creature1 in self.creatures:
            for creature2 in self.creatures:
                creature1.interacts_with(creature2)

    def draw(self):
        plt.axis([0, self.width, 0, self.height])

        location_x = []
        location_y = []
        colors = []

        # TODO Deze naar creature zelf
        for creature in self.creatures:
            location_x.append(creature.pos_x)
            location_y.append(creature.pos_y)
            colors.append(creature.color)

        plt.scatter(location_x, location_y, c=colors)

        plt.draw()
        plt.pause(0.1)
        plt.clf()

    def simulate(self, iterations):
        for i in range(iterations):
            self.step()

            self.draw()


class Creature:
    def __init__(self, pos_x, pos_y, angle, speed=1, sight=10):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle
        self.speed = speed
        self.sight = sight

        self.alive = True

    def move(self):
        change_x = math.cos(self.angle) * self.speed
        change_y = math.sin(self.angle) * self.speed

        self.pos_x += change_x
        self.pos_y += change_y

        if not (0 <= self.pos_x <= 100):
            self.pos_x -= change_x

            self.angle += math.pi

        if not (0 <= self.pos_y <= 100):
            self.pos_y -= change_y

            self.angle += math.pi

    def sees(self, creature):
        if distance(self, creature) < self.sight and self is not creature:
            return True
        return False

    def draw(self, ax):
        pass

class Rabbit(Creature):
    color = 'blue'
    predator = False

    def move(self):
        if random.random() < 0.05:
            self.angle = random.uniform(0, 2 * math.pi)
        else:
            super().move()

    def interacts_with(self, creature):
        if self.sees(creature) and creature.predator:
            self.angle = math.atan2(self.pos_y - creature.pos_y, self.pos_x - creature.pos_x)


class Fox(Creature):
    color = 'red'
    predator = True

    def move(self):
        super().move()

        self.hungry = True
        self.angle = np.random.normal(self.angle, 0.2)

    def interacts_with(self, creature):
        if self.sees(creature) and not creature.predator and self.hungry:
            creature.alive = False
            self.hungry = False


if __name__ == '__main__':
    simulation_field = Field(100, 100)

    simulation_field.add_creatures(Rabbit, 10)
    simulation_field.add_creatures(Fox, 2, 2, 5)

    simulation_field.simulate(100)
