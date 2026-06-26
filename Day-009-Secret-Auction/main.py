import art

print(art.logo)
# TODO-1: Ask the user for input
bidding_continues=True
bidding_dictionary={}
while bidding_continues:
    name=str(input("What is your name?: "))
    bid=int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bidding_dictionary[name]=bid
    # print(bidding_dictionary)
    # TODO-3: Whether if new bids need to be added
    other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_bidders=="yes":
        print("\n"*100)
    else:
        bidding_continues=False
    # TODO-4: Compare bids in
        for bidders in bidding_dictionary:
            winning_bid=max(bidding_dictionary.values())
            if bidding_dictionary[bidders]==winning_bid:
                winner=bidders
                print(f"The winner is {winner} with a bid of ${winning_bid}.")


