from setuptools import setup

package_name = "rn2"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Arjun",
    maintainer_email="arjun@example.com",
    description="ROS2 Server Node for receiving mission data",
    license="Apache License 2.0",
    entry_points={
        "console_scripts": [
            "rn2_server = rn2.rn2_server:main",
        ],
    },
)
