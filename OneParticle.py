from functions import *
from plotting import *

B1=np.array([0,0,B0])
S1init=np.array([1,0,0])
T=50
H1=Hj1(B1,mu)

Heun(h,S1init,T,mu,gamma,alfa,H1,"S1Heun","t1Heun")
#plot1Spin(S1,len(t1)-1)
S1=np.load("S1.npy")
t1=np.load("t1.npy")

#plotXandYfor1Spin(S1,t1)
#plot1Spin(S1,len(t1)-1)

"""Comparison"""
Euler(h,S1init,T,mu,gamma,alfa,H1,"S1Euler","t1Euler")

analyticSol1Particle(h,T,S1init, "S1Analytic","t1Analytic")

compareSolutions("S1Heun.npy","S1Euler.npy","S1Analytic.npy","t1Heun.npy","ComparisonPlot")