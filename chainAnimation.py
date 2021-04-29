
"""ANIMATION"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import PIL

import matplotlib as mpl 
mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\krist\\Documents\\Dokumenter\\H19\\ffmpeg\\bin\\ffmpeg.exe'
writer = animation.PillowWriter(fps=30) 

X=0
Y=1
Z=2

S=np.load("antiFerroAni.npy") 

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the grid
x=np.linspace(-0.2,0.2,10)
y=np.zeros(10)
z=np.zeros(10)
#xx, yy, zz = np.meshgrid(x,y,z)


#print(S)
#Q=ax.quiver(x, y, z, S[ti,0,X], S[ti,0,Y], S[ti,0,Z], length=0.1, normalize=True)
U=S[0,:,X]
V=S[0,:,Y]
W=S[0,:,Z]

l=0.2
ax.set_xlim(-l,l)
ax.set_ylim(-l,l)
ax.set_zlim(-l,l)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

Q=ax.quiver(x, y, z, U, V, W, length=0.5, normalize=True)




def updateAni(ti):
    global Q
    global S
    global xx
    global yy
    global zz
    U=S[ti*50,:,X]
    V=S[ti*50,:,Y]
    W=S[ti*50,:,Z]
    Q.remove()
    Q=ax.quiver(x, y, z, U, V, W, length=0.1, normalize=True)


ani=FuncAnimation(fig,updateAni,blit=False,save_count=200)

f = r"C:\\Users\\krist\\Documents\\Dokumenter\\V21\\Numerisk fysikk\\NumericalPhysicsProject2\\antiFerroSpinChain.gif" 
ani.save(f,writer=writer)
plt.show()

