import csv
from tkinter import *
from Musician import *
from DataSet import *

options2 = []
musicians = []
RowCount = 0
with open('MusiciansFakeFile.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        RowCount = RowCount + 1
        musicians.append(Musician(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8],row[9], row[10], row[11]))
DS = DataSet(musicians)

def YesCallBack():
    DS.update("Yes")
    question = DS.setprompt()
    v.set(question)

def NoCallBack():
    DS.update("No")
    question = DS.setprompt()
    v.set(question)

root = Tk()

root.geometry("500x500")
root.configure(background='black')
b1 = Button(root, text = "Yes",  font = ("Helvetica",20), command = YesCallBack)
b1.place(relx = 0.25, rely = 0.5, anchor = CENTER)
b2 = Button(root, text = "No", font = ("Helvetica",20), command = NoCallBack)
b2.place(relx = 0.75, rely = 0.5, anchor = CENTER)

v = StringVar()
Label(root, textvariable=v, bg = "black",fg="white", font=("Helvetica",18)).place(relx = .5, rely = .25, anchor = CENTER)
v.set(DS.setprompt())
mainloop()
