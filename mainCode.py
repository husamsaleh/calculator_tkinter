from tkinter import *
import tkinter.messagebox
from tkinter import Tk
from pygame import mixer
from tkinter import Button,Menu ,Label,Frame
import math
from sympy import *

root = Tk()
root.iconbitmap(default="hm.ico")
root.title("Calculator")
root.configure(background='#34495e')
root.geometry('380x540')
root.resizable(False, False)

DISPLAY = Label(root, width=57, height=5)

#images////////////////////////////////////////////////////////////////////start

divide_image = PhotoImage(file='div_img.png')
img_label_d = Label(image=divide_image)

plus_image = PhotoImage(file='plus_img.png')
img_label_p = Label(image=plus_image)

sub_image = PhotoImage(file='subtract_img.png')
img_label_s = Label(image=sub_image)

mult_image = PhotoImage(file='multiply_img.png')
img_label_m = Label(image=mult_image)

eql_img = PhotoImage(file='equal_img.png')
img_label_e = Label(image=eql_img)

clear_img = PhotoImage(file='clear_img.png')
img_label_c = Label(image=clear_img)

dot_img = PhotoImage(file='dot.png')
img_label_dot = Label(image=dot_img)

x2_img = PhotoImage(file='x2.png')
img_label_x2 = Label(image=x2_img)

b2_img = PhotoImage(file='b2.png')
img_label_b2 = Label(image=b2_img)

back_img = PhotoImage(file='back_space_img.png')
img_label_back = Label(image=back_img)

brak_l = PhotoImage(file='bracket1L.png')
img_label_brackl = Label(image=brak_l)

brak_r = PhotoImage(file='bracket2r.png')
img_label_brackr = Label(image=brak_r)

sqt_img = PhotoImage(file='sqrt_img.png')
img_label_sqt = Label(image=sqt_img)

#images////////////////////////////////////////////////////////////////////end

def new(): tkinter.messagebox.showinfo('Calculator', 'you can also press C')

def helpo(): tkinter.messagebox.showinfo('About' , 'The calculator was made by Husam Saleh using only Python TKinter, hopefully, it will make your work more efficient ')

def mute_music(): global muted
mixer.music.set_volume(0)

def unmute_music(): global unmute
mixer.music.set_volume(0.5)

def lower(): global unmute
mixer.music.set_volume(0.2)

#***** Main Menu start*****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu ,tearoff=False)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Restart", command=lambda: [new(),bt_clear()])
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

audio = Menu(menu, tearoff=False)
menu.add_cascade(label="audio", menu=audio)

mute = Menu(menu, tearoff=False)
audio.add_command(label="Mute", command=mute_music)

unmute = Menu(menu, tearoff=False)
audio.add_command(label="unmute", command=unmute_music)

low = Menu(menu, tearoff=False)
audio.add_command(label="Lower Audio", command=lower)

about = Menu(menu, tearoff=False)
menu.add_cascade(label="About" ,command=helpo )

#***** Main Menu end *****

#***** Toolbar start *****

toolbar = Frame(root, bg="light blue")
toolbar.grid()

#***** Toolbar end *****

mixer.init()
expression = ""
input_text = StringVar()
input_text2 = StringVar()

#Let us create a frame for the input field
input_frame = Frame(root, width=20, height=20, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.grid(row=0, column=0 ,columnspan=3)

#Let us create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 16, 'bold'), textvariable=input_text, width=20, bg="#eee", bd=0,justify=RIGHT)
input_field.grid(row=0, column=0 ,columnspan=3 )
input_field.grid(ipady=10)

#/// input_frame2 = Frame(root, width=4, height=5, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2) input_frame2.grid(row=0, column=3 ,columnspan=1)

#Let us create a input field inside the 'Frame'
input_field2 = Entry(input_frame2, font=('arial', 10, 'bold'), textvariable=input_text2, width=5, bg="#eee", bd=0,justify=LEFT)
input_field2.grid(row=0, column=3 ,columnspan=1)
input_field2.grid(ipady=2)

def p_music(): mixer.music.load("clear_click.mp3")
mixer.music.play()

def num_music(): mixer.music.load("numbers_click.mp3")
mixer.music.play()

def eq_music(): mixer.music.load("equal_click.mp3")
mixer.music.play()

def op_music(): mixer.music.load("op_music.mp3")
mixer.music.play()

def btn_click(item): global expression
expression = expression + str(item)
input_text.set(expression)

def sqrt(): global expression
expression = math.sqrt(float(expression))
input_text.set(float(expression))
expression = str(expression)

def cos(): global expression
expression = float(expression)
expression = round(math.cos(math.radians(expression)), 5)
input_text.set(float(expression))
expression = str(expression)

def sin(): global expression
expression = float(expression)
expression = round(math.sin(math.radians(expression)), 5)
input_text.set(float(expression))
expression = str(expression)

def tan(): global expression
expression = float(expression)
expression = round(math.tan(math.radians(expression)), 5)
input_text.set(float(expression))
expression = str(expression)

def bt_clear(): global expression
expression = ""
input_text.set("")
input_text2.set("")

def bt_equal(): global expression
result = str(eval(expression))
# 'eval':This function is used to evaluates the string expression directly input_text.set(result)

#if input_text == result:
 #   return bt_clear()
def oss(): global expression
expo = str(expression)
input_text.set("**")

def c_input(): global expression
input_text2.set(str("cos"))

def s_input(): global expression
input_text2.set(str("sin"))

def t_input(): global expression
input_text2.set(str("tan"))

def ro_input(): global expression
input_text2.set(str("root"))

def backspace(): global expression
expression = expression[:-1]
input_text.set(expression)

num1 = Button(root, text="1", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", activebackground="red", command=lambda: [btn_click(1)])
num1.grid(row=3, column=0)

num2 = Button(root, text="2", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [btn_click(2)])
num2.grid(row=3, column=1)

num3 = Button(root, text="3", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(3)])
num3.grid(row=3, column=2)

num4 = Button(root, text="4", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [btn_click(4)])
num4.grid(row=2, column=0)

num5 = Button(root, text="5", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(5)])
num5.grid(row=2, column=1)

