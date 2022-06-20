from unicodedata import name


class DVD():

    def __init__(self, name, releaseYear, director) -> None:
        self.name = name
        self.releaseYear = releaseYear
        self.directir = director

    def toString(self):
        return f"The movie {self.name} directed by {self.director}, released in {self.releaseYear}"

dvdBox = [DVD] * 10

forrestDVD = DVD('Forrest Gump', '1994', 'Robert Zemeckis')
incrediblesDVD =  DVD("The Incredibles", 2004, "Brad Bird")
findingDoryDVD =  DVD("Finding Dory", 2016, "Andrew Stanton")
lionKingDVD    =  DVD("The Lion King", 2019, "Jon Favreau")


dvdBox[2] = forrestDVD
dvdBox[3] = incrediblesDVD
dvdBox[4] = findingDoryDVD
dvdBox[5] = lionKingDVD

print(dvdBox)
