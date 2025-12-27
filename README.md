# Smart AI Object Identifier 🤖
***A camera with a 3D printed case controlled by a raspberry pi, identifying what's in front of it and then displaying it on an LCD***

<img width="2000" height="1500" alt="image" src="https://github.com/user-attachments/assets/9a818459-087f-43e4-8150-e9734a9b3013" />

**Video of it in action:**

![identifier](https://github.com/user-attachments/assets/c4363cb5-11ea-4132-8c17-6c0c5335510e)
## What is it?

There is a raspberry pi 5 which runs object recognition, and this is connected to an arducam whose case I have 3D printed.
The raspberry pi 5 is also connected to an LCD display. When something is placed in front, the camera detects it, labels it, then that label is displayed 
on the LCD.

## Why?

The process of identifying something using a camera and then acting has many applications. One of these is a manufacturing line where this could be used to identify defects then stop to grab the 
defected peice. Other than that, designing the camera model was a great way for me to learn CAD. Most computer vision systems display what was identified on the computer, so this LCD instantaneously 
displaying it makes it feel more magical. 

## Structure

*Case model* has the files for the camera case, and the *Failed model* contains the old 3d model for the case, but did not work because its dimensions were not correct.
Assembly and Assembly-2 both have details on how I made it, the commands I ran, more problems I faced, and details of how I accomplised it.

<img width="788" height="782" alt="image" src="https://github.com/user-attachments/assets/0dc004d1-1968-4157-ba96-7ccd679417cb" />
<img width="1197" height="735" alt="image" src="https://github.com/user-attachments/assets/c8e24c35-d99d-4a11-a355-7f4dd64bb94a" />
<img width="760" height="785" alt="image" src="https://github.com/user-attachments/assets/b5702b40-9efb-4a16-90f7-3f10a57bf691" />
<img width="551" height="691" alt="image" src="https://github.com/user-attachments/assets/8d5e353c-7d75-46c8-80ab-54fe8dd17a23" />


<img width="3000" height="3407" alt="identifier" src="https://github.com/user-attachments/assets/3a5c2cff-6de7-4fbf-b759-a4464bd7d593" />


<img width="1036" height="240" alt="image" src="https://github.com/user-attachments/assets/ec6daa46-1642-4f36-bf63-9e3f7465944e" />


Smart AI Object Identifier is a simple yet useful project that uses computer vision and a camera with a 3d printed case to identify objects then displays them on the lcd.
