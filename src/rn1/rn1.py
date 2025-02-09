import rclpy
import requests
from rclpy.node import Node
from rn2.action import MissionAction  # Import the action from RN2
from rclpy.action import ActionClient
import time

class MissionClient(Node):
    def __init__(self):
        super().__init__('mission_client')
        self.client = ActionClient(self, MissionAction, 'mission_action')

    def send_mission(self, mission):
        goal_msg = MissionAction.Goal()
        goal_msg.name = mission["name"]
        goal_msg.description = mission.get("description", "")

        self.client.wait_for_server()
        self.get_logger().info(f"Sending mission: {mission['name']}")
        self.client.send_goal_async(goal_msg)

def main():
    rclpy.init()
    node = MissionClient()
    
    while rclpy.ok():
        response = requests.get("http://localhost:8000/mission")
        if response.status_code == 200 and "name" in response.json():
            node.send_mission(response.json())
        time.sleep(1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
