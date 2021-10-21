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
chance_cards = [["Go Back 3 square spaces",-1,-1], #####################################################################################################################################
                ["Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",-1,-1], #############
                ["You have been elected Chairman of the Board. Pay each player £50",-1,-1], ############################################################################################
                ["Speeding fine £15",-15,-1], ##########################################################################################################################################
                ["Make general repairs on all your property. For each house pay £25. For each hotel pay £100",-1,-1], ##################################################################
                ["Get Out of Jail Free",-1,-1], ########################################################################################################################################
                ["Your building loan matures. Collect £150",150,-1], ###################################################################################################################
                ["Bank pays you dividend of £50", 50, -1], #############################################################################################################################
                ["Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled",-1,-1], #########
                ["Go to Jail. Go directly to Jail, do not pass Go, do not collect £200",-1,10], ########################################################################################
                ["Take a trip to Kings Cross Station. If you pass Go, collect £200",200, 5], ###########################################################################################
                ["Advance to Pall Mall. If you pass Go, collect £200", 200, 11], #######################################################################################################
                ["Advance to Mayfair",0,39], ###########################################################################################################################################
                ["Advance to Go (Collect £200)",200,0], ################################################################################################################################
                ["Advance to Trafalgar Square. If you pass Go, collect £200", 200, 24], ################################################################################################
                ["Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled",-1,-1], #########
            ]

community_chest =[["You are assessed for street repairs. £40 per house. £115 per hotel", -1, -1],  ######
                  ["It is your birthday. Collect £10 from every player", 10, -1], #######################
                  ["Pay school fees of £50", -50, -1],  #################################################
                  ["Bank error in your favour. Collect £200", 200 , -1], ################################
                  ["Advance to Go (Collect £200)", 200, 0], #############################################
                  ["Go to Jail. Go directly to jail, do not pass Go, do not collect £200", -50, 10],#####            
                  ["Doctor’s fee. Pay £50", -50, -1],  ##################################################
                  ["From sale of stock you get £50", 50, -1],  ##########################################
                  ["Get Out of Jail Free", -1,-1],  #####################################################
                  ["Holiday fund matures. Receive £100", 100, -1], ######################################
                  ["Income tax refund. Collect £20", 20, -1], ###########################################
                  ["Life insurance matures. Collect £100", 100, -1],    #################################
                  ["Pay hospital fees of £100", -100, -1],   ############################################
                  ["Receive £25 consultancy fee", -25, -1],  ############################################
                  ["You have won second prize in a beauty contest. Collect £10", 10, -1], ###############
                  ["You inherit £100", 100, -1]   #######################################################
            ]

# cost of houses on each of the property colours. Hotels are the same price as a house but you must have bought 4 houses on each square in the set before buying hotels
house_cost =    [["brown", "purple", "light blue", 50],
                 ["pink", "orange", 100],
                 ["red", "yellow", 150],
                 ["green", "dark blue", 200]
            ]



#--------------------functions--------------------------


# this function runs through the lists in house_cost above and matches one of the colours with the argument set_colour, then finds the appropriate cost per house and multiplies it by the number of houses requested.
# hotels are the same cost as houses so the house_cost_calc can be used to calculate the cost of hotels.
def house_cost_calc(set_colour, no_of_houses):
    cost = 0
    for i in range(len(house_cost)):
        price = house_cost[i][-1]
        length = len(house_cost[i])-1
        print(house_cost[i], length, price)
       
        for j in range(length):
            colour = house_cost[i][j]
            if set_colour == colour:
               cost = price * no_of_houses
               print(j, cost)
            else:
               print("The colour you have selected is not eligible for house building.")
        
    return cost   

# function required to establish if the player can buy houses for the set
#                 1. Is the whole set in the name of the player?
#                 2. Does the set contain the maximum no of houses allowed (4 * no of squares in the set)
#                 3. Is the set eligible for houses (eg stations or utilities)
# if the player is able to buy houses, we then need to return the max number that can be bought for that set. If not then message returns which explains why the player cannot buy a house.


#rolls two dice and creates the total
def roll(player_no):
    die1 = rd.randint(1,6)
    die2 = rd.randint(1,6)
    total = die1 + die2
    print(player[player_no][0]+ ", you rolled a ", die1, " and a ", die2, "totaling", total)
    return die1, die2, total

def double(die1, die2):
    if die1 == die2:
        print("double!!!")
        
