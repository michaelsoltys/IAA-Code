Solution to Problem 6.21
Implementation of ElGamal Digital Signiture Scheme
Author: Ryan McIntyre

Input is given in the command line:
	prime p (will not be checked for primality)
	integers g,x,k in Zp-{0} s.t. gcd(p-1,k)=1

Call in command line:
	python sign.py 11 6 3 7

After call, user will be prompted for a message.
Type your message, and hit enter. The signature
will be printed.

Output is x such that g^x = h (mod p).
