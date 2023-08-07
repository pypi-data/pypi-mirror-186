import numpy as np
import Global as g
import FinVtx as fin
import scipy.integrate as sc
import quadpy
import vegas 
integ = vegas.Integrator([[0.0,1]], nhcube_batch = 2000, sync_ran =False)
class Earth:
    def __init__(self,n,model_name):
        self.n=n
        self.x=np.zeros(n)
        self.d=np.zeros(n)
        self.model_name=model_name
    
    def get_density(self,r,model_name):
        d = 0
        if self.model_name=='PREM':
            x=r*g.m/float(g.R_E)
            d = np.piecewise(x, [r< 0, (r >= 0*g.m) & (r<1221500*g.m),(1221500*g.m<=r) & (r<3480000*g.m),
                (3480000*g.m<=r) & (r<5701000*g.m), (5701000*g.m<=r) & (r<5771000*g.m),
                (5771000*g.m<=r) & (r<5971000*g.m), (5971000*g.m<=r) & (r<6151000*g.m), 
                (6151000*g.m<=r) & (r<6346600*g.m), (6346600*g.m<=r) & (r<6356000*g.m),
                (6356000*g.m<=r) & (r<6358000*g.m),(6368000*g.m<=r) & (r<=g.R_E), r>g.R_E  ], 
                [0, lambda x: (13.0885 - 8.8381*x*x), lambda x: (12.5815 - x*(1.2638 + x*(3.6426 + x*5.5281))),
                    lambda x: (7.9565 - x*(6.4761 - x*(5.5283 - x*3.0807))), 
                    lambda x: (5.3197 - 1.4836*x), lambda x: (11.2494 - 8.0298*x), 
                    lambda x: (7.1089 - 3.8045*x), lambda x: (2.691 + 0.6924*x), 2.9, 2.6,1.02,0 ])
        return d*g.m/g.cm

    '''
    def get_density(self,r,model_name):
        d = 0
        if self.model_name=='PREM':
            x=self.x
            d=self.d
            x=r*g.m/float(g.R_E)
            d=0*np.int_(r<0)
            d=d+np.int_(np.logical_and(0*g.m<=r,r<1221500*g.m))*(13.0885 - 8.8381*x*x) #+
            d=d+np.int_(np.logical_and(1221500*g.m<=r,r<3480000*g.m))*(12.5815 - x*(1.2638 + x*(3.6426 + x*5.5281))) #+
            d=d+np.int_(np.logical_and(3480000*g.m<=r,r<5701000*g.m))*(7.9565 - x*(6.4761 - x*(5.5283 - x*3.0807))) #+
            d=d+np.int_(np.logical_and(5701000*g.m<=r,r<5771000*g.m))*(5.3197 - 1.4836*x)#+
            d=d+np.int_(np.logical_and(5771000*g.m<=r,r<5971000*g.m))*(11.2494 - 8.0298*x) #+
            d=d+np.int_(np.logical_and(5971000*g.m<=r,r<6151000*g.m))*(7.1089 - 3.8045*x) #+
            d=d+np.int_(np.logical_and(6151000*g.m<=r,r<6346600*g.m))*(2.691 + 0.6924*x) #+
            d=d+np.int_(np.logical_and(6346600*g.m<=r,r<6356000*g.m))*(2.9) #+
            d=d+np.int_(np.logical_and(6356000*g.m<=r,r<6358000*g.m))*(2.6)
            d=d+np.int_(np.logical_and(6368000*g.m<=r,r<=g.R_E))*1.02
            d=d+0*np.int_(np.logical_and(g.R_E<r,r<=g.R_A))
            d=d+0*np.int_(r>=g.R_A)
        else:
            print(str(model_name)+' is unknown')
            
        return d*g.m/g.cm
        #return d
   
    '''
    @vegas.batchintegrand
    def get_density_vegas(self,xx):
        dim = np.shape(xx)[0]
        r = (np.sum((np.tile(self.v1,(dim,1)).T+np.tile(self.na,(dim,1)).T*xx[:,0])**2, axis = 0))**0.5
        #x=self.x
        #d=self.d
        d = 0
        if self.model_name=='PREM':
            x=r*g.m/float(g.R_E)
            d = np.piecewise(x, [r< 0, (r >= 0*g.m) & (r<1221500*g.m),(1221500*g.m<=r) & (r<3480000*g.m),
                (3480000*g.m<=r) & (r<5701000*g.m), (5701000*g.m<=r) & (r<5771000*g.m),
                (5771000*g.m<=r) & (r<5971000*g.m), (5971000*g.m<=r) & (r<6151000*g.m),
                (6151000*g.m<=r) & (r<6346600*g.m), (6346600*g.m<=r) & (r<6356000*g.m),
                (6356000*g.m<=r) & (r<6358000*g.m),(6368000*g.m<=r) & (r<=g.R_E), r>g.R_E  ],
                [0, lambda x: (13.0885 - 8.8381*x*x), lambda x: (12.5815 - x*(1.2638 + x*(3.6426 + x*5.5281))),
                    lambda x: (7.9565 - x*(6.4761 - x*(5.5283 - x*3.0807))),
                    lambda x: (5.3197 - 1.4836*x), lambda x: (11.2494 - 8.0298*x),
                    lambda x: (7.1089 - 3.8045*x), lambda x: (2.691 + 0.6924*x), 2.9, 2.6,1.02,0 ])
        return d*g.m/g.cm

    
    def column_depth(self,v1,v2,N): #rectangular method
        import time
        tt = time.time()
        depth = 0
        x_start=v1
        n=v2-v1
        n.div(float(N))
        for i in range(0,N+1,1):
            depth = depth + n.mag()*self.get_density((x_start+n.div_f(float(2))).mag(),self.model_name)
            #print('asdasda',n.mag(),x_start,depth,self.get_density((x_start+n.div_f(float(2))).mag(),self.model_name))
            x_start=x_start+n
        tt = time.time()-tt
        return depth, tt
    
    def column_depth_quad(self,v1,v2,eps):
        import time
        tt = time.time()
        depth=np.zeros(self.n)
        n=v2-v1
        n_mag = np.sqrt(n[0]**2+n[1]**2+n[2]**2) 
        a = sc.quad(lambda t: g.m*self.get_density(np.sqrt(((v1+n*t)**2).sum()),'PREM')*n_mag,0,1,epsabs= eps)
        tt = time.time()-tt
        return a[0],a[1],tt

    def column_depth_vegas(self,v1,v2,eps):
        import time
        tt = time.time()
        depth=np.zeros(self.n)
        n=v2-v1
        n_mag = np.sqrt(n[0]**2+n[1]**2+n[2]**2)
        self.na = n
        self.v1 = v1
        result = integ(self.get_density_vegas, nitn = 10)
        tt = time.time()-tt
        return n_mag*result.mean,result.sdev/result.mean,tt
        
        
