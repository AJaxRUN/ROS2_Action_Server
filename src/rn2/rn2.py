import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rn2.action import MissionAction

class MissionServer(Node):
    def __init__(self):
        super().__init__('mission_server')
        self.server = ActionServer(self, MissionAction, 'mission_action', self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info(f"Received mission: {goal_handle.request.name}")
        goal_handle.succeed()
        return MissionAction.Result()

def main():
    rclpy.init()
    node = MissionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
