import pandas as pd
#import nupropagator.Global.Global as g
import math as m
import numpy as np
from scipy.interpolate import interp1d
f1=[i for i in range(1,38)]
class Cross_section:
    def __init__(self,model='CT10nlo',pdg=14,n_tt=2212):
        import importlib
        path = importlib.util.find_spec('nupropagator').submodule_search_locations[0]
        import logging
        self.log = logging.getLogger('nupropagator.Cross_section')
        self.log.debug(f'Cross_section path={path}')
        self.crossnc=pd.read_csv(path+'/cross_section/'+str(model)+'_'+str(n_tt)+'_'+str(pdg)+'_nc.dat',sep='\t', engine='python', header = None,names=['E','mean'])
        self.a=0
        self.crosscc=pd.read_csv(path+'/cross_section/'+str(model)+'_'+str(n_tt)+'_'+str(pdg)+'_cc.dat',sep='\t', engine='python', header = None, names=['E','mean'])
        self.e_max=(self.crosscc['E']).max()
        self.fcc=interp1d(np.array(self.crosscc['E']),self.crosscc['mean'],kind='cubic')
        print(self.crossnc['E'])
        self.fnc=interp1d(np.array(self.crossnc['E']),self.crossnc['mean'],kind='cubic')
        self.a=self.fcc
        self.ff=interp1d(np.array(self.crosscc['E']),self.crosscc['mean']+self.crossnc['mean'],kind='cubic')


    def get_point_energy(self):
        return np.array(self.crosscc[0])

    def get_point_sectioncc(self):
        return np.array(self.crosscc[1])

    def cross_sectioncc(self,energy):
        return (self.fcc(energy))

    def ratio_nc(self,energy):
        return self.fnc(energy)/(self.fcc(energy)+self.fnc(energy))

    def get_point_sectionnc(self):
        return np.array(self.crossnc[1])

    def cross_sectionnc(self,energy):
        return (self.fnc(energy))

    def tot(self,energy):
        return (self.fnc(energy)+self.fcc(energy))*g.cm**2

#    def tot1(self,energy):
#        if  energy<0. or
#        return (self.fnc(energy)+self.fcc(energy))


class C_s:
    def __init__(self):
        self.crossp=pd.read_csv('C10nlo_2212_14_cc.dat',sep='\t', engine='python', header=None)
        self.crossn=pd.read_csv('C10nlo_2112_14_cc.dat',sep='\t', engine='python', header=None)
        e=self.crossp[0]
        self.e_max=e.max()
        self.fp=interp1d(e,self.crossp[1],kind='cubic')
        self.fn=interp1d(e,self.crossn[1],kind='cubic')
        self.ff=interp1d(e,self.crossn[1]+self.crossp[1],kind='cubic')

class C_s1:
    def __init__(self):
        self.crossp=pd.read_csv('cross/mysec_cc_nu_cteq5.dat',sep='\t', engine='python', header=None)
        self.crossn=pd.read_csv('cross/mysec_cc_nu_cteq5.dat',sep='\t', engine='python', header=None)
        e=self.crossp[0]
        self.fp=interp1d(10**e,self.crossp[1],kind='cubic')
        self.fn=interp1d(10**e,self.crossn[1],kind='cubic')
        self.ff=interp1d(10**e,self.crossn[1]+self.crossp[1],kind='cubic')
