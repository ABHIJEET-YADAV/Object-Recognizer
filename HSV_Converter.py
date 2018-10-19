import cv2

img = cv2.imread('Images/car.jpg')

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', imgHSV)

cv2.imshow('Hue Channel ', imgHSV[:, :, 0])
cv2.imshow('Saturation Channel ', imgHSV[:, :, 1])
cv2.imshow('Value Channel ', imgHSV[:, :, 2])

cv2.waitKey(0)

cv2.destroyAllWindows()