debug = False
#debug = True


# Implements intcode as a python class up to day 5

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

    # 5
    def jump_if_true(self,mode):
        par_pos = self.interpret_parameters(2,mode)
        if self.code[par_pos[0]]:
            self.pos=self.code[par_pos[1]]
        else:
            self.pos += 3
        return True

    # 6
    def jump_if_false(self,mode):
        par_pos = self.interpret_parameters(2,mode)
        if not self.code[par_pos[0]]:
            self.pos=self.code[par_pos[1]]
        else:
            self.pos += 3
        return True

    # 7
    def less_than(self,mode):
        par_pos = self.interpret_parameters(3,mode)
        if self.code[par_pos[0]] < self.code[par_pos[1]]:
            self.code[par_pos[2]] = 1
        else:
            self.code[par_pos[2]] = 0
        self.pos += 4
        return True

    # 7
    def equals(self,mode):
        par_pos = self.interpret_parameters(3,mode)
        if self.code[par_pos[0]] == self.code[par_pos[1]]:
            self.code[par_pos[2]] = 1
        else:
            self.code[par_pos[2]] = 0
        self.pos += 4
        return True

    # 99
    def terminate(self, mode=0):
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
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
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
