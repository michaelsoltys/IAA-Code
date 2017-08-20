# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 2.33 - Routing
## Ryan McIntyre
## 6/7/2017
## python 3.5.2

import os

class route:
    
    def __init__(self):
        self.rt = set()
        self.nt = set()
        self.cons = dict()
        self.cur_save = None
        
        self.like = dict()
        self.like['add'] = set(['add','Add','ADD','+'])
        self.like['rt'] = set(['rt','Rt','RT','router','Router','ROUTER',])
        self.like['nt'] = set(['nt','Nt','NT','network','Network','NETWORK',])
        self.like['del'] = set(['del','Del','DEL','delete','Delete','DELETE','-'])
        self.like['con'] = set(['con','Con','CON','connect','Connect','CONNECT','c'])
        self.like['display'] = set(['display','Display','DISPLAY'])
        self.like['quit'] = set(['quit','Quit','QUIT','exit','Exit','EXIT','q'])
        self.like['tree'] = set(['tree','Tree','TREE'])
        self.like['save'] = set(['save','Save','SAVE'])
        self.like['load'] = set(['load','Load','LOAD'])
        self.like['yes'] = set(['yes','Yes','YES','y'])
        self.like['no'] = set(['no','No','NO','n'])
        self.like['list'] = set(['list','List','LIST'])
        
    def reset(self):
        self.rt = set()
        self.nt = set()
        self.cons = dict()
        self.cur_save = None
        
    def add_rt(self,n_list):
        invalid = []
        repeat = []
        entry_list = n_list.split(',')
        for entry in entry_list:
            entrys = entry.split('-')
            if len(entrys)==1:
                try:
                    n = int(entrys[0])
                    if not n in self.rt:
                        self.rt.add(n)
                    else:
                        repeat.append(n)
                except:
                    invalid.append(entry)
            elif len(entrys)==2:
                try:
                    n1 = int(entrys[0])
                    n2 = int(entrys[1])
                    if n1>n1:
                        n1,n2 = n2,n1
                    for n in range(n1,n2+1):
                        if not n in self.rt:
                            self.rt.add(n)
                        else:
                            repeat.append(n)
                except:
                    invalid.append(entry)
            else:
                invalid.append(entry)
        if len(repeat) or len(invalid):
            print(' ')
        if len(repeat)>0:
            print('The following weren\'t added, as they were already routers or were repeated:')
            print('    '+', '.join(['rt'+str(label) for label in repeat]))
        if len(invalid)>0:
            print('The following weren\'t added, as they were incorrectly formatted:')
            print('    '+', '.join(invalid))
        if len(repeat) or len(invalid):
            print(' ')
    
    def del_rt(self,n_list):
        invalid = []
        dne = []
        entry_list = n_list.split(',')
        for entry in entry_list:
            entrys = entry.split('-')
            if len(entrys)==1:
                try:
                    n = int(entrys[0])
                    if n in self.rt:
                        self.rt.remove(n)
                        pairs = set()
                        for pair in self.cons:
                            if 'rt'+str(n) in pair:
                                pairs.add(pair)
                        for pair in pairs:
                            self.cons.pop(pair)
                    else:
                        dne.append(n)
                except:
                    invalid.append(entry)
            elif len(entrys)==2:
                try:
                    n1 = int(entrys[0])
                    n2 = int(entrys[1])
                    if n1>n1:
                        n1,n2 = n2,n1
                    for n in range(n1,n2+1):
                        if n in self.rt:
                            self.rt.remove(n)
                            pairs = set()
                            for pair in self.cons:
                                if 'rt'+str(n) in pair:
                                    pairs.add(pair)
                            for pair in pairs:
                                self.cons.pop(pair)
                        else:
                            dne.append(n)
                except:
                    invalid.append(entry)
            else:
                invalid.append(entry)
        if len(dne) or len(invalid):
            print(' ')
        if len(dne)>0:
            print('The following weren\'t deleted, as they weren\'t routers (or were repeated):')
            print('    '+', '.join(['rt'+str(label) for label in dne]))
        if len(invalid)>0:
            print('The following weren\'t deleted, as they were incorrectly formatted:')
            print('    '+', '.join(invalid))
        if len(dne) or len(invalid):
            print(' ')
    
    def add_nt(self,n_list):
        invalid = []
        repeat = []
        entry_list = n_list.split(',')
        for entry in entry_list:
            entrys = entry.split('-')
            if len(entrys)==1:
                try:
                    n = int(entrys[0])
                    if not n in self.nt:
                        self.nt.add(n)
                    else:
                        repeat.append(n)
                except:
                    invalid.append(entry)
            elif len(entrys)==2:
                try:
                    n1 = int(entrys[0])
                    n2 = int(entrys[1])
                    if n1>n1:
                        n1,n2 = n2,n1
                    for n in range(n1,n2+1):
                        if not n in self.nt:
                            self.nt.add(n)
                        else:
                            repeat.append(n)
                except:
                    invalid.append(entry)
            else:
                invalid.append(entry)
        if len(repeat) or len(invalid):
            print(' ')
        if len(repeat):
            print('The following weren\'t added, as they were already networks or were repeated:')
            print('    '+', '.join(['nt'+str(label) for label in repeat]))
        if len(invalid):
            print('The following weren\'t added, as they were incorrectly formatted:')
            print('    '+', '.join(invalid))
        if len(repeat) or len(invalid):
            print(' ')

    def del_nt(self,n_list):
        invalid = []
        dne = []
        entry_list = n_list.split(',')
        for entry in entry_list:
            entrys = entry.split('-')
            if len(entrys)==1:
                try:
                    n = int(entrys[0])
                    if n in self.nt:
                        self.nt.remove(n)
                        pairs = set()
                        for pair in self.cons:
                            if 'nt'+str(n) in pair:
                                pairs.add(pair)
                        for pair in pairs:
                            self.cons.pop(pair)
                    else:
                        dne.append(n)
                except:
                    invalid.append(entry)
            elif len(entrys)==2:
                try:
                    n1 = int(entrys[0])
                    n2 = int(entrys[1])
                    if n1>n1:
                        n1,n2 = n2,n1
                    for n in range(n1,n2+1):
                        if n in self.nt:
                            self.nt.remove(n)
                            pairs = set()
                            for pair in self.cons:
                                if 'nt'+str(n) in pair:
                                    pairs.add(pair)
                            for pair in pairs:
                                self.cons.pop(pair)
                        else:
                            dne.append(n)
                except:
                    invalid.append(entry)
            else:
                invalid.append(entry)
        if len(dne) or len(invalid):
            print(' ')
        if len(dne)>0:
            print('The following weren\'t deleted, as they weren\'t networks or were repeated:')
            print('    '+', '.join(['nt'+str(label) for label in dne]))
        if len(invalid)>0:
            print('The following weren\'t deleted, as they were incorrectly formatted:')
            print('    '+', '.join(invalid))
        if len(dne) or len(invalid):
            print(' ')

    def con(self,x,y,w):
        for word in self.like['nt']:
            x = x.replace(word,'nt')
            y = y.replace(word,'nt')
        for word in self.like['rt']:
            x = x.replace(word,'rt')
            y = y.replace(word,'rt')
        tx = ''
        ty = ''
        try:
            tx = x[:2]
            ty = y[:2]
        except:
            print('\nInvalid network / router identifiers.\n Try "rt" for rouger or "nt" for network.\n')
        else:
            vx = 0
            vy = 0
            if not tx in ['rt','nt']:
                print('\n"'+tx+'" is not a valid node type.\n Try "rt" for router or "nt" for network.\n')
            elif ty not in ['rt','nt']:
                print('\n"'+tx+'" is not a valid node type.\n Try "rt" for router or "nt" for network.\n')
            elif tx=='nt' and ty=='nt':            
                print('\nCan\'t connect two networks.\n')
            else:
                try:
                    vx = int(x[2:])
                    vy = int(y[2:])
                except:
                    print('\nRouters or networks are identified by integers (e.g. rt85, nt72).\n')
                else:
                    if not vx in eval('self.'+tx):
                        print('\n',x,'doesn\'t exist.\n')
                    elif not vy in eval('self.'+ty):
                        print('\n',y,'doesn\'t exist.\n')
                    else:
                        try:
                            w = eval(w)
                            if w<0:
                                print('\nInvalid weight',w,'.\n Costs must be positive to add or 0 to delete.\n')
                            elif w==0:
                                if (x,y) in self.cons:
                                    self.cons.pop((x,y))
                                else:
                                    print('\nCannot delete connection '+str((x,y))+'; it does not exist.\n')
                            elif w>0:
                                self.cons[(x,y)] = w
                            else:
                                print('\nInvalid cost ',w,'\n')
                        except:
                            print('\nCost should be positive integer or float.\n')
                        
    def display(self):
        objects = ['rt'+str(n) for n in self.rt] + ['nt'+str(n) for n in self.nt]
        if len(objects):
            m = max([len(ob) for ob in objects])+2
            lines = ['\n' + ''.ljust(m) + '|'+ '|'.join([ob.ljust(m) for ob in objects])+'|']
            fill = ''.ljust(len(lines[0])-1,'-')
            lines.append(fill)
            i = 0
            while i < len(objects):
                line = objects[i].ljust(m)+'|'
                j = 0
                while j < len(objects):
                    row = objects[i]
                    col = objects[j]
                    if (col,row) in self.cons:
                        line += str(self.cons[(col,row)]).ljust(m) + '|'
                    else:
                        line += ''.ljust(m) + '|'
                    j += 1
                lines.append(line)
                lines.append(fill)
                i += 1
            lines = [line[:-1] for line in lines[:-1]]
            lines[-1] = lines[-1]+'\n'
            for line in lines:
                print(line)
        else:
            print('\nNothing to display. Try adding some routers, networks and connections.\n')
    
    def tree(self,x):
        Q1 = ['rt'+str(n) for n in self.rt] + ['nt'+str(n) for n in self.nt]
        if x in Q1:
            Q2 = []
            adj = dict([(q,set()) for q in Q1])
            for con in self.cons:
                adj[con[0]].add(con[1])
            dist = dict()
            prev = dict()
            for v in Q1:
                dist[v] = float('inf')
            dist[x] = 0
            while len(Q1):
                Q1.sort(key = lambda q : dist[q])
                u = Q1[0]
                Q1.remove(u)
                Q2.append(u)
                for v in adj[u]:
                    alt = dist[u] + self.cons[(u,v)]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
            Q2.remove(x)
            Q2.sort(key = lambda q : dist[q])
            m = max([len(str(dist[q])) for q in Q2]) + 2
            lines = ['\nTree for '+str(x)+':']
            for v in Q2:
                if v in prev:
                    line = v
                    a = v
                    while a in prev:
                        a = prev[a]
                        line = a + ', ' + line
                    line = str(dist[v]).ljust(m) + ': ' + line 
                    lines.append(line)
                else:
                    lines.append(''.ljust(m)+': no path to '+v)
            lines[-1] = lines[-1] + '\n'
            for line in lines:
                print(line)
                
        else:
            print('Invalid arguement "',x,'" for "tree".')
        
    def parse(self,args):
        i = 0
        while i+1 < len(args):
            if args[i][-1]==',':
               args[i] = args[i]+args[i+1]
               args.remove(args[i+1])
            else:
                i += 1
        i = 0
        if args[0] in self.like['add']:
            if len(args)==3:
                if args[1] in self.like['rt']:
                    self.add_rt(args[2])
                elif args[1] in self.like['nt']:
                    self.add_nt(args[2])
                else:
                    print('\nInvalid arguement "'+str(args[1])+'" for "add".\n')
            else:
                print('\n"add" takes 2 additional arguements.',len(args)-1,'given.\n' )

        elif args[0] in self.like['del']:
            if len(args)==3:
                if args[1] in self.like['rt']:
                    self.del_rt(args[2])
                elif args[1] in self.like['nt']:
                    self.del_nt(args[2])
                else:
                    print('\nInvalid arguement "'+str(args[1]),'" for "del".\n')
            else:
                print('\n"del" take 2 additional arguements.',len(args)-1,'given.\n')
        
        elif args[0] in self.like['con']:
            if len(args)==4:
                self.con(args[1],args[2],args[3])
            else:
                print('\n"con" takes 3 additional arguements.',len(args)-1,'given.\n')
        
        elif args[0] in self.like['display']:
            self.display()
        elif args[0] in self.like['tree']:
            if len(args) == 2:
                self.tree(args[1])
            else:
                print('\nExpected 1 additional arguement for "tree".',len(args)-1,'given.\n')
        elif args[0] in self.like['save']:
            if len(args) == 1:
                self.save()
            elif len(args) == 2:
                self.save(args[1])
            else:
                print('\nExpected at most 1 additional arguement for "save".',len(args)-1,'given.\n')
        elif args[0] in self.like['load']:
            if len(args) == 2:
                self.load(args[1])
            else:
                print('\nExpected a saved name to "load".',
                      'Try "load <name>",\n or "save list" to see a list of saves\' names.')
        else:
            print('\nInvalid arguement "'+str(args[0])+'"')
    
    def save(self,name=None):
        if name == None:
            name = self.cur_save
        if name == None:
            print('\nThis one hasn\'t been saved before, so it requires a name.',
                  '\nTry "save <name>"')
        elif name in self.like['list']:
            L = os.listdir('saves/')
            L = [l for l in L if len(l)>5]
            L = [l[:-5] for l in L if l[-5:]=='.save']
            print('Current saves:')
            for l in L:
                print('   ',l)
            print(' ')
        elif name == self.cur_save:
            path = 'saves/'+str(name)+'.save'
            while True:
                inp = input('\nOverwrite save "'+name+'"?'+'\n... ')
                if inp in self.like['yes']:
                    file = open(path,'w')
                    file.write(str(self.rt))
                    file.write('\n')
                    file.write(str(self.nt))
                    file.write('\n')
                    file.write(str(self.cons))
                    file.close()
                    self.cur_save = name
                    break
                elif inp in self.like['no']:
                    break
                else:
                    print('\nType y for "yes" or n for "no".')
        elif self.cur_save != None:
            path = 'saves/'+name+'.save'
            go = False
            while True:
                print('\nYou already have an earlier save,','"'+self.cur_save+'"','for this one.')
                inp = input('Are you sure you want write under a new name?\n... ')
                if inp in self.like['yes']:
                    go = True
                    break
                elif inp in self.like['no']:
                    break
                else:
                    print('\nType y for "yes" or n for "no".')
            if go:
                if os.path.isfile(path):
                    while True:
                        print('\nThere is another save already using your new name.')
                        inp = input('\nDo you want to overwrite it?\n... ')
                        if inp in self.like['yes']:
                            file = open(path,'w')
                            file.write(str(self.rt))
                            file.write('\n')
                            file.write(str(self.nt))
                            file.write('\n')
                            file.write(str(self.cons))
                            file.close()
                            self.cur_save = name
                            break
                        elif inp in self.like['no']:
                            break
                        else:
                            print('\nType y for "yes" or n for "no".')
                else:
                    file = open(path,'w')
                    file.write(str(self.rt))
                    file.write('\n') 
                    file.write(str(self.nt))
                    file.write('\n')
                    file.write(str(self.cons))
                    file.close()
                    self.cur_save = name
        else:
            path = 'saves/'+name+'.save'
            file = open(path,'w')
            file.write(str(self.rt))
            file.write('\n')
            file.write(str(self.nt))            
            file.write('\n')
            file.write(str(self.cons))
            file.close()
            self.cur_save = name

    def load(self,name):
        path = 'saves/'+name+'.save'
        if os.path.isfile(path):
            file = open(path,'r')
            lines = file.read().split('\n')
            file.close()
            self.rt = eval(lines[0])
            self.nt = eval(lines[1])
            self.cons = eval(lines[2])
            self.cur_save = name
        else:
            print('\nSave "'+name+'" does not exist.')
        
if __name__ == '__main__':
    D = route()
    while True:
        inp = input('\nInput a command or type "quit" to quit.\n... ')
        args = [arg.replace(' ','') for arg in inp.split(' ') if arg]
        if args[0] in D.like['quit']:
            break
        D.parse(args)