import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')

        #Navigation psubscription                                             
        self.subscription_GPS = self.create_subscription(NavSatFix, 'GPS',self.listener_callback_2, 1)
        self.subscription_IMU = self.create_subscription(Imu, 'IMU',self.listener_callback_2, 1)
        self.subscription_wheel_speed = self.create_subscription(Int32, 'wheel_speed',self.listener_callback, 1)
        self.subscription_trilladora_speed = self.create_subscription(Int32, 'trilladora_speed',self.listener_callback, 1)

        #Collect psubscription
        self.subscription_fill = self.create_subscription(Int32, 'fill',self.listener_callback, 1)
        self.subscription_kilograms = self.create_subscription(Int32, 'kilograms',self.listener_callback, 1)

        #Check publishers 
        self.subscription_fuel_level = self.create_subscription(Int32, 'fuel_level',self.listener_callback, 1)
        self.subscription_mileage = self.create_subscription(Int32, 'mileage',self.listener_callback, 1)
        self.subscription_oil_level = self.create_subscription(Int32, 'oil_level',self.listener_callback, 1)
        self.subscription_wheel_preasure = self.create_subscription(Int32, 'wheel_preasure',self.listener_callback, 1)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
    
    def listener_callback_2(self, msg):
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
