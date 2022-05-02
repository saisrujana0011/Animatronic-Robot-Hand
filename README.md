# Animatronic-Robot-Hand
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
