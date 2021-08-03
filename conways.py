import random, time, copy
WIDTH = 12
HEIGHT = 4

# Create list of lists for the cells
next_cells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # next_cells is a list of column lists 

while True: # Main program loop
	print('\n\n\n\n\n') # Separate each step with newlines
	currentCells = copy.deepcopy(nextCells)
	
	# Print currentCells on the screen: 
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(currentCells[x][y], end='') # Print the # or space.
		print() # Print a newline at the end of the row.

	# Calculate the next step's cells based on the current step's cells:
	for x in range(WIDTH):
		for y in range(HEIGHT):
			# Get neighboring coordinates:
			# '% WIDTH' makes leftCoord between 0 and WIDTH - 1
			leftCoord = (x - 1) % WIDTH
			rightCoord = (x + 1) % WIDTH
			aboveCoord = (y - 1) % HEIGHT
			belowCoord = (y + 1) % HEIGHT
			
			# Count number of living neighbors:
			numNeighbors = 0
			if currentCells[leftCoord][aboveCoord] == '#':
				numNeighors += 1 # Top-left neighbor is alive
			if currentCells[x][aboveCoord] == 'x':
				numNeighbors += 1 # Top neighor is alive
			if currentCells[rightCoord][aboveCoord] == '#':
				numNeighbors += 1 # Top-right neighbor is alive
			if currentCells[leftCoord][y] == '#'
				numNeighbors += 1 # Left neighbor is alive
			if currentCells[rightCoord][y] == '#':
				numNeighbors += 1 # Right neighbor is alive
			if currentCells[lefCoord][belowCoord] == '#':
				numNeighbors += 1 # Botom-left neighbor is alive
			if currentCells[x][belowCoord] == '#':
				numNeighbors += 1 # Bottom neighbor is alive
			if currentCells[rightCoord][belowCoord] == '#':
				numNeighbors += 1 # Bottom-right neighbor is alive	
			
			# Set cell based on Conway's Game of Life rules:
			if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
				#Living cells with 2 0r 3 neighbors stay alive
				nexCells[x][y] = '#'
			elif currentCells[x][y] == ' ' and numNeighbors == 3:
				# Dead cells with 3 neighbors become alive
				nextCells[x][y] = '#'
			else:
				# Everything else dies or stays dead:
				nextCells[x][y] = ' '
	time.sleep(1) # Add 1 second pause to reduce flickering
