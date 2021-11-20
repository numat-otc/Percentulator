from tkinter import *  # tkinter library
import os  # windows terminal commands

root = Tk()
root.title("🔺% Calc")  # empty title ("tk" by default)
# root.geometry('350x450+700+200') # Change window size

# GUI
Label(text="Percentage Change Calculator").grid(column=2)  # title

number1_text = Label(text="Value One [x]").grid(column=2)
number1_input = Entry(); number1_input.grid(column=2)

number2_text = Label(text="Value Two [y]").grid(column=2)
number2_input = Entry(); number2_input.grid(column=2)


# calculate function
def Calculate():
    # check if all variables are valid types
    try:
        num1 = float(number1_input.get())
        num2 = float(number2_input.get())

    except:
        os.system('msg "%username%" Error: input value(s) invalid, must be a number.')
        return

    Result1 = round((num2 / num1), 2)  # x Multiplier
    Result2 = round((num2 / num1 - 1) * 100, 2)  # % Change
    Result3 = round((num2 / num1 - 1) * 100 + 100, 2)  # % From Initial

    if Result2 > 0:
        incdec = "increase"
    else:
        incdec = "decrease"; Result2 = -Result2

    print(Result1, Result2, Result3)

    Label(text="X to Y Transformations:"
               "\nx{} multiplier"
               "\n{}% {}"
               "\n{}% of value x".format(Result1, Result2, incdec, Result3)).grid(row=7, column=2)


root.bind('<Return>', lambda event: Calculate())  # calculate when press ENTER
calculate_button = Button(text="Calculate", command=Calculate).grid(column=2)  # calculate button

root.mainloop()
