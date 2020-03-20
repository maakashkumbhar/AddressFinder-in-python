from tkinter import *
from PIL import ImageTk,Image
import qrcode


root = Tk()
root.title("Address Finder")

#Longitude Label and entry for the Same
Longitude_label = Label(root,text="Longitude")
Longitude_label.grid(row=0,column=0)


Longitutde_entry = Entry(root,width = 30)
Longitutde_entry.grid(row=0,column=1)

#Latitude Label and Entry for the same
Latitude_label = Label(root,text="Latitude")
Latitude_label.grid(row=1,column=0)


Latitude_entry = Entry(root,width = 30)
Latitude_entry.grid(row=1,column=1)

##Frame to Display the Maps 
frame_for_maps = LabelFrame(root,text = "Map is Diplayed here",padx=20,pady=20)
frame_for_maps.grid(row=2,column=0)

##Showing image on the Frame
Image_to_display = ImageTk.PhotoImage(Image.open("55.jpg"))
Image_Label = Label(frame_for_maps,image=Image_to_display)
Image_Label.grid(row=4,column=0,columnspan=3)
## Frame for Qr Code LookUp

frame_for_Qr = LabelFrame(root,text="QrCode will be shown here",padx=20,pady=20)
frame_for_Qr.grid(row=3,column=0)
#making a function for generating the qr code For the Langitude and Latitude entered

def make_qr():
    lat=321423434
    qr = qrcode.make(data=lat)
    qr.save('File1.png')
    label_file = ImageTk.PhotoImage(Image.open("File1.png"))
    label_file = Label(frame_for_Qr,image=label_file)
    label_file.grid(row=5,column=1)
Button_to_display = Button(root,text="ClickToseeQR",command=make_qr)
Button_to_display.grid(row =4,column=4)
root.mainloop()

