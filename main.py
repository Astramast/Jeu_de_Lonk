import deck
import player


def update_table(list_players, players_army_choices, update_decks=True):
    for player_number in range(len(list_players)):
        print("L'armée du joueur", player_number + 1, "est",
              list_players[player_number].armies[players_army_choices[player_number]].cards)
        if update_decks:
            list_players[player_number].armies[players_army_choices[player_number]].update_have_king()
            list_players[player_number].armies[players_army_choices[player_number]].update_have_queen()
            list_players[player_number].armies[players_army_choices[player_number]].update_have_jack()


def create_armies(list_players):
    for each_player_number in range(len(list_players)):
        print("Tour joueur ", each_player_number + 1)
        done = 0
        while not done:
            print("Vos cartes : ", list_players[each_player_number].get_player_hand())
            print("Vos armées : ")
            for i in range(5):
                print("Armée", i + 1, list_players[each_player_number].get_player_armies()[i].cards)
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
                    if len(list_players[each_player_number].armies[army_number].cards) == 0:
                        seemsgood = False
                    elif len(list_players[each_player_number].armies[army_number].cards) == 1 \
                            and list_players[each_player_number].armies[army_number].cards == [11]:
                        seemsgood = False
                    list_players[each_player_number].armies[army_number].fullupdate()
                    if list_players[each_player_number].armies[army_number].update_have_king() and \
                            list_players[each_player_number].armies[army_number].update_have_queen():
                        seemsgood = False
                        print("Les Rois (13) ne peuvent pas être dans la même armée qu'un Fou (12) !")
                if seemsgood:
                    done = bool(int(input("Avez-vous terminé ? (0 : non/1 : oui) : ")))
                else:
                    print("Il faut au moins une carte dans chaque armée et les Mages (11) ne peuvent être seuls !")


def play_jacks(list_players, number_players, players_army_choices):
    for player_number in range(number_players):
        if list_players[player_number].armies[players_army_choices[player_number]].have_jack:
            print('entré', player_number)
            list_players[player_number].armies[players_army_choices[player_number]], \
                list_players[(player_number - 1) % number_players].armies[
                players_army_choices[(player_number - 1) % number_players]] \
                = list_players[(player_number - 1) % number_players].armies[
                      players_army_choices[(player_number - 1) % number_players]], \
                list_players[player_number].armies[players_army_choices[player_number]]
            list_players[(player_number - 1) % number_players]. \
                armies[players_army_choices[(player_number - 1) % number_players]].have_jack = False
            update_table(list_players, players_army_choices, update_decks=False)


def play_round(list_players, number_players):
    players_army_choices = []
    for player_number in range(number_players):
        player_choice = int(input("Joueur " + str(player_number + 1)+ ", choisissez une armée à jouer (1 à 5) : "))
        players_army_choices.append(player_choice - 1)
        print("Le joueur", player_number + 1, "joue une armée de",
              len(list_players[player_number].armies[players_army_choices[player_number]].cards), "cartes")

    update_table(list_players, players_army_choices, update_decks=True)
    play_jacks(list_players, number_players, players_army_choices)

    kings_on_board = False
    queens_on_board = False
    for player_number in range(number_players):
        if list_players[player_number].armies[players_army_choices[player_number]].have_king:
            kings_on_board = True
        elif list_players[player_number].armies[players_army_choices[player_number]].have_queen:
            queens_on_board = True

    if kings_on_board:
        if queens_on_board:
            for player_number in range(number_players):
                if not list_players[player_number].armies[players_army_choices[player_number]].have_queen:
                    list_players[player_number].armies[players_army_choices[player_number]].value = 0
        else:
            for player_number in range(number_players):
                if not list_players[player_number].armies[players_army_choices[player_number]].have_king:
                    list_players[player_number].armies[players_army_choices[player_number]].value = 0
    elif queens_on_board:
        for player_number in range(number_players):
            if not list_players[player_number].armies[players_army_choices[player_number]].have_queen:
                list_players[player_number].armies[players_army_choices[player_number]].value = \
                    list_players[player_number].armies[players_army_choices[player_number]].value - \
                    12 * list_players[player_number].armies[players_army_choices[player_number]].cards.count(12)

    players_values = []
    for player_number in range(number_players):
        players_values.append((player_number,
                               list_players[player_number].armies[players_army_choices[player_number]].value))
    players_values.sort(key=lambda t: t[1], reverse=True)
    winner_value = players_values[0][1]
    round_winners = []
    for results in players_values:
        if results[1] == winner_value:
            round_winners.append(results[0])
    for winner in round_winners:
        list_players[winner].points += 1


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
            each_player.hand.add_card(lonk_deck.take_top_card())
    create_armies(players)
    for i in range(5):
        play_round(players, player_number)


if __name__ == "__main__":
    main()
