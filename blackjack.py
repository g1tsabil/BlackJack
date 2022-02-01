from random import randint

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]*4

def cards_distribution(player_name):
    for elm in player_name:
        card1 = randint(0, len(deck)-1)
        remove_1 = deck.pop(card1)
        card2 = randint(0, len(deck)-1)
        remove_2 = deck.pop(card2)
        elm.append(remove_1)
        elm.append(remove_2)
        
num_players = int(input('How many players will participate? '))

if num_players > 4:
    while num_players > 4:
        print('\nThis game only allows three players!\n')
        num_players = int(input('How many players will participate? '))

player_num = 0
player_name_lst = []
while player_num != num_players:
    player = input('\nWhat is the name of the player? ')
    player_name_lst.append([player])
    player_num += 1

cards_distribution(player_name_lst)

blackjack = []
stand = []
bust = []

print('')

for elm in player_name_lst:
    print("{}'s current hand has value of {}.".format(elm[0], sum(elm[1:])))

for elm in player_name_lst:
    if (len(player_name_lst) - len(bust)) == 1:
        print('\nCongratulations {} won!'.format(elm[0]))
    else:
        while sum(elm[1:]) < 21:
            move = input('\nWould {} like to hit or stand? '.format(elm[0]))
            if move.lower() == 'hit':    
                card = randint(0, len(deck)- 1)
                elm.append(deck[card])
                deck.remove(deck[card])
                print("{}'s new hand value is {}".format(elm[0], sum(elm[1:])))
            elif move.lower() == 'stand':
                print("{}'s hand remains {}".format(elm[0], sum(elm[1:])))
                stand.append(elm)
                break
        if sum(elm[1:]) == 21:
            print ('{} got blackjack with a hand value of 21!'.format(elm[0]))
            blackjack.append(elm[0])
        elif sum(elm[1:]) > 21:
            print('{} went bust with a hand value of {}!'.format(elm[0], sum(elm[1:])))
            bust.append(elm)

highest = 0
winner = []
if len(blackjack) == 0 and len(stand) >= 1:
    for elm in stand:    
        if sum(elm[1:]) > highest:
            highest = sum(elm[1:])
            winner = list([elm[0]])
        elif sum(elm[1:]) == highest:
            winner.append(elm[0])
        else:
            None
    for elm in winner:
        print('\nCongratulations to {} for the highest hand value!'.format(elm))
elif len(blackjack) == 0 and len(stand) == 0 and len(bust) == len(player_name_lst):
    print('\nAll players went bust!')

    
    
