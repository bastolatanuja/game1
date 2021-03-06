from tkinter import *
import os
from PIL import ImageTk,Image
import pygame
pygame.mixer.init()
import time

def play():
    pygame.mixer.music.load("tkimg\\bsound.mp3")
    pygame.mixer.music.play(loops=0)

#assign velocity
xvelocity=1
yvelocity=2
Xvelocity=2
Yvelocity=1
xvelocity1=2
yvelocity1=2

#Main screen
master = Tk()
master.title('404 NOT FOUND')

master.geometry("639x688")#("639x698")
master.resizable(0,0)
# load=Image.open("Login.png")
# render=ImageTk.PhotoImage(load)
# img=Label(master,image=render)
# img.place(x=0,y=0)

#canvas
canvas=Canvas(master,width=639,height=688)
canvas.pack()

Background = PhotoImage(file='tkimg\\Login.png')
B_image=canvas.create_image(0,0,image=Background,anchor=NW)


photo_image = PhotoImage(file='tkimg\\Ellipse 1.png')
my_image=canvas.create_image(0,0,image=photo_image,anchor=NW)

image2 = PhotoImage(file='tkimg\\blue eclips.png')
mimage2=canvas.create_image(50,0,image=image2,anchor=NW)

image3 = PhotoImage(file='tkimg\\blue eclips.png')
mimage3=canvas.create_image(180,0,image=image2,anchor=NW)


#image width and height
image_width=photo_image.width()
image_height=photo_image.height()

image_width1=image2.width()
image_height1=image2.height()
def goto_sign():
    master.destroy()
    os.system('python signuppage.py')

def goto_login():
    master.destroy()
    os.system('python login.py')



sn_img=Image.open("tkimg\\snbutton.png")
sn_img=ImageTk.PhotoImage(sn_img)

ca_img=Image.open("tkimg\\ca button.png")
ca_img=ImageTk.PhotoImage(ca_img)



#button
std_login_btn=Button(master,image=sn_img,width=255,height=40,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white',activebackground='#00437c' , command =lambda:[play(),goto_login()])

std_login_btn.place(x=187,y=300)


login_btn=Button(master,image=ca_img,width=255,height=40,relief= FLAT,border=0, font=('arial',14,'bold'), bg='#00437c', fg='white',activebackground='#00437c',command= lambda:[play(),goto_sign()])
login_btn.place(x=187,y=390)

#animation
while True:
    coordinates=canvas.coords(my_image)

   #print(coordinates)
    if(coordinates[0]>=(500-image_width) or (coordinates[0]<0)):
        xvelocity= -xvelocity
    if (coordinates[1] >= (600- image_height) or (coordinates[1] < 0)):
        yvelocity = -yvelocity
    if (coordinates[0] >= (360 - image_width1) or (coordinates[0] < 0)):
        Xvelocity = -Xvelocity
    if (coordinates[1] >= (700 - image_height1) or (coordinates[1] < 0)):
        Yvelocity = -Yvelocity
    if (coordinates[0] >= (300 - image_width1) or (coordinates[0] < 0)):
        xvelocity1 = -xvelocity1
    if (coordinates[1] >= (600 - image_height1) or (coordinates[1] < 0)):
        yvelocity1 = -yvelocity1
    canvas.move(my_image, xvelocity, yvelocity)
    canvas.move(mimage2, Xvelocity, Yvelocity)
    canvas.move(mimage3, xvelocity1, yvelocity1)
    master.update()
    time.sleep(0.01)
master.mainloop()