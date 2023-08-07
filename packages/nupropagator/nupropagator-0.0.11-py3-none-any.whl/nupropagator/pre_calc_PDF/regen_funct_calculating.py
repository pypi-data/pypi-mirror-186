import cross_section.cross as cs
import numpy as np
import time as time
from scipy.integrate import*
import vegas as vegas
import nudisxs.integrand_1dx as i1x
from nudisxs.disxs import *


#def crossy(c):
#    b=quad(lambda x: crossxy(energy,np.exp(x),y,c)*np.exp(x),np.log(dis.xl(energy)[0]),np.log(dis.xl(energy)[1]),epsrel=eps)
    #if b[0]<0:
    #    return 0
    #else:
    #    return b[0]*normfactor





def calc_regfun(ne,ny,y_low,y_up,ratio, nupdg=16,model = 'CT10nlo'):
    #dis = disxs()
    integ = i1x.integrand_1dx()
    integ.dis.init_pdf(name = model)
    integ.dis.init_neutrino(pdg=nupdg)
    integ.init_vegas_integrator()
    e_low=10
    s_p=cs.Cross_section(model,nupdg,2212)
    s_n=cs.Cross_section(model,nupdg,2112)
    e_up=10.**(14)
    funreg=np.zeros([ne,2*ny])
    fullcross_n=np.zeros(ne)
    fullcross_p=np.zeros(ne)
    ycross_n=np.zeros([ne,2*ny])
    ycross_p=np.zeros([ne,2*ny])
    e=np.logspace(np.log10(e_low),np.log10(e_up),num=ne)
    y=np.logspace(np.log10(y_low),-1,num=ny)
    y1=np.linspace(0.11,y_up,num=ny)
    fullcross_p=s_p.ff(e)
    integ.dis.init_current('nc')
    integ.dis.init_target('proton')
    for i in range(ne):
        tt  = time.time()
        for j in range(2*ny):
            if j<ny:
                ycross_p[i][j]=integ.calculate(e[i]/(1-y[j]),y[j])
            else:
                ycross_p[i][j]=integ.calculate(e[i]/(1-y1[j-ny]),y1[j-ny])
        print('p ',i,time.time()-tt)

    integ.dis.init_target('neutron')
    for i in range(ne):
        tt  = time.time()
        for j in range(2*ny):
            if j<ny:
                ycross_n[i][j]=integ.calculate(e[i]/(1-y[j]),y[j])
            else:
                ycross_n[i][j]=integ.calculate(e[i]/(1-y1[j-ny]),y1[j-ny])
        print('n ',i,time.time()-tt)
    fullcross_n=s_n.ff(e)
        
    for i in range(ne):
        for j in range(2*ny):
            funreg[i][j]=(ratio*ycross_p[i][j]+ycross_n[i][j])/(ratio*fullcross_p[i]+fullcross_n[i])

    fil=open('regfun_'+str(model)+'_'+str(nupdg)+'_'+str(ratio)+'.dat','w')
    for i in range(ne):
        for j in range(2*ny):
            if j<ny:
                fil.write(str(e[i])+'\t'+str(y[j])+'\t'+str(funreg[i][j])+'\n')
            else:
                fil.write(str(e[i])+'\t'+str(y1[j-ny])+'\t'+str(funreg[i][j])+'\n')

    fil.close()



calc_regfun(300,200,10**(-16),0.999999999,1.2)
