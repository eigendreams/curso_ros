cmake_minimum_required(VERSION 2.8.3)
project(test)
find_package(
	catkin 
	REQUIRED COMPONENTS 
		roscpp 
		rospy 
		std_msgs 
		geometry_msgs
		message_generation 
		dynamic_reconfigure
)
generate_dynamic_reconfigure_options(
    cfg/DYN.cfg
)
add_message_files( FILES float32_12.msg float32_3.msg )
generate_messages(
	DEPENDENCIES
	std_msgs
)
catkin_package(
    CATKIN_DEPENDS 
    	message_runtime
    	roscpp 
    	std_msgs
    	geometry_msgs
)