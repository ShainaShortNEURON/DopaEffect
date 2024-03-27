### Using DOPA effect as BL since this appears to be a normal healthy DA response SMS 15FEB2024
import os
from netpyne import specs

from __main__ import cfg
Dt = cfg.dt
Tfinal = cfg.duration

# Create a folder to save the results if it doesn't exist
results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

### Set variables for Individul Patient Loop

## equations designed as % changes from baseline = 1

## Variables below should increase at similar rates as a fnx of amph. mediated dopa release
Nap_pyr_soma=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Hva_pyr_soma=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Iks_pyr_soma=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Nap_pyr_bas=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Hva_pyr_bas=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Iks_pyr_bas=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Nap_pyr_trunk=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Hva_pyr_trunk=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Iks_pyr_trunk=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Hva_pyr_apical=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];
Iks_pyr_apical=[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1];

#Connecticity of the circuit should change as a fnx of different patient (ie. schizo lower synatpic connectivity)
exex=[1, 1, 1, 1, 1, 1];
exin=[1, 1, 1, 1, 1, 1];
inex=[1, 1, 1, 1, 1, 1];
exexInterAssem=[1, 1, 1, 1, 1, 1];
inin=[1, 1, 1, 1, 1, 1];

#Strength of AMPA and NMDA conductions will be altered according to Goldman-Rakic 1998 publication
AMPAgEE=[.85, .85, .85, .85, .85, .85, .85];
NMDAgEE=[.85, .85, .85, .85, .85, .85, .85];
AMPAgEE_assem=[.85, .85, .85, .85, .85, .85, .85];
NMDAgEE_assem=[.85, .85, .85, .85, .85, .85, .85];
AMPAgEI=[1.1, 1.2, 1.3, 1.3, 1.3, 1.3, 1.3];
NMDAgEI=[1.1, 1.2, 1.3, 1.3, 1.3, 1.3, 1.3];
GABAgIE=[1, 1, 1.1, 1.2, 1.3, 2, 3];
GABAgII=[1, 1, 1.1, 1.2, 1.3, 2, 3];


