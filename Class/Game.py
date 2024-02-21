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
        print("Enter the player's name")
        name = str(input())
        while name == "":
            name = str(input())
        return Player(name)

    def choice_number_manche(self):
        return random.randint(4, 19)

    def game(self):
        winPrec = ""
        win_manche = ""
        count_manche = 0
        count1 = 0
        count2 = 0
        winner = ""
        primo = ""
        secondo = ""
        mossaprec = ""
        while winner == "" and count_manche < self.nManche:
            if count_manche + 1 == 1:
                primo = self.player.play(int(self.action()))
                secondo = self.botPlayer.play()
            else:
                if winPrec == self.botPlayer:
                    secondo = self.botPlayer.play()
                    while secondo == mossaprec:
                        secondo = self.botPlayer.play()
                    primo = self.player.play(int(self.action()))
                elif winPrec == self.player:
                    primo = self.player.play(int(self.action()))
                    while primo == mossaprec:
                        print("You cannot use the one that won you the previous round")
                        primo = self.player.play(int(self.action()))
                    secondo = self.botPlayer.play()
                else:
                    primo = self.player.play(int(self.action()))
                    secondo = self.botPlayer.play()

            print("Manche %s" % str(count_manche + 1))
            print("Move played by ", self.player, " : ", primo)
            print("Move played by ", self.botPlayer, " : ", secondo)
            win_manche = self.rules(primo, secondo)
            if win_manche is None:
                win_manche = "Draw"
                print("Manche ended in a draw")
            else:
                print("Manche won by %s" % win_manche)

            if win_manche == self.botPlayer:
                mossaprec = secondo
                count2 += 1
            elif win_manche == self.player:
                count1 += 1
                mossaprec = primo

            if count_manche + 1 == self.nManche:
                if count1 > count2:
                    winner = self.player
                    print("Game won by %s" % winner)
                elif count2 > count1:
                    winner = self.botPlayer
                    print("Game won by %s" % winner)
                else:
                    winner = "Draw"
                    print("Match ended in a draw")
            else:
                if count1 == 3:
                    winner = self.player
                    print("Game won by %s" % winner)
                elif count2 == 3:
                    winner = self.botPlayer
                    print("Game won by %s" % winner)

            count_manche += 1
            winPrec = win_manche

    def action(self):
        print("Press\n0 for Rock\n1 for Paper\n2 for Scissor")
        action = input()
        while (not action.isnumeric()) or (int(action) > 2 or int(action) < 0):
            if (not action.isnumeric()) or (int(action) > 2 or int(action) < 0):
                print("Bad selection, retry\n")
            action = input()
        return action

    def rules(self, primo, secondo):
        win = None
        if (primo == "Rock" and secondo == "Scissor") or (primo == "Scissor" and secondo == "Paper") or (
                primo == "Paper" and secondo == "Rock"):
            win = self.player
        elif (secondo == "Rock" and primo == "Scissor") or (secondo == "Scissor" and primo == "Paper") or (
                secondo == "Paper" and primo == "Rock"):
            win = self.botPlayer
        return win
