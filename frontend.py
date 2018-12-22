from tkinter import *
import backend

def get_selected_row(event):
	try:
		global selected_tuple
		selected_tuple=None
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
		e5.delete(0,END)
		e5.insert(END,selected_tuple[5])
		e6.delete(0,END)
		e6.insert(END,selected_tuple[6])
	except IndexError:
		pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(),material_text.get(),type_text.get(),weight_text.get(),price_text.get(),purity_text.get()):
        list1.insert(END,row)

def gold_command():
    list1.delete(0,END)
    for row in backend.g_search():
        list1.insert(END,row)

def diamond_command():
    list1.delete(0,END)
    for row in backend.d_search():
        list1.insert(END,row)

def silver_command():
    list1.delete(0,END)
    for row in backend.s_search():
        list1.insert(END,row)

def necklaces_command():
    list1.delete(0,END)
    for row in backend.n_search():
        list1.insert(END,row)

def earrings_command():
    list1.delete(0,END)
    for row in backend.e_search():
        list1.insert(END,row)

def rings_command():
    list1.delete(0,END)
    for row in backend.r_search():
        list1.insert(END,row)

def bracelets_command():
    list1.delete(0,END)
    for row in backend.b_search():
        list1.insert(END,row)

def add_command():
    backend.insert(name_text.get(),material_text.get(),type_text.get(),weight_text.get(),price_text.get(),purity_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),material_text.get(),type_text.get(),weight_text.get(),price_text.get(),purity_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],name_text.get(),material_text.get(),type_text.get(),weight_text.get(),price_text.get(),purity_text.get())

def asc_sort_command():
    list1.delete(0,END)
    for row in backend.view_asc():
        list1.insert(END,row)

def desc_sort_command():
    list1.delete(0,END)
    for row in backend.view_desc():
        list1.insert(END,row)


window=Tk()

window.wm_title("Welcome User !!!")

l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Material")
l2.grid(row=0,column=2)

l3=Label(window,text="Type")
l3.grid(row=1,column=0)

l4=Label(window,text="Weight(in gms)")
l4.grid(row=1,column=2)

l5=Label(window,text="Price")
l5.grid(row=2,column=0)

l6=Label(window,text="Purity (in carats)")
l6.grid(row=2,column=2)

name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)

material_text=StringVar()
e2=Entry(window,textvariable=material_text)
e2.grid(row=0,column=3)

type_text=StringVar()
e3=Entry(window,textvariable=type_text)
e3.grid(row=1,column=1)

weight_text=StringVar()
e4=Entry(window,textvariable=weight_text)
e4.grid(row=1,column=3)

price_text=StringVar()
e5=Entry(window,textvariable=price_text)
e5.grid(row=2,column=1)

purity_text=StringVar()
e6=Entry(window,textvariable=purity_text)
e6.grid(row=2,column=3)

list1=Listbox(window,height=6,width=42)
list1.grid(row=3,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=8,column=3)

b7=Button(window,text="Sort(asc.)",width=12,command=asc_sort_command)
b7.grid(row=0,column=4)

b8=Button(window,text="Sort(desc.)",width=12,command=desc_sort_command)
b8.grid(row=1,column=4)

b9=Button(window,text="Gold",width=12,command=gold_command)
b9.grid(row=2,column=4)

b10=Button(window,text="Diamond",width=12,command=diamond_command)
b10.grid(row=3,column=4)

b11=Button(window,text="Silver",width=12,command=silver_command)
b11.grid(row=4,column=4)

b12=Button(window,text="Rings",width=12,command=rings_command)
b12.grid(row=5,column=4)

b13=Button(window,text="Necklaces",width=12,command=necklaces_command)
b13.grid(row=6,column=4)

b14=Button(window,text="Bracelets",width=12,command=bracelets_command)
b14.grid(row=7,column=4)

b15=Button(window,text="Earrings",width=12,command=earrings_command)
b15.grid(row=8,column=4)

window.mainloop()
