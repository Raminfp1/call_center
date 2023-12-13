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
        self.tree_frame.place(x=50, y=50)

        self.menu = tk.Menu(self.tree_frame, tearoff=0)
        
        submenu = tk.Menu(self.menu, tearoff=0)
        submenu.add_command(label="0", command=self.on_submenu_click)
        submenu.add_command(label="1", command=self.on_submenu_click)
        submenu.add_command(label="2", command=self.on_submenu_click)
        submenu.add_command(label="3", command=self.on_submenu_click)
        submenu.add_command(label="4", command=self.on_submenu_click)
        submenu.add_command(label="5", command=self.on_submenu_click)
        submenu.add_command(label="6", command=self.on_submenu_click)
        submenu.add_command(label="7", command=self.on_submenu_click)
        submenu.add_command(label="8", command=self.on_submenu_click)
        submenu.add_command(label="9", command=self.on_submenu_click)
        submenu.add_command(label="*", command=self.on_submenu_click)
        submenu.add_command(label="#", command=self.on_submenu_click)
        self.menu.add_cascade(label="Add", menu=submenu)
        
        submenu2 = tk.Menu(self.menu, tearoff=0)
        submenu2.add_command(label="No", command=self.on_submenu_click)
        submenu2.add_command(label="Yes", command=self.del_dg)
        self.menu.add_cascade(label="Delete", menu=submenu2)
        
        
        
        
        self.tree.bind("<Button-3>", self.on_right_click)
        self.tree_frame.bind("<Button-1>", self.close_menu)

        return
    ########################################

    def disp_data(self,data,parent=""):
        for key, value in data.items():
            category_node = self.tree.insert(parent, "end", text=key)
            self.disp_data(value, category_node)
     
        print(data)

########################################

    def on_right_click(self,event):
        
        item = self.tree.selection()

        print("item=",item, "event.y=",self.tree.identify_column(event.y) , " " ,self.tree.identify_column(event.y)  )


        if item:
            print("Right-clicked on item:", item)
            col = self.tree.identify_column(event.x)
            row = self.tree.selection()[0]
            val=self.tree.item(row)['text']
            print('row =',row,col,val)
        
            self.menu.post(event.x_root, event.y_root)
              
        
        return    
    ########################################

    
    def close_menu(self,event):
        print("close")
        self.menu.unpost()
    ########################################

    def del_dg(self):
        pass
    ########################################

    def on_submenu_click(self):
        print("Submenu item clicked")


    ########################################

if __name__=="__main__":
    main()

