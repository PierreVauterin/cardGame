import random 

def openPack():
    for i in range(nbCardsInPack):
        value = random.randint(1,100)
        if value==legendaryDrop: print(f"Card #{i} is legendary!")
        elif value>legendaryDrop and value <=epicDrop: print(f"Card {i} is epic!")
        elif value>epicDrop and value <=rareDrop: print (f"Card {i} is just rare...")
    pass


epicDrop = 15
rareDrop = 30
legendaryDrop = 1
nbCardsInPack = 5

openPack()