#pip install tk, pip install Pillow, pip install webp
from tkinter import *
from PIL import ImageTk
from PIL import Image
window = Tk()
window.geometry('540x359+450+300')
window.title("Medical Inventory System")



def openHome():
    from PIL import ImageTk, Image
    home_window = Toplevel(window)
    home_window.geometry('540x500+450+300')
    home_window.title("Home-Medical Inventory System")

    LabelImage = (Image.open(r".\datas\Krishna.png"))
    imageHome=LabelImage.resize((round(LabelImage.size[0]*0.8), round(LabelImage.size[1]*0.8)))
    Image=ImageTk.PhotoImage(imageHome)

    Profile = Label(home_window, compound = TOP, image = Image, text = "Details").pack(side = TOP,expand=True)
    Name1 = Label(home_window, compound = LEFT, font = ('calibri', 14, 'bold'), text="Krishna Kant Tripathi").pack(side = TOP,expand=True)
    Name12 = Label(home_window, compound = LEFT, font = ('calibri', 14), text="Roll number 50").pack(side = TOP)
    Name13 = Label(home_window, compound = LEFT, font = ('calibri', 14), text="Reg number 11915229").pack(side = TOP)
    Name2 = Label(home_window, compound = LEFT, font = ('calibri', 14, 'bold'), text="Ramkrushna Naik").pack(side = TOP,expand=True)
    Name12 = Label(home_window, compound = LEFT, font = ('calibri', 14), text="Roll number 35").pack(side = TOP)
    Name13 = Label(home_window, compound = LEFT, font = ('calibri', 14), text="Reg number 11910722").pack(side = TOP)
    Name3 = Label(home_window, compound = LEFT, font = ('calibri', 14, 'bold'), text="Ashutosh Kumar").pack(side = TOP, expand = True)
    Name12 = Label(home_window, compound = LEFT, font = ('calibri', 14), text="Roll number 23").pack(side = TOP)
    Name13 = Label(home_window, compound = LEFT, font = ('calibri', 14), text="Reg number 12008573").pack(side = TOP)
    exitHome = Button(home_window, compound = TOP,text = "Press to go back",font = ('calibri', 13, 'italic'), command = (home_window.destroy)).pack(anchor = W,expand=True)

    home_window.mainloop()

