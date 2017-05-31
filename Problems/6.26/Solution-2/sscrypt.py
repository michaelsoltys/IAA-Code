# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 6.26
## Matthew Morales
## Spring 2015
## python 3

import random
import sys

argument = sys.argv[1]

#receive binary string
def receive_binary():

	return input("Enter Binary String: ")

#create super increasing set, based on string size
def super_increasing(n):
	print n
	a = []
	rolling_sum = 1
	for entry in n:
		a.append(rolling_sum)
		rolling_sum = 2*rolling_sum

	return a

#generate a list of completely reduced fractions from 0 to 1 w/ n being the largest denominator.
#fractions are listed from smallest to largest, by their nature, completely reduced fractions are created by coprime pairs
def farey(n): #this is where the program slows down incredibly, as the string grows
    def gcd(a,b):
        while b: a,b = b,a%b
        return a

    def simplify(a,b):
        g = gcd(a,b)
        return (a/g,b/g)

    fs = dict()
    for i in xrange(1,n+1):
        for i2 in xrange(1,i+1):
            if i2 < n and i != i2:
                r = simplify(i2,i)
                fs[float(i2)/i] = r

    return [fs[k] for k in sorted(fs.keys())] 

#generate a number larger than sigma_sequence, and a comprime less than said random number
def coprime_pairs(sigma):
	q = int(random.random() * 100)
	q = q + sigma

	coprimes = farey(q)
	#note: the above tuples of coprime pairs are ALL coprime pairs less than q. Now we need to select a reasonable one, done below.

	for item in coprimes:
		if item[1] > sigma:
			if item[0] > int(q/4):
				used_pair = item
				break
	return used_pair

#creat public key
def public_key(w, pairs):
	beta = []

	for item in w:
		beta.append(item*pairs[0] % pairs[1])

	return beta

#encrypt using keys
def encrypt(input, beta_key):
	knapsack = 0
	counter = 0
	for item in input:
		knapsack = knapsack + (int(item) * beta_key[counter])
		print("string: (%s)   beta: (%s)" % (item, beta_key[counter]))
		counter += 1
	return knapsack

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def decrypt(encrypted, r, q, w):
	modular_inv = modinv(r, q)
	counter = 0
	rebuild_array = []
	decrypted_message_array = []
	decrypted_message = ""

	midcrypt = (encrypted * modular_inv) % q
	#print("midcrypt (%s)" % (midcrypt))
	#print("w (%s)" % (w))

	for entry in reversed(w):
		decrypted_message_array.append(0)
		if entry <= midcrypt:
			midcrypt = midcrypt - entry
			rebuild_array.append(counter)
		counter += 1
	#print rebuild_array

	for entry in rebuild_array:
		decrypted_message_array[entry] = 1

	decrypted_message_array.reverse()

	for item in decrypted_message_array:
		decrypted_message = decrypted_message + str(item)

	return decrypted_message

def write_encrypted_message(message):

	print('Generating encrypted.txt') 
	name = 'encrypted.txt'  # Name of text file coerced with +.txt
	try:
		file = open(name,'wb')   # Trying to create a new file or open one
		file.write(str(message))
		file.close()

	except:
		print('File Creation Failed')
		sys.exit(0) # quit Python

def write_decrypted_message(message):

	print('Generating decrypted.txt') 
	name = 'decrypted.txt'  # Name of text file coerced with +.txt
	try:
		file = open(name,'wb')   # Trying to create a new file or open one
		file.write(str(message))
		file.close()

	except:
		print('File Creation Failed')
		sys.exit(0) # quit Python

def write_public_key(key):
	print('Generating public.txt') 

	name = 'public.txt'  # Name of text file coerced with +.txt
	
	try:
		file = open(name,'wb')   # Trying to create a new file or open one
		for item in key:
			file.write(str(item))
			file.write("\n")
		file.close()

	except:
		print('File Creation Failed')
		sys.exit(0) # quit Python

def write_private_key(w, q, r):
	print('Generating private.txt') 

	name = 'private.txt'  # Name of text file coerced with +.txt

	try:
		file = open(name,'wb')   # Trying to create a new file or open one
		for item in w:
			file.write(str(item))
			file.write("|")

		file.write("\n")
		file.write(str(q))
		file.write("\n")
		file.write(str(r))
		file.close()

	except:
		print('File Creation Failed')
		sys.exit(0) # quit Python

def parse_private():  #returns keys as a tuple of the form (superincreasing sequence, number chosen as larger than the sum of S_I Sequence, and Q's Coprime)
	private_keys = open("private.txt")
	lines = private_keys.readlines()
	private_keys.close()

	w = (lines[0].rstrip('\n').split('|'))
	w.pop(-1)
	w = map(int, w)
	q = int(lines[1].rstrip('\n'))
	r = int(lines[2].rstrip('\n'))

	keys = (w, q, r)
	
	return keys

def parse_encrypted_message():
	message = open("encrypted.txt")
	content = int(message.read())
	return content

def check_super_increasing(w):
	rolling_total = 0
	check = True
	for item in w:
		if item > rolling_total:
			rolling_total = rolling_total + item
		else:
			print "W is not a Super Increasing Sequence"
			check = False
			sys.exit(0)
	if check == True:
		print("W: %s is a Super Increasing Sequence" % (w))

if argument == '-e':
	#encrypt, write public key to file, encrypted message to file, private keys to file
	binary_string = str(receive_binary())
	s_i_sequence = super_increasing(binary_string)
	sigma_sequence = s_i_sequence[-1] + (s_i_sequence[-1]-1)

	used_pairs = coprime_pairs(sigma_sequence)
	beta = public_key(s_i_sequence, used_pairs)

	encrypted_mess = encrypt(binary_string, beta)

	write_encrypted_message(encrypted_mess)
	write_public_key(beta)
	write_private_key(s_i_sequence, used_pairs[1], used_pairs[0])

elif argument == '-d':
	#decrypt using private keys
	keys = parse_private()
	encrypted_mess = parse_encrypted_message()

	decrypted = decrypt(encrypted_mess, keys[2], keys[1], keys[0])
	print decrypted
	write_decrypted_message(decrypted)

elif argument =='-v':
	#verify w is super increasing (from text file) and that GCD(q,r) = 1 and prints the corresponding public key
	keys = parse_private()

	check_super_increasing(keys[0])
	#print keys[0]
	#check that 2w[n] is < q, super quick, not going to make another function for that
	print "2r[n] < B" if (2*keys[0][-1]) < keys[1] else "2r[n] !< B"
	if egcd(keys[1], keys[2])[0] == 1:
		print("The greatest common denominator of %s and %s is 1" % (keys[1], keys[2]))
	else:
		print("The greatest common denominator of %s and %s is **NOT** 1" % (keys[1], keys[2]))
	print "The public key is as follows: "
	print public_key(keys[0], (keys[2], keys[1]))
else:
	print 'Invalid Argument Passed'