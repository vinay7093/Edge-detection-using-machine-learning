import cv2

# Load the image
img = cv2.imread('images.jfif')
img = cv2.resize(img, (250,350))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 100, 200)  

cv2.imshow('Canny Edge Detection', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
