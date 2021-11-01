import random
import math

import matplotlib.pyplot as plt


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.creatures = []

        # Create the matplotlib figure with space for two graphs horizontally
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)

        # Make sure that the x and y axis in the plot have the same scale
        self.ax1.set_aspect('equal')

    def add_creatures(self):
        pass

    def draw(self):
        # Set the leftmost plot to correct width
        self.ax1.axis([0, self.width, 0, self.height])

        # CHANGE THIS LINE
        self.ax1.plot(50, 50, 'o', color='blue')

        # Draw both plots to the screen with a slight pause of 0.01 seconds
        plt.draw()
        plt.pause(5)

        # Empty the plots so that we can draw again next cycle
        self.ax1.cla()
        self.ax2.cla()

    def step(self):
        pass

    def simulate(self, iterations):
        pass
