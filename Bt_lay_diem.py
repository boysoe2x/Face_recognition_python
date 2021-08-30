from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter
import os
import re
import cv2
import face_recognition
import threading

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
    try:
        img = cv2.imread(pic)
        cv2.imshow('Old image', img)
        image = face_recognition.load_image_file(pic)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(image)[0]
        cv2.rectangle(image, (face_locations[3], face_locations[0]), (face_locations[1], face_locations[2]), (255, 0, 255), 2)
        cv2.imshow("Face location image", image)
        cv2.waitKey(0)
    except:
        messagebox.showinfo("Lỗi", "Không tồn tại folder như vậy.")
    return

def btnclick():
    global txtfolder
    txtfolder = filedialog.askdirectory()
    txt.delete(0, "end")
    txt.insert(0, txtfolder)
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
    thread = threading.Thread(target=xulyanh, args=(imgpath,))
    thread.start()
    return

btn = tkinter.Button(frame, text="Chọn folder", command=btnclick)
btn.grid(column=0, row=2)

btncombo = Button(frame, text="Hiển thị", command=btncomboclick)
btncombo.grid(column=1, row=2)

frame.mainloop()