import numpy as np
import matplotlib.pyplot as plt

chessboard = np.zeros((8, 8))

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chessboard[i, j] = 1

extent = [0, 8, 0, 8]

plt.imshow(chessboard, cmap="binary_r", interpolation="nearest", extent=extent)
plt.title("Chessboard with Python by Prerna Kukade ")
plt.show()