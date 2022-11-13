#EXPERIMENTAL ANALYSIS

#Create a module naming cvzone using OpenCV and Mediapipe


import cv2
import mediapipe as mp
import math

class HandDetector:
   
    def __init__(self, mode=False,maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,min_detection_confidence=self.detectionCon, min_tracking_confidence = self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True, flipType=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        if  self.results.multi_hand_landmarks:
            for handType,handLms in zip(self.results.multi_handedness,self.results.multi_hand_landmarks):
                myHand={}
                ## lmList
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py = int(lm.x * w), int(lm.y * h)
                    mylmList.append([px, py])
                    xList.append(px)
                    yList.append(py)
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] =  (cx, cy)

                if flipType:
                    if handType.classification[0].label =="Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:myHand["type"] = handType.classification[0].label
                allHands.append(myHand)

                ## draw
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),(bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),(255, 0, 255), 2)
                    cv2.putText(img,myHand["type"],(bbox[0] - 30, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN,2,(255, 0, 255),2)
        if draw:
            return allHands,img
        else:
            return allHands

    def fingersUp(self,myHand):
        myHandType =myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers



#We can install cvzone package to get the module in prior.




#Create the main file and import the above module


import cv2
import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector
import serial
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detect = HandDetector(detectionCon=0.8,maxHands=1)
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

#Record Code 
#-------------

import cv2
import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector
import serial
 
fi = open('record.txt', 'x')
 
 
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
 
detect = HandDetector(detectionCon=0.8,maxHands=1)
ms=cvzone.SerialModule.SerialObject("COM6",9600,1)
 
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
        fi.write(ans+"\n")
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
#A File named record.txt will be created. Content being the data generated. Only the data will be recorded but not the frames of the given input.

#Playback Code 
#-----------------

import time
import serial
import cvzone.SerialModule
import cv2
 
ms=cvzone.SerialModule.SerialObject("COM6",9600,1)
 
with open('readme.txt', 'r') as f:
    for i in range(100):
        s=f.readline()
        print(s)
        ms.sendData(s)
        time.sleep(0.5)
