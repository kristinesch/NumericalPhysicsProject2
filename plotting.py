
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

X=0
Y=1
Z=2

def plotLastFrame(S,ti):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.8))


    ax.quiver(x, y, z, S[ti,:,X], S[ti,:,Y], S[ti,:,Z], length=0.1, normalize=True)

    plt.show()

def plot1Spin(S,ti):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(0,0,0)

    print(S[ti,0,X], S[ti,0,Y], S[ti,0,Z])
    #print(S)
    ax.quiver(x, y, z, S[ti,0,X], S[ti,0,Y], S[ti,0,Z], length=0.1, normalize=True)

    plt.show()

def plotXandYfor1Spin(S,t):
    x=S[:,:,X]
    y=S[:,:,Y]
    length=np.sqrt(x*x+y*y)
    plt.plot(t,x)
    plt.plot(t,y)
    plt.plot(t,length,color="red")
    plt.show()

#comparing Heund, Euler and analytic solution for 1 spin
def compareSolutions(SHeundFile,SEulerFile,SAnalyticFile,tFile,filename):
    SHeund=np.load(SHeundFile)
    SEuler=np.load(SEulerFile)
    SAnalytic=np.load(SAnalyticFile)
    t=np.load(tFile)
    print(SHeund)
    fig, ax=plt.subplots(1,1)
    ax.plot(t,SHeund[:,0,X],label="Heund")
    ax.plot(t,SEuler[:,0,X],label="Euler")
    ax.plot(t,SAnalytic[:,0,X],label="Analytic")
    fig.legend()
    fig.savefig(filename)
    plt.show()




