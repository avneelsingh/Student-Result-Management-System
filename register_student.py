from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os

class RegisterStudent:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Background Image
        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        # Left Image
        self.left = ImageTk.PhotoImage(file="images/side.png")
        left = Label(self.root,image=self.left).place(x=80,y=100,width=400 , height=500)

        # Register Frame
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        self.title = Label(frame1,text="Student Registration",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        # Row 1
        f_name = Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name = Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_lname.place(x=370,y=130,width=250)
        
        
        # Row 2
        contact = Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_contact.place(x=50,y=200,width=250)
        
        email = Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_email.place(x=370,y=200,width=250)
        
        
        # Row 3
        question = Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        self.cmb_quest = ttk.Combobox(frame1,font=("times new roman",13,"bold"),state="readonly",justify=CENTER)
        self.cmb_quest["values"] = ("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name","Your Favorite Crickter Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_answer.place(x=370,y=270,width=250)


        # Row 4
        password = Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_password.place(x=50,y=340,width=250)
        
        c_password = Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword = Entry(frame1,font=("times new roman",15,"bold"),bg='lightgray')
        self.txt_cpassword.place(x=370,y=340,width=250)

        # Terms and Conditions
        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text="I Agree Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",13,"bold")).place(x=50,y=380)

        self.btn_image = ImageTk.PhotoImage(file="images/register.png")
        btn_register = Button(frame1,image=self.btn_image,bd=0,cursor="hand2",command=self.Register).place(x=50,y=420)
        
        btn_login = Button(self.root,text="Sign In",font=("times new roman",20,"bold"),command=self.login_window,bd=0,cursor="hand2").place(x=190,y=460,width=180)

    def login_window(self):
        self.root.destroy()
        os.system("python login_student.py") 

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END) 
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)

    def Register(self):
        f_name = self.txt_fname.get()
        l_name = self.txt_lname.get()
        contact = self.txt_contact.get()
        email = self.txt_email.get()
        password = self.txt_password.get()
        cpassword = self.txt_cpassword.get()
        question = self.cmb_quest.get()
        answer = self.txt_answer.get().strip()

        if (f_name=="" or l_name=="" or contact=="" or email=="" or question=="" or answer=="" or password=="" or cpassword==""):

            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif not f_name.replace(" ", "").isalpha():
            messagebox.showerror("Error","First Name should contain only letters",parent=self.root)

        elif not l_name.replace(" ", "").isalpha():
            messagebox.showerror("Error","Last Name should contain only letters",parent=self.root)

        elif contact.isdigit():
            messagebox.showerror("Error","Phone Number should contain only digits",parent=self.root)

        elif len(contact) != 10:
            messagebox.showerror("Error","Phone Number should contain exactly 10 digits",parent=self.root)

        elif email.endswith('@gmail.com'):
            messagebox.showerror("Error","Email should end with @gmail.com",parent=self.root)

        elif question == "Select":
            messagebox.showerror("Error","Please select a question",parent=self.root)

        elif len(password) < 6:
            messagebox.showerror("Error","Password should contain atleast 6 characters",parent=self.root)

        elif password != cpassword:
            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please Agree Our Terms and Conditions",parent=self.root)

        else:
            con=None
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from student_regis where email=?",(email,))

                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","User Already Exists, Please Try With Another Email",parent=self.root)

                else:
                    cur.execute("INSERT INTO student_regis(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                    (f_name,l_name,contact,email,question,answer,password))

                    con.commit()
                    
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()
                    self.login_window()

            except Exception as ex:
                messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)
            
            finally:
                if con is not None:
                    con.close()    

root = Tk()
obj = RegisterStudent(root)
root.mainloop()