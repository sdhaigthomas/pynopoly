#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Sep 21 17:00:40 2021

@author: sam
"""
import random as rd# importing random as rd!
import csv

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

community_chest = [["Advance to Go (Collect £200)", 200, 0],
                  ["Bank error in your favour. Collect £200", 200 , -1],
                  ["Doctor’s fee. Pay £50", -50, -1],
                  ["Go to Jail. Go directly to jail, do not pass Go, do not collect £200", 10, -1],
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

#rolls two die and creates the total
def roll():
    die1 = rd.randint(1,6)
    die2 = rd.randint(1,6)
    total = die1 + die2
    return die1, die2, total

def double(die1, die2):
    if die1 == die2:
        print("double!!!")

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
        player[i].append(False) #get out of jail free card bool
    
    return player

#gets the card, selects top card reads it and puts it at the bottom of the deck 
def cards(card_type):
        card = card_type[0]
        print(card)
        #print(card_type)
        card_type.append(card_type.index(card))
        card_type.pop(0)
        
def check_balance(player_no, prop_price, prop_n):
    balance = int(player[player_no][2])
    prop_price = int(prop_price)
    player_name = player[player_no][0]
    #print(player_name, "the property you want to purchase is", prop_price )
    if balance >= prop_price:
        print(player_name, "You have £" + str(balance) + ". Press (Y / N) to purchase")
        purchase = input()
        if purchase == "y":
            print("debit", prop_price, "from", balance)
            print("new balance is £", balance - prop_price)
            player[player_no][2] = balance - prop_price
            property_transfer(player_no, prop_n)
            print("new player balance is:", player[player_no][2])
        else:
            print("You chose to pass on the purchase.")
    else:
        print("You appear not to have enough funds in your bank account to make this purchase.")

#searches property availability and if not calls the functions to 
def prop_available(square_no, player_no):
    prop_name = squares[square_no][1]
    if squares[square_no][4] == 'bank':
        prop_price = squares[square_no][3]
        print(prop_name, "is unowned. It is available for £", prop_price + ".")
        # call check_balance function which checks the players balance, and gives the option to buy it if the player has enough money.
        check_balance(player_no, prop_price, prop_name)
        
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
                print("Just visiting!!!")
            elif squares[square_no][1] == "FREE PARKING":
                print("Congratulations you win the money in the middle!!!")
                #call free_parking funtion which checks the amount of money, prints it out and debits it to the player account
            elif squares[square_no][1] == "GO TO JAIL":
                print("Go directly to jail!")
            
        else:
            print("rent!", squares[square_no][5])

# 
       
def new_square_cal(player_no, die1, die2):
    total = die1 + die2
    new_player_pos = player[player_no][3] + total
    player[player_no][3] = new_player_pos
    double(die1, die2)
    print(die1, die2, player[player_no][3])
    return player[player_no][3]
    


#-------------------end of funtions-----------------  
   
player = assign_player_data()#sets a global variable from the assign_player_data function
rolll = roll()

new_square = new_square_cal(0, rolll[0], rolll[1])
prop_available(new_square, 0)

#print(player)
