from .casino import Deck

class Blackjack():
    card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    stake_return = {
        "loss": lambda stake: 0,
        "push": lambda stake: stake,
        "blackjack": lambda stake: stake + int(stake * 1.5),
        "win": lambda stake: stake + stake
    }

    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.players_hands = {}
        self.players_bets = {}

    def play(self):
        def get_hand_score(hand):
            score = 0
            aces = 0
            # get_score
            for card in hand:
                if card.rank == 'A':
                    aces += 1
                score += self.card_values[card.rank]
                while score > 21 and aces:
                    aces -= 1
                    score -= 10
            return score

        def get_hand_result(player_hand, dealer_hand):
            player_score = get_hand_score(player_hand)
            dealer_score = get_hand_score(dealer_hand)

            player_blackjack = player_score == 21 and len(player_hand) == 2
            dealer_blackjack = dealer_score == 21 and len(dealer_hand) == 2

            player_bust = player_score > 21
            dealer_bust = dealer_score > 21

            if player_bust:
                return 'loss' if not dealer_bust else 'push'
            if player_blackjack:
                return 'blackjack' if not dealer_blackjack else 'push'
            if player_score == dealer_score:
                return 'push'
            if dealer_bust or player_score > dealer_score:
                return 'win'
            if dealer_blackjack or player_score < dealer_score:
                return 'loss'

            return None

        # if input("All players added?:").upper().startswith("N"):
            # return None
        if not self.players:
            return None
        # self.setup()
        print("-- Remove Poor Players --")
        for player in self.players:
            print(player, player.chips)
            if player.chips >= 10:
                self.players_bets[player] = 10
                print(player, "kept. Can cover bet.")
            else:
                self.players.remove(player)
                print(player, "ejected. Cannot cover bet.")

        print("-- Take Bet --")
        for player in self.players:
            print("Before:", player, player.chips)
            player.chips -= 10
            print("After:", player, player.chips)

        for player in self.players:
            self.players_hands[player] = []

        # self.deal()
        for player in self.players*2:
            self.players_hands[player].append(self.deck.get_card())

        dealer_hand = []
        dealer_hand.append(self.deck.get_card())
        dealer_hand.append(self.deck.get_card())
        print("Opening Hands:")
        print('\t', "Dealer", [dealer_hand[0]])
        for name, hand in self.players_hands.items():
            print('\t', name, hand)

        # main loop, for each player
        # Hit or Stick until Stick or bust.
        print("-- Players Choices --")
        for name, hand in self.players_hands.items():
            # for _ in range(5):
            #     hand.append(Card('A', '♠'))
            while True:
                # show hand, score then hit or Stick
                score = get_hand_score(hand)
                print(name, score, hand)
                # check_bust
                if score > 21:
                    # print("Final score:", score)
                    break
                # hit_or_stick
                choice = input("[H]it or [S]tick?: ")
                if choice == "S":
                    # print("Final score:", score)
                    break
                else:
                    hand.append(self.deck.get_card())
            # Player has no more decisions. Stuck, or Bust
        # All Players have made their decisions
        # Play through the Dealer's turn
        dealer_score = get_hand_score(dealer_hand)
        print("Dealer", dealer_score, dealer_hand)
        while dealer_score < 17:
            dealer_hand.append(self.deck.get_card())
            dealer_score = get_hand_score(dealer_hand)
            print("Dealer", dealer_score, dealer_hand)

        # Get the scores any payout winners
        print("-- Resolving Bets --")
        # print(self.players_bets)
        for name, hand in self.players_hands.items():
            player_bet = self.players_bets[name]
            print(name, "Bet:", player_bet)
        
            # check if blackjack
            bet_result = get_hand_result(player_hand=hand, dealer_hand=dealer_hand)
            if bet_result:
                bet_return = self.stake_return[bet_result](player_bet)
            name.chips += bet_return

            print(name, bet_result, bet_return, name.chips)
