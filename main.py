import random 

def openPack():
    for i in range(nbCardsInPack):
        value = random.randint(1,100)
        if value==legendaryDrop: print(f"Card #{i+1} is legendary!")
        elif value>legendaryDrop and value <=epicDrop: print(f"Card {i+1} is epic!")
        elif value>epicDrop and value <=rareDrop: print (f"Card {i+1} is just rare...")
        else: print(f"Card {i+1} is common...")
    pass


epicDrop = 15
rareDrop = 30
legendaryDrop = 1
nbCardsInPack = 5

openPack()