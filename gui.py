import tkinter as tk
import tkinter.messagebox
import bot
import os
import string

def addUser():
    temp = accountEntry.get()
    temp = temp.strip()
    if temp != "":
        accountsList.insert(tk.END, temp)   
    accountEntry.delete(first=0, last=tk.END)


def Login():
    password = pwEntry.get()
    username = userEntry.get()
    postNumber = nmbrOfPostsEntry.get()
    if password == "" or username == "" or postNumber == "":
        tk.messagebox.showerror("Error", "Please provide all the required information")
        return
    mybot = bot.InstaBot(username, password, postNumber)
    print(username, password)

root = tk.Tk()

#Creating and placing the login grid
LoginInterface = tk.Frame(root)
userEntry = tk.Entry(LoginInterface)
pwEntry = tk.Entry(LoginInterface)
nmbrOfPostsEntry= tk.Entry(LoginInterface)
tk.Label(LoginInterface, text = "Username").grid(row = 0)
tk.Label(LoginInterface, text = "Password").grid(row = 1)
tk.Label(LoginInterface, text = "Number of posts to like").grid(row = 2)
userEntry.grid(row = 0, column = 1)
pwEntry.grid(row = 1, column = 1)
nmbrOfPostsEntry.grid(row = 2, column = 1)
loginBtn = tk.Button(LoginInterface, text = "Go", command = Login)
loginBtn.grid(row = 3, column = 1)

#Accounts to like interface
AccountsToLikeInterface = tk.Frame(root)
accountsList = tk.Listbox(AccountsToLikeInterface)
accountsList.grid(row = 0, column = 0)
accountEntry = tk.Entry(AccountsToLikeInterface)
accountEntry.grid(row = 1, column = 0)
addBtn = tk.Button(AccountsToLikeInterface, text = "Add", command = addUser)
addBtn.grid(row = 1, column = 1)
root.update_idletasks()

#TODO add a file to save the list of users

LoginInterface.place(height = 100, width = 400, x = 0, y = 0)
root.update_idletasks()
AccountsToLikeInterface.place(x = 0, y = LoginInterface.winfo_height())
root.minsize(400,400)
root.mainloop()

