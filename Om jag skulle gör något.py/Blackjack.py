import random

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]
random.shuffle(deck)

def calculate_score(hand):
    score = 0
    aces = 0

    for card, _ in hand:
        if card in ['Jack', 'Queen', 'King']:
            score += 10
        elif card == 'Ace':
            score += 11
            aces += 1
        else:
            score += int(card)

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

while True:
    player_score = calculate_score(player_card)
    dealer_score = calculate_score(dealer_card)

    print("Cards Player Has:", player_card)
    print("Score Of The Player:", player_score)
    print()

    if player_score > 21:
        print("Dealer wins (Player busted)")
        exit()
    if player_score == 21:
        print("player has blackjack")
        exit()

    choice = input('What do you want? ["play" or "stop"]: ').lower()

    if choice == "play":
        player_card.append(deck.pop())
    elif choice == "stop":
        break
    else:
        print("Invalid choice.")

while dealer_score < 17:
    dealer_card.append(deck.pop())
    dealer_score = calculate_score(dealer_card)

print("\nCards Dealer Has:", dealer_card)
print("Score Of The Dealer:", dealer_score)

if dealer_score > 21:
    print("Player wins (Dealer busted)")
elif player_score > dealer_score:
    print("Player wins")
elif dealer_score > player_score:
    print("Dealer wins")
else:
    print("It's a tie")