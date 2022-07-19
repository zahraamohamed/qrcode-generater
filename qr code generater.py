# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 00:37:06 2022

@author: zahraa resen
"""
import qrcode
from tkinter import *
from tkinter import messagebox


#Creating the window
window = Tk()
window.title(' QR Code Generator')
window.geometry('700x700')
window.config(bg='whitesmoke')

#Function to generate the QR code and save it
def generateCode():
  #Creating a QRCode object of the size specified by the user
  qr = qrcode.QRCode(version = 3,
            box_size = 10,
            border = 5)
  qr.add_data(text.get()) #Adding the data to be encoded to the QRCode object
  qr.make(fit = True) #Making the entire QR Code space utilized
  img = qr.make_image() #Generating the QR Code
  fileLocation=loc.get()+'\\'+name.get() #Getting the directory where the file has to be save
  img.save(f'{fileLocation}.png') #Saving the QR Code
   #Showing the pop up message on saving the file
  messagebox.showinfo(" QR Code Generator","QR Code is saved successfully!")


   
  
#Label for the window
headingFrame = Frame(window,bg="whitesmoke",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code  ", bg='whitesmoke', font=('cairo',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR code
Frame1 = Frame(window,bg="whitesmoke")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text="Enter the text/URL: ",bg="whitesmoke",fg='black',font=('cairo',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('cairo'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the location to save QR Code
Frame2 = Frame(window,bg="whitesmoke")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

label2 = Label(Frame2,text="Enter the location to save the QR Code: ",bg="whitesmoke",fg='black',font=('cairo',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)

loc = Entry(Frame2,font=('cairo'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name
Frame3 = Frame(window,bg="whitesmoke")
Frame3.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="whitesmoke",fg='black',font=('cairo',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('cairo'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Button to generate and save the QR Code
button = Button(window, text='Generate Code',font=('Courier',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
window.mainloop()

