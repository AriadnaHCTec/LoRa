import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
                                                        #tipo   #nombre 
        self.publisher_llantas = self.create_publisher(Int32, 'presion_llantas', 1)
        self.publisher_aceite = self.create_publisher(Int32, 'nivel_aceite', 1)
        self.publisher_llenado = self.create_publisher(Int32, 'llenado', 1)
        self.publisher_penudos = self.create_publisher(String, 'penudos', 1)
        timer_period = 1 
        timer_period_llantas = 2 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.timer_llantas = self.create_timer(timer_period_llantas, self.timer_callback_llantas)
        self.nivel_de_llenado = 0
        
    def timer_callback(self):
        msg_nivel_aceite = Int32()
        msg_llenado = Int32()
        msg_penudos = String()

        msg_nivel_aceite.data = 5
        msg_llenado.data = self.nivel_de_llenado
        msg_penudos.data = "penudos"

        self.publisher_aceite.publish(msg_nivel_aceite)
        self.publisher_llenado.publish(msg_llenado)
        self.publisher_penudos.publish(msg_penudos)
        self.nivel_de_llenado += 1
        # self.get_logger().info('Publishing: "%s"' % msg.data)

    def timer_callback_llantas(self):
        msg_presion_llantas = Int32()

        msg_presion_llantas.data = 10

        self.publisher_llantas.publish(msg_presion_llantas)

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
