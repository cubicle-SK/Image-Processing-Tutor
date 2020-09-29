#!/usr/bin/env python
# coding: utf-8

# In[62]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog as tkFileDialog
from tkinter.filedialog import askdirectory
from PIL import Image,ImageTk, ImageFilter
import numpy as np
from skimage.util import random_noise
import cv2
from scipy.ndimage import convolve as conv
from scipy.ndimage import correlate as corr
import pydicom
import datetime

class MyWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.dodo=Button(self, text='open dicom file', command=self.dcm).pack()
        self.dodo1=Button(self,text='open image file', command=self.img).pack()
        self.canvas = Canvas(self,width=450, height=500, bg='white')   
        self.canvas.place(x=0,y=60) 
        self.canvas.create_rectangle(10, 10, 440, 500, width=2)
        widget = Label(self.canvas, text='AMITY', fg='blue',font=('Times New Roman',38), anchor=CENTER)
        widget.place(x=168,y=15)
        widget = Label(self.canvas, text='UNIVERSITY', fg='blue',font=('Times New Roman',21), anchor=CENTER)
        widget.place(x=166, y=55)
        widget = Label(self.canvas, text='GURGAON', fg='blue',font=('Times New Roman',12), anchor=CENTER)
        widget.place(x=200,y=83)
        self.canvas.create_line(180, 93, 285, 93, fill='blue')
        widget = Label(self.canvas, text='IMAGE PROCESSING TUTOR', fg='green', font=('Comic Sans MS',20), anchor=CENTER)
        widget.place(x=80,y=140)
        self.canvas.create_line(10, 230, 440, 230)
        widget = Label(self.canvas, text='Developed By :', font=('Arial',16), anchor=CENTER)
        widget.place(x=180,y=240)
        widget = Label(self.canvas, text='Ms. SAUMYA KANSAL', font=('Arial',16), anchor=CENTER)
        widget.place(x=150,y=260)
        widget = Label(self.canvas, text='Guided By :', font=('Arial',16), anchor=CENTER)
        widget.place(x=190,y=290)
        widget = Label(self.canvas, text='Mr. SANDEEP PANWAR JOGI', font=('Arial',16), anchor=CENTER)
        widget.place(x=120,y=310)
        self.canvas.create_line(10, 350, 440, 350)
        widget = Label(self.canvas, text='DEPARTMENT OF BIOMEDICAL ENGINEERING', font=('Times New Roman',15,'bold'), anchor=CENTER, fg='blue')
        widget.place(x=39,y=450)
        widget = Label(self.canvas, text='AMITY SCHOOL OF ENGINEERING AND TECHNOLOGY', font=('Times New Roman',15,'bold'), anchor=CENTER,fg='blue')
        widget.place(x=11,y=469)
        self.label=Label(self, image=None)
        self.label.pack()
        self.btn1 = Button(self, text='color', command=self.color, state='disabled')
        #self.btn1.pack()
        self.btn2=Button(self, text='noise', command=self.noise, state='disabled')
        #self.btn2.pack()
        self.b1=Button(self, text='rotate', command=self.rotate, state='disabled')
        #self.b1.pack()
        self.b2=Button(self, text='filter', command=self.filtre, state='disabled')
        #self.b2.pack()
        self.b5=Button(self, text='compare', command=self.compare, state='normal')
        #self.b5.pack()
        self.b5.place(x=300, y=660)
        self.b1.place(x=250, y=625)
        self.b2.place(x=350, y=625)
        self.btn1.place(x=50, y=625)
        self.btn2.place(x=150, y=625)
    
    def dcm(self):
        try:
            self.T.pack_forget()
        except:
            True
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        try:
            self.btn1.configure(state='disabled')
            self.btn2.configure(state='disabled')
            self.b1.configure(state='disabled')
            self.b2.configure(state='disabled')
            self.b5.configure(state='disabled')
        except:
            True
        try:
            self.label.pack_forget()
        except:
            True
        self.canvas.destroy()
        self.denter()
        self.b3=Button(self, text='browse', command=self.denter)
        #self.b3.pack()
        self.b3.place(x=100, y=660)
        self.b4=Button(self, text='Save_dcm', command=self.save_dicom,state='disabled')
        #self.b4.pack()
        self.b4.place(x=200, y=660)
        self.b5.configure(state='disabled')
    def img(self):
        try:
            self.T.pack_forget()
        except:
            True
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        try:
            self.btn2.configure(state='disabled')
            self.b1.configure(state='disabled')
            self.b2.configure(state='disabled')
        except:
            True
        try:
            self.label.pack_forget()
        except:
            True
        self.enter()
        self.canvas.destroy()
        self.b3=Button(self, text='browse', command=self.enter)
        #self.b3.pack()
        self.b3.place(x=100, y=660)
        self.b4=Button(self, text='Save_img', command=self.save,state='disabled')
        #self.b4.pack()
        self.b4.place(x=200, y=660)
        self.b5.configure(state='disabled')
    
    def compare(self):
        def comp():
            try:
                if self.counting==1:
                    True
            except:
                self.counting=0
            n=int(sp.get())
            if self.counting==1:
                self.comp.destroy()
            else:
                self.counting=1
                for oop in range(1,n+1):
                    ifile = tkFileDialog.askopenfile(parent=self.comp,mode='rb',title='Choose a file')
                    path = ifile.name
                    image=Image.open(path)
                    w,h=image.size
                    if h>300:
                        image=image.resize((int(w/2),int(h/2)))
                    w,h=image.size
                    if h>300:
                        image=image.resize((int(w/2),int(h/2)))
                    render=ImageTk.PhotoImage(image)
                    p,q=image.size
                    self.com_b.configure(text='exit')
                    self.label_com = Label(self.comp, image=render)
                    self.label_com.image=render
                    if oop==1:
                        a=p
                        b=q
                        self.label_com.place(x=10,y=80)
                        #dimx=x+a
                        #dimy=y+b
                    elif oop==2:
                        b1=q
                        self.label_com.place(x=12+a,y=80)
                        #dimx=x+p
                        #dimy=dimy
                    elif oop==3:
                        a=p
                        if b>b1:
                            bf=b
                        else:
                            bf=b1
                        self.label_com.place(x=10,y=82+bf)
                        #dimx=dimx
                        #dimy=y+q
                    elif oop==4:
                        self.label_com.place(x=12+a,y=82+bf)
                        #dimx=x+p
                        #dimy=y+q
                #print(dimx,dimy)
                #self.comp.geometry(str(dimx)+"x"+str(dimy)+"+10+10")
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        self.comp=Toplevel(self)
        self.comp.title('compare')
        texti=Label(self.comp, text='choose number of files to compare')
        texti.pack()
        sp = Spinbox(self.comp, from_= 1, to = 4)
        sp.pack()
        self.com_b=Button(self.comp, text='enter', command=comp)
        self.com_b.pack()
        
        
    def save(self):
        filename = tkFileDialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
             return
        self.to_save=self.to_save.convert('RGB')
        self.to_save.save(filename)
        self.text=Label(self,wraplength=450,text='file saved'+str(filename))
        self.text.pack()
        
    def save_dicom(self):
        photo=self.to_save.copy()
        w,h=photo.size
        photo=photo.resize((int(w*2),int(h*2)))
        photo=np.asarray(photo)
        self.dcm_file.PixelData=photo.tostring()
        filename = tkFileDialog.asksaveasfile(mode='wb', defaultextension=".dcm")
        if not filename:
             return
        self.dcm_file.Rows=w*2
        self.dcm_file.Columns=h*2
        dt = datetime.datetime.now()
        self.dcm_file.ContentDate = dt.strftime('%Y%m%d')
        timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
        self.dcm_file.ContentTime = timeStr
        self.dcm_file.HighBit = 7
        self.dcm_file.BitsStored = 8
        self.dcm_file.BitsAllocated = 8
        self.T.insert(END,str(self.dcm_file))
        self.dcm_file.save_as(filename)
        self.text=Label(self,wraplength=450,text='file Upadted')
        self.text.pack()
   
    def save_dicom_f(self):
        photo=self.to_save_f.copy()
        w,h=photo.size
        photo=photo.resize((int(w*2),int(h*2)))
        photo=np.asarray(photo)
        self.dcm_file.PixelData=photo.tostring()
        filename = tkFileDialog.asksaveasfile(mode='wb', defaultextension=".dcm")
        if not filename:
             return
        self.dcm_file.Rows=w*2
        self.dcm_file.Columns=h*2
        dt = datetime.datetime.now()
        self.dcm_file.ContentDate = dt.strftime('%Y%m%d')
        timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
        self.dcm_file.ContentTime = timeStr
        self.dcm_file.HighBit = 7
        self.dcm_file.BitsStored = 8
        self.dcm_file.BitsAllocated = 8
        self.T.insert(END, str(self.dcm_file))
        self.dcm_file.save_as(filename)
        self.text=Label(self,wraplength=450,text='file updated')
        self.text.pack()
        
    def save_f(self):
        filename = tkFileDialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
             return
        self.to_save_f=self.to_save_f.convert('RGB')
        self.to_save_f.save(filename)
        self.text=Label(self,wraplength=450,text='file saved'+str(filename))
        self.text.pack()
        
    def enter(self):
        try:
            self.codeb4.forget()
        except:
            None
        ifile = tkFileDialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        path = ifile.name
        self.image=Image.open(path)
        self.btn1.configure(state='normal')
        self.btn2.configure(state='normal')
        self.b1.configure(state='normal')
        self.b2.configure(state='normal')
        self.b5.configure(state='normal')
        w,h=self.image.size
        if h>300:
            self.image_new = self.image.resize((int(w/2),int(h/2)))
        else:
            self.image_new = self.image
        self.render = ImageTk.PhotoImage(self.image_new)
        self.label.configure(image=self.render)
        self.label.image=self.render
        self.label.pack()
        self.naam='image'
        self.codeb4=Button(self, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=100)
        self.codeb4.pack()
        w,h=self.image_new.size
        #print(w,h)
        if h>300:
            self.image_new=self.image_new.resize((int(w/2),int(h/2)))
        #elif h<150:
        #    self.image_new=self.image_new.resize((int(w*2),int(h*2)))

    def denter(self):
        try:
            self.codeb4.forget()
        except:
            None
        ifile = tkFileDialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        path = ifile.name
        im=pydicom.dcmread(path)        
        self.dcm_file=pydicom.dcmread(path)
        #print(str(im))
        photo=np.array(im.pixel_array)
        photo=np.uint8(cv2.normalize(photo, None, 0, 255, cv2.NORM_MINMAX))
        photo=cv2.equalizeHist(photo)
        self.image_new=Image.frombytes('L', (photo.shape[1],photo.shape[0]), photo.astype('b').tostring())
        self.render = ImageTk.PhotoImage(image=self.image_new) 
        self.label.configure(image=self.render)
        self.label.image=self.render
        self.label.pack()
        self.btn2.configure(command=self.dnoise,state='normal')
        self.b1.configure(command=self.drotate,state='normal')
        self.b2.configure(command=self.dfiltre,state='normal')
        S = Scrollbar(self)
        X = Scrollbar(self,orient=HORIZONTAL)
        S.pack(side=RIGHT)
        X.pack(side=BOTTOM)
        self.T = Text(self, height=7,wrap=None,yscrollcommand=S.set, xscrollcommand=X.set)
        self.T.pack()
        self.naam='dicom'
        self.codeb4=Button(self, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=100)
        self.codeb4.pack()
        S.config(command=self.T.yview)
        X.config(command=self.T.xview)
        quote = str(im)
        self.T.insert(END, quote)
        w,h=self.image_new.size
        self.image_new=self.image_new.resize((int(w/2),int(h/2)))
        
    def code(self):
        gamma=Toplevel(self)
        S = Scrollbar(gamma)
        X = Scrollbar(gamma,orient=HORIZONTAL)
        S.pack(side=RIGHT)
        X.pack(side=BOTTOM)
        naam={'root':'rotate an image','nose':'add noise to image','hello':'get colored image','fil':'add filter to image','dicom':'reading a dicom file','image':'reading an image'}
        c1='\t\tCode for:'+naam[self.naam]+'\n\nPYTHON\nImage.rotate(angle)\n\nMATLAB\nimrotate(image,angle)'
        xo='\n\nMATLAB\noutput = imnoise(image,mode,*args)\n\tFor more information https://www.mathworks.com/help/images/ref/imnoise.html'
        c2='\t\tCode for:'+naam[self.naam]+'\n\nPYTHON\nmode=gaussian/speckle\n\toutput=random_noise(photo,mode=mode, mean=m,var=v, clip=True)\n\nmode=salt/pepper/saltnpepper\n\toutput=random_noise(photo,mode=mode, amount=a, clip=True)\n\nmode=localvar/poisson\n\toutput=random_noise(photo,mode=mode, clip=True)'+xo
        c3='\t\tCode for:'+naam[self.naam]+'\n\nPYTHON\n1)\tUsing OpenCV\n\tb,g,r=cv2.split(image)\n\tplt.imshow(r);plt.imshow(g);plt.imshow(b)\n2)\tSetting undesired image color to zero\n\timage[:,:,i]=0\tred=0; green=1; blue=2\n\nMATLAB\nDisplay only the required image\nimshow(image(:,:,i)); red=1; green=2; blue=3'
        xox='\n\nMATLAB\noutput = imfilter(image,kernel,*args)\n\tFor more information https://www.mathworks.com/help/images/ref/imfilter.html'
        c4='\t\tCode for:'+naam[self.naam]+'\n\nPYTHON\noutput=cv2.bilateralFilter(image, sigmaColor, sigmaSpace)\noutput=cv2.blur(image, ksize)\noutput=cv2.GaussianBlur(image, ksize, sigmaX)\noutput=cv2.Laplacian(image, ddepth)\noutput=cv2.medianBlur(image, ksize)\noutput=cv2.Sobel(image, ddepth, dx, dy)'+xox
        c5='\t\tCode for:'+naam[self.naam]+'\n\nPYTHON\nimport pydicom\nfile=pydicom.dcmread(file_path)\nimage=file.pixel_array()\n\nMATLAB\nfile=dicominfo(file_path)\nimage=dicomread(file)'
        c6='\t\tCode for:'+naam[self.naam]+'\n\nPYTHON\n1)\timage=PIL.Image.open(file_path)\n2)\timage=cv2.imread(file_path)\n\nMATLAB\nimage=imread(file_path)'
        fun={'root':c1,'nose':c2,'hello':c3,'fil':c4,'dicom':c5,'image':c6}
        T = Text(gamma, height=15,wrap=None,yscrollcommand=S.set, xscrollcommand=X.set)
        T.pack()
        S.config(command=T.yview)
        X.config(command=T.xview)
        quote = str(fun[self.naam])
        T.insert(END, quote)
        gamma.title("CODE")
    
    def drotate(self):
        def rot():
            self.root.title("angle:"+str(sp.get()))
            imi=self.image_new.copy()
            imi = imi.rotate(int(sp.get()))
            self.rot_im=imi
            r0t = ImageTk.PhotoImage(imi)
            label_rot.configure(image=r0t)
            label_rot.image = r0t
            self.to_save=imi
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        self.root=Toplevel(self)
        self.text=Label(self.root,wraplength=450,text='enter degree of rotation:')
        self.text.pack()
        sp = Spinbox(self.root, from_= 0, to = 360)
        sp.pack()
        self.naam='root'
        b4=Button(self.root, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b4.pack()
        b3=Button(self.root, text='enter', command=rot).pack()
        self.b4.configure(state='normal')
        render=ImageTk.PhotoImage(self.image_new)
        label_rot = Label(self.root,image=render)
        label_rot.image=render
        label_rot.pack()
        
    
    def dnoise(self):
        #def rota():
        #    self.joke=self.rot_im.copy()
        #    render=ImageTk.PhotoImage(self.joke)
        #    label_no.configure(image=render)
        #    label_no.image=render
        #def normal():
        #    self.joke=self.image_new.copy()
        #   render=ImageTk.PhotoImage(self.joke)
        #    label_no.configure(image=render)
        #    label_no.image=render
        def nina():
            self.joke=self.to_save.copy()
            render=ImageTk.PhotoImage(self.joke)
            label_no.configure(image=render)
            label_no.image=render
        def no_amount():
            global amount
            try:
                tex_l.pack()
                key.pack()
            except:
                True
            tex_l.configure(text='choose proportion to be replaced')
            amount=Spinbox(self.nose,text='proportion to be replaced',format="%.2f",increment=0.01, from_=0,to=1)
            amount.pack()
            key.configure(text='enter', command=nono)
        def no_MnV():
            global mean,var
            try:
                tex_l.pack()
                key.pack()
            except:
                True
            tex_l.configure(text='choose mean and variance respectively')
            mean=Spinbox(self.nose,format="%.1f",increment=0.1,from_=0.1,to=10)
            mean.pack()
            var=Spinbox(self.nose,format="%.2f",increment=0.01, from_=0,to=1)
            var.pack()
            key.configure(text='enter', command=nono)
        def nono():
            tex_l.pack_forget()
            key.pack_forget()
            imi=self.joke
            imag=np.asarray(imi)
            photo=imag.copy()
            mode=v1.get()
            if ((mode=='s&p') or (mode=='salt') or (mode=='pepper')):
                a=amount.get()
                sp=random_noise(photo,mode=mode, amount=np.float(a), clip=True)
            
            elif ((mode=='gaussian')or(mode=='speckle')):
                m=np.float(mean.get())
                v=np.float(var.get())
                sp=random_noise(photo,mode=mode, mean=m,var=v, clip=True)
            else:
                sp=random_noise(photo,mode=mode, clip=True)
            data=sp
            data = data / data.max() #normalizes data in range 0 - 255
            data = 255 * data
            sp = data.astype(np.uint8)
            imi=Image.fromarray(sp)
            self.to_save=imi
            b3.configure(state='normal')
            self.b4.configure(state='normal')
            render=ImageTk.PhotoImage(imi)
            label_no.configure(image=render)
            label_no.image = render # keep a reference!
            try:
                amount.destroy()
            except:
                True
            try:
                mean.destroy()
                var.destroy()
            except:
                True
        self.nose=Toplevel(self)
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        self.nose.title("noisy image")
        v1=StringVar()
        #b1=Button(self.nose, text='add noise to rotated image', command=rota).pack()
        #b2=Button(self.nose, text='add noise to original image', command=normal).pack()
        b3=Button(self.nose, text='add noise to noisy image', command=nina, state='disabled')
        b3.pack()
        n1=Checkbutton(self.nose, text='s&p',command=no_amount, variable=v1,onvalue = 's&p', offvalue = 0).pack()
        n2=Checkbutton(self.nose,text='salt',command=no_amount, variable=v1,onvalue = 'salt', offvalue = 0).pack()
        n3=Checkbutton(self.nose,text='pepper',command=no_amount, variable=v1,onvalue = 'pepper', offvalue = 0).pack()
        n4=Checkbutton(self.nose, text='localvar',command=nono, variable=v1,onvalue = 'localvar', offvalue = 0).pack()
        n5=Checkbutton(self.nose,text='gaussian',command=no_MnV, variable=v1,onvalue = 'gaussian', offvalue = 0).pack()
        n6=Checkbutton(self.nose,text='poisson',command=nono, variable=v1,onvalue = 'poisson', offvalue = 0).pack()
        n7=Checkbutton(self.nose,text='speckle',command=no_MnV, variable=v1,onvalue = 'speckle', offvalue = 0).pack()
        b=Button(self.nose, text='filter this image', command=self.filtre).pack()
        bfi=Button(self.nose, text='Save_jpg', command=self.save).pack()
        render=ImageTk.PhotoImage(self.image_new)
        label_no=Label(self.nose,image=render)
        label_no.image=render
        label_no.pack()
        self.naam='nose'
        b4=Button(self.nose, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b4.pack()
        self.joke=self.image_new.copy()
        tex_l=Label(self.nose,text='hello')
        tex_l.pack()
        key=Button(self.nose, text="I'll work later")
        key.pack()
        
        
    def rotate(self):
        def rot():
            self.root.title("angle:"+str(sp.get()))
            imi=self.image_new.copy()
            imi = imi.rotate(int(sp.get()))
            r0t = ImageTk.PhotoImage(imi)
            label_rot.configure(image=r0t)
            label_rot.image = r0t
            self.to_save=imi
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        self.root=Toplevel(self)
        self.root.title("rotate image")
        self.text=Label(self.root,wraplength=450,text='enter degree of rotation:')
        self.text.pack()
        sp = Spinbox(self.root, from_= 0, to = 360)
        sp.pack()
        self.naam='root'
        b4=Button(self.root, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b4.pack()
        self.b4.configure(state='normal')
        label_rot = Label(self.root,image=self.render)
        label_rot.pack()
        b3=Button(self.root, text='enter', command=rot).pack()
    
    def color(self):
        def pri():
            imi=self.image_new.copy()
            imag=np.asarray(imi)
            photo=imag.copy()
            num=v1.get()
            for i in range(3):
                if i!=num:
                    photo[:,:,i]=0
            imi=Image.fromarray(photo)
            self.to_save=imi
            render=ImageTk.PhotoImage(imi)
            label_col.configure(image=render)
            label_col.image = render # keep a reference!
        self.hello=Toplevel(self)
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        v1=IntVar()
        self.hello.title("Color Image")
        self.b4.configure(state='normal')
        self.naam='hello'
        b1=Checkbutton(self.hello, text='green',command=pri, variable=v1,onvalue = 1, offvalue = 0).pack()
        b2=Checkbutton(self.hello,text='blue',command=pri, variable=v1,onvalue = 2, offvalue = 0).pack()
        b3=Checkbutton(self.hello,text='red',command=pri, variable=v1,onvalue = 0, offvalue = 0).pack()
        label_col=Label(self.hello,image=self.render)
        label_col.pack()
        b4=Button(self.hello, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b4.pack()
        
    def noise(self):
        #def normal():
        #    self.joke=self.image_new.copy()
        #    render=ImageTk.PhotoImage(self.joke)
        #    label_no.configure(image=render)
        #    label_no.image=render
        def nina():
            self.joke=self.to_save.copy()
            render=ImageTk.PhotoImage(self.joke)
            label_no.configure(image=render)
            label_no.image=render
        def no_amount():
            global amount
            try:
                tex_l.pack()
                key.pack()
            except:
                True
            tex_l.configure(text='density')
            amount=Spinbox(self.nose,text='density',format="%.2f",increment=0.01, from_=0,to=1)
            amount.pack()
            key.configure(text='enter', command=nono)
        def no_MnV():
            global mean,var
            try:
                tex_l.pack()
                key.pack()
            except:
                True
            tex_l.configure(text='choose mean and variance respectively')
            mean=Spinbox(self.nose,format="%.1f",increment=0.1,from_=0.1,to=10)
            mean.pack()
            var=Spinbox(self.nose,format="%.2f",increment=0.01, from_=0,to=1)
            var.pack()
            key.configure(text='enter', command=nono)
        def nono():
            tex_l.pack_forget()
            key.pack_forget()
            imi=self.joke.copy()
            imag=np.asarray(imi)
            photo=imag.copy()
            mode=v1.get()
            if ((mode=='s&p') or (mode=='salt') or (mode=='pepper')):
                a=amount.get()
                sp=random_noise(photo,mode=mode, amount=np.float(a), clip=True)
            
            elif ((mode=='gaussian')or(mode=='speckle')):
                m=np.float(mean.get())
                v=np.float(var.get())
                sp=random_noise(photo,mode=mode, mean=m,var=v, clip=True)
            else:
                sp=random_noise(photo,mode=mode, clip=True)
            data=sp
            data = data / data.max() #normalizes data in range 0 - 255
            data = 255 * data
            sp = data.astype(np.uint8)
            imi=Image.fromarray(sp)
            self.to_save=imi
            b3.configure(state='normal')
            render=ImageTk.PhotoImage(imi)
            label_no.configure(image=render)
            label_no.image = render # keep a reference!
            try:
                amount.destroy()
            except:
                True
            try:
                mean.destroy()
                var.destroy()
            except:
                True
        self.nose=Toplevel(self)
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.fil.destroy()
        except:
            True
        self.nose.title("noisy image")
        v1=StringVar()
        self.b4.configure(state='normal')
        #b2=Button(self.nose, text='add noise to original image', command=normal).pack()
        b3=Button(self.nose, text='add noise to noisy image', command=nina, state='disabled')
        b3.pack()
        self.naam='nose'
        n1=Checkbutton(self.nose, text='s&p',command=no_amount, variable=v1,onvalue = 's&p', offvalue = 0).pack()
        n2=Checkbutton(self.nose,text='salt',command=no_amount, variable=v1,onvalue = 'salt', offvalue = 0).pack()
        n3=Checkbutton(self.nose,text='pepper',command=no_amount, variable=v1,onvalue = 'pepper', offvalue = 0).pack()
        n4=Checkbutton(self.nose, text='localvar',command=nono, variable=v1,onvalue = 'localvar', offvalue = 0).pack()
        n5=Checkbutton(self.nose,text='gaussian',command=no_MnV, variable=v1,onvalue = 'gaussian', offvalue = 0).pack()
        n6=Checkbutton(self.nose,text='poisson',command=nono, variable=v1,onvalue = 'poisson', offvalue = 0).pack()
        n7=Checkbutton(self.nose,text='speckle',command=no_MnV, variable=v1,onvalue = 'speckle', offvalue = 0).pack()
        b=Button(self.nose, text='filter this image', command=self.filtre).pack()
        label_no=Label(self.nose,image=self.render)
        label_no.image=self.render
        label_no.pack()
        self.joke=self.image_new.copy()
        tex_l=Label(self.nose,text='hello')
        tex_l.pack()
        b4=Button(self.nose, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b4.pack()
        key=Button(self.nose, text="I'll work later")
        key.pack()
    
    def filtre(self):
        def fil_imi():
            self.x=self.to_save_f.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def normal():
            f1.configure(state=NORMAL)
            f2.configure(state=NORMAL)
            f3.configure(state=NORMAL)
            f4.configure(state=NORMAL)
            f5.configure(state=NORMAL)
            f6.configure(state=NORMAL)
            self.x=self.image_new.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def noisy_im():
            f1.configure(state=NORMAL)
            f2.configure(state=NORMAL)
            f3.configure(state=NORMAL)
            f4.configure(state=NORMAL)
            f5.configure(state=NORMAL)
            f6.configure(state=NORMAL)
            self.x=self.to_save.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def filtering():
                b4.configure(state='normal')
                filt=str(v1.get())
                if filt=='gaus':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='choose: size of kernel and sigma')
                    self.sp=Spinbox(self.fil,from_=0,to=10)
                    self.sp.pack()
                    self.sigma=Spinbox(self.fil,format="%.1f",increment=0.1,from_=0,to=10)
                    self.sigma.pack()
                    key.configure(text='filtre',command=gaussian)
                elif filt=='avg':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='kernel size:')
                    self.sp=Spinbox(self.fil,from_=0,to=100)
                    self.sp.pack()
                    key.configure(text='filtre',command=average)
                elif filt=='med':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='')
                    key.configure(text='filtre',command=median)
                elif filt=='bil':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='choose: diameter,sigmaColor and sigmaSpace')
                    self.sp=Spinbox(self.fil,from_=0,to=10)
                    self.sp.pack()
                    self.sigma=Spinbox(self.fil,from_=10,to=150)
                    self.sigma.pack()
                    self.sigma1=Spinbox(self.fil,from_=10,to=150)
                    self.sigma1.pack()
                    key.configure(text='filtre',command=bilateral)
                elif filt=='lap':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='')
                    key.configure(text='filtre',command=laplacian)
                elif filt=='sob':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='choose axis:')
                    self.r1=Radiobutton(self.fil, text='x-axis', variable=self.c, value='x')
                    self.r2=Radiobutton(self.fil, text='y-axis', variable=self.c, value='y')
                    self.r1.pack()
                    self.r2.pack()
                    key.configure(text='filtre',command=sobel)
                else:
                    False
        
        def  gaussian():
            tex_l.pack_forget()
            key.pack_forget()
            size=int(self.sp.get())
            sigma=np.float(self.sigma.get())
            self.sp.destroy()
            self.sigma.destroy()
            size=(size,size)
            m,n = [(ss-1.)/2. for ss in size]
            y,x = np.ogrid[-m:m+1,-n:n+1]
            h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
            h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
            sumh = h.sum()
            if sumh != 0:
                h /= sumh
            a=cv2.split(self.x)
            n=len(a)
            if n>2:
                for i,ini in enumerate(a): 
                    a[i]=corr(ini, h, mode='nearest')
                imi=cv2.merge([a[0],a[1],a[2]])
            elif n==1:
                a[0]=corr(a[0], h, mode='nearest')
                imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def average():
            tex_l.pack_forget()
            key.pack_forget()
            size=int(self.sp.get())
            self.sp.destroy()
            h=np.ones((size,size))
            h[:,:]=1/(size*size)
            a=cv2.split(self.x)
            n=len(a)
            if n>2:
                for i,ini in enumerate(a): 
                    a[i]=corr(ini, h, mode='nearest')
                imi=cv2.merge([a[0],a[1],a[2]])
            elif n==1:
                a[0]=corr(a[0], h, mode='nearest')
                imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def median():
            tex_l.pack_forget()
            key.pack_forget()
            median_im=Image.fromarray((self.x*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(size = 3))
            self.to_save_f=median_im
            render=ImageTk.PhotoImage(median_im)
            label_new.configure(image=render)
            label_new.image=render
        def bilateral():
            tex_l.pack_forget()
            key.pack_forget()
            size=int(self.sp.get())
            self.sp.destroy()
            sigma=int(self.sigma.get())
            sigma2=int(self.sigma1.get())
            self.sigma.destroy()
            self.sigma1.destroy()
            im_bil1=cv2.bilateralFilter(self.x,size,sigma,sigma2)
            imi=Image.fromarray(im_bil1)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def laplacian():
            tex_l.pack_forget()
            key.pack_forget()
            a=cv2.split(self.x)
            n=len(a)
            if n>2:
                for i,ini in enumerate(a): 
                    a[i]=cv2.Laplacian(ini,cv2.CV_16S,3)
                    a[i] =cv2.convertScaleAbs(a[i])
                imi=cv2.merge([a[0],a[1],a[2]])
            elif n==1:
                a[0]=cv2.Laplacian(a[0],cv2.CV_16S,3)
                a[0] =cv2.convertScaleAbs(a[0])
                imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def sobel():
            tex_l.pack_forget()
            key.pack_forget()
            a=cv2.split(self.x)
            axis=self.c.get()
            self.r1.pack_forget()
            self.r2.pack_forget()
            if axis=='x':
                x=1
                y=0
            else:
                x=0
                y=1
            n=len(a)
            if n>2:
                for i,ini in enumerate(a): 
                    a[i] = cv2.Sobel(ini,cv2.CV_16S,x,y,ksize=-1)
                    a[i] =cv2.convertScaleAbs(a[i])
                imi=cv2.merge([a[0],a[1],a[2]])
            elif n==1:
                a[0] = cv2.Sobel(a[0],cv2.CV_16S,x,y,ksize=-1)
                a[0] =cv2.convertScaleAbs(a[0])
                imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
            
        self.fil=Toplevel(self)
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        self.fil.title("filter")
        v1=StringVar()
        noise=True
        self.c=StringVar()
        n1=Checkbutton(self.fil, text='add noise to image',command=self.noise, variable=v1,onvalue = 'yes', offvalue = 0).pack()
        b2=Button(self.fil, text='filter original image', command=normal).pack()
        b3=Button(self.fil, text='filter noisy image', command=noisy_im).pack()
        b4=Button(self.fil, text='add filter to this image', command=fil_imi, state='disabled')
        b4.pack()
        label_fil=Label(self.fil,image=None)
        label_fil.pack()
        self.naam='fil'
        f1=Checkbutton(self.fil, text='gaussian kernel',command=filtering, variable=v1, onvalue='gaus', offvalue=0, state=DISABLED)
        f1.pack()
        f2=Checkbutton(self.fil, text='average kernel',command=filtering, variable=v1, onvalue='avg', offvalue=0,state=DISABLED)
        f2.pack()
        f3=Checkbutton(self.fil, text='median kernel',command=filtering, variable=v1, onvalue='med', offvalue=0,state=DISABLED)
        f3.pack()
        f4=Checkbutton(self.fil, text='bilateral kernel',command=filtering, variable=v1, onvalue='bil', offvalue=0,state=DISABLED)
        f4.pack()
        f5=Checkbutton(self.fil, text='laplacian kernel',command=filtering, variable=v1, onvalue='lap', offvalue=0,state=DISABLED)
        f5.pack()
        f6=Checkbutton(self.fil, text='sobel kernel',command=filtering, variable=v1, onvalue='sob', offvalue=0,state=DISABLED)
        f6.pack()
        tex_l=Label(self.fil,text='hello')
        tex_l.pack()
        b1=Button(self.fil, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b1.pack()
        self.b4.configure(state='normal')
        key=Button(self.fil, text="I'll work later")
        key.pack()
        label_new=Label(self.fil,image=None)
        label_new.pack()
        bfi=Button(self.fil, text='Save', command=self.save_f)
        bfi.pack()

    def dfiltre(self):
        def fil_imi():
            self.x=self.to_save_f.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def rota():
            f1.configure(state=NORMAL)
            f2.configure(state=NORMAL)
            f3.configure(state=NORMAL)
            f4.configure(state=NORMAL)
            f5.configure(state=NORMAL)
            f6.configure(state=NORMAL)
            self.x=self.rot_im.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def normal():
            f1.configure(state=NORMAL)
            f2.configure(state=NORMAL)
            f3.configure(state=NORMAL)
            f4.configure(state=NORMAL)
            f5.configure(state=NORMAL)
            f6.configure(state=NORMAL)
            self.x=self.image_new.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def noisy_im():
            f1.configure(state=NORMAL)
            f2.configure(state=NORMAL)
            f3.configure(state=NORMAL)
            f4.configure(state=NORMAL)
            f5.configure(state=NORMAL)
            f6.configure(state=NORMAL)
            self.x=self.to_save.copy()
            render=ImageTk.PhotoImage(self.x)
            label_fil.configure(image=render)
            label_fil.image=render
            self.x=np.asarray(self.x)
        def filtering():
                b4.configure(state='normal')
                filt=str(v1.get())
                if filt=='gaus':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='choose: size of kernel and sigma')
                    self.sp=Spinbox(self.fil,from_=1,to=10)
                    self.sp.pack()
                    self.sigma=Spinbox(self.fil,format="%.1f",increment=0.1,from_=0,to=10)
                    self.sigma.pack()
                    key.configure(text='filtre',command=gaussian)
                elif filt=='avg':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='kernel size:')
                    self.sp=Spinbox(self.fil,from_=0,to=100)
                    self.sp.pack()
                    key.configure(text='filtre',command=average)
                elif filt=='med':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='')
                    key.configure(text='filtre',command=median)
                elif filt=='bil':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='choose: diameter,sigmaColor and sigmaSpace')
                    self.sp=Spinbox(self.fil,from_=0,to=10)
                    self.sp.pack()
                    self.sigma=Spinbox(self.fil,from_=10,to=150)
                    self.sigma.pack()
                    self.sigma1=Spinbox(self.fil,from_=10,to=150)
                    self.sigma1.pack()
                    key.configure(text='filtre',command=bilateral)
                elif filt=='lap':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='')
                    key.configure(text='filtre',command=laplacian)
                elif filt=='sob':
                    try:
                        tex_l.pack()
                        key.pack()
                    except:
                        True
                    tex_l.configure(text='choose axis:')
                    self.r1=Radiobutton(self.fil, text='x-axis', variable=self.c, value='x')
                    self.r2=Radiobutton(self.fil, text='y-axis', variable=self.c, value='y')
                    self.r1.pack()
                    self.r2.pack()
                    key.configure(text='filtre',command=sobel)
                else:
                    False
        
        def  gaussian():
            tex_l.pack_forget()
            key.pack_forget()
            size=int(self.sp.get())
            sigma=np.float(self.sigma.get())
            self.sp.destroy()
            self.sigma.destroy()
            size=(size,size)
            m,n = [(ss-1.)/2. for ss in size]
            y,x = np.ogrid[-m:m+1,-n:n+1]
            h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
            h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
            sumh = h.sum()
            if sumh != 0:
                h /= sumh
            a=cv2.split(self.x)
            a[0]=corr(a[0], h, mode='nearest')
            imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def average():
            tex_l.pack_forget()
            key.pack_forget()
            size=int(self.sp.get())
            self.sp.destroy()
            h=np.ones((size,size))
            h[:,:]=1/(size*size)
            a=cv2.split(self.x)
            a[0]=corr(a[0], h, mode='nearest')
            imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def median():
            tex_l.pack_forget()
            key.pack_forget()
            self.r1.pack_forget()
            self.r2.pack_forget()
            median_im=Image.fromarray((self.x*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(size = 3))
            self.to_save_f=median_im
            render=ImageTk.PhotoImage(median_im)
            label_new.configure(image=render)
            label_new.image=render
        def bilateral():
            tex_l.pack_forget()
            key.pack_forget()
            size=int(self.sp.get())
            self.sp.destroy()
            sigma=int(self.sigma.get())
            sigma2=int(self.sigma1.get())
            self.sigma.destroy()
            self.sigma1.destroy()
            im_bil1=cv2.bilateralFilter(self.x,size,sigma,sigma2)
            imi=Image.fromarray(im_bil1)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def laplacian():
            tex_l.pack_forget()
            key.pack_forget()
            a=cv2.split(self.x) 
            a[0]=cv2.Laplacian(a[0],cv2.CV_16S,3)
            a[0] =cv2.convertScaleAbs(a[0])
            imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
        def sobel():
            tex_l.pack_forget()
            key.pack_forget()
            a=cv2.split(self.x)
            axis=self.c.get()
            self.r1.pack_forget()
            self.r2.pack_forget()
            if axis=='x':
                x=1
                y=0
            else:
                x=0
                y=1
            a[0] = cv2.Sobel(a[0],cv2.CV_16S,x,y,ksize=-1)
            a[0] =cv2.convertScaleAbs(a[0])
            imi=a[0]
            imi=Image.fromarray(imi)
            self.to_save_f=imi
            render=ImageTk.PhotoImage(imi)
            label_new.configure(image=render)
            label_new.image=render
            
        self.fil=Toplevel(self)
        try:
            self.text.pack_forget()
        except:
            True
        try:
            self.root.destroy()
        except:
            True
        try:
            self.comp.destroy()
        except:
            True
        try:
            self.hello.destroy()
        except:
            True
        try:
            self.nose.destroy()
        except:
            True
        self.fil.title("filter")
        v1=StringVar()
        noise=True
        self.c=StringVar()
        self.b4.configure(state='normal')
        n1=Checkbutton(self.fil, text='add noise to image',command=self.noise, variable=v1,onvalue = 'yes', offvalue = 0).pack()
        b1=Button(self.fil, text='filter rotated image', command=rota).pack()
        b2=Button(self.fil, text='filter original image', command=normal).pack()
        b3=Button(self.fil, text='filter noisy image', command=noisy_im).pack()
        b4=Button(self.fil, text='add filter to this image', command=fil_imi, state='disabled')
        b4.pack()
        label_fil=Label(self.fil,image=None)
        label_fil.pack()
        self.naam='fil'
        f1=Checkbutton(self.fil, text='gaussian kernel',command=filtering, variable=v1, onvalue='gaus', offvalue=0, state=DISABLED)
        f1.pack()
        f2=Checkbutton(self.fil, text='average kernel',command=filtering, variable=v1, onvalue='avg', offvalue=0, state=DISABLED)
        f2.pack()
        f3=Checkbutton(self.fil, text='median kernel',command=filtering, variable=v1, onvalue='med', offvalue=0, state=DISABLED)
        f3.pack()
        f4=Checkbutton(self.fil, text='bilateral kernel',command=filtering, variable=v1, onvalue='bil', offvalue=0, state=DISABLED)
        f4.pack()
        f5=Checkbutton(self.fil, text='laplacian kernel',command=filtering, variable=v1, onvalue='lap', offvalue=0,state=DISABLED)
        f5.pack()
        f6=Checkbutton(self.fil, text='sobel kernel',command=filtering, variable=v1, onvalue='sob', offvalue=0, state=DISABLED)
        f6.pack()
        tex_l=Label(self.fil,text='hello')
        tex_l.pack()
        key=Button(self.fil, text="I'll work later")
        key.pack()
        label_new=Label(self.fil,image=None)
        label_new.pack()
        bfi=Button(self.fil, text='Save_jpg', command=self.save_f)
        bfi.pack()
        bf=Button(self.fil,text='Save as dcm', command=self.save_dicom_f).pack()
        b5=Button(self.fil, text='code',command=self.code, highlightbackground ='red',fg='green',highlightthickness=10,height=2,width=20)
        b5.pack()
        
window=tk.Tk()
try:
    p1 = PhotoImage(file = 'logo_IPT.png') 
    window.iconphoto(False, p1) 
except:
    True
mywin=MyWindow(window)
mywin.pack(side="top", fill="both", expand=True)
window.title('Image Processing tutor')
window.geometry("450x700+10+10")
window.mainloop()


# In[ ]:





# In[ ]:




