class ATMCard:
	def __init__(self, defaultpin, defaultBalance):
		self.defaultPin = defaultPin
		self.defaultBalance = defaultBalance
		
	def cekPinAwal(self):
		return self.defaultPin
		
	def cekSaldoAwal(self):
		return self.defaultBalance