import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='ntrip',
            executable='ntrip',
            name='ntrip_client',
            output='screen',
            parameters=[
                {'ip': '199.184.151.36'},  # Ip
                {'port': 2101},  # Change to your port number, WGS84
                {'user': 'MSTKRT03'},  # Change to your username
                {'passwd': '29YK5SJ6S83W'},  # Change to your password
                {'mountpoint': 'RTK_SNUS_X'},  # Change to your mountpoint
                {'report_interval': 1} # the report interval to the NTRIP Caster, default is 1 sec
            ]
        ),
    ])
