debug = False
debug = True


# Implements intcode as a python class up to day 5

class Intcode:

    def interpret_parameters(self, n_params, modes):
        inparams = []
        for k in range(n_params): # slice does not work if the code is a dict
            inparams.append(self.lookup(self.pos+1+k))
        pos = [None]*n_params
        for k in range(n_params):
            mode = modes%10
            modes = modes//10
            if mode == 0:
                pos[k] = inparams[k]
            elif mode == 1:
                pos[k] = self.pos+1+k
            elif mode == 2:
                pos[k] = inparams[k] + self.relative_base
            else:
                pass
        return pos

    def lookup(self,pos):
        try:
            return self.code[pos]
        except IndexError:
            return 0
        except KeyError:
            return 0

    def store(self,pos,val):
        try:
            self.code[pos]=val
        except IndexError:
            # raise IndexError('Trying to store code outside list. Try init code as dict.')
            print('Changing stored code from list to dict')
            self.make_code_dict()

    def make_code_dict(self):
        dict_code = { i : self.code[i] for i in range(len(self.code) ) }
        self.code = dict_code

# operations for the different opcodes

    # 1
    def add(self, mode=0):
        par_pos = self.interpret_parameters(3,mode)
        self.store(par_pos[2], \
            self.lookup(par_pos[0]) + self.lookup(par_pos[1])
            )
        self.pos += 4
        return True

    # 2
    def mult(self, mode=0):
        par_pos = self.interpret_parameters(3,mode)
        self.store(par_pos[2], \
            self.lookup(par_pos[0]) * self.lookup(par_pos[1])
            )
        self.pos += 4
        return True
    
    # 3
    def input(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        self.store(par_pos[0], int(input('>')))
        self.pos += 2
        return True

    # 4
    def output(self, mode=0):
        par_pos = self.interpret_parameters(1,mode)
        print(self.lookup(par_pos[0]))
        self.pos += 2
        return True

    # 5
    def jump_if_true(self,mode):
        par_pos = self.interpret_parameters(2,mode)
        if self.lookup(par_pos[0]):
            self.pos=self.lookup(par_pos[1])
        else:
            self.pos += 3
        return True

    # 6
    def jump_if_false(self,mode):
        par_pos = self.interpret_parameters(2,mode)
        if not self.lookup(par_pos[0]):
            self.pos=self.lookup(par_pos[1])
        else:
            self.pos += 3
        return True

    # 7
    def less_than(self,mode):
        par_pos = self.interpret_parameters(3,mode)
        if self.lookup(par_pos[0]) < self.lookup(par_pos[1]):
            self.store(par_pos[2], 1)
        else:
            self.store(par_pos[2], 0)
        self.pos += 4
        return True

    # 8
    def equals(self,mode):
        par_pos = self.interpret_parameters(3,mode)
        if self.lookup(par_pos[0]) == self.lookup(par_pos[1]):
            self.store(par_pos[2], 1)
        else:
            self.store(par_pos[2], 0)
        self.pos += 4
        return True

    # 9
    def relative_base_offset(self,mode):
        np = 1
        par_pos = self.interpret_parameters(np,mode)
        self.relative_base += self.lookup(par_pos[0])
        self.pos += (np + 1)
        return True

    # 99
    def terminate(self, mode=0):
        self.terminated = True
        return True

    def __init__(self, code = [], pos = 0):
        self.code = code
        self.pos = pos
        self.terminated = False
        self.relative_base = 0
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
            9: self.relative_base_offset,
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
            opcode = self.lookup(self.pos)
            if debug: print('pos:', self.pos, ' opcode:', opcode, ' rel_base:', self.relative_base)
            op = self.op_dict[opcode%100]
            mode = opcode//100
            op(mode)

