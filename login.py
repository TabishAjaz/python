import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("GUI")
window.geometry()
#creating Label:
name_label=ttk.Label(window,text="Enter your name  :",foreground='blue')
name_label.grid(row=0,column=0,sticky=tk.W)
emial_label=ttk.Label(window,text="Email Id:",foreground="red")
emial_label.grid(row=1,column=0,sticky=tk.W)
age_label=ttk.Label(window ,text="Enter your age :",foreground="green")

age_label.grid(row=2,column=0,sticky=tk.W)
gender_label=ttk.Label(window,text="Gender")
gender_label.grid(row=3,column=0)
#creating variables:
name_var=tk.StringVar()  #variables to store data in entry box
email_var=tk.StringVar()
age_var=tk.IntVar()
gender_var=tk.StringVar()
#creating entry box:
name_entry=ttk.Entry(window,width=16,textvariable=name_var)
name_entry.grid(row=0,column=1)
name_entry.focus()#for cursor pointing to the box
email_entry=ttk.Entry(window,width=16,textvariable=email_var)
email_entry.grid(row=1,column=1)
age_entry=ttk.Entry(window,width=16,textvariable=age_var)
age_entry.grid(row=2,column=1)
#creating combo box:
gender_combobox=ttk.Combobox(window,width=14,textvariable=gender_var,state="readonly")#state=so no one can write.
gender_combobox['values']=("Male","Female","others")
gender_combobox.current(0)#for filling default
gender_combobox.grid(row=3,column=1)

#creating radiobutton:
user_type=tk.StringVar()#variable
student_rdbtn=tk.Radiobutton(window,value="student",text="student",variable=user_type,background="red")
student_rdbtn.grid(row=4,column=0)
teacher_rdbtn=tk.Radiobutton(window,value="teacher",text="teacher",variable=user_type,background="green")
teacher_rdbtn.grid(row=4,column=1)

#creating check button:
chk_var=tk.IntVar()
chk_button=ttk.Checkbutton(window,text="agree all terms and conditions ",variable=chk_var)
chk_button.grid(row=6,columnspan=3)
#creating button
def action():
    user_name=name_var.get()
    user_email=email_var.get()
    user_age=age_var.get()
    user_gender=gender_var.get()
    usertype=user_type.get()
    if chk_var.get()==0:
        subscribed="NO"
    else:
        subscribed="Yes"
    print(f'{user_name} is {user_age} years old ,having email_id {user_email}\n')
    print(user_gender,usertype,subscribed)
    with open('file.txt','a') as f:
        f.write(f'{user_name},{user_age},{user_email},{user_gender},{usertype},{subscribed}\n')
    name_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)

submit_button=tk.Button(window,text="submit",command=action)
submit_button.grid(row=5,column=0)
window.mainloop()
