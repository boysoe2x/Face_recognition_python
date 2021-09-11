from tkinter import *
import tkinter
import cv2
import face_recognition
import PIL.Image , PIL.ImageTk
import time

frame = Tk()
frame.title("Frame opencv")

video = cv2.VideoCapture(0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
canvas = Canvas(frame, width = canvas_w, height = canvas_h, bg = "white")
canvas.pack()

recognition = 1
gray = 0

def face_rec_change():
    global recognition
    recognition = 1 - recognition

def rgbtogray():
    global gray
    gray = 1 - gray

face_rec_btn = tkinter.Button(frame, text = "Face recognition:ON", command = face_rec_change)
face_rec_btn.pack()

gray_btn = tkinter.Button(frame, text = "Gray image:OFF", command = rgbtogray)
gray_btn.pack()

def update_frame():
    global photo
    ret, img = video.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(img)

    if(recognition == 1):
        a = len(face_locations)
        i = 0
        while i < a:
            cv2.rectangle(img, (face_locations[i][3], face_locations[i][0]), (face_locations[i][1], face_locations[i][2]), (255, 0, 255), 2)
            i = i + 1
        face_rec_btn.configure(text = "Face recognition:ON")
    else:
        face_rec_btn.configure(text = "Face recognition:OFF")

    if(gray == 1):
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray_btn.configure(text = "Gray image:ON")
    else:
        gray_btn.configure(text = "Gray image:OFF")

    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
    canvas.create_image(0, 0, image = photo, anchor = tkinter.NW)
    frame.after(20, update_frame)
    
update_frame()
frame.mainloop()