import random 
from cardCollection import getSpecificCard

legendaryDrop = 1
epicDrop = 11
rareDrop = 30
dropRates = [rareDrop,epicDrop,legendaryDrop]

nbCardsInPack = 5

def openPack():
    print("Opening a pack!")
    for i in range(0,nbCardsInPack):
        value = random.randint(1,100)
        if value==legendaryDrop: print(f"WOW!! Card {i+1} is legendary! You got {getSpecificCard("legendary")}")
        elif value>legendaryDrop and value <=epicDrop: print(f"Nice, card {i+1} is epic! You got {getSpecificCard("epic")}")
        elif value>epicDrop and value <=rareDrop: print (f"Oh, card {i+1} is rare... You got {getSpecificCard("rare")}")
        else: print(f"Card {i+1} is common. You got {getSpecificCard("common")}")
    print("\n")

def printDropRates(dropRates=dropRates):
    print(f"Common card: {100-dropRates[0]}%\nRare card: {dropRates[0]-dropRates[1]}%\nEpic card: {dropRates[1]-dropRates[2]}%\nLegendary card: {dropRates[2]}%\n")

printDropRates()

openPack()
openPack()