class calculate_interest():
	def __init__(self, principal, rate, time_per_year, years):
		self.principal = principal
		self.rate = rate
		self.time_per_year = time_per_year
		self.years = years

	# simple interest
	def simple_interest(self):
		return round(self.principal * (1 + self.rate * self.years), 2)

	# compound interest
	def compound_interest(self):
		body = 1 + (self.rate / self.time_per_year)
		exponent = self.time_per_year * self.years
		return round(self.principal * pow(body, exponent), 2)

	# future value of annuity
	def fv_of_annuity(self):
		numberator = pow((1 + self.rate), self.years) - 1
		FV = self.principal * (numberator / self.rate)
		return round(FV,2)

	def annual_interest(self):
		interest_list = {}
		for i in range(1, self.years + 1):
			total_interest = round(self.principal * (pow((1 + self.rate), i) - 1), 2)
			interest_list["year %s" % i] = "$ %s" % total_interest
		return interest_list


interests = calculate_interest(1000, 0.06, 1, 10)
fv = interests.compound_interest()
total = interests.annual_interest()
print(total)
print(fv)

