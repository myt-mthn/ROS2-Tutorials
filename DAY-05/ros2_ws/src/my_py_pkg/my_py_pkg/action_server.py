import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from action_pkg.action import Fibonacci

class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
        self,
        Fibonacci,
        'fibonacci',
        self.execute_callback
        )
        self.get_logger().info("Fibonacci Action Server is ready!")
        
    def execute_callback(self, goal_handle):
        self.get_logger().info(f"Received goal: order = {goal_handle.request.order}")
        # Prepare result & feedback
        feedback_msg = Fibonacci.Feedback()
        result = Fibonacci.Result()
        sequence = [0, 1]
        feedback_msg.partial = sequence.copy()
        # Publish initial feedback
        goal_handle.publish_feedback(feedback_msg)
        self.get_logger().info(f"Feedback: {feedback_msg.partial}")
        # Generate Fibonacci sequence
        for i in range(2, goal_handle.request.order):
            sequence.append(sequence[i - 1] + sequence[i - 2])
            feedback_msg.partial = sequence.copy()
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f"Feedback: {feedback_msg.partial}")
        
        result.sequence = sequence
        goal_handle.succeed()
        self.get_logger().info(f"Sending result: {result.sequence}")
        return result
    
def main(args=None):
    rclpy.init(args=args)
    node = FibonacciActionServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()