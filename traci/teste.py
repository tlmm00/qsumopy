import traci
import traci.constants as tc

sumoBinary = "/usr/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "./sumo-files/inter.sumocfg"]

traci.start(sumoCmd)

step = 0
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    step+=1

    # get the id of all vehicles present on the simulation
    vehicles = traci.vehicle.getIDList()

    # generate a list of the position of all vehicles present on the simulation
    locations = [traci.vehicle.getPosition(v) for v in vehicles]
    
print("steps: ", str(step))
traci.close()