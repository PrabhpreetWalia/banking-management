from ast import Delete
from cProfile import label
from tkinter import *
from tkinter import messagebox
import sqlite3

# SQL database
conn = sqlite3.connect('bank.db')
c = conn.cursor()


# c.execute(''' 
#     CREATE TABLE customers(
#     account_number INTEGER PRIMARY KEY,
#     full_name TEXT,
#     mobile_number INTEGER,
#     pin INTEGER,
#     balance REAL
# )''')

# conn.commit()

# c.execute(''' 
#     CREATE TABLE admin(
#     admin_number INTEGER PRIMARY KEY,
#     password TEXT
# )''')

# conn.commit()



root = Tk()
root.title("Banking Management System")


#Employee functions
def employeefunc():
    mainFrame.pack_forget()
    global employeeFrame
    employeeFrame = LabelFrame(root, padx=100, pady=100)
    employeeFrame.pack()
    loginLabel = Label(employeeFrame, text="Admin Login")
    email = Label(employeeFrame, text="Admin Id: ")
    password = Label(employeeFrame, text="Password: ")
    emailEntry = Entry(employeeFrame, width=50)
    passwordEntry = Entry(employeeFrame, width=50)
    loginBtn = Button(employeeFrame, text="LOGIN", command = lambda: checkLoginemployee(emailEntry.get(), passwordEntry.get()))

    loginLabel.grid(row=0, column=0, columnspan=2, pady=10)
    email.grid(row=1, column=0, pady=10)
    password.grid(row=2, column=0, pady=10)
    emailEntry.grid(row=1, column=1, pady=10)
    passwordEntry.grid(row=2, column=1, pady=10)
    loginBtn.grid(row=3, column=0, columnspan=2, pady=10)

    employeeFrame.configure(bg="#222831")
    loginLabel.configure(bg="#222831")
    loginLabel.configure(fg="#fff")
    email.configure(bg="#222831")
    password.configure(bg="#222831")
    email.configure(fg="#fff")
    password.configure(fg="#fff")
    emailEntry.configure(bg="#222831")
    passwordEntry.configure(bg="#222831")
    emailEntry.configure(fg="#fff")
    passwordEntry.configure(fg="#fff")
    loginBtn.configure(bg="#00ADB5")
    loginBtn.configure(fg="#fff")

def loginadminfunc(Id, password):
    employeeFrame.pack_forget()
    global employeeLoginFrame
    employeeLoginFrame = LabelFrame(root, padx=100, pady=100)
    employeeLoginFrame.pack()
    selectLabel = Label(employeeLoginFrame, text="Select your option")
    depositBtn = Button(employeeLoginFrame, text="Create bank account", command= createfunc, padx=3, pady=5, width=20)
    withdrawBtn = Button(employeeLoginFrame, text="Close bank account", command=closebyadminfunc, padx=3, pady=5, width=20)
    pinBtn = Button(employeeLoginFrame, text="Create admin account", command=createadminfunc, padx=3, pady=5, width=20)
    closeBtn = Button(employeeLoginFrame, text="Close admin Account", command=closeadminfunc, padx=3, pady=5, width=20)
    exittBtn = Button(employeeLoginFrame, text="Exit", command=exitfunc, padx=3, pady=5, width=20)

    selectLabel.grid(row=0, column=0, columnspan=2,pady=10)
    depositBtn.grid(row=1, column=0, padx=20, pady=10)
    withdrawBtn.grid(row=1, column=1, padx=20, pady=10)
    pinBtn.grid(row=2, column=0, padx=20, pady=10)
    closeBtn.grid(row=2, column=1, padx=20, pady=10)
    exittBtn.grid(row=3, column=0, padx=20, pady=10, columnspan=2) 

    employeeLoginFrame.config(bg="#222831")
    selectLabel.config(bg="#222831")
    selectLabel.config(fg="#fff")
    depositBtn.config(bg="#00ADB5")
    depositBtn.config(fg="#fff")
    withdrawBtn.config(bg="#00ADB5")
    withdrawBtn.config(fg="#fff")
    pinBtn.config(bg="#00ADB5")
    pinBtn.config(fg="#fff")
    closeBtn.config(bg="#00ADB5")
    closeBtn.config(fg="#fff")
    exittBtn.config(bg="#00ADB5")
    exittBtn.config(fg="#fff")


