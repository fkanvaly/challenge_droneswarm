from drone import Drone
import numpy as np
import cv2

class DroneSwarm():

    def __init__(self):
        self.swarm = [Drone(i) for i in range(1,6)]
        self.swarmView = np.zeros((360*2, 640*3,3))
        
    def get_swarmView(self):
        line1 = np.hstack((np.hstack((self.swarm[0].view, self.swarm[1].view)), self.swarm[2].view))
        line2 = np.hstack((np.hstack((self.swarm[2].view, self.swarm[3].view)), np.zeros((360, 640,3), np.uint8)))
        self.swarmView= np.vstack((line1,line2))
        return self.swarmView
    
    def getView(self, L):
        """return a list of each drone view"""
        return [ self.swarm[i].view for i in L]

    def turn_off(self, L):
        for i in L: self.swarm[i].turn_off()

    def take_off(self, L):
        for i in L: self.swarm[i].take_off()
    
    def land(self, L): 
        for i in L: self.swarm[i].land()

    def stop(self, L):
        for i in L: self.swarm[i].stop()

    def linearVelocity(self, L, lv):
        """lv is a array [v.x, v.y, v.z]"""
        for i in L: self.swarm[i].linearVelocity(lv)

    def angularVelocity(self, L, av):
        """av is a array [w.x, w.y, w.z]"""
        for i in L: self.swarm[i].angularVelocity(av)

    def up(self, L, speed):
        for i in L: self.swarm[i].up(speed)

    def down(self, L, speed):
        for i in L: self.swarm[i].down(speed)

    def foreward(self, L, speed):
        for i in L: self.swarm[i].forward(speed)

    def backward(self, L, speed):
        for i in L: self.swarm[i].backward(speed)

    def right(self, L, speed):
        for i in L: self.swarm[i].right(speed)

    def left(self, L, speed):
        for i in L: self.swarm[i].left(speed)

    def clockwise(self, L, speed):
        for i in L: self.swarm[i].clockwise(speed)

    def counter_clockwise(self, L, speed):
        for i in L: self.swarm[i].counter_clockwise(speed)



if __name__ == "__main__":
    swarm = DroneSwarm()
    i = -1
    try:
        while(1):
            cv2.imshow('img',swarm.get_swarmView())
            k = cv2.waitKey(1)
            if k==27:    # Esc key to stop
                break
            elif k==-1:  # yaw ccw
                continue 
    finally:
        swarm.turn_off(i)