def Inventory():
    import tkinter as tk    #import tkinter
    from tkinter import ttk
    from csv import DictWriter
    import os 
    inventory_window = Toplevel(window)
    inventory_window.geometry('540x359+450+300')
    inventory_window.title('Inventory-Medical Inventory System')

    inventoryIMG=(Image.open(r".\datas\inventoryIMG.png"))
    imageInventory=inventoryIMG.resize((round(inventoryIMG.size[0]*0.5), round(inventoryIMG.size[1]*0.5)))
    inventoryyimg=ImageTk.PhotoImage(imageInventory)
    Profile = Label(inventory_window, compound = TOP, image = inventoryyimg, text = "Inventory").grid(row = 0, column = 4, rowspan = 7, columnspan = 4)
    #create labels
    #name label
    name_label = ttk.Label(inventory_window,text = "Medicine Name: ")
    name_label.grid(row=0, column=2)

    #email label
    email_label = ttk.Label(inventory_window,text = "Helps in which disease: ")
    email_label.grid(row=1, column = 2,sticky =tk.W)

    #age label
    expiry = ttk.Label(inventory_window,text = "Expiry Date: ")
    expiry.grid(row=2, column = 2)

    #mobile number label
    medCode = ttk.Label(inventory_window, text = "Medicine unique code: ")
    medCode.grid(row=3, column = 2)

    #gender label
    type = ttk.Label(inventory_window,text = "Type of Medicine: ")
    type.grid(row=4, column = 2)

    itemnumber = ttk.Label(inventory_window, text ="Enter the Quantity of medicine:").grid(row = 6, column = 2)

    #Create entry box
    #name entry box
    name_var = tk.StringVar()
    name_entrybox = ttk.Entry(inventory_window, width = 16, textvariable = name_var)
    name_entrybox.grid(row=0 , column = 3)
    name_entrybox.focus()

    #email entry box
    disease_var = tk.StringVar()
    disease_entrybox = ttk.Entry(inventory_window, width = 16, textvariable = disease_var)
    disease_entrybox.grid(row = 1, column = 3)

    item_num = tk.StringVar()
    itemnum_entrybox = ttk.Entry(inventory_window, width = 16, textvariable = item_num).grid(row = 6, column =3)
    #age entry box
    expiry_var = tk.StringVar()
    expiry_entrybox = ttk.Entry(inventory_window,width = 16, textvariable= expiry_var)
    expiry_entrybox.grid(row=2, column =3)

    #mobile entry box
    medCode_var = tk.StringVar()
    medCode_entrybox = ttk.Entry(inventory_window, width= 16, textvariable = medCode_var)
    medCode_entrybox.grid(row=3, column= 3)

    #gender entry box
    #create combobox
    type_var = tk.StringVar()
    type_combobox = ttk.Combobox(inventory_window,width = 13, textvariable = type_var, state="readonly")
    type_combobox['values'] = ('Anticeptic', 'Syringe', 'Antidode')
    type_combobox.current(0)
    type_combobox.grid(row = 4, column=3)

    exitInventory = Button(inventory_window, compound = TOP,text = "Press to go back",font = ('calibri', 13, 'italic'), command = (inventory_window.destroy)).grid(row = 8, column = 0, columnspan = 3)

    #Create radio button
    cust_age = tk.StringVar()
    radiobtn1 = ttk.Radiobutton(inventory_window, text = 'For Children', value='For Children', variable = cust_age)
    radiobtn1.grid(row=5, column=2)

    radiobtn2 = ttk.Radiobutton(inventory_window, text = 'For adults', value='For adults', variable = cust_age)
    radiobtn2.grid(row=5, column=3)



    #Create button code action function
    def action():
        medname = name_var.get()
        medexpiry = expiry_var.get()
        meddisease = disease_var.get()
        medID = medCode_var.get()
        medictype = type_var.get()
        custAge = cust_age.get()
        itemnum = item_num.get()

        #write to csv file code here
        with open('datas\inventory.csv', 'a', newline = '') as f:
            dict_writer = DictWriter(f, fieldnames=['Name', 'Expiry', 'Disease','Medicine ID', 'Type', 'age group', 'quantity'])
            if os.stat('datas\inventory.csv').st_size == 0:        #if file is not empty than header write else not
                dict_writer.writeheader()
        
            dict_writer.writerow({
                'Name' : medname,
                'Expiry' : medexpiry,
                'Disease' : meddisease,
                'Medicine ID' : medID,
                'Type' : medictype,
                'age group' : custAge,
                'quantity' : itemnum
            })
        #Change color after submit button
        name_entrybox.delete(0, tk.END)
        expiry_entrybox.delete(0, tk.END)
        disease_entrybox.delete(0, tk.END)
        medCode_entrybox.delete(0, tk.END)
        name_label.configure(foreground = 'Blue')
        email_label.configure(foreground = 'Blue')
        expiry.configure(foreground = 'Blue')
        medCode.configure(foreground = 'Blue')
        type.configure(foreground = 'Blue')

    #submit button
    submit_button = ttk.Button(inventory_window, text = "Submit", command = action)  
    submit_button.grid(row=7, column=2, columnspan = 2)
    inventory_window.mainloop()  

def MedsW():
    import tkinter
    import csv
    meds_window = Toplevel(window)
    meds_window.geometry('540x359+450+300')
    meds_window.title("Home-Medical Inventory System")

    # open file
    with open("datas\inventory.csv", newline = "") as file:
        reader = csv.reader(file)

    # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                label = tkinter.Label(meds_window, width = 10, height = 2, text = row, relief = tkinter.RIDGE)
                label.grid(row = r, column = c)
                c += 1
            r += 1
    exitmeds = Button(meds_window, compound = TOP,text = "Press to go back",font = ('calibri', 13, 'italic'), command = (meds_window.destroy)).grid(row = r+2, column = 0, columnspan = c)
    meds_window.mainloop()