def nearest_train_station_calc(player_no):
    nearest_station = 0
    if player[player_no][3] == 7:
        nearest_station = 15
    elif player[player_no][3] == 22:
        nearest_station = 25
    elif player[player_no][3] == 36:
        nearest_station = 5
    print("nearest station is", nearest_station)
    return nearest_station

def train_station_rental_calc(station, sent_through_chance):
    rent = 0
    station_proprietor = int(squares[station][4])
    print("station proprietor", station_proprietor)
    station_count = 0
    stations = [5,15,25,35]
    for i in stations:
        print(i)
        if int(squares[i][4]) == station_proprietor:
            print("station", i , "is owned by ", station_proprietor) 
            station_count += 1
    if station_count == 1:
        rent = 25 
    elif station_count == 2:
        rent = 50
    elif station_count == 3:
        rent = 100
    elif station_count == 4:
        rent = 200
    else:
        print("error in station rent")
    if sent_through_chance == True:
        rent = rent * 2
    print("the rent you owe is ", rent)
    squares[station][5] = rent
    return rent

def three_spaces_back_calc(player_no, square_no):
    new_square = square_no - 3
    return new_square

def nearest_utility_calc(player_no):
    nearest_utility = 0
    if player[player_no][3] == 7 or player[player_no][3] == 36:
        nearest_utility = 12
    elif player[player_no][3] == 22:
        nearest_utility = 28
    print("nearest utility is", nearest_utility)
    return nearest_utility

def utility_rent_calc(square_no, player_no, sent_through_chance):
    rent = 0
    owner_of_utility = int(squares[square_no][4])
    colour_of_utility = squares[square_no][0]
    if sent_through_chance == True:
        
        print("the colour of set is ", colour_of_utility)
        if owner_of_utility != player_no and owner_of_utility != 0: # if you don't own the utility yourself and the bank isnt the owner...
            print("roll dice and lets make a calculation.......................")
            roll_dice1 = roll(player_no)
            print("...and the dice are.......................", roll_dice1)
            print("The owner of the utility is: ", owner_of_utility)
            rent = 10 * roll_dice1[2]
        elif owner_of_utility != player_no:
            print("no rent to pay since you own the utility")
            rent = 0 
    else:
        print("The dice you previously rolled are...", roll_dice[0], " and ", roll_dice[1])
        same_ownership = False
        for i in squares:
            if i[0] == colour_of_utility and int(i[4]) == owner_of_utility and i[1] != squares[square_no][1]:
                    print("The other utility is owned by the same guy", i[0], i[4])
                    same_ownership = True
        print("same_ownership ", same_ownership)       

        if same_ownership == True:
            rent = roll_dice1[2] * 10
        else:
            rent = roll_dice1[2] * 4
    
    return rent

# ------------------------------------------------------temporary funtion that assigns all purchasable properties to player 1

def prop_4_player2():
    for i in squares:
        if i[4] == '0' and i[0] != "NA":
            i[4] = 2
    print(squares)

# ------------------------------------------------------temporary funtion that assigns all purchasable properties to player 1



#changes the owner of the property to the player no. 
def property_transfer(player_no, prop_name):
    print("Player no", player_no, "and property no", prop_name)
    for i in squares:
        if prop_name == i[1]:
            print(i[1],i[4])
            i[4] = player_no
            print("the new owner is ", i[4])
            
def house_or_hotel_transfer(player_no, set_colour, no_of_units_purchased):
    print("we are assigning houses and or hotels to your ", set_colour, " set.")
    for i in squares:
        if set_colour == i[0] and player_no == int(i[4]): #checks to see if the set colour matches with the purchase request AND that the player is the registered owner of the property
            print(i[1],i[11])
            new_no_of_units = int(i[11])
            new_no_of_units += no_of_units_purchased
            i[11] = new_no_of_units
            print(i[1],i[11])

#creates a list of player data which is updated each move such as player balance, position on the board and whether the player has a get out of jail free card...
def assign_player_data():
    player = []
    
    no_of_players = int(input("how many players do you want? "))
    print(no_of_players)
    no_of_players += 1 #add banker as player0
    
    
    for i in range(no_of_players):
        if i == 0:
            player.append(["banker"])
            player[i].append(0)#assigning piece to player
            player[i].append(20580-(1500*(no_of_players-1)))#assigning balance to banker
            player[i].append(0)# position on the board.
            player[i].append(False) #get out of jail free card bool
            player[i].append(False)#in jail bool
        else:
            player.append([input("Player's name: ")])
            x = int(input("choose a piece 1 = 🚗 | 2 = 👞 "))
            player[i].append(x)#assigning piece to player
            player[i].append(1500)#assigning balance to player
            player[i].append(0)# position on the board
            player[i].append(True) #get out of jail free card bool
            player[i].append(False)#in jail bool
    
    return player

