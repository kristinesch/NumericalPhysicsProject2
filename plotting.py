
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



def plot1Spin3D(S,ti):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(0,0,0)

    print(S[ti,0,X], S[ti,0,Y], S[ti,0,Z])
    #print(S)
    ax.quiver(x, y, z, S[ti,0,X], S[ti,0,Y], S[ti,0,Z], length=0.1, normalize=True)

    plt.show()



def plot1Spin(S,t,filename,plotTitle):
    x=S[:,:,X]
    y=S[:,:,Y]
    z=S[:,:,Z]
    length=np.sqrt(x*x+y*y+z*z)
    fig,ax=plt.subplots(2,1)
    fig.suptitle(plotTitle)
    ax[0].plot(t,x,label="x",color="blue")
    ax[0].plot(t,y,label="y",color="red")
    # ax[0].set_xlabel("time")
    # ax[0].set_ylabel("coordinate")
    ax[1].plot(t,z,label="z",color="green")
    ax[1].plot(t,length,label="Length",color="orange")
    ax[1].set_xlabel("time")
    #ax[1].set_ylabel("coordinate")
    fig.legend()
    fig.savefig(filename)
    plt.show()

def plot1spinLifetime(S,t,tau,filename,plotTitle,l0):
    decay=l0*np.exp(-t/tau)
    x=S[:,:,X]
    y=S[:,:,Y]
    fig,ax=plt.subplots(1,1)
    fig.suptitle(plotTitle)
    ax.plot(t,x,label="x",color="blue")
    ax.plot(t,y,label="y",color="green")
    ax.plot(t,decay,label="exponential decay",color="red")
    fig.legend()
    fig.savefig(filename)
    plt.show()



#comparing Heund, Euler and analytic solution for 1 spin
def compareSolutions(SHeundFile,SEulerFile,SAnalyticFile,tFile,filename):
    SHeund=np.load(SHeundFile)
    SEuler=np.load(SEulerFile)
    SAnalytic=np.load(SAnalyticFile)
    t=np.load(tFile)


    #Plotting:
    fig, ax=plt.subplots(1,1)
    ax.set_xlabel("time")
    ax.set_ylabel("x")
    fig.suptitle("Oscillation of x-coordinate for one spin")
    ax.plot(t,SHeund[:,0,X],label="Heun")
    ax.plot(t,SEuler[:,0,X],label="Euler")
    ax.plot(t,SAnalytic[:,0,X],label="Analytic")
    fig.legend()
    fig.savefig(filename)
    plt.show()



def plotErrorVsStepsize(HeunError,HeunSteps,EulerError,EulerSteps,filename):
    print("OK")
    fig, ax=plt.subplots(1,1)
    ax.set_xlabel("Step size")
    ax.set_ylabel("Error")
    fig.suptitle("Error as a function of step size")
    # ax.plot(np.log(HeunSteps),np.log(HeunError),label="Heun")
    # ax.plot(np.log(EulerSteps),np.log(EulerError),label="Euler")
    ax.plot(HeunSteps,HeunError,label="Heun")
    ax.plot(EulerSteps,EulerError,label="Euler")
    ax.set_xscale('log')
    ax.set_yscale('log')
    fig.legend()
    fig.savefig(filename)
    plt.show()

def plotXYZvsTime(S,t,filename,title,plotTitle):
    fig, ax=plt.subplots(3,1)
    print("S",len(S))
    for i in range(len(S[0])):
        ax[0].plot(t,S[:,i,X])
        ax[1].plot(t,S[:,i,Y])
        ax[2].plot(t,S[:,i,Z])
    ax[2].set_xlabel("time")
    ax[0].set_ylabel("$S_{x}$")
    ax[1].set_ylabel("$S_{y}$")
    ax[2].set_ylabel("$S_{z}$")
    for i in range(3):
        ax[i].set_ylim(-1,1)
    fig.suptitle(plotTitle+title)
    fig.savefig(filename)
    plt.show()

def plotZvsTime(S,t,title,filename):
    fig, ax=plt.subplots(1,1)
    for i in range(len(S[0])):
        ax.plot(t,S[:,i,Z])
    ax.set_xlabel("time")
    ax.set_ylabel("z")
    fig.suptitle(title)
    fig.savefig(filename)
    plt.show()

def plotFinalPosition(S,t,title,filename):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the grid
    x=np.linspace(-0.2,0.2,10)
    y=np.zeros(10)
    z=np.zeros(10)
    n=len(S)
    U=S[n-1,:,X]
    V=S[n-1,:,Y]
    W=S[n-1,:,Z]

    l=0.2
    ax.set_xlim(-l,l)
    ax.set_ylim(-l,l)
    ax.set_zlim(-l,l)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    fig.suptitle(title)

    ax.quiver(x, y, z, U, V, W, length=0.1, normalize=True)
    fig.savefig(filename)


