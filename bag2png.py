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
    #tutaj należy umieścić ścieżki zapisu i odczytu plików
	#save_dir = ''
     #   filename = ''

        # Use a CvBridge to convert ROS images to OpenCV images so they can be saved.
        self.bridge = CvBridge()

        # Open bag file.
        i = 0;
        with rosbag.Bag(filename, 'r') as bag:
            for topic, msg, t in bag.read_messages():
            #należy przetwarzać obraz z prawej i lewej kamery oddzielnie
                if topic == "/pylon_stereo_node/right/image_raw":
                    try:
                        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
                    except CvBridgeError, e:
                        print e
                    timestr = "%06d" % i
                    i = i + 1;
                    image_name = str(save_dir)+"/right_"+timestr+".png"
                    cv2.imwrite(image_name, cv_image)
                

# Main function.    
if __name__ == '__main__':
    image_creator = ImageCreator()
