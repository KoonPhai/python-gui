import tkinter as tk

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack()
number_input = tk.Entry(master=window)
number_input.pack()
go_button = tk.Button(master=window, text='ผลลัพ')
go_button.pack()
output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()