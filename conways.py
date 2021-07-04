import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create list of lists for the cells
next_cells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    next_cells.append(column) # next_cells is a list of column lists 
print(next_cells)
