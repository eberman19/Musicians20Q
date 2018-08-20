from Musician import *
from DataSet import *
import csv

def CountQuestions(MusicianNum, ds):
    ##pass
    name = ds.MusicianList[MusicianNum].Name
    Mnumber = 0
    QCount = 0
    MCount = 0
    TotalCount = 0
    NamesList = []
    
    while ds.ZeroCount < 9: 
        for x in range(len(ds.MusicianList)):
            if name == ds.MusicianList[x].Name:
                Mnumber = x    
        if ds.MusicianList[Mnumber].Characteristics[ds.FrequentTopic] == "1":
            ds.update("Yes")
            QCount += 1
        else :
            ds.update("No")
            QCount += 1
    ds.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
    for l in range(len(ds.MusicianList)):
        NamesList.append(ds.MusicianList[l].Name)
    MCount = NamesList.index(name)
    TotalCount = MCount + QCount + 1
    ds.reset()
    return TotalCount;

def RunTest(DS):
    Questions = []
    for x in range(len(DS.MusicianList)):
        #print(x)
   ##    Questions.append(CountQuestions(x))
        Questions.append(CountQuestions(x, DS))
        print(DS.MusicianList[x].Name, CountQuestions(x, DS))

if __name__ == "__main__":
    musicians = []
    RowCount = 0
    with open('MusiciansFakeFile.txt', newline='') as inputfile:
        for row in csv.reader(inputfile):
            RowCount = RowCount + 1
            musicians.append(Musician(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8],row[9], row[10], row[11]))
    DS = DataSet(musicians)
    RunTest(DS)
