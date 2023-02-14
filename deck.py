from random import shuffle
from card.py import Card, LonkCard


class Deck:
	def __init__(self, cards_list=[]):
		self.cards = cards_list
		self.cards.sort()
		self.amount = len(self.cards)

	@classmethod
	def generate(cls, repetitions=4, values=13):
		param = [Card(i + 1) for i in range(values)]*repetitions
		return cls(param)

	def getCards(self):
		return self.cards

	def getAmount(self):
		return self.amount

	def addCard(self, card):
		self.cards.append(card)
		self.update_value()

	def removeCard(self, card_value):
		for card in self.cards:
			if 
			self.update_value()
		else:
			raise ValueError("This card is not in the deck")

	def takeTopCard(self):
		ret_val = self.cards.pop(0)
		self.update_value()
		return ret_val

	def sort_deck(self):
		self.cards.sort()

	def shuffle(self):
		shuffle(self.cards)

	def have_king(self):
		return self.have_card(13)

	def have_queen(self):
		return self.have_card(12)

	def have_jack(self):
		return self.have_card(11)

	def have_card(self, value):
		return value in self.cards

	def update_value(self):
		self.value = sum(self.cards)

	def __repr__(self):
		return str(self.cards)

if __name__ == "__main__":
	deck = Deck()
	print(deck)
