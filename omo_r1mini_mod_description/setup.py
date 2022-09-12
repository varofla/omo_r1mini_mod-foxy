import os
import glob

from setuptools import setup

package_name = "omo_r1mini_mod_description"

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob.glob("launch/*.launch.py"),
        ),
        (
            os.path.join("share", package_name, "urdf"),
            glob.glob("urdf/*.urdf"),
        ),
        (
            os.path.join("share", package_name, "meshes/sensors"),
            glob.glob("meshes/sensors/*"),
        ),
        (
            os.path.join("share", package_name, "meshes/wheels"),
            glob.glob("meshes/wheels/*"),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="varofla",
    maintainer_email="admin@varofla.com",
    description="ROS2 TF2 Tree for omo r1 mini mod",
    license="Apache 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
