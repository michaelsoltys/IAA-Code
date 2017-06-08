# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 2.33 - Routing
## Ryan McIntyre
## 6/7/2017
## python 3.5.2


class route:
    
    def __init__(self):
        self.rt = set()
        self.nt = set()
        self.cons = dict()
        
        self.like = dict()
        self.like['add'] = set(['add','Add','ADD','+'])
        self.like['rt'] = set(['rt','Rt','RT','router','Router','ROUTER',])
        self.like['nt'] = set(['nt','Nt','NT','network','Network','NETWORK',])
        self.like['del'] = set(['del','Del','DEL','delete','Delete','DELETE','-'])
        self.like['con'] = set(['con','Con','CON','connect','Connect','CONNECT','c'])
        self.like['display'] = set(['display','Display','DISPLAY'])
        self.like['quit'] = set(['quit','Quit','QUIT','exit','Exit','EXIT','q'])
        
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
            if tx not in ['rt','nt']:
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
        
    def parse(self,args):
        i = 0
        while i+1 < len(args):
            if args[i][-1]==',':
               args[i] = args[i]+args[i+1]
               args.remove(args[i+1])
            else:
                i += 1
        i = 0
        while i < len(args):
            for word in self.like['rt']:
                if word in args[i]:
                    args[i] = args[i].replace(word,'rt')
            for word in self.like['nt']:
                if word in args[i]:
                    args[i] = args[i].replace(word,'nt')
            i += 1
        
        if args[0] in self.like['add']:
            if len(args)==3:
                if args[1] in self.like['rt']:
                    self.add_rt(args[2])
                elif args[1] in self.like['nt']:
                    self.add_nt(args[2])
                else:
                    print('\nInvalid arguement',args[1],'for "add".\n')
            else:
                print('\n"add" takes 2 additional arguements.',len(args)-1,'given.\n' )

        elif args[0] in self.like['del']:
            if len(args)==3:
                if args[1] in self.like['rt']:
                    self.del_rt(args[2])
                elif args[1] in self.like['nt']:
                    self.del_nt(args[2])
                else:
                    print('\nInvalid arguement',args[1],'for "del".\n')
            else:
                print('\n"del" take 2 additional arguements.',len(args)-1,'given.\n')
        
        elif args[0] in self.like['con']:
            if len(args)==4:
                self.con(args[1],args[2],args[3])
            else:
                print('\n"con" takes 3 additional arguements.',len(args)-1,'given.\n')
        
        elif args[0] in self.like['display']:
            self.display()
        else:
            print('Invalid arguement',args[0])
            

if __name__ == '__main__':
    D = route()
    while True:
        inp = input('Input a command or type "quit" to quit.\n... ')
        args = [arg.replace(' ','') for arg in inp.split(' ')]
        if args[0] in D.like['quit']:
            break
        D.parse(args)