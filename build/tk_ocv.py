from tkinter import *
from PIL import Image, ImageTk
import cv2
import fast_ocv
# Create an instance of TKinter Window or frame
win = Tk()
cap = fast_ocv.WebcamVideoStream(src=1).start()

# Set the size of the window
win.geometry("1280x720")

# Create a Label to capture the Video frames
img_size = (1184, 624)
label = Label(win)
label.place(x=96, y=96)


# Define function to show frame
def img_tk(cap, img_size):
    frame = cap.read()
    img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(cv2.resize(frame, img_size), cv2.COLOR_BGR2RGB)))
    label.imgtk = img
    label.configure(image=img)
    label.after(1, img_tk, cap, img_size)


img_tk(cap, img_size)
win.mainloop()