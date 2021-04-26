from os import system, name 
from data.logo import logo

def new_bidder(bidder_list: dict):
    name = input("Enter your name: ")
    bid_amount = input("Enter your bid: $")
    bidder_list[name] = bid_amount 

def clear_screen():
    if name == "nt":
        _ = system("cls")
    elif name == "posix":
        _ = system("clear")

auction_end = False
auction_bidders = {}
print(logo)
print("Welcome to the 100 Days Auction House! \n")
while not auction_end:
    new_bidder(auction_bidders)
    flag = input("Are there any more bidders? (y/n): ")
    if flag.lower() not in ["yes", "y"]:
        clear_screen()
        auction_end = True
        winner_name = max(auction_bidders, key = auction_bidders.get)
        print(f"The Winner of the auction is: {winner_name} with a bid of ${auction_bidders[winner_name]}")
    else:
        clear_screen()