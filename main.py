from tkinter import*
import math,random,os
from tkinter import messagebox

root= Tk()
root.geometry("1600x1600+0+0")
root.title("Emad Billing Software")
bgcolor = "#074463"


###########################function #############################
# Function For Total
def total():
    # Cosmetics
    c_so_p = soap.get()*30
    c_fc_p = face_cream.get() * 120
    c_fw_p = face_wash.get() * 70
    c_s_p = spray.get() * 180
    c_g_p = gell.get() * 140
    c_l_p = loshan.get() * 180

    # Grocery
    g_r_p = rice.get()*30
    g_g_p = ginger.get() * 120
    g_w_p = wheat.get() * 40
    g_oi_p = oil.get() * 90
    g_o_p = onions.get() * 70
    g_gar_p = garlic.get() * 120

    # Cold Dribks

    co_sp_p = sprite.get() * 30
    co_se_p = seven_up.get() * 33
    co_m_p = miranda.get() * 40
    co_co_p = cocacola.get() * 70
    co_fr_p = Frooto.get() * 50
    co_p_p = Pepsi.get() * 60

    total_cosmetic_price = float(
                            c_so_p+
                            c_fc_p +
                            c_fw_p +
                            c_s_p +
                            c_g_p +
                            c_l_p
                            )
    total_grocery_price = float(
                            g_r_p+
                            g_g_p+
                            g_w_p+
                            g_oi_p+
                            g_o_p+
                            g_gar_p
                            )

    total_cold_drink_price = float(
                                co_sp_p+
                                co_se_p+
                                co_m_p+
                                co_co_p+
                                co_fr_p+
                                co_p_p
    )


    cosmetic_price.set(str(f"{total_cosmetic_price} Taka"))
    cosmetic_tax.set(f"{round((total_cosmetic_price*0.05),2)} Taka")
    grocery_price.set(str(f"{total_grocery_price} Taka"))
    grocery_tax.set(f"{round((total_grocery_price*0.05),2)} Taka")
    cold_drink_price.set(str(f"{total_cold_drink_price} Taka"))
    cold_drink_tax.set(f"{round((total_cold_drink_price*0.05),2)} Taka")




# End Total Function



# Start Bill Generate

def welcome_bill():
    root.textarea.delete('1.0', END)
    root.textarea.insert(END, "\tWelcome Webcode Retail\n")
    root.textarea.insert(END, f"\nBill Number: {bill_no.get()}")
    root.textarea.insert(END, f"\nCustomer Name: {c_name.get()}")
    root.textarea.insert(END, f"\nPhone Number: {c_phone.get()}")

    root.textarea.insert(END, "\n======================================")
    root.textarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
    root.textarea.insert(END, "\n======================================")
