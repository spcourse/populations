from field import Field
from walker import Walker

simulation_field = Field(100, 100)

creature = Walker(15, 10, 1, 0)

simulation_field.creatures.append(creature)

simulation_field.draw()
