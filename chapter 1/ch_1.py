import cv2
#loading image
image = cv2.imread("C:\\Users\\Bisrat worku\\Desktop\\OIP.jpg")
cv2.imshow('image', image)
cv2.waitKey(1000)

#loading grayscale image

gray_image = cv2.imread("C:\\Users\\Bisrat worku\\Desktop\\OIP.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("gray", gray_image)
cv2.waitKey()

#saving images

cv2.imwrite('gray.jpg', gray_image)