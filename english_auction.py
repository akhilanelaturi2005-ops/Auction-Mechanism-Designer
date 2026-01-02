
from bidder import Bidder

def english_auction(bidders):
    bids = {b.name: b.bid() for b in bidders}
    winner = max(bids, key=bids.get)
    price = bids[winner]
    return winner, price