#gets the card, selects top card reads it and puts it at the bottom of the deck 
def cards(card_type):
    card = card_type[0]
    print("moving top card to bottom of deck")
    card_type.append(card_type.index(card))
    card_type.pop(0)





def check_balance1(player_no, cost, transaction_type):
    balance = int(player[player_no][2])
    cost = abs(int(cost))
    player_name = player[player_no][0]
    if balance >= cost:
        print(player_name, "You have £" + str(balance) + ". You have sufficient funds to continue with this transaction.")
        owner_square_you_occupy = int(squares[player[player_no][3]][4])
        if transaction_type == "house_or_hotel_purchase":
            transaction(player_no, cost, 0, transaction_type) #making payee the bank
        else:
            transaction(player_no, cost, owner_square_you_occupy, transaction_type)
    else:
        print("You appear not to have enough funds in your bank account to complete this transaction.")
        print("checking mortgage value of your portfolio")
        
    
    
    
    
def transaction(trans_party1, cost, trans_party2, trans_type):
    if trans_type == "prop_purchase":
        purchase = input()
        if purchase == "y":
            print("you have decided to make the purchase")
            property_transfer(trans_party1, squares[player[trans_party1][3]][1])
    elif trans_type == "house_or_hotel_purchase":
        purchase = input()
        if purchase == "y":
            print("you have decided to make the house or hotel purchase")
            ### we need to go back to the portfolio function in order to then call the house_or_hotel_purchase function...
            
    if trans_type == "receipt": # if active player is receiving funds
        payer = trans_party2
        payee = trans_party1
    else:                       # if active player is paying out 
        payer = trans_party1
        payee = trans_party2 
    
    transaction_val = abs(cost)
    payer_balance = player[payer][2]
    
    payee_balance = player[payee][2]
    print("debit", transaction_val, "from", payer, "s", payer_balance)
    print("credit", transaction_val, "to", payee, "s", payee_balance)
    player[payer][2] = payer_balance - transaction_val
    player[payee][2] = payee_balance + transaction_val
    print("new player balance is:", player[trans_party1][2])
 
 
 
# Inspects property availability for purchase and if not calls the functions to charge rent, pick chance cards, go to jail etc.
def prop_available(square_no, player_no, sent_through_chance_card):
    prop_name = squares[square_no][1]
    print("The person who owns the property you are on is ", player[int(squares[square_no][4])][0]) 
    if squares[square_no][4] == '0' and squares[square_no][0] == "NA":  # this means Go, Community Chest, Income Tax, Chance, Just Visiting Jail, Community Chest, Free Parking, Chance, Go To Jail, Community Chest, Chance, Super Tax
                                                                        #U nique squares number 8 and are chronologically: Go, community_chest, tax, chance, jail, free_parking, chance, go_to_jail
        if squares[square_no][1] == "COMMUNITY CHEST":
            comunity_chest_calc(square_no, player_no)
        elif squares[square_no][1] == "CHANCE":
            chance_card_calc(square_no, player_no)
        elif squares[square_no][1] == "INCOME TAX" or squares[square_no][1] == "Super TAX":
            tax_type = squares[square_no][1]
            input(tax_type + ". Press any key to pay your £200 owed")
            check_balance1(player_no, 200, "penalty_pay")
        elif squares[square_no][1] == "FREE PARKING":
            print("You landed on Free Parking!")          
        elif squares[square_no][1] == "GO TO JAIL":
            go_to_jail(player_no)
        elif squares[square_no][1] == "Just Visiting Jail":
            print("just visiting jail")
        else:
            print("you are on square: ", squares[square_no][1]) # to help debug
    elif squares[square_no][4] == '0' and squares[square_no][0] != "NA":  # this means property is owned by the bank and for sale
        print("you have landed on property which is owned by the bank and is for sale")
        prop_price = squares[square_no][3]
        print(prop_name, "is unowned. It is available for £", prop_price + ".")
        check_balance1(player_no, prop_price, "prop_purchase")
        
    elif player_no == int(squares[square_no][4]): # you have landed on your own property
        print("This property belongs to you. Welcome home!")

    elif player_no != int(squares[square_no][4]): # you have landed on someone else's property
        rent_calculator(player_no, square_no, sent_through_chance_card)

    return player_no # the player_no needs to be returned so that the active player can be updated.


