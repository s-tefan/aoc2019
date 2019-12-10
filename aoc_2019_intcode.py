class Intcode:
 
# operations for the different opcodes

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

    def terminate(self,mode=0):
        self.terminated = True
        return True




    def __init__(self, code = [], pos = 0):
        self.code = code
        self.pos = pos
        self.terminated = False
        self.op_dir = {
            1: self.add,
            2: self.mult,
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
            op = self.op_dir[opcode%100]
            mode = opcode//100
            op(mode)
            



 


test_code = [1,9,10,3,2,3,11,0,99,30,40,50]
test = Intcode(test_code, 0)
test.run()
print(test.code)
