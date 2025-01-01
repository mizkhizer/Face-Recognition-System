from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import face_recognition
import numpy as np

class Train:
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

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 27, "bold"), bg="green", fg="skyblue")
        title_lbl.place(x=0, y=130, width=1530, height=45)


        # Button for face Acquisition
        b1_1 = Button(self.root, text="Face Acquisition", command=self.faceAcquisition, cursor="hand2",  font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=650, y=370, width=200, height=50)

        # Button for training data
        b2_2 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",  font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b2_2.place(x=650, y=470, width=200, height=50)

    def faceAcquisition(self):
        # Path to the directory containing training images
        data_dir = "dataset"

        # Loop through all image files in the directory
        for filename in os.listdir(data_dir):
            # Load the image
            img_path = os.path.join(data_dir, filename)
            img = cv2.imread(img_path)

            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to the image
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply adaptive thresholding to the image
            thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            # Apply morphological operations to the image
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            dilate = cv2.dilate(thresh, kernel, iterations=3)
            erode = cv2.erode(dilate, kernel, iterations=3)

            # Display the image (optional)
            #cv2.imshow("user_1", erode)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        messagebox.showinfo("Result", "Acquisition dataset completed!!")

    def train_classifier(self):
        if not os.path.exists("embeddings"):
            os.makedirs("embeddings")
        data_dir = "dataset"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        images = []
        ids = []
        embeddings = []

        for image_path in path:
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)
            if len(face_encodings) == 1:
                embeddings.append(face_encodings[0])
                ids.append(int(os.path.split(image_path)[1].split('.')[1]))

        ids = np.array(ids)

        # Save the face embeddings
        np.savetxt("embeddings/face_encodings.txt", embeddings)

        messagebox.showinfo("Result", "Training dataset completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
