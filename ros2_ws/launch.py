import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(package="rn1", executable="mission_client"),
        launch_ros.actions.Node(package="rn2", executable="mission_server"),
    ])
