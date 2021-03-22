from functions import *
from plotting import *

B1=np.array([0,0,B0])
S1init=np.array([1,0,0])
T=20
H1=Hj1(B1,mu)

#Heun(h,S1init,T,mu,gamma,alfa,H1,"S1","t1")
#plot1Spin(S1,len(t1)-1)
S1=np.load("S1.npy")
t1=np.load("t1.npy")

#plotXandYfor1Spin(S1,t1)
#plot1Spin(S1,len(t1)-1)

spinAnimation(S1)