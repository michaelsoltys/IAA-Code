Implementation of Algorithm 6.3 - the Rabin-Miller primality test.
Author: Ryan McIntyre

Input: any positive integer n. Optional # of iterations (default 20).

Output: "True" if n is prime. Probably "False" if n is not prime.
Chance that output is "True" for non-prime input is (much) less 
than (1/2)^(# of iterations).
