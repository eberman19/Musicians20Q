import csv

class Musician:

    Characteristic = ["Band", "Male", "White", "Alive"]
    Genre = ["Rock","R&B","Pop","Country","Hip Hop"]

    def __init__(self, Name, Genre, Band, Gender, White, Alive, HairColor, Frequency):
        self.Name = Name
        self.Genre = Genre
        self.Band = Band
        self.Gender = Gender
        self.White = White
        self.Alive = Alive
        self.HairColor = HairColor
        self.Frequency = Frequency

        self.Characteristics = (Band, Gender, White, Alive)
        self.NCharacteristics = len(self.Characteristics)
        self.CSV = self.Name + "," + self.Genre + "," + self.Band + "," + self.Gender + "," + self.White + "," + self.Alive + "," + self.HairColor + "," + self.Frequency + "\n"

    def setFrequency(self,fq):
        print(fq)
        self.Frequency = fq
        self.updateCSV()

    def updateCSV(self):
        self.CSV = self.Name + "," + self.Genre + "," + self.Band + "," + self.Gender + "," + self.White + "," + self.Alive + "," + self.HairColor + "," + self.Frequency + "\n"

    def __iadd__(self,other):
        self.setFrequency(str(int(self.Frequency) + other))
        return self
