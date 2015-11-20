from setuptools import setup


setup(
    name='drone-tower',
    version='0.1',
    description="Ansible Tower plugin for Drone.",
    url="https://github.com/msteinert/drone-tower",
    maintainer="Drone Contributors",
    maintainer_email="support@drone.io",
    packages=["drone_tower"],
    scripts=["bin/drone-tower"],
    install_requires=["ansible-tower-cli", "drone"],
)
