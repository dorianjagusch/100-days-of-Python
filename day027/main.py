import readline
import tkinter as t

window = t.Tk()
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)
window.title("Miles to Km Converter")

miles_input = t.Entry(width=9)
miles_input.grid(row=0, column=1)

miles_label = t.Label(text="Miles")
miles_label.grid(row=0, column=2)

equality_label = t.Label(text="is equal to")
equality_label.grid(row=1, column=0)

result_label = t.Label(text="0")
result_label.grid(row=1, column=1)

km_label = t.Label(text="Km")
km_label.grid(row=1, column=2)


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


calc_button = t.Button(text="Calculate", command=convert)
calc_button.grid(row=2, column=1)

window.mainloop()