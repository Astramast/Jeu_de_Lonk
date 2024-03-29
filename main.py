from Deck.py import Deck
from Player.py import Player


def update_table(list_players, players_army_choices):
	for player_number in range(len(list_players)):
		print("L'armée du joueur", player_number + 1, "est",
			list_players[player_number].armies[players_army_choices[player_number]])

def create_armies(list_players):
	for each_player_number in range(len(list_players)):
		print("Tour joueur ", each_player_number + 1)
		done = False
		while not done:
			print("Vos cartes : ", list_players[each_player_number].get_player_hand())
			print("Vos armées : ")
			for i in range(5):
				print("Armée", i + 1, list_players[each_player_number].get_armies()[i])
			input_modify = input("Voulez-vous retirer une carte ou ajouter une carte ? (0/1) : ")
			while not input_modify.isdigit():
				input_modify = input("Voulez-vous retirer une carte ou ajouter une carte ? (0/1) : ")
			player_army_choice = input("Choisissez une armée (1 à 5) : ")
			while (not player_army_choice.isdigit()) or (not 0 < int(player_army_choice) < 6):
				player_army_choice = input("Choisissez une armée (1 à 5) : ")
			player_card_choice = input("Choisissez une carte (1 à 13) : ")
			while not player_card_choice.isdigit():
				player_card_choice = input("Choisissez une carte (1 à 13) : ")
			input_modify = bool(int(input_modify))
			player_army_choice = int(player_army_choice)
			player_card_choice = int(player_card_choice)
			if input_modify:
				list_players[each_player_number].add_card_to_army(player_army_choice - 1, player_card_choice)
			else:
				list_players[each_player_number].remove_card_from_army(player_army_choice - 1, player_card_choice)
			if len(list_players[each_player_number].get_player_hand()) == 0:
				seemsgood = True
				for army_number in range(5):
					if list_players[each_player_number].get_army_amount(army_number) == 0:
						seemsgood = False
					elif list_players[each_player_number].get_army_amount(army_number) == 1 \
							and list_players[each_player_number].army_have_jack(army_number):
						seemsgood = False
					if list_players[each_player_number].army_have_king(army_number) and \
							list_players[each_player_number].army_have_queen(army_number):
						seemsgood = False
						print("Les Rois (13) ne peuvent pas être dans la même armée qu'un Fou (12) !")
				if seemsgood:
					done = bool(int(input("Avez-vous terminé ? (0 : non/1 : oui) : ")))
				else:
					print("Il faut au moins une carte dans chaque armée et les Mages (11) ne peuvent être seuls !")

def main():
	players = []
	lonk_deck = deck.Deck()
	lonk_deck.shuffle()
	player_number = 0
	while player_number > 5 or player_number < 2:
		print("Le nombre de joueurs doit être entre 2 et 5")
		player_number = input("Nombre de Joueurs : ")
		while not player_number.isdigit():
			print("Veuillez entrer un nombre de 2 à 5")
			player_number = input("Nombre de Joueurs : ")
		player_number = int(player_number)
	for _ in range(player_number):
		players.append(player.Player())
	for _ in range(10):
		for each_player in players:
			each_player.add_card(lonk_deck.take_top_card())
	create_armies(players)
	for i in range(5):
		play_round(players, player_number)


if __name__ == "__main__":
	main()
