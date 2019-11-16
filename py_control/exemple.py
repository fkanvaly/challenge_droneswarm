#! python3

from drone_swarm import DroneSwarm
from time import sleep

if __name__ == "__main__":
    swarm = DroneSwarm()

    # Nécessaire pour rendre les drones actifs
    swarm.turn_on()
    print("Drones démarrés")
    sleep(1)

    swarm.take_off()
    print("Décollage\n")

    for t in range(10):
        print("Altitudes : " + ", ".join("%0.1f" % p[2]
                                         for p in swarm.get_position()))
        sleep(1)

    swarm.set_angular_velocity([0, 0, 10])
    print("\nRotation")
    
    for t in range(5):
        print("Orientations : ", swarm.get_orientation())
        sleep(1)

    print()

    for i in range(swarm.drones_number):
        swarm.land(i)
        print("%s atterrit" % i)
        sleep(1)

    sleep(10)

    # Nécessaire pour stopper les threads de commande des drones
    swarm.turn_off()
    print("\nDrones éteints")

