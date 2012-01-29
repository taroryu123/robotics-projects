#!/usr/bin/env python

"""
pan_tilt.py

subscribes to the source of color blob location coordinates
and updates the aim of the camera, based on those coordinates.
"""

import roslib ; roslib.load_manifest('nomad_camera_tracking')
import rospy

from geometry_msgs.msg import Point
from PanTilt import PanTilt

panTilt = None

def mainControlLoop():

    global panTilt

    panTilt = PanTilt('/dev/ttyUSB0')
    panTilt.centerCamera()
    cameraAim = Point()
    cameraAim.z = 0

    trackingCamera = rospy.Publisher('trackingCamera', Point)
    
    while not rospy.is_shutdown():
        cameraAim.x, cameraAim.y = panTilt.getCameraAim()
        trackingCamera.publish(cameraAim)
        rospy.sleep(1.0)

    return

if __name__ == '__main__':

    rospy.init_node('pan_tilt', log_level = rospy.DEBUG)
    rospy.loginfo('pan_tilt starting')

    mainControlLoop()

    rospy.logwarn('Stopping')

    sys.exit(0)

