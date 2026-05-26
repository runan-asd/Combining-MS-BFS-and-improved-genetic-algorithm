import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox, Canvas,font
import os
from database import db
from mainpage import MainPage

class LoginPage:
    
    def  __init__(self,master):

        self.root = master
        self.font_1 = font.Font(family='宋体', size=36, weight='bold')
        self.font_2 = font.Font(family='微软雅黑', size=18, weight='normal')
        self.root.geometry('1000x625')
        self.root.resizable(0, 0)
        self.root.title('登录')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.page = tk.Frame(self.root)
        self.page.pack()

        self.canvas = Canvas(self.page, width=1080,height=667)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\登录背景改.jpg")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()


        self.inp_1 = tk.Entry(self.page,textvariable=self.username,font=self.font_2,foreground="#000000",bg="#FFFFFF")
        self.inp_2 = tk.Entry(self.page,textvariable=self.password,font=self.font_2,foreground="#000000",bg="#FFFFFF", show='*')

        self.butt1 = tk.Button(self.page, text='登录',font=self.font_2,command=self.login)
        self.butt2 = tk.Button(self.page, text='退出',font=self.font_2,command=self.root.destroy)

        self.canvas.create_window(600, 267, width=400, height=40,window=self.inp_1)
        self.canvas.create_window(600, 352, width=400, height=40,window=self.inp_2)
        self.canvas.create_window(300, 500, width=75, height=40,window=self.butt1)
        self.canvas.create_window(700, 500, width=75, height=40,window=self.butt2)

    def login(self):
        
        name = self.username.get()
        pwd = self.password.get()
        flag,massage = db.check_login(name,pwd)
        
        if flag:
            self.page.destroy()
            MainPage(self.root)
        else:
            messagebox.showwarning(title='警告', message=massage)

if __name__ == '__main__':
        root = tk.Tk()
        LoginPage(master=root)
        root.mainloop()