def repair_bill_calc(player_no, cost_per_house, cost_per_hotel):
    hotel_count = 0
    house_count = 0
    for i in squares:
        if player_no == int(i[4]):
            print(i[1], i[11])
            no_of_houses = int(i[11])
            if no_of_houses == 5:
                hotel_count += 1
            elif no_of_houses < 5:
                house_count += no_of_houses
            else:
                print("error counting houses in property: ", [1])
    print("no of hotels: ", hotel_count)
    print("no of houses: ", house_count)
    total_bill = (hotel_count * cost_per_hotel) + (house_count * cost_per_house)
    print("total property repair bill = £", total_bill)
    check_balance1(player_no, total_bill, "penalty_pay")
            
                
def rent_calculator(player_no, square, sent_through_chance_card): # sent_through_chance_card is a boolean variable 
    rent = 0 
    if square == 12 or square == 28: # if a utility
        print("rolling dice")
        print ("multiply the dice total by 4 if one property is owned, 10 if both properties are owned")
        rent = utility_rent_calc(square, player_no, sent_through_chance_card)
    
    elif square == 5 or square == 15 or square == 25 or square == 35: # if a train station
        rent = train_station_rental_calc(square, sent_through_chance_card)
    
    else: # vanilla properties whose rent only changes based on the number of houses and hotels on each
        rent_without_houses = 5
        no_house = int(squares[square][11])
        new_val = rent_without_houses + no_house
        rent = abs(int(squares[square][new_val]))
        print(rent)
        print(no_house)
        print(new_val)
        print("square no: ", square)
        print("rent! Checking if you have £" + str(rent))   
    check_balance1(player_no, rent, "rent")  

def comunity_chest_calc(square_no, player_no):
    input("press any key to pick the COMMUNITY CHEST card")
    owner_square_you_occupy = int(squares[player[player_no][3]][4])  # this is the owner of the property on which the active player has landed
    print(community_chest[0][0])
    if community_chest[0][2] >= 0 and community_chest[0][2] != 10: # if the community_chest card is an 'advance to'... card but not Go to Jail
        advance_to_new_square(player_no, community_chest[0][2])
        
    elif community_chest[0][2] == 10: # if go to jail
        go_to_jail(player_no)
        
    elif community_chest[0][2] < 0 and community_chest[0][1] > 0: # if no movement of player is required and a payment is to be received...
        if community_chest[0][0] == "It is your birthday. Collect £10 from every player":
           for i in range(len(player)-1):
               if player_no != i+1:
                   print("player", i+1, "is paying out to ", player_no)
                   transaction(player_no, 10, i+1, "receipt")
        else:                
            transaction(player_no, community_chest[0][1], owner_square_you_occupy, "receipt")
        
    elif community_chest[0][2] < 0 and community_chest[0][1] < 0: # if no movement of player is required and a payment is to be made...
        if community_chest[0][0] == "You are assessed for street repairs. £40 per house. £115 per hotel":
            print("just checking on your property portfolio. This could be expensive...")
            repair_bill_calc(player_no, 40, 115)
        else:
            check_balance1(player_no, community_chest[0][1], "penalty_pay")     
        
    elif community_chest[0][0] == "Get Out of Jail Free":
        get_out_of_jail_card(player_no)
        
    else:
        print("any other community chest cards")
    cards(community_chest)   

