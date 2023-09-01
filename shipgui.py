import main
import tkinter as tk

window = tk.Tk()

window.title("Ship of Thesaurus")


window.rowconfigure(0, minsize=800, weight=1)

window.columnconfigure(1, minsize=800, weight=1)



frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

frm_text = tk.Frame(window)

txt_edit = tk.Text(frm_text, font=("Helvetica", 20))

txt_display = tk.Text(frm_text, font=("Helvetica", 20))

def repair():
    new_ship = main.shipofthesaurus(txt_edit.get("1.0", tk.END))
    txt_display.delete("1.0", tk.END)
    txt_display.insert("1.0", new_ship)
    
txt_edit.insert("1.0", "Welcome to the Ship of Thesaurus. Give us a body of \
English text, and we will return it to you completely unchanged.")

repair()

def swap():
    swap_text = txt_display.get("1.0", tk.END)
    swap_display = txt_edit.get("1.0", tk.END)
    txt_display.delete("1.0", tk.END)
    txt_display.insert("1.0", swap_display)
    txt_edit.delete("1.0", tk.END)
    txt_edit.insert("1.0", swap_text)

btn_repair = tk.Button(frm_buttons, text="Repair", font=("Comic Sans MS", 20), command=repair)

btn_swap = tk.Button(frm_buttons, text="Swap", font=("Comic Sans MS", 20), command=swap)

btn_repair.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_swap.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")

frm_text.grid_columnconfigure(0, weight=1)
frm_text.grid_rowconfigure(0, weight = 1)
frm_text.grid_rowconfigure(1, weight = 1)

frm_text.grid(row=0, column=1, sticky='nsew')

txt_edit.grid(row=0, column=0, sticky='nsew')

txt_display.grid(row=1, column=0, sticky='nsew')

window.mainloop()