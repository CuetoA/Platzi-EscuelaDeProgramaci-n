from unicodedata import name


class DVD():

    def __init__(self, name, releaseYear, director) -> None:
        self.name = name
        self.releaseYear = releaseYear
        self.directir = director

    def toString(self):
        return f"The movie {self.name} directed by {self.director}, released in {self.releaseYear}"

dvdBox = [DVD] * 10

print(dvdBox)
