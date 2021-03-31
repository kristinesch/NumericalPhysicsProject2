
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

S=np.load("basicAni.npy") 

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the grid
x=np.linspace(-100,100,10)
y=np.zeros(10)
z=np.zeros(10)
#xx, yy, zz = np.meshgrid(x,y,z)


#print(S)
#Q=ax.quiver(x, y, z, S[ti,0,X], S[ti,0,Y], S[ti,0,Z], length=0.1, normalize=True)
U=S[0,:,X]
V=S[0,:,Y]
W=S[0,:,Z]

# ax.set_xlim(-10,10)
# ax.set_ylim(-10,10)
#ax.set_zlim(-0.5,0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

Q=ax.quiver(x, y, z, U, V, W, length=0.1, normalize=True)




def updateAni(ti):
    global Q
    global S
    global xx
    global yy
    global zz
    U=S[ti*10,:,X]
    V=S[ti*10,:,Y]
    W=S[ti*10,:,Z]
    Q.remove()
    Q=ax.quiver(x, y, z, U, V, W, length=0.1, normalize=True)


ani=FuncAnimation(fig,updateAni,blit=False,save_count=200)

f = r"C:\\Users\\krist\\Documents\\Dokumenter\\V21\\Numerisk fysikk\\NumericalPhysicsProject2\\spinChain.gif" 
ani.save(f,writer=writer)
plt.show()

