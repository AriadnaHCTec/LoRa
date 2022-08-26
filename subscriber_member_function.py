import rclpy
from rclpy.node import Node

#import tf_transformations
import json

from std_msgs.msg import Int32
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')

        #Navigation psubscription                                             
        self.subscription_GPS = self.create_subscription(NavSatFix, 'GPS',self.listener_callback_GPS, 1)
        self.subscription_IMU = self.create_subscription(Imu, 'IMU',self.listener_callback_IMU, 1)
        self.subscription_wheel_speed = self.create_subscription(Int32, 'wheel_speed',self.listener_callback_wheel_speed, 1)
        self.subscription_trilladora_speed = self.create_subscription(Int32, 'trilladora_speed',self.listener_callback_trilladora_speed, 1)

        #Collect psubscription
        self.subscription_fill = self.create_subscription(Int32, 'fill',self.listener_callback_fill, 1)
        self.subscription_kilograms = self.create_subscription(Int32, 'kilograms',self.listener_callback_kilograms, 1)

        #Check publishers 
        self.subscription_fuel_level = self.create_subscription(Int32, 'fuel_level',self.listener_callback_fuel_level, 1)
        self.subscription_mileage = self.create_subscription(Int32, 'mileage',self.listener_callback_mileage, 1)
        self.subscription_oil_level = self.create_subscription(Int32, 'oil_level',self.listener_callback_oil_level, 1)
        self.subscription_wheel_preasure = self.create_subscription(Int32, 'wheel_preasure',self.listener_callback_wheel_preasure, 1)

        timer_period_1 = 1 # 1 second

        #Create timers that call the timer_callback
        self.timer = self.create_timer(timer_period_1, self.timer_callback)

        #create json
        self.data_dictionary = {} 

    def timer_callback(self):
        if len(self.data_dictionary) == 0:
            pass
        else:
            json_string = json.dumps(self.data_dictionary)
            print (json_string)
            self.data_dictionary.clear()
            pass

    def listener_callback_GPS(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["altitude"] = msg.altitude
        self.data_dictionary["longitude"] = msg.longitude
        self.data_dictionary["latitude"] = msg.latitude
        pass
    
    def listener_callback_IMU(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        
        self.data_dictionary["qx"] = msg.orientation.x
        self.data_dictionary["qy"] = msg.orientation.y
        self.data_dictionary["qz"] = msg.orientation.z
        self.data_dictionary["qw"] = msg.orientation.w
        pass

    def listener_callback_wheel_speed(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["wheel_speed"] = msg.data
        pass

    def listener_callback_trilladora_speed(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["trilladora_speed"] = msg.data
        pass

    def listener_callback_kilograms(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["kilograms"] = msg.data
        pass

    def listener_callback_fuel_level(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["fuel_level"] = msg.data
        pass

    def listener_callback_mileage(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["mileage"] = msg.data
        pass

    def listener_callback_fill(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["fill"] = msg.data
        pass

    def listener_callback_oil_level(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["oil_level"] = msg.data
        pass

    def listener_callback_wheel_preasure(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.data_dictionary["wheel_preasure"] = msg.data
        pass

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
