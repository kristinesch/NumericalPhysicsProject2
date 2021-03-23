import numpy as np
from constants import *

"""Initialization"""
#initialize spin array

"""Function returning Hj"""
#J is a constant
#S is an array of spins for all particles
#B is the magnetic field

#only 1 particle
def Hj1(B,mu): 
    return -mu*B 

#multiple particles
"""
def H(S,J,B,mu):
    Hx=
    Hy=
    Hz=
    

"""

"""function for f(y,t) in Heun method"""
def f(S,mu,gamma,alfa,H): #H and S are arrays of vectors
    ScrossH=np.cross(S,H) #cross product of S with H
    return (-gamma/(np.abs(mu)*(1+alfa*alfa)))*(ScrossH+np.cross((alfa*S),ScrossH))


"""Heun method"""


def Heun(h,S0,T,mu,gamma,alfa,Hj,oneSpin=False): #T is the total time
    if oneSpin:
        N=1
    else: 
        N=len(S0[0])
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    S[0]=S0.copy()
    for i in range(len(t)-1):
        print(i/len(t))
        S_intermediate=S[i]+h*f(S[i],mu,gamma,alfa,Hj)
        S[i+1]=S[i]+(h/2)*(f(S[i],mu,gamma,alfa,Hj)+f(S_intermediate,mu,gamma,alfa,Hj))
    return S, t

"""Euler method"""


def Euler(h,S0,T,mu,gamma,alfa,Hj,oneSpin=False):
    if oneSpin:
        N=1
    else: 
        N=len(S0[0])
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    S[0]=S0.copy()
    for i in range(len(t)-1):
        S[i+1]=S[i]+h*f(S[i],mu,gamma,alfa,Hj)
    return S,t

"""Error estimate"""
#Analytic solution for 1 particle, with magn.field in z-direction, and the spin in the xy-plane


def analyticSol1Particle(h,T,S0,Hj):
    N=len(S0)
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    x0=S0[X]
    y0=S0[Y]
    Hz=Hj[Z]
    theta=gamma*Hz/mu
    for i in range(len(t)):
        S[i,X]=x0*np.cos(theta*t[i])-y0*np.sin(theta*t[i])
        S[i,Y]=x0*np.sin(theta*t[i])+y0*np.cos(theta*t[i])
        S[i,Z]=0
    return S, t


#calculates total error: the difference between two arrays
#NB written for only 1 spin
def calculateError(Snum, Sanalytic): 
    #print("YO",Sanalytic)
    errors=np.abs(Snum[:,0,X]-Sanalytic[:,0,X])
    totalError=np.sum(errors)
    return totalError

#Calculates error for given method as a function of stepsize
def errorVsStepsize(n,methodFunction,S0,T,mu,gamma,alfa,Hj): #n is the number of elements in hList
    hList=np.linspace(0.01,1,n)
    errors=np.zeros(len(hList))
    i=0
    for hi in hList:
        Sanalytic,tana=analyticSol1Particle(hi,T,S0,Hj)
        Si,ti=methodFunction(hi,S0,T,mu,gamma,alfa,Hj,oneSpin=True)
        errors[i]=calculateError(Si,Sanalytic)
        i+=1
    return errors, hList

