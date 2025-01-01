import tkinter as tk
from tkinter import Label, Button
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import pandas as pd

class printAttendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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

        title_lbl = Label(self.root, text="UPDATED ATTENDANCE", font=("times new roman", 27, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        # Button for printing attendance
        b1_1 = Button(self.root, text="PRINT ATTENDANCE", command=self.PT, cursor="hand2", font=("times new roman", 10, "bold"), bg="blue", fg="white")
        b1_1.place(x=650, y=370, width=200, height=50)

    def PT(self):
        # Load the attendance log from the JSON file
        with open('attendance.json', 'r') as f:
            attendance_log = json.load(f)

        # Convert the attendance log to a Pandas DataFrame
        df = pd.DataFrame(attendance_log, index=[0])  # Specify an index, for example, [0]

        # Write the attendance data to an Excel file
        writer = pd.ExcelWriter('attendance_log.xlsx')
        df.to_excel(writer, index=False)
        writer.close()
        messagebox.showinfo("Result", "printed!!")

if __name__ == "__main__":
    root = tk.Tk()
    obj = printAttendence(root)
    root.mainloop()
