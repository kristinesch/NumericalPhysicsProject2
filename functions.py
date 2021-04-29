import numpy as np
from constants import *
from numba import jit


"""Function returning Hj"""
#J is a constant
#S is an array of spins for all particles
#B is the magnetic field

#only 1 particle
#@jit(nopython = True)
def Hj1(B,mu): 
    return mu*B 

#multiple particles
#at a given time
@jit(nopython = True)
def Hj(S,J,B,mu,dz): #S is an array with dim (N,3)
    N=len(S)
    Hj=np.zeros((N,3))
    Hj[0]=0.5*J*(S[1])+dz*np.array([0,0,2*S[0,Z]])+mu*B
    for j in range(1,N-1):
        Hj[j]=0.5*J*(S[j-1]+S[j+1])+dz*np.array([0,0,2*S[j,Z]])+mu*B
    Hj[N-1]=0.5*J*(S[N-2])+dz*np.array([0,0,2*S[N-1,Z]])+mu*B
    return Hj

def HjInf(S,J,B,mu,dz): #periodic BCs
    N=len(S)
    Hj=np.zeros((N,3))
    Hj[0]=0.5*J*(S[1]+S[-1])+dz*np.array([0,0,2*S[0,Z]])+mu*B
    for j in range(1,N-1):
        #print(Hj[i,j])
        Hj[j]=0.5*J*(S[j-1]+S[j+1])+dz*np.array([0,0,2*S[j,Z]])+mu*B
    Hj[N-1]=0.5*J*(S[N-2]+S[0])+dz*np.array([0,0,2*S[N-1,Z]])+mu*B
    return Hj


"""function for f(y,t) in Heun method"""
@jit(nopython = True)
def f(S,mu,gamma,alfa,H): #H and S are arrays of vectors
    ScrossH=np.cross(S,H) #cross product of S with 
    return (-gamma/(np.abs(mu)*(1+alfa*alfa)))*(ScrossH+np.cross((alfa*S),ScrossH))



"""Heun method"""

#@jit(nopython = True)
#only works for 1 spin!!!
def Heun(h,S0,T,mu,gamma,alfa,Hj,oneSpin=False): #T is the total time
    if oneSpin:
        N=1
    else: 
        N=len(S0)
        #print("N=",N)
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    S[0]=S0.copy()
    for i in range(len(t)-1):
        print(i/len(t))
        S_intermediate=S[i]+h*f(S[i],mu,gamma,alfa,Hj)
        S[i+1]=S[i]+(h/2)*(f(S[i],mu,gamma,alfa,Hj)+f(S_intermediate,mu,gamma,alfa,Hj))
    return S, t

#fixed
def HeunMethod(h,S0,T,mu,gamma,alfa,Hjfunc,J,B,dz): #Hj is a function
    N=len(S0)
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    S[0]=S0.copy()
    for i in range(len(t)-1):

        x=i*100/len(t)
        if (x//10==0):
            print(x)

        Hjt=Hjfunc(S[i],J,B,mu,dz) #at this given time
        #print(Hjt)
        S_intermediate=S[i]+h*f(S[i],mu,gamma,alfa,Hjt)
        S[i+1]=S[i]+(h/2)*(f(S[i],mu,gamma,alfa,Hjt)+f(S_intermediate,mu,gamma,alfa,Hjt))
    
    return S, t


"""Euler method"""

#@jit(nopython = True)
def Euler(h,S0,T,mu,gamma,alfa,Hj,oneSpin=False):
    if oneSpin:
        N=1
    else: 
        N=len(S0) 
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    S[0]=S0.copy()
    for i in range(len(t)-1):
        S[i+1]=S[i]+h*f(S[i],mu,gamma,alfa,Hj)
    return S,t

"""Error estimate"""
#Analytic solution for 1 particle, with magn.field in z-direction, and the spin in the xy-plane

@jit(nopython = True)
def analyticSol1Particle(h,T,S0,Hj,gamma,mu):
    N=len(S0)
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    x0=S0[X]
    y0=S0[Y]
    z0=S0[Z]
    Hz=Hj[Z]
    theta=gamma*Hz/mu
    for i in range(len(t)):
        S[i,X]=x0*np.cos(theta*t[i])-y0*np.sin(theta*t[i])
        S[i,Y]=x0*np.sin(theta*t[i])+y0*np.cos(theta*t[i])
        S[i,Z]=z0
    return S, t


#calculates total error: the difference between two arrays after a given time (last elements of arrays)
#NB written for only 1 spin
#@jit(nopython = True)
def calculateError(Snum, Sanalytic): 
    N=len(Snum)-1
    errors=np.abs(Snum[N,0,X]-Sanalytic[N,0,X])
    totalError=np.sum(errors)
    return totalError

#Calculates error for given method as a function of stepsize
#@jit(nopython = True)
def errorVsStepsize(methodFunction,S0,T,mu,gamma,alfa,Hj): #n is the number of elements in hList
    hList=np.linspace(0.00001,0.1,5)
    errors=np.zeros(len(hList))
    i=0
    for hi in hList:
        print(hi)
        Sanalytic,tana=analyticSol1Particle(hi,T,S0,Hj,gamma,mu)
        Si,ti=methodFunction(hi,S0,T,mu,gamma,alfa,Hj,oneSpin=True)
        errors[i]=calculateError(Si,Sanalytic)
        i+=1
    return errors, hList

