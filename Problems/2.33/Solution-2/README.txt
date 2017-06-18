Solution to Problem 2.33 
Author: Ryan McIntyre

Allows user to input routers, networks, and weighted connections with 
commands as specified in the text. See "tree" command for implementation
of Dijkstra's algorithm.

Run in the command line:
	python routed.py

For specifications of inputs, see the text. This version will accept,
in place of 'rt', the equivalents 'Rt','RT','router','Router','ROUTER'
in all arguements. Other keywords have been expanded in a similar
fashion.

I've also added the "save", "load", and "list" keywords.
	"save <name>" saves the current setup under the key "name"
	"save list" prints a list of all saves
	"load <name>" attempts to load save labelled "name"
