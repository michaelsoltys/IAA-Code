Implementation of the CYK algorithm
Solution to Problem 8.49
Author: Ryan McIntyre

Given a CFG G in CNF and a string w, determines whether w is an element
of L(G). If G is not in CNF, this fact is printed instead.

Input is given in the command line:
	python cyk.py G.txt w

Where G.txt contains V;T;P;S separated by semicolons. New lines are
ignored. V is a comma separated list of variables, which may contain
multiple characters but should not contain spaces or any of the metasymbols
:;,| nor should any variable be an initial segment of another variable or
term.

T is a comma separated list of terms, which follow the same rules as
variables; also, obviously a term should not be identical to a variable.

P is a comma separated list of productions grouped by initial variable,
followed by a colon and, the possible "implications" of that variable being
separated by |.  For example, if the productions are
	P --> 0
	P --> 1
	P --> QQ
	Q --> P
	Q --> the_empty_string
	Q --> 2
then their representation in G.txt should be
	P:0|1|QQ,Q:P||2

Finally, S is the start variable, and should be a member of V.

See bin_palindrome_CFG_CNG.txt and bin_palindrome_CFG_not_CNF.txt for
examples of input format.
