import cv2

#ice aktarma
img= cv2.imread("ev.jpg",0) #0 parametresi, resmi gri tonlamada (grayscale) okuma talimatı verir.

#gorsellestir
cv2.imshow("ilk resim",img)

k = cv2.waitKey(0) 

if k ==27 :
    cv2.destroyAllWindows() #tüm açık pencereleri kapatır.
elif k== ord('s'):
    cv2.imwrite("ev_gray.png",img) #gri tonlamalı resmi "ev_gray.png" adıyla kaydeder.
    cv2.destroyAllWindows()
    
    #Bu kod, "ev.jpg" adlı resmi okur, ekranda gösterir ve kullanıcıdan bir tuş girişi bekler. Eğer kullanıcı Esc tuşuna basarsa, pencere kapanır. Eğer 's' tuşuna basarsa, resmi gri tonlamalı olarak "ev_gray.png" olarak kaydeder ve pencere kapanır.






