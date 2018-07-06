from Musician import *

class DataSet:

    def __init__(self, MusicianList):
        self.MusicianList = MusicianList
        self.GenreCount = self.updateGenreCount()
        self.ratio = self.updateratio()
        self.FrequentTopic = self.updateFrequentTopic()
        self.ZeroCount = self.updateZeroCount()

    def updateGenreCount(self):
        GenreCount = [0,0,0,0,0]
        for x in range(len(self.MusicianList)):
            if self.MusicianList[x].Genre == ("Rock"):
                GenreCount[0] += int(self.MusicianList[x].Frequency)
            if self.MusicianList[x].Genre == ("R&B"):
                GenreCount[1] += int(self.MusicianList[x].Frequency)
            if self.MusicianList[x].Genre == ("Pop"):
                GenreCount[2] += int(self.MusicianList[x].Frequency)
            if self.MusicianList[x].Genre == ("Country"):
                GenreCount[3] += int(self.MusicianList[x].Frequency)
            if self.MusicianList[x].Genre == ("Hip Hop"):
                GenreCount[4] += int(self.MusicianList[x].Frequency)
        return GenreCount

    def updateratio(self):
        ratio = [0,0,0,0]
        for x in range(self.MusicianList[0].NCharacteristics):
            count = 0
            for k in range(len(self.MusicianList)):
                if self.MusicianList[k].Characteristics[x] == '1':
                    count += 1
            if (count < ((len(self.MusicianList))-count)):
                ratio[x] = (count/((len(self.MusicianList))-count))
            else :
                ratio[x] = (((len(self.MusicianList))-count)/count)
        return ratio;

    def updateFrequentTopic(self):
        for r in range(len(self.ratio)):
            if self.ratio[r] == (min(self.ratio, key=lambda x:abs(x-1))):
                FrequentTopic = r
        return FrequentTopic;

    def updateZeroCount(self):
        ZeroCount = 0
        for r in range(len(self.ratio)):
            if self.ratio[r] == 0.0: #all either a 1 or a 0 in the column
                ZeroCount += 1 # no need to ask the question because it does not eliminate any answers
        return ZeroCount;

    def NarrowingOptions(self, YesorNo):
        optionstemp = []
        if YesorNo == "Yes":
            for x in range(len(self.MusicianList)):
                if self.MusicianList[x].Characteristics[self.FrequentTopic] == "1":
                    optionstemp.append(self.MusicianList[x])
        elif YesorNo == "No":
            for x in range(len(self.MusicianList)):
                if self.MusicianList[x].Characteristics[self.FrequentTopic] != "1":
                    optionstemp.append(self.MusicianList[x])
        self.MusicianList = optionstemp
        return self.MusicianList;

    def update(self, YesorNo):
        updated = self.NarrowingOptions(YesorNo)
        self.ratio = self.updateratio()
        self.FrequentTopic = self.updateFrequentTopic()
        self.ZeroCount = self.updateZeroCount()

musicians = []
RowCount = 0
with open('MusiciansFile.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        RowCount = RowCount + 1
        musicians.append(Musician(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))
        
##DS = DataSet(musicians)
##print(len(DS.MusicianList))
##thecount = 0
##for x in range(len(DS.MusicianList)):
##    if DS.MusicianList[x].Characteristics[DS.FrequentTopic] == "0":
##        thecount += 1
##print(thecount)
##        
##DS.NarrowingOptions("No")
##print(DS.FrequentTopic)
##print(DS.MusicianList[0].Characteristics[DS.FrequentTopic])
##print(len(DS.MusicianList))
