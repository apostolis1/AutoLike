import tkinter as tk
import tkinter.messagebox
import bot

def Login():
    password = pwEntry.get()
    username = userEntry.get()
    postNumber = nmbrOfPostsEntry.get()
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
LoginInterface.pack()

root.minsize(400,400)


root.mainloop()

