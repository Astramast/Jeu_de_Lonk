from random import shuffle


class Deck:
    def __init__(self, repetitions=4, values=13):
        self.cards = [i + 1 for i in range(values)]*repetitions
        self.cards.sort()
        self.have_king = self.update_have_king()
        self.have_queen = self.update_have_queen()
        self.have_jack = self.update_have_jack()
        self.value = sum(self.cards)

    def get_cards(self):
        return self.cards

    def add_card(self, card_value):
        self.cards.append(card_value)

    def remove_card(self, card_value):
        if card_value in self.cards:
            self.cards.remove(card_value)
        else:
            raise ValueError("This card is not in the deck")

    def take_top_card(self):
        return self.cards.pop(0)

    def sort_deck(self):
        self.cards.sort()

    def shuffle_deck(self):
        shuffle(self.cards)

    def update_have_king(self):
        self.have_king = 13 in self.cards
        return self.have_king

    def update_have_queen(self):
        self.have_queen = 12 in self.cards
        return self.have_queen

    def update_have_jack(self):
        self.have_jack = 11 in self.cards
        return self.have_jack

    def update_value(self):
        self.value = sum(self.cards)

    def fullupdate(self):
        self.update_have_jack()
        self.update_have_queen()
        self.update_have_king()
        self.update_value()


if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)