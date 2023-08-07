import pandas as pd
import math as m
import numpy as np
from scipy.integrate import *
from scipy.interpolate import interp2d
from scipy.interpolate import interp1d
import collections as c
import time as t
import matplotlib.pyplot as plt
import Flux as fff
import cross as cs
import mpmath as mp
s=cs.C_s()
class zf:
    def __init__(self):
        self.crosscc=pd.read_csv('zm_factor.dat',sep='\t', engine='python', header=None,names=['energy','y','d'])
#        self.crosscc=pd.read_csv('z_factor2.dat',sep='\t', engine='python', header=None,names=['energy','y','d'])
        self.y=list(c.Counter(self.crosscc['y']).keys())
        self.e=list(c.Counter(self.crosscc['energy']).keys())
        ne=len(self.e)
        self.y=sorted(self.y)
        self.e=sorted(self.e)
        ny=len(self.y)
        self.d=np.zeros([ne,ny])
        self.e_max=(np.array(self.e)).max()
        for i in range(ne):
            a=self.crosscc[self.crosscc['energy']==self.e[i]]
            for j in range(ny):
                b=a[a['y']==self.y[j]]
                self.d[i][j]=b['d']
            print(i)
        self.f=interp2d((self.y),self.e,self.d,kind='cubic')
    
    def plot_data(self):
        e=np.logspace(1,8,num=8)
        y=self.y
        regfun=np.zeros([len(e),len(y)])
        for i in range(len(e)):
            regfun[i]=self.f(y,e[i])
            fig=plt.figure(figsize=(18,12))
            plt.plot(y,regfun[i])
            plt.title(r'Neutrino regeneration function for $E_{\nu}$ = '+str('{:1.1e}'.format(e[i])),fontsize=14)
            plt.xlabel('e',fontsize=15)
            plt.ylabel(r'$\Phi_{\nu}(E_{\nu},y)$',fontsize=15)
            plt.xscale('log')
            plt.show()
            plt.close()
    
    def plot_data1(self):
        e=np.logspace(1,8,num=80)
        x=10.**(10)
        y=np.array([x,x/2,x/5,x/10,x/20,x/50,x/100,x/1000])
        regfun=np.zeros([len(y),len(e)])
        fig=plt.figure(figsize=(18,12))
#        for i in range(len(y)):
        regfun=self.f(y,e)
        for i in range(len(y)):
            plt.plot(e,regfun[:,i],label=str(y[i]))
        plt.title(r'Neutrino regeneration function for $E_{\nu}$',fontsize=14)
        plt.xlabel('e',fontsize=15)
        plt.ylabel(r'$\Phi_{\nu}(E_{\nu},y)$',fontsize=15)
        plt.legend()
        plt.grid(True)
        plt.xscale('log')
        plt.show()
        plt.close()

