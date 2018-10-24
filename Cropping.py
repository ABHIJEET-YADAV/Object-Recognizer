import cv2

img = cv2.imread('Images/car3.jpg')

height, width = img.shape[:2]

#Starting pixel coordinates(top left, of cropping rectangle)

start_row, start_col = int(height*.25), int(width*.25)

#Ending pixel coordinates (bottom right)

end_row, end_col = int(height*.75), int(width*.75)

#Use the indexing to crop the image

cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('Original', img)
cv2.waitKey(0)

cv2.imshow('Cropped', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()