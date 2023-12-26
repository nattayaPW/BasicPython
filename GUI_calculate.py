#คำนวณราคา

from tkinter import * # Library: TK Interface * คือ import ฟังก์ชั่นหลักทั้งหมด
from tkinter import ttk,messagebox
import pyautogui as pg

GUI = Tk()
GUI.geometry('1000x700') #กำหนดขนาดหน้าจอ
GUI.title('โปรแกรมคำนวณราคาผลไม้')
    
def calculate(x):
    print(x)

def message():
    weigh_1 = input_weigh.get()
    #try ใช้กรณีที่หากทำไม่สำเร็จ หรือติด error ให้ทำ except แทน
    try:
        weigh_2 = float(input_weigh.get())*12
        messagebox.showinfo('ราคาสินค้าทั้งหมด',f'น้ำหนักสินค้า{weigh_1} ราคา*12 = {weigh_2}') 
    except:
        messagebox.showerror('กรอกข้อมูลผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        weigh.focus() #focus ที่ input กรอกผิด
    input_weigh.set('') #set ค่า inputให้ว่าง

""" ใช้ ifelse
    if  input_weigh.get().isnumeric():
        weigh2 = float(weigh)*12
        messagebox.showinfo('ราคาสินค้าทั้งหมด',f'น้ำหนักสินค้า{weigh} ราคา*12 = {weigh2}') 
    else:
        weigh2 = 'ไม่สามารถคำวณได้ กรุณากรอกข้อมูลให้ถูกต้อง'   
            messagebox.showinfo('ราคาสินค้าทั้งหมด',f'ไม่สามารถคำวณได้ กรุณากรอกข้อมูลให้ถูกต้อง')"""


label1 = Label(GUI, text='โปรแกรมคำนวณราคาสินค้า',font=(None,30, 'bold'))

img = PhotoImage(file='pic.png')
img = img.zoom(15) #with 150, I ended up running out of memory
img = img.subsample(32) #mechanically, here it is adjusted to 32 instead of 320

BG = Label(GUI, image=img)

B1 = Button(GUI,text='คำนวณราคา',command=message) #สร้างปุ่มชื่อ คำนวณราคา พอคลิกแล้วเรียกฟังก์ชั่น calculate 
"""B1.pack(ipadx=20, ipady=10, pady=20) 
กำหนดตำแหน่งปุ่ม
B2 = ttk.Button(GUI,text='Calender2',command=calculate)
B2.pack(ipadx=20, ipady=10, pady=20)"""


# name using widget Label
name_label = ttk.Label(GUI, text = 'น้ำหนักสินค้า', font=('calibre',10, 'bold'))
#name_label.pack(ipadx=20, ipady=10, pady=20)  
# creating a entry for input
# name using widget Entry
input_weigh = StringVar() #ใช้เก็บข้อมูลinput
weigh = ttk.Entry(GUI,textvariable = input_weigh, font=('calibre',10,'normal'))


# placing the label and entry in
# the required position using grid
# method

label1.grid(pady=4, padx=5)
BG.grid(row=1,column=0,rowspan=4)
name_label.grid(row=2,column=1)
weigh.grid(row=2,column=2)
B1.grid(row=3,column=2)

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา