import numpy as np
from nudisxs.disxs import *
import time as t
import matplotlib.pyplot as plt

def finetine_plt()-> None:
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['savefig.dpi'] = 300

def plot_xsec_vs_enu(enu,xsec)->None:
    finetine_plt()
    fig, axs = plt.subplots(1, 1)
    plt.plot(enu,xsec)
    fig.supxlabel(r'$\bf{E_\nu}$, [GeV]', weight="bold")
    fig.supylabel(r'$\bf{\sigma}$')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('xs_vs_enu.pdf')

def main():
    dis = disxs()
    dis.init_pdf(name = 'nCTEQ15_208_82')
    dis.init_current('cc')
    enu = np.logspace(1,20,1000)
    tot =  np.zeros_like(enu)
    for ie,e in enumerate(enu):
        tot[ie] = dis.calculate_total(e)
    plot_xsec_vs_enu(enu,tot)


def calc_xs(ne, model = 'CT10nlo', nupdg = 16):
    dis = disxs()
    dis.init_pdf(name = model)
    dis.init_neutrino(pdg=nupdg)
    e = np.logspace(1, 20, num = ne)
    x = np.zeros(ne)
    nc_n = np.zeros(ne)
    nc_n_max = np.zeros(ne)
    cc_n = np.zeros(ne)
    cc_n_max = np.zeros(ne)
    nc_p = np.zeros(ne)
    nc_p_max = np.zeros(ne)
    cc_p = np.zeros(ne)
    cc_p_max = np.zeros(ne)

    dis.init_target('proton')
    dis.init_current('cc')
    for i in range(ne):
        tt = t.time()
        cc_p[i] = dis.calculate_total(e[i])
        w = []
        for x,wgt in dis.integrator.random():
            w.append(dis.xs_cc(e[i],x[0],x[1]))
        cc_p_max[i] = (np.array(w)).max()
        print('p  CC ', i, t.time() - tt)
    fil11 = open(str(model)+'_2212_'+str(nupdg)+'_cc.dat', 'w')
    fil12 = open(str(model)+'_2212_'+str(nupdg)+'_cc_max.dat', 'w')
    for i in range(ne):
        fil11.write(str(e[i]) + '\t' + str(cc_p[i]) + '\n')
        fil12.write(str(e[i]) + '\t' + str(cc_p_max[i]) + '\n')
    fil11.close()
    fil12.close()

    dis.init_target('neutron')
    for i in range(ne):
        tt = t.time()
        cc_n[i] = dis.calculate_total(e[i])
        w = []
        for x,wgt in dis.integrator.random():
            w.append(dis.xs_cc(e[i],x[0],x[1]))
        cc_n_max[i] = (np.array(w)).max()
        print('n  CC ', i, t.time() - tt)
    fil21 = open(str(model)+'_2112_'+str(nupdg)+'_cc.dat', 'w')
    fil22 = open(str(model)+'_2112_'+str(nupdg)+'_cc_max.dat', 'w')
    for i in range(ne):
        fil21.write(str(e[i]) + '\t' + str(cc_n[i]) + '\n')
        fil22.write(str(e[i]) + '\t' + str(cc_n_max[i]) + '\n')
    fil21.close()
    fil22.close()

    dis.init_target('proton')
    dis.init_current('nc')
    for i in range(ne):
        tt = t.time()
        nc_p[i] = dis.calculate_total(e[i])
        w = []
        for x,wgt in dis.integrator.random():
            w.append(dis.xs_nc(e[i],x[0],x[1]))
        nc_p_max[i] = (np.array(w)).max()
        print('p  NC ', i, t.time() - tt)
    fil31 = open(str(model)+'_2212_'+str(nupdg)+'_nc.dat', 'w')
    fil32 = open(str(model)+'_2212_'+str(nupdg)+'_nc_max.dat', 'w')
    for i in range(ne):
        fil31.write(str(e[i]) + '\t' + str(nc_p[i]) + '\n')
        fil32.write(str(e[i]) + '\t' + str(nc_p_max[i]) + '\n')
    fil31.close()
    fil32.close()

    dis.init_target('neutron')
    for i in range(ne):
        tt = t.time()
        nc_n[i] = dis.calculate_total(e[i])
        w = []
        for x,wgt in dis.integrator.random():
            w.append(dis.xs_nc(e[i],x[0],x[1]))
        nc_n_max[i] = (np.array(w)).max()
        print('n  NC ', i, t.time() - tt)
    fil41 = open(str(model)+'_2112_'+str(nupdg)+'_nc.dat', 'w')
    fil42 = open(str(model)+'_2112_'+str(nupdg)+'_nc_max.dat', 'w')
    for i in range(ne):
        fil41.write(str(e[i]) + '\t' + str(nc_n[i]) + '\n')
        fil42.write(str(e[i]) + '\t' + str(nc_n_max[i]) + '\n')
    fil41.close()
    fil42.close()
   
calc_xs(200)