for patient in (0,): # ,1,2,3,4,5

        # Network parameters
        netParams = specs.NetParams()  # object of class NetParams to store the network parameters
        netParams.defaultThreshold = 0.0

        ###############################################################################
        ## Cell types
        ###############################################################################
        # Pyramidal cell
        PyrCell = {'secs':{}, 'globals': {'ko0_k_ion': 3.82, 'ki0_k_ion': 160, 'cao0_ca_ion': 2, 'cai0_ca_ion': 50e-6}}
        # soma
        PyrCell['secs']['soma'] = {'geom': {}, 'mechs': {}}
        PyrCell['secs']['soma']['geom'] = {'diam': 23, 'L': 23, 'cm': 1.2, 'Ra': 150, 'nseg': 1}
        PyrCell['secs']['soma']['mechs'] = {
            'pas': {'g': 3.33e-5, 'e': -70},
            'kdyn': {},
            'Naf': {'gnafbar': 0.086},#same
            'Nap': {'gnapbar': [0.00154*Nap_pyr_soma[patient]]},#reduced to 75% of baseline #DopaEffect
            'Hva': {'ghvabar': [0.000272*Hva_pyr_soma[patient]]},#reduced to 80% of baseline (as in original model) #DopaEffect
            'kdr': {'gkdrbar': 0.0338},#same
            'IKs': {'gKsbar': [0.000105*Iks_pyr_soma[patient]]},# reducted by 75% of baseline (50% of baseline used in original mode) #DopaEffect
            'iC': {'gkcbar': 0.0022},#same
            'cadyn': {'CAF': 385.948e-9, 'tca': 250}}#same

        # basal dendrite
        PyrCell['secs']['Bdend'] = {'geom': {}, 'mechs': {}}
        PyrCell['secs']['Bdend']['geom'] = {'diam': 16.0, 'L': 150.0, 'cm': 2.3, 'Ra': 150, 'nseg': 1}
        PyrCell['secs']['Bdend']['topol'] = {'parentSec': 'soma', 'parentX': 0, 'childX': 0}
        PyrCell['secs']['Bdend']['mechs'] = {
            'pas': {'g': 6.39e-5, 'e': -70},
            'kdyn': {},
            'Naf': {'gnafbar': 0.028},
            'Nap': {'gnapbar': [0.0007*Nap_pyr_bas[patient]]},
            'Hva': {'ghvabar': [0.00056*Hva_pyr_bas[patient]]},
            'kdr': {'gkdrbar': 0.0092},
            'IKs': {'gKsbar': [0.00018*Iks_pyr_bas[patient]]},
            'iC': {'gkcbar': 0.0038},
            'cadyn': {'CAF': 964.87e-9, 'tca': 120}}

        # apical proximal dendrite
        PyrCell['secs']['Adend_proximal'] = {'geom': {}, 'mechs': {}}
        PyrCell['secs']['Adend_proximal']['geom'] = {'diam': 2.6, 'L': 400.0, 'cm': 2.3, 'Ra': 150, 'nseg': 1}
        PyrCell['secs']['Adend_proximal']['topol'] = {'parentSec': 'soma', 'parentX': 1, 'childX': 0}
        PyrCell['secs']['Adend_proximal']['mechs'] = {
            'pas': {'g': 6.39e-5, 'e': -70},
            'kdyn': {},
            'Naf': {'gnafbar': 0.028},
            'Nap': {'gnapbar': [0.0007*Nap_pyr_trunk[patient]]},
            'Hva': {'ghvabar': [0.00056*Hva_pyr_trunk[patient]]},
            'kdr': {'gkdrbar': 0.0092},
            'IKs': {'gKsbar': [0.00018*Iks_pyr_trunk[patient]]},
            'iC': {'gkcbar': 0.0038},
            'cadyn': {'CAF': 964.87e-9, 'tca': 120}}

        # apical distal dendrite
        PyrCell['secs']['Adend_distal'] = {'geom': {}, 'mechs': {}}
        PyrCell['secs']['Adend_distal']['geom'] = {'diam': 2.6, 'L': 400.0, 'cm': 2.3, 'Ra': 150, 'nseg': 1}
        PyrCell['secs']['Adend_distal']['topol'] = {'parentSec': 'Adend_proximal', 'parentX': 1, 'childX': 0}
        PyrCell['secs']['Adend_distal']['mechs'] = {
            'pas': {'g': 6.39e-5, 'e': -70},
            'kdyn': {},
            'Naf': {'gnafbar': 0.028},
            'Hva': {'ghvabar': [0.00017*Hva_pyr_apical[patient]]},
            'kdr': {'gkdrbar': 0.0092},
            'IKs': {'gKsbar': [0.00018*Iks_pyr_apical[patient]]},
            'iC': {'gkcbar': 0.0022},
            'cadyn': {'CAF': 964.87e-9, 'tca': 80}}

        netParams.cellParams['PyrCell'] = PyrCell

        ###############################################################################
        # Inhibitory cell
        InhCell = {'secs':{}}
        # soma
        InhCell['secs']['soma'] = {'geom': {}, 'mechs': {}}
        InhCell['secs']['soma']['geom'] = {'diam': 15, 'L': 15, 'cm': 1.0, 'Ra': 150, 'nseg': 1}
        InhCell['secs']['soma']['mechs'] = {
            'pas': {'g': 1.0e-5, 'e': -68},
            'kdyn': {},
            'Naf': {'gnafbar': 0.100},
            'kdr': {'gkdrbar': 0.040}}

        # dendrite
        InhCell['secs']['dend'] = {'geom': {}, 'mechs': {}}
        InhCell['secs']['dend']['geom'] = {'diam': 10, 'L': 150, 'cm': 1.92, 'Ra': 150, 'nseg': 1}
        InhCell['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX': 1, 'childX': 0}
        InhCell['secs']['dend']['mechs'] = {
            'pas': {'g': 1.92e-5, 'e': -68},
            'kdyn': {},
            'Naf': {'gnafbar': 0.020},
            'kdr': {'gkdrbar': 0.008}}

        netParams.cellParams['InhCell'] = InhCell


        ###############################################################################
        ## Synaptic mechs
        ###############################################################################

        netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.5, 'tau2': 2.5, 'e': 0}
        netParams.synMechParams['NMDA'] = {'mod': 'Exp2SynNMDA', 'tau1': 10, 'tau2': 250.0, 'e': 0}
        netParams.synMechParams['GABA'] = {'mod': 'ExpSyn', 'tau': 1.0, 'e': -75}


        ###############################################################################
        ## Populations
        ###############################################################################
        # Structuring excitatory assemblies
        Nassemblies = 2
        Nexc = 10
        Nexc_total = Nassemblies * Nexc       # without overlap between assemblies
        for na in range(Nassemblies):
            ### Populations
            netParams.popParams['Pyr_Assembly'+str(na+1)] = {'numCells': Nexc, 'cellType': 'PyrCell'}

        # Inhibitory
        Ninh = 10                             # global inhibitory neurons 
        netParams.popParams['InhPop'] = {'numCells': Ninh, 'cellType': 'InhCell'}


        ###############################################################################
        ## Connections
        ###############################################################################
        for na in range(Nassemblies):
            ## Intra-assembly
            # pyr-to-pyr AMPA/NMDA, to basal dendrite
            netParams.connParams['PYR->PYR(intra)_AMPA/NMDA_Assembly'+str(na+1)] = {
                'preConds': {'pop': 'Pyr_Assembly'+str(na+1)}, 
                'postConds': {'pop': 'Pyr_Assembly'+str(na+1)},
                'connFunc': 'fullConn',
                'weight': [2.0e-3*AMPAgEE[patient], 0.56e-3*NMDAgEE[patient]],
                'delay': 'uniform(2,4)',
                'sec': ['Bdend','Adend_proximal'],   # synapses sampled at these regions
                'loc': 0.5,
                'synMech': ['AMPA','NMDA']}

            # pyr-to-inh AMPA/NMDA, to dendrite
            netParams.connParams['PYR->INH_AMPA/NMDA_Assembly'+str(na+1)] = {
                'preConds': {'pop': 'Pyr_Assembly'+str(na+1)}, 
                'postConds': {'pop': 'InhPop'},
                'connFunc': 'fullConn',
                'weight': [0.6*value for value in [2.0e-3*AMPAgEI[patient], 0.56e-3*NMDAgEI[patient]]],
                'delay': 'uniform(2,4)',
                'sec': 'dend',
                'loc': 0.5,
                'synMech': ['AMPA','NMDA']}
            
            # inh-to-pyr GABA, to soma
            netParams.connParams['INH->PYR_GABA_Assembly'+str(na+1)] = {
                'preConds': {'pop': 'InhPop'},
                'postConds': {'pop': 'Pyr_Assembly'+str(na+1)}, 
                'connFunc': 'fullConn',
                'weight': 7.8e-3*GABAgIE[patient],
                'delay': 'uniform(2,4)',
                'sec': 'soma',
                'loc': 0.5,
                'synMech': 'GABA'}
            
            ## Inter-assembly
            for nb in range(Nassemblies):
                if nb != na:
                    # pyr-to-pyr AMPA/NMDA, to basal dendrite
                    netParams.connParams['PYR->PYR(inter)_AMPA/NMDA_Assembly'+str(na+1)+'_to_Assembly'+str(nb+1)] = {
                        'preConds': {'pop': 'Pyr_Assembly'+str(na+1)}, 
                        'postConds': {'pop': 'Pyr_Assembly'+str(nb+1)},
                        'connFunc': 'fullConn',
                        'weight': [0.1*value for value in [2.0e-3*AMPAgEE_assem[patient], 0.56e-3*NMDAgEE_assem[patient]]],
                        'delay': 'uniform(2,4)',
                        'sec': ['Bdend','Adend_proximal'],   # synapses sampled at these regions
                        'loc': 0.5,
                        'synMech': ['AMPA','NMDA']}
                
        # inh-to-inh GABA, to soma
        netParams.connParams['INH->INH_GABA'] = {
            'preConds': {'pop': 'InhPop'},
            'postConds': {'pop': 'InhPop'}, 
            'connFunc': 'fullConn',
            'weight': 0.65e-3*GABAgII[patient],
            'delay': 'uniform(2,4)',
            'sec': 'soma',
            'loc': 0.5,
            'synMech': 'GABA'}
                    

        ###############################################################################
        ## Background stimulation
        ###############################################################################
        ### Source Stimulation - Spontaneous firing
        netParams.stimSourceParams['NetStim_PYR_exc']  = {'type': 'NetStim', 'interval': 1.0, 'start': 0, 'noise': 1, 'seed': 1}
        netParams.stimSourceParams['NetStim_PYR_exc2'] = {'type': 'NetStim', 'interval': 5.0, 'start': 0, 'noise': 1, 'seed': 2}
        netParams.stimSourceParams['NetStim_PYR_inh']  = {'type': 'NetStim', 'interval': 1.0, 'start': 0, 'noise': 1, 'seed': 3}
        netParams.stimSourceParams['NetStim_INH_exc']  = {'type': 'NetStim', 'interval': 1.0, 'start': 0, 'noise': 1, 'seed': 4}
        netParams.stimSourceParams['NetStim_INH_exc2'] = {'type': 'NetStim', 'interval': 5.0, 'start': 0, 'noise': 1, 'seed': 5}
        netParams.stimSourceParams['NetStim_INH_inh']  = {'type': 'NetStim', 'interval': 1.0, 'start': 0, 'noise': 1, 'seed': 6}

        ### Target Stimulation - Spontaneous firing
        for na in range(Nassemblies):
            # exc to PYR
            netParams.stimTargetParams['NetStim_PYR_exc->PYR_Assembly'+str(na+1)] = {
                'source': 'NetStim_PYR_exc',
                'conds': {'pop': 'Pyr_Assembly'+str(na+1)},
                'sec': 'soma',
                'loc': 0.5,
                'weight': 1.0e-3,
                'delay': 2*Dt,
                'synMech': 'AMPA'}

            netParams.stimTargetParams['NetStim_PYR_exc->PYR_Assembly_NMDA'+str(na+1)] = {
                'source': 'NetStim_PYR_exc2',
                'conds': {'pop': 'Pyr_Assembly'+str(na+1)},
                'sec': 'soma',
                'loc': 0.5,
                'weight': 0.1e-3,
                'delay': 2*Dt,
                'synMech': 'NMDA'}

            # inh to PYR
            netParams.stimTargetParams['NetStim_PYR_inh->PYR_Assembly'+str(na+1)] = {
                'source': 'NetStim_PYR_inh',
                'conds': {'pop': 'Pyr_Assembly'+str(na+1)},
                'sec': 'soma',
                'loc': 0.5,
                'weight': 7.5e-3,
                'delay': 2*Dt,
                'synMech': 'GABA'}

        # exc to INH
        netParams.stimTargetParams['NetStim_INH_exc->INH'] = {
            'source': 'NetStim_INH_exc',
            'conds': {'pop': 'InhPop'},
            'sec': 'soma',
            'loc': 0.5,
            'weight': 0.55e-3,
            'delay': 2*Dt,
            'synMech': 'AMPA'}

        netParams.stimTargetParams['NetStim_INH_exc->INH_NMDA'] = {
            'source': 'NetStim_INH_exc2',
            'conds': {'pop': 'InhPop'},
            'sec': 'soma',
            'loc': 0.5,
            'weight': 0.055e-3,
            'delay': 2*Dt,
            'synMech': 'NMDA'}

        # inh to INH
        netParams.stimTargetParams['NetStim_INH_inh->INH'] = {
            'source': 'NetStim_INH_inh',
            'conds': {'pop': 'InhPop'},
            'sec': 'soma',
            'loc': 0.5,
            'weight': 1.25e-3,
            'delay': 2*Dt,
            'synMech': 'GABA'}


        ###############################################################################
        ## Assembly recall
        ###############################################################################
        netParams.stimSourceParams['IClamp'] =  {'type': 'IClamp', 'del': Tfinal/6, 'dur': 100, 'amp': 1.00}
        netParams.stimTargetParams['IClamp->Pyr_Assembly1'] = {
                'source': 'IClamp',
                'sec': 'soma',
                'loc': 0.5,
                'conds': {'pop':'Pyr_Assembly1'}}




        