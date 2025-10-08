# Smart AI Object Identifier

## Overview

This project aims to identify the object in the screenshot taken by a camera using AI and computer vision

## Connecting

There are two main parts:
  - Raspberry Pi 5
  - Arducam

First, unlock the ribbon cable connector on the arducam and pi by lifting the metal hinge on each one. Now choose one end and put it blue face facing the lense of the arducam. Next, put the other end of the cable into the raspberry pi's connector, shiny face facing the pi's
usb ports. Now make sure both ends have fit in snugly and close the hinge by gently tapping it down.

## 3D Case

The Arducam is quite fragile so it needs a case to stand up straight and be suitable for taking images safer and at a better angle.
More details at Assembly.md.

## Using

Once you open the raspberry pi 5 there are some commands to run to ensure the camera is funcioning. Firstly, run **sudo raspi-config** and navigate to settings to enable the camera. Now in the *libcamera library*, a libary used for interacting with cameras there are some basic
commands to run:
  1. libcamera-hello - Displayes a simple preview
  2. libcamera-hello -t 8000 - Display a simple preview for 8000ms or 8s
  3. libcamera-still -o example_image.jpg - Captures an image
  4. libcamera-vid -o example_video.mp4 -t 9000 - Captures a video with a duratio of 9s

## Computer Vison

Need to open Thonny the lightweight python editor. Need to use machine learning libraries like OpenCV and image processing libraries like MatPlotLib but I dont know the exact code because I have not set up hardware yet.
