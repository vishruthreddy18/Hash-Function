import math


class hash:
	message = ''
	IV = 1234567890

	A = 0
	B = 0
	C = 0
	D = 0
	E = 0
	
	F = 0

	def __init__(self):
		pass
	
	def unify(self, h):							#Uses the most obvious algorithm to restrict the length
		while not (1000000000<h<9999999999):			
			if h < 1000000000:
				h = h * (h % 8543 + 1) + 1
			else:
				h = int(h / 13) + 123
		return h

	def pad(self,message):
		a = 0
		b = 0
		c = 0
		d = 0
		e = len(message)

		if e == 0:
			e += 2

		if len(message) < 32:					#Pads the input message
			i = 1
			while len(message) < 32:
				message += str(len(message) ^ i)
				i += 1
		#print(message)
		for i in message[:8]:					#Uses the Bernstein Hash Algorithm
			a += 33 * a + ord(i)				#to divide the input message into 4 different parts
		for i in message[8:16]:					#The fifth is based on the length of the message to avoide collisions.
			b += 33 * b + ord(i)
		for i in message[16:24]:
			c += 33 * c + ord(i)
		for i in message[24:]:
			d += 33 * d + ord(i)*90
		
		return self.unify(a), self.unify(b), self.unify(c), self.unify(d), self.unify(e)		


	def FF(self,INPUT1, INPUT2):
		INPUT = str(INPUT1 + INPUT2)	
		h = 0		

		for i in INPUT:						#Uses the Rotating Hash Algorithm
			h = (h << 4) ^ (h) + int(i)
		#print(h)
		#print(self.unify(h))
		return self.unify(h)
	
	def hash(self, m):						#Uses the Merkel-Damgard construction
		self.message = m
		
		self.A, self.B, self.C, self.D, self.E = self.pad(self.message)
		
		self.A = self.FF(self.IV, self.A)
		self.B = self.FF(self.A , self.B)
		self.C = self.FF(self.B , self.C)
		self.D = self.FF(self.C , self.D)
		self.F = self.FF(self.D , self.E)
		return hex(self.F)

