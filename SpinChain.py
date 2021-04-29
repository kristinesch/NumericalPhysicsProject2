from functions import *
from plotting import *
import random

#Some parameters
J=0.8
B0=0
alfa=0.05
dz=0.1 
T=10
mu=1
h=0.01
gamma=1
N=10

#Magnetic field
B10=np.array([0,0,B0])

#for random numbers
random.seed(4)

"""FUNCTIONS"""

#initializing N spins in random directions
def initSpins(N): #N=number of spins
    spins=np.zeros((N,3))
    for spin in spins:
        theta=random.uniform(0,2*np.pi)
        phi=random.uniform(0,np.pi)
        spin[X]=np.cos(theta)*np.sin(phi)
        spin[Y]=np.sin(theta)*np.sin(phi)
        spin[Z]=np.cos(phi)
    return spins

#initializing N spins, all along the z-direction except the first, which is sligthly tilted
def initTiltedSpin(N):
    spins=np.zeros((N,3))
    phi=np.pi/6
    spins[0,X]=np.sin(phi)
    spins[0,Z]=np.cos(phi)
    spins[1:,Z]=1
    return spins

def groundState(N,h,T,mu,gamma,alfa,Hj,J,dz,B):
    spins=initSpins(N)
    S,t=HeunMethod(h,spins,T,mu,gamma,alfa,Hj,J,B,dz)
    if J>0:
        plotTitle="Ferromagnetic spins"
        filename="Jpos"
    else: 
        plotTitle="Anti-ferromagnetic spins"
        filename="Jneg"

    plotXYZvsTime(S,t,filename," (J="+str(J)+", alfa="+str(alfa)+")",plotTitle)

    

#plots spin coords, and saves data to make animation from
def magnon(N,h,T,mu,gamma,alfa,Hj,J,B10,dz,plotfile,animationfile,B,plotTitle):
    spinsWithTilt=initTiltedSpin(10)
    SMag,tMag=HeunMethod(h,spinsWithTilt,T,mu,gamma,alfa,Hj,J,B,dz)
    np.save(animationfile,SMag)
    plotXYZvsTime(SMag,tMag,plotfile," (J="+str(J)+", alfa="+str(alfa)+")",plotTitle)




#print(spinsWithTilt)
#print(tenSpins)

""""
#check if length 1
lengths=tenSpins[:,X]*tenSpins[:,X]+tenSpins[:,Y]*tenSpins[:,Y]+tenSpins[:,Z]*tenSpins[:,Z]
print(lengths)
"""

"""GROUND STATES"""
# tenSpins=initSpins(10)
# tenSpins=initSpins(10) 


# groundState(N,h,200,mu,gamma,alfa,Hj,J,dz,B10) 
# groundState(N,h,200,mu,gamma,alfa,Hj,-J,dz,B10)

"""MAGNON"""
Jmag=0
alfaMag=0
S1=initSpins(3)
SMag,tMag=HeunMethod(h,S1,500,mu,gamma,alfaMag,Hj,Jmag,B10,dz)
plotXYZvsTime(SMag,tMag,"MagnonTest"," (J="+str(Jmag)+", alfa="+str(alfaMag)+")","Spin chain without coupling")

#tilt 1st spins DELETE??
spinsWithTilt=initTiltedSpin(10)
SMagTilt,tMagTilt=HeunMethod(h,spinsWithTilt,1000,mu,gamma,alfaMag,Hj,Jmag,B10,dz)
plotXYZvsTime(SMag,tMag,"MagnonTestTilt"," (J="+str(Jmag)+", alfa="+str(alfaMag)+")","Spin chain without coupling")




"""Damping and coupling off"""
magnon(N,h,100,mu,gamma,0,Hj,0,B10,dz,"noDampingOrCoupling","noDampingOrCouplingAni",B10,"Spin chain")

"""Damping off"""
magnon(N,h,20,mu,gamma,0,Hj,J,B10,dz,"noDamping","noDampingAni",B10,"Spin chain")

"""Basic magnon"""
magnon(N,h,100,mu,gamma,alfa,Hj,J,B10,dz,"basic","basicAni",B10,"Spin chain")

"""periodic BCs"""
magnon(N,h,20,mu,gamma,alfa,HjInf,J,B10,dz,"periodicBC","periodicBCani",B10, "Spin chain with periodic BCs")

"""Antiferromagnetic coupling"""
magnon(N,h,200,mu,gamma,alfa,Hj,-J,B10,dz,"antiFerro","antiFerroAni",B10, "Spin chain with antiferromagnetic coupling")



"""MAGNETIZATION"""

"""Plot Z component of basic magnon"""
spins=initTiltedSpin(10)
S,t=HeunMethod(h,spins,1000,mu,gamma,alfa,Hj,J,B10,dz)
#plotZvsTime(S,t,"Spin chain with coupling and damping","basicZ")
def plotTotalZ(S,t,filename):
    fig,ax=plt.subplots(1,1)
    totZ=[]
    for i in range(len(t)):
        totZ.append(np.sum(S[i,:,Z]))
    ax.plot(t,totZ)
    fig.suptitle("Total")
    fig.savefig(filename)
    plt.show()
plotTotalZ(S, t, "totalZ")

"""3D PLOTS OF FINAL SPINS"""
#ferromagnetic coupling
spins=initSpins(10)
SMag,tMag=HeunMethod(h,spins,500,mu,gamma,alfa,Hj,J,B10,dz)
#plotFinalPosition(SMag,tMag,"Spin directions after simulation for ferromagnetic coupling","finalFerro")

#antiferromagnetic coupling
spins=initSpins(10)
SMag,tMag=HeunMethod(h,spins,500,mu,gamma,alfa,Hj,-J,B10,dz)
#plotFinalPosition(SMag,tMag,"Spin directions after simulation for anti-ferromagnetic coupling","finalAntiFerro")