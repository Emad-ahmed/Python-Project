from tkinter import*
from tkinter import ttk
import pymysql
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title("Student Management System")
root.geometry("1600x1600+0+0")

roll_no_var = StringVar()
name_var = StringVar()
email_var = StringVar()
gender_var =StringVar()
contact_var = StringVar()
dob_var = StringVar()

search_by = StringVar()
search_txt = StringVar()


def add_student():
    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmanage")
    cur = conn.cursor()




    cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",
                (
                    roll_no_var.get(),
                    name_var.get(),
                    email_var.get(),
                    gender_var.get(),
                    contact_var.get(),
                    dob_var.get(),
                    txt_address.get('1.0', END)
                ))
    clearall()
    conn.commit()
    messagebox.showinfo("Successfull", "Insert Successfully")
    fetchdata()
    conn.close()


def fetchdata():
    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmanage")
    cur = conn.cursor()
    cur.execute("select * from students")
    rows =cur.fetchall()

    if len(rows) !=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', END, values=row)

        conn.commit()

    conn.close()

def clearall():


    roll_no_var.set(""),
    name_var.set(""),
    email_var.set(""),
    gender_var.set(""),
    contact_var.set(""),
    dob_var.set(""),
    txt_address.delete('1.0', END)




def get_cursor(ev):
    cursor_row = student_table.focus()
    contents = student_table.item(cursor_row)
    row = contents['values']

    roll_no_var.set(row[0]),
    name_var.set(row[1]),
    email_var.set(row[2]),
    gender_var.set(row[3]),
    contact_var.set(row[4]),
    dob_var.set(row[5]),
    txt_address.delete('1.0', END)
    txt_address.insert(END, row[6])




def update_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmanage")
    cur = conn.cursor()

    cur.execute("update students set name=%s, email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                (

                    name_var.get(),
                    email_var.get(),
                    gender_var.get(),
                    contact_var.get(),
                    dob_var.get(),
                    txt_address.get('1.0', END),
                    roll_no_var.get()
                ))

    conn.commit()


    fetchdata()
    clearall()
    conn.close()


def delete_data():
    m = messagebox.askyesno("Clear Message", "Do You Want To Clear")


    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmanage")
    cur = conn.cursor()
    cur.execute("delete from students where roll_no=%s", roll_no_var.get())

    conn.commit()
    fetchdata()

    conn.close()


def searchdata():
    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmanage")
    cur = conn.cursor()
    cur.execute("select * from students where "+str(search_by.get())+" LIKE '%"+str(search_txt.get())+"%'")
    rows =cur.fetchall()

    if len(rows) !=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', END, values=row)

        conn.commit()

    conn.close()




########################## All Variable ######################





######################## End #######################################


title_label = Label(root, text="Emad Student Management System",bd=10,relief=GROOVE, font=("times new roman", 40, "bold"), bg="yellow", fg="blue")
title_label.pack(side=TOP, fill=X)

#################### Manage Frame #####################

Manage_frame = Frame(root, bd=4, relief = RIDGE, bg='crimson')
Manage_frame.place(x=20,  y=100, width=410, height=600)

