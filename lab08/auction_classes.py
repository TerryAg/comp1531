import time
class Auction:
	def __init__(self):
		self.items = []

	def post_item(self, user, item):
		# Posts an item given by user for bidding
		if item.in_auction():
			return 0 # Fail

		self.item.in_auction = True
		self.items.append({
			'owner':user, # User obj
			'item':item # Item obj
			})

	def all_items(self):
		# Prints all items in current auction
		for item in self.items:
			print(item)

	def bid_for_item(self, user, item, price):
		item.add_bidding_info(user, price)
		self.items.append(item)

	def finished_bidding(self):
		# Checks if any items have not had a bid in 48 hours
		for item in self.items:
			if (time.time() - item.latest_bid()) > 48*60*60:
				announce_winner(item)

	def announce_winner(self, item):
		# Called when auction for item has finished
		winner = item.bidding_info[-1]
		print("{} has won the bid for {} at price {}".format(
			winner['id'], item, winner['price']))
		self.items.remove(item)

class Item:
	def __init__(self, item_id, name, description, owner):
		self.item_id = item_id
		self.name = name
		self.description = description
		self.owner = owner # User obj
		self.bidding_info = [] # list of dictionaries:
								# {'time':123456, 'id':user_id, 'price':bid_price}
		self.in_auction = False # Determines if item is already in an auction


	def add_bidding_info(self, user, price):
		self.bidding_info.append({
			'time': time.now(),
			'id':user.get_id(),
			'price':price
			})

	def print_bidding_history(self):
		print("Item {} bidding history:".format(self.name))
		for b in sorted(self.bidding_info, key=lambda x: x['time']):
			print("Bid of ${} at time {} by user {}".format(b['price'], b['time'], b['id']))

	def latest_bid(self):
		# returns time of latest bid
		if not bidding_info:
			return None # list is empty
		return bidding_info[-1]['time']

	def in_auction(self):
		return self.in_auction

	def __str__(self):
		return (self.name, self.description)

class Electronic(Item):
	def __init__(self, voltage, brand):
		self.voltage = voltage
		self.brand = brand

class Book(Item):
	def __init__(self, author, publish_year):
		self.author = author
		self.publish_year = publish_year

class Furniture(Item):
	def __init__(self, age, material):
		self.age = age
		self.material = material

class User:
	def __init__(self, user_id, name, posted_items, bids):
		self._user_id = user_id
		self.name = name
		self.posted_items = posted_items # List of items user owns
		self.bids = bids # Dictionary of {item:bid}

	def add_to_auction(self, item, auction):
		if item in self.posted_items:
			if not auction.post_item(self, item):
				print("Item is already in another auction")
			else:
				print("Item successfully added")
		else:
			print("User does not have such item")

	def bid_item(self, auction, item, price):
		# Bids for an item in an auction
		# item isinstance Item
		auction.bid_for_item(self, item, price)

	def get_id(self):
		return self._user_id