def checkLoginemployee(Id, password):
    c.execute(" Select password FROM admin WHERE admin_number = " + Id)
    pin = c.fetchone()
    conn.commit()
    if pin is None:
        messagebox.showerror("Wrong", "Wrong Account Number!!!")
        
    if str(pin[0]) == str(password):
        loginadminfunc(Id, password)
    else:
        messagebox.showerror("Wrong", "Wrong Password!!!")

def createfunc():

    createCustomer = Toplevel(employeeLoginFrame)
    createCustomer.title("Create Account")
    accNum = Label(createCustomer, text="Account Number: ")
    name = Label(createCustomer, text="Full Name: ")
    mobile = Label(createCustomer, text="Mobile Number: ")
    pin = Label(createCustomer, text="PIN: ")
    balance = Label(createCustomer, text="Balance: ")
    
    accNumEntry = Entry(createCustomer, width=35)
    nameEntry = Entry(createCustomer, width=35)
    mobileEntry = Entry(createCustomer, width=35)
    pinEntry = Entry(createCustomer, width=35)
    balanceEntry = Entry(createCustomer, width=35)

    submitBtn = Button(createCustomer, text="SUBMIT", command=lambda: addtobase(accNumEntry.get(),nameEntry.get(),mobileEntry.get(),pinEntry.get(),balanceEntry.get(),createCustomer), width=20)

    accNum.grid(row=0,column=0,padx=3,pady=5)
    name.grid(row=1,column=0,padx=3,pady=5)
    mobile.grid(row=2,column=0,padx=3,pady=5)
    pin.grid(row=3,column=0,padx=3,pady=5)
    balance.grid(row=4,column=0,padx=3,pady=5)
    accNumEntry.grid(row=0,column=1,padx=3,pady=5)
    nameEntry.grid(row=1,column=1,padx=3,pady=5)
    mobileEntry.grid(row=2,column=1,padx=3,pady=5)
    pinEntry.grid(row=3,column=1,padx=3,pady=5)
    balanceEntry.grid(row=4,column=1,padx=3,pady=5)
    submitBtn.grid(row=5, column=0, columnspan=2, pady=7, padx=10)

    createCustomer.configure(bg="#222831")
    accNum.configure(bg="#222831")
    accNum.configure(fg="#fff")
    name.configure(bg="#222831")
    name.configure(fg="#fff")
    mobile.configure(bg="#222831")
    mobile.configure(fg="#fff")
    pin.configure(bg="#222831")
    pin.configure(fg="#fff")
    balance.configure(bg="#222831")
    balance.configure(fg="#fff")
    accNumEntry.configure(bg="#222831")
    nameEntry.configure(bg="#222831")
    mobileEntry.configure(bg="#222831")
    pinEntry.configure(bg="#222831")
    balanceEntry.configure(bg="#222831")
    accNumEntry.configure(fg="#fff")
    nameEntry.configure(fg="#fff")
    mobileEntry.configure(fg="#fff")
    pinEntry.configure(fg="#fff")
    balanceEntry.configure(fg="#fff")
    submitBtn.configure(bg="#00ADB5")
    submitBtn.configure(fg="#fff")


def addtobase(accNum, name, mobile, pin, balance, createCustomer):
    c.execute('''INSERT INTO customers 
    VALUES (?, ?, ?, ?, ?) ''', (accNum, name, mobile, pin, balance))
    conn.commit() 
    messagebox.showinfo("info", "Account created successfuly!!!")
    createCustomer.destroy()

