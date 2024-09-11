#calculator using tkinter GUI

#import everything from tkinter module
from tkinter import *

#declaring global expression variable
expression = ""

# function for updating expression
def press(num):
    global expression

    #joining of string
    expression = expression + str(num)

    equation.set(expression)
#function to evaluate the final expresion
def equalpress():
    # try and except statement is used for handeling errors
    try:
        global expression
        #eval function to evaluate
        #str function to convert to string
        total=str(eval(expression))

        equation.set(total)

        #initialize the expresion variable
        expression= ""

    # if error generates then handle by except block
    except:
        equation.set("error")
        expression = ""


#function to clear contents in text feild
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    # creating GUI
    gui = Tk()
    gui.configure(background="light green")#setting background colour
    gui.title("simple calculator")#setting title
    gui.geometry("370x250")#setting configuration of window

    #we create an instance of this variable class
    equation = StringVar()

    #creating text field
    expression_field = Entry(gui,textvariable=equation)

    #grid method is used for styling
    expression_field.grid(columnspan=4, ipadx=70)

    # creating buttons and adding function to it
    button1 = Button(gui, text='1', fg='black', bg='blue', command=lambda: press(1), height=1, width=10)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='2', fg='black', bg='blue', command=lambda: press(2), height=1, width=10)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='3', fg='black', bg='blue', command=lambda: press(3), height=1, width=10)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text='4', fg='black', bg='blue', command=lambda: press(4), height=1, width=10)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='5', fg='black', bg='blue', command=lambda: press(5), height=1, width=10)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='6', fg='black', bg='blue', command=lambda: press(6), height=1, width=10)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text='7', fg='black', bg='blue', command=lambda: press(7), height=1, width=10)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='8', fg='black', bg='blue', command=lambda: press(8), height=1, width=10)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='9', fg='black', bg='blue', command=lambda: press(9), height=1, width=10)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text='0', fg='black', bg='blue', command=lambda: press(0), height=1, width=10)
    button0.grid(row=5, column=0)

    # creating button for operators

    plus = Button(gui, text='+', fg='black', bg='blue', command=lambda: press("+"), height=1, width=10)
    plus.grid(row=2, column=3)

    minus = Button(gui, text='-', fg='black', bg='blue', command=lambda: press("-"), height=1, width=10)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text='*', fg='black', bg='blue', command=lambda: press("*"), height=1, width=10)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text='/', fg='black', bg='blue', command=lambda: press("/"), height=1, width=10)
    divide.grid(row=5, column=3)

    equal = Button(gui, text='=', fg='black', bg='blue', command=equalpress, height=1, width=10)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='clear', fg='black', bg='blue', command=clear, height=1, width=10)
    clear.grid(row=5, column='1')

    decimal = Button(gui, text='.', fg='black', bg='blue', command=lambda: press("."), height=1, width=10)
    decimal.grid(row=6, column=0)

    # start the GUI
    gui.mainloop()