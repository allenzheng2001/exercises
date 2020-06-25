def isAscending(s):
	for i in range(len(s)-1):
		if (s[i] >= s[i+1]):
			return False
	return True

def isDescending(s):
	for i in range(len(s)-1):
		if (s[i] <= s[i+1]):
			return False
	return True

def permutation(s):
	if (s is None or len(s) == 0):
		return []
	if (len(s) == 1):
		return [s]
	l = []

	for i in range(len(s)):
		n = s[i]
		remainder = s[:i]+s[i+1:]
		for x in permutation(remainder):
			perm = [n]
			perm.extend(x)
			l.append(perm)
	return l

		
def main():
	cards = [1,2,3,4,5,6]
	# cards = [1, 2, 3]
	arrangements = 0
	# print (permutation(cards))
	# print("permutations: ", permutation(cards))
	for p in permutation(cards):
		found = False
		i = 0
		while(i in range(len(p)) and not found):
			temp = p[:i] + p[i+1:]
			if(isAscending(temp) or isDescending(temp)):
				found = True
				arrangements+=1
			else:
				i+=1

	print("The number of arrangements is " + str(arrangements))

main()
