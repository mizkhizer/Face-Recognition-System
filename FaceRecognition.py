import cv2
import numpy as np
from PIL import Image, ImageTk
from tkinter import Label
import face_recognition
import mysql.connector
import tkinter as tk
import json
from datetime import datetime

class FaceRecognitionSystem:
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

        title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 27, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        b1_1 = tk.Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 16, "bold"), bg="darkgreen", fg="white", command=self.face_recognize)
        b1_1.place(x=650, y=420, width=200, height=40)

    def mark_attendance(self, i):
        conn = mysql.connector.connect(host="localhost", user="root", password="Password@12345", database="face_recognizer")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM student WHERE student_id = %s", (i,))
        result = my_cursor.fetchone()

        if result:
            student_id,dep, classroll, name =result[4], result[0], result[6], result[5]
            with open("attendance.json","a") as f:
                json.dump({"Student_id": student_id, "classroll": classroll, "name": name, "dep": dep, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, f)
            conn.commit()

    def face_recognize(self):
        embeddings = np.loadtxt("embeddings/face_encodings.txt")
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations)

            for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(embeddings, [face_encoding])

                if True in matches:
                    index = matches.index(True)
                    id = index + 1
                    self.mark_attendance(id)

                for (x, y, w, h) in face_locations:
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
                    cv2.putText(img, "Recognized", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
