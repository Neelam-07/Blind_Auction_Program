
# Blind auction program:

bidding= {}

def highest_bidder(bidding_data):
    higest_bid= 0
    winner= " "
    for bidder in bidding_data:
       if bidding_data[bidder] > higest_bid:
           higest_bid = bidding_data[bidder]
           winner = bidder
    print(f"Higest bidder is {winner} & amount is {higest_bid}")

game_on= False
while not game_on:
    name= input("eneter your name ?/n")
    price= int(input("eneter the bidding price u wanna bid ?/n"))
    bidding[name]=price
    print(bidding)
    ask_user= input("Is there anymore bidders, Y or N ?/n ")
    
    if ask_user == "N":
        game_on= True
        highest_bidder(bidding)

    else:
        continue

