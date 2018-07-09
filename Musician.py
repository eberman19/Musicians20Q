import csv

class Musician:

    Characteristic = ["Rock","R&B","Pop","Country","Hip Hop","Band", "Male", "White", "Alive"]
    Genre = ["Rock","R&B","Pop","Country","Hip Hop"]

    def __init__(self, Name, Rock, RnB, Pop, Country, HipHop, Band, Gender, White, Alive, HairColor, Frequency):
        self.Name = Name
        self.Rock = Rock
        self.RnB = RnB
        self.Pop = Pop
        self.Country = Country
        self.HipHop = HipHop
        self.Band = Band
        self.Gender = Gender
        self.White = White
        self.Alive = Alive
        self.HairColor = HairColor
        self.Frequency = Frequency

        self.Characteristics = (Rock, RnB, Pop, Country, HipHop, Band, Gender, White, Alive)
        self.NCharacteristics = len(self.Characteristics)
        self.CSV = self.Name + "," + self.Rock + "," + self.RnB + ","+ self.Pop + ","+ self.Country + ","+ self.HipHop + "," + self.Band + "," + self.Gender + "," + self.White + "," + self.Alive + "," + self.HairColor + "," + self.Frequency + "\n"

    def setFrequency(self,fq):
        self.Frequency = fq
        self.updateCSV()

    def updateCSV(self):
        self.CSV = self.Name + "," + self.Rock + "," + self.RnB + ","+ self.Pop + ","+ self.Country + ","+ self.HipHop + "," + self.Band + "," + self.Gender + "," + self.White + "," + self.Alive + "," + self.HairColor + "," + self.Frequency + "\n"

    def __iadd__(self,other):
        self.setFrequency(str(int(self.Frequency) + other))
        return self
