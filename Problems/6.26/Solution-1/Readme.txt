Algorithm P6 - Implement the Merkle-Hellman subset-sum cryptosystem in Python


Usage:
To run encryption,
  sscript.py -e M1 M2 M3 ... Mn x
while Mn is the public keys, x is the binary string to encrypt. n must greater or equals the length of x

To run decryption,
  sscript.py -d r1 r2 .. rn  A B S
while Rn is super increasing sequence, A and B is pair of positive integers with gcd(A,B)=1 and 2Rn <B, and S is the encrypted string retrieved earlier by -e parameter

To verify secret key and A/B, run
  sscript.py -v r1 r2 .. rn  A B
while Rn is super increasing sequence, A and B is pair of positive integers with gcd(A,B)=1 and 2Rn <B


To run tests with sample data from book, simply run sscrypt_test.sh on linux,
Or on windows, rename sscrypt_test.bat_ to .bat and run it (due to gmail policy I cannot send .bat file in a zip so I have to rename it)

it will run will follow parameters:

python sscrypt.py -e 89 243 212 150 245 10101
python sscrypt.py -d 3 11 24 50 115 113 250 546
python sscrypt.py -v 3 11 24 50 115 113 250