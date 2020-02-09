import tkinter as tk
import tkinter.messagebox
import bot
import os
import string

myUSERS = []

def loadList(): #called in the initlization to load the users from the users.txt file
    if os.path.isfile("users.txt"):
        with open("users.txt", "r") as f:
            tempUsers = f.read()
        global myUSERS
        myUSERS = tempUsers.split(',')
        myUSERS[:] = [user for user in myUSERS if user]#remove empty space
        print(myUSERS)


def updateList():
    print(myUSERS)
    with open("users.txt", "w") as f:
        for user in myUSERS:
            f.write(user + ',')

def addUser():
    temp = accountEntry.get()
    temp = temp.strip()
    if temp != "":
        accountsList.insert(tk.END, temp)
        myUSERS.append(temp)
    updateList()
    accountEntry.delete(0, tk.END)

def Login():
    password = pwEntry.get()
    username = userEntry.get()
    postNumber = nmbrOfPostsEntry.get()
    if password == "" or username == "" or postNumber == "":
        tk.messagebox.showerror("Error", "Please provide all the required information")
        return
    mybot = bot.InstaBot(username, password, int(postNumber), myUSERS, checkBtn._getboolean)
    mybot.signIn()
    mybot.like()
    print(username, password)

def initilizeList():#Initilize with past elements from users.txt
    for user in myUSERS:
        accountsList.insert(tk.END, user)

def removeUser():
    if accountsList.size() > 0:
        temp = accountsList.get(tk.ACTIVE)
        myUSERS.remove(temp)
        accountsList.delete(tk.ACTIVE)
        updateList()


def saveData():
    if userEntry.get().strip() == "" or pwEntry.get().strip() == "":
        tkinter.messagebox.showerror("Error", "Please provide username and password")
        return
    data = userEntry.get() + ',' + pwEntry.get()
    with open("data.txt", "w") as f:
        f.write(data)

def loadData():
    if os.path.isfile("data.txt"):
        with open("data.txt", 'r') as f:
            tempData = f.read()
        myData = tempData.split(',')
        userEntry.insert(0, myData[0])
        pwEntry.insert(0, myData[1])

root = tk.Tk()
root.title("AutoLike")

#Creating and placing the login grid
LoginInterface = tk.Frame(root)
userEntry = tk.Entry(LoginInterface)
pwEntry = tk.Entry(LoginInterface)
nmbrOfPostsEntry = tk.Entry(LoginInterface)
tk.Label(LoginInterface, text="Username").grid(row=0)
tk.Label(LoginInterface, text="Password").grid(row=1)
tk.Label(LoginInterface, text="Number of posts to like").grid(row=2)
checkBtn = tk.Checkbutton(LoginInterface, text = "Like only from the list")
saveDataBtn = tk.Button(LoginInterface, text="Save", command=saveData)
saveDataBtn.grid(row = 1, column = 3)
checkBtn.grid(row = 3)
userEntry.grid(row=0, column=1)
pwEntry.grid(row=1, column=1)
nmbrOfPostsEntry.grid(row=2, column=1)
loginBtn = tk.Button(LoginInterface, text="Go", command=Login)
loginBtn.grid(row=3, column=1)

#Accounts to like interface
AccountsToLikeInterface = tk.Frame(root)
accountsList = tk.Listbox(AccountsToLikeInterface, width =40)
accountsList.grid(row=0, column=0, columnspan=3)
accountEntry = tk.Entry(AccountsToLikeInterface)
accountEntry.grid(row=1,column=0)
addBtn = tk.Button(AccountsToLikeInterface, text="Add", command=addUser)
addBtn.grid(row=1, column=1)
removeBtn = tk.Button(AccountsToLikeInterface, text="Remove", command=removeUser)
removeBtn.grid(row=1, column=2)
root.update_idletasks()


LoginInterface.place(height=100, width=400, x=0, y=0)
root.update_idletasks()
AccountsToLikeInterface.place(x=0, y=LoginInterface.winfo_height())
root.minsize(400, 400)

loadData()
loadList()
initilizeList()
root.mainloop()