def closebyadminfunc():

    closeCustomer = Toplevel(employeeLoginFrame)
    closeCustomer.title("Create Account")

    accNum = Label(closeCustomer, text="Account Number: ")
    accNumEntry = Entry(closeCustomer, width=35)
    deleteBtn = Button(closeCustomer, text="DELETE", width=40, command= lambda: deletefrombase(accNumEntry.get(), closeCustomer))
    
    accNum.grid(row=0,column=0,padx=3,pady=5)
    accNumEntry.grid(row=0,column=1,padx=3,pady=5)
    deleteBtn.grid(row=1, column=0, columnspan=2, padx=5,pady=7)

    closeCustomer.configure(bg="#222831")
    accNum.configure(bg="#222831")
    accNum.configure(fg="#fff")
    accNumEntry.configure(bg="#222831")
    accNumEntry.configure(fg="#fff")
    deleteBtn.configure(bg="#00ADB5")
    deleteBtn.configure(fg="#fff")

    
def deletefrombase(accNum, closeCustomer):
    c.execute("DELETE FROM customers WHERE account_number = "+ str(accNum))
    conn.commit()
    messagebox.showinfo("info", "Account deleted!!!")
    closeCustomer.destroy()

def createadminfunc():
    createAdmin = Toplevel(employeeLoginFrame)
    createAdmin.title("Create Admin Account")
    accNum = Label(createAdmin, text="Account Number: ")
    password = Label(createAdmin, text="Password: ")
    accNumEntry = Entry(createAdmin, width=35)
    passwordEntry = Entry(createAdmin, width=35)
    submitBtn = Button(createAdmin, text="SUBMIT", command=lambda: addtoadmin(accNumEntry.get(), passwordEntry.get(), createAdmin))

    accNum.grid(row="0", column="0",padx=3,pady=5)
    password.grid(row="1", column="0",padx=3,pady=5)
    accNumEntry.grid(row="0", column="1",padx=3,pady=5)
    passwordEntry.grid(row="1", column="1",padx=3,pady=5)
    submitBtn.grid(row=2, column=0, columnspan=2, padx=5,pady=7)

    createAdmin.configure(bg="#222831")
    accNum.configure(bg="#222831")
    accNum.configure(fg="#fff")
    accNumEntry.configure(bg="#222831")
    accNumEntry.configure(fg="#fff")
    password.configure(bg="#222831")
    password.configure(fg="#fff")
    passwordEntry.configure(bg="#222831")
    passwordEntry.configure(fg="#fff")
    submitBtn.configure(bg="#00ADB5")
    submitBtn.configure(fg="#fff")


def addtoadmin(accNum, password, createAdmin):
    c.execute('''INSERT INTO admin 
    VALUES (?, ?) ''', (accNum, password))
    conn.commit() 
    messagebox.showinfo("info", "Admin account created successfuly!!!")
    createAdmin.destroy()

def closeadminfunc():
    closeAdmin = Toplevel(employeeLoginFrame)
    closeAdmin.title("Delete Admin Account")

    accNum = Label(closeAdmin, text="Admin Number: ")
    accNumEntry = Entry(closeAdmin, width=35)
    deleteBtn = Button(closeAdmin, text="DELETE", width=40, command= lambda: deletefromadmin(accNumEntry.get(), closeAdmin))
    
    accNum.grid(row=0,column=0,padx=3,pady=5)
    accNumEntry.grid(row=0,column=1,padx=3,pady=5)
    deleteBtn.grid(row=1, column=0, columnspan=2, padx=5,pady=7)

    closeAdmin.configure(bg="#222831")
    accNum.configure(bg="#222831")
    accNum.configure(fg="#fff")
    accNumEntry.configure(bg="#222831")
    accNumEntry.configure(fg="#fff")
    deleteBtn.configure(bg="#00ADB5")
    deleteBtn.configure(fg="#fff")

def deletefromadmin(accNum, closeAdmin):
    c.execute("DELETE FROM admin WHERE admin_number = "+ str(accNum))
    conn.commit()
    messagebox.showinfo("info", "Admin account deleted successfuly!!!")
    closeAdmin.destroy()