m_title = Label(Manage_frame, text="Manage Students", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
m_title.grid(row=0, columnspan=2, pady=20)

m_roll = Label(Manage_frame, text="Roll No", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
m_roll.grid(row=1, column=0, pady=10, padx=20, sticky=W)

txt_Roll= Entry(Manage_frame,font=("times new roman", 15, "bold"), textvariable = roll_no_var,bd=5, fg="black", relief= GROOVE)
txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky=W)



m_name = Label(Manage_frame, text="Name", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
m_name.grid(row=2, column=0, pady=10, padx=20, sticky=W)

txt_name= Entry(Manage_frame,font=("times new roman", 15, "bold"), textvariable = name_var,bd=5, fg="black", relief= GROOVE)
txt_name.grid(row=2, column=1, pady=10, padx=20, sticky=W)


m_email = Label(Manage_frame, text="Email", font=("times new roman", 15, "bold"),  bg="crimson", fg="white")
m_email.grid(row=3, column=0, pady=10, padx=20, sticky=W)

txt_email= Entry(Manage_frame,font=("times new roman", 15, "bold"),bd=5, fg="black", relief= GROOVE, textvariable = email_var)
txt_email.grid(row=3, column=1, pady=10, padx=20, sticky=W)

m_gender = Label(Manage_frame, text="Gender", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
m_gender.grid(row=4, column=0, pady=10, padx=20, sticky=W)

combo_gender= ttk.Combobox(Manage_frame,font=("times new roman", 13, "bold"), state="readonly",textvariable = gender_var)
combo_gender['values'] = ('male', 'female', 'other')
combo_gender.grid(row=4, column=1, pady=10, padx=30, sticky=W)


m_contact = Label(Manage_frame, text="Contact", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
m_contact.grid(row=5, column=0, pady=10, padx=20, sticky=W)

txt_contact= Entry(Manage_frame,font=("times new roman", 15, "bold"),bd=5, fg="black", relief= GROOVE, textvariable = contact_var)
txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky=W)


m_dob = Label(Manage_frame, text="D.O.B", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
m_dob.grid(row=6, column=0, pady=10, padx=20, sticky=W)

txt_dob= Entry(Manage_frame,font=("times new roman", 15, "bold"),bd=5, fg="black", relief= GROOVE,textvariable = dob_var)
txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky=W)


m_address = Label(Manage_frame, text="Address", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
m_address.grid(row=7, column=0, pady=10, padx=20, sticky=W)

txt_address = Text(Manage_frame, width=26, height=4)
txt_address.grid(row=7, column=1, pady=10, padx=20, sticky=W)

############ Button Frame ##########################


btn_frame = Frame(Manage_frame, bd=4, relief = RIDGE, bg='crimson')
btn_frame.place(x=0,  y=500, width=400)

addbtn_button = Button(btn_frame, text="Add", width=10, command = add_student).grid(row=0, column=0, padx=10, pady=10)
update_button = Button(btn_frame, text="Update", width=10, command = update_data).grid(row=0, column=1, padx=10, pady=10)
delete_button = Button(btn_frame, text="Delete", width=10, command = delete_data).grid(row=0, column=2, padx=10, pady=10)
clear_button = Button(btn_frame, text="Clear", width=10, command = clearall).grid(row=0, column=3, padx=10, pady=10)


##################### Detail Frame #####################

detail_frame = Frame(root, bd=4, relief = RIDGE, bg='crimson')
detail_frame.place(x=500,  y=100, width=790, height=580)

lblserach = Label(detail_frame, text="Search By", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
lblserach.grid(row=0, column=0, pady=10, padx=20, sticky=W)


combo_search= ttk.Combobox(detail_frame, textvariable =search_by,font=("times new roman", 13, "bold"), state="readonly", width=10)
combo_search['values'] = ('roll_no', 'name', 'contact')
combo_search.grid(row=0, column=1, pady=10, padx=30, sticky=W)


txt_search= Entry(detail_frame,textvariable =search_txt,font=("times new roman", 14, "bold"),bd=5, fg="black", relief= GROOVE)
txt_search.grid(row=0, column=2, pady=10, padx=20, sticky=W)

search_button = Button(detail_frame, text="search", width=10, pady=5, command = searchdata).grid(row=0, column=3, padx=10, pady=10)
showall_button = Button(detail_frame, text="Show All", width=10, pady=5, command = fetchdata).grid(row=0, column=4, padx=10, pady=10)


################# Table Frame ##################

tabel_frame = Frame(detail_frame, bd=4, relief = RIDGE, bg='crimson')
tabel_frame.place(x=0,  y=100, width=740, height=400)

scroll_x = Scrollbar(tabel_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(tabel_frame, orient=VERTICAL)
student_table = ttk.Treeview(tabel_frame, columns=("roll", "name","email", 'gender', "contact", "dob", "Address"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command = student_table.xview)
scroll_y.config(command = student_table.yview)

student_table.heading("roll", text="Roll No.")
student_table.heading("name", text="Name.")
student_table.heading("email", text="Email.")
student_table.heading("gender", text="Gender.")
student_table.heading("contact", text="Contact.")
student_table.heading("dob", text="0.0.8")
student_table.heading("Address", text="Address.")
student_table["show"] = 'headings'

student_table.column('roll', width=100)
student_table.column('name', width=100)
student_table.column('email', width=100)
student_table.column('gender', width=100)
student_table.column('contact', width=100)
student_table.column('dob', width=100)
student_table.column('Address', width=150)
student_table.pack(fill=BOTH, expand = 1)
student_table.bind("<ButtonRelease-1>", get_cursor)

fetchdata()







root.mainloop()