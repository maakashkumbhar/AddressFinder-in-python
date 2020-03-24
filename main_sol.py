from tkinter import *
import qrcode
from PIL import ImageTk,Image

#Function for getting the Data From entry#
def To_get_data():
    s1 = str(Label_entry1.get())
    s2 = str(Label_entry2.get())
    qr1 = qrcode.make(data=s1)
    qr2 = qrcode.make(data=s2)
    qr1.save('File2.png')
    qr2.save('File3.png')
    label_file1 = ImageTk.PhotoImage(Image.open("File2.png"))
    label_file1 = Label(Frame_For_QrCode,image=label_file1)
    label_file1.grid(row=5,column=1)
    label_file2 = ImageTk.PhotoImage(Image.open("File3.png"))
    label_file2 = Label(Frame_For_QrCode,image=label_file2)
    label_file2.grid(row=5,column=1)
    
# making the functional Window of the tkinter app

root = Tk()
###############
# label of the Window
root.title("Address Finder")

#Label for Longitude 
Label_Longitude = Label(root,text="Longitude")
Label_Longitude.grid(row=0,column=0)

Label_entry1 = Entry(root,width=20)
Label_entry1.grid(row=0,column=1)


#Label for Latitude 
Label_Latitude = Label(root,text="Latitude")
Label_Latitude.grid(row=0,column=2)

Label_entry2 = Entry(root,width=20)
Label_entry2.grid(row=0,column=3)

# Frame For The Space to Display QrCode1
Frame_For_QrCode = LabelFrame(root,height=200,width=500,text="Space to display The QrCode1")
Frame_For_QrCode.grid(row=1,rowspan=2)

# Frame For The Space to Display QrCode2
Frame_For_QrCode2 = LabelFrame(root,height=200,width=500,text="Space to display The QrCode2")
Frame_For_QrCode.grid(row=2,rowspan=2)


#Button to Get the data

Button1 = Button(root,text="Submit",command=To_get_data)
Button1.grid(row=2,column=1,columnspan=2)


###############
#the Continous loop which enebels the Tjinter to know wahts going on in the application
root.mainloop()