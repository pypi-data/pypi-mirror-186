import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import time as t

class cross_ground:
    def __init__(self,model,mode,pdg,target):
        import importlib
        path = importlib.util.find_spec('nupropagator').submodule_search_locations[0]
        import logging
        self.log = logging.getLogger('nupropagator.cross_ground')
        self.log.debug(f'cross_ground path={path}')
        self.cross_lim=pd.read_csv(path+'/cross_section/'+str(model)+'_'+str(target)+'_'+str(pdg)+'_'+str(mode)+'_max.dat',sep='\t', engine='python', header=None,names=['energy','max'])
        self.energy = np.array(self.cross_lim['energy'])
        self.max = np.array(self.cross_lim['max'])
        self.f = interp1d(self.energy, self.max, kind='cubic')
