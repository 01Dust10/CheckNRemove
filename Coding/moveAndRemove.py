import os
from datetime import date
import datetime
from tkinter import *
import tkinter as tk
import random
import string

def checkNdelete():
    today = date.today()
    list = os.listdir()
    for file in list:
        print(file)
        if(file!="moveAndRemove.py"):
            tm = datetime.datetime.fromtimestamp(os.path.getmtime(file))
            diff = today.day - tm.day
            if (diff >= 0):
                resultsText.insert(tk.END, "Removed: %s\n"%(file))
                os.remove(file)
            else:
                resultsText.insert(tk.END, "Skipped: %s\n"%(file))
        else:
            continue
def makeTxtFiles(n):
    chars = string.ascii_letters + string.digits
    for i in range(n):
        with open( ''.join(random.choices(chars, k=5)), "w", encoding="utf-8") as file:
            file.write("blah blah")

root = tk.Tk()
root.title("check and remove")
root.geometry("500x350")

checkButton = tk.Button(root, text = "Check", command=checkNdelete, width=10, height=3)
txtButton = tk.Button(root, text = "Text FIles", command=lambda: makeTxtFiles(5), width=10, height=3)
resultsText = tk.Text(root, height=40, width=30)

checkButton.pack(pady = 30, padx=10)
txtButton.pack()
resultsText.pack(padx=5)
root.mainloop()