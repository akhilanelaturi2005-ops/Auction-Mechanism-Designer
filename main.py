
from bidder import Bidder
from english_auction import english_auction
from dutch_auction import dutch_auction
from sealed_bid_auction import sealed_bid_auction

bidders = [
    Bidder("A", 100),
    Bidder("B", 120),
    Bidder("C", 110)
]

print("English Auction:", english_auction(bidders))
print("Dutch Auction:", dutch_auction(bidders, 150))
print("Sealed Bid Auction:", sealed_bid_auction(bidders))
