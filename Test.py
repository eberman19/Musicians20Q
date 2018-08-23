from Musician import *
from DataSet import *
import csv

def CountQuestions(MusicianNum, ds):
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
    SortedMusicianList = sorted(ds.MusicianList, key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
    NamesList = [Musician.Name for Musician in SortedMusicianList]
    MCount = NamesList.index(name)
    TotalCount = MCount + QCount + 1
    ds.reset()
    return TotalCount;

def RunTest(DS):
    Questions = []
    FullCount = 0
    for x in range(len(DS.MusicianList)):
        Questions.append(CountQuestions(x, DS))
        print(DS.MusicianList[x].Name, CountQuestions(x, DS))
    f = open('MusiciansTestData2.txt','w')
    for x in range(len(DS.OriginalMusicianList)):
        f.write(DS.OriginalMusicianList[x].Name + " , " + str(CountQuestions(x, DS)) + "\n")
    FullCount = sum(Questions)
    f.write("\n" + "\n" + "\n" + str(FullCount))
    print(FullCount)
    f.close()

if __name__ == "__main__":
    musicians = []
    RowCount = 0
    with open('MusiciansFakeFile.txt', newline='') as inputfile:
        for row in csv.reader(inputfile):
            RowCount = RowCount + 1
            musicians.append(Musician(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7], row[8],row[9], row[10], row[11]))
    DS = DataSet(musicians)
    RunTest(DS)
