import cv2
import numpy as np

#resim olustur
img= np.zeros((586,586,3),np.uint8)
print(img.shape)
cv2.imshow("Siyah",img)


#cizgi
#(resim,baslangic noktasi,bitis noktasi,renk,kalinlik)
cv2.line(img,(100,100),(100,300),(0,255,0),3) #BGR=(0,255,0)
cv2.imshow("Cizgi",img)

#dikdortgen
#(resim,baslangic,bitis,renk)
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED)
cv2.imshow("Dikdortgen",img)

#Cember
#(resim,merkez,yaricap,renk)
cv2.circle(img,(300,300),45,(0,0,255))
cv2.imshow("Cember",img)

#metin
#(resim,baslangic noktasi,font,kalinligi,renk)
cv2.putText(img,"Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))
cv2.imshow("Metin",img)