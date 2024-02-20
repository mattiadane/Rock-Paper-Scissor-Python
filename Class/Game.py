import random
from Class.Player import Player
from Class.BotPlayer import BotPlayer


class Game:

    def __init__(self):
        self.nManche = self.choice_number_manche()
        print("Game Launched\nThe first to win 3 rounds wins, the maximum number of rounds is %s" % str(self.nManche))
        self.player = self.generate_player()
        self.botPlayer = BotPlayer("Bot")
        self.game()

    def generate_player(self):
        print("Enter the player's name\n")
        name = str(input())
        while name == "":
            name = str(input())
        return Player(name)

    def choose_who_starts(self):
        return random.randint(0, 1)

    def choice_number_manche(self):
        return random.randint(4,19)

    def game(self):
        number = self.choose_who_starts()
        win_manche = ""
        count_manche = 0
        count1 = 0
        count2 = 0
        winner = ""
        while winner == "" or count_manche < self.nManche:
            if number == 1:
                self.play_turn(self.player, self.botPlayer)
                number -= 1
            else:
                self.play_turn(self.botPlayer, self.player)
                number += 1

            if win_manche == self.botPlayer:
                count2 += 1
            else :
                count1 += 1

            if count1 == 3:
                winner = self.player
            elif count2 == 3:
                winner = self.botPlayer

            count_manche += 1

    def play_turn(self, player, next_player):
        print("It's %s's turn" % player)
        if isinstance(player, BotPlayer):
            print("SI")
        elif isinstance(player, Player):
            print("NO")

