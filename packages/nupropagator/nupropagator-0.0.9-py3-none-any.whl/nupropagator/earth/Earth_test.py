import Earth as E
import numpy as np
import Global as g
import matplotlib.pyplot as plt
import FinVtx as fin
N = 100
epsrel = 10**(-3)
e=E.Earth(1,'PREM')
v1 = fin.FinVtx(0,0,g.R_E)
v2 = fin.FinVtx(0,0,-g.R_E)
v11 = np.array([0,0,g.R_E])
v22 = np.array([0,0,-g.R_E])
tt1 = np.zeros(N)
tt2 = np.zeros(N)
tt3 = np.zeros(N)
res1 = np.zeros(N)
res2 = np.zeros(N)
res3 = np.zeros(N)
res4 = np.zeros(N)
cc = np.zeros(N)
res_th = 1.09*10**10
for i in range(N):
    res1[i],tt1[i] = e.column_depth(v1,v2,1000)

for i in range(N):
    res2[i],cc[i],tt2[i] = e.column_depth_quad(v11,v22,10**(-3))

for i in range(N):
    res3[i],cc[i],tt3[i] = e.column_depth_vegas(v11,v22,10**(-3))
print('time',tt1.mean(),tt2.mean(),tt3.mean())
print('reldif',res1.mean()/res_th-1,res2.mean()/res_th-1,res3.mean()/res_th-1)
print(res2/res_th-1)
fig=plt.figure(figsize = (18,12))
plt.hist(res1/res_th-1,1000,range = [0.002,0.005],label='rect, time = '+str(tt1.mean())+r'$\pm$'+str(tt1.std()))
plt.hist(res2/res_th-1,1000,range = [0.002,0.005],label='quad, time = '+str(tt2.mean())+r'$\pm$'+str(tt2.std()))
plt.hist(res3/res_th-1,1000,range = [0.002,0.005],label='vegas, time = '+str(tt3.mean())+r'$\pm$'+str(tt3.std()))
plt.title('Integral difference')
plt.xlabel(r'density, $g/cm^3$')
plt.xlim(0,0.005)
plt.legend()
plt.grid(True)
plt.show()

fig.savefig('earth_test.png')

