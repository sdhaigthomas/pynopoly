#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Sep 21 17:00:40 2021

@author: sam
"""
import random as rd# importing random as rd
import csv

active_player = 0 # active player is a global variable which is updated through the player_turn function

print("welcome to pynopoly(v2.0)")



#making list from CSV file containing property data property_data3.csv
with open('property_data3.csv', newline = '') as f:
    reader = csv.reader(f)
    squares = list(reader)
    
#defining chance cards and commuity chest, -1 = NA (it will call a function or not do anthing) 
chance_cards = [["Advance to Go (Collect £200)",200,0],
                ["Advance to Trafalgar Square. If you pass Go, collect £200",200,24],
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

community_chest = [["Go to Jail. Go directly to jail, do not pass Go, do not collect £200", 10, -1],
                  ["Advance to Go (Collect £200)", 200, 0],
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
rd.shuffle(chance_cards)
rd.shuffle(community_chest)

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
    
    for i in range(no_of_players):
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
    print(card[0])
    if card[0] ==  "Go to Jail. Go directly to jail, do not pass Go, do not collect £200":
        go_to_jail()
    
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
            pay_rent(player_no, cost, prop_n, balance)
        else:
            purchase_prop(player_no, cost, prop_n, balance)
        
    else:
        print("You appear not to have enough funds in your bank account to complete this transaction.")

def purchase_prop(player_no, prop_price, prop_n, balance):
    purchase = input()
    if purchase == "y":
        print("debit", prop_price, "from", balance)
        print("new balance is £", balance - prop_price)
        player[player_no][2] = balance - prop_price
        property_transfer(player_no, prop_n)
        print("new player balance is:", player[player_no][2])
    else:
        print("You chose to pass on the purchase.")
    
def pay_rent(player_no, rent, prop_n, balance):
    rent = abs(rent)
    print("debit", rent, "from", balance)
    print("new balance is £", balance - rent)
    player[player_no][2] = balance - rent
    print("new player balance is:", player[player_no][2])
    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------



   
# def check_balance(player_no, prop_price, prop_n):
#     balance = int(player[player_no][2])
#     prop_price = int(prop_price)
#     player_name = player[player_no][0]
#     #print(player_name, "the property you want to purchase is", prop_price )
#     if balance >= prop_price:
#         print(player_name, "You have £" + str(balance) + ". Press (Y / N) to purchase")
#         purchase = input()
#         if purchase == "y":
#             print("debit", prop_price, "from", balance)
#             print("new balance is £", balance - prop_price)
#             player[player_no][2] = balance - prop_price
#             property_transfer(player_no, prop_n)
#             print("new player balance is:", player[player_no][2])
#         else:
#             print("You chose to pass on the purchase.")
#     else:
#         print("You appear not to have enough funds in your bank account to make this purchase.")


#searches property availability and if not calls the functions to 
def prop_available(square_no, player_no):
    prop_name = squares[square_no][1]
    if squares[square_no][4] == 'bank':
        prop_price = squares[square_no][3]
        print(prop_name, "is unowned. It is available for £", prop_price + ".")
        check_balance1(player_no, prop_price, prop_name, "purchase")
        
    else:
        if squares[square_no][4] == "NA":
            if squares[square_no][1] == "GO":
                print("You receive £" + str(squares[square_no][5]))
            elif squares[square_no][1] == "COMMUNITY CHEST":
                
                input("press any key to pick the COMMUNITY CHEST card")
                cards(community_chest)
                
            elif squares[square_no][1] == "INCOME TAX":
                input("Income Tax")
                #call income_tax funtion
                
            elif squares[square_no][1] == "CHANCE":
                input("press Enter to pick the CHANCE card")
                cards(chance_cards)
                
            elif squares[square_no][1] == "Just Visiting Jail":
                print("Just visiting jail!!!")
                
            elif squares[square_no][1] == "FREE PARKING":
                print("Congratulations you win the money in the middle!!!")
                #call free_parking funtion which checks the amount of money, prints it out and debits it to the player account
                
            elif squares[square_no][1] == "GO TO JAIL":
                print("Go directly to jail!")
                go_to_jail()
        elif active_player == squares[square_no][4]:
            print("This property belongs to you. Welcome home!")

        else:
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

def go_to_jail():
    in_jail = True
    new_player_pos = 10
    player[active_player][3] = new_player_pos
    if player[active_player][4] == True:
        get_out_of_jail_use = input("you have a get out of jail card do you wish to use it (y/n)")
        if get_out_of_jail_use == "y":
            in_jail = False
            player[active_player][4] = False
        else:
            in_jail = True
    player[active_player][5] = in_jail
                
                
# you receive £400

    
# calculates the new square value 
def new_square_cal(player_no, die1, die2):
    total = die1 + die2
    new_player_pos = player[player_no][3] + total
    
    if new_player_pos > 39:
        subtracter = 40 - player[player_no][3]
        new_pos = total - subtracter
        print("new_position:", new_pos)
        player[player_no][3] = new_pos
    else:
        print("new_position:", new_player_pos)
        player[player_no][3] = new_player_pos
    
    double(die1, die2)
    return player[player_no][3]
    
#this function to be called when the active player has completed his move(s)
def player_turn(player_no, total_players, die1, die2):
    player_turn = 0
    
    if player_no == total_players - 1:
        if die1 == die2:
            player_turn = player_no
            #print("active player is the last player in 'player' list. Double means active player doesn't change")
        else:
            player_turn = 0
            #print("active player is the last player in 'player' list. Active player updates to 0")
    else:
        if die1 == die2:
            player_turn = player_no
            #print("active player is not last on player list. Double thrown so active player does not change")
        else:
            player_turn =+ 1
            #print("active player is not last on player list. Adds 1 to active player value.")
    active_player = player_turn
    print("the active player is: ", player[active_player][0])
    return active_player


#-------------------end of funtions-----------------  

    
    
    
player = assign_player_data()#sets a global variable from the assign_player_data function
print(player)





while True:
    #print(player)
    player_name = player[active_player][0]
    move = input(player_name + ", Press Enter To Roll")
    roll_dice = roll(active_player)
    new_square = new_square_cal(active_player, roll_dice[0], roll_dice[1])
    #new_square = new_square_cal(active_player, 1, 1)
    active_player = player_turn(prop_available(new_square, active_player), len(player), roll_dice[0], roll_dice[1])
    print(player)