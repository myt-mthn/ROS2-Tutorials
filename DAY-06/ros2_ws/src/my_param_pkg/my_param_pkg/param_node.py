import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from example_interfaces.msg import Int64

class paramNode(Node):
    def __init__(self):
        super().__init__("parameter_node")
        self.declare_parameter("Number", 3)
        self.num_publisher = self.create_publisher(Int64, "Number", 10)
        self.num_timer = self.create_timer(1.0, self.publish_number)

    def publish_number(self):
        msg = Int64
        msg.data = self.get_parameter("Number").value
        self.num_publisher.publish(msg)

def main():
    rclpy.init()
    node = paramNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()