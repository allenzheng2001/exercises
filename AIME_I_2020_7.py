import math

class Combo():

	def factorial(n):
		ans = 1
		while(n > 0):
			ans *= n
			n -= 1
		return ans

	def nCr(n,r):
		return int((Combo.factorial(n)/((Combo.factorial(r)*Combo.factorial(n-r)))))

	def nPr(n,r):
		return int((Combo.factorial(n)/Combo.factorial(n-r)))

class NT():

	def primeFactors(n):
		factors = []
		
		if (n < 1):
			print("No factors")
		
		if (n == 1):
			return [[1,1]]
		
		m = 0

		while(n % 2 == 0):
			n /= 2
			m += 1
			

		factors.append([2, m])

		for i in range(3, (int(math.sqrt(n))+1), 2):
			k = 0
			while (n % i == 0):
				n /= i
				k += 1
			factors.append([i, k])

		if (n > 1):
			factors.append([n, 1])

		return factors





def main():

	sum = 0
	for i in range(1,13):
		sum += Combo.nCr(11, i-1) * Combo.nCr(12, i)
	ans = 0
	for s in NT.primeFactors(sum):
		if (s[1] > 0):
			ans += s[0]
	print('The sum of the prime numbers is', ans)


main()