def bill_area():
    cold_drink = float(sprite.get() * 30 +
                       seven_up.get() * 33 +
                       miranda.get() * 40 +
                       cocacola.get() * 70 +
                       Frooto.get() * 50 +
                       Pepsi.get() * 60)

    cosmetics = float(
        soap.get() * 30 +
        face_cream.get() * 120 +
        face_wash.get() * 70 +
        spray.get() * 180 +
        gell.get() * 140 +
        loshan.get() * 180
    )
    grocery = float(
        rice.get() * 30 +
        ginger.get() * 120 +
        wheat.get() * 40 +
        oil.get() * 90 +
        onions.get() * 70 +
        garlic.get() * 120
    )
    g_tax = round((grocery * 0.05), 2)
    cold_tax = round((cold_drink * 0.05), 2)
    cos_tax = round((cosmetics * 0.05), 2)

    if c_name.get() == "" or c_phone =="":
        messagebox.showerror("Error", "Customer Details Are Must")

    elif(cosmetic_price == "0.0 Taka" and grocery_price == "0.0 Taka" and cold_drink == "0.0 Taka"):
        messagebox.showerror("Error", "No Product Selected")


    else:
        welcome_bill()

        # Cosmetics ##
        if(soap.get() != 0):
            root.textarea.insert(END, f"\n Bath Soap\t\t{soap.get()}\t\t{soap.get()*30}")



        if (face_cream.get() != 0):
            root.textarea.insert(END, f"\n Face Cream\t\t{face_cream.get()}\t\t{face_cream.get() * 33}")
        if (face_wash.get() != 0):
            root.textarea.insert(END, f"\n Face Wash\t\t{face_wash.get()}\t\t{face_wash.get() * 40}")
        if (spray.get() != 0):
            root.textarea.insert(END, f"\n Hair Spray\t\t{spray.get()}\t\t{spray.get() * 50}")
        if (gell.get() != 0):
            root.textarea.insert(END, f"\n Hair Gell\t\t{gell.get()}\t\t{gell.get() * 70}")
        if (loshan.get() != 0):
            root.textarea.insert(END, f"\n Loshan\t\t{loshan.get()}\t\t{loshan.get() * 60}")

    # Grocery

        if(rice.get() != 0):
            root.textarea.insert(END, f"\n Rice\t\t{rice.get()}\t\t{rice.get()*30}")

        if (ginger.get() != 0):
            root.textarea.insert(END, f"\n Ginger\t\t{ginger.get()}\t\t{ginger.get() * 120}")
        if (wheat.get() != 0):
            root.textarea.insert(END, f"\n Wheat\t\t{wheat.get()}\t\t{wheat.get() * 40}")
        if (oil.get() != 0):
            root.textarea.insert(END, f"\n Oil\t\t{oil.get()}\t\t{oil.get() * 90}")
        if (onions.get() != 0):
            root.textarea.insert(END, f"\n Onions\t\t{onions.get()}\t\t{onions.get() * 70}")
        if (garlic.get() != 0):
            root.textarea.insert(END, f"\n Garlic\t\t{garlic.get()}\t\t{garlic.get() * 120}")

    # Cold Drinks
        if(sprite.get() != 0):
            root.textarea.insert(END, f"\n Sprite\t\t{sprite.get()}\t\t{sprite.get()*30}")

        if (seven_up.get() != 0):
            root.textarea.insert(END, f"\n Seven Up\t\t{seven_up.get()}\t\t{seven_up.get() * 120}")
        if (miranda.get() != 0):
            root.textarea.insert(END, f"\n Miranda\t\t{miranda.get()}\t\t{miranda.get() * 40}")
        if (cocacola.get() != 0):
            root.textarea.insert(END, f"\n Cocacola\t\t{cocacola.get()}\t\t{cocacola.get() * 90}")
        if (Frooto.get() != 0):
            root.textarea.insert(END, f"\n Frooto\t\t{Frooto.get()}\t\t{Frooto.get() * 70}")
        if (Pepsi.get() != 0):
            root.textarea.insert(END, f"\n Pepsi\t\t{Pepsi.get()}\t\t{Pepsi.get() * 120}")



        total_value = float(cold_drink + cosmetics + grocery + g_tax + cold_tax + cos_tax)

        mainjio = str(total_value)

        print(total)



        root.textarea.insert(END, "\n--------------------------------------")
        if cosmetic_tax.get() != "0.0 Taka":
            root.textarea.insert(END, f"\n Cosmetic Tax\t\t\t     {cosmetic_tax.get()}")
        if grocery_tax.get() != "0.0 Taka":
            root.textarea.insert(END, f"\n Grocery Tax\t\t\t     {grocery_tax.get()}")
        if cold_drink_tax.get() != "0.0 Taka":
            root.textarea.insert(END, f"\n Cold Drink Tax\t\t\t     {cold_drink_tax.get()}")
        root.textarea.insert(END, f"\n\n Total Bill\t\t\t   {mainjio} Taka")

        root.textarea.insert(END, "\n--------------------------------------")
        save_bill()


#########################end Function  ###############


def save_bill():
    op = messagebox.askyesno("Save Bill", "Do You Want To Save The Bill")

    if op>0:
        bill_data = root.textarea.get('1.0', END)
        f1 = open("bills/" + str(bill_no.get())+".txt","w")
        f1.write(bill_data)
        f1.close()
        messagebox.showinfo("Saved"  , f"Bill no. {bill_no.get()} saved successfully")
    else:
        return


def find_bill():
    present = "no"
    for i in os.listdir("bills/"):
        if(i.split('.'))[0] == search_bill.get():
            f1 = open(f"bills/{i}","r")
            root.textarea.delete('1.0', END)
            for d in f1:
                root.textarea.insert(END, d)
            f1.close()
            present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill no.")


def clear_data():
    op = messagebox.askyesno("Exit", "Do You Really Want To Clear Data")
    if op > 0:
        soap.set(0)
        face_cream.set(0)
        face_wash.set(0)
        spray.set(0)
        gell.set(0)
        loshan.set(0)

        # Grocery
        rice.set(0)
        ginger.set(0)
        wheat.set(0)
        oil.set(0)
        onions.set(0)
        garlic.set(0)

        # Cold Drinks
        sprite.set(0)
        seven_up.set(0)
        miranda.set(0)
        cocacola.set(0)
        Frooto.set(0)
        Pepsi.set(0)

        # Total Product Price And Tax

        cosmetic_price.set("")
        grocery_price.set("")
        cold_drink_price.set("")

        cosmetic_tax.set("")
        grocery_tax.set("")
        cold_drink_tax.set("")

        # Customer

        c_name.set("")
        c_phone.set("")

        bill_no.set("")
        x = random.randint(1000, 9999)
        bill_no.set(str(x))
        search_bill.set("")
        welcome_bill()

