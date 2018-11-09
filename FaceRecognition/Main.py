import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = 'FaceRecognition/Faces/'

onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

print("Model Training Done")

face_classifier = cv2.CascadeClassifier('"venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"')
