import cv2
import time

#video ismi
video_name="book.mp4"

#video ice aktar: capture,cap
cap=cv2.VideoCapture(video_name)

# Video özelliklerini yazdır
print("Genislik: ",cap.get(3))
print("Yukseklik: ",cap.get(4))

# Eğer video açılmamışsa hata mesajı ver
if cap.isOpened() ==False:
    print("Hata")
    
 #frame, bir video dosyasındaki tek bir görüntü karesini ifade eder. Bir video aslında ardışık olarak gösterilen birçok görüntü karesinden (frame) oluşur.   
 # Video oynatma döngüsü   
while True:    
    ret,frame = cap.read()

    if ret ==True: # Frame başarıyla okunursa
         time.sleep(0.01) # uyari: kullanmazsak cok hizli olur
         cv2.imshow("Video",frame)
         
         # 'q' tuşuna basıldığında çıkış yap
         if cv2.waitKey(1) & 0xFF == ord("q"):
             break

    # Frame okunamazsa (video biterse) döngüden çık
    else: break

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()# stop capture
cv2.destroyAllWindows()
    
