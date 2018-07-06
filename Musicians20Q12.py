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
        musicians.append(Musician(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

DS = DataSet(musicians)
FrequentGenre = DS.GenreCount.index(max(DS.GenreCount))

Qanswer = ""
def YesCallBack():
    Qanswer = "Yes"
def NoCallBack():
    Qanswer = "No"
root = Tk()
root.geometry("300x500")
b1 = Button(root, text = "Yes", command = YesCallBack)
b1.place(relx = 0.25, rely = 0.5, anchor = CENTER)
b2 = Button(root, text = "No", command = NoCallBack)
b2.place(relx = 0.75, rely = 0.5, anchor = CENTER)

v = StringVar()
Label(root, textvariable=v).place(relx = .5, rely = .25, anchor = CENTER)
v.set("New Text!")

task = "not done"
while task != "done":
   ## answer = input("Is the musician/band a %s singer/group? Yes or No " % (Musician.Genre[FrequentGenre]))
    v.set("Is the musician/band a %s singer/group? Yes or No ")
    mainloop()

    if answer == "Yes":
        for x in range(len(musicians)):
            if musicians[x].Genre == (Musician.Genre[FrequentGenre]):
                options2.append(musicians[x])
                task = "done"
    elif answer == "No":
        DS.GenreCount[FrequentGenre] = -1 #this is not a possible answer so now it cannot be repeated
        FrequentGenre = DS.GenreCount.index(max(DS.GenreCount))

DS = DataSet(options2)
while (DS.ZeroCount < 4):
        answer = input("Does the musician/band have this charactertic: %s? Yes or No " % (Musician.Characteristic[DS.FrequentTopic]))
        DS.update(answer)
          
game = "not complete"
MCount = 0
DS.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)

while (game != "complete"):
    answer = input("Are you thinking of %s? Yes or No " % (DS.MusicianList[MCount].Name))
    if answer == "Yes":
        game = "complete"
        for x in range(len(musicians)):
            if DS.MusicianList[MCount].Name == musicians[x].Name:
                musicians[x].setFrequency(str(int(musicians[x].Frequency) + 1))
                print(musicians[x].Frequency)
                print(musicians[x].CSV)
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