def chance_card_calc(square_no, player_no):            
    input("press Enter to pick the CHANCE card")
    owner_square_you_occupy = int(squares[player[player_no][3]][4])  # the owner of the property on which the active player has landed
    print(chance_cards[0][0])
    if chance_cards[0][2] >= 0 and chance_cards[0][2] != 10: # if the chance card is an 'advance to'... card but not Go to Jail
        advance_to_new_square(player_no, chance_cards[0][2])
                
    elif chance_cards[0][0] == "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.":
        nearest_utility = nearest_utility_calc(player_no)
        print("player no: ", player_no, "utility: ", nearest_utility, "owner of the utility: ", squares[nearest_utility][4])
        advance_to_new_square(player_no, nearest_utility)
                
    elif chance_cards[0][0] == "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled":
        #station_rent = train_station_rental_calc(nearest_train_station_calc(player_no), True)
        #print("station rent is... £", station_rent)
        nearest_station = nearest_train_station_calc(player_no)
        print("nearest_station = ", nearest_station)
        advance_to_new_square(player_no, nearest_station)
            
    elif chance_cards[0][0] == "You have been elected Chairman of the Board. Pay each player £50":
        for i in range(len(player)-1):
            if player_no != i+1:
                print("player", i+1, "is is receiving funds from ", player_no)
                transaction(player_no, 50, i+1, "penalty_pay")
        
    elif chance_cards[0][0] == "Go Back 3 square spaces":
        print("three spaces back calc says we are now on square...", three_spaces_back_calc(player_no, square_no))   
        new_square = three_spaces_back_calc(player_no, square_no)
        print("three spaces back new square is... ", new_square)
        go_backwards(player_no, new_square)
    
    elif chance_cards[0][2] < 0 and chance_cards[0][1] > 0: # if no movement of player is required and a payment is to be received...  
        transaction(player_no, chance_cards[0][1], owner_square_you_occupy, "receipt")
        
    elif chance_cards[0][2] == 10: # if go to jail
        go_to_jail(player_no)
        
    elif chance_cards[0][0] == "Get Out of Jail Free":
        get_out_of_jail_card(player_no)
        
    elif chance_cards[0][2] < 0 and chance_cards[0][1] < 0: # if no movement of player is required and a payment is to be made...
        if chance_cards[0][0] == "Make general repairs on all your property. For each house pay £25. For each hotel pay £100":
            print("just checking on your property portfolio. This could be expensive...")
            repair_bill_calc(player_no, 25,100)
        else:
            check_balance1(player_no, chance_cards[0][1], "penalty_pay")
  
    else:
        print("other chance cards exist...")
    cards(chance_cards) 
    

    
def advance_to_new_square(player_no, new_square_no):
    current_square = player[player_no][3]
    virtual_die = new_square_no - current_square
    if virtual_die < 0:
        virtual_die = 40 - current_square + new_square_no 
    else:
        virtual_die = new_square_no - current_square
        
    new_square_no = new_square_cal(player_no, virtual_die, 0)
    
    prop_available(new_square_no, player_no, True)

def go_backwards(player_no, new_square_no):
    player[player_no][3] = new_square_no
    prop_available(new_square_no, player_no, True)
    


def go_to_jail(player_no):
    in_jail = True
    new_player_pos = 10
    print("You are in jail!")
    player[player_no][3] = new_player_pos
    if player[player_no][4] == True:
        get_out_of_jail_use = input("you have a get out of jail card do you wish to use it (y/n)")
        if get_out_of_jail_use == "y":
            in_jail = False
            print("Just visiting...")
            player[player_no][4] = False
        else:
            in_jail = True
    player[player_no][5] = in_jail
                
def get_out_of_jail_card(player_no):
    player[player_no][4] == True
    
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
    #print("the active player is: ", player[active_player][0])
    return active_player



def make_go_payment(player_no):
    if player[player_no][3] == 0:
        print("Congratulations you landed on Go. You just collected £200")
    else:
        print("You passed Go. You just collected £200")
    player[player_no][2] += 200 # active customer balance credited
    player[0][2] -= 200 # bank balance debited 
    print("your new player balance is: £", player[player_no][2])
    
    
    
def move(player_keystroke, player_no):
    
    print(player_keystroke, player_no)
    if player_keystroke == "p":
        portfolio(player_keystroke, player_no)
                
        input("...and press any key to roll dice")
    else:
        print("not portfolio")
        


