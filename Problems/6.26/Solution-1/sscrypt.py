# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 6.26
## Qingwen Zhu
## python 3

__author__ = 'Qingwen Zhu'

import sys;


# get Great Common Division
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# get Mode Inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# function for calculate the encrypted string S from Mn and x
def encrypt(Ms, x):
    print("Start encyption, input parameters are:")
    print("  List of M:" + str(Ms));
    print("  x:" + x);
    print("Computing S:");
    S = 0;
    for i in range(len(x)):
        print(str(Ms[i]) + ":" + x[i]);
        S = S + int(Ms[i]) * int(x[i]);

    print("Caculated S: " + str(S));

    print("The Encrypted string is " + str(S));
    return S;

# function for decrypt the encrypted string S from public key Rn and integer pair (A,B) and the encrypted String S

def decrypt(Rn, A, B, S):
    print("Start decyption, input parameters are:")
    print("  List of R:" + str(Rn));
    print("  A:" + str(A));
    print("  B:" + str(B));
    print("  S:" + str(S));
    print("Computing :");
    #calculate the A Inverse Mod B
    AinvmodB = modinv(A, B);
    print("  inverse of " + str(A) + " in mod " + str(B) + " is " + str(AinvmodB));
    decryptedS = S * AinvmodB % B;
    print(" S multiple A inv mod B  then mod B is " + str(decryptedS));
    print("Apply simple greedy to \"" + str(decryptedS) + "\" restore the original value :");
    remainingS = decryptedS
    originalString = "";
    #Apply Simple greedy algorithm to decrypt the S
    for i in range(len(Rn) - 1, -1, -1):
        if remainingS >= Rn[i]:
            remainingS = remainingS - Rn[i];
            originalString = "1" + originalString;
            print("      [debug]  for R[" + str(i) + "]:deduct:" + str(Rn[i]) + ",remaining:" + str(remainingS))
        else:
            originalString = "0" + originalString;

    print("Final Decrypted String is: " + originalString);
    return originalString;

# function for verify the public key Rn and integer pair (A,B)

def verification(Rn, A, B):
    print("Start verification, input parameters are:")
    print("  List of R:" + str(Rn));
    print("  A:" + str(A));
    print("  B:" + str(B));

    #verify if the Greatest Common Divisor is 1
    if egcd(A, B)[0] != 1:
        error_verification(True, "!!!A(" + str(A) + ") and B(" + str(B) + ") do not satisfy  gcd(A,B)=1");
        exit(0);
    #verify if Rn is super increasing
    for i in range(len(Rn) - 1):
        if Rn[i] * 2 > Rn[i + 1]:
            error_verification(True, "!!! R[" + str(i) + "]=" + str(Rn[i]) + " is larger than R[" + str(
                i + 1) + "]=" + str(Rn[i + 1]) + "/2, please fix input!");
            exit(0);
    print("Computing ...");
    #calculate the Mn by using equation Mn = A* Rn mod B
    M = [A * r % B for r in Rn];
    print("Calculated Mn: "+str(M));


def error_encryption(w,detail=False):
    if w:
        print("Wrong input, please in the format:");
    else:
        print("To run encryption,")
    print("  sscript.py -e M1 M2 M3 ... Mn x");
    print("while Mn is the public keys, x is the binary string to encrypt. n must greater or equals the length of x");
    if (detail):
        print(detail);


def error_decryption(w, detail=False):
    if w:
        print("Wrong input for decryption, please in the format:");
    else:
        print("To run decryption,")
    print("  sscript.py -d r1 r2 .. rn  A B S");
    print("while Rn is super increasing sequence, A and B is pair of positive integers with gcd(A,B)=1 and 2Rn <B");
    print("S is the encrypted string retrieved earlier by -e parameter\r\n");
    if (detail):
        print(detail);


def error_verification(w, detail=False):
    if w:
        print("Wrong input, please in the format:");
    else:
        print("To verify secret key and A/B, run")
    print("  sscript.py -v r1 r2 .. rn  A B");
    print("while Rn is super increasing sequence, A and B is pair of positive integers with gcd(A,B)=1 and 2Rn <B\r\n");
    if (detail):
        print(detail);


def usage():
    print("Sscrypt by Qingwen Zhu - Simple  Merkle-Hellman subset-sum cryptosystem implementation");
    print("Usage:");
    error_encryption(False);
    print("");
    error_decryption(False);
    print("");
    error_verification(False);

if (len(sys.argv)) < 2:
    usage();
    exit(0);
action = sys.argv[1]
if action == '-e':
    x = str(sys.argv[-1]);
    Ms = sys.argv[2:-1];
    if len(sys.argv) < 4 or len(x) > len(Ms):
        error_encryption(True, "!!! your inputted Mn is too short");
        exit(0);
    encrypt(Ms, x);
elif action == '-d':
    if len(sys.argv) < 5:
        error_decryption(True, "!!! your inputted Rn is too short");
        exit(0);
    Rn = [int(n) for n in sys.argv[2:-3]];
    A = int(sys.argv[-3]);
    B = int(sys.argv[-2]);
    S = int(sys.argv[-1]);
    #verify if the Greatest Common Divisor is 1
    if egcd(A, B)[0] != 1:
        error_decryption(True, "!!!A(" + str(A) + ") and B(" + str(B) + ") do not satisfy  gcd(A,B)=1");
        exit(0);
    #verify if Rn is super increasing
    for i in range(len(Rn) - 1):
        if Rn[i] * 2 > Rn[i + 1]:
            error_decryption(True,
                             "!!! R[" + str(i) + "]=" + str(Rn[i]) + " is larger than R[" + str(i + 1) + "]=" + str(
                                 Rn[i + 1]) + "/2, please fix input!");

    decrypt(Rn, A, B, S);

elif action == '-v':
    if len(sys.argv) < 3:
        error_verification(True, "!!! your inputted Rn is too short");
        exit(0);
    Rn = [int(n) for n in sys.argv[2:-2]];
    A = int(sys.argv[-2]);
    B = int(sys.argv[-1]);
    verification(Rn, A, B);
else :
    usage();

    exit(0);