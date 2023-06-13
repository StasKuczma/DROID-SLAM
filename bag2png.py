#!/usr/bin/python

# Start up ROS pieces.
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Reading bag filename from command line or roslaunch parameter.
import os
import sys

class ImageCreator():
    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        #save_dir = '/home/mnowicki/Desktop/img/'
        #filename = '/home/mnowicki/Desktop/InnolotWZL2/Outdoor/test_2018-05-25-08-56-06_naOkolo.bag'
	save_dir = '/home/mnowicki/Desktop/img/'
        filename = '/home/mnowicki/catkin_adasub/2018-12-18-15-48-55.bag'

        # Use a CvBridge to convert ROS images to OpenCV images so they can be saved.
        self.bridge = CvBridge()

        # Open bag file.
        i = 0;
        with rosbag.Bag(filename, 'r') as bag:
            for topic, msg, t in bag.read_messages():
                #if topic == "/bluefox3/stereo/left/image_raw":
                if topic == "/camera/image_mono":
                    try:
                        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                    except CvBridgeError, e:
                        print e
                    timestr = "%06d" % i
                    i = i + 1;
                    image_name = str(save_dir)+"/left_"+timestr+".png"
                    cv2.imwrite(image_name, cv_image)
                

# Main function.    
if __name__ == '__main__':
    image_creator = ImageCreator()
