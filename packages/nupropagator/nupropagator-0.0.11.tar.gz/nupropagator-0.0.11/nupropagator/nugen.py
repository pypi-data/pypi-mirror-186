import numpy as np
from nupropagator.cross_section import cross as cs
from nupropagator.cross_section import cross_ground as cg
from nudisxs.disxs import *
from scipy.spatial.transform import Rotation as R

class NuGen:
    def __init__(self):
        self.nu_energy_GeV = 0.
        self.nu_direction  = [0.,0.,1.]
        self.target        = -1 # not possible value. must be configured
        self.current = {-1: 'nc', 1: 'cc'}
        self.cs_p = cs.Cross_section(self.pdf_model,14,2212)
        self.cs_n = cs.Cross_section(self.pdf_model,14,2112)
        self.cross_ground_p_NC = cg.cross_ground(self.pdf_model,'nc',self.nu_pdg,2212)
        self.cross_ground_n_NC = cg.cross_ground(self.pdf_model,'nc',self.nu_pdg,2112)
        self.cross_ground_p_CC = cg.cross_ground(self.pdf_model,'cc',self.nu_pdg,2212)
        self.cross_ground_n_CC = cg.cross_ground(self.pdf_model,'cc',self.nu_pdg,2112)
        self.cross_ground = {(1,2112): self.cross_ground_n_CC.f, (1,2212): self.cross_ground_p_CC.f,
                 (-1,2112): self.cross_ground_n_NC.f, (-1,2212): self.cross_ground_p_NC.f}
        self.xsec_xy = {1: self.dis.xs_cc, -1: self.dis.xs_nc}

    def configure(self,opts):
        self.configure_simulation_mode(opts)
        self.configure_neutrino(opts)
        self.configure_target(opts)
        import logging
        self.log = logging.getLogger('nupropagator.NuGen')
        self.log.info(f'neutrino energy mode={self.nu_energy_mode}')
        self.log.info(f'neutrino direction mode={self.nu_direction_mode}')
        self.log.info(f'target mode={self.target_mode}')
        self.log.info(f'neutrino pdg ={self.nu_pdg}')

    def configure_simulation_mode(self,opts):
        self.nu_energy_mode = opts.neutrinoPrimary_energy_mode
        self.nu_direction_mode = opts.neutrinoPrimary_direction_mode
        self.target_mode = opts.neutrinoPrimary_target_mode
        self.current_mode = opts.neutrinoPrimary_current_mode

    def configure_neutrino(self,opts):
        self.nu_pdg = opts.neutrinoPrimary_pdgid
        if self.nu_energy_mode != 'random':
            self.nu_energy_GeV = opts.neutrinoPrimary_energy_GeV
        if self.nu_direction_mode != 'random':
            self.nu_direction = opts.neutrinoPrimary_direction

    def configure_target(self,opts):#FIXME
        self.pdf_model = opts.neutrinoPrimary_pdf_model
        self.dis = disxs()
        self.dis.init_pdf(self.pdf_model)
        if self.target_mode != 'random':
            self.target = opts.neutrinoPrimary_target

    def get_neutrino_direction(self):#FIXME
        if self.nu_direction_mode == 'random':
            nu_phi = 2*np.pi*np.random.random()
            nu_cos = 2*np.random.random()-1
            nu_sin = (1-nu_cos**2)**0.5
        else:
            nu_phi = np.arctan2(self.nu_direction[1],self.nu_direction[0])
            nu_cos = self.nu_direction[2]
            nu_sin = np.sqrt(self.nu_direction[0]**2+self.nu_direction[1])

        return nu_cos, nu_sin, nu_phi

    def get_neutrino_energy(self):
        if self.nu_energy_mode != 'random':
            return self.nu_energy_GeV
        else:
            # select random
            return self.nu_energy_GeV # FIX')

    def get_target(self):
        # get nucleon FIXME. Should be more generic: not only for water
        if self.target_mode == 'random':
            a = np.random.random()
            if a<=4./9:
                self.target = 2112
                self.dis.init_target('neutron')
            else:
                self.target = 2212
                self.dis.init_target('proton')

    def get_current(self):# FIXME
        if self.current_mode == 'random':
            a = np.random.random()
            if self.target == 2212:
                mode = np.int_(a <= self.cs_p.ratio_nc(self.nu_energy_GeV))*(-1)
                mode = mode + np.int_(a> self.cs_p.ratio_nc(self.nu_energy_GeV))*1
            if self.target == 2112:
                mode = np.int_(a <= self.cs_n.ratio_nc(self.nu_energy_GeV))*(-1)
                mode = mode + np.int_(a> self.cs_n.ratio_nc(self.nu_energy_GeV))*1
        else:
            mode = 0
        return mode

    def get_xy_Bjorken_old(self,mode):
        x=y=-1.0 # impossible values
        self.dis.init_current(current[mode])
        
        def get_random(x,y,crossing,diff_xsec_xy):
            c =  crossing(self.nu_energy_GeV)*np.random.random()
            xsec = diff_xsec_xy(self.nu_energy_GeV,x,y)
            if(c-xsec >= 0): 
              return true 

        while(True):
            x = np.random.random()
            y = np.random.random()
            if get_random(x,y,self.cross[(self.current,self.target)],self.xsec_xy[self.current]):
               break 
        return x,y

    def get_xy_Bjorken_new(self,mode):#FIXME
        x = []
        y = []
        weight = []
        integ = inregrand_2dxy()
        integ.dis.init_neutrino(self.nu_pdg)
        integ.dis.current(self.current)
        integ.dis.init_target(self.target)
        integ.calculate(self.nu_energy_GeV)
        for Bj,wgt in integ.integrator.random():
            x.append(Bj[0])
            y.append(Bj[1])
            weight.append(wgt)
        x = np.array(x)
        y = np.array(y)
        weight = np.array(weight)
        xsection = np.zeros(len(x))
        xsection = integ.dis.xsdis_as_array(self.nu_energy_GeV,x,y)
        return np.array(x),np.array(y),np.array(weight),np.array(xsection)
    '''
    def get_xy_Bjorken_grond_algo(self,mode):
        x=y=-1.0 # impossible values
        while(True):
            x = np.random.random()
            y = np.random.random()
            if mode == -1:
                self.dis.init_current('nc')
                rn_p_NC =  self.cross_ground_p_NC.f(self.nu_energy_GeV)*np.random.random()
                rn_n_NC =  self.cross_ground_n_NC.f(self.nu_energy_GeV)*np.random.random()
                rn_NC = rn_p_NC*np.int_(self.target == 2212) + rn_n_NC*np.int_(self.target == 2112)
                xsec = self.dis.xs_nc(self.nu_energy_GeV,x,y)
                if(rn_NC-xsec >= 0): break
            if mode == 1:
                self.dis.init_current('cc')
                rn_p_CC =  self.cross_ground_p_CC.f(self.nu_energy_GeV)*np.random.random()
                rn_n_CC =  self.cross_ground_n_CC.f(self.nu_energy_GeV)*np.random.random()
                xsec = self.dis.xs_cc(self.nu_energy_GeV,x,y)
                rn_CC = rn_p_CC*np.int_(self.target == 2212) + rn_n_CC*np.int_(self.target == 2112)
                if(rn_CC-xsec >= 0):
                    break
        return x,y
    '''
    def get_particles_momenta(self,x, y, nu_cos, nu_sin, nu_phi):#FIXME
        self.dis.dis_kinematics(self.nu_energy_GeV,x,y)
        t = np.array([0,0,nu_phi])
        t1 = np.array([0,np.arccos(nu_cos),0])
        r = R.from_rotvec(t.T)
        r1 = R.from_rotvec(t1.T)
        self.dis.particles[0]['Px_GeV'],self.dis.particles[0]['Py_GeV'],self.dis.particles[0]['Pz_GeV'] = r.apply(r1.apply(np.array([self.dis.particles[0]['Px_GeV'],self.dis.particles[0]['Py_GeV'],self.dis.particles[0]['Pz_GeV']])))
        self.dis.particles[1]['Px_GeV'],self.dis.particles[1]['Py_GeV'],self.dis.particles[1]['Pz_GeV'] = np.array([self.nu_energy_GeV*np.cos(nu_phi)*nu_sin-self.dis.particles[0]['Px_GeV'],self.nu_energy_GeV*np.sin(nu_phi)*nu_sin-self.dis.particles[0]['Py_GeV'],self.nu_energy_GeV*nu_cos-self.dis.particles[0]['Pz_GeV']])
        final_lepton = [self.dis.particles[0]['pdgid'],self.dis.particles[0]['Px_GeV'],self.dis.particles[0]['Py_GeV'],self.dis.particles[0]['Pz_GeV'],self.dis.particles[0]['E_GeV']]
        final_nucleon = [self.dis.particles[1]['pdgid'],self.dis.particles[1]['Px_GeV'],self.dis.particles[1]['Py_GeV'],self.dis.particles[1]['Pz_GeV'],self.dis.particles[1]['E_GeV']]
        return final_lepton,final_nucleon

    def get_event(self):
        # get neutrino energy
        self.dis.init_neutrino(self.nu_pdg)
        nu_cos, nu_sin, nu_phi = self.get_neutrino_direction()
        nu_energy = self.get_neutrino_energy()
        self.get_target()
        mode = self.get_current()
        x,y = self.get_xy_Bjorken(mode)
        return self.get_particles_momenta(x, y, nu_cos, nu_sin, nu_phi)

    def get_event_fix_en(self):
        self.dis.init_neutrino(self.nu_pdg)
        nu_cos, nu_sin, nu_phi = self.get_neutrino_direction()
        nu_energy = self.get_neutrino_energy()
        self.get_target()
        mode = self.get_current()
        x,y,weight = self.get_xy_Bjorken_fix_en(mode)
        return self.get_particles_momenta(x, y, nu_cos, nu_sin, nu_phi)

    def next(self):
        return self.get_event()
