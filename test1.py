import tkinter as tk
from tkinter import ttk

def on_right_click(event):
    item = tree.identify_row(event.y)
    if item:
        menu.post(event.x_root, event.y_root)

def close_menu(event):
    menu.unpost()

root = tk.Tk()

tree = ttk.Treeview(root)
tree["columns"] = ("column1", "column2")
tree.column("#0", width=100, minwidth=100, stretch=tk.NO)
tree.column("column1", width=100, minwidth=100, stretch=tk.NO)
tree.column("column2", width=100, minwidth=100, stretch=tk.NO)

tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("column1", text="Column 1", anchor=tk.W)
tree.heading("column2", text="Column 2", anchor=tk.W)

tree.insert("", "end", text="Item 1", values=("Value 1A", "Value 1B"))
tree.insert("", "end", text="Item 2", values=("Value 2A", "Value 2B"))
tree.insert("", "end", text="Item 3", values=("Value 3A", "Value 3B"))

tree.pack()

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Menu Item 1")
menu.add_command(label="Menu Item 2")

tree.bind("<Button-3>", on_right_click)
root.bind("<Button-1>", close_menu)

root.mainloop()