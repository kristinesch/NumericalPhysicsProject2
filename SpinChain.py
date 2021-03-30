from functions import *
from plotting import *
import random


J=-0.8
B0=0
alfa=0.05
dz=0.1 
T=100
mu=1
h=0.01
gamma=1

B10=np.array([0,0,B0])

random.seed(4)


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

def initTiltedSpin(N):
    spins=np.zeros((N,3))
    phi=np.pi/6
    spins[0,X]=np.sin(phi)
    spins[0,Z]=np.cos(phi)
    spins[1:,Z]=1
    return spins


tenSpins=initSpins(10)
#print(spinsWithTilt)
#print(tenSpins)

""""
#check if length 1
lengths=tenSpins[:,X]*tenSpins[:,X]+tenSpins[:,Y]*tenSpins[:,Y]+tenSpins[:,Z]*tenSpins[:,Z]
print(lengths)
"""

"""GROUND STATES"""

# S10,t10=HeunMethod(h,tenSpins,T,mu,gamma,alfa,Hj,J,B10,dz)

# #plotZvsTime(S10,t10,"10spinsJ=0,8","J="+str(J))
# plotZvsTime(S10,t10,"10spinsJ=-0,8","J="+str(J))

"""MAGNON"""


alfaMag=0
JMag=0

S1=initSpins(3)
#print(S1)

# SMag,tMag=HeunMethod(h,S1,T,mu,gamma,alfaMag,Hj,JMag,B10,dz)
# plotZvsTime(SMag,tMag,"MagnonTest","J=0, alfa=0")

#tilt 1st spin
# spinsWithTilt=initTiltedSpin(10)
# SMagTilt,tMagTilt=HeunMethod(h,spinsWithTilt,T,mu,gamma,alfaMag,Hj,JMag,B10,dz)
# plotZvsTime(SMagTilt,tMagTilt,"MagnonTestTilt","J=0, alfa=0")

#With coupling!!
Jcoup=0.8
spinsWithTilt=initTiltedSpin(10)
SMagTilt,tMagTilt=HeunMethod(h,spinsWithTilt,T,mu,gamma,alfaMag,Hj,Jcoup,B10,dz)
plotZvsTime(SMagTilt,tMagTilt,"MagnonTestTiltCoupled","J=0.8, alfa=0")
