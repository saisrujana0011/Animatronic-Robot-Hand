# Animatronic-Robot-Hand

I. INTRODUCTION 

Animatronics is a hybrid of animation and electronics. It can 
be pre-customized (programming) or remotely controlled. It 
is the utilization of link pulled gadgets or actuators to quicken 
a reproduction of a human or a creature or carry similar 
attributes, in any case, lifeless thing. Robot hands are 
intended to realize the same dexterous and versatile 
manipulation that we humans can do. Thus, for robot-hand 
research, understanding the anatomy and motion of the 
human hand is fundamental. On the other hand, from the point 
of view of human-hand research, describing the mechanisms 
and mechanics behind hand posture and motion helps to 
understand how we realize such dexterous and versatile 
manipulations. However, there is a wide gap between robotic 
and human informatics, and it is difficult to interchange the 
diverse knowledge accumulated in each research field 
directly. We have been involved in digital-hand research for 
more than a decade. The goal of this project is to simulate the 
animatronic hand using Image processing for promoting 
ergonomic product design, taking the individual differences 
in hand properties into account. Interestingly, this robot hand 
is applicable to not only ergonomic product design as 
previously described but to interface the flexible human-like 
motions. For example, a simple animatronic model with 
image processing libraries enabled us to reproduce the motion 
of the human hand. The 5 finger movements chosen for this 
project were: 1)Thumb open 2) Index finger open 3) Middle 
finger open 4) Ring finger open 5) Pinky finger Open and 
many combinations. In this project, we used OpenCV for 
hand recognition. OpenCV is free for use, crossplatform 
library of programming functions that mainly work on realtime computer vision. Along with OpenCV, we use The 
Proteus Design Suite which is a proprietary software tool 
suite used primarily for electronic design simulation where 
we simulated Arduino UNO which is an open-source 
microcontroller board based on an 8-bit ATMega328P 
microcontroller with an operating voltage of 5V and clock 
speed of 16MHz. It has 6 analog I/O pins and 14 digital I/O 
pins and is programmable with the Arduino IDE (Integrated 
Development Environment), via a type B USB Cable. PWM 
Servo Motor is simulated to represent each finger in proteus. 
The PWM sent to the motor determines the position of the 
shaft, and based on the duration of the pulse sent via 2 the 
control wire; the rotor will turn to the desired position which 
represents the status of the finger. 






II. BLOCK DIAGRAM


![image](https://user-images.githubusercontent.com/91731751/166305552-098d570c-2b5f-4f05-b61a-b0454b7f6727.png)

Image Acquisition generally deals with the action of 
retrieval of image from a source , usually hardware like 
cameras, sensors etc. Then the data acquired is sent through 
the process of hand and finger detection which is then sent 
through the virtual COM port created by the VSPE software 
interfaced with physical interface COMPIM given to the 
servos. Whatever the gestures provided at the input are been 
reflected as the movement of servos motors which 
represents the hands of Robot.

III . METHODOLOGY 

Hand tracking module utilizes ML pipeline consisting of two 
models : 
1.Palm detector 
2.Hand landmark 

A. PALM DETECTION 
To detect initial hand locations, we employ a single shot 
detector (SSD) model for real-time application. 
The core of SSD is predicting category scores and box offsets 
for a fixed set of default bounding boxes using small 
convolutional filters applied to feature maps. 
SSD has two components: a backbone model and SSD head. 
Backbone model usually is a pre-trained image classification 
network as a feature extractor. 
The backbone model is based on a standard architecture used 
for high quality image classification 
The SSD head is where the hand is detected. 

![image](https://user-images.githubusercontent.com/91731751/166306232-a7f2797a-6916-4583-a7c5-8df862f1915a.png)


B. HAND LANDMARKING

![image](https://user-images.githubusercontent.com/91731751/166306319-e2b2ea61-1b94-4f92-938f-2884104075e7.png)


Basically, the MediaPipe uses a single-shot palm detection 
model and once that is done it performs precise key point 
localization of 21 3D palm coordinates in the detected hand region.The MediaPipe pipeline utilizes multiple models like, 
a palm detection model that returns an oriented hand 
bounding box from the full image. The cropped image 
region is fed to a hand landmark model defined by the palm 
detector and returns high-fidelity 3D hand key points.

![image](https://user-images.githubusercontent.com/91731751/166306429-fefd50ab-8f41-4a7f-8b8b-fa89e4740b64.png)


They start with a small set of labelled hand images and use a 
neural network to get rough estimates of the hand keypoints. 
They have a huge multi-view system set up to take images 
from different view-points or angles comprising of 31 HD 
cameras.They pass these images through the detector to get 
many rough keypoint predictions. Once you get the detected 
keypoints of the same hand from different views, keypoint 
triangulation is performed to get the 3D location of the 
keypoints. The 3D location of keypoints is used to robustly 
predict the keypoints through reprojection from 3D to 2D. 
This is especially crucial for images where keypoints are 
difficult to predict. This way they get a much improved 
detector in a few iterations.In summary, they use keypoint 
detectors and multi-view images to come up with an 
improved detector. The detection architecture used is similar 
to the one used for body pose. The main source of 
improvement is the multi-view images for the labelled set of 
images. 


IV. DETECTOR FLOW 

![image](https://user-images.githubusercontent.com/91731751/166306550-bb3cb0c4-24e4-4506-82b1-99233c47c241.png)


The coordinates of the hand key points are obtained, through 
distance calculations we can generate hand data according to 
its state. A simulation network of animatronic hand is 
designed in proteus. To pass this hand data to the animatronic 
hand physically we use serial communication port. For 
simulation we use a serial port which works virtually. 
The Virtual Serial port emulator is used to create a virtual port 
The emulator generates COM port drivers even without 
physical COM port. COMPIM is used to model physical 
COM interfaces in proteus. Now that we have a port in virtual 
the COMPIM uses it to communicate virtually. The arduino 
is ready to read the data from the COM and react accordingly. 



