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


"""Heun method function"""
#T is the total time
def Heun(h,S0,T,mu,gamma,alfa,Hj,SFile,tFile): 
    print(S0)
    N=len(S0)
    t=np.arange(0,T,h)
    S=np.zeros((len(t),N,3))
    S[0]=S0
    print("S",S)
    for i in range(len(t)-1):
        print("i",i)
        S_intermediate=S[i]+h*f(S[i],mu,gamma,alfa,Hj)
        S[i+1]=S[i]+(h/2)*(f(S[i],mu,gamma,alfa,Hj)+f(S_intermediate,mu,gamma,alfa,Hj))
    np.save(SFile,S)
    np.save(tFile,t)