num6 = Button(root, text="6", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(6)])
num6.grid(row=2, column=2)

num7 = Button(root, text="7", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(7)])
num7.grid(row=1, column=0)

num8 = Button(root, text="8", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(8)])
num8.grid(row=1, column=1)

num9 = Button(root, text="9", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(9)])
num9.grid(row=1, column=2)

num0 = Button(root, text="0", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(0)])
num0.grid(row=4, column=0)

#operations//////////////////////////////////////////////////////////////////////////////////////

button_add = Button(root, image=plus_image, height=65,width=88, bg="#ecf0f1",cursor="tcross" , command=lambda:[btn_click("+")])
button_add.grid(row=4, column=1)

button_sub = Button(root, image=sub_image, height=65,width=88, bg="#ecf0f1" ,cursor="hand1", command=lambda:[btn_click("-")])
button_sub.grid(row=4, column=2)

button_mult = Button(root, image=mult_image, height=65,width=88, bg="#ecf0f1" , cursor="X_cursor", command=lambda:[btn_click("*")])
button_mult.grid(row=5, column=0)

button_dev = Button(root, image=divide_image, height=65,width=88, bg="#ecf0f1" ,cursor="hand1", command=lambda:[btn_click("/")] )
button_dev.grid(row=6, column=0)

#operations//////////////////////////////////////////////////////////////////////////////////////

button_equal = Button(root, image=eql_img, height=65,width=88, bg="#bdc3c7" , cursor="circle ", command=lambda:[ p_music(),bt_equal()])
button_equal.grid(row=5, column=1, columnspan=1)

button_clear = Button(root, image=clear_img, height=65,width=380, bg="#ecf0f1" , cursor="diamond_cross", command=lambda:[p_music(),bt_clear()])
button_clear.grid(row=7, column=0, columnspan=4 )

DOT_BUTTON = Button(root, image=dot_img, height=65,width=95, bg="#ecf0f1", cursor="hand1" , command = lambda: btn_click(".") )
DOT_BUTTON.grid(row=2, column=3,columnspan=1 )

Exponentiation = Button(root, image=b2_img, height=65,width=95, bg="#ecf0f1" , cursor="hand1",command = lambda: oss() ) #btn_click("**") Exponentiation.grid(row=1, column=3)

braket_l = Button(root, image=brak_l, height=65, width=88, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ btn_click(")")])
braket_l.grid(row=6, column=2)

braket_r = Button(root, image=brak_r,height=65, width=88,bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [btn_click("(")])
braket_r.grid(row=6, column=1)

ro_ot = Button(root, image=sqt_img, height=65, width=95, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ sqrt(),ro_input()])
ro_ot.grid(row=3, column=3)

button_cos = Button(root, text="cos", height=4, width=13, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [cos(),c_input() ])
button_cos.grid(row=4, column=3)

button_sin = Button(root, text="sin", height=4, width=13, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ sin() ,s_input()])
button_sin.grid(row=5, column=3)

button_tan = Button(root, text="tan", height=4, width=12, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ tan(),t_input()])
button_tan.grid(row=5, column=2)

back_space = Button(root, image=back_img, height=65, width=95, bg="#ecf0f1", fg="black", cursor="hand2", command=lambda: [ backspace()])
back_space.grid(row=6, column=3)

root.mainloop()
