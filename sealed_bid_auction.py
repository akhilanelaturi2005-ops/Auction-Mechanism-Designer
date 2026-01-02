
def sealed_bid_auction(bidders):
    bids = {b.name: b.bid() for b in bidders}
    winner = max(bids, key=bids.get)
    return winner, bids[winner]
