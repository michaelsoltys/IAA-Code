# Matthew Morales
# From: https://github.com/slimpig879/DFA.git

import random

# ">" corresponds to an input state, the following integers correspond to a transition based on 0, 1 input, the final number is just a State Number Used for recombining the table.
# "*" corresponds to a final state
def read_transition_file():
	transition_table = open("transition.txt","r")
	lines = transition_table.readlines()
	transition_table.close()

	state_list = []
	table = {}

	for line in lines:
		state_list.append(line.rstrip('\n').split('|'))

	#print 'q' + state_list[0][3] #just testing the concatenation of q + state

	for entry in state_list:
		for x in range(1, 3):
			entry[x] = 'q' + entry[x]
		table['q' + entry[3]] = entry

	return table

def print_table(t_table):
	for item in t_table:
		if t_table.get(item)[0] == ">":
			print("%s|  %s %s : %s" % (item, t_table.get(item)[0], t_table.get(item)[1], t_table.get(item)[2]))
		elif t_table.get(item)[0] == "*":
			print("%s|  %s %s : %s" % (item, t_table.get(item)[0], t_table.get(item)[1], t_table.get(item)[2]))
		else:
			print("%s|    %s : %s" % (item, t_table.get(item)[1], t_table.get(item)[2]))

def distinguishable(test_group, final):
	
	while test_group:
		#do while test_group is not empty
		test_a = {}
		sample_state = random.choice(test_group.keys()) #select a random state from the remaining non_final states
		test_a[sample_state] = test_group.pop(sample_state)
		poppable_states = []

		#compare Test Group A to test Group B, if Something in B indistinguishable from A, Pop off B. Remainder need to be Retested against a Random State from B.
		#Repeat until Test Group B is Empty.
		for item in test_a:
			for states in test_group:
				if test_a[item][1] == test_group[states][1] and test_a[item][2] == test_group[states][2]: 
					print "states are indistingquishable:"
					print test_a[item]
					print test_group[states]

					#states are indistingquishable. Replace all references to test_group state just tested. 
					poppable_states.append(states)
					for entry in test_group:
						if test_group.get(entry)[1] == states:
							test_group[entry][1] = item
							
						if test_group.get(entry)[2] == states:
							test_group[entry][2] = item
					
			#remove indistinguishable state from test group.
			for pops in poppable_states:
				print("Popping indistinguishable state: %s" % (pops))
				test_group.pop(pops)
		final[item] = test_a.pop(item)

	poppable_entries = []
	#explicitly equal states taken care of above, states with equivalent looping patterns dealt with below
	for state in final:
		for entry in final:
			if state != entry:
				#making sure not to check a state against itself, thus popping a potentially distinguished state
				if final[state][1] == entry and final[entry][1] == state and final[entry][2] == final[state][2]:
					#print ("State: %s" % (state))
					#print ("Entry: %s" % (entry))
					#the states loop back on each other and can be combined.
					if state not in poppable_entries:
						poppable_entries.append(entry)
						#remove references to states slated for removal
						if final[state][1] == entry:
							final[state][1] = state
						if final[state][2] == entry:
							final[state][2] = state
				if final[state][2] == entry and final[entry][2] == state and final[entry][1] == final[state][1]:
					#states loop back on each other
					if state not in poppable_entries:
						poppable_entries.append(entry)

	for pops in poppable_entries:
		print("Popping indistinguishable state: %s" % (pops))
		final.pop(pops)

	return final

t_table = read_transition_file()
print_table(t_table)

final = {}
non_final = {}

# splitting states based on accepting ('final') states and rejecting ('non_final') states
for items in t_table:
	if t_table.get(items)[0] == "*" :
		final[items] = t_table.get(items)
	else:
		non_final[items] = t_table.get(items)

dfa_min = distinguishable(non_final, final)

print_table(dfa_min)