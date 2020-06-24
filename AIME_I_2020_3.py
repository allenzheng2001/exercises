# A positive integer $N$ has base-eleven representation abc and base-eight representation $\underline1\kern 0.1em\underline{b}\kern 0.1em\underline{c}\kern 0.1em\underline{a},$ where $a,b,$ and $c$ represent (not necessarily distinct) digits. Find the least such $N$ expressed in base ten. 
class Number():
	A = (1, 2, 3, 4, 5, 6, 7)
	B = (0, 1, 2, 3, 4, 5, 6, 7)
	C = (0, 1, 2, 3, 4, 5, 6, 7)

	def __init__(self, a = 1, b = 0, c = 0):
		if (a in Number.A):
			self.a = a
		if (b in Number.B):
			self.b = b 
		if (c in Number.C):
			self.c = c

	def inc(self):
		if(self.c == 7):
			if(self.b == 7):
				if (self.a == 7):
					self.a += 0
				else:
					self.a+=1
					self.b = 0
					self.c = 0
			else:
				self.c = 0
				self.b+=1
		else:
			self.c+=1		



	def __str__(self):
		return str(121*self.a + 11*self.b + self.c)

	def base8(self):
		return 512 + 64*self.b + 8*self.c + self.a

	def base11(self):
		return 121*self.a + 11*self.b + self.c



def main():
	N = Number(1, 0, 0)
	while(N.__str__() != "999"):
		if(N.base8() == N.base11()):
			print("The lowest possible number is " + N.__str__())
			break
		else:
			N.inc()

	if (N.__str__() == "999"):
		print("Impossible Problem")



main()