def exit_app():
    op = messagebox.askyesno("Exit", "Do You Want To Exit")
    if op>0:
        root.destroy()



title = Label(root,bd=12,fg = "white",relief = GROOVE, bg=bgcolor, text="Emad Billing Software", font = ("times new roman", "30", "bold"), pady=2).pack(fill=X)

############################################
###################### All Variable############
# Cosmatics
soap = IntVar()
face_cream = IntVar()
face_wash = IntVar()
spray = IntVar()
gell = IntVar()
loshan = IntVar()

# Grocery
rice = IntVar()
ginger = IntVar()
wheat = IntVar()
oil = IntVar()
onions = IntVar()
garlic = IntVar()

# Cold Drinks
sprite = IntVar()
seven_up =IntVar()
miranda = IntVar()
cocacola = IntVar()
Frooto = IntVar()
Pepsi = IntVar()

# Total Product Price And Tax

cosmetic_price = StringVar()
grocery_price = StringVar()
cold_drink_price = StringVar()

cosmetic_tax = StringVar()
grocery_tax = StringVar()
cold_drink_tax = StringVar()

# Customer

c_name = StringVar()
c_phone = StringVar()
x= random.randint(1000, 9999)
bill_no = StringVar()
bill_no.set(str(x))
search_bill = StringVar()

###################### End Variable ###################




#Customer Details Frame
F1 = LabelFrame(root,bd=10,bg=bgcolor,fg="gold", relief= GROOVE, text="Customer Details", font = ("times new roman", "15", "bold",), pady=2)
F1.place(x=0, y=80, relwidth=1)


cname_label = Label(F1,bg=bgcolor,fg="white", text = "Customer Name", font = ("times new roman", "15", "bold",) ).grid(row=0, column=0, padx=20, pady=5)
cname_text = Entry(F1,bd=7, relief=SUNKEN, width=15,font = "arial 15", textvariable = c_name).grid(row=0, column=1, pady=5, padx=10)


cphn_label = Label(F1,bg=bgcolor,fg="white", text = "Phone No.", font = ("times new roman", "15", "bold",) ).grid(row=0, column=2, padx=20, pady=5)
cphn_text = Entry(F1,bd=7, relief=SUNKEN, width=15,font = "arial 15", textvariable = c_phone).grid(row=0, column=3, pady=5, padx=10)



cbill_label = Label(F1,bg=bgcolor,fg="white", text = "Bill Number", font = ("times new roman", "15", "bold",) ).grid(row=0, column=4, padx=20, pady=5)
cbill_text = Entry(F1,bd=7, relief=SUNKEN, width=15,font = "arial 15", textvariable = search_bill).grid(row=0, column=5, pady=5, padx=10)


bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold", command = find_bill).grid(row=0, column=6, pady=10, padx=10)
# End Customer Details


############################################
# Cosmetics Frame
F2 = LabelFrame(root,bd=10,bg=bgcolor,fg="gold", relief= GROOVE, text="Cosmetics", font = ("times new roman", "15", "bold",), pady=2)
F2.place(x=5, y=180, width=325, height=380)

bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky=W)
bath_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = soap).grid(row=0, column=1, padx=10, pady=10)

facecream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
facecream_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = face_cream).grid(row=1, column=1, padx=10, pady=10)

face_wash__lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=W)
face_wash_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = face_wash).grid(row=2, column=1, padx=10, pady=10)

hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
hair_s_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = spray).grid(row=3, column=1, padx=10, pady=10)

hair_g_lbl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
hair_g_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = gell).grid(row=4, column=1, padx=10, pady=10)

body_l_lbl = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
body_l_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = loshan).grid(row=5, column=1, padx=10, pady=10)
# End Cosmetics



# Grocerry Frame
F3 = LabelFrame(root,bd=10,bg=bgcolor,fg="gold", relief= GROOVE, text="Grocerry", font = ("times new roman", "15", "bold",), pady=2)
F3.place(x=340, y=180, width=325, height=380)

g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky=W)
g1_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = rice).grid(row=0, column=1, padx=10, pady=10)

g2_lbl = Label(F3, text="Ginger", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
g2_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = ginger).grid(row=1, column=1, padx=10, pady=10)

g3_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=W)
g3_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = wheat).grid(row=2, column=1, padx=10, pady=10)

g4_lbl = Label(F3, text="Oil", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
g4_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = oil).grid(row=3, column=1, padx=10, pady=10)

g5_lbl = Label(F3, text="Onions", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
g5_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = onions).grid(row=4, column=1, padx=10, pady=10)

g6_lbl = Label(F3, text="Garlic", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
g6_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = garlic).grid(row=5, column=1, padx=10, pady=10)


