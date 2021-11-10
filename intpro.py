#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
from tkinter import *
from tkinter import messagebox


# In[2]:


root = Tk()
root.title("Hospital Appointment")

def emergency_click():
    myLabel=Label(root, fg="red",text=("Emergency Services Selected"))
    myLabel.grid(columnspan=3, padx=10, pady=10 , )
    
                   
    myLabel1 = Label(root, text="Current Temperature:")
    myLabel1.grid() 
                   
    enter_temp = Entry(root, width= 35 , borderwidth=5)
    enter_temp.grid(row=2,column=1, columnspan=3, padx=10, pady=10)
    
    def pop_button():
        response=messagebox.askquestion("Emergancy Services","Is your temp. greater than 37 (degree Celsius) ?")
        
        if response=="yes":
            Label(root,text="You will be shifted to isolation ward fearing covid.",fg="red").grid()
            messagebox.showinfo("Emergancy Services","you will be shifted to isolated ward due to Covid-19")
        else:
            Label(root,text="You will be taken to normal ward.",fg="green").grid()
        
    
    pop_button=Button(root, text="Save Temp.", command=pop_button,fg="Yellow",bg="Black")
    pop_button.grid(column=1)
    
    def submit_button():
        messagebox.showinfo("Emergancy Services","Your appointment is booked successfully." )
        root.destroy()
    
    pop_button=Button(root, text="Save Info", command=submit_button,fg="white",bg="Black",padx=10, pady=10)
    pop_button.grid(column=0)
    

    
def regular_click():
    myLabel=Label(root,fg="red", text=("You have requested for Regular Services"))
    myLabel.grid(columnspan=3, padx=10, pady=10)
    
    myLabel2 = Label(root, text="Whether you live in containment zone?")
    myLabel2.grid() 
    
    
                   
    enter_place = Entry(root, width= 35 , borderwidth=5)
    enter_place.grid(row=2,column=1, columnspan=3, padx=10, pady=10)
    
    def pop1_button():
        response=messagebox.askquestion("Regular Services","Do you live in containment zone?")
        
        if response=="yes":
            Label(root,text="Sorry! you can't come for a Medical chackup.",fg="red").grid()
            messagebox.showinfo("Regular Services","your appointment can't be booked. Sorry!")
            root.destroy()
        else:
            Label(root,text="you can come for medical checkup.",fg="green").grid()
        
    
    pop1_button=Button(root, text="Save zone", command=pop1_button,fg="Yellow",bg="Black")
    pop1_button.grid(row=3,column=1)
    
    myLabel3 = Label(root, text="Any recent travel history:")
    myLabel3.grid() 
    
    
                   
    enter_place = Entry(root, width= 35 , borderwidth=5)
    enter_place.grid(row=4,column=1, columnspan=3, padx=10, pady=10)
    
    def pop2_button():
        response=messagebox.askquestion("Regular Services","Any recent travel history?")
        
        if response=="yes":
            Label(root,text="Sorry! you can't come for a Medical checkup.",fg="red").grid()
            messagebox.showinfo("Regular Services","your appointment can't be booked. Sorry!")
            root.destroy()
        else:
            Label(root,text="you can come for medical checkup.",fg="green").grid()
            
    pop2_button=Button(root, text="Save Data", command=pop2_button,fg="Yellow",bg="Black")
    pop2_button.grid(row=5,column=1)
    
    
    myLabel4 = Label(root, text="Your Body Temperature:")
    myLabel4.grid() 
    
    
                   
    enter_place = Entry(root, width= 35 , borderwidth=5)
    enter_place.grid(row=6,column=1, columnspan=3, padx=10, pady=10)
    
    def pop3_button():
        response=messagebox.askquestion("Regular Services","Is your temp.greater than 37?")
        
        if response=="yes":
            Label(root,text="Sorry! you can't come for medical checkup",fg="red").grid()
            messagebox.showinfo("Regular Services","your appointment can't be booked. Sorry!")
            root.destroy()
        else:
            Label(root,text="you can come for medical checkup.",fg="green").grid()
            
    pop3_button=Button(root, text="Save Temp.", command=pop3_button,fg="Yellow",bg="Black")
    pop3_button.grid(row=7,column=1)
    
    def submit_button():
        messagebox.showinfo("Regular Services","Your appointment  booked successfully of Tomorrow!" )
        root.destroy()
            
       
    pop_button=Button(root, text="Save Info", command=submit_button,fg="white",bg="Black",padx=10, pady=10)
    pop_button.grid(row=8,column=0)


emergencyButton=Button(root, text ="Emergency" ,font=18, padx=50,pady=20 ,bd=4 ,fg="black",bg="white" ,command=emergency_click)
emergencyButton.grid(row=0 ,column=0)

regularButton=Button(root, text ="Scheduled",font=18,padx=50,pady=20 , bd=4 ,fg="black",bg="white" ,command=regular_click)
regularButton.grid(row=0 , column=1)




root.mainloop()


# In[ ]:




