"""ANIMATION"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
#for only 1 spin first
X=0
Y=1
Z=2

S=np.load("S1.npy") 

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the grid
x, y, z = np.meshgrid(0,0,0)


#print(S)
#Q=ax.quiver(x, y, z, S[ti,0,X], S[ti,0,Y], S[ti,0,Z], length=0.1, normalize=True)
U=S[0,0,X]
V=S[0,0,Y]
W=S[0,0,Z]

Q=ax.quiver(x, y, z, U, V, W, length=0.1, normalize=True)


def updateAni(ti):
    global Q
    global S
    global x
    global y
    global z
    U=S[ti*10,0,X]
    V=S[ti*10,0,Y]
    W=S[ti*10,0,Z]
    Q.remove()
    Q=ax.quiver(x, y, z, U, V, W, length=0.1, normalize=True)


ani=FuncAnimation(fig,updateAni,blit=False)
plt.show()
print("OK")