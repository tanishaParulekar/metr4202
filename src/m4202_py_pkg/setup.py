from setuptools import find_packages, setup

package_name = 'm4202_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tparu001k',
    maintainer_email='tparu001k@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # insert variable for and path to node that you want to build and install in this section.
            "m4202_node = m4202_py_pkg.m4202_first_node:main"
        ],
    },
)