def searchmed():
    import tkinter
    import csv
    from tkinter import ttk, messagebox

    searchmed_window = Toplevel(window)
    searchmed_window.geometry('580x359+450+300')
    searchmed_window.title("Search-Medical Inventory System")

    data = []
    result = []
    with open("datas\inventory.csv", newline = "") as file:
        reader = csv.reader(file)

        r = 1
        for row in reader:
            c = 0
            for col in row:
                label = tkinter.Label(searchmed_window, width = 10, height = 2, text = col, relief = tkinter.RIDGE)
                label.grid(row = r, column = c)
                c += 1
            break
        for row in reader:
            data.append(row)

    lbl = ttk.Label(searchmed_window, text = "Enter the Name of medicine: ").grid(row =0, column = 0, columnspan = 2)
    exitSearch = Button(searchmed_window, compound = TOP,text = "Press to go back",font = ('calibri', 13, 'italic'), command = (searchmed_window.destroy)).grid(row = 0, column =5)
    name_var = tkinter.StringVar()
    name_entrybox = ttk.Entry(searchmed_window, width = 16, textvariable = name_var)
    name_entrybox.grid(row=0 , column = 2)

    def action():
        try:
            name = name_var.get()
            c=0
            col = [x[0] for x in data]
            if name in col:
                for x in range(0,len(data)):
                    if name == data[x][0]:
                        result.append(data[x])

            for res in result[0]:
                label = tkinter.Label(searchmed_window, width = 10, height = 2, text =res)
                label.grid(row = r+1, column = c)
                c += 1
        except:
            #label = tkinter.Label(searchmed_window, text = "No entry found kindly check spelling\n or add the entry first").grid(row = r+1, column = 0, columnspan = 6)
            messagebox.showwarning("warning","No entry found kindly check spelling\n or add the entry first")
    search_btn = ttk.Button(searchmed_window, text = "Search", command = action).grid(row = 0, column = 3)
    searchmed_window.mainloop()
    

home=(Image.open(r".\datas\home.png"))
image1=home.resize((round(home.size[0]*0.1), round(home.size[1]*0.1)))
homeimg=ImageTk.PhotoImage(image1)



sales=(Image.open(r".\datas\search.jpg"))
image2=sales.resize((round(sales.size[0]*0.1), round(sales.size[1]*0.1)))
saleimg=ImageTk.PhotoImage(image2)



meds=(Image.open(r".\datas\meds.png"))
image3=meds.resize((round(meds.size[0]*0.25), round(meds.size[1]*0.25)))
medsimg=ImageTk.PhotoImage(image3)



inventory=(Image.open(r".\datas\inventory.png"))
image5=inventory.resize((round(inventory.size[0]*0.06), round(inventory.size[1]*0.06)))
inventoryimg=ImageTk.PhotoImage(image5)


welcomeImage = (Image.open(r".\datas\welcome.jpg"))
imageWelcome=welcomeImage.resize((round(welcomeImage.size[0]*0.6), round(welcomeImage.size[1]*0.6)))
Imagewel=ImageTk.PhotoImage(imageWelcome)



a=Button(window, compound = TOP,image = homeimg ,text="Home",relief =FLAT, cursor = "hand2", padx=20, command = openHome).grid(row = 0, column = 0)
b=Button(window, compound = TOP,image = saleimg,text="Search",relief =FLAT, cursor = "hand2",padx=20, command = searchmed).grid(row = 0, column = 1)
c=Button(window, compound = TOP,image = inventoryimg,text="Inventory",relief =FLAT, cursor = "hand2",padx=20, command = Inventory).grid(row = 0, column = 2)
d=Button(window, compound = TOP,image = medsimg,text="Admin of Meds",relief =FLAT, cursor = "hand2",padx=20, command = MedsW).grid(row = 0, column = 3)
welcome = Label(window, compound = TOP, image = Imagewel, text = "Welcome To Medical Inventory System").grid(row = 1, column = 0, columnspan = 4, rowspan = 4)
exitHome = Button(window, compound = TOP ,text = "Press to say Good Bye",font = ('calibri', 13, 'italic'), command = (window.destroy)).grid(row = 5,column = 0, columnspan = 4)



window.mainloop()
