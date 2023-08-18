from classes.casino import Player
from classes.games import Blackjack

p1 = Player("Cameron", chips=25)
p2 = Player("Hayley")
p3 = Player("Rando")

game = Blackjack()
game.players.append(p1)
game.players.append(p2)
game.players.append(p3)
game.players

while True:
    game.play()
    if input("Play again? ").upper().startswith("N"):
        break