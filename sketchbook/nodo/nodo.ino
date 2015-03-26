#include "ros.h"
#include "std_msgs/Int16.h"

ros::NodeHandle nh;

std_msgs::Int16 potx_lec_msg;
std_msgs::Int16 potz_lec_msg;

ros::Publisher potx_lec_pub("potx", &potx_lec_msg);
ros::Publisher potz_lec_pub("potz", &potz_lec_msg);

int potx_lec;
int potz_lec;

void setup() {

  nh.initNode();

  nh.advertise(potx_lec_pub);
  nh.advertise(potz_lec_pub);
}

void loop() {

  nh.spinOnce();

  potx_lec = analogRead(A0);
  poty_lec = analogRead(A1);

  potx_lec_msg.data = potx_lec;
  potz_lec_msg.data = potz_lec;

  potx_lec_pub.publish(&potx_lec_msg);
  potz_lec_pub.publish(&potz_lec_msg);

  delay(1000);

}
