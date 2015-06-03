#!/usr/bin/env python
# license: GPL2.0
# author: marcino239.github.io

import rospy
import math

from std_msgs.msg import Float64

def talker():
	pub = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
	rospy.init_node('my_brain')
	r = rospy.Rate(10) # 10hz

	time_step = 0.0

	while not rospy.is_shutdown():
		
		val = math.sin( time_step / 40.0 )
		pub.publish( val )
		
		time_step = time_step + 1.0
		r.sleep()

if __name__ == '__main__':
    try:
		talker()
    except rospy.ROSInterruptException:
		print( 'Got ROSInterruptException.  Giving up' )
		pass
