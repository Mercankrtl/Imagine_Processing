import cv2
import matplotlib.pyplot as plt

#resmi ice aktarma
img=cv2.imread("ev_gray.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #standart renk düzeni olan BGR'den gri tonlama düzenine dönüşüm yapar.
plt.figure()  #bir grafik figürü oluşturur. 
plt.imshow(img, cmap="gray") 
plt.axis("on")  # Eksenleri açık bırak
#plt.axis("off") #Grafik eksenlerini (x ve y eksenlerini) gizler.
plt.show()

# esikleme (Thresholding İşlemi)
_,thresh_img=cv2.threshold(img,thresh=60 , maxval=255 ,type=cv2.THRESH_BINARY )

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

#_: Threshold fonksiyonu, eşik değerini döner.
#thresh=60: Eşik değeri. Piksel değerleri 0 ile 255 arasında olmalıdır. Bu örnekte, eşik değeri 60 olarak belirlenmiştir.
#type=cv2.THRESH_BINARY: İkili (binary) eşikleme türü. Piksel değerleri şunlara göre belirlenir:
#Eğer piksel değeri eşikten küçükse, piksel değeri 0 yapılır (siyah).
#Eğer piksel değeri eşikten büyük veya eşitse, piksel değeri 255 yapılır (beyaz).




#Adaptive Thresholding (Uyarlamalı Eşikleme) 
thresh_img2= cv2.adaptiveThreshold(img ,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()

#cv2.adaptiveThreshold() Fonksiyonu:Yerel bölgelerdeki parlaklık farklılıklarına bağlı olarak, her piksel için eşik değeri dinamik olarak belirlenir.
#255: Maksimum değer (maxValue): Bir pikselin değeri eşik değerini geçerse bu maksimum değer atanır.Burada, beyaz pikseller için maksimum değer olan 255 kullanılmıştır.
#cv2.ADAPTIVE_THRESH_MEAN_C: Her piksel için eşik değeri, pikselin çevresindeki belirli bir bölgedeki komşu piksellerin ortalaması alınarak hesaplanır.
#type=cv2.THRESH_BINARY: İkili (binary) eşikleme türü. Piksel değerleri şunlara göre belirlenir:
#Eğer piksel değeri eşikten küçükse, piksel değeri 0 yapılır (siyah).
#Eğer piksel değeri eşikten büyük veya eşitse, piksel değeri 255 yapılır (beyaz).







