from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from win32api import GetSystemMetrics
import tkinter
import os
import re
import cv2
import face_recognition
import threading

txtfolder = ""
txtfolder_out = ""

frame = Tk()
frame.title("Face recognition")

lab1 = tkinter.Label(frame, text="Folder ảnh gốc", fg="red")
lab1.grid(column=0, row=1)
lab2 = tkinter.Label(frame, text="Ảnh gốc", fg="red")
lab2.grid(column=1, row=1)

lab3 = tkinter.Label(frame, text="Folder đã nhận diện", fg="red")
lab3.grid(column=0, row=4)
lab4 = tkinter.Label(frame, text="Ảnh nhận diện", fg="red")
lab4.grid(column=1, row=4)

txt = Entry(frame, width=20)
txt.grid(column=0, row=2)

combo = Combobox(frame)
combo.grid(column=1, row=2)

txt_out = Entry(frame, width=20)
txt_out.grid(column=0, row=5)

combo_out = Combobox(frame)
combo_out.grid(column=1, row=5)

def processing():
    txt_out.delete(0, "end")
    txt_out.insert(0, txtfolder_out)
    btn.configure(state = "disabled")
    btncombo.configure(state = "disabled")
    btncombo_out.configure(state = "disabled")

def complete(listpic_new):
    combo_out['value'] = listpic_new
    combo_out.current(0)
    btn.configure(state = "normal")
    btncombo.configure(state = "normal")
    btncombo_out.configure(state = "normal")

# Ham xu ly anh!!!!!!!!!!!!!!!!!!!!
def xulyanh(listpic):
    processing()
    global txtfolder_out
    global txtfolder
    j = 0
    listpic_new = []
    for pic in listpic:
        try:
            j = j + 1
            listpic_new.append(pic)
            new_pic = txtfolder_out + pic
            pic = txtfolder + pic
            image = face_recognition.load_image_file(pic)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(image)
            a = len(face_locations)
            i = 0
            while i < a:
                cv2.rectangle(image, (face_locations[i][3], face_locations[i][0]), (face_locations[i][1], face_locations[i][2]), (255, 0, 255), 2)
                i = i + 1
            image = re_size(image)
            print(pic)
            cv2.imwrite(new_pic, image)
            cv2.waitKey(0)
        except:
            messagebox.showinfo("Lỗi", "Lỗi nhận diện")
    if(j == len(listpic)):
        messagebox.showinfo("Thông báo", "Hoàn thành nhận diện.")
    complete(listpic_new)
    return

def re_size(image):
    win_w = GetSystemMetrics(0)
    win_h = GetSystemMetrics(1) - 100
    h = image.shape[0]
    w = image.shape[1]
    fw = w/win_w
    fh = h/win_h
    ff = 0
    if fw > fh:
        ff = fw
    else:
        ff = fh
    if ff > 1:
        w = int(w / ff)
        h = int(h / ff)
    image = cv2.resize(image, (w, h))
    return image

def cut_string():
    global txtfolder
    a = 0
    b = 0
    c = 0
    for i in txtfolder:
        if(i == '/'):
            a = b
            b = c
        c = c + 1
    return txtfolder[:a+1]

def btnclick():
    global txtfolder
    global txtfolder_out
    txtfolder = filedialog.askdirectory() + '/'
    txtfolder_out = cut_string()
    txtfolder_out = txtfolder_out + "Images_output/"

    filelist = os.listdir(txtfolder_out)
    for f in filelist:
        os.remove(txtfolder_out + f)

    txt.delete(0, "end")
    txt.insert(0, txtfolder)
    try:    
        combo['value'] = os.listdir(txtfolder)
        combo.current(0)
    except:
        messagebox.showinfo("Lỗi", "Không tồn tại folder như vậy.")

    thread = threading.Thread(target=xulyanh, args=(os.listdir(txtfolder),))
    thread.start()
    return

def btncomboclick():
    pic = txtfolder + combo.get()
    img = cv2.imread(pic)
    img = re_size(img)
    cv2.imshow("Ảnh gốc", img)
    return

def btncombo_outclick():
    pic = txtfolder_out + combo_out.get()
    img = cv2.imread(pic)
    img = re_size(img)
    cv2.imshow("Ảnh đã nhận diện", img)
    return

btn = tkinter.Button(frame, text="Chọn folder", command=btnclick)
btn.grid(column=0, row=3)

btncombo = Button(frame, text="Hiển thị ảnh", command=btncomboclick)
btncombo.grid(column=1, row=3)

btncombo_out = Button(frame, text="Hiển thị ảnh", command=btncombo_outclick)
btncombo_out.grid(column=1, row=6)

frame.mainloop()