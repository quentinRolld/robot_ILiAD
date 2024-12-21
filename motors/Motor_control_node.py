import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/motor_rates',
            self.motor_rates_callback,
            10
        )
        # Initialize PWM
        #self.pwm = 

    def motor_rates_callback(self, msg):
        # Retrieve duty cycles from message
        motor_1_duty_cycle = msg.dutyC1
        motor_1_direction = msg.direction1
        motor_2_duty_cycle = msg.dutyC2
        motor_2_direction = msg.direction2
        

        # Apply computed angles to the servos
        self.apply_servo_angles(servo_angles)

    def apply_servo_angles(self, servo_angles):
        # Apply servo angles using the provided function
        if len(servo_angles) == 6:
            self.kit.servo[0].angle = servo_angles[0]
            self.kit.servo[1].angle = servo_angles[1]
            self.kit.servo[2].angle = servo_angles[2]
            self.kit.servo[3].angle = servo_angles[3]
            self.kit.servo[4].angle = servo_angles[4]
            self.kit.servo[5].angle = servo_angles[5]
        else:
            self.get_logger().warn("Received invalid number of servo angles")

def main(args=None):
    rclpy.init(args=args)
    servo_control_node = MotorControlNode()
    rclpy.spin(servo_control_node)
    servo_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()