# Imports and global variables

import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')

values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

playing = True


class Card:

	def __init__(self,suit,rank):

		self.suit = suit
		self.rank = rank

	def __str__(self):

		return f"{self.rank} of {self.suit}"


class Deck:

	def __init__(self):

		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))


	def __str__(self):

		self.deck_comp = ''

		for card in self.deck:
			self.deck_comp += '\n'+card.__str__()

		return 'The deck has: '+ self.deck_comp


	def shuffle_deck(self):
		random.shuffle(self.deck)


	def deal(self):
		return self.deck.pop()


class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace_count = 0


	def add_card(self,card):
		self.cards.append(card)
		self.value = self.value + values[card.rank]
		if card.rank == 'Ace':
			self.ace_count += 1


	def adjust_for_aces(self):
		while self.value > 21 and self.ace_count:
			self.value -= 10
			seld.ace_count -= 1


class Chips:

	def __init__(self,total=100):
		self.total = total
		self.bet = 0


	def win_bet(self):
		self.total += self.bet


	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):

	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet?"))
		except Exception:
			print('Sorry, a bet must be an integer!')
		else:
			if chips.bet > chips.total:
				print(f"Sorry, your bet can't exceed {chips.total}")
			else:
				break


def hit(deck,hand):

	hand.add_card(deck.deal())
	hand.adjust_for_aces()


def hit_or_stand(deck,hand):

	global playing

	while True:
		x = input("Would you like to take a Hit or Stand? Enter 'h' or 's' ")

		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("Player stands. Dealer is playing.")
			playing = False
		else:
			print("Sorry, please try again.")
			continue
		break


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
 

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:

    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    
    # Create & shuffle the deck, deal two cards to each player

    play_deck = Deck()
    play_deck.shuffle_deck()

    player_hand = Hand()
    player_hand.add_card(play_deck.deal())
    player_hand.add_card(play_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(play_deck.deal())
    dealer_hand.add_card(play_deck.deal())
        
    # Set up the Player's chips
    
    players_chip = Chips(1000)
    # Prompt the Player for their bet

    take_bet(players_chip)
    # Show cards (but keep one dealer card hidden)

    show_some(player_hand,dealer_hand)
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        
        hit_or_stand(play_deck,player_hand)
        # Show cards (but keep one dealer card hidden)
 
        show_some(player_hand,dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
        	player_busts(player_hand,dealer_hand,players_chip)
        	break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
    	while dealer_hand.value < 17:
    		hit(play_deck,dealer_hand)   
    
        # Show all cards
    	show_all(player_hand,dealer_hand)
        # Run different winning scenarios
    	if dealer_hand.value >21:
        	dealer_busts(player_hand,dealer_hand,players_chip)
        	break
    	elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,players_chip)
    	elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,players_chip)
    	else:
        	push(player_hand,dealer_hand)
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",players_chip.total)
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    #    break
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break