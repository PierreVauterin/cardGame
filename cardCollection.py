import random

legendaryCards = ["Gormok the destroyer", "Finizul", "Joe"]
epicCards = ["Arathula the spider mother", "Nevastros lord of the oceans", "Menezul the demon lord"]
rareCards = ["Knight", "Greater demon","Hungry shark"]
commonCards = ["Peasant", "Clown fish", "Spider","Imp"]

cards = [commonCards,rareCards,epicCards,legendaryCards]

def getSpecificCard(rarity,cards=cards):
    if rarity=="common":
        return cards[0][random.randint(0,len(cards[0])-1)]
    elif rarity == "rare":
        return cards[1][random.randint(0,len(cards[1])-1)]
    elif rarity == "epic":
        return cards[2][random.randint(0,len(cards[2])-1)]
    elif rarity == "legendary":
        return cards[3][random.randint(0,len(cards[3])-1)]
    