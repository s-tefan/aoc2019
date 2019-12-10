debug = False


class Intcode:



    def interpret_parameters(self, n_params, modes):
        inparams = self.code[self.pos+1:self.pos+1+n_params]
        pos = [None]*n_params
        for k in range(n_params):
            mode = modes%10
            modes = modes//10
            if mode == 0:
                pos[k] = inparams[k]
            elif mode == 1:
                pos[k] = self.pos+1+k
            else:
                pass
        return pos

# operations for the different opcodes

    # 1
    def add(self, mode=0):
        par_pos = self.interpret_parameters(3,mode)
        self.code[par_pos[2]] = \
            self.code[par_pos[0]] + self.code[par_pos[1]]
        self.pos += 4
        return True

    # 2
    def mult(self, mode=0):
        par_pos = self.interpret_parameters(3,mode)
        self.code[par_pos[2]] = \
            self.code[par_pos[0]] * self.code[par_pos[1]]
        self.pos += 4
        return True
    
    # 3
    def input(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        self.code[par_pos[0]] = \
            int(input('>'))
        self.pos += 2
        return True

    # 4
    def output(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        print(self.code[par_pos[0]])
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

    def set_code_from_string(self,codestring):
        stripsplitline = codestring.strip().split(',')
        self.set_code(list(map(int,stripsplitline)))

    
    def run(self):
        self.terminated = False
        while not self.terminated:
            if debug: print(self.code)
            opcode = self.code[self.pos]
            if debug: print(opcode)
            op = self.op_dict[opcode%100]
            mode = opcode//100
            op(mode)
            



 
def test():
    test_code2 = [1,9,10,3,2,3,11,0,99,30,40,50]
    test2 = Intcode(test_code2, 0)
    test2.run()
    print(test2.code)

    test5 = Intcode([3,0,4,0,99],0)
    test5.run()
    print(test5.code)

    test5a = Intcode([1002,4,3,4,33])
    test5a.run()
    print(test5a.code)

    test5b = Intcode([1101,100,-1,4,0])
    test5b.run()
    print(test5b.code)


