import readline # this makes raw_input() more 'friendly' by giving command history use of up and down arrows.

V = [] # list of vertices of the graphs, represented as strings. 
       # entries beginning with an 'rt' represent routers.
       # entries beginning with an 'nt' represent networks.
       
E = {} # dictionary of edges and their costs.  
       # edges represent connections in the graph.



def add_rt(*routers):
    global V
    '''add rt routers
    This command adds routers to the routing table, where routers is a comma separated
    list of (positive) integers and integer ranges. That is, routers can be 6,9,10-13,4,8
    which would include routers
    rt4,rt6,rt8,rt9,rt10,rt11,rt12,rt13
    Your program should be robust enough to accept any such legal sequence (including
    a single router), and to return an error message if the command attempts to add a
    router that already exists (but other valid routers in the list routers should be added
    regardless). '''
    for router in routers:
          try:
              V.index(router)
              print item + " already present"
          except ValueError:
               V += router
    print 'add rt', routers      
    
    

def del_rt(*routers):
    global V
    '''del rt routers
    Deletes routers given in routers . If the command attempts to delete a router that does
    not exist, an error message should be returned; again, we want robustness: routers that
    exist should be deleted, while attempting to delete non-existent routers should return
    an  error message (specifying the "offending" routers). The program should not stop
    after displaying an error message.  '''
    for router in routers:
            print router
            try:
                V.remove(router)
                print 'del rt', routers
            except ValueError, e:
                print router + 'not in list'
    

def add_nt(*networks):
    '''add nt networks
    Add networks as specified in networks ; same format as for adding routers. So for
    example "add nt 89" would result in the addition of nt89. The handling of errors
    should be done analogously to the case of adding routers.'''

    print 'add nt', networks

def del_nt(*networks):
    '''Deletes networks given in networks . '''
    print 'del nt', networks

def con(x, y, z):
   '''Connect node x and node y, where x, y are existing routers and networks (for example,
   x = rt8 and y = rt90, or x = nt76 and y = rt1) and z is the cost of the connection.
   If x or y does not exist an error message should be returned. Note that the network
   is directed; that is, the following two commands are not equivalent: "con rt3 rt5 1"
   and "con rt5 rt3 1."

   Important: Two networks cannot be connected directly; an attempt to do so should
   generate an error message. If a connection between x and y already exists, it is updated
   with the new cost z.'''
   
   print 'con', x, y, z

def display ():
    '''This command displays the routing table, i.e., the link-state database. For example, the
    result of adding rt3, rt5, nt8, nt9 and giving the commands "con rt5 rt3 1" and
    "con rt3 nt8 6" would display the following routing table:
        rt3 rt5 nt8 nt9
    rt3      1
    rt5
    nt8      6
    nt9

    Note that (according to the RFC 2338, describing OSPF Version 2) we read the table as
    follows: "column first, then row." Thus, the table says that there is a connection from
    rt5 to rt3, with cost 1, and another connection from rt3 to nt8, with cost 6.'''

    print 'display'

def tree (x):
    '''This commands computes the tree of shortest paths, with x as the root, from the link-
    state database. Note that x must be a router in this case. The output should be given
    as follows:

    w1 : x, v1, v2 , . . . ,vn, y1
    : no path to y2
    w3 : x, u1, u2, . . . ,um, y3 
    .
    .
    .
    where w1 is the cost of the path (the sum of the costs of the edges), from x to y1 , with
    vi's the intermediate nodes (i.e., the "hops") to get from x to y1 . Every node yj in the
    database should be listed; if there is no path from x to yj it should say so, as in the 
    above example output.
    Following the example link-state database in the explanation of the display command,
    the output of "tree rt5" would be:
    1 : rt5,rt3
    7 : rt5,rt3,nt8
    : no path to nt9
    Just as it is done in the OSPF (Open Shortest Path First) standard, the path-tree
    should be computed with Dijkstra's greedy algorithm.
    Finally, there may be several paths of the same value between two nodes; in that case,
    explain in the comments in your program how does your scheme select one of them.
    '''
    print 'tree', x

def quit ():
    '''Kills the daemon.'''
    exit(0)

functions = {
    'add rt': add_rt, 'del rt': del_rt,
    'add nt': add_nt, 'del nt': del_nt,
    'con': con, 'display': display, 'tree': tree, 'quit': quit
}

while True:
    line = raw_input ('sfwr4C03router 1.0> ')
    
    line = line.split()
    nodes = line[1].split(',')
    if line[0] == 'add':
        add_rt(nodes)
    elif line[0] == 'del':
        del_rt(nodes)
    
        
    
    
    '''
    for cmd in functions:
        if cmd == line or line.startswith(cmd + ' '):
            try:
                functions[cmd] (*(line[len(cmd) + 1:].split()))
            except TypeError, e:
                print 'you done goofed', e
	    break
    else:
        print 'you really done goofed'
        
    '''  
        
        
        
        
        
        
