import cv2

img = cv2.imread('Images/car3.jpg')

B,G,R = cv2.split(img)

cv2.imshow('RGB Image', img)

cv2.imshow('Red Channel ', R)
cv2.imshow('Green Channel ', G)
cv2.imshow('Blue Channel ', B)

cv2.waitKey(0)
cv2.destroyAllWindows()

merged = cv2.merge([B, G, R])
cv2.imshow('Merged', merged)

merged1 = cv2.merge([B+100, G, R])
cv2.imshow('Merged with Blue', merged1)

cv2.waitKey(0)
cv2.destroyAllWindows()
