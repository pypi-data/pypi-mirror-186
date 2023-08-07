import pandas as pd
#import math as m
import numpy as np
from scipy.integrate import *
from scipy.interpolate import interp2d
from scipy.interpolate import interp1d
#import scipy.special as scp
import collections as c
import time as t
import matplotlib.pyplot as plt
#import cross as cs
import cross_section.cross as cs
#import mpmath as mp
#import zf as zf2
#import jb as jb2
import Global.Global as glb
import vegas as vegas

class reg:
    def __init__(self,pdg=14, model = 'CT10nlo', ratio=1.2,A = 8):
        self.model = model
        self.nupdg = pdg
        self.A = A 
        self.s_p=cs.Cross_section(model,pdg,2212)
        self.s_n=cs.Cross_section(model,pdg,2112)
        self.E = 0
        self.x = 0
        self.crosscc = pd.read_csv('regfun_'+str(model)+'_'+str(pdg)+'_'+ str(ratio) + '.dat', sep = '\t', engine = 'python', header = None, names = ['energy', 'y', 'd'])
        self.y = list(c.Counter(self.crosscc['y']).keys())
        self.e = list(c.Counter(self.crosscc['energy']).keys())
        ne = len(self.e)
        a1 = np.array([1, 1, 1, 1])
        b1 = np.array([1, 1, 1, 1])
        self.y = np.array(sorted(self.y))
        self.e = np.array(sorted(self.e))
        self.n_e=len(self.e)
        self.e_low_l=np.log10(self.e.min())
        self.e_up_l=np.log10(self.e.max())
        ny = len(self.y)
        self.y_up=self.y.max()
        self.f = [0 for i in range(len(self.e))]
        self.d = np.zeros([ne, ny])
        for i in range(ne):
            a = self.crosscc[self.crosscc['energy'] == self.e[i]]
            for j in range(ny):
                b = a[a['y'] == self.y[j]]
                self.d[i][j] = b['d']
            print(i, ratio)
            self.f[i] = interp1d(self.y, self.d[i], kind='cubic')
        self.ratio = ratio
        #self.g = fff.Flux('KM','flux_data/Numu_H3a+KM_E2.DAT',3)
        #self.gg = self.g.flux_x(e) # flux in e
        #self.ggg = (self.g.flux_x(e) - self.g.flux_x(e - eps))/(eps) # (flux)' in e

    def set_E(self,E):
        self.E = E
    def set_x(self,x):
        self.x = x


    def flux_model(self, E, K = 10.**(-18), gamma = 2, alpha = 1, E_0 = 10.**6, E_cut = 3*10.**(10)):
        return K*(E_0/E)**(gamma + 1)*(1 + E/E_0)**(-alpha)/(1 + np.tan(np.pi*E/(2*E_cut)))
    

    def plot_data(self):
        e = np.logspace(1, 10, num = 10)
        y = self.y
        print(y)
        regfun = np.zeros([len(e), len(y)])
        for i in range(len(e)):
            j = int(round(self.n_e/(self.e_up_l - self.e_low_l)*(np.log10(e[i]) - self.e_low_l)))
            regfun[i] = self.f[j](y)
            fig = plt.figure(figsize = (18, 12))
            plt.plot(y, regfun[i])
            plt.title(r'Neutrino regeneration function for $E_{\nu}$ = ' + str('{:1.1e}'.format(e[i])), fontsize = 14)
            plt.xlabel('y', fontsize = 15)
            plt.ylabel(r'$\Phi_{\nu}(E_{\nu},y)$', fontsize = 15)
            plt.xscale('log')
            plt.savefig('regfun' + str('{:1.1e}'.format(e[i])) + '.png')
            plt.show()
            plt.close()


    #def flux_x_exp(self, E):
    #    if E <= self.e_cut:
    #        return self.g.flux_x(E)
    #    else:
    #        return self.gg*np.exp((E - self.e_cut)*self.ggg/self.gg)


    #def plot_flux_x(self):
    #    e = np.logspace(1, 10, num = 1000)
    #    b = np.zeros(len(e))
    #    b1 = np.zeros(len(e))
    #    for i in range(len(e)):
    #        b[i] = self.flux_x_exp(e[i])
    #    fig = plt.figure(figsize = (18, 12))
    #    plt.plot(e,b*e*e,label = 'exp. extrapol.')
    #    plt.title(r'$ F_{\nu}(x=0,E)_{exp}$', fontsize = 14)
    #    plt.xlabel(r'$E_{\nu}$', fontsize = 15)
    #    plt.ylabel(r'$F_{\nu}(x=0,E)$, $GeV^{-1}\cdot s^{-1}$', fontsize = 15)
    #    plt.xscale('log')
    #    plt.yscale('log')
    #    plt.savefig('F(x=0)_extr_exp.png')
    #    plt.show()

    def eta(self, y, E):
        E_y = E/(1. - y)
        a = self.flux_model(E_y)/(self.flux_model(E)*(1. - y))
        return a

    #def plot_eta(self):
    #    e = np.logspace(1, 11, num = 12)
    #    y = np.logspace(-11, np.log10(self.y_up), 1000)
    #    b = np.zeros([len(e), len(y)])
    #    for i in range(len(e)):
    #        for j in range(len(y)):
    #            b[i][j] = self.eta(y[j], e[i])
    #    for i in range(len(e)):
    #        fig = plt.figure(figsize = (18, 12))
    #        plt.plot(y, b[i])
    #        plt.title(r'$\eta=\frac{F_{\nu}(E/(1-y),x=0)}{F_{\nu}(E,x=0)\cdot (1-y)}$ for $E_{\nu}$ = ' + str('{:1.1e}'.format(e[i])), fontsize = 14)
    #        plt.xlabel('y', fontsize = 15)
    #        plt.ylabel(r'$\eta(y,E)$', fontsize = 15)
    #        plt.xscale('log')
    #        plt.yscale('log')
    #        plt.savefig('eta' + str('{:1.1e}'.format(e[i])) + '.png')
    #        plt.show()
    #        plt.close()
    
    @vegas.batchintegrand
    def Z_0_int(self,xx):
        i = int(round(self.n_e/(self.e_up_l - self.e_low_l)*(np.log10(self.E) - self.e_low_l)))
        a = self.eta(xx[:,0],self.E)*self.f[i](xx[:,0])
        return a

    def Z_0(self, E):
        tt = t.time()
        self.set_E(E)
        integ = vegas.Integrator([[0.0,1.]], nhcube_batch = 2000, sync_ran =False)
        result = integ(self.Z_0_int, nitn = 10) 
        print( result.mean, t.time() - tt)
        return result.mean 
        
    def plot_Z_0(self):
        fig = plt.figure(figsize = (18, 12))
        e = np.logspace(1, 10, num = 300)
        z = np.zeros(len(e))
        for i in range(len(e)):
            z[i] = self.Z_0(e[i])
        plt.plot(e, z)
        plt.title(r'$Z_{\nu}(x=0,E)$', fontsize = 14)
        plt.xlabel(r'$E_{\nu}$', fontsize = 15)
        plt.xscale('log')
        plt.yscale('log')
        plt.savefig('Z(x=0,E).png')
        plt.show()



    def lam_minus_1(self, E):
        return glb.N_A*(self.s_p.fcc(E)*self.ratio+self.s_n.fcc(E))/(1+self.ratio)

 #   def plam_minus_1(self, E, r):
  #      return (s.fp(E) + r*(s.fn(E) - s.fp(E)))


    def plot_lam_minus_1(self):
        fig = plt.figure(figsize = (18, 12))
        e = np.logspace(1,20,num=10000)
        z = np.zeros(len(e))
        z1 = np.zeros(len(e))
        z2 = np.zeros(len(e))
        z3 = np.zeros(len(e))
        z4 = np.zeros(len(e))
        z5 = np.zeros(len(e))
        for i in range(len(e)):
            z[i] = (self.lam_minus_1(e[i]))
        plt.plot(e, z)
        plt.title(r'Total xsec of  neutrino scattering on nucleon', fontsize = 14)
        plt.xlabel(r'$E_{\nu}$, GeV', fontsize = 15)
        plt.ylabel(r'$\sigma(E)$, $cm^{2}$', fontsize = 15)
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True)
        plt.legend()
        plt.savefig('sigma(E).png')
        plt.show()

    def D_nu(self, E, y):
        #print('mom',E,y,E/(1.-y))
        return self.lam_minus_1(E/(1. - y)) - self.lam_minus_1(E)




    def plot_D_nu(self):
        e = np.logspace(1, 14, num = 14)
        y = np.logspace(-11, 0, num = 1000)
        b = np.zeros([len(e), len(y)])
        for i in range(len(e)):
            for j in range(len(y)):
                b[i][j] = self.D_nu(e[i], y[j])
        for i in range(len(e)):
            fig = plt.figure(figsize = (18, 12))
            plt.plot(y, b[i])
            plt.title(r'$D(E,y)$ for $E_{\nu}$ = ' + str('{:1.1e}'.format(e[i])), fontsize = 14)
            plt.xlabel('y', fontsize = 15)
            plt.ylabel(r'$D(E,y)$, $cm^{-2}$', fontsize = 15)
            plt.xscale('log')
            plt.yscale('log')
            plt.savefig('D(E,y)' + str('{:1.1e}'.format(e[i])) + '.png')
            plt.show()
            plt.close()

    @vegas.batchintegrand
    def Z_1_int(self,  xx):
        i = int(round(self.n_e/(self.e_up_l - self.e_low_l)*(np.log10(self.E) - self.e_low_l)))
        return self.eta(xx[:,0], self.E)*self.f[i](xx[:,0])*(1 - np.exp(-self.x*self.D_nu(self.E, xx[:,0])))/(self.x*self.D_nu(self.E, xx[:,0]))


    def Z_1(self, E, x):
        tt = t.time()
        self.set_E(E)
        self.set_x(x)
        integ1 = vegas.Integrator([[0.0,1.-self.E/10**(20)]], nhcube_batch = 2000, sync_ran =False)
        result = integ1(self.Z_1_int, nitn = 10)
        print(E, t.time() - tt)
        return result.mean 

    def plot_Z_1(self):
        e = np.logspace(1, 8, num = 800)
        x1 = np.logspace(0, 11, num = 12)
        x = np.zeros(len(x1) + 1)
        x[0] = 0
        for i in range(len(x1)):
            x[i+1] = x1[i]    
        b = np.zeros([len(e), len(x)])
        for i in range(len(e)):
            for j in range(len(x)):
                if j == 0: b[i][j] = self.Z_0(e[i])
                else: b[i][j] = self.Z_1(e[i], x[j])
                print(i, j)
        fil=open('z_factor_'+str(self.model)+'_'+str(self.nupdg)+'.dat', 'w')
        for i in range(len(e)):
            for j in range(len(x)):
                fil.write(str(e[i]) + '\t' + str(x[j]) + '\t' + str(b[i][j]) + '\n')
        fil.close()
        fig = plt.figure(figsize = (18, 12))
        for j in range(len(x)):
            plt.plot(e, b[:, j], label = '$x$ = ' + str('{:1.1e}'.format(x[j])) + r' $ g/cm^2$')
        plt.title(r' = Z-factor', fontsize = 14)
        plt.xlabel('E, GeV', fontsize = 15)
        plt.ylabel(r'$Z_1(E,x)$', fontsize = 15)
        plt.xscale('log')
        #plt.yscale('log')
        #plt.xlim(10, 10.**10)
        plt.grid(True)
        plt.legend()
        plt.savefig('Z_1(E,x)'+str(self.model)+'_'+str(self.nupdg)+'_'+str(x[j])+'.png')
        plt.show()
        plt.close()
        return e, b



a = reg()
#a.plot_Z_0()
#a.plot_data()
#a.plot_D_nu()
a.plot_Z_1()

