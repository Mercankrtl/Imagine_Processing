import cv2

img= cv2.imread("futbol.jpg")
print("Resim boyutu: ",img.shape)
cv2.imshow("Orijinal",img)

#resized
imgResized = cv2.resize (img,(800,422))
print("Resized Img Shape: ",imgResized.shape)
cv2.imshow("Img Resized ", imgResized)

#kirp
imgCropped = img[:100,:200] #width,height -> height,width
cv2.imshow("Kirpik Resim",imgCropped)

