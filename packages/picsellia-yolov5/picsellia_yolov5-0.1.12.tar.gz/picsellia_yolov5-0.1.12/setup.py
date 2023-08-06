"""Setup script for object_detection with TF2.0."""
import os
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'tensorboard>=2.2',
    'torch>=1.7.0',
    'torchvision>=0.8.1',
    'tqdm>=4.41.0',
    'pillow==7.2.0',
    'matplotlib==3.3.4',
    'Cython==0.29.21',
    'pycocotools==2.0.2',
    'lvis==0.5.3',
    'scipy==1.10.1',
    'pandas<=1.1.5',
    'opencv-python>=4.1.2',
    'ruamel.yaml==0.16.13',
    'PyYAML>=5.3.1',
    'thop==0.0.31-2005241907',
    'seaborn>=0.11.0'
]

setup(
    name='picsellia_yolov5',
    version='0.1.12',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=(
        [p for p in find_packages(where='.')]),
    package_dir={
        'yolov5': 'yolov5',
        'data': os.path.join('yolov5', 'data')
    },
    description='Picsellia wrapper for pytorch implementation of Yolov5',
    python_requires='>=3.8',
)
