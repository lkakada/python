print(": Compound Interest :")

def cal_compound_interest():
	amount = float(input("Enter the principal amount: "))
	rate = float(input("Enter rate percentage: "))

	x = float(input('Press \'1\' for duration of time in days  \n\'2\' for time in months and \n\'3\' for time in years\n'))

	if x == 1:
		time = float(input("Enter number of days: "))
		time = time / (12*30)
	elif x == 2:
		time = float(input("Enter number of months: "))
		time = time / 12
	else:
		time = float(input("Enter number of years: "))

	total_amount = (amount * (1 + (rate / 100)) ** time)
	print("\nTotal amount is %.4f " % total_amount)

	compound_interests = total_amount - amount
	print("\nCompound Interest = %.4f " % compound_interests)
	print("\nTotal amount = %.4f " % total_amount)



























