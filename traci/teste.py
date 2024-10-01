import traci

sumoBinary = "/usr/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "./sumo-files/inter.sumocfg"]

traci.start(sumoCmd)

step = 0
while step < 1000:
    traci.simulationStep()
    step += 1

print(step)
traci.close()