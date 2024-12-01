import cv2
import matplotlib.pyplot as plt

#karistirma
# İlk resim yükleniyor ve renk kanalları BGR'den RGB'ye çevriliyor.
img1= cv2.imread("futbol.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)


# İkinci resim yükleniyor ve renk kanalları BGR'den RGB'ye çevriliyor.
img2=cv2.imread("ev.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

# Orijinal img1 ve img2 görselleri gösteriliyor.
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


# Görsellerin boyutları ekrana yazdırılıyor.
print(img1.shape)
print(img2.shape)

# img1 boyutu 200x200 piksele yeniden boyutlandırılıyor.
img1=cv2.resize(img1,(200,200))
print(img1.shape)


# img2 boyutu da 200x200 piksele yeniden boyutlandırılıyor.
img2=cv2.resize(img2,(200,200))
print(img2.shape)

# Yeniden boyutlandırılmış img1 ve img2 görselleri gösteriliyor.
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# İki görüntü belirli ağırlıklarla karıştırılıyor: alpha * img1 + beta * img2
#karistirilmis resim= alpha*img1 + beta*img2
blended=cv2.addWeighted(src1=img1 , alpha=0.5 , src2=img2, beta=0.5 , gamma=0.0)
plt.figure()
plt.imshow(blended)




















