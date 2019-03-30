def fibonacci_iterative(numOne, numTwo, iterNum):
	"""
		numOne is start point
		numTwo is step range
		iterNum is how many numbers to print
	"""
	for i in range (0, iterNum):
		print(numOne) #printing
		numTwo += numOne #adding previous number to the current one
		numOne = numTwo - numOne #changing previous number to current 

def fibonacci_recursive(num):
	nums = []
	if num in (1, 2):
		nums.append(1)
	nums.append(fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2))
	print (nums)

#calling iterative function
# fibonacci_iterative(0, 1, 10)

#calling recursive function
# print (fibonacci_recursive(7))

fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
print (fib(15))