# Customer Functions
def customerfunc():
    mainFrame.pack_forget()
    global customerFrame
    customerFrame = LabelFrame(root, padx=100, pady=100)
    customerFrame.pack()
    loginLabel = Label(customerFrame, text="Customer Login")
    customerId = Label(customerFrame, text="Customer ID: ")
    password = Label(customerFrame, text="Password: ")
    customerIdEntry = Entry(customerFrame, width=50)
    passwordEntry = Entry(customerFrame, width=50)
    loginBtn = Button(customerFrame, text="LOGIN", command = lambda: checkLogincustomer(customerIdEntry.get(), passwordEntry.get()))

    loginLabel.grid(row=0, column=0, columnspan=2, pady=10)
    customerId.grid(row=1, column=0, pady=10)
    password.grid(row=2, column=0, pady=10)
    customerIdEntry.grid(row=1, column=1, pady=10)
    passwordEntry.grid(row=2, column=1, pady=10)
    loginBtn.grid(row=3, column=0, columnspan=2, pady=10)

    customerFrame.configure(bg="#222831")
    loginLabel.configure(bg="#222831")
    loginLabel.configure(fg="#fff")
    customerId.configure(bg="#222831")
    customerId.configure(fg="#fff")
    customerIdEntry.configure(bg="#222831")
    customerIdEntry.configure(fg="#fff")
    password.configure(bg="#222831")
    password.configure(fg="#fff")
    passwordEntry.configure(bg="#222831")
    passwordEntry.configure(fg="#fff")
    loginBtn.configure(bg="#00ADB5")
    loginBtn.configure(fg="#fff")


    
def logincustomerfunc(Id, password):
    customerFrame.pack_forget()
    global customerLoginFrame
    customerLoginFrame = LabelFrame(root, padx=100, pady=100)
    customerLoginFrame.pack()
    selectLabel = Label(customerLoginFrame, text="Select your option")
    depositBtn = Button(customerLoginFrame, text="Deposit", command= lambda: depositfunc(Id), padx=3, pady=5, width=20)
    withdrawBtn = Button(customerLoginFrame, text="Withdraw", command=lambda: withdrawfunc(Id), padx=3, pady=5, width=20)
    balanceBtn = Button(customerLoginFrame, text="Check Balance", command=lambda: balancefunc(Id), padx=3, pady=5, width=20)
    exittBtn = Button(customerLoginFrame, text="Exit", command=exitfunc, padx=3, pady=5, width=20)

    selectLabel.grid(row=0, column=0, columnspan=2,pady=10)
    depositBtn.grid(row=1, column=0, padx=20, pady=10)
    withdrawBtn.grid(row=1, column=1, padx=20, pady=10)
    balanceBtn.grid(row=3, column=0, padx=20, pady=10)
    exittBtn.grid(row=3, column=1, padx=20, pady=10)

    customerLoginFrame.config(bg="#222831")
    selectLabel.config(bg="#222831")
    selectLabel.config(fg="#fff")
    depositBtn.config(bg="#00ADB5")
    depositBtn.config(fg="#fff")
    withdrawBtn.config(bg="#00ADB5")
    withdrawBtn.config(fg="#fff")
    balanceBtn.config(bg="#00ADB5")
    balanceBtn.config(fg="#fff")
    exittBtn.config(bg="#00ADB5")
    exittBtn.config(fg="#fff")

def checkLogincustomer(Id, password):
    c.execute(" Select pin FROM customers WHERE account_number = " + Id)
    pin = c.fetchone()
    conn.commit()
    if pin is None:
        messagebox.showerror("Wrong", "Wrong Account Number!!!")
        
    if str(pin[0]) == str(password):
        logincustomerfunc(Id, password)
    else:
        messagebox.showerror("Wrong", "Wrong Password!!!")

