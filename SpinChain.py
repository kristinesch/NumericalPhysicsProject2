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


tenSpins=initSpins(10)
#print(spinsWithTilt)
#print(tenSpins)

""""
#check if length 1
lengths=tenSpins[:,X]*tenSpins[:,X]+tenSpins[:,Y]*tenSpins[:,Y]+tenSpins[:,Z]*tenSpins[:,Z]
print(lengths)
"""

"""GROUND STATES"""
# tenSpins=initSpins(10)
# S10,t10=HeunMethod(h,tenSpins,T,mu,gamma,alfa,Hj,J,B10,dz)


# plotXYZvsTime(S10,t10,"Jpos"," (J="+str(J)+", alfa="+str(alfa)+")","Ferromagnetic spins")
# plotXYZvsTime(S10,t10,"Jneg"," (J="+str(J)+", alfa="+str(alfa)+")","Anti-ferromagnetic spins")

groundState(N,h,500,mu,gamma,alfa,Hj,J,dz,B10)
groundState(N,h,500,mu,gamma,alfa,Hj,-J,dz,B10)

# """MAGNON"""

# S1=initSpins(3)
# print(S1)

# SMag,tMag=HeunMethod(h,S1,T,mu,gamma,0,Hj,0,B10,dz)
# plotXYZvsTime(SMag,tMag,"MagnonTest"," (J="+str(J)+", alfa="+str(alfa)+")","Spin chain")

# #tilt 1st spin
# spinsWithTilt=initTiltedSpin(10)
# SMagTilt,tMagTilt=HeunMethod(h,spinsWithTilt,T,mu,gamma,0,Hj,0,B10,dz)
# plotXYZvsTime(SMag,tMag,plotfile," (J="+str(J)+", alfa="+str(alfa)+")",plotTitle)




"""Damping and coupling off"""
#magnon(N,h,100,mu,gamma,0,Hj,0,B10,dz,"noDampingOrCoupling","noDampingOrCouplingAni",B10,"Spin chain")

"""Damping off"""
#magnon(N,h,20,mu,gamma,0,Hj,J,B10,dz,"noDamping","noDampingAni",B10,"Spin chain")

"""Basic magnon"""
#magnon(N,h,20,mu,gamma,alfa,Hj,J,B10,dz,"basic","basicAni",B10,"Spin chain")

"""periodic BCs"""
#magnon(N,h,20,mu,gamma,0,HjInf,J,B10,dz,"periodicBC","periodicBCani",B10, "Spin chain with periodic BCs")