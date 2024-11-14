import random

secretCards = ["The treasure"]
legendaryCards = ["Gormok the destroyer", "Finizul", "Joe"]
epicCards = ["Arathula the spider mother", "Nevastros lord of the oceans", "Menezul the demon lord"]
rareCards = ["Knight", "Greater demon","Hungry shark"]
commonCards = ["Peasant", "Clown fish", "Spider","Imp"]

cards = [commonCards,rareCards,epicCards,legendaryCards,secretCards]

def getSpecificCard(rarity,cards=cards):
    if rarity=="common":
        return cards[0][random.randint(0,len(cards[0])-1)]
    elif rarity == "rare":
        return cards[1][random.randint(0,len(cards[1])-1)]
    elif rarity == "epic":
        return cards[2][random.randint(0,len(cards[2])-1)]
    elif rarity == "legendary":
        if random.randint(1,100)==1:return cards[4][random.randint(0,len(cards[4])-1)]
        else: return cards[3][random.randint(0,len(cards[3])-1)]
    