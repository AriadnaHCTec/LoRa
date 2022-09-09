#!/usr/bin/env python3

import rospy
import serial
import time
import json

from std_msgs.msg import Int32
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu


rospy.init_node("trilladora")

#Navigation publishers                                             
publisher_GPS = rospy.Publisher('GPS', NavSatFix, queue_size=1)
publisher_IMU = rospy.Publisher('IMU', Imu, 1)
publisher_wheel_speed = rospy.Publisher('wheel_speed', Int32, queue_size=1)
publisher_trilladora_speed = rospy.Publisher('trilladora_speed', Int32, queue_size=1)
#Collect publishers
publisher_fill = rospy.Publisher('fill', Int32, queue_size=1)
publisher_kilograms = rospy.Publisher('kilograms', Int32, queue_size=1)
#Check publishers 
publisher_fuel_level = rospy.Publisher('fuel_level', Int32, queue_size=1)
publisher_mileage = rospy.Publisher('mileage', Int32, queue_size=1)
publisher_oil_level = rospy.Publisher('oil_level', Int32, queue_size=1)
publisher_wheel_preasure = rospy.Publisher('wheel_preasure', Int32, queue_size=1)

gps = NavSatFix()
imu = Imu()
wheel_speed = Int32()
trilladora_speed = Int32()
fill = Int32()
kilograms = Int32()
fuel_level = Int32()
mileage = Int32()
oil_level = Int32()
wheel_preasure = Int32()

rate = rospy.Rate(1)

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=0.1)

def main():
    while not rospy.is_shutdown():
        #data = str(arduino.readline())
        info = arduino.readline()
        info = str(info)
        if len(info) > 4:
            
            info = info[2:-1]
            print (info)
            json_object = json.loads(info)
            
            for i in json_object:
                if i == "altitude":
                    gps.altitude = json_object[i]
                    publisher_GPS.publish(gps)
                
                elif i == "longitude" :
                    gps.longitude = json_object[i]
                    publisher_GPS.publish(gps)

                elif i == "altitude" :
                    gps.altitude = json_object[i]
                    publisher_GPS.publish(gps)

                elif i == "qx" :
                    imu.orientation.x = json_object[i]
                    publisher_IMU.publish(imu)


                elif i == "qy" :
                    imu.orientation.y = json_object[i]
                    publisher_IMU.publish(imu)

                elif i == "qz" :
                    imu.orientation.z = json_object[i]
                    publisher_IMU.publish(imu)

                elif i == "qw" :
                    imu.orientation.w = json_object[i]
                    publisher_IMU.publish(imu)

                elif i == "wheel_speed" :
                    wheel_speed.data = json_object[i]
                    publisher_wheel_speed.publish(wheel_speed)

                elif i == "trilladora_speed" :
                    trilladora_speed.data = json_object[i]
                    publisher_trilladora_speed.publish(trilladora_speed)

                elif i == "fill" :
                    fill.data = json_object[i]
                    publisher_fill.publish(fill)

                elif i == "kilograms" :
                    kilograms.data = json_object[i]
                    publisher_kilograms.publish(kilograms)

                elif i == "fuel_level" :
                    fuel_level.data = json_object[i]
                    publisher_fuel_level.publish(fuel_level)

                elif i == "mileage" :
                    mileage.data = json_object[i]
                    publisher_mileage.publish(mileage)

                elif i == "oil_level" :
                    oil_level.data = json_object[i]
                    publisher_oil_level.publish(oil_level)

                elif i == "wheel_preasure" :
                    wheel_preasure.data = json_object[i]
                    publisher_wheel_preasure.publish(wheel_preasure)

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
