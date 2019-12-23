# Advent of Code 2019 day 22

# card shuffling as arithmetics in Z_p


def inv(x,n):
# Multiplicative inverse, used in version 1
# where we generate the deck
    qlist = []
    rlist = [n,x]
    r=1
    while r != 0:
        q = rlist[-2]//rlist[-1]
        r = rlist[-2]%rlist[-1]
        qlist.append(q)
        rlist.append(r)
    qlist.pop()
    b = -qlist.pop()
    a = 1
    while qlist:
        q = qlist.pop()
        a0,b0 = a,b
        a = b0
        b = (a0 - q*b0) % n
    return b



def read(instr):
    # take indata as a string and make into a list
    # of (operation, parameter)
    lines = instr.split('\n')
    commlist=[]
    for line in lines:
        linecomm = ""
        for comm in comms:
            if line[:len(comm)] == comm:
                linecomm = comm
                par = line[len(comm):]
        try: intpar = int(par)
        except: intpar = None
        commlist.append((linecomm,intpar))
    return commlist


comms = ["deal with increment", "deal into new stack","cut"]

g_fcndict = { \
    "deal with increment": (lambda x,k,n: (x*k)%n),
    "deal into new stack": (lambda x,k,n: (-x-1)%n),
    "cut": (lambda x,k,n: (x+k)%n )
    }

g_invfcndict = {
    "deal with increment": (lambda x,k,n: (x*inv(k,n))%n),
    "deal into new stack": (lambda x,k,n: (-x-1)%n),
    "cut": (lambda x,k,n: (x-k)%n )
    }


''' Obsolete
def test0():
    s = sys.stdin.read()
    n = 10
    commlist = read(s)

    cardlist = list(range(n))
    for comm in reversed(commlist):
        if comm[0] in comms:
            fcn = g_invfcndict[comm[0]]
            new_cardlist = [fcn(x,comm[1],n) for x in cardlist]
            cardlist = new_cardlist
            #print(comm,':',cardlist)
    print(cardlist)

    
    for k0 in range(9):
        k = k0
        for comm in commlist:
            if comm[0] in comms:
                fcn = g_fcndict[comm[0]]
                k = fcn(k,comm[1],n)
        print('Card', k0,'is in position', k)
'''

def doit(commlist,n,kort):
    # does it        
        # Version 1
        # generate the shuffled deck
        # then look up card
        cardlist = list(range(n))
        for comm in reversed(commlist):
            if comm[0] in comms:
                fcn = g_invfcndict[comm[0]]
                new_cardlist = [fcn(x,comm[1],n) for x in cardlist]
                cardlist = new_cardlist
                #print(comm,':',cardlist)
        print(cardlist)
        print(cardlist.index(kort))

        # Version 2
        # does not generate the deck
        # tracks the positions through shuffling
        k = kort
        for comm in commlist:
            if comm[0] in comms:
                fcn = g_fcndict[comm[0]]
                k = fcn(k,comm[1],n)
                print(comm[0],comm[1],'Card',kort,'in position',k)

def part1():
    with open("input22.txt", "r") as f:
        s = f.read()
        commlist = read(s)
        doit(read(s),10007,2019)

def test1():
    with open("test22.txt", "r") as f:
        s = f.read()
        commlist = read(s)
        for kort in range(10):
            doit(commlist,10,kort)

import sys


#test1()
part1()