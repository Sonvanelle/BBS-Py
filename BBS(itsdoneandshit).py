from random import randint
from string import ascii_lowercase

# Written by Ming Wei, Edited and Proofread by Charles
	
def isprime(number): # prime number checker based on primality test
	if number <= 1:  # https://en.wikipedia.org/wiki/Primality_test
		return False
	elif number <=3:
		return True
	elif number % 2 == 0 or number % 3 == 0:
		return False
	i = 5
	while i * i <= number:
		if number % i == 0 or number % (i+2) == 0:
			return False
		i += 6
	return True

def gcd(a,b):     # greatest common divisor based on euclid's algorithm
	while b != 0: # https://en.wikipedia.org/wiki/Euclidean_algorithm
		i = a
		a = b
		b = i % b
	return a

def key():
	p = randint(1003, 10000)
	q = randint(1003, 10000)
	
	while p % 4 != 3 or q % 4 != 3 or not isprime(p) or not isprime(q): 
	    # make p and q prime and p%4=q%4=3
		if p % 4 != 3 or not isprime(p):
			p = randint(1003, 10000)
		if q % 4 != 3 or not isprime(q):
			q = randint(1003, 10000)
	while p == q: #make p != q
		q = randint(1003, 10000)
		if q % 4 != 3 or not isprime(q):
			continue
			
	n = p*q
	print('Your public key is :', n)
	print('Your private keys are : %s and %s' %(p,q))

def encrypt():
	messagelist = []
	rando = []
	
	message = input('Please enter your message : ').replace(' ', '').lower()
	while not message.isalpha(): # message can only be letters
		print('Please input only letters!')
		message = input('Please enter your message: ').replace(' ', '').lower()
	publickey = int(input('Please enter the public key: '))

	for i in range(len(message)): # change letters to respective numbers
		messagelist.append(ascii_lowercase.index(message[i])) 
	
	seed = randint(100,10000)
	while seed ** 4 < publickey: # seed squared > square root of n
		seed = randint(100,10000)
		if gcd(seed, publickey) != 1: # coprime if gcd = 1
			continue
	print('Your seed is :', seed)
	
	initno = seed * seed
	for i in range(len(messagelist)): # number of int based on length of message
		if i == 0:
			rando.append(initno % publickey)
		else:
			rando.append((initno ** 2 ** i) % publickey) # xi = x0 ** i mod N
		
	for i in range(len(messagelist)): # C = (M + x) mod 26
		messagelist[i] = ascii_lowercase[(messagelist[i] + rando[i]) % 26]
	print('Ciphertext :', ''.join(messagelist))
	print('x-value :',rando[len(rando)-1]) # last random int produced

	
def decrypt():
	rando = []
	cipherlist = []
	
	privatep = int(input('Please enter the first private key : '))
	privateq = int(input('Please enter the second private key : '))
	ciphertext = input('Please enter the ciphertext : ').replace(' ', '')
	x = int(input('Please enter the x-value: '))
	publickey = privatep * privateq
	
	for i in range(len(ciphertext)):
		cipherlist.append(ascii_lowercase.index(ciphertext[i]))
	
	p = pow(x, int((privatep + 1)/4)** (len(ciphertext)-1), privatep) # formula
	q = pow(x, int((privateq + 1)/4)** (len(ciphertext)-1), privateq) # formula
	initno = (privatep * q * pow(privatep,privateq-2,privateq) + privateq * p * pow(privateq,privatep-2,privatep)) % publickey
	
	for i in range(len(cipherlist)):
		if i == 0:
			rando.append(initno % publickey) 
		else:
			rando.append((initno ** 2 ** i) % publickey) # xi = x0 ** i mod N

	for i in range(len(cipherlist)): # M = (C - x) mod N
		cipherlist[i] = ascii_lowercase[(cipherlist[i] - rando[i]) % 26]
	print('This is your plaintext : ' + ''.join(cipherlist))


def title():
	"""Something silly."""
	print("""  ____  _                   _     _                       _           _     
 |  _ \| |                 | |   | |                     | |         | |    
 | |_) | |_   _ _ __ ___   | |__ | |_   _ _ __ ___    ___| |__  _   _| |__  
 |  _ <| | | | | '_ ` _ \  | '_ \| | | | | '_ ` _ \  / __| '_ \| | | | '_ \ 
 | |_) | | |_| | | | | | | | |_) | | |_| | | | | | | \__ \ | | | |_| | |_) |
 |____/|_|\__,_|_| |_| |_| |_.__/|_|\__,_|_| |_| |_| |___/_| |_|\__,_|_.__/ 
                                   
                                 in Python                                         
                                                                            """)

title()
	
while True:
	
	print("=== Main Menu ===")
	print('1. Make keys\n2. Encrypt\n3. Decrypt')
	choice = input('What would you like to do?: ')
	print('')
	if choice == '1': # make keys
		key()
		print('')
		continue
	elif choice == '2': # encryption
		encrypt()
		print('')
		continue
	elif choice == '3': # decryption
		decrypt()
		print('')
		continue
	else:
		print('Invalid choice! Enter 1, 2, or 3.')
		print('')
		continue
