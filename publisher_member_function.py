import rclpy
from rclpy.node import Node

from random import randint

from std_msgs.msg import Int32
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        #Navigation publishers                                             
        self.publisher_GPS = self.create_publisher(NavSatFix, 'GPS', 1)
        self.publisher_IMU = self.create_publisher(Imu, 'IMU', 1)
        self.publisher_wheel_speed = self.create_publisher(Int32, 'wheel_speed', 1)
        self.publisher_trilladora_speed = self.create_publisher(Int32, 'trilladora_speed', 1)

        #Collect publishers
        self.publisher_fill = self.create_publisher(Int32, 'fill', 1)
        self.publisher_kilograms = self.create_publisher(Int32, 'kilograms', 1)

        #Check publishers 
        self.publisher_fuel_level = self.create_publisher(Int32, 'fuel_level', 1)
        self.publisher_mileage = self.create_publisher(Int32, 'mileage', 1)
        self.publisher_oil_level = self.create_publisher(Int32, 'oil_level', 1)
        self.publisher_wheel_preasure = self.create_publisher(Int32, 'wheel_preasure', 1)

        #Frequencies     seconds
        time_adjust = 1/100
        timer_period_5 = 5 * time_adjust
        timer_period_10 = 10 * time_adjust
        timer_period_20 = 20 * time_adjust

        #Create timers that call the timer_callback
        self.timer_5 = self.create_timer(timer_period_5, self.timer_callback_5)
        self.timer_10 = self.create_timer(timer_period_10, self.timer_callback_10)
        self.timer_20 = self.create_timer(timer_period_20, self.timer_callback_20)

        #Initial values for variables
        self.fill_level = 0 # from 0 -> 100 +- 2
        self.wheel_speed = 100 # 10 +- 1 (add speed changes) +- 1 (add sensor noise) 
        self.trilladora_speed = 30 # 30 +- 1 (add peed changes) +- 1 (add sensor noise) 

    def timer_callback_5(self):
        msg_GPS = NavSatFix()
        msg_IMU = Imu()
        msg_wheel_speed = Int32()
        msg_trilladora_speed = Int32()

        msg_GPS.latitude = 1.0
        msg_IMU.orientation.x = 2.0
        msg_wheel_speed.data = self.wheel_speed
        msg_trilladora_speed.data = self.trilladora_speed

        self.publisher_GPS.publish(msg_GPS)
        self.publisher_IMU.publish(msg_IMU)
        self.publisher_wheel_speed.publish(msg_wheel_speed)
        self.publisher_trilladora_speed.publish(msg_trilladora_speed)

        self.wheel_speed = 100 + randint(-1,1) + randint (-1,1)
        self.trilladora_speed = 30 + randint(-1,1) + randint (-1,1)

    def timer_callback_10(self):
        msg_wheel_preasure = Int32()
        msg_wheel_preasure.data = 5
        self.publisher_wheel_preasure.publish(msg_wheel_preasure)

    def timer_callback_20(self):
        msg_fill = Int32()
        msg_kilograms = Int32()
        msg_fuel_level = Int32()
        msg_mileage = Int32()
        msg_oil_level = Int32()

        msg_fill.data = self.fill_level
        msg_kilograms.data = 7
        msg_fuel_level.data = 8
        msg_mileage.data = 9
        msg_oil_level.data = 10

        self.publisher_fill.publish(msg_fill)
        self.publisher_kilograms.publish(msg_kilograms)
        self.publisher_fuel_level.publish(msg_fuel_level)
        self.publisher_mileage.publish(msg_mileage)
        self.publisher_oil_level.publish(msg_oil_level)

        if self.fill_level >= 100:
            self.fill_level = 0
        else:
            self.fill_level += 1 + randint(-2,2)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
