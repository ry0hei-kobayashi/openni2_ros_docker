import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from openni2_interfaces.srv import GetXtionImage

class ImageServiceServer(Node):
    def __init__(self):
        super().__init__('image_service_server')
        self.srv = self.create_service(GetXtionImage, 'xtion_rgb_image', self.get_image_callback)
        self.subscription = self.create_subscription(
            Image,
            '/camera/rgb/image_raw',
            self.image_callback,
            10)
        self.current_image = None
        self.get_logger().info('Image Service Server is ready.')

    def image_callback(self, msg):
        self.current_image = msg

    def get_image_callback(self, request, response):
        if self.current_image is not None:
            response.rgb_image = self.current_image
            self.get_logger().info('Image sent to client.')
        else:
            self.get_logger().warning('No image available.')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ImageServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

