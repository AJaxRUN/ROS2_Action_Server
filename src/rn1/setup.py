from setuptools import setup

package_name = "rn1"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Arjun",
    maintainer_email="arjun@example.com",
    description="ROS2 Client Node for sending mission data",
    license="Apache License 2.0",
    entry_points={
        "console_scripts": [
            "rn1_client = rn1.rn1_client:main",
        ],
    },
)
