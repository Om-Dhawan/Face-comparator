import cv2
import face_recognition
import numpy as np

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:",
                                          title="Please pick an image",
                                          filetypes= (("all files","*.*"),
                                            ("jpeg","*.jpeg"),("jpg","*.jpg"),("png","*.png")
                                            ))

    return filepath

window = Tk()
button = Button(text="Open Image",command=openFile)
button.pack()

i1 = openFile()
img = cv2.imread(i1)

# scale_percent = 50 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)  
img = cv2.resize(img, (640,480), interpolation = cv2.INTER_AREA)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

i2 = openFile()
img2 = cv2.imread(i2)

# scale_percent = 50 # percent of original size
# width = int(img2.shape[1] * scale_percent / 100)
# height = int(img2.shape[0] * scale_percent / 100)
# dim = (width, height)  
img2 = cv2.resize(img2, (640,480), interpolation = cv2.INTER_AREA)

rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

# cv2.imshow("Img", img)
# cv2.imshow("Img 2", img2)
imgStack=cv2.hconcat([img,img2])
# imgStack = img2
if True in result:
    cv2.putText(imgStack, "Person in both images is same", (430, 50), 2, 1, (0,0,0), 5, cv2.LINE_AA)
    cv2.putText(imgStack, "Person in both images is same", (430, 50), 2, 1, (70, 155, 30), 2, cv2.LINE_AA)
else:
    cv2.putText(imgStack, "Person in both images is NOT same", (400, 50), 2, 1, (0,0,0), 5, cv2.LINE_AA)
    cv2.putText(imgStack, "Person in both images is NOT same", (400, 50), 2, 1, (40, 55, 210), 2, cv2.LINE_AA)
cv2.imshow("Result", imgStack)
cv2.waitKey(0)