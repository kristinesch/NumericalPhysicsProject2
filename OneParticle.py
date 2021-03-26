from functions import *
from plotting import *

#%load_ext line_profiler

B1=np.array([0,0,B0])
theta=np.pi/9
S1init=np.array([np.sin(theta),0,np.cos(theta)])
T=100
H1=Hj1(B1,mu)

# S1Heun, t1Heun = Heun(h,S1init,T,mu,gamma,alfa,H1,oneSpin=True)
# np.save("S1Heun",S1Heun)
# np.save("t1Heun",t1Heun)

#plot1Spin(S1,len(t1)-1)

#plotXandYfor1Spin(S1,t1)
#plot1Spin(S1,len(t1)-1)

"""Comparison"""
# S1Euler, t1Euler=Euler(h,S1init,T,mu,gamma,alfa,H1,oneSpin=True)
# np.save("S1Euler",S1Euler)
# np.save("t1Euler",t1Euler)

# S1Analytic, t1Analytic=analyticSol1Particle(h,T,S1init,H1)
# np.save("S1Analytic",S1Analytic)
# np.save("t1Analytic",t1Analytic)

# print("calculations done")

# #compareSolutions("S1Heun.npy","S1Euler.npy","S1Analytic.npy","t1Heun.npy","ComparisonPlot")

# HeunError, HeunhList=errorVsStepsize(Heun,S1init,T,mu,gamma,alfa,H1)
# print("yo")
# EulerError, EulerhList=errorVsStepsize(Euler,S1init,T,mu,gamma,alfa,H1)

# plotErrorVsStepsize(HeunError,HeunhList,EulerError, EulerhList,"ErrorPlot")
# print("done")

#%lprun -f plotErrorVsStepsize x = plotErrorVsStepsize(HeunError,HeunhList,EulerError, EulerhList,"test")


"""With damping"""
dampedAlfa=0.05
S1HeunDamped, t1HeunDamped = Heun(h,S1init,T,mu,gamma,dampedAlfa,H1,oneSpin=True)
np.save("S1HeunDamped",S1HeunDamped)
np.save("t1HeunDamped",t1HeunDamped)

plotXYZ1Spin(S1HeunDamped,t1HeunDamped)