from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import os
import re
import cv2
# import face_recognition

txtfolder = ""

frame = Tk()
frame.title("Hello")

lab1 = tkinter.Label(frame, text="Nhập đường dẫn file ảnh", fg="red")
lab1.grid(column=0, row=0)
lab2 = tkinter.Label(frame, text="Chọn file ảnh", fg="red")
lab2.grid(column=1, row=0)

txt = Entry(frame, width=20)
txt.grid(column=0, row=1)

combo = Combobox(frame)
combo.grid(column=1, row=1)

# Ham xu ly anh!!!!!!!!!!!!!!!!!!!!
def xulyanh(pic):
    img = cv2.imread(pic)
    cv2.imshow('Old image', img)
    # image = face_recognition.load_image_file(pic)
    # face_locations = face_recognition.face_locations(image)
    cv2.waitkey(0)
    return

def btnclick():
    global txtfolder
    txtfolder = txt.get()
    try:    
        combo['value'] = os.listdir(txtfolder)
        combo.current(0)
    except:
        messagebox.showinfo("Lỗi", "Không tồn tại folder như vậy.")
    return

def btncomboclick():
    global imgpath
    imgpath = txtfolder + "\ " + combo.get()
    imgpath = imgpath.replace(' ', '')
    xulyanh(imgpath)
    return

btn = tkinter.Button(frame, text="Chọn folder", command=btnclick)
btn.grid(column=0, row=2)

btncombo = Button(frame, text="Hiển thị", command=btncomboclick)
btncombo.grid(column=1, row=2)

frame.mainloop()