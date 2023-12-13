import tkinter as tk
from tkinter import ttk

########################################
print(__name__)
########################################
def main():
    root = tk.Tk()
    root.geometry("1200x800")
    myfont=font=('Arial ', 12)
    root.title("Treeview Example")
    el={">":{"0":{"00":{},"01":{},"02":{"023":{},"024":{"0240":{},"0244":{},"0248":{}},"026":{}},"07":{},"09":{},"0*":{}}
             ,"1":{}}}
    el[">"]['2']={}    
    el[">"]['2']['24']={}    
    

    print(el)
    print(el[">"]["0"]["00"])
    el[">"]["0"].pop("00")
    print(el)
    
    
    ins=TreeData(root)
    ins.disp_data(el)
    #ins.populate_tree(tree_data)
    #ins.update_tree(tree_data,el)
    root.mainloop()
    return




#########################################
class TreeData:
    def __init__(self,root):
        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack()

        self.menu_open=False

        # Create a Treeview widget
        self.tree = ttk.Treeview(self.tree_frame, columns=("#1", "#2","#3","#4"), height=30)

        #s=ttk.Style()
        #s.configure('Treeview', rowheight=30)


        # Define columns
        self.tree.heading("#0", text="NUM")
        self.tree.heading("#1", text="First")
        self.tree.heading("#2", text="Second")
        self.tree.heading("#3", text="Theried")
        self.tree.heading("#4", text="FourTH")


        self.tree.column("#0", minwidth=40, width=150, stretch=tk.NO,anchor="w")
        self.tree.column("#1", minwidth=40, width=80, stretch=tk.NO,anchor=tk.CENTER)
        self.tree.column("#2", minwidth=80, width=80, stretch=tk.NO,anchor=tk.CENTER)
        self.tree.column("#3", minwidth=80, width=80, stretch=tk.NO,anchor=tk.CENTER)
        self.tree.column("#4", minwidth=80, width=80, stretch=tk.NO,anchor=tk.CENTER)

    
        # Pack the tree
        self.tree.pack()
        self.tree_frame.place(x=100, y=90)

        self.tree.bind('<ButtonRelease-3> ', self.selectItem)


        return
    ########################################

    def disp_data(self,data,parent=""):
        for key, value in data.items():
            category_node = self.tree.insert(parent, "end", text=key)
            self.disp_data(value, category_node)
     
        print(data)

########################################

    def selectItem(self,event):
        curItem = self.tree.item(self.tree.focus())
        item = self.tree.identify_row(event.y)
        if item:
            print("Right-clicked on item:", item)



        col = self.tree.identify_column(event.x)
        print("selection",self.tree.selection())
        row = self.tree.selection()[0]
        
        print ('curItem = ', curItem)
        
        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        elif col == '#4':
            cell_value = curItem['values'][3]
        
        print ('cell_value = ', cell_value)
        print('row =',row,col)
        #self.show_menu()
        
        
        
        # Change the value of a specific cell
        #self.tree.set ("I003", "#3", "Ramin")
        #self.tree.set("I002", 0, "EHSAN")
        #print(curItem)       
        return 
    ########################################
    def on_right_click(self,event):
        print("alyk")
        item = self.tree.identify_row(event.y)
        print("Clicked on item:", item)
        if item:
            if(not self.menu_open):
                print("open")
                self.menu.post(event.x_root, event.y_root)
                self.menu_open = True
            else:
                print("close")
                self.menu.unpost()
                self.menu_open = False

    def on_submenu_click(self):
        print("Submenu item clicked")



    def show_menu(self):
        print("hi")
        self.menu = tk.Menu(self.tree_frame, tearoff=0)
        self.menu.add_command(label="Do something", command=self.on_right_click)
        submenu = tk.Menu(self.menu, tearoff=0)
        submenu.add_command(label="Submenu item1", command=self.on_submenu_click)
        submenu.add_command(label="Submenu item2", command=self.on_submenu_click)
        submenu.add_command(label="Submenu item3", command=self.on_submenu_click)
        submenu.add_command(label="Submenu item4", command=self.on_submenu_click)
        submenu.add_command(label="Submenu item5", command=self.on_submenu_click)
        self.menu.add_cascade(label="Submenu", menu=submenu)
    
        self.tree.bind("<Button-3>",self.on_right_click)

        #self.tree.bind("<Button-3>", lambda event:self.menu.post(event.x_root, event.y_root))


if __name__=="__main__":
    main()

