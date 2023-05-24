import tkinter as tk

def show_output():
    number = int(number_input.get())

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack()
number_input = tk.Entry(master=window)
number_input.pack()
go_button = tk.Button(
    master=window, text='ผลลัพ' ,
    command=show_output
    )
go_button.pack()
output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()