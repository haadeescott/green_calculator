from tkinter import *
import tkinter.font as font

root = Tk()
root.title(" GREEN CALCULATOR ")

# entry texbox
e= Entry(root, width=35, borderwidth=5, bg='#C0FFDC')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_cleartext():
    e.delete(0,END)

def button_click(number):
    # e.delete(0, END)
    
    # number will be inserted at the front instead
    # e.insert(0, number)
    # therefore need to reverse order of insertion by converting entry of numbers into string
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    
    # to allow number to be passed outside of function
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
        
    if math == "division":
        e.insert(0, f_num / float(second_number))    
        
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))    
        
def button_subtract():
    first_number = e.get()
    
    # to allow number to be passed outside of function
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    
    # to allow number to be passed outside of function
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    
    # to allow number to be passed outside of function
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


# initialize buttons

myFont = font.Font(weight="bold")

# cannot pass parameters in button, use lambda instead

button_0= Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg= '#59F19B')
button_1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg='#71F9AC')
button_2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg='#71F9AC')
button_3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg='#71F9AC')
button_4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg='#8EFEBF')
button_5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg='#8EFEBF')
button_6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg='#8EFEBF')
button_7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg='#9EFEC8')
button_8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg='#9EFEC8')
button_9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg='#9EFEC8')
button_add= Button(root, text="+", padx=39, pady=20, command=button_add, bg='#47BB7A')
button_equal= Button(root, text="=", padx=96, pady=20, command=button_equal, bg='#47BB7A')
button_clear= Button(root, text="Clear", padx=78, pady=20, command=button_cleartext, bg='#59F19B')

button_subtract= Button(root, text="-", padx=40, pady=20, command=button_subtract, bg= '#3EB673')
button_divide= Button(root, text="÷", padx=40, pady=20, command=button_divide, bg='#3EB673')
button_multiply= Button(root, text="×", padx=40, pady=20, command=button_multiply, bg='#3EB673')

# --------------
button_0['font']=myFont
button_1['font']=myFont
button_2['font']=myFont
button_3['font']=myFont
button_4['font']=myFont
button_5['font']=myFont
button_6['font']=myFont
button_7['font']=myFont
button_8['font']=myFont
button_9['font']=myFont
button_add['font']=myFont
button_equal['font']=myFont
button_clear['font']=myFont
button_subtract['font']=myFont
button_divide['font']=myFont
button_multiply['font']=myFont

# paste buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan= 2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()