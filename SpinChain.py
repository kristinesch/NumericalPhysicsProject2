from functions import *
from plotting import *
import random


J=0.5
B0=0
alfa=0.05
dz=0.1 

B1=np.array([0,0,B0])

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

#check if length 1
lengths=tenSpins[:,X]*tenSpins[:,X]+tenSpins[:,Y]*tenSpins[:,Y]+tenSpins[:,Z]*tenSpins[:,Z]
print(lengths)


