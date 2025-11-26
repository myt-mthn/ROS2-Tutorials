import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from action_pkg.action import Fibonacci

class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__("Fibonacci_action_server")

        self.action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback
        )
        self.get_logger().info("Fibonacci Action Server Ready!")
    
    def execute_callback(self, goal_handle):
        pass
