Solution to Problem 2.33 
Author: Ryan McIntyre

Allows user to input routers, networks, and weighted connections with 
commands as specified in the text. See "tree" command for implementation
of Dijkstra's algorithm.

Run in the command line:
	python routed.py

For specifications of inputs, see the text or the end of this readme. This
version will accept, in place of 'rt', the equivalents 'Rt', 'RT',
'router', 'Router', 'ROUTER' in all arguements. Other keywords have been
expanded in a similar fashion.

I've also added the "save", "load", and "list" keywords:

	"save <name>" saves the current setup under the key "name"
	"save list" prints a list of all saves
	"load <name>" attempts to load save labelled "name"

Inputs from text:

	"add rt <routers>"
		adds routers
		accepts integers and integer ranges, comma-separated
		i.e. "add rt 1,4-8" adds rt1, rt4,rt5,rt6,rt7,rt8

	"add nt <networks>"
		adds networks in a manner identical to "add rt <routers>"

	"del rt <routers>", "del nt <networks>
		deletes routers / networks individually or in ranges

	"con <x y z>"
		connects nodes x and y (which are existing routers / networks) with
		weight or cost z

	"display"
		displays the currently loaded setup

	"tree <x>"
		computes the tree of shortest paths from x to every other router or
		network, and displays the result

	"quit"
		quits