def portfolio(player_keystroke, player_no):
    print("Portfolio:")
    houses = 0
    hotels = 0

    for i in squares:
        if int(i[4]) == player_no:
            if int(i[11]) == 5:
                houses = 0
                hotels = 1
                print(i[1], "part of the ", i[0], "set. Currently, you have ", hotels, " hotel")
                
            else:
                houses = int(i[11])
                hotels = 0
                print(i[1], "part of the ", i[0], "set. Currently, you have ", houses, " houses")
                
                
                
                
    purchase = input("Do you wish to buy any houses or hotels for your portfolio?")
    
    if purchase == "y":
        
        set_colour = input("type the set colour for which you wish to buy property...")
        
        # we need to check if the set is eligible for house purchase ie not stations or utilities...
        # ...and if the whole set is owned...
        # and if so whether there are any houses already on the set, in order to work out the limit on the number of houses which can be placed on the set.
        
        if set_colour == "transparent" or set_colour == "white":
            print("You can't buy houses for stations or utilities...")
        else: 
            set_size_owned = 0
            set_size = 0
            set_houses = 0
            set_hotels = 0
            house_cost = 0
            for i in squares:
                if int(i[4]) == player_no and set_colour == i[0]:
                    set_size_owned += 1
                    if int(i[11]) == 5:
                        houses = 0
                        hotels = 1
                        set_hotels +=1
                        print(i[1], "part of the ", i[0], "set. Currently, you have ", hotels, " hotel")
                    
                    else:
                        houses = int(i[11])
                        set_houses += int(i[11])
                        hotels = 0
                        print(i[1], "part of the ", i[0], "set. Currently, you have ", houses, " houses")
            
                if set_colour == i[0]:
                    set_size += 1
            
            
            if set_size == set_size_owned:
                max_houses = (set_size_owned * 4) - set_houses
                max_hotels = set_size_owned - set_hotels
                
                if max_houses == 0:
                    if max_hotels == 0:
                        print("you have bought all the houses and hotels for this property")
                    elif max_hotels > 0:
                        hotel_option = input("you have the maximum no of houses available on this set. Do you want to buy a hotel for each square on the set? Press Y or any other key to carry on without the purchase")
                        if hotel_option == "y":
                            print("working out the cost of hotels for this set...")
                            hotel_cost = house_cost_calc(set_colour, set_size)
                            print("The cost of buying a hotel on each square of the ", set_colour, " set is £", hotel_cost)
                            
                            # here we need to add check balance then if funds available, transaction function to be called. 
                            check_balance1(player_no, hotel_cost, "house_or_hotel_purchase") # have we got enough funds, if so call transaction function using bank as payee, player_no as payor
                            print(" calling house_or_hotel_transfer function to update the squares list with the correct no of houses or hotels...")
                            house_or_hotel_transfer(player_no, set_colour, 1)
                            
                else: 
                    print("set size is ", set_size_owned, "so you can buy a maximum of ", max_houses, "houses and ", max_hotels, "hotel(s)")

                    no_of_houses = int(input("how many houses do you want to buy on the set coloured " + set_colour))
                    while no_of_houses > max_houses:
                        no_of_houses = int(input("Too many houses. Try again."))
                    house_cost = house_cost_calc(set_colour, no_of_houses)    
                    print("You wish to buy ", str(no_of_houses), "on the ", set_colour, " set. This will cost...", house_cost)
                    # here we need to add check balance then if funds available, transaction function to be called. 
                    check_balance1(player_no, house_cost, "house_or_hotel_purchase") # have we got enough funds, if so call transaction function using bank as payee, player_no as payor
                    print(" calling house_or_hotel_transfer function to update the squares list with the correct no of houses or hotels...")
                    house_per_square = int(no_of_houses/set_size)
                    house_or_hotel_transfer(player_no, set_colour, house_per_square)
                
            elif set_size != set_size_owned:
                print("In order to buy houses for this property you need to own the whole set...")
                input("press any key to continue")
                portfolio(player_keystroke, player_no)
            else:
                print("Throw exception!!!!!!!!")


#-------------------end of funtions-----------------  

#prop_4_player2()     # buys all property in name of player 2
    
#shuffling the chance and community chest cards
#rd.shuffle(chance_cards)
#rd.shuffle(community_chest)   
player = assign_player_data()#sets a global variable from the assign_player_data function
print(player)





while True:
    #print(player)
    player_name = player[active_player][0]
    player_keystroke = str(input(player_name + ", Enter 'P' to display your properties, or any other key to roll dice..."))
    move(player_keystroke, active_player)
    
    roll_dice = roll(active_player)
    new_square = new_square_cal(active_player, roll_dice[0], roll_dice[1])
    #new_square = new_square_cal(active_player, 30, 3)
    active_player = player_turn(prop_available(new_square, active_player, False), len(player), roll_dice[0], roll_dice[1])
    print("players: ", player)
  