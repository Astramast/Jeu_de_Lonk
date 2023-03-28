from Deck.py import Deck


class Player:
	def __init__(self):
		self.hand = deck.Deck([])
		self.armies = []
		for _ in range(5):
			self.armies.append(deck.Deck([]))
		self.points = 0
		self.ready = False
		self.choice = 0

	def get_armies(self):
		return self.armies

	def get_hand(self):
		return self.hand

	def get_points(self):
		return self.points

	def get_army(self, number):
		return self.armies[number]

	def get_army_amount(self, number):
		return self.armies[number].get_amount()

	def army_have_king(self, number):
		return self.armies[number].have_king()

	def army_have_queen(self, number):
		return self.armies[number].have_queen()

	def army_have_jack(self, number):
		return self.armies[number].have_jack()

	def add_card_to_army(self, army_number, card_value):
		if self.hand.have_card(card_value):
			self.armies[army_number].add_card(card_value)
			self.hand.remove_card(card_value)
		else:
			print("Vous n'avez pas cette carte en main")

	def remove_card_from_army(self, army_number, card_value):
		if card_value in self.armies[army_number].cards:
			self.hand.add_card(card_value)
			self.armies[army_number].remove_card(card_value)
		else:
			print("Cette carte n'est pas dans l'armée")

	def is_ready(self):
		return self.ready

	def get_choice(self):
		return self.choice

	def choose(self, value):
		if value > 4:
			raise ValueError("Choice value too high")
		self.choice = value

	def add_card(self, value):
		self.hand.add_card(value)

if __name__ == "__main__":
	player = Player()
	print(player.hand)
	print(player.armies)
