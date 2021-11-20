from tkinter import *  # tkinter library
from tkinter import messagebox
from fractions import Fraction

root = Tk()
root.title("🔺% Calc")  # empty title ("tk" by default)
# root.geometry('350x450+700+200') # Change window size



# GUI
Label(text="Percentage Change Calculator").grid(column=2)  # title

x_text  = Label(text="Value One [x]").grid(column=2)
x_input = Entry(); x_input.grid(column=2)

y_text  = Label(text="Value Two [y]").grid(column=2)
y_input = Entry(); y_input.grid(column=2)

m_text  = Label(text="Multiplier [*]").grid(column=2)
m_input = Entry(); m_input.grid(column=2)

c_text  = Label(text="Percent Change [🔺%]").grid(column=2)
c_input = Entry(); c_input.grid(column=2)

p_text  = Label(text="Percentage [%]").grid(column=2)
p_input = Entry(); p_input.grid(column=2)

#f_text  = Label(text="Fraction [/]").grid(column=2)
#f_input = Entry(state='disabled'); f_input.grid(column=2)

# calculate function
def Calculate():
    while True:
        # Type 1: x, y
        try:
            x = float(x_input.get())
            y = float(y_input.get())
            break
        except: print("type 1 fail, x or y absent") # debug error

        # Type 2: x, m/c/p
        try:
            x = float(x_input.get())
            while True: # Get a scale for y
                try: # Get m
                    m = float(m_input.get());   y = x * m;              break
                except: pass
                try: # Get c
                    c = float(c_input.get());   y = x * (c / 100 + 1);  break
                except: pass
                try: # Get p
                    p = float(p_input.get());   y = x * (p / 100);      break
                except:
                    print("total fail (2), no scale")
                    messagebox.showinfo(title="error", message="Error: Missing a scaling value: [*],[🔺%],[%]."); return  # debug error
            break
        except: print("type 2 fail, x")# debug error

        # Type 3: y, m/c/p
        try:
            y = float(y_input.get())
            while True: # Get a scale for x
                try: # Get m
                    m = float(m_input.get());   x = y / m;              break
                except: pass
                try: # Get c
                    c = float(c_input.get());   x = y / (c / 100 + 1);  break
                except: pass
                try: # Get p
                    p = float(p_input.get());   x = y / (p / 100);      break
                except:
                    print("total fail (3), no scale")
                    messagebox.showinfo(title="error", message="Error: Missing a scaling value: [*],[🔺%],[%]."); return # debug error

        except:
            print("type 3 fail"); print("total fail, x and y absent") # debug error
            messagebox.showinfo(title="error", message="Error: Missing value one [x] and/or value two [y]")
            return

    m = round((y / x), 2)  # x Multiplier
    c = round((y / x - 1) * 100, 2)  # % Change
    p = round((y / x - 1) * 100 + 100, 2)  # % From Initial
    f = Fraction(int(round(y,0)), int(round(x,0)))
    print(x, y, m, c, p, f) # Debug

    x_input.delete(0, "end"); x_input.insert(0, x)
    y_input.delete(0, "end"); y_input.insert(0, y)
    m_input.delete(0, "end"); m_input.insert(0, "x{}".format(m))
    c_input.delete(0, "end"); c_input.insert(0, "{}%".format(c))
    p_input.delete(0, "end"); p_input.insert(0, "{}%".format(p))
    #f_input.delete(0, "end"); f_input.insert(0, f)

def clear():
    x_input.delete(0, "end")
    y_input.delete(0, "end")
    m_input.delete(0, "end")
    c_input.delete(0, "end")
    p_input.delete(0, "end")


root.bind('<Return>', lambda event: Calculate())  # calculate when press ENTER
calculate_button = Button(text="Calculate", command=Calculate).grid(column=2)  # calculate button
clear_button = Button(text="Clear", command=clear).grid(column=2)  # calculate button

root.mainloop()
