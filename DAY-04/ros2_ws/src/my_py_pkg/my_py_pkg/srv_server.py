import rclpy
from rclpy.node import Node

# Import the generated service interface
from service_pkg.srv import TestService


class ServiceServer(Node):
    def __init__(self):
        super().__init__('ServiceServerNode')

        # Create the service
        self.srv = self.create_service(
            TestService,           # Service type
            'test_service',       # Service name
            self.callback  # Callback function
        )

        self.get_logger().info("Service Server Ready: ")

    def callback(self, request, response):
        # Log incoming request
        self.get_logger().info(
            f"Incoming request: {request.input}"
        )

        # Perform the operation
        response.output = "hello client... Got your req..."

        # Log and return response
        self.get_logger().info(f"Sending response: {response.output}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
