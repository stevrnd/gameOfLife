"""

File    : conway.py
Date    : Friday 11 August 2023
Desc    : Recreation of Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
History : 11/08/2023 - v1.0 - Created project file
          12/08/2023 - v1.1 - Imported numpy and matplotlib and created update function
          13/08/2023 - v1.2 - Fixed bug in update function


"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

__author__ = "Steven Diep"
__maintainer__ = "Steven Diep"
__email__ = "steven_diep@hotmail.co.uk"
__status__ = "Prototype"  # "Development" "Prototype" "Production"

# Set the dimensions of the grid
height = 100
width = 100

# Create a random initial grid with 0s and 1s
grid = np.random.choice([0, 1], width * height).reshape((height, width))


# Create a function to update the grid for each frame
# The 'frameNum' param is not used explicitly. It is a placeholder from 'FuncAnimation'
def update(frameNum, img, grid, width, height):
    new_grid = grid.copy()
    for i in range(height):
        for j in range(width):
            # Checking total of live cells at given coordinate
            total = int((grid[i, (j - 1) % width] + grid[i, (j + 1) % width] +
                         grid[(i - 1) % height, j] + grid[(i + 1) % height, j] +
                         grid[(i - 1) % height, (j - 1) % width] + grid[(i - 1) % height, (j + 1) % width] +
                         grid[(i + 1) % height, (j - 1) % width] + grid[(i + 1) % height, (j + 1) % width]))
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation. (total < 2)
            # Any live cell with more than three live neighbours dies, as if by overpopulation. (total > 3)
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if total == 3:
                    new_grid[i, j] = 1
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


# Create a figure and axis
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')

# Create the animation object
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, width, height), frames=100, interval=50, blit=True)

# Show the animation
plt.show()
