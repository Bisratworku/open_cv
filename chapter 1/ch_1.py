import cv2
#loading image
img = "C:\\Users\\Bisrat worku\\Desktop\\OIP.jpg"
image = cv2.imread(img)
#cv2.imshow('image', image)
#cv2.waitKey(1000)

#loading grayscale image

gray_image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
#cv2.imshow("gray", gray_image)
#cv2.waitKey()

#saving images

cv2.imwrite('gray.jpg', gray_image)

#color chanales
colors = [x for x in dir(cv2) if x.startswith('COLOR_')]
print(colors[:5])
col_1 = cv2.imread(img, cv2.COLOR_BAYER_BG2RGB)
cv2.imshow("1", col_1)
cv2.waitKey() 