def depositfunc(Id):
    depositFrame = Toplevel(customerLoginFrame)
    depositFrame.title("Deposit Money")

    deposit = Label(depositFrame, text="Enter Deposit Amount: ")
    depositEntry = Entry(depositFrame, width=35)
    depositBtn = Button(depositFrame, text="DEPOSIT", width=40, command= lambda: addmoney(Id, depositEntry.get(), depositFrame))
    
    deposit.grid(row=0,column=0,padx=3,pady=5)
    depositEntry.grid(row=0,column=1,padx=3,pady=5)
    depositBtn.grid(row=1, column=0, columnspan=2, padx=5,pady=7)

    depositFrame.configure(bg="#222831")
    deposit.configure(bg="#222831")
    deposit.configure(fg="#fff")
    depositEntry.configure(bg="#222831")
    depositEntry.configure(fg="#fff")
    depositBtn.configure(bg="#00ADB5")
    depositBtn.configure(fg="#fff")


def addmoney(Id, deposit, depositFrame):

    c.execute("SELECT balance FROM customers WHERE account_number = "+ Id)
    balance = c.fetchone()[0]
    conn.commit()
    new_balance = balance + float(deposit)
    c.execute(" UPDATE customers SET balance = "+ str(new_balance) +" WHERE account_number ="+ str(Id))
    conn.commit()
    messagebox.showinfo("info", "Deposit Successful!!!")
    depositFrame.destroy()

def withdrawfunc(Id):
    withdrawFrame = Toplevel(customerLoginFrame)
    withdrawFrame.title("Withdraw Money")

    withdraw = Label(withdrawFrame, text="Enter WIthdraw Amount: ")
    withdrawEntry = Entry(withdrawFrame, width=35)
    withdrawBtn = Button(withdrawFrame, text="WITHDRAW", width=40, command= lambda: withdrawmoney(Id, withdrawEntry.get(), withdrawFrame))
    
    withdraw.grid(row=0,column=0,padx=3,pady=5)
    withdrawEntry.grid(row=0,column=1,padx=3,pady=5)
    withdrawBtn.grid(row=1, column=0, columnspan=2, padx=5,pady=7)

    withdrawFrame.configure(bg="#222831")
    withdraw.configure(bg="#222831")
    withdraw.configure(fg="#fff")
    withdrawEntry.configure(bg="#222831")
    withdrawEntry.configure(fg="#fff")
    withdrawBtn.configure(bg="#00ADB5")
    withdrawBtn.configure(fg="#fff")

    

def withdrawmoney(Id, withdraw, withdrawFrame):

    c.execute("SELECT balance FROM customers WHERE account_number = "+ Id)
    balance = c.fetchone()[0]
    conn.commit()

    if balance < float(withdraw):
        messagebox.showerror("Error", "Not sufficent Balance")
        return
    else:
        new_balance = balance - float(withdraw)

    c.execute(" UPDATE customers SET balance = "+ str(new_balance) +" WHERE account_number ="+ str(Id))
    conn.commit()
    messagebox.showinfo("info", "Withdrawl Successful!!!")
    withdrawFrame.destroy()

def balancefunc(Id):
    c.execute("SELECT balance FROM customers WHERE account_number ="+ Id)
    messagebox.showinfo("", "Your account balance is "+ str(c.fetchone()[0]))
    conn.commit()

def exitfunc():
    conn.close()
    root.destroy()


# Starting page
mainFrame = LabelFrame(root, padx=100, pady=100)


roleLabel = Label(mainFrame, text="Please select your role")
employerBtn = Button(mainFrame, text="EMPLOYEE", padx=20, pady=20, command=employeefunc)
customerBtn = Button(mainFrame, text="CUSTOMER", padx=20, pady=20, command= customerfunc)

mainFrame.configure(bg="#222831")
roleLabel.configure(bg="#222831")
roleLabel.configure(fg="#fff")
customerBtn.configure(bg="#00ADB5")
customerBtn.configure(fg="#fff")
employerBtn.configure(bg="#00ADB5")
employerBtn.configure(fg="#fff")

mainFrame.pack()
roleLabel.grid(row=0, column=0, columnspan=2)
employerBtn.grid(row=1, column=0,padx=20,pady=20)
customerBtn.grid(row=1, column=1,padx=20,pady=20)



root.mainloop()
