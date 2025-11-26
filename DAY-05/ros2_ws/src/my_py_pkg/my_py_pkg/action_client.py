import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from action_pkg.action import Fibonacci

class FibonacciActionClient(Node):
    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._client = ActionClient(self, Fibonacci, 'fibonacci')
    
    def send_goal(self, order):
        self._client.wait_for_server()
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order
        self.get_logger().info(f"Sending goal: order={order}")
        return self._client.send_goal_async(
        goal_msg,
        feedback_callback=self.feedback_callback
        )
        
    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: {feedback_msg.feedback.partial}")
    
    def get_result(self, goal_future):
        goal_handle = goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error("Goal rejected!")
            return
        self.get_logger().info("Goal accepted.")
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        return result_future.result().result

def main(args=None):
    rclpy.init(args=args)
    node = FibonacciActionClient()
    goal_future = node.send_goal(10)
    rclpy.spin_until_future_complete(node, goal_future)
    result = node.get_result(goal_future)
    print(f"Final Result: {result.sequence}")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
