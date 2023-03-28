class Card:
	def __init__(self, value):
		self.value = value

	def getValue(self):
		return self.value

	def __repr__(self):
		return f"{value}"

class LonkCard(Card):
	def __init__(self, value, name):
		super.__init__(value)
		self.name = name

	def getName(self):
		return name

	def __repr__(self):
		return f"Card {name} \nValue : {value}"

