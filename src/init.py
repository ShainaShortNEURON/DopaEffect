from netpyne import sim

simConfig, netParams = sim.loadFromIndexFile('index.npjson')
sim.createSimulateAnalyze(netParams, simConfig)