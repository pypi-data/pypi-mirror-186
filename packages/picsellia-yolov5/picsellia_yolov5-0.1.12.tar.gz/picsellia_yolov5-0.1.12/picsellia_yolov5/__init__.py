import sys
import os 
from setuptools import find_packages
import picsellia_yolov5
for p in find_packages(where=picsellia_yolov5.__path__[0]):
    sys.path.append(os.path.join(picsellia_yolov5.__path__[0],p.replace('.','/')))

sys.path.append(picsellia_yolov5.__path__[0])
sys.path.append(os.path.join(picsellia_yolov5.__path__[0],'yolov5'))
