from functions import *
from plotting import *
import random


J=0.8
B0=0
alfa=0.05
dz=0.1 
T=500
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

tenSpins=initSpins(10)
print(tenSpins)

""""
#check if length 1
lengths=tenSpins[:,X]*tenSpins[:,X]+tenSpins[:,Y]*tenSpins[:,Y]+tenSpins[:,Z]*tenSpins[:,Z]
print(lengths)
"""

S10,t10=HeunMethod(h,tenSpins,T,mu,gamma,alfa,Hj,J,B10,dz)

plotZvsTime(S10,t10,"10spins")


