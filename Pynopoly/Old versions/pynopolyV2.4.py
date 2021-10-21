#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Sep 21 17:00:40 2021

@author: sam
"""
import random as rd# importing random as rd
import csv

active_player = 1 # active player is a global variable which is updated through the player_turn function

print("welcome to pynopoly(v2.0)")



#making list from CSV file containing property data property_data3.csv
with open('property_data3.csv', newline = '') as f:
    reader = csv.reader(f)
    squares = list(reader)
    
#defining chance cards and commuity chest, -1 = NA (it will call a function or not do anything) 
chance_cards = [["Advance to Trafalgar Square. If you pass Go, collect £200", 200, 24],
                ["Advance to Go (Collect £200)",200,0],
                ["Advance to Mayfair",0,39],
                ["Advance to Pall Mall. If you pass Go, collect £200", 200, 11],
                ["Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled",-1,-1],
                ["Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled",-1,-1],
                ["Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",-1,-1],
                ["Bank pays you dividend of £50", 50, 0],
                ["Get Out of Jail Free",-1,-1],
                ["Go Back 3 squaresaces",-1,-1],
                ["Go to Jail. Go directly to Jail, do not pass Go, do not collect £200",-1,-1],
                ["Make general repairs on all your property. For each house pay £25. For each hotel pay £100",-1,-1],
                ["squareseeding fine £15",-1,-1],
                ["Take a trip to Kings Cross Station. If you pass Go, collect £200",200,35],
                ["You have been elected Chairman of the Board. Pay each player £50",-1,-1],
                ["Your building loan matures. Collect £150",-1-1,],
            ]

community_chest =[["Advance to Go (Collect £200)", 200, 0],
                  ["Go to Jail. Go directly to jail, do not pass Go, do not collect £200", 10, -1],
                  ["Bank error in your favour. Collect £200", 200 , -1],
                  ["Doctor’s fee. Pay £50", -50, -1],
                  ["From sale of stock you get £50", 50, -1],
                  ["Get Out of Jail Free", -1,-1],
                  ["Holiday fund matures. Receive £100", 100, -1],
                  ["Income tax refund. Collect £20", 20, -1],
                  ["It is your birthday. Collect £10 from every player", -1, -1],
                  ["Life insurance matures. Collect £100", 100, -1],
                  ["Pay hosquaresital fees of £100", -100, -1],
                  ["Pay school fees of £50", -50, -1],
                  ["Receive £25 consultancy fee", -25, -1],
                  ["You are assessed for street repairs. £40 per house. £115 per hotel", -1, -1],
                  ["You have won second prize in a beauty contest. Collect £10", 10, -1],
                  ["You inherit £100", 100, -1]
            ]

#shuffling the chance and community chest cards
#rd.shuffle(chance_cards)
#rd.shuffle(community_chest)

#--------------------functions--------------------------

#rolls two dice and creates the total
def roll(active_playerx):
    die1 = rd.randint(1,6)
    die2 = rd.randint(1,6)
    total = die1 + die2
    #player_name = player[active_player][0]
    print(player_name + ", you rolled a ", die1, " and a ", die2, "totaling", total)
    return die1, die2, total

def double(die1, die2):
    if die1 == die2:
        print("double!!!")
        
        
        
        
# ------------------------------------------------------temporary funtion that assigns all purchasable properties to player 1
"""
def prop_4_player1():
    for i in squares:
        if i[4] == "bank":
            i[4] = 1
    print(squares)
 """
# ------------------------------------------------------temporary funtion that assigns all purchasable properties to player 1



#changes the owner of the property to the player no. 
def property_transfer(player_no, prop_name):
    print("Player no", player_no, "and property no", prop_name)
    for i in squares:
        if prop_name == i[1]:
            print(i[1],i[4])
            i[4] = player_no
            print("the new owner is ", i[4])

#creates the list af data for each player
def assign_player_data():
    player = []
    
    no_of_players = int(input("how many players do you want? "))
    print(no_of_players)
    no_of_players += 1 #add banker as player0
    
    
    for i in range(no_of_players):
        if i == 0:
            player.append(["banker"])
            player[i].append("NA")#assigning piece to player
            player[i].append(20580-(1500*(no_of_players-1)))#assigning balance to banker
            player[i].append(0)# position before rolling dice (Go)
            player[i].append(False) #get out of jail free card bool
            player[i].append(False)#in jail bool
        else:
            player.append([input("Player's name: ")])
            x = int(input("choose a piece 1 = 🚗 | 2 = 👞 "))
            player[i].append(x)#assigning piece to player
            player[i].append(1500)#assigning balance to player
            player[i].append(0)# position before rolling dice (Go)
            player[i].append(True) #get out of jail free card bool
            player[i].append(False)#in jail bool
    
    return player

#gets the card, selects top card reads it and puts it at the bottom of the deck 
def cards(card_type):
    card = card_type[0]
    print("moving top card to bottom of deck")
    card_type.append(card_type.index(card))
    card_type.pop(0)


    
#--------------------------------------------------------- splitting out the check_balance function into three functions....

def check_balance1(player_no, cost, prop_n, transaction_type):
    balance = int(player[player_no][2])
    cost = abs(int(cost))
    player_name = player[player_no][0]
    if balance >= cost:
        print(player_name, "You have £" + str(balance) + ". You have sufficient funds to continue with this transaction.")
        if transaction_type == "rent":
            pay_rent(player_no, cost, balance, player[player_no][3])
        else:
            purchase_prop(player_no, cost, prop_n, balance)
        
    else:
        print("You appear not to have enough funds in your bank account to complete this transaction.")

def purchase_prop(player_no, prop_price, prop_n, balance):
    purchase = input()
    if purchase == "y":
        landlord_balance = player[0][2]
        print("debit", prop_price, "from", balance)
        print("new balance is £", balance - prop_price)
        player[player_no][2] = balance - prop_price
        property_transfer(player_no, prop_n)
        print("new player balance is:", player[player_no][2])
        player[0][2] = landlord_balance + prop_price
        print("banks balance is now: £", player[0][2])
    else:
        print("You chose to pass on the purchase.")
    
def pay_rent(player_no, cost, balance, square_no):
    print("is this an int? ", square_no)
    rent = abs(cost)
    tenant_balance = balance
    landlord = int(squares[4][4])
    if squares[square_no][4] == "NA":
        landlord = 0
    else:
        landlord = int(squares[square_no][4])
        
    landlord_balance = player[int(squares[square_no][4])][2]
    print("debit", rent, "from", "player", player_no, "s", tenant_balance)
    print("credit", rent, "to", "player", landlord, "s", landlord_balance)
    print("new balance is £", balance - rent)
    player[player_no][2] = balance - rent
    player[landlord][2] = landlord_balance + rent
    print("new player balance is:", player[player_no][2])
    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------



#searches property availability and if not calls the functions to 
def prop_available(square_no, player_no):
    prop_name = squares[square_no][1]
    print("squares[square no][4], is ", squares[square_no][4]) # who owns the square you are on
    print("squares[square_no][0] is ", squares[square_no][0]) # any property without NA can be bought or if already bought, will charge you rent
    if squares[square_no][4] == '0' and squares[square_no][0] == "NA": # this means Go, Community Chest, Income Tax, Chance, Just Visiting Jail, Community Chest, Free Parking, Chance, Go To Jail, Community Chest, Chance, Super Tax
    #Unique squares number 8 and are chronologically: Go, community_chest, tax, chance, jail, free_parking, chance, go_to_jail
        print("you have landed on a square which is not a property you can buy")
        if squares[square_no][1] == "COMMUNITY CHEST":
                
            input("press any key to pick the COMMUNITY CHEST card")
            print(community_chest[0][0])
            if community_chest[0][0] == "Advance to Go (Collect £200)":
                advance_to_go(player_no)
                cards(community_chest)
            elif community_chest[0][0] == "Go to Jail. Go directly to jail, do not pass Go, do not collect £200":
                go_to_jail()
                cards(community_chest)
            else:
                print("any community chest cards other than advance to GO!")
        
        elif squares[square_no][1] == "Just Visiting Jail":
                print("just visiting jail")
                
        elif squares[square_no][1] == "INCOME TAX":
                input("Income Tax!")
                pay_rent(player_no, -200, player[player_no][2], square_no)
                
        elif squares[square_no][1] == "CHANCE":
            input("press Enter to pick the CHANCE card")
            print(chance_cards[0][0])
            advance_to_trafalgar(player_no)
            cards(chance_cards)
                
        elif squares[square_no][1] == "Just Visiting Jail":
            print("Just visiting jail!!!")
                
        elif squares[square_no][1] == "FREE PARKING":
            print("You landed on Free Parking!")
            #call free_parking funtion which checks the amount of money, prints it out and debits it to the player account
                
        elif squares[square_no][1] == "GO TO JAIL":
            print("Go directly to jail!")
            go_to_jail()
        
        
    elif squares[square_no][4] == '0' and squares[square_no][0] != "NA":  # this means property is owned by the bank and for sale
        print("you have landed on property which is owned by the bank and is for sale")
        prop_price = squares[square_no][3]
        print(prop_name, "is unowned. It is available for £", prop_price + ".")
        check_balance1(player_no, prop_price, prop_name, "purchase")
        
    elif active_player == squares[square_no][4]: # you have landed on your own property
        print("This property belongs to you. Welcome home!")

    elif active_player != squares[square_no][4]:
            rent_without_houses = 5
            no_house = int(squares[square_no][11])
            new_val = rent_without_houses + no_house
            rent = abs(int(squares[square_no][new_val]))
            print(rent)
            print(no_house)
            print(new_val)
            print("rent! Checking if you have £" + str(rent))
            check_balance1(player_no, rent, squares[square_no][1], "rent")
    return player_no


def advance_to_go(player_no):
    current_square = player[player_no][3] 
    virtual_die = 40 - current_square # making up a false die to transport player to GO! depending on which square you are on, using new_square_cal
    new_square_cal(player_no, virtual_die, 0) # using the virtual die and 0 to get to GO!
    
def advance_to_trafalgar(player_no):
    current_square = player[player_no][3]
    virtual_die = 24 - current_square
    if virtual_die < 0:
        virtual_die = 40 - current_square + 24 
    else:
        virtual_die = 24 - current_square
    new_square_cal(player_no, virtual_die, 0)
    prop_available(24, player_no)



def go_to_jail():
    in_jail = True
    new_player_pos = 10
    player[active_player][3] = new_player_pos
    if player[active_player][4] == True:
        get_out_of_jail_use = input("you have a get out of jail card do you wish to use it (y/n)")
        if get_out_of_jail_use == "y":
            in_jail = False
            print("Just visiting...")
            player[active_player][4] = False
        else:
            in_jail = True
    player[active_player][5] = in_jail
                

    
# calculates the new square value 
def new_square_cal(player_no, die1, die2):
    total = die1 + die2
    new_player_pos = player[player_no][3] + total
    
    if new_player_pos > 39:
        subtracter = 40 - player[player_no][3]
        new_pos = total - subtracter
        print("new_position:", new_pos)
        player[player_no][3] = new_pos
        make_go_payment(player_no) # When you go past GO! or when you land on GO! then collect £200
    else:
        print("new_position:", new_player_pos)
        player[player_no][3] = new_player_pos
    
    double(die1, die2)
    return player[player_no][3]



    
#this function to be called when the active player has completed his move(s)
def player_turn(player_no, total_players, die1, die2):
    player_turn = 1
    print("total_players: ", total_players)
    if player_no == total_players-1:
        if die1 == die2:
            player_turn = player_no
            print("active player is the last player in 'player' list. Double means active player doesn't change")
        else:
            player_turn = 1
            print("active player is the last player in 'player' list. Active player updates to 1")
    else:
        if die1 == die2:
            player_turn = player_no
            print("active player is not last on player list. Double thrown so active player does not change")
        else:
            player_turn += 1
            print("active player is not last on player list. Adds 1 to active player value.")
    active_player = player_turn
    print("the active player is: ", player[active_player][0])
    return active_player



def make_go_payment(player_no):
    if player[player_no][3] == 0:
        print("Congratulations you landed on Go. You just collected £200")
    else:
        print("You passed Go. You just collected £200")
    player[player_no][2] += 200 # active customer balance credited
    player[0][2] -= 200 # bank balance debited 
    print("your new player balance is: £", player[player_no][2])
    
    
#-------------------end of funtions-----------------  

    
    
    
player = assign_player_data()#sets a global variable from the assign_player_data function
print(player)





while True:
    #print(player)
    player_name = player[active_player][0]
    move = input(player_name + ", Press Enter To Roll")
    roll_dice = roll(active_player)
    new_square = new_square_cal(active_player, roll_dice[0], roll_dice[1])
    #new_square = new_square_cal(active_player, 0, 36)
    active_player = player_turn(prop_available(new_square, active_player), len(player), roll_dice[0], roll_dice[1])
    print(player)