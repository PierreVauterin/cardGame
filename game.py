class player:
    
    def __init__(self,deck,hand):
        self.deck = deck
        self.hand = hand

    def draw(self,nbCardsToDraw):
        for i in range(nbCardsToDraw):
            self.hand.append(self.deck[0])
            del self.deck[0]

class game:

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2