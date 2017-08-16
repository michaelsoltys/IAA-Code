Implementation of the Rabin-Miller primality test
Solution to Problem 6.11
Author: Ryan McIntyre

For the naive version, Algorithm 6.3. Here we implement the
version which operates on binary strings.

In binary.py, we define binary addition, multiplication,
and exponentiation (using repeated squaring).

Call in the command line with a binary integer to test for
primality.

sample call:
	python rm.py 1001111111111

Note that this verion is slower than the naive version,
but the naive version has a lot of integers for which it
executes, but outputs a false negative with the message
"the impossible has happened".
