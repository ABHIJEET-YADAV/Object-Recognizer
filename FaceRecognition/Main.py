import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'FaceRecognition/Faces/'

onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels = [], []