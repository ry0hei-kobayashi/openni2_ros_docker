import rclpy
from rclpy.node import Node
from openni2_interfaces.srv import GetXtionImage

class ImageServiceClient(Node):
    def __init__(self):
        super().__init__('image_service_client')
        self.cli = self.create_client(GetXtionImage, 'get_image')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        self.get_logger().info('Service available, sending request.')
        self.request_image()

    def request_image(self):
        req = ImageService.Request()
        future = self.cli.call_async(req)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        response = future.result()
        if response is not None:
            self.get_logger().info('Image received from server.')
        else:
            self.get_logger().warning('No response from server.')

def main(args=None):
    rclpy.init(args=args)
    node = ImageServiceClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

