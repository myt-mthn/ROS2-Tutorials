import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class param_node(Node):
    def __init__(self):
        super().__init__('param_node')
        
        self.declare_parameter('number_param', 10)

        self.publisher = self.create_publisher(Int32, 'number', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

        self.get_logger().info('Parameter node initialized with number_param set to 10')
    
    def timer_callback(self):
        number_value = self.get_parameter('number_param').value
        msg = Int32()
        msg.data = number_value
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {number_value}')


def main(args=None):
    rclpy.init(args=args)
    node = param_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# This code defines a ROS 2 node that publishes a parameter value to a topic.