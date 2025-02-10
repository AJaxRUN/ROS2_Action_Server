#!/userbin/env python3
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.get_logger().info("Hiii from Aj")
    #     self.i = 0
    #     self.pub = self.create_publisher(String, 'chatter', 10)
    #     timer_period = 1.0
    #     self.tmr = self.create_timer(timer_period, self.timer_callback)

    # def timer_callback(self):
    #     msg = String()
    #     msg.data = 'Hello World: {0}'.format(self.i)
    #     self.i += 1
    #     self.get_logger().info('Publishing: "{0}"'.format(msg.data))
    #     self.pub.publish(msg)


def main(args=None):
    try:
        rclpy.init(args=args)
        node = Talker()
        rclpy.spin(node)
        rclpy.shutdown()
        
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()