from netpyne import specs

Dt = 0.05
Tfinal = 30000
patient = 0
###############################################################################
# Simulation options
###############################################################################
simConfig = specs.SimConfig()

simConfig.duration = Tfinal
simConfig.dt = Dt
simConfig.hParams = {'v_init': -66,'celsius': 23}
simConfig.verbose = False
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
#                          'ko_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'ko'},
#                          'cai_basal':{'sec':'Bdend','loc':0.5,'var':'cai'},
#                          'ko_apical': {'sec': 'Adend_distal', 'loc': 0.5, 'var': 'ko'},
#                          'synapse_inmda':{'sec':'soma','loc':0.5,'synMech':'NMDA','var':'i'},}  # Dict with traces to record
simConfig.recordStim = True
simConfig.recordStep = 0.1        # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = '00'         # Set file output name
#simConfig.saveJson = True

#simConfig.analysis['plotTraces'] = {'include': ['all'], 'saveFig': True}
#simConfig.analysis['plotRaster'] = {'saveFig': True}

# Update simConfig to save figures with patient flags
simConfig.analysis['plotTraces'] = {'include': ['all'], 'saveFig': 'traces_pat{0}.png'.format(patient)}
simConfig.analysis['plotRaster'] = {'saveFig': 'raster_pat{0}.png'.format(patient)}



# Add this block of code inside the loop
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig.recordStim = True
simConfig.recordStep = 0.1
simConfig.recordSpikes = 'all'  # Record spike times for all cells

simConfig.filename = 'patient_{0}'.format(patient)
simConfig.savePickle = True  # Save data in pickle format