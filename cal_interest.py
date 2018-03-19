print(": Simple Interest :\n")

def simple_interest():
	rate = float(input("Enter rate percentage: "))
	principle = input("Enter the principle amount: ")
	x = float(input("Select \'1\' for duration of time in days \n\'2\' for in months and \n\'3\' for time in years."))
	
	principle = float(principle)

	if (x == 1):
		time = float(input("Enter number of days: "))
		time = time / (12 * 30)
	elif (x == 2):
		time = float(input("Enter number of months: "))
		time = time / 12
	else:
		time = float(input("Enter number of years: "))

	simple_interests = (principle * rate * time ) / 100
	print("Simple Interest = %f " % simple_interests)

	total = principle + simple_interests
	print("Total amount = %f " % total)

simple_interest()



























