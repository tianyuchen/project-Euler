lst_Fib = [1, 2]
while lst_Fib[len(lst_Fib) - 1] < 4 * (10 ** 6):
	lst_Fib.append(lst_Fib[len(lst_Fib) - 2] + lst_Fib[len(lst_Fib) - 1])
print lst_Fib[len(lst_Fib) - 2]

def totaleven(lst):
	total = 0
	for number in lst:
		if number % 2 == 0:
			total += number
	return total

print totaleven(lst_Fib)
