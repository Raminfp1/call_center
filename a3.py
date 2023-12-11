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
    
    el=[
            [" >","salam","","",""],
            ["0","","","",""],
            ["00","","","",""],
            ["000","","","",""],
            ["0000","","","",""],
            ["00009","","","",""],
            ["0001","","","",""],
            ["00010","","","",""],
            ["00011","","","",""],
            ["001","","","",""],
            ["0010","","","",""],
            ["01","","","",""],
            ["010","","","",""],
            ["02","","","",""],
            ["020","","","",""],
            ["021","","","",""],
            ["1","","","",""],
            ["10","","","",""],
            ["11","","","",""],
            ["12","","","",""],
            ["2","","","",""],
            ["20","","","",""],
            ["21","","","",""],
            ["23","","","",""],
        ]    
    
    
    
    #ins_el(el)
    
    
    ins=TreeData(root)
    ins.disp_data(el)
    #ins.populate_tree(tree_data)
    #ins.update_tree(tree_data,el)
    root.mainloop()
    return

#########################################

#########################################

def str1_less(str1,str2):
    len_s1=len(str1)
    len_s2=len(str2)
    
    for i in range(min(len_s1,len_s2)):
        #print(i,str1[i],str2[i])
        if (str1[i]<str2[i]):
            return 1
        elif(str1[i]>str2[i]):
            return 0
    if(len_s1<len_s2): 
        return 1
    elif(len_s1>len_s2):
        return 0
    else:
        return 2 #find it

######################################
def add_el(new,el):

    print(el)    
   
    for i in range(len(el)):
        #print(i,new,el[i][1])
        les=str1_less(new,el[i][0])
        if(les):
            break
    
    if(i==len(el)-1 and les==0):
        i=i+1
    indx=i
    print(indx,les,len(el))
    
    if(les==2):
        print("Already Exist!")
        return 0

    print(el)    

    el.insert(indx,[new,'','','',''])
    print(el) 
    return 1
########################################   
def del_el(old,el):
    print(el)
    
    f=0
    for i in range(len(el)):
        if(el[i][0]==old):
            print(i,el[i])
            del el[i]
            f=1
            break
        
    print(el)
    return f
##########################################
    def ins_el(el,ns="000",keys=['1','2','3','5','*','#']):
    
        return
 
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
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.tree_frame.place(x=100, y=90)
        return
    
########################################
    def read_first_column(self):
        values = []
        for row in self.tree.get_children():
            self.tree.item(row,open=True)

            values.append(self.tree.item(row)['text'])

        print("******************",values)
        return
        
    
    def disp_data(self,el):
        print(el)
        par=self.tree.insert("", "end", text=" >",values=(el[0][1],el[0][2],el[0][3],el[0][4]))
        #print(par)
        #self.tree.insert("I001", "end", text="0")
        #self.tree.insert("I001", "end", text="1")
        #self.tree.insert("I003", "end", text="2")
        
        for e in el:
            if(len(e[0])==1): #level1
                self.tree.insert("I001", "end", text=e[0])
        
        for e in el:
            if(len(e[0])==2): #level1
                self.tree.insert("I002", "end", text=e[0])
        self.read_first_column()
        
        
        #for i in range(1,len(el)):
        #    par=self.tree.insert("", "end", text=" >",values=(el[0][1],el[0][2],el[0][3],el[0][4]))
            
        #    if(e[0]==' >'):
        #        par=""
        #    else:
        #        par=str(e[0][:-1])
        #    print(e,e[0],par)
        #    self.tree.insert(par, "end", text=e[0])

        return
########################################

    def populate_tree(self, data, parent=""):
        
        for key, value in data.items():
            if isinstance(value, dict):
                category_node = self.tree.insert(parent, "end", text=key)
                self.populate_tree(value, category_node)
            else:
                item_node = self.tree.insert(parent, "end", text=key)
                if isinstance(value, list):
                    for sub_item in value:
                        self.tree.insert(item_node, "end", text=sub_item)
        return
    




########################################
    def update_tree(self,data,el):
        self.populate_tree(data)    
        print(el)

        # Update the data in the treeview based on the dictionary
        print(self.tree.get_children())

        for item in self.tree.get_children():
            first_value = self.tree.item(item, "text")
            print("First value of row", item, ":", first_value)


        
        for  item in ["I001","I002","I00A","I010"]: #self.tree.get_children():
            key = self.tree.item(item, "text")
            print(key)
            if key in el:
                values = el[key]
                self.tree.item(item, values=(key,2,3,4))


        #self.tree.item("1",text="000", values=(key,2,3,4))

        return
    


########################################

    def selectItem(self,event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
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

        # Change the value of a specific cell
        self.tree.set ("I003", "#3", "Ramin")
        #self.tree.set ()

        self.tree.set("I002", 0, "EHSAN")
        print(curItem)       
        return 
    ########################################

'''

# Add child nodes
c1=tree.insert(p1, "end", text=">0", values=("Charlie", "20","erYwt","wertwe"))
c2=tree.insert(p1, "end", text=">1", values=("Diana", "28","wertwer","tewd"))
d1=tree.insert(c2, "end", text=">1.1", values=("Bob", "30","rweyt","wert"))
print("c1=",c1)
print("c2=",c2)
print("d1=",d1)

# Pack the tree
tree.pack()
tree.bind('<ButtonRelease-1>', selectItem)

#scrollbar = Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
#scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#tree.configure(yscrollcommand=scrollbar.set)



'''
########################################
if __name__=="__main__":
    main()

