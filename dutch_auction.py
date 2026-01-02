
def dutch_auction(bidders, start_price):
    price = start_price
    while price > 0:
        for b in bidders:
            if b.bid() >= price:
                return b.name, price
        price -= 1
