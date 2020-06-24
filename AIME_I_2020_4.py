#Let $S$ be the set of positive integers $N$ with the property that the last four digits of $N$ are $2020,$ and when the last four digits are removed, the result is a divisor of $N.$ For example, $42{,}020$ is in $S$ because $4$ is a divisor of $42{,}020.$ Find the sum of all the digits of all the numbers in $S.$ For example, the number $42{,}020$ contributes $4+2+0+2+0=8$ to this total. 
def digitsum(num):
	sum = 0
	for digit in str(num):
		sum += int(digit)
	return sum		

def main():
	x = 1
	sum = 0
	while(x <= 2020):
		n = int(str(x)+"2020")
		if(n%x == 0):
			sum+=digitsum(n)
		x+=1		
	print("The sum is " + str(sum))


main()
