class Intcode:
 
# operations for the different opcodes

    # 1
    def add(self, mode=0):
        if mode == 0:
            arg1pos = self.code[self.pos+1]
            arg2pos = self.code[self.pos+2]
            resultpos = self.code[self.pos+3]
        elif mode == 1:
            arg1pos = self.pos+1
            arg2pos = self.pos+2
            resultpos = self.pos+3
        elif mode ==2:
            pass
        self.code[resultpos] = \
            self.code[arg1pos] + self.code[arg2pos]
        self.pos += 4
        return True

    # 2
    def mult(self, mode=0):
        if mode == 0:
            arg1pos = self.code[self.pos+1]
            arg2pos = self.code[self.pos+2]
            resultpos = self.code[self.pos+3]
        elif mode == 1:
            arg1pos = self.pos+1
            arg2pos = self.pos+2
            resultpos = self.pos+3
        elif mode ==2:
            pass
        self.code[resultpos] = \
            self.code[arg1pos] * self.code[arg2pos]
        self.pos += 4
        return True

    # 3
    def input(self, mode=0):
        if mode == 0:
            resultpos = self.code[self.pos+1]
        elif mode == 1:
            resultpos = self.pos+1
        elif mode == 2:
            pass
        self.code[resultpos] = \
            int(input('>'))
        self.pos += 2
        return True

    # 3
    def output(self, mode=0):
        if mode == 0:
            argpos = self.code[self.pos+1]
        elif mode == 1:
            argpos = self.pos+1
        elif mode == 2:
            pass
        print(self.code[argpos])
        self.pos += 2
        return True


    # 99
    def terminate(self,mode=0):
        self.terminated = True
        return True


    def __init__(self, code = [], pos = 0):
        self.code = code
        self.pos = pos
        self.terminated = False
        # A dictionary of operations for opcodes
        self.op_dict = {
            1: self.add,
            2: self.mult,
            3: self.input,
            4: self.output,
            99: self.terminate,
        }

    def set_code(self, code, pos=0):
        self.code = code
        self.pos = pos

    def set_code_from_string(codestring):
        stripsplitline = line.strip().split(',')
        self.set_code(list(map(int,stripsplitline)))

    
    def run(self):
        self.terminated = False
        while not self.terminated:
            print(self.code)
            opcode = self.code[self.pos]
            print(opcode)
            op = self.op_dict[opcode%100]
            mode = opcode//100
            op(mode)
            



 


test_code2 = [1,9,10,3,2,3,11,0,99,30,40,50]
test2 = Intcode(test_code2, 0)
test2.run()
print(test2.code)

test5 = Intcode([3,0,4,0,99],0)
test5.run()
print(test5.code)

