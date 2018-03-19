print(": Factorial: \n")

def factorial():
	n = int(input("Enter the number to find factorial: "))
	fact = 1
	for i in range(1, n+1):
		fact = fact * i	

	print("Factorial of a number %s is %s " % (n, fact))

factorial()