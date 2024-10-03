from tkinter import *
import tkinter as tk
from tkinter import ttk
from customtkinter  import *
window = Tk ()
window.title ('ChatBot')
window.geometry('750x700')
micro_icon  = PhotoImage (file= 'tải_xuống__1_-removebg-preview.png')
logo_path = PhotoImage(file = 'logo.png')
send_icon = PhotoImage(file = 'send-icon-2048x1863-u8j8xnb6__1_-removebg-preview.png')
title_label = Label(window,text='ChatBot',fg='pink',font=('.VnCentury Schoolbook',50),width = 16).place(x = 50, y = 0)
entry_histroy = CTkTextbox(window,fg_color ='#912CEE',border_color= '#912CEE' ,height=400,width=700,corner_radius= 32).place(x = 30,y = 80)
entry_command = CTkEntry(window,fg_color ='Violet',border_color='Violet',height=100,width=500,corner_radius= 32).place(x = 30,y = 490)
buton_send = CTkButton(window,image=send_icon,text = 'SEND',height=10,width=10).place(x = 530, y = 490)
buton_listen = CTkButton(window,image=micro_icon,text= 'LISTEN',height=10,width=10).place(x = 630,y = 490)
window.iconphoto(False,logo_path)

window.mainloop()