from setuptools import find_packages, setup
import os 
from glob import glob


package_name = 'openni2_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={'': '.'},
    data_files=[
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),  # Include launch files
    ],
    #data_files=[
    #    ('share/ament_index/resource_index/packages',
    #        ['resource/' + package_name]),
    #    ('share/' + package_name, ['package.xml']),
    #],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ry0hei-kobayashi',
    maintainer_email='kobayashi.ryohei621@mail.kyutech.jp',
    license='Apache Licence 2.0',
    entry_points={
        'console_scripts': [
        'xtion_service_server = openni2_service.xtion_service_server:main',
        'xtion_service_client = openni2_service.xtion_service_client:main',
        ],
    },
)
