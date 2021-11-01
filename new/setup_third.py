import random
import math

import matplotlib.pyplot as plt
import numpy as np


def distance(creature1, creature2):
    return math.sqrt((creature1.pos_x - creature2.pos_x) ** 2 + (creature1.pos_y - creature2.pos_y) ** 2)


class Field:
    def __init__(self, width, height, animate=True, max_population=160):
        self.width = width
        self.height = height
        self.animate = animate
        self.max_population = max_population

        self.creatures = []

        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)
        self.ax1.set_aspect('equal')

        self.rabbit_history = []
        self.fox_history = []

    def add_creatures(self, Creature_type, number, speed=1, sight=10):
        for _ in range(number):
            rand_pos_x = random.uniform(0, self.width)
            rand_pos_y = random.uniform(0, self.height)
            rand_angle = random.uniform(0, 2 * math.pi)

            creature = Creature_type(rand_pos_x, rand_pos_y, rand_angle, speed, sight)

            self.creatures.append(creature)

    def step(self):
        for creature in self.creatures:
            creature.move()

        self.handle_collisions()

        self.resolve_deaths()

        self.resolve_births()

        self.resolve_overpopulation()

        while self.count_creature(Rabbit) < 5:
            self.add_creatures(Rabbit, 1, 1, 10)

        while self.count_creature(Fox) < 2:
            self.add_creatures(Fox, 1, 3, 10)

    def count_creature(self, Creature_type):
        count = 0
        for creature in self.creatures:
            if type(creature) is Creature_type:
                count += 1

        return count

    def resolve_overpopulation(self):
        while self.count_creature(Rabbit) > self.max_population:
            i = random.randint(0, len(self.creatures) - 1)
            if type(self.creatures[i]) is Rabbit:
                self.creatures.pop()

    def resolve_deaths(self):
        for creature in self.creatures[:]:
            if not creature.alive:
                self.creatures.remove(creature)

    def resolve_births(self):
        count_births = {}

        for creature in self.creatures:
            if creature.pregnant:
                key = (type(creature), creature.speed, creature.sight)
                if key in count_births:
                    count_births[key] += 1
                else:
                    count_births[key] = 1

        for key in count_births:
            Creature_type, speed, sight = key
            self.add_creatures(Creature_type, count_births[key], speed, sight)

    def handle_collisions(self):
        for creature1 in self.creatures:
            for creature2 in self.creatures:
                if creature1.sees(creature2) and creature1 is not creature2:
                    creature1.interacts_with(creature2)
                    break

    def draw(self):
        self.ax1.axis([0, self.width, 0, self.height])

        for creature in self.creatures:
            creature.draw(self.ax1)

        rabbit_count = 0
        fox_count = 0

        for creature in self.creatures:
            if type(creature) is Rabbit:
                rabbit_count += 1
            else:
                fox_count += 1

        self.rabbit_history.append(rabbit_count)
        self.fox_history.append(fox_count)

        self.ax2.plot(range(self.iteration + 1), self.rabbit_history, '-b')
        self.ax2.plot(range(self.iteration + 1), self.fox_history, '-r')

        plt.draw()
        plt.pause(0.01)

        self.ax1.cla()
        self.ax2.cla()

    def simulate(self, iterations):
        for self.iteration in range(iterations):
            self.step()

            if self.animate:
                self.draw()


class Creature:
    def __init__(self, pos_x, pos_y, angle, speed=1, sight=10):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle
        self.speed = speed
        self.sight = sight

        self.alive = True
        self.pregnant = False
        self.color = "black"

    def move(self):
        self.pregnant = False

        change_x = math.cos(self.angle) * self.speed
        change_y = math.sin(self.angle) * self.speed

        self.pos_x += change_x
        self.pos_y += change_y

        if not (0 <= self.pos_x + change_x <= 100):
            self.pos_x -= change_x

            self.angle += math.pi

        if not (0 <= self.pos_y <= 100):
            self.pos_y -= change_y

            self.angle += math.pi

    def draw(self, ax):
        ax.plot(self.pos_x, self.pos_y, 'o', c=self.color)

    def sees(self, creature):
        if self is not creature and distance(self, creature) < self.sight:
            return True
        return False


class Rabbit(Creature):
    def __init__(self, *args):
        super().__init__(*args)

        self.color = 'blue'
        self.predator = False

    def move(self):
        if random.random() < 0.05:
            self.angle = random.uniform(0, 2 * math.pi)
        else:
            super().move()

    def interacts_with(self, creature):
        # if creature.predator:
        #     self.angle = math.atan2(self.pos_y - creature.pos_y, self.pos_x - creature.pos_x)
        if type(creature) is type(self) and random.random() < 0.1:
            self.pregnant = True


class Fox(Creature):
    def __init__(self, *args):
        super().__init__(*args)

        self.color = 'red'
        self.predator = True
        self.hungry = True
        self.last_eaten = 0

    def move(self):
        super().move()

        self.last_eaten += 1
        self.angle = np.random.normal(self.angle, 0.2)

        if self.last_eaten > 25:
            self.alive = False

    def interacts_with(self, creature):
        if not creature.predator and creature.alive:
            creature.alive = False

            if random.random() < 0.15:
                self.pregnant = True

            self.hungry = False
            self.last_eaten = 0


if __name__ == '__main__':
    simulation_field = Field(100, 100)

    simulation_field.add_creatures(Rabbit, 25, 1, 10)
    simulation_field.add_creatures(Fox, 3, 3, 10)

    simulation_field.simulate(1000)
