import rclpy
from rclpy.node import Node

# Import the service type
from service_pkg.srv import TestService


class ServiceClient(Node):
    def __init__(self):
        super().__init__('ServiceClientNode')

        # Create the client object
        self.client = self.create_client(TestService, 'test_service')

        # Wait for the server to come online
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Service not available... waiting")

    def send_request(self, req):
        # Create the request object
        request = TestService.Request()
        request.input = req

        # Send the request
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        return future.result()


def main(args=None):
    rclpy.init(args=args)

    client = ServiceClient()

    # Example request
    response = client.send_request("Hello server")
    print(f"Result from server: {response.output}")

    rclpy.shutdown()


if __name__ == '__main__':
    main()
