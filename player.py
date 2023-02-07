import deck


class Player:
	def __init__(self):
		self.hand = deck.Deck(0)
		self.armies = []
		for _ in range(5):
			self.armies.append(deck.Deck(0, 0))
		self.points = 0

	def get_player_armies(self):
		return self.armies

	def get_player_hand(self):
		return self.hand.cards

	def add_card_to_army(self, army_number, card_value):
		if card_value in self.hand.cards:
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


if __name__ == "__main__":
	player = Player()
	print(player.hand.cards)
	print(player.armies)
