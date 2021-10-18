
## Assignment 4: Reproducing rabbits and overpopulation

In the previous assignment we have studied at what rate the number of rabbit decreases when two foxes are prowling in the forest. Eventually, all rabbits will be eaten. In real life this process is slightly different, as the number of rabbits will also increase through reproduction. In this assignment we will take a look at the effects of reproduction and a limited supply of food on the population of the rabbits and foxes. Both of these aspects will be added to our simulation.

As with the previous assignments, we are going to make adjustments to the code we have written previously. Create a file called `predator_prey_4.py`, copy all code written so far into it and continue working with the new file.

The question we'll be answering this assignment is the following one: 'How often do the rabbits survive and how often do the foxes eat most of the rabbits?'

{: .language-python}   
     A simulated world with: N_rabbits=25 (v=1), N_fox=2 (v=2), N_simulations = 500:
     In XX.X percent of the cases the rabbits win

We'll answer this question incrementally. We will be adding two functions, `reproducing_rabbits()` and `overpopulation()`, that describe these phenomena and call them from within `predator_prey()`.

#### Part 4a: reproducing rabbits

The first aspect that we will implement is the rabbits' ability to reproduce. Declare a new function called `reproducing_rabbits()` that is called after the currently existing functions (moving rabbits, moving foxes and eating rabbits by the foxes) in `predator_prey()`. This function will verify whether there are any rabbits close together, and if that's the case the program should generate new baby rabbits at a random position in the forest.

Apply the following strategy:

  1. Don't call the function until 200 seconds have passed. The rabbits start relatively close to each other and start out too young to reproduce. This is an adjustment of the `predator_prey()` function that determines what functions are called and when.

  2. First determine how many pairs of rabbits are close together (distance < 1). This determines the number of nests. Avoid double counting a rabbit. Only assign a rabbit to 1 nest each.

  3. For each nest, generate 4 new rabbits, give them random positions in the forest, a random direction and add them to the list of rabbits.

If you monitor this program for a couple of simulations you'll see how incredibly unstable this system is. If the foxes do not eat enough rabbits by the time they start reproducing, the number of rabbits starts growing exponentially. This will slow down your program significantly, and eventually crash it. For the following assignment we'll be mending this undesired and unrealistic effect.

#### [Part 4b]: maximum number of rabbits in the forest

The second functionality that we'll add will be limiting the number of rabbits that can live simultaneously in the forest. There is only enough food available in the forest for 50 rabbits to survive. Declare a new function `overpopulation()` that is called after `reproducing_rabbits()`. The goal of this function is to make sure there are never more than 50 rabbits living in the forest. Verify the length of the list of rabbits and remove any excess elements. Beware to remove the rabbits from each of the corresponding lists: x-position, y-position, and angle.

After 1000 seconds you'll (usually) find a stable state. Either the rabbits will have won (rabbits are near their maximum number of 50), or the foxes have won (almost all rabbits have been eaten). The graphs below show the number of rabbits as function of the time for two individual simulations, one where the foxes won (left) and one where the rabbits won (right).

 ![](DynamicaWinstVossen.png){: style="width:40%"}
 ![](DynamicaWinstKonijnen.png){: style="width:40%"}

Create this type of graph for a single simulation in a new function `success_chance_rabbits()`. This way we can verify whether the new `overpopulation()` function is programmed correctly. The function should run a single simulation by calling the `predator_prey()` function, and then create the graph.

<b>Hint:</b> The function that we have to define here is a lot like the function `average_half_life()` that we used in assignment 3c. The function `predator_prey()` already `return`s the number of rabbits for every step in time. Use that information as the foundation of your plot.

Aside from drawing the plot it's also important to draw conclusions on whether the rabbits or the foxes have won. If at time step 1000 the number of rabbits is greater than 45 the rabbits have won, if their numbers are fewer than 5 the foxes have won. Every other amount of rabbits results in a tie between rabbits and foxes.

At the end of the simulation the program should `print` to the screen who has won.

{: .language-python}   
     The number of rabbits after t=1000 steps was XXX.
     This means that the XXX have won.


#### The assignment: chance of success for the rabbits

We're now able to answer the original question of this assignment: what is the chance the rabbits will win? More concrete: in what percentage of the simulations is the number of rabbits in the forest after 1000 time steps (seconds) greater than 45? Edit the `success_chance_rabbits()` from assignment 4b in such a way that it now runs 200 simulations and keep track for each of the simulations whether the rabbits won (more than 45 rabbits), or the foxes have won (fewer than 5 rabbits) or that there was a tie (all other cases).

<b>Note:</b> You no longer need to show the graph that you've created for assignment 4b for each of the simulations. Make sure it is only plotted if the function `success_chance_rabbits()` only runs 1 simulation.

Calculate the fraction after all of the simulations have run and `print` the success chances of the rabbits to the screen like so:

{: .language-python}
     A simulated world with: N_rabbits=25 (v=1), N_fox=2 (v=2), N_simulations = 200:
     In XX.X percent of the cases the rabbits win

### Conclusion

In this assignment we have simulated population dynamics by using the computational strength of a computer. We have included some elementary aspects and studied how the development of rabbits is dependent on the free parameters of our system. The 'real' simulations that scientists do, work in much the same way. Whether it be population dynamics, traffic flow under new circumstances or the movements of people during an emergency situation in a stadium. Our simulation can easily be expanded if you feel like doing so. What are the first elements you'd add? Foxes moving slower, the longer they haven't had any food, reproducing foxes, foxes that can smell rabbits when they're near, rabbits that can hide in specific parts of the forest etc etc. The possibilities are endless. Our time to implement them unfortunately isn't.
