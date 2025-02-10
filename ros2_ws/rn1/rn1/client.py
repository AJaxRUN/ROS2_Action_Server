#!/userbin/env python3
import rclpy
import requests
from rclpy.node import Node
from rclpy.action import ActionClient
from mission_action.action import Mission

API_URL = "http://0.0.0.0:8080/mission"
class MissionClient(Node):

    def __init__(self):
        super().__init__('mission_client')
        self.client = ActionClient(self, Mission, "mission_action")
        self.timer = self.create_timer(1.0, self.fetch_and_send_mission)

    def fetch_and_send_mission(self):
        response = requests.get(API_URL).json()
        mission = response.get("mission", {})
        if mission:
            goal = Mission.Goal()
            goal.mission_data = str(mission)
            self.send_goal(goal)

    def send_goal(self, goal):
        self.client.wait_for_server()
        future = self.client.send_goal_async(goal)
        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Mission rejected")
            return
        self.get_logger().info("Mission accepted")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Mission Result: {result.success}")

def main(args=None):
    rclpy.init(args=args)
    node = MissionClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()