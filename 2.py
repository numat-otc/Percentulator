from tkinter import *  # tkinter library
from tkinter import messagebox

root = Tk()
root.title("🔺% Calc")  # empty title ("tk" by default)
# root.geometry('350x450+700+200') # Change window size

# GUI
Label(text="Percentage Change Calculator").grid(column=2)  # title

valx_text = Label(text="Value One [x]").grid(column=2)
valx_input = Entry(); valx_input.grid(column=2)

valy_text = Label(text="Value Two [y]").grid(column=2)
valy_input = Entry(); valy_input.grid(column=2)

valm_text = Label(text="Multiplier [*]").grid(column=2)
valm_input = Entry(); valm_input.grid(column=2)

valc_text = Label(text="Percent Change [🔺%]").grid(column=2)
valc_input = Entry(); valc_input.grid(column=2)

valp_text = Label(text="Percentage [%]").grid(column=2)
valp_input = Entry(); valp_input.grid(column=2)


# calculate function
def Calculate():
    # check if all variables are valid types
    try:
        x = float(valx_input.get())
        y = float(valy_input.get())

    except:
        messagebox.showinfo(title="error",message="Error: input value(s) invalid, must be a number.")
        return

    Result1 = round((y / x),                    2)  # x Multiplier
    Result2 = round((y / x - 1) * 100,          2)  # % Change
    Result3 = round((y / x - 1) * 100 + 100,    2)  # % From Initial

    if Result2 > 0:
        incdec = "increase"
    else:
        incdec = "decrease"; Result2 = -Result2

    print(Result1, Result2, Result3)

    Label(text="X to Y Transformations:"
               "\nx{} multiplier"
               "\n{}% {}"
               "\n{}% of value x".format(Result1, Result2, incdec, Result3)).grid(row=13, column=2)


root.bind('<Return>', lambda event: Calculate())  # calculate when press ENTER
calculate_button = Button(text="Calculate", command=Calculate).grid(column=2)  # calculate button


root.mainloop()
