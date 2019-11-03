def quit(*args):
       root.destroy()
             

def clock_time():
       time=datetime.datetime.now()
       time=(time.strftime("%H:%M:%S"))#for hours,min and sec.

       txt.set(time)

       root.after(1000,clock_time)

root=Tk()
root.title("clock")
canvas=Canvas(root,width=500,height=200)
canvas.pack()
my_image=PhotoImage(file='C:\\Users\\TABISH AJAZ\\Desktop\\animatrix-gif-5.gif')

canvas.create_image(0,0, anchor=NW, image=my_image)

root.attributes("-fullscreen",False)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, clock_time)
fnt=font.Font(family='Halventica', size=60, weight='bold')
txt=StringVar()
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="black")
#lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.2,rely=0.2,anchor=NW)
#lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
