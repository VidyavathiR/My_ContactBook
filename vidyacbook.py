#importing library tkinter
from tkinter import *
from tkinter import messagebox
rt=Tk()
rt.geometry('600x600')
rt.configure(bg='#17202A')
rt.title('Vidya Contact Book')
rt.resizable(0,0)
contactlist = [
                 ['Vidya',9090909990],
                 ['Shalu',9999991111],
                 ['Naveen',8888888888],
                 ['Akash',777777777],
                 ['Aravind',2343443355],
                 ['Anandhu',898989898],
                 ['Bhuvi',989898988],
                 ['Veera',7676767676],
                 ['Tulsi',676776767],
                 ['Chandru',6767676767]
               ]
Name=StringVar()
Number=StringVar()
#frame creation
frame = Frame(rt)
frame.pack(side = 'right')
scroll= Scrollbar(frame, orient=VERTICAL)
scroll.pack(side="right", fill='y')
listbox=Listbox(frame, yscrollcommand=scroll.set, bg='#FFFFFF',font=('Times new roman',16),width='15', height='30', borderwidth='3', relief='raised')
scroll.config(command=listbox.yview)
listbox.pack(side='left', fill="both", expand=1)
#function to get selected value
def selected():
    print("hello",len(listbox.curselection()))
    if len(listbox.curselection())==0:
          messagebox.showerror("error","Please, select the name")
    else:
        
          return int(listbox.curselection()[0])
#ADDFUNCTION
def add():
    if Name.get()!=" " and Number.get()!=" ":
        contactlist.append([Name.get(), Number.get()])
        print(contactlist)
        Select_set()
        
        messagebox.showinfo("confirmation","successfully added")
    else:
        messagebox.showerror("error","Please, fill the details")

#editfunction
def edit():
    if Name.get() and Number.get():
        contactlist[selected()]=[Name.get(),Number.get()]
        messagebox.showinfo("confirmation","Successfully updated")
        Select_set()
    elif not(Name.get()) and not(Number.get()) and not(len(listbox.curselection())==0):
        messagebox.showerror("error","Please fill the information")
             
    else:
        if len(listbox.curselection())==0:
             messagebox.showerror("error","Please, select the name and \n press view button")
        else:
             message1 = """To Load the information\n
                           First select the row and press Load button\n.
                           then fill both the name and contactno field.
                        """
             messagebox.showerror("Error", message1)

def delete():
    if len(listbox.curselection())!=0:
        result=messagebox.askyesno("confirmation","Are you sure??\n you want to delete this contact")
        if result==True:
         del contactlist[selected()]
        Select_set() 
    else:
        messagebox.showerror("error","Please, select the contact name to delete")

def view():
    NAME, NUMBER= contactlist[selected()]
    Name.set(NAME)
    Number.set(NUMBER)

def exit():
    rt.destroy()
    
def Select_set() :
    contactlist.sort()
    listbox.delete(0,END)
    for name,number in contactlist:
        listbox.insert(END, name)
Select_set()


def EntryReset():
    Name.set("")
    Number.set("")

#validation fun for name
def vid(input): 
      
    if input.isalpha(): 
        print(input) 
        return True
                          
    elif input == "": 
        print(input) 
        return True
  
    else: 
        print(input) 
        return False
    
Label(rt, text = 'Name',font=("Times new roman",20,"bold"), bg = '#BDC3C7',width=9).place(x= 30, y=20)
s=Entry(rt, textvariable = Name,width=25)
s.place(x= 200, y=30)

reg = rt.register(vid) 
  
s.config(validate ="key", validatecommand =(reg, '%P')) 


#validation fun for contactno
def callback(input): 
      
    if input.isdigit(): 
        print(input) 
        return True
                          
    elif input == "": 
        print(input) 
        return True
  
    else: 
        print(input) 
        return False
    
Label(rt, text = 'Contact No.', font=("Times new roman",20,"bold"),bg = '#BDC3C7',width=9).place(x= 30, y=70)
e=Entry(rt, textvariable = Number, width=25)
e.place(x= 200, y=80)


reg = rt.register(callback) 
e.config(validate ="key", validatecommand =(reg, '%P')) 


Button(rt,text=" ADD", font='Helvetica 18 bold',bg='#FDFEFE', command = add, padx=20, relief='sunken',width=7). place(x= 50, y=140)
Button(rt,text="UPDATE", font='Helvetica 18 bold',bg='#FDFEFE',command = edit, padx=20, relief='sunken',width=7).place(x= 50, y=200)
Button(rt,text="DELETE", font='Helvetica 18 bold',bg='#FDFEFE',command = delete, padx=20, relief='sunken',width=7).place(x= 50, y=260)
Button(rt,text="VIEW", font='Helvetica 18 bold',bg='#FDFEFE', command = view, relief='sunken',width=10).place(x= 50, y=325)
Button(rt,text="RESET", font='Helvetica 18 bold',bg='#FDFEFE', command = EntryReset, relief='sunken',width=10).place(x= 50, y=390)
Button(rt,text="CLOSE", font='Helvetica 24 bold',bg='#AEB6BF', command = exit, relief='groove',width=7).place(x= 240, y=500)



rt.mainloop()      
