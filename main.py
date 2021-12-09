import deck
import player


def create_armies(list_players):
    for each_player_number in range(len(list_players)):
        print("Tour joueur ", each_player_number + 1)
        done = 0
        while not done:
            print("Vos cartes : ", list_players[each_player_number].get_player_hand())
            print("Vos armées : ")
            for i in range(5):
                print("Armée", i + 1, list_players[each_player_number].get_player_armies()[i].cards)
            input_modify = bool(input("Voulez-vous retirer une carte ou ajouter une carte ? (0/1) : "))
            player_army_choice = int(input("Choisissez une armée (1 à 5) : "))
            player_card_choice = int(input("Choisissez une carte (1 à 13) : "))
            if input_modify:
                list_players[each_player_number].add_card_to_army(player_army_choice - 1, player_card_choice)
            else:
                list_players[each_player_number].remove_card_from_army(player_army_choice - 1, player_card_choice)
            if len(list_players[each_player_number].get_player_hand()) == 0:
                seemsgood = True
                for army_number in range(5):
                    if len(list_players[each_player_number].armies[army_number].cards) == 0:
                        seemsgood = False
                    elif len(list_players[each_player_number].armies[army_number].cards) == 1 \
                            and list_players[each_player_number].armies[army_number].cards == [11]:
                        seemsgood = False
                if seemsgood:
                    done = bool(int(input("Avez-vous terminé ? (0 : non/1 : oui) : ")))
                else:
                    print("Il faut au moins une carte dans chaque armée et les mages (11) ne peuvent être seuls !")


def play_round(list_players, number_players):
    players_army_choices = []
    for player_number in range(number_players):
        players_army_choices.append(
            int(input("Joueur " + str(player_number + 1)+ ", choisissez une armée à jouer (1 à 5) : ")))
        print("Le joueur", player_number + 1, "joue une armée de",
              len(list_players[player_number].armies[players_army_choices[player_number]].cards), "cartes2")
    for player_number in range(len(players_army_choices)):
        print("L'armée du joueur", player_number + 1, "est",
              list_players[player_number].armies[players_army_choices[player_number]].cards)
        list_players[player_number].armies[players_army_choices[player_number]].update_have_king()
        list_players[player_number].armies[players_army_choices[player_number]].update_have_queen()
        list_players[player_number].armies[players_army_choices[player_number]].update_have_jack()



def main():
    players = []
    lonk_deck = deck.Deck()
    lonk_deck.shuffle_deck()
    player_number = int(input("Nombre de Joueurs : "))
    while 5 < player_number < 2:
        print("Le nombre de joueurs doit être entre 2 et 5")
        player_number = int(input("Nombre de Joueurs : "))
    for _ in range(player_number):
        players.append(player.Player())
    for _ in range(10):
        for each_player in players:
            each_player.hand.add_card(lonk_deck.take_top_card())
    create_armies(players)
    play_round(players, player_number)

if __name__ == "__main__":
    main()
