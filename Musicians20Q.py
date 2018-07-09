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

answer = ""
def YesCallBack():
    answer = "Yes"
    DS.update(answer)
    if DS.ZeroCount < 9:
        v.set("Does the musician/band have this charactertic: %s?" % (Musician.Characteristic[DS.FrequentTopic]))
    if DS.ZeroCount == 9:
        DS.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
        v.set("Are you thinking of %s?" % (DS.MusicianList[MCount].Name))

def NoCallBack():
    answer = "No"
    DS.update(answer)
    if DS.ZeroCount < 9:
        v.set("Does the musician/band have this characteristic: %s?" % (Musician.Characteristic[DS.FrequentTopic]))
    if DS.ZeroCount == 9:
        DS.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
        v.set("Are you thinking of %s? Yes or No " % (DS.MusicianList[MCount].Name))

root = Tk()
root.geometry("500x500")
root.configure(background='black')
b1 = Button(root, text = "Yes",  font = ("Helvetica",20), command = YesCallBack)
b1.place(relx = 0.25, rely = 0.5, anchor = CENTER)
b2 = Button(root, text = "No", font = ("Helvetica",20), command = NoCallBack)
b2.place(relx = 0.75, rely = 0.5, anchor = CENTER)

v = StringVar()
Label(root, textvariable=v, bg = "black",fg="white", font=("Helvetica",18)).place(relx = .5, rely = .25, anchor = CENTER)
v.set("Does the musician/band have this characteristic: %s?" % (Musician.Characteristic[DS.FrequentTopic]))

game = "not complete"
MCount = 0

mainloop()
                
##game = "not complete"
##MCount = 0
##DS.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
while (game != "complete"):
    answer = input("Are you thinking of %s? Yes or No " % (DS.MusicianList[MCount].Name))
    if answer == "Yes":
        game = "complete"
        for x in range(len(musicians)):
            if DS.MusicianList[MCount].Name == musicians[x].Name:
                musicians[x].setFrequency(str(int(musicians[x].Frequency) + 1))
        print("I got it! Thanks for playing.")
    if answer == "No":
        if (len(DS.MusicianList)) == (MCount + 1):
            game = "complete"
            print("I'm sorry. I do not know who you are thinking of.")
    MCount += 1

f = open('MusiciansFakeFile.txt','w')
for x in range(len(musicians)):
    f.write(musicians[x].CSV)
f.close()
