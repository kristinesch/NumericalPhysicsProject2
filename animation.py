"""ANIMATION"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

import PIL

import matplotlib as mpl 
mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\krist\\Documents\\Dokumenter\\H19\\ffmpeg\\bin\\ffmpeg.exe'
writer = animation.PillowWriter(fps=30) 

#for only 1 spin first
X=0
Y=1
Z=2

S=np.load("S1HeunDamped.npy") 

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
f = r"C:\\Users\\krist\\Documents\\Dokumenter\\V21\\Numerisk fysikk\\NumericalPhysicsProject2\\1spin.gif" 
ani.save(f,writer=writer)
plt.show()
print("OK")