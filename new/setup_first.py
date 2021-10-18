import random
import math
import matplotlib.pyplot as plt


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.creatures = []

    def add_creatures(self, Creature_type, number, speed=1):
        for _ in range(number):
            rand_pos_x = random.uniform(0, self.width)
            rand_pos_y = random.uniform(0, self.height)
            rand_angle = random.uniform(0, 2 * math.pi)

            creature = Creature_type(rand_pos_x, rand_pos_y, rand_angle, speed)

            self.creatures.append(creature)

    def step(self):
        for creature in self.creatures:
            creature.move()

    def simulate(self, iterations):
        for i in range(iterations):
            self.step()

            self.draw()

    def draw(self):
        plt.axis([0, self.width, 0, self.height])

        location_x = []
        location_y = []
        colors = []

        for creature in self.creatures:
            location_x.append(creature.pos_x)
            location_y.append(creature.pos_y)
            colors.append(creature.color)

        plt.scatter(location_x, location_y, c=colors)

        plt.draw()
        plt.pause(0.1)
        plt.clf()


class Walker:
    def __init__(self, pos_x, pos_y, angle, speed=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle
        self.speed = speed

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


class Rabbit(Walker):
    def __init__(self, *args):
        super().__init__(*args)

        self.color = 'blue'

    def move(self):
        if random.random() < 0.05:
            self.angle = random.uniform(0, 2 * math.pi)
        else:
            super().move()


if __name__ == '__main__':
    simulation_field = Field(100, 100)

    simulation_field.add_creatures(Rabbit, 25, 1)

    simulation_field.simulate(100)
