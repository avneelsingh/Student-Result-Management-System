from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class StudentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title Frame
        title=Label(self.root,text="Manage Student Details", font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.course_list = []
        self.var_search = StringVar()
        self.fetch_course()

        # Widgets
        self.lbl_rollno = Label(self.root, text="Roll No", font=("goudy old style",15,"bold"), bg="white").place(x=10, y=60)

        self.lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style",15,"bold"), bg="white").place(x=360, y=60)

        self.lbl_name = Label(self.root, text="Name", font=("goudy old style",15,"bold"), bg="white").place(x=10, y=100)

        self.lbl_contact = Label(self.root, text="Contact", font=("goudy old style",15,"bold"), bg="white").place(x=360, y=100)

        self.lbl_email = Label(self.root, text="Email", font=("goudy old style",15,"bold"), bg="white").place(x=10, y=140)

        self.lbl_addmission = Label(self.root, text="Admission", font=("goudy old style",15,"bold"), bg="white").place(x=360, y=140)

        self.lbl_gender = Label(self.root, text="Gender", font=("goudy old style",15,"bold"), bg="white").place(x=10, y=180)

        self.lbl_course = Label(self.root, text="Course", font=("goudy old style",15,"bold"), bg="white").place(x=360, y=180)
        
        self.lbl_state = Label(self.root, text="State", font=("goudy old style",15,"bold"), bg="white").place(x=10, y=220)

        self.txt_state = Entry(self.root,textvariable=self.var_state, font=("goudy old style",15,"bold"), bg="lightyellow").place(x=150, y=220, width=150)

        self.lbl_city = Label(self.root, text="City", font=("goudy old style",15,"bold"), bg="white").place(x=310, y=220)

        self.txt_city = Entry(self.root,textvariable=self.var_city, font=("goudy old style",15,"bold"), bg="lightyellow").place(x=380, y=220, width=100)

        self.lbl_pin = Label(self.root, text="Pin", font=("goudy old style",15,"bold"), bg="white").place(x=500, y=220)

        self.txt_pin = Entry(self.root,textvariable=self.var_pin, font=("goudy old style",15,"bold"), bg="lightyellow").place(x=560, y=220, width=120)
        
        self.lbl_address = Label(self.root, text="Address", font=("goudy old style",15,"bold"), bg="white").place(x=10, y=260)

        # Entry Fields
        self.txt_rollno = Entry(self.root,textvariable=self.var_roll, font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_rollno.place(x=150, y=60, width=200)

        self.txt_dob = Entry(self.root,textvariable=self.var_dob, font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_dob.place(x=485, y=60, width=200)

        self.txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_name.place(x=150, y=100, width=200)

        self.txt_contact = Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_contact.place(x=485, y=100, width=200)

        self.txt_email = Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_email.place(x=150, y=140,width=200)

        self.txt_addmission = Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_addmission.place(x=485, y=140,width=200)

        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=150, y=180,width=200)
        self.txt_gender.current(0)

        self.txt_course = ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=485, y=180,width=200)
        self.txt_course.set("Select")

        self.txt_address = Text(self.root, font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=260, width=540, height=100)

        # Buttons
        self.btn_add = Button(self.root, text="Add", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search Panel
        self.lbl_Search_rollno = Label(self.root, text="Roll No:", font=("goudy old style",16,"bold"), bg="white")
        self.lbl_Search_rollno.place(x=700, y=60)

        self.txt_Search_rollno = Entry(self.root,textvariable=self.var_search, font=("goudy old style",15,"bold"), bg="lightyellow")
        self.txt_Search_rollno.place(x=850, y=60, width=190)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1070, y=60, width=120, height=28)

        # Content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.StudentTable = ttk.Treeview(self.C_Frame, columns=("roll","name","email","gender","dob","contact","course","admission","state","city","pin","address"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)

        self.StudentTable.heading("roll", text="Roll No")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("dob", text="D.O.B")
        self.StudentTable.heading("contact", text="Contact")
        self.StudentTable.heading("course", text="Course")
        self.StudentTable.heading("admission", text="Admission")
        self.StudentTable.heading("state", text="State")
        self.StudentTable.heading("city", text="City")
        self.StudentTable.heading("pin", text="PIN")
        self.StudentTable.heading("address", text="Address")

        self.StudentTable["show"] = "headings"

        self.StudentTable.column("roll",width=100)
        self.StudentTable.column("name",width=100)
        self.StudentTable.column("email",width=100)
        self.StudentTable.column("gender",width=100)
        self.StudentTable.column("dob",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("course",width=100)
        self.StudentTable.column("admission",width=100)
        self.StudentTable.column("state",width=100)
        self.StudentTable.column("city",width=100)
        self.StudentTable.column("pin",width=100)
        self.StudentTable.column("address",width=200)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    # Function to clear the input fields
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_course.set("Select"),
        self.var_a_date.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END)
        self.txt_rollno.config(state=NORMAL)
        self.var_search.set("")

    # Function to get data from the selected row    
    def get_data(self,ev):
        self.txt_rollno.config(state="readonly")
        r = self.StudentTable.focus()
        content = self.StudentTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_course.set(row[6]),
        self.var_a_date.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])

    # Function to add a new student to the database
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        roll = self.var_roll.get().strip()
        name = self.var_name.get().strip()
        email = self.var_email.get().strip()
        state = self.var_state.get().strip()
        city = self.var_city.get().strip()
        pin = self.var_pin.get().strip()
        contact = self.var_contact.get().strip()

        if roll=="":
            messagebox.showerror("Error","Roll Number should be required",parent=self.root)
        elif not roll.isdigit():
            messagebox.showerror("Error","Roll No should contain only Integer values",parent=self.root)

        elif name == "":
            messagebox.showerror("Error","Name should be required",parent=self.root)
        elif not name.replace(" ", "").isalpha():
            messagebox.showerror("Error","Name should contain only letters",parent=self.root)
                
        elif email == "":
            messagebox.showerror("Error","Email should be required",parent=self.root)
        elif not email.endswith('@gmail.com'):
                messagebox.showerror("Error","Email should end with @gmail.com",parent=self.root)

        elif state == "":
            messagebox.showerror("Error","State should be required",parent=self.root)
        elif not state.replace(" ", "").isalpha():
            messagebox.showerror("Error","State name should contain only letters",parent=self.root)

        elif city == "":
            messagebox.showerror("Error","City should be required",parent=self.root)
        elif not city.replace(" ", "").isalpha():
            messagebox.showerror("Error","City name should contain only letters",parent=self.root)

        elif not pin.isdigit():
            messagebox.showerror("Error","PIN should contain only Integer values",parent=self.root)
        elif len(pin) != 6:
            messagebox.showerror("Error","PIN should contain exactly 6 digits",parent=self.root)

        elif not contact.isdigit():
            messagebox.showerror("Error","Phone Number should contain only Integers",parent=self.root)
        elif len(contact) != 10:
            messagebox.showerror("Error","Phone Number should contain exactly 10 digits",parent=self.root)

        else:
            try:
                cur.execute("SELECT * FROM student WHERE roll=?",(roll,))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","Roll No already present",parent=self.root)
                else:
                    cur.execute("""INSERT INTO student(roll, name, email, gender, dob, contact, course, admission, state, city, pin, address) VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (roll,name,email,self.var_gender.get(),self.var_dob.get(),contact,self.var_course.get(),self.var_a_date.get(),state,city,pin,self.txt_address.get("1.0", END)))
                
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
            finally:
                con.close()

    # Function to delete a student from the database
    def delete(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            selected = self.StudentTable.focus()
            if selected == "":
                messagebox.showerror("Error","Select Student from List",parent=self.root)
                return

            data = self.StudentTable.item(selected)
            row = data.get("values")
            if not row:
                messagebox.showerror("Error","Please select a valid student",parent=self.root)
                return
            
            roll = row[0]
            op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)

            if op:
                cur.execute("DELETE FROM student WHERE roll=?",(roll,))
                con.commit()
                messagebox.showinfo("Delete","Student Deleted Successfully",parent=self.root)
                self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        finally:
            con.close()

    # Function to update a course in the database
    def update(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()

        roll = self.var_roll.get().strip()
        name = self.var_name.get().strip()
        email = self.var_email.get().strip()
        state = self.var_state.get().strip()
        city = self.var_city.get().strip()
        pin = self.var_pin.get().strip()
        contact = self.var_contact.get().strip()
        
        if roll == "":
            messagebox.showerror("Error","Roll Number should be required",parent=self.root)
        elif not roll.isdigit():
            messagebox.showerror("Error","Roll Number should contain only Integer values",parent=self.root)

        elif name == "":
            messagebox.showerror("Error","Name should be required",parent=self.root)
        elif not name.replace(" ", "").isalpha():
            messagebox.showerror("Error","Name should contain only letters",parent=self.root)

        elif email == "":
            messagebox.showerror("Error","Email should be required",parent=self.root)
        elif not email.endswith("@gmail.com"):
            messagebox.showerror("Error","Email should end with @gmail.com",parent=self.root)

        elif state == "":
            messagebox.showerror("Error","State should be required",parent=self.root)
        elif not state.replace(" ", "").isalpha():
            messagebox.showerror("Error","State name should contain only letters",parent=self.root)

        elif city == "":
            messagebox.showerror("Error","City should be required",parent=self.root)
        elif not city.replace(" ", "").isalpha():
            messagebox.showerror("Error","City name should contain only letters",parent=self.root)

        elif not pin.isdigit() or len(pin) != 6:
            messagebox.showerror("Error","PIN should contain exactly 6 digits",parent=self.root)

        elif not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Error","Phone Number should contain exactly 10 digits",parent=self.root)
        else:
            try:
                selected = self.StudentTable.focus()
                if selected == "":
                    messagebox.showerror("Error","Select Student from List",parent=self.root)
                    return

                data = self.StudentTable.item(selected)
                row = data.get("values")
                if not row:
                    messagebox.showerror("Error","Please select a valid student",parent=self.root)
                    return
            
                student_id = row[0]

                cur.execute("UPDATE student SET name=?,email=?,gender=?,dob=?,contact=?,course=?,admission=?,state=?,city=?,pin=?,address=? WHERE roll=?",
                (name,email,self.var_gender.get(),self.var_dob.get(),contact,self.var_course.get(),self.var_a_date.get(),state,city,pin,self.txt_address.get("1.0", END),student_id))

                con.commit()
                messagebox.showinfo("Success","Student Updated Successfully",parent=self.root)
                self.show()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

            finally:
                con.close()
                
    # Function to show all students in the Treeview
    def show(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows=cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        finally:
            con.close()

    # Function to fetch courses from the database and store it in the course list
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        finally:
            con.close()

    # Function to search courses by name
    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            roll = self.var_search.get().strip()
            if roll == "":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
                return
            
            cur.execute("SELECT * FROM student WHERE roll=?", (roll,))
            row=cur.fetchone()
            if row is not None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                self.StudentTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

        finally:
            con.close()   

if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()