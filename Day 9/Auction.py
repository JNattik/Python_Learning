bidder_dictionary = {}
bidding_finished = False

def find_highest_bidder():
    highest_bid = 0
    winner = ""
    for x in bidder_dictionary:
        bid_amount = bidder_dictionary[x]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = x
    print(f"The winner is {winner} with an amount of ${highest_bid}. Congratulations.")

while not bidding_finished:
    print("Welcome to the secret auction program.")
    Ask_name = input("What is your name?: ")
    Ask_bid = int(input("What's your bid?: "))
    bidder_dictionary[Ask_name] = Ask_bid
    Other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if Other_bidders == "no":
        bidding_finished = True
        find_highest_bidder()
    elif Other_bidders == "yes":
        bidding_finished = False



