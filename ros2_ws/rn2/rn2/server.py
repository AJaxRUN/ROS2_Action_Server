import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from mission_action.action import Mission

class MissionServer(Node):
    def __init__(self):
        super().__init__("mission_server")
        self.server = ActionServer(self, Mission, "mission_action", self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info(f"Received mission at the server: {goal_handle.request.mission_data}")
        goal_handle.succeed()
        return Mission.Result(success=True)

def main(args=None):
    rclpy.init(args=args)
    node = MissionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
