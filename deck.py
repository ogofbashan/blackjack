class PlayingCards():
    def __init__(self, deck = []):
        self.deck = deck

    def startDeckBuilder(self):
        for _ in range(7):
            self.endDeckBuilder()

    def endDeckBuilder(self):
        for s in ['\u2663', '\u2660', '\u2666', '\u2665']:
            for name in range (1,14):
                    if name == 1:
                        name = 'A'+ s
                    elif name == 11:
                        name = 'J' + s
                    elif name == 12:
                        name = 'Q' + s
                    elif name == 13:
                        name = 'K' + s
                    else:
                        name = str(name) + s
                    self.deck.append(name)
        return self.deck
