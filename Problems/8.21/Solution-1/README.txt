Solution to Problem 8.21
Implementation of DFA minimization
Author: Ryan McIntyre

Input is a text file formatted as described in the text,
but with commas instead of spaces. See input.txt for a sample
matching figure 8.10*, where rows represent states in alphabetical
order.

Call in command line:
	python minimize.py input.txt output.txt

Output is formatted the same as the input. It is printed in the
console and written to the designated file. If no output file is
named, the result is written to "./output_of_<input_filename>.txt".

* fig:dfa-to-table
