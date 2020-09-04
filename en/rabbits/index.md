# Population dynamics: predator-prey model

A classical example of a complex dynamical system is the so-called predator-prey model. The basis of the mathematical description of the populations are the famous [Lotka-Volterra equations](https://en.wikipedia.org/wiki/Lotka–Volterra_equations). The math quickly become very complex and it's not always as easy to predict what the effects of a change of behavior are on the different populations in a system.

In this module we'll create a simulation ourselves of a well-organized system: a forest of 100 by 100 meters inhabited by 25 rabbits and 2 foxes. By programming it ourselves, we can add new phenomena. Visualizing the system gives us direct feedback on our code and shows us the consequences of the new behavioral elements that we add. The goal of this module is to add complexity to the behavior of rabbits and foxes in our simulation and to ultimately find out whether the foxes or the rabbits will emerge victorious when released in our isolated neck of the woods.

## Start: two moving rabbits on your screen

> Note: animations cannot be created in the online Python IDE! You'll need a local installation on your own computer. Don't hesitate to send us an email if you need any assistance.

We start out this module, against the philosophy of this course, not with an empty screen, but with the following bit of code. Not because it is terribly difficult, but because we then have a common start and can all add pieces of code in the same manner.

{: .language-python}
    import matplotlib.pyplot as plt


    def predator_prey():
        # define the starting position of rabbits (x-position and y-position at t=0)
        rabbits_position_x = [10., 60.]
        rabbits_position_y = [2., 10.]

        # take steps in time t
        for t in range(10):

            # move the rabbits
            rabbits_position_x, rabbits_position_y = move_rabbits(rabbits_position_x, rabbits_position_y)

            # plot the position of the rabbits
            draw_forest(rabbits_position_x, rabbits_position_y)

        return


    def move_rabbits(rabbits_position_x, rabbits_position_y):
        # move the rabbits (0.6 to the right and 0.8 upwards)
        rabbits_count = len(rabbits_position_x)
        for rabbit_nr in range(rabbits_count):
            rabbits_position_x[rabbit_nr] = rabbits_position_x[rabbit_nr] + 0.6
            rabbits_position_y[rabbit_nr] = rabbits_position_y[rabbit_nr] + 0.8

        return rabbits_position_x, rabbits_position_y


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



The piece of code above consists of 3 functions:

   1. `predator_prey()`: defines the starting position of the rabbits, controls the simulation by taking steps in time (a second each) and calls for each step in the functions `move_rabbits()` and `draw_forest()`. Is called as the 'main program' at the bottom of the code.

   2. `move_rabbits()`: changes the position of the rabbits and returns the result

   3. `draw_forest()`:  displays the rabbits to the screen

 In our piece of code there are two lists that we'd like to use in multiple functions: `rabbits_position_x` and `rabbits_position_y`. These lists are used in each of the three functions: the starting positions are defined in `predator_prey()`, they're changed and then returned in the `move_rabbits()` function and are used to display the rabbits locations in `draw_forest()`. We pass the lists as arguments to the functions, and return them when we have changed their contents. You might notice that the return in `move_rabbits()` has two values separated by a comma, and that the variables are stored in much the same way. Returning and assigning multiple variables this way in Python is called _tuple unpacking_.


## Assignment 1: modelling the movement of rabbits

In the example above we assumed that rabbits move 0.6 meters to the right and 0.8 meters upwards at every time interval (of a second). This is a far cry from a realistic system of course: rabbits do not move synchronously, they do not run in a straight line and if we we're to run the system for long enough they would happily run out of our simulated forest. That is not the intention of this assignment. The rabbits each move their own way and if rabbits near the edge of the forest they'll quickly return to the relative safety of the forest. In this first assignment we'll introduce the code necessary to approach realistic rabbit behavior. Create a file called `predator_prey_1.py` and copy the above code into that file. Then follow the next part of the assignment.

#### Part (1a): new parametrization of the movement of rabbits

In the function `move_rabbits()` we now have the rabbits move to the right and up. We could also have implemented the movement of rabbits in a different way. For example by saying that rabbits all move with the same speed (1 meter per second) and that they, specifically for this example, also move with the same angle.

Add to the main program a variable called `rabbit_speed` that contains the universal speed for all rabbits. Also add a list called `rabbits_angle` that holds the angle (in radians) of each rabbit relative to the x-axis, with which they move in a specific direction. You will use the new variables in two functions, specifically `predator_prey()` (choosing the initial values) and `move_rabbits()` (calculating new positions). Make sure that you pass the variables to the function `move_rabbits()`. Add `rabbits_angle` to the return value of the function as well, as we will need this later.

> It is fairly easy to convert from degrees to radians: $$ radians = \frac{\pi * degrees}{180} $$. 90 degrees is the same as $$\frac{1}{2}\pi$$

In `move_rabbits()` where you calculate the new positions of the rabbits, you'll have to first convert the speed and angle into speed along the x- and y-axis, so you can calculate the new values of its x- and y-coordinate. After all, their positions are stored as x and y values. For each rabbit we first calculate:

{: .language-python}
       angle = rabbits_angles[rabbit]
       velocity_x = rabbit_speed * cos(angle)
       velocity_y = rabbit_speed * sin(angle)

Because our time steps are exactly 1 second we can then calculate the new positions as follows:

{: .language-python}
       rabbits_position_x[rabbit] = rabbits_position_x[rabbit] + velocity_x
       rabbits_position_y[rabbit] = rabbits_position_y[rabbit] + velocity_y

The code above actually read `velocity_x * dt`, but since the change in time (`dt`) is 1 second we can leave out that multiplication. This implementation allows us to give each rabbit a unique direction at the start of a simulation. Apply the above changes to your program, give each of the rabbits their own direction and run the simulation for 20 seconds instead of 10.

<b>Note:</b> to be able to use trigonometric functions in your code like this you first have to import the math library from Python: `from math import cos, sin, pi`

#### Part (1b): the edge of the forest

Our rabbits, cowards that they are, will never leave the forest. As soon as they accidentally set foot outside the forest they turn around and make their way back where they came from into the forest. Adjust the function `move_rabbits()` in such a way that the rabbits will always remain inside the forest.

Utilize the following strategy when the rabbit has moved outside of the forest after a movement:

   1. take one step back (both x and y) so the rabbit is in its original position
   2. turn the rabbit around by changing the angle with which the rabbits moves into an angle exactly opposite the one they were taking: 'angle_new = angle + $$\pi$$'. Replace their direction with the new one in `rabbits_angle` so that the rabbit runs back through the forest at the following time step.

Try this by moving one rabbit straight for the edge of the forest and see if they indeed properly 'bounce' back into the forest as soon as they pass the boundary.


#### Part (1c): random rabbit behavior

Everyone who owns a rabbit has seen them move and knows they do not move in a straight line, but instead freeze in place every now and then to then change direction. This is a characteristic we'll be implementing as well in our simulation.

![](konijnen.gif){:.inline}{: style="width:30%"}

Edit the function `move_rabbits()` such that the rabbits will freeze in place on average once per 20 seconds and then continue moving in a random new direction. Practically this means that a rabbit has a 5% chance for each second to sit still and change direction and has a 95% chance to just continue along the same direction. A possible implementation of this behavior is by using a random number $$x$$ (between 0 and 1). Then, this number can be used as a probability to either do a regular move, or change angles:

{: .language-python}
    x < 0.05 (5% chance): no move, but instead a new random angle (0 < angle < 2*$$\pi$$)
    x > 0.05 (95% chance): regular move

<b>Note:</b> to generate a random number you need the random library. Make sure it's included in your code `import random`

#### Part (1d): simulation with 25 rabbits

A world with only two rabbits is not very realistic. Edit the start of `predator_prey()` such that it includes 25 rabbits in the simulation. Make sure your code generates a random position inside of the square described by $$20 < (x,y) > 30$$ for each of the rabbits. Also assign each of the rabbits a random starting direction: $$0 < $$angle$$ > 2\pi$$.
