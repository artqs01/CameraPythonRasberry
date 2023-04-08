#!/bin/python3

import tkinter
import customtkinter
import cv2
# from picamera2 import Picamera2
from ui import *

# main window init
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = CameraWindow()
app.geometry("640x480")

app.mainloop()

# cv2.startWindowThread()
# picam2 = Picamera2()
# picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
# picam2.start()

# while True:
#     im = picam2.capture_array()
#     cv2.imshow("Camera", im)
#     cv2.waitKey(1)
    
# cv2.destroyAllWindows()

