import cv2
import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector
import serial
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detect = HandDetector(detectionCon=0.8,maxHands=1)
10
ms=cvzone.SerialModule.SerialObject("COM2",9600,1)
while True:
stat,img = cap.read()
img = cv2.flip(img, 1)
hand,img = detect.findHands(img,flipType=False)
if hand:
h=hand[0]
f = detect.fingersUp(h)
if f[0]==1:
f[0]=0
else:
f[0]=1
ans=""
for i in f:
ans+=str(i)
print(ans)
ms.sendData(ans)
cv2.imshow("image",img)
cv2.waitKey(1)