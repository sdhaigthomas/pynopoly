import random
import csv
print("Welcome to Pynopoly")
#assigning varibles
players_no = 0
player_data = []
players_turn = 0

#making list from CSV file containing property data property_data3.csv
with open('property_data3.csv', newline = '') as f:
    reader = csv.reader(f)
    sp = list(reader)

#defineing chance cards
chance_cards = [["Advance to Go (Collect £200)",200,0],
                ["Advance to Trafalgar Square. If you pass Go, collect £200",200,24],
                ["Advance to Mayfair",0,39],
                ["Advance to Pall Mall. If you pass Go, collect £200", 200, 11],
                ["Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled",-1,-1],
                ["Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled",-1,-1],
                ["Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",-1,-1],
                ["Bank pays you dividend of £50", 50, 0],
                ["Get Out of Jail Free",-1,-1],
                ["Go Back 3 Spaces",-1,-1],
                ["Go to Jail. Go directly to Jail, do not pass Go, do not collect £200",-1,-1],
                ["Make general repairs on all your property. For each house pay £25. For each hotel pay £100",-1,-1],
                ["Speeding fine £15",-1,-1],
                ["Take a trip to Kings Cross Station. If you pass Go, collect £200",200,35],
                ["You have been elected Chairman of the Board. Pay each player £50",-1,-1],
                ["Your building loan matures. Collect £150",-1-1,],
            ]

#--------------------functions--------------------------


#for chance cards to see what station to move to.
def station_dest(players_pos):
    if players_pos == 7:
        station = 15
    elif players_pos == 22:
        station = 25
    elif players_pos == 36:
        station = 5
    return station

#telling the player what their roll was and where thay landed, returning their updated position and not updating the players turn if its a double 
def landed(player_name, die1, die2, pp, pt, pppr):
    total = die1 + die2
    post_roll_pos = pppr
    if rollreturn[3] == 1:
        print(player_name, "you rolled a", die1, "and a", die2, "totaling", total, "which leaves you on", post_roll_pos, "Thats a double!")
    else:
        print(player_name, "you rolled a", die1, "and a", die2, "totaling", total, "which leaves you on", post_roll_pos)
        pt =+ 1
        players_turn = pt
    
    return post_roll_pos

#randomises two die, makes a total and figures out if its a double and returns the whole lot.
def roll():
    double = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    if die1 == die2:
        double = 1
    return die1, die2, total, double


def property_transfer(player_no, prop_name):
    print("Player no", player_no, "and property no", prop_name)
    for i in sp:
        if prop_name == i[1]:
            print(i[1],i[4])
            i[4]=player_no
            print("the new owner is ", i[4])
                                                                                                                 
def check_balance(player_no, prop_price, prop_n):
    balance = int(player_data[player_no][2])
    prop_price = int(prop_price)
    player_name = player_data[player_no][0]
    #print(player_name, "the property you want to purchase is", prop_price )
    if balance >= prop_price:
        print(player_name, "You have £" + str(balance) + ". Press Y to purchase, N to let it go.")
        purchase = input()
        if purchase == "y":
            print("debit", prop_price, "from", balance)
            print("new balance is £", balance - prop_price)
            player_data[player_no][2] = balance - prop_price
            property_transfer(player_no, prop_n)
            print(player_data[player_no][2])
        else:
            print("You chose to pass on the purchase.")
    else:
        print("You appear not to have enough funds in your bank account to make this purchase.")

def new_player_position_cal(player_position, total_dice, player_name):
    if player_position + total_dice > 39:
        subtracter = 40 - player_position
        new_pos = total_dice - subtracter
        print("new_position:", new_pos)
    else:
        new_pos = player_position + total_dice
    return new_pos
        
        
def purchase_prop(prop_name, square_no, player_no):
    if sp[square_no][4] == 'bank':
        prop_price = sp[square_no][3]
        print(prop_name, "is unowned. It is available for £", prop_price + ".")
        # call check_balance function which checks the players balance, and gives the option to buy it if the player has enough money.
        check_balance(player_no, prop_price, prop_name)
        
    else:
        if sp[square_no][4] == "NA":
            if sp[square_no][1] == "GO":
                print("You receive £" + str(sp[square_no][5]))
            elif sp[square_no][1] == "COMMUNITY CHEST":
                input("press any key to pick the COMMUNITY CHEST card")
                #call COMMUNITY CHEST function
            elif sp[square_no][1] == "INCOME TAX":
                print("Income tax £" + str(sp[square_no][5]))
                #call income_tax funtion
            elif sp[square_no][1] == "CHANCE":
                input("press any key to pick the CHANCE card")
                #call CHANCE function
            elif sp[square_no][1] == "Just Visiting Jail":
                print("Just visiting!!!")
            elif sp[square_no][1] == "FREE PARKING":
                print("Congratulations you win the money in the middle!!!")
                #call free_parking funtion which checks the amount of money, prints it out and debits it to the player account
            elif sp[square_no][1] == "GO TO JAIL":
                print("Go directly to jail!")
            
        else:
            print("rent!", sp[square_no][5])
#-------------------end of funtions-----------------        


rollreturn = roll()

#players turn
players = int(input("how many players do you want? "))




for i in range(players):
    player_data.append([input("Player's name: ")])
    x = int(input("choose a piece 1 = 🚗 | 2 = 👞 "))
    
    player_data[players_no].append(x)
    player_data[players_no].append(1500)# balance
    player_data[players_no].append(0)# position before rolling dice
    player_data[players_no].append(False) #get out of jail free card bool
    print(player_data)
    print(players_no)
    players_no += 1


while True:
    rollreturn = roll()
    players_name = player_data[players_turn][0]
    players_position = player_data[players_turn][3]
    die1 = rollreturn[0]
    die2 = rollreturn[1]
    total = rollreturn[2]
    double = rollreturn[3]
    player_position_post_roll = new_player_position_cal(players_position, total, players_name)
    
    
    move = input(players_name + " press enter to roll.")
    # landed simply adds some colourful descriptive text for the player and returns player_position_post_roll. It is largely not very helpful
    position_update = landed(players_name, die1, die2, players_position, players_turn, player_position_post_roll)
    # is the property available and if so allow purchase
    
    purchase_prop(sp[player_position_post_roll][1], player_position_post_roll, players_turn)
    
    player_data[players_turn][3] = position_update # position_update could be replaced with 'player_position_post_roll'
    
    #this code should be put in a function and called every time a player rolls the dice
    if players_turn == players - 1:
        if die1 == die2:
            players_turn = players_turn
        else:
            players_turn = 0
    else:
        if die1 == die2:
            players_turn = players_turn
        else:
            players_turn =+ 1