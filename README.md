# What it does
This is my attempt at Conway's Game of Life in Python. Just doing it for fun and games.
A grid of size set to 100 by 100 is initialised randomly with 1s and 0s - 1 being alive/white and 0 being dead/black.
The game follows four simple rules:
  * Any live cell with fewer than 2 live neighbours dies due to underpopulation.
  * Any live cell with more than 3 live neighbours dies due to overpopulation.
  * Any dead cell with exactly 3 live neighbours becomes a live cell due to reproduction.
  * Any live cell with exactly 2 or 3 neighbours survives to the next generation.

# Usage Notes
To start the game, run 'python -m conway.py' from the terminal inside the main project folder.
You may also check out 'demo.py' as I used that to understand how matplotlib.animation works.

# Credits
Goes to the resources that helped me:
* https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
* https://www.youtube.com/watch?v=dOKHY_PUvqU&t=315s&ab_channel=JieJenn
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#
* https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html
