from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for i in range(nr_letters)]
    password_symbols=[random.choice(symbols) for k in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for j in range(nr_numbers)]
    password_list=password_numbers+password_symbols+password_letters

    random.shuffle(password_list)
    passwrd="".join(password_list)
    password.insert(0,passwrd)
    pyperclip.copy(passwrd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def savingtofile():
    webname.focus()
    wbname = webname.get().strip()
    ename = emailname.get().strip()
    pass1 = password.get().strip()
    if len(wbname)==0 :
        messagebox.showwarning(title="oops",message="Please do not leave any of the fields empty")
        webname.focus()
    elif len(pass1)==0:
        messagebox.showwarning(title="oops", message="Please do not leave any of the fields empty")
        password.focus()
    else:
        isok= messagebox.askokcancel(title=wbname,message=f"Is the password entered {pass1} correct.\n "
                                                          f"Is it okay to save it")
        if isok:
            with open("data.txt","a") as file:
                file.write(f"{wbname}|{ename}|{pass1}\n")
            webname.delete(0,END)
            password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
# window creation
window= Tk()
window.title("Password Manager")
window.config(pady=20,padx=20,)
image=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200,)
canvas.create_image(100,100,image=image,)
canvas.grid(row=0,column=1)

# website  name capture
label1=Label(text="Website:")
label1.grid(row=1,column=0)
webname=Entry(width=39)
webname.focus()
webname.grid(row=1,column=1,columnspan=2,)

# email name capture
label2=Label(text="Email/Username:")
label2.grid(row=2,column=0)
emailname=Entry(width=39)
emailname.insert(0,"cyriackunnumpuram2@gmail.com")
emailname.grid(row=2,column=1,columnspan=2)

# password capture
label3=Label(text="Password:")
label3.grid(row=3,column=0)
password=Entry(width=21)
password.grid(row=3,column=1,)

# password generator
passwordbutton=Button(text="Generate Password",command=generator)
passwordbutton.grid(row=3,column=2,)

# add to text button
addbutton=Button(text="Add",width=36,command=savingtofile)
addbutton.grid(row=4,column=1,columnspan=2)


window.mainloop()