from tkinter import Label,Button,Toplevel,Tk
from tkinter import ttk
from PIL import Image,ImageTk
import os
from students import Student
from trains import Train
from facerecognitions import FaceRecognitionSystem
from Attendenceprint import printAttendence

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

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

        #title
        title_lbl=Label(text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="green",fg="skyblue")
        title_lbl.place(x=0,y=128,width=1530,height=45)
        

        #Student button1
        b1_1=Button(text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=250,width=150,height=40)

        #Detect face button 2
        b1_1=Button(text="DETECT FACE",command=self.face_data,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        b1_1.place(x=750,y=250,width=150,height=40)

        #Attendance face button3
        b1_1=Button(text="ATTENDENCE MARKING",command=self.Attendence_print,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        b1_1.place(x=1050,y=250,width=150,height=40)

        #Help button4
        b1_1=Button(text="HELP",cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=480,width=150,height=40)

        #Train data button5 
        b1_1=Button(text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("times new roman",10,"bold"),bg="blue",fg="white")
        b1_1.place(x=750,y=480,width=150,height=40)

        #Photos button6 
        b1_1=Button(text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="blue",fg="white")
        b1_1.place(x=1050,y=480,width=150,height=40)
    def open_img(self):
        os.startfile("dataset")

#==========Functions button============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognitionSystem(self.new_window)
    def Attendence_print(self):
        self.new_window=Toplevel(self.root)
        self.app=printAttendence(self.new_window)
    


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
