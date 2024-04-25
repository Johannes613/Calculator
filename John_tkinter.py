#John Calculator
import tkinter

wind=tkinter.Tk()
wind.title("Calculator")

wind.geometry("290x400")
result=tkinter.Entry(wind,width=45,borderwidth=7)
result.grid(row=0,column=0,columnspan=3)

def click(number):
    current=result.get()
    result.delete(0, tkinter.END)
    result.insert(0,str(current)+str(number))

def add():
    first_number=result.get()
    global f_use
    f_use=int(first_number)
    global math
    math="addition"
    result.delete(0, tkinter.END)
def subtract():
    first_number=result.get()
    global f_use
    f_use=int(first_number)

    global math
    math="subtraction"
    result.delete(0,tkinter.END)

def clear():
    result.delete(0,tkinter.END)
def multiply():
    first_number=result.get()
    global f_use
    f_use=int(first_number)
    global math
    math="multiplication"
    result.delete(0, tkinter.END)
def divide():
    first_number=result.get()
    global f_use
    f_use=int(first_number)
    global math
    math="division"
    result.delete(0, tkinter.END)

def equal():
    second_number=result.get()
    result.delete(0,tkinter.END)
    if math=="addition":
        result.insert(0,int(f_use) + int(second_number))
    if math=="subtraction":
        result.insert(0,int(f_use) - int(second_number))
    if math=="multiplication":
        result.insert(0,int(f_use) * int(second_number))
    if math=="division":
        result.insert(0,int(f_use) / int(second_number))

button_1=tkinter.Button(wind,text="1",padx=40,pady=15,command=lambda: click(1))
button_2=tkinter.Button(wind,text="2",padx=40,pady=15,command=lambda: click(2))
button_3=tkinter.Button(wind,text="3",padx=40,pady=15,command=lambda: click(3))
button_4=tkinter.Button(wind,text="4",padx=40,pady=15,command=lambda: click(4))
button_5=tkinter.Button(wind,text="5",padx=40,pady=15,command=lambda: click(5))
button_6=tkinter.Button(wind,text="6",padx=40,pady=15,command=lambda: click(6))
button_7=tkinter.Button(wind,text="7",padx=40,pady=15,command=lambda: click(7))
button_8=tkinter.Button(wind,text="8",padx=40,pady=15,command=lambda: click(8))
button_9=tkinter.Button(wind,text="9",padx=40,pady=15,command=lambda: click(9))
button_0=tkinter.Button(wind,text="0",padx=40,pady=15,command=lambda: click(0))
button_equal=tkinter.Button(wind,text="=",padx=88,pady=15,command=equal)
button_clear=tkinter.Button(wind,text="Clear",padx=78,pady=15,command=clear)
button_add=tkinter.Button(wind,text="+",padx=40,pady=15,command=add)
button_subtract=tkinter.Button(wind,text="-",padx=40,pady=15,command=subtract)
button_multiply=tkinter.Button(wind,text="*",padx=40,pady=15,command=multiply)
button_divide=tkinter.Button(wind,text="/",padx=40,pady=15,command=divide)


button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_subtract.grid(row=6,column=2)
button_multiply.grid(row=6,column=0)
button_divide.grid(row=6,column=1)

wind.mainloop()







