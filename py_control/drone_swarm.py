from drone import Drone
import numpy as np
import cv2

class DroneSwarm():

    def __init__(self, number):
        self.drones = [Drone(i) for i in range(1, number+1)]
        self.swarm_view = np.zeros((360*2, 640*3,3))
        
    def get_swarm_view(self):
        line1 = np.hstack((np.hstack((self.drones[0].view, self.drones[1].view)), self.drones[2].view))
        line2 = np.hstack((np.hstack((self.drones[2].view, self.drones[3].view)), np.zeros((360, 640,3), np.uint8)))
        self.swarm_view = np.vstack((line1,line2))
        return self.swarm_view
    
    def get_view(self, drone=None):
        """return a list of each drone view"""
        if drone is None:
            return [drone.view for drone in self.drones]
        else:
            return self.drones[i].view

    def turn_off(self, drone=None):
        self.__swarm_do("turn_off", drone)

    def take_off(self, drone=None):
        self.__swarm_do("take_off", drone)
    
    def land(self, drone=None): 
        self.__swarm_do("land", drone)

    def stop(self, drone=None):
        self.__swarm_do("stop", drone)

    def set_linear_velocity(self, lv, drone=None):
        """lv is a array [v.x, v.y, v.z]"""
        self.__swarm_do("linear_velocity", drone, lv)

    def set_angular_velocity(self, av, drone=None):
        """av is a array [w.x, w.y, w.z]"""
        self.__swarm_do("angular_velocity", drone, av)

    def up(self, speed, drone=None):
        self.__swarm_do("up", drone, speed)

    def down(self, speed, drone=None):
        self.__swarm_do("down", drone, speed)

    def foreward(self, speed, drone=None):
        self.__swarm_do("foreward", drone, speed)

    def backward(self, speed, drone=None):
        self.__swarm_do("backward", drone, speed)

    def right(self, speed, drone=None):
        self.__swarm_do("right", drone, speed)

    def left(self, speed, drone=None):
        self.__swarm_do("left", drone, speed)

    def clockwise(self, speed, drone=None):
        self.__swarm_do("clockwise", drone, speed)

    def counter_clockwise(self, speed, drone=None):
        self.__swarm_do("counter_clockwise", drone, speed)

    def __swarm_do(self, f, drone_id=None, *args, **kwargs):
        """
        If drone_id is None then call f for each of the swarm drone, else
        call self.f with drone_id argument.
        """
        if drone_id is None:
            for drone in self.drones:
                getattr(drone, f)(*args, **kwargs)
        else:
            getattr(self.drones[drone_id], f)(*args, **kwargs)



if __name__ == "__main__":
    swarm = DroneSwarm(5)
    i = -1
    try:
        while(1):
            cv2.imshow('Swarm view', swarm.get_swarm_view())
            k = cv2.waitKey(1)
            if k==27:    # Esc key to stop
                break
            elif k==-1: 
                continue 
    finally:
        swarm.turn_off()