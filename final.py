from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import numpy as np
import cv2
import imutils
import pytesseract
from easyocr import Reader
import mysql.connector
from datetime import datetime

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


print("Press SPACE to capture image \n")
print("Press ESC to close Camera\n")
cam = cv2.VideoCapture(0)
cv2.namedWindow("LPR windows 1")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("LPR window 1", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
       # img_name = "opencv_frame_{}.png".format(img_counter)
      # img_name = "opencv.png".format(img_counter)
        img_name = "opencv.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()


img = Image.open("opencv.png")
#img=Image.open("opencv.png")
img = cv2.imread('opencv.png',cv2.IMREAD_COLOR)
#img=cv2.imread('opencv.png',cv2.IMREAD_COLOR)
img = cv2.resize(img, (800,600) )

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray, (5,5), 0) 
edged = cv2.Canny(blur, 10, 200) 

#cv2.imshow("1 - Grayscale Conversion", gray)
#cv2.waitKey(0)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
#gray = cv2.bilateralFilter(gray, 11, 17, 17)
#cv2.imshow("2 - Bilateral Filter", gray)
#cv2.waitKey(0)

# Find Edges of the grayscale image
#edged = cv2.Canny(gray, 170, 200)
#cv2.imshow("3 - Canny Edges", edged)
#cv2.waitKey(0)

# Find contours based on Edges
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Create copy of original image to draw all contours
img1 = img.copy()
cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)
#cv2.imshow("4- All Contours", img1)
#cv2.waitKey(0)

# sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumberPlateCnt = None  # we currently have no Number plate contour

# Top 30 Contours
img2 = img.copy()
cv2.drawContours(img2, cnts, -1, (0, 255, 0), 3)
#cv2.imshow("5- Top 30 Contours", img2)
#cv2.waitKey(0)

# loop over our contours to find the best possible approximate contour of number plate
count = 0
idx = 7
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    # print ("approx = ",approx)
    if len(approx) == 4:  # Select the contour with 4 corners
        NumberPlateCnt = approx  # This is our approx Number Plate Contour

        # Crop those contours and store it in Cropped Images folder
        x, y, w, h = cv2.boundingRect(c)  # This will find out co-ord for plate
        new_img = gray[y:y + h, x:x + w]  # Create new image
        cv2.imwrite('Cropped Images-Text/' + str(idx) + '.png', new_img)  # Store new image
        idx += 1

        break

# Drawing the selected contour on the original image
# print(NumberPlateCnt)
cv2.drawContours(img, [NumberPlateCnt], -1, (0, 255, 0), 3)
#cv2.imshow("Final Image With Number Plate Detected", img)
#cv2.waitKey(0)

Cropped_img_loc = 'Cropped Images-Text/7.png'
cv2.imshow("Cropped Image ", cv2.imread(Cropped_img_loc))

# Use tesseract to covert image into string
#name_text = pytesseract.image_to_string(Cropped_img_loc, lang='eng')
name_text = pytesseract.image_to_string(Cropped_img_loc, config='--psm 13')
print("Number is :", name_text)

#reader = Reader(['en'])
# detect the text from the license plate
#detection = reader.readtext(Cropped_img_loc, allowlist='0123456789KLBCEF')


#if len(detection) == 0:
    # if the text couldn't be read, show a custom message
 #    text = "Impossible to read the text from the license plate"
    #cv2.putText(img, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 3)
   # cv2.imshow('Image', img)
   #  cv2.waitKey(0)
#else:
    # draw the contour and write the detected text on the image
    # cv2.drawContours(img, [n_plate_cnt], -1, (0, 255, 0), 3)
   # text = f"{detection[0][1]} {detection[0][2] * 100:.2f}%"
 #    name_text=f"{detection[0][1]}"
   # cv2.putText(img, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    # display the license plate and the output image
    #cv2.imshow('license plate', license_plate)
   # cv2.imshow('Image', img)
   #  print(name_text)
    # cv2.waitKey(0)

 #database connection phase
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="12345",
  database='LPR'
)
 
cursorObject = dataBase.cursor()

dt=datetime.now()
date=dt.date()
time=dt.time()

cursorObject.execute('insert into VEHICLE(Vehicle_no,Date,Time) values(%s,%s, %s)', (name_text,date,time))

dataBase.commit()
# Disconnecting from the server
dataBase.close()   
#UI front end phase
root = Tk()
img = PhotoImage(file="Bg.png")
label = Label(root, image=img)
label.pack()

TextBox = PhotoImage(file="TextBox.png")
TextBoxlabel = Label(root, image=TextBox, border=0)
TextBoxlabel.place(x=385, y=218)

# Textbox
nametext = Label(root, text=name_text, border=0, bg='white', foreground='#1A1A1A', font=("arial", 14))
nametext.place(x=435, y=220)

#button = PhotoImage(file="button.png")
#Buttonlabel = Button(root, image=button, border=0)
#Buttonlabel.place(x=385, y=270)

#button2 = PhotoImage(file="Button21.png", )
#Buttonlabel = Button(root, image=button2, border=0)
#Buttonlabel.place(x=385, y=322)

# Wait for user input before closing the images displayed
if cv2.waitKey(0) == 113:
    exit()
cv2.destroyAllWindows()

root.mainloop()
