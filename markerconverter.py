#!/usr/bin/env python
import roslib; roslib.load_manifest('markerconverter')
import rospy
from std_msgs.msg import String
from ar_pose.msg import ARMarkers

name_mapping = {'0': 'Milk', '1': 'Cornflakes', '2': 'Plate', '3': 'Spoon', '4': 'Cup' }
pub = rospy.Publisher('ASFSD', String)
    
def append_to_list(data):
    global pub
    global name_mapping
    string = "("
    for marker in data.markers:
        #print("ID is: %s and %s"%(marker.id, marker.pose.pos))
        string += "(%s - %s %s %s %s %s %s %s)"%(name_mapping[str(marker.id)], marker.pose.pose.position.x, marker.pose.pose.position.y, marker.pose.pose.position.z, marker.pose.pose.orientation.x, marker.pose.pose.orientation.y, marker.pose.pose.orientation.z, marker.pose.pose.orientation.w)
		
    string += ")"
    print ("String is: %s"%string)
    pub.publish(String(string))

def listener():
    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("ar_pose_markers", ARMarkers, append_to_list)
    rospy.spin()
    

if __name__ == '__main__':
    listener()
