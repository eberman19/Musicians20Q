from Musician import *
from tkinter import *

class DataSet:

    def __init__(self, MusicianList):
        self.MusicianList = MusicianList
        self.OriginalMusicianList = MusicianList
        self.GenreCount = self.updateGenreCount()
        self.ratio = self.updateratio()
        self.FrequentTopic = self.updateFrequentTopic()
        self.ZeroCount = self.updateZeroCount()
        self.mode = 1
        self.game = "incomplete"
        
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

    def updateratio(self, weight=lambda musician: int(musician.Frequency)): #this splits data closest to equal probabilities (frequencies) on both sides.
        #(self, weight=lambda musician: 1): #would split data according to equal # of musicians on both sides
        ratio = [0,0,0,0,0,0,0,0,0]
        for x in range(self.MusicianList[0].NCharacteristics):
            count1 = 0
            count0 = 0
            for k in range(len(self.MusicianList)):
                
                if self.MusicianList[k].Characteristics[x] == '1':
                    count1 += weight(self.MusicianList[k])
                if self.MusicianList[k].Characteristics[x] == '0':
                    count0 += weight(self.MusicianList[k])
            if count1 < count0:
                ratio[x] = count1/count0
            else:
                try:
                    ratio[x] = count0/count1
                except ZeroDivisionError:
                    print(count0,count1,[mus.Characteristics[x] for mus in self.MusicianList])
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
        if self.mode == 1:
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
        if self.mode == 2:
            if YesorNo == "No":
                self.MusicianList=self.MusicianList[1::]
                if len(self.MusicianList) == 0:
                    self.game = "lost"
            if YesorNo == "Yes":
                self.MusicianList=self.MusicianList[:1]
                self.game = "complete"
        return self.MusicianList;

    def update(self, YesorNo):
        updated = self.NarrowingOptions(YesorNo)
        if self.mode == 1:
            self.ratio = self.updateratio()
            self.FrequentTopic = self.updateFrequentTopic()
            self.ZeroCount = self.updateZeroCount()

    def reset(self):
        self.MusicianList = self.OriginalMusicianList
        self.ratio = self.updateratio()
        self.FrequentTopic = self.updateFrequentTopic()
        self.ZeroCount = self.updateZeroCount()

    def print(self, FileName):
        f = open(FileName,'w')
        for x in range(len(self.OriginalMusicianList)):
            f.write(self.OriginalMusicianList[x].CSV)
        f.close()

    def setprompt(self):
        question = str()
        if self.ZeroCount < 9:
            question=("Does the musician/band have this charactertic: %s?" % (Musician.Characteristic[self.FrequentTopic]))
        if self.ZeroCount == 9:
            self.mode = 2
            if self.game == "complete":
                question = "I got it! Thanks for playing."
                for x in range(len(self.OriginalMusicianList)):
                    if self.MusicianList[0].Name == self.OriginalMusicianList[x].Name:
                        self.OriginalMusicianList[x].setFrequency(str(int(self.OriginalMusicianList[x].Frequency) + 1))
                self.print('MusiciansFakeFile.txt')
            elif self.game == "lost":
                question = "I'm sorry. I do not know who you are thinking of."
            else:
                self.MusicianList.sort(key=lambda MusicianGuess: MusicianGuess.Frequency, reverse = True)
                question=("Are you thinking of %s?" % (self.MusicianList[0].Name))           
        return question
