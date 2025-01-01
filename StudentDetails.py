from tkinter import Label,Button,Tk,StringVar,Frame,RIDGE,LabelFrame
from tkinter import END, END, END,W,HORIZONTAL,VERTICAL,BOTTOM,RIGHT,X,Y,BOTH, ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        #first img
        img=Image.open(r"up.jpg")
        img=img.resize((1530,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=135)

        #bg img
        img1=Image.open(r"bg.jpg")
        img1=img1.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #===============variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_Student_id=StringVar()
        self.var_name=StringVar()
        self.var_classroll=StringVar()
        self.var_makautroll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_gender=StringVar()
        self.var_teacher=StringVar()
        #title
        title_lbl=Label(text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",27,"bold"),bg="green",fg="skyblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=10,y=45,width=1400,height=550)
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=660,height=200)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select department","Computer","DS","IT","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select course","B.TECH","BE","BCA","MCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select year","2024","2025","2026","2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        #Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=400)
        #Student Id
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_Student_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #Student Name
        studentNAME_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentNAME_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #Student Class roll
        studentROLL_label=Label(class_student_frame,text="Class roll",font=("times new roman",12,"bold"),bg="white")
        studentROLL_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        studentroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_classroll,width=20,font=("times new roman",12,"bold"))
        studentroll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #Student Makaut Roll no
        studentMACAUT_label=Label(class_student_frame,text="MAKAUT roll",font=("times new roman",12,"bold"),bg="white")
        studentMACAUT_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        studentmacaut_entry=ttk.Entry(class_student_frame,textvariable=self.var_makautroll,width=20,font=("times new roman",12,"bold"))
        studentmacaut_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Student Email
        studentEMAIL_label=Label(class_student_frame,text="Student Email",font=("times new roman",12,"bold"),bg="white")
        studentEMAIL_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        studentemail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        studentemail_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #Student Phone Number
        studentPHONE_label=Label(class_student_frame,text="Student Phone No.",font=("times new roman",12,"bold"),bg="white")
        studentPHONE_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        studentphone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        studentphone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #Gender
        gen_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gen_label.grid(row=3,column=0,padx=10,sticky=W)
        gen_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only")
        gen_combo["values"]=("Select gender","MALE","FEMALE","NON-APPLICABLE")
        gen_combo.current(0)
        gen_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #Teacher Name
        studentTNAME_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        studentTNAME_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        studenttname_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        studenttname_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #TakePhotoSample buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=2)
        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=160,width=700,height=70)
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)      
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)       
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)      
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)        

        btn_photo_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_photo_frame.place(x=0,y=195,width=700,height=35)
               
        take_photo_btn=Button(btn_photo_frame,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
                
        update_photo_btn=Button(btn_photo_frame,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=580)
        #=====SEARCH SYSTEM======
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=650,height=60)
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select","Macautroll","StudentID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)
        showall_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)
        #=====TABLE FRAME=====
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=200,width=650,height=260)
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=("dep","course","year","sem","id","name","classroll","makautroll","email","phone","gender","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="StudentName")
        self.student_table.heading("classroll",text="Classroll")
        self.student_table.heading("makautroll",text="Makautroll")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="TakeSamplePhoto")
        self.student_table["show"]="headings"
        #student table column size
        self.student_table.column("dep",width=150)
        self.student_table.column("course",width=150)
        self.student_table.column("year",width=150)
        self.student_table.column("sem",width=150)
        self.student_table.column("id",width=150)
        self.student_table.column("name",width=150)
        self.student_table.column("classroll",width=150)    
        self.student_table.column("makautroll",width=150)
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=150)
        self.student_table.column("gender",width=150)
        self.student_table.column("teacher",width=150)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
    #===========Function declaration============
    def add_data(self):
        if self.var_dep.get()=="Select Department"or self.var_name.get()==""or self.var_Student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Password@12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_dep.get(),
                                                                                       self.var_course.get(),
                                                                                       self.var_year.get(),
                                                                                       self.var_sem.get(),
                                                                                       self.var_Student_id.get(),
                                                                                       self.var_name.get(),
                                                                                       self.var_classroll.get(),
                                                                                       self.var_makautroll.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_phone.get(),
                                                                                       self.var_gender.get(),
                                                                                       self.var_teacher.get(),
                                                                                       self.var_radio1.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

#================fetch data=======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Password@12345", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content.get("values")

        if data:
            if len(data) >= 13:
                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_sem.set(data[3])
                self.var_Student_id.set(data[4])
                self.var_name.set(data[5])
                self.var_classroll.set(data[6])
                self.var_makautroll.set(data[7])
                self.var_email.set(data[8])
                self.var_phone.set(data[9])
                self.var_gender.set(data[10])
                self.var_teacher.set(data[11])
                self.var_radio1.set(data[12])
            else:
                messagebox.showerror("Error", "Incomplete data found in the selected row.")
        else:
            messagebox.showerror("Error", "No data found in the selected row.")

     #================update function============
    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_name.get()==""or self.var_Student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Password@12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,classroll=%s,makautroll=%s,email=%s,phone=%s,gender=%s,teacher=%s,photo=%s where Student_id=%s",(
                                                                                       self.var_dep.get(),
                                                                                       self.var_course.get(),
                                                                                       self.var_year.get(),
                                                                                       self.var_sem.get(),
                                                                                       self.var_name.get(),
                                                                                       self.var_classroll.get(),
                                                                                       self.var_makautroll.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_phone.get(),
                                                                                       self.var_gender.get(),
                                                                                       self.var_teacher.get(),
                                                                                       self.var_radio1.get(),
                                                                                       self.var_Student_id.get()
                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
#==========delete function============
    def delete_data(self):
        if self.var_Student_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Password@12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_Student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
#=============reset function===========
    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_sem.set("Select semester")
        self.var_Student_id.set("")
        self.var_name.set("")
        self.var_classroll.set("")
        self.var_makautroll.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_gender.set("Select gender")
        self.var_teacher.set("")
        self.var_radio1.set("")
     #===========Generate data set or Take photo sample==================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_name.get()==""or self.var_Student_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Password@12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,classroll=%s,makautroll=%s,email=%s,phone=%s,gender=%s,teacher=%s,photo=%s where Student_id=%s",(
                                                                                       self.var_dep.get(),
                                                                                       self.var_course.get(),
                                                                                       self.var_year.get(),
                                                                                       self.var_sem.get(),
                                                                                       self.var_name.get(),
                                                                                       self.var_classroll.get(),
                                                                                       self.var_makautroll.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_phone.get(),
                                                                                       self.var_gender.get(),
                                                                                       self.var_teacher.get(),
                                                                                       self.var_radio1.get(),
                                                                                       self.var_Student_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #======Load predefined data on face frontals from opencv=====

                # Initialize the camera
                cap = cv2.VideoCapture(0)

                # Create a directory for storing the dataset
                if not os.path.exists("dataset"):
                    os.makedirs("dataset")

                # Create a dataset
                count = 0
                while True:
                    ret, frame = cap.read()
                    cv2.imshow("frame", frame)
                    if cv2.waitKey(1) == 13:
                        break
                    if cv2.waitKey(1) == ord('q'):
                        count += 1
                        filename = "dataset/u."+str(id)+"."+ str(count) + ".jpg"
                        cv2.imwrite(filename, frame)
                        messagebox.showinfo("photo", " photo click completed!!")
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
        
if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
