# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 2.35 Sample Solution
## Joel Helling
## 3/9/2015
## python 3.4

## The current algorithm reduces a text files by ~45%, while windows zip utility
## can reduce the same file ~65%

import sys
import array
class Node(object):
    def __init__(self,letters,freq,leftChild,rightChild):
        self.letters = letters
        self.freq = freq
        self.leftChild = leftChild
        self.rightChild = rightChild

    # combine node strings and add frequencies into a new node with
    # children: left, node1; right, node2
    def merge_nodes(node1,node2):
        totalFreq = node1.get_freq() + node2.get_freq()
        catLetters = node1.get_letters() + node2.get_letters()
        return Node(catLetters,totalFreq,node1,node2)

    def get_freq(self):
        return self.freq

    def get_rightChild(self):
        return self.rightChild

    def get_leftChild(self):
        return self.leftChild

    def get_letters(self):
        return self.letters

    def print(self):
        print("{0} : {1}".format(repr(self.letters),self.freq))

class NodeList(object):
    def __init__(self):
        self.list = []

    # use insertion sort on the frequencies of the added nodes. 
    # if frequencies are equal, order by string value
    # the list is sorted in descending order
    def add(self,newNode):
        for index in range(len(self.list)):
            if newNode.get_freq() > self.list[index].get_freq():
                self.list.insert(index,newNode)
                break
            elif newNode.get_freq() == self.list[index].get_freq() \
                and newNode.get_letters() > self.list[index].get_letters():
                self.list.insert(index,newNode)
                break
        else:
            self.list.append(newNode)

    # remove two smallest nodes in the list.
    def pop2(self):
        return self.list.pop(),self.list.pop()

    def pop(self):
        return self.list.pop()

    def len(self):
        return len(self.list)

    def print(self):
        for node in self.list:
            node.print()

class HuffmanTree(object):
    def __init__(self):
        self.freqs = {}
        self.codes = {}
        self.tree = None
        self.bits = 0


    def encode_file(self,inputFileName,outputFileName):
        with open(inputFileName,"r") as input, open(outputFileName,"wb") as output:
            # get letter frequencies
            self._set_freqs(input)
            # build tree from list
            self._build_tree()
            # get char codes from tree
            self._set_code()
            # reread file to encode
            input.seek(0)
            self._add_header(output)
            self._encode_text(input,output)
            # output to output file

    def decode_file(self,inputFileName,outputFileName):
        with open(inputFileName,"rb") as input, open(outputFileName,"w") as output:
            # read header section of file for frequencies
            self._read_header(input)
            # build tree from list
            self._build_tree()
            self._decode_text(input,output)

    # go through each bit of the input bin file, and move through the tree,
    # 0 for left, and 1 for right.
    def _decode_text(self,input,output):
        bin_file = input.read()
        bits_read = 0
        mask = 0b10000000
        write_buffer = ""
        curr_node = self.tree
        for byte in bin_file:
            while mask:
                if byte & mask == 0:
                    curr_node = curr_node.get_leftChild()
                elif byte & mask > 0:
                    curr_node = curr_node.get_rightChild()
                bits_read += 1
                mask = mask >> 1
                if len(curr_node.get_letters()) == 1:
                    write_buffer += curr_node.get_letters()
                    curr_node = self.tree
                if bits_read > self.bits:
                    output.write(write_buffer)
                    mask = 0
            mask = 0b10000000

    # parse the header into a frequency dictionary
    def _read_header(self,input):
        header = ''
        byte = input.read(1)
        while byte.decode("ascii") != '\x00':
            header += byte.decode("ascii")
            byte = input.read(1)

        headerfreqs, bits = header.split(';')
        self.bits = int(bits)
        freqs = headerfreqs.split(':')
        for freq in freqs:
            # used instead of split to accomodate for a , being in the 
            # header as a node in the frequency list.
            c = freq[0]
            num = freq[2:]
            self.freqs[c] = int(num)

    # preppend the frequencies calculated by the input file,
    # followed by the number of bits to be read,
    # ended with a null character.
    def _add_header(self,output):
        heading = ''
        for key in self.freqs:
            heading += "{},{}:".format(key,self.freqs[key])
        heading = heading[:len(heading)-1] + ';'
        bheading = bytearray(heading,"ascii")
        output.write(bheading)

    # create a binary array based on the characters in the input to their 
    # huffman code and adds the bits to the array.
    def _encode_text(self,input,output):
        bytelen = 8
        bin_code_array = array.array('B')
        numbits = 0
        buffer = 0
        buffilled = 0
        for line in input:
            for c in range(len(line)):
                code = self.codes[line[c]]
                numbits += len(code)
                for bit in list(code):
                    if bit == '1':
                        buffer = (buffer << 1) | 0x01
                    elif bit == '0':
                        buffer = (buffer << 1)
                    buffilled += 1
                    if buffilled == bytelen:
                        bin_code_array.extend([buffer])
                        buffer = 0
                        buffilled = 0

        if buffilled != 0:
            bin_code_array.extend([buffer << (bytelen - buffilled)])

        barray = bytearray(str(numbits),"ascii")
        barray.append(0)
        output.write(barray)
        bin_code_array.tofile(output)

    # counts the frequency of the letters in the file
    # and stores the result in a dictionary
    def _set_freqs(self,input):
        self.freqs = {}
        numChars = 0
        for line in input:
            for c in range(len(line)):
                if line[c] in self.freqs:
                    self.freqs[line[c]] += 1
                else:
                    self.freqs[line[c]] = 1
                numChars += 1
        for key in self.freqs:
            self.freqs[key] = int((self.freqs[key]/numChars) * 100)

    # converts a list of nodes with frequencies to a huffman tree.
    def _build_tree(self):
        hufflist = NodeList()
        for key in self.freqs:
            hufflist.add(Node(key,self.freqs[key],None,None))
        for i in range(hufflist.len()-1):
            node1,node2 = hufflist.pop2()
            mergedNode = Node.merge_nodes(node1,node2)
            hufflist.add(mergedNode)
        self.tree = hufflist.pop()

    # traverses the tree to find the leaf for char. 
    # returns a string representation of the huffman code.
    def _get_char_code(self,char):
        currNode = self.tree
        code = ""
        while currNode:
            if currNode.get_letters() == char:
                return code
            elif char in currNode.get_leftChild().get_letters():
                code += "0"
                currNode = currNode.get_leftChild()
            else:
                code += "1"
                currNode = currNode.get_rightChild()

    # sets the code of a character based on its frequency
    def _set_code(self):
        self.codes = {}
        for key in self.freqs:
            self.codes[key] = self._get_char_code(key)

def main():
    freqs = {}
    if len(sys.argv) > 3:
        encoder = HuffmanTree()
        if sys.argv[1] == "-e":
            encoder.encode_file(sys.argv[2],sys.argv[3])
        elif sys.argv[1] == "-d":
            encoder.decode_file(sys.argv[2],sys.argv[3])
        else:
            print("Unrecognized flag: -e<encode>/-d<decode>") 
    else:
        print("Usage: python Huffman.py <flag> <inputFile> <outputFile>")

main();
