import cv2

img = cv2.imread('Images/car.jpg')

cv2.imshow('Original Image',img)
cv2.waitKey(0)

#size of our image 3/4 of it's original size
img_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow('Scaling -Linear Interplotation', img_scaled)
cv2.waitKey()

#doubled the size of our image
img_scaled1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interplotation', img_scaled1)
cv2.waitKey()

#skew the re-sizing by setting exact dimensions
img_scaled2 = cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled2)
cv2.waitKey()

cv2.destroyAllWindows()