# Tiffany Antopolski (collaborated with Vineet Sharma).
# antopota
# sfwreng4c03, assignment #2
# March 7, 2011

'''
tiffany@kilmer:~$ python
>>> import routed
>>> help(routed)
Help on module routed:

NAME
    routed

FILE
    /home/tiffany/Desktop/antopota/routed/routed.py

DESCRIPTION
    # Tiffany Antopolski (collaborated with Vineet Sharma).
    # antopota
    # swreng4c03, assignment #2
    # March 7, 2011

FUNCTIONS
    add(prefix, ranges)
        Invoked by the add command to add routers and networks to the routing table, depending on the prefix.
        If prefix == rt ----> router is added, if prefix == nt ----> network is added.
    
    con(src, dest, cost)
        Connects src to dest, where src, dest are existing routers and networks and cost is the cost of the connection.
        If a connection between src and dest already exists, it is updated with the new cost.
    
    display()
        Invoked by the display command to display the routing table (link-state database).
    
    expand(prefix, ranges)
        Expands the vertices (given by prefix) into the routers given in the range.
    
    find_first_by(distance, candidates)
        Finds the first best candidate.
    
    main()
        Routing table management daemon.
    
    neighbours(u, Q)
        Returns the neighbouring nodes connected to u.
    
    quit()
        Invoked by the quit command to exit the program.
    
    rm(prefix, ranges)
        Invoked by the del command to delete routers and networks from the routing table. If prefix = rt ---> router
        is removed, if prefix == nt --> network is removed.
    
    test()
        Test cases for the program.  To run, type 'test' without the quotes at the prompt.
    
    tree(source)
        Invoked by the tree command.  Computes the tree of shortest paths with source as the root,
        from the link-state database.  Source must be a router.  The path-tree is computed with Dijkstra's
        greedy algorith.

DATA
    E = {}
    V = []
    infinity = inf
'''

# The 'big' design desicion of routed.py was how to store the routing table.  I decided to store the vertices(nodes) of 
# the graph as a list of vertices.  Then, when nodes are connected, the connections are stored in a dictionary, where
# each connection is a 'key: value' pair.  The key is a tuple consisting of the two nodes that make the edge, and the 
# value is the cost of that particular connection.  This dictionary (stored in E) is the description of the digraph
# created by adding routers to V and connections to E.
#
# The functions 'add' and 'rm'(for remove) co-routine with the 'expand' function.  These funcitons are  responsible for 
# adding and removing vertices from V.  'rm' is also  responsible for deleting connections from E, if the vertex to 
# be removed is part of a connection.  The 'rm' function name was chosen over the more obvious 'del' because del is a 
# Python keyword.
#
# No problems major problems where encountered.  The 'robust' behaviour described in the assignment handout was 
# implemented along with a couple of extra features:
# 1. Negative cost edges cannot be added to the routing table
# 2. A node (nt or rt) cannot be connected to itself
# 
# The tree function lists all the shortest paths to all the nodes in the graph from a given router source.  If the graph
# happens to contain two or more shortest paths to a node, then the path with the highest cost edge going into the 
# destination is the one that will be traversed.  If the edges of two shortest paths have exactly the same weights, 
# then the one with vertices added first will be traveversed.
#
# There where no real problems encountered while solving this problem.  Understanding the problem and how Dijkstra's 
# algorithm applies was the rate limiting step.

import readline # gives commandline powers to raw_input (i.e. commandline history, arrow up and arrow down).

infinity = float('inf')
V = [] # list of vertices
E = {} # list of directed edges

def expand(prefix, ranges):
    '''Expands the vertices (given by prefix) into the routers given in the range.'''
    
    if prefix != 'nt' and prefix != 'rt': # only rt and nt type vertices are allowed
        raise ValueError('expecting rt or nt;', prefix, 'given.')

    for i in ranges.split(','):
        if '-' in i:
            # expand the range
            try:
                start, end = i.split('-')
                for k in xrange(int(start), int(end) + 1):
                    yield prefix + str(k)

            except ValueError:
                print 'warning: malformed range', i
        else:
            # just a single number
            try:
                yield prefix + str(int(i))

            except ValueError:
                print 'warning: invalid integer', i

def add(prefix, ranges):
    '''Invoked by the add command to add routers and networks to the routing table, depending on the prefix.
    If prefix == rt ----> router is added, if prefix == nt ----> network is added.'''
    
    for vertex in expand(prefix,ranges):
        if vertex in V:
            print "warning:", vertex, "already added."
        else:
            V.append(vertex)

def rm(prefix, ranges):
    '''Invoked by the del command to delete routers and networks from the routing table. If prefix = rt ---> router
    is removed, if prefix == nt --> network is removed.'''
    
    for vertex in expand(prefix, ranges):
        if vertex in V:
              V.remove(vertex)
              connections = [] # create list of all the connections formed by the vertex to be removed.
              for v1,v2 in E:
                  if v1 == vertex or v2 == vertex:
                      connections.append((v1,v2))

              # delete the connections
              for edge in connections:
                  del E[edge]
        else:
            print "warning:", vertex, "does not exist."

