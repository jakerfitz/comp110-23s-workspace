import random

def blackjack():
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    def deal(hand):
        card = deck.pop()
        if card == 'A':
            if sum(hand) + 11 > 21:
                hand.append(1)
            else:
                hand.append(11)
        elif card in ['K', 'Q', 'J']:
            hand.append(10)
        else:
            hand.append(card)

    def total(hand):
        return sum(hand)

    def play_again():
        again = input("Do you want to play again? (Y/N) : ")
        if again.lower() == 'y':
            player_hand.clear()
            dealer_hand.clear()
            deck.extend([2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4)
            random.shuffle(deck)
            game()
        else:
            print("Bye!")
            exit()

    def game() -> None:
        deal(player_hand)
        deal(dealer_hand)
        deal(player_hand)
        deal(dealer_hand)

        while True:
            print(f"Player Hand: {player_hand} Total: {total(player_hand)}")
            print(f"Dealer Hand: [{dealer_hand[0]}, X]")

            choice = input("Do you want to [H]it or [S]tand? ").lower()
            
            if choice == 'h':
                deal(player_hand)
                if total(player_hand) > 21:
                    print(f"Player Hand: {player_hand} Total: {total(player_hand)}")
                    print("Busted! You lose!")
                    play_again()
                    
            elif choice == 's':
                while total(dealer_hand) < 17:
                    deal(dealer_hand)

                print(f"Player Hand: {player_hand} Total: {total(player_hand)}")
                print(f"Dealer Hand: {dealer_hand} Total: {total(dealer_hand)}")

if __name__ == "__main__":
    blackjack()