# Cold Drink Frame

F4 = LabelFrame(root,bd=10,bg=bgcolor,fg="gold", relief= GROOVE, text="Cold Drinks", font = ("times new roman", "15", "bold",), pady=2)
F4.place(x=670, y=180, width=325, height=380)

c1_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky=W)
c1_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = sprite).grid(row=0, column=1, padx=10, pady=10)

c2_lbl = Label(F4, text="7 Up", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
c2_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = seven_up).grid(row=1, column=1, padx=10, pady=10)

c3_lbl = Label(F4, text="Miranda", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky=W)
c3_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = miranda).grid(row=2, column=1, padx=10, pady=10)

c4_lbl = Label(F4, text="Coca cola", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
c4_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = cocacola).grid(row=3, column=1, padx=10, pady=10)

c5_lbl = Label(F4, text="Frooto", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
c5_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = Frooto).grid(row=4, column=1, padx=10, pady=10)

c6_lbl = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bgcolor, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
c6_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN, textvariable = Pepsi).grid(row=5, column=1, padx=10, pady=10)




###################################
# Bill Area

F5 = Frame(root,bd=10, relief = GROOVE)
F5.place(x=1010, y=180, width=350, height=380)

bill_title = Label(F5, text= "Bill Area", font = "arial 15 bold", bd=7, relief = GROOVE).pack(fill=X)


########################
# Text Editor
scrool_y = Scrollbar(F5, orient = VERTICAL)
root.textarea = Text(F5, yscrollcommand = scrool_y.set)
scrool_y.pack(side = RIGHT, fill=Y)
scrool_y.configure(command = root.textarea.yview)
root.textarea.pack(fill=BOTH, expand =1)
################################


# Button Frame

F6 = LabelFrame(root,bd=10,bg=bgcolor,fg="gold", relief= GROOVE, text="Bill Menu", font = ("times new roman", "15", "bold",), pady=2)
F6.place(x=0, y=560, relwidth=1, height=140)

m1_lbl = Label(F6,bg=bgcolor, fg="white", text="Total Costmatic Price", font=("times new roman", 14, "bold")).grid(row=0,column=0, padx=20, pady=1, sticky=W)
m1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN, textvariable = cosmetic_price).grid(row=0, column=1,padx=10, pady=1)


m2_lbl = Label(F6,bg=bgcolor, fg="white", text="Total Grocery Price", font=("times new roman", 14, "bold")).grid(row=1,column=0, padx=20, pady=1, sticky=W)
m2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN, textvariable = grocery_price).grid(row=1, column=1,padx=10, pady=1)



m3_lbl = Label(F6,bg=bgcolor, fg="white", text="Total Cold Drink Price", font=("times new roman", 14, "bold")).grid(row=2,column=0, padx=20, pady=1, sticky=W)
m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN, textvariable = cold_drink_price).grid(row=2, column=1,padx=10, pady=1)


ct_lbl = Label(F6,bg=bgcolor, fg="white", text="Costmatic Tax", font=("times new roman", 14, "bold")).grid(row=0,column=2, padx=20, pady=1, sticky=W)
ct_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN, textvariable = cosmetic_tax).grid(row=0, column=3,padx=10, pady=1)


gt_lbl = Label(F6,bg=bgcolor, fg="white", text="Grocery Tax", font=("times new roman", 14, "bold")).grid(row=1,column=2, padx=20, pady=1, sticky=W)
gt_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN, textvariable = grocery_tax).grid(row=1, column=3,padx=10, pady=1)

cot_lbl = Label(F6,bg=bgcolor, fg="white", text="Cold Drink Tax", font=("times new roman", 14, "bold")).grid(row=2,column=2, padx=20, pady=1, sticky=W)
cot_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN, textvariable = cold_drink_tax).grid(row=2, column=3,padx=10, pady=1)


btn_F = LabelFrame(F6,bd=7, relief =GROOVE)
btn_F.place(x=750, width=590, height=105)

total = Button(btn_F,command = total, text="Total",bd=5, bg="cadetblue", fg="white", pady=15, width=11, font="arial 12 bold").grid(row=0, column=0, padx=5, pady=5)

gen_btn = Button(btn_F,command=bill_area, text="Generate Bill",bd=5, bg="cadetblue", fg="white", pady=15, width=11, font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)

clear_btn = Button(btn_F, text="Clear",bd=5, bg="cadetblue", fg="white", pady=15, width=11, font="arial 12 bold", command = clear_data).grid(row=0, column=2, padx=5, pady=5)

exit = Button(btn_F, text="Exit",bd=5, bg="cadetblue", fg="white", pady=15, width=11, font="arial 12 bold", command = exit_app).grid(row=0, column=3, padx=5, pady=5)





root.mainloop()