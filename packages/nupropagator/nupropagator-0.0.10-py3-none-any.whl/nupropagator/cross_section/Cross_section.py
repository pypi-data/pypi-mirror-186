import pandas as pd
import math as m
import numpy as np
from scipy.interpolate import interp1d

class Cross_section:
    def __init__(self,energy,flavor,string='cc'):
        self.df = pd.read_csv('cross/mysec_'+str(string)+'_nu'+str(int((1-m.fabs(flavor)/flavor)/2)*'bar')+'_cteq5.dat', sep='\t', engine='python', header=None,names=['energy','cross_section'])
        self.f=interp1d(np.array(self.df['energy']),np.array(self.df['cross_section']),kind='cubic')
        
    def get_point_energy(self):
        return 10**(np.array(self.df['energy']))
    
    def get_point_section(self):
        return np.array(self.df['cross_section'])
    
    def cross_section(self,energy):
        return(self.f(np.log10(energy)))
