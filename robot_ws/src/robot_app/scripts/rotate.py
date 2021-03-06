#nodo de ejemplo que hace girar el robot

#!/usr/bin/env python

#libreria de ros
import rospy


from geometry_msgs.msg import Twist

#creamos clase rotar
class Rotator():
    def __init__(self):
        #esto es un  publisher
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def rotate_forever(self):
        self.twist = Twist()

        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.twist.angular.z = 0.1
            self._cmd_pub.publish(self.twist)
            rospy.loginfo("Rotating robot: %s", self.twist)
            r.sleep()

#funcion principal
def main():
    rospy.init_node('rotate')
    try:
        rotator = Rotator()
        rotator.rotate_forever()
    except rospy.ROSInterruptException:
        pass

#se crea un punto de entrada 
if __name__ == '__main__':
    main()