"""

File    : demo.py
Date    : Friday 11 August 2023
Desc    : A demo file to learn how to use FuncAnimation
            (https://www.youtube.com/watch?v=dOKHY_PUvqU&t=315s&ab_channel=JieJenn)
History : 11/08/2023 - v1.0 - Created project file
          11/08/2023 - v1.1 - Implemented an animation for a straight line graph


"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

__author__ = "Steven Diep"
__maintainer__ = "Steven Diep"
__email__ = "steven_diep@hotmail.co.uk"
__status__ = "Prototype"  # "Development" "Prototype" "Production"

x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 105)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)


def animation_frame(i):
    x_data.append(i * 10)
    y_data.append(i)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,


animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.01), interval=10)

plt.show()
