from Musician import *
from DataSet import *
import csv

##def CountQuestions(musician, ds):
def CountQuestions(musician):
    ##pass
    name = DS.MusicianList[musician].Name
    Mnumber = 0
    QCount = 0
    while DS.ZeroCount < 9: 
        for x in range(len(DS.MusicianList)):
            if name == DS.MusicianList[x].Name:
                Mnumber = x    
        if DS.MusicianList[Mnumber].Characteristics[DS.FrequentTopic] == "1":
            DS.update("Yes")
            QCount += 1
        else :
            DS.update("No")
            QCount += 1
    MCount = 0           
    DS.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
    NamesList = []
    for l in range(len(DS.MusicianList)):
        NamesList.append(DS.MusicianList[l].Name)
    MCount = NamesList.index(name)
    TotalCount = MCount + QCount + 1
    return TotalCount;

def RunTest(DS):
    Questions = []
    for x in range(len(DS.MusicianList)):
##        Questions.append(CountQuestions(DS.MusicianList[x], DS))
##        Questions.append(CountQuestions(x))
        print(DS.MusicianList[x].Name, CountQuestions(x))

if __name__ == "__main__":
    musicians = []
    RowCount = 0
    with open('MusiciansFakeFile.txt', newline='') as inputfile:
        for row in csv.reader(inputfile):
            RowCount = RowCount + 1
            musicians.append(Musician(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8],row[9], row[10], row[11]))
    DS = DataSet(musicians)

    RunTest(DS)
