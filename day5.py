i = open('day5.txt', 'r').read()

reset = [ int(v) for v in i.split(',')]

program = reset
program = [3,0,4,0,99]
program = [1002,4,3,4,33]
program = [1101,100,-1,4,0]
program = reset
program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

def run(program, inptiter):
  inpt = iter(inptiter)
  pc = 0
  while pc >= 0 and pc < len(program):
    strop = str(program[pc])
    pmode = [int(c) for c in strop[-3::-1]]
    op = int(strop[-2:])

    def oper(num):
      mode = pmode[num-1] if num <= len(pmode) else 0
      literal = program[pc+num]
      if mode == 0: # position mode
        return program[literal]
      elif mode == 1: # immediate mode
        return literal
      else:
        raise RuntimeError("Unknown parameter mode", mode)
    
    #print("Executing op", strop, " = program[", pc, "]", "op", op, "pmodes", pmode)
    print("Executing op", strop, " = program[", pc, "]")

    if op == 1:
      value = oper(1) + oper(2)
      dest = program[pc+3]
      print("          add, program[", dest, "] =", value, "=", oper(1), "+", oper(2))
      program[dest] = value
      pc += 3
    elif op == 2:
      value = oper(1) * oper(2)
      dest = program[pc+3]
      print("          mul, program[", dest, "] =", value, "=", oper(1), "*", oper(2))
      program[dest] = value
      pc += 3
    elif op == 3:
      i = next(inpt)
      dest = program[pc+1]
      print("          input, program[", dest, "] =",i)
      program[dest] = i
      pc += 1 
    elif op == 4:
      value = oper(1)
      yield value
      print("          output" ,value)
      pc += 1 
    elif op == 5:
      p1 = oper(1)
      p2 = oper(2) -1
      newpc = p2 if p1 != 0 else pc+2
      print("          jump-if-true", "from", pc, "newpc", newpc, "<-", pc, "val", p1)
      pc = newpc
    elif op == 6:
      p1 = oper(1)
      p2 = oper(2) -1
      newpc = p2 if p1 == 0 else pc+2 
      print("          jump-if-false", "from", pc, "newpc", newpc, "<-", pc, "val", p1)
      pc = newpc
    elif op == 7:
      p1 = oper(1)
      p2 = oper(2)
      dest = program[pc+3]
      program[dest] = 1 if p1 < p2 else 0
      print("          less than", p1 < p2, "=", p1, "<", p2)
      pc+=3 
    elif op == 8:
      p1 = oper(1)
      p2 = oper(2)
      dest = program[pc+3]
      program[dest] = 1 if p1 == p2 else 0
      print("          equals", p1 == p2, "=", p1, "<", p2)
      pc+=3 
    elif op == 99:
      break
    else:
      raise RuntimeError("Unknown operation", op)
    pc+=1

out = run(program, [5])
print("output", [x for x in out])