def con(src, dest, cost):
    '''Connects src to dest, where src, dest are existing routers and networks and cost is the cost of the connection.
    If a connection between src and dest already exists, it is updated with the new cost.'''
    
    if src not in V:
        raise KeyError(src + ' is not a known node')

    if dest not in V:
        raise KeyError(dest + ' is not a known node')

    if src == dest:
        raise ValueError('Unable to connect a node to itself.')

    if src.startswith('nt') and dest.startswith('nt'):
        raise ValueError('Unable to connect two networks.')

    cost = int(cost)
    if cost < 0:
        raise ValueError('can not connect with a negative cost')

    E[(src, dest)] = cost

def find_first_by(distance, candidates):
    '''Finds the first best candidate.'''
    
    least_distance = infinity
    best_candidate = None

    for candidate in candidates:
        if distance[candidate] < least_distance:
            least_distance = distance[candidate]
            best_candidate = candidate

    # best_candidate may be None if we didn't find a finite distance
    return best_candidate

def neighbours(u,Q):
    '''Returns the neighbouring nodes connected to u.'''
    
    v = []
    for node in Q:
        if (node != u and ((u,node) in E)):
            v.append(node)
    return v

def tree(source):
    '''Invoked by the tree command.  Computes the tree of shortest paths with source as the root,
    from the link-state database.  Source must be a router.  The path-tree is computed with Dijkstra's
    greedy algorith.'''

    if source.startswith('nt'):
        raise ValueError('Tree source must be a router.')

    distance = {} # dicationary of distances (initially 0 to source, infinity to all other vertices.
    previous = {} # dictionary of previous vertices visiited.

    for v in V:
        # initialisation
        distance[v] = infinity
        previous[v] = None

    distance[source] = 0
    Q = list(V)

    while Q:
        u = find_first_by(distance, Q)

        if not u:
            # Found no items with non-infinite distance therefore
            # all remaining items are disconnected from the graph
            break

        Q.remove(u)

        for v in Q:
            if (u, v) in E:
                alt = distance[u] + E[(u,v)]
                if alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u

    for vertex in V:
        # do not display the source node
        if vertex != source:
            if distance[vertex]<infinity:
                path = []
                print distance[vertex],'\t : ',
                path.append(vertex)
                vertex = previous[vertex]
                while vertex:
                    path.append(vertex)
                    vertex = previous[vertex]
                print ','.join(reversed(path))

            else:
                print ' ','\t : ','no path to',vertex

def display():
    '''Invoked by the display command to display the routing table (link-state database).'''
    
    # print a header with source across
    print
    print
    print '    **          **FROM**    '
    print '    TO'
    print '    **',
    for src in V:
        print '%6s ' % (src,),
    print

    # print the rows of the routing table
    for dest in V:
        # print the destination at the start of the row
        print '%6s ' % (dest,),

        # do the columns...
        for src in V:
           if (src,dest) in E:
               print '%6d ' % (E[(src,dest)],),
           else:
               print '       ',
        # newline at the end of the row
        print

def quit():
    '''Invoked by the quit command to exit the program.'''
    
    exit()


def main():
    '''Routing table management daemon.'''
    
    while True:
        try:
            line = raw_input('routed 1.0> ')
            line = line.split()

            command = line[0]
            args = line[1:]

            try: # get the command and invoke the appropriate function.
                if command == 'add':
                    add(*args)
                elif command == 'del':
                    rm(*args)
                elif command == 'con':
                    con(*args)
                elif command == 'display':
                    display(*args)
                elif command == 'quit':
                    quit(*args)
                elif command == 'tree':
                    tree(*args)
                elif command == 'test':
                    test()
                else:
                    raise ValueError('Unknown command:', command)
            except Exception, e:
                print 'error: ', e
        except IndexError, e:
            print 'error: Enter a command,', e  
def test():
    '''Test cases for the program.  To run, type 'test' without the quotes at the prompt.'''
    
    # try to break the loop without using quit
    print 'routed 1.0> add wt 3,4,5-10'
    try:
        add('wt', '3,4,5-10')
    except Exception, e:
        print e
    print ########################################
    print 'routed 1.0> con rt1 rt2 1'
    try:
        con('rt1', 'rt2', '1')
    except Exception, e:
        print e
    print ########################################
    print 'routed 1.0> add rt 1, 1-3'
    add('rt', '1,1-3')
    print ########################################
    print 'routed 1.0> del rt 1-4'
    try:
        rm('rt','1-4')
    except Exception, e:
        print e
    print ########################################
    print 'routed 1.0> add rt 6.9,10,10-13,4,8'
    add('rt', '6,9,10-13,4,8')
    print ########################################
    print 'routed 1.0> add nt 1,2'
    add('nt', '1,2')
    print ########################################
    print 'routed 1.0> con rt3 rt1 1'
    con('rt3', 'rt1', '1')
    print 'routed 1.0> con rt1 nt1 1'
    con('rt1', 'nt1', '1')
    print 'routed 1.0> con rt3 nt1 2'
    con('rt3', 'nt1', '2')
    print 'routed 1.0> con rt3 rt2 1'
    con('rt3', 'rt2', '1')
    print 'routed 1.0> con rt2 nt1 1'
    con('rt2', 'rt1', '1')
    print ########################################
    print 'routed 1.0> tree rt3'
    tree('rt3')
    print ########################################
    print 'display'
    display()
    print ########################################
    print 'routed 1.0> add rt 11, 12, 13, 14'
    try:
        add('rt', '11, 12, 13, 14')
    except Exception, e:
        print e
    print ########################################

if (__name__ == '__main__'):
    main()
