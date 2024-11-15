class player:
    
    def __init__(self,deck):
        self.deck = deck
        self.hand = []

    def draw(self,nbCardsToDraw):
        for i in range(nbCardsToDraw):
            self.hand.append(self.deck[0])
            del self.deck[0]

class game:

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2

        player1.draw(5)
        player2.draw(5)

    def endGame():
        pass

    def turn():
        pass