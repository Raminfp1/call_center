import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import scrolledtext
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
    #ins_el(el)
    delete_item_from_nested_dict("024", el)
    print(el)
    
    
    ins=TreeData(root)
    ins.disp_data(el)
    #ins.populate_tree(tree_data)
    #ins.update_tree(tree_data,el)
    root.mainloop()
    return


def delete_item_from_nested_dict(item, nested_dict):
    print("------------------------------------------------------------------------------------")
    keys = item.split(".")  # Split the item into keys
    print("keys=",keys)
    current_dict = nested_dict
    for key in keys[:-1]:  # Traverse the dictionary to reach the parent of the item
        print("current_dict =",current_dict,"--",current_dict.get(key, {}))
        current_dict = current_dict.get(key, {})

    print(current_dict,keys,keys[-1])    
    current_dict.pop(keys[-1], None)  # Remove the item from the dictionary
    print("------------------------------------------------------------------------------------")





#########################################
class TreeData:
    def __init__(self,root):
        self.tree_frame = Frame(root)
        self.tree_frame.pack()


        # Create a Treeview widget
        self.tree = ttk.Treeview(self.tree_frame, columns=("#1", "#2","#3","#4"), height=30)

        s=ttk.Style()
        #s.theme_use('clam')

        # Add the rowheight
        s.configure('Treeview', rowheight=30)


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


        # Add data to the tree
        #p1=self.tree.insert("", "end", text=" >", values=("", "","",""))
         

        #print("p1=",p1)

        # Pack the tree
        self.tree.pack()
        #self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.tree_frame.place(x=100, y=90)
        return
    ########################################

    def disp_data(self,data,parent=""):
        for key, value in data.items():
            category_node = self.tree.insert(parent, "end", text=key)
            self.disp_data(value, category_node)
     
        
        
        print(data)




if __name__=="__main__":
    main()

