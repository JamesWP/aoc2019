i = open('day5.txt', 'r').read()

reset = [0] + [ int(v) for v in i.split(',')]

program = reset
program = [3,0,4,0,99]
program = [1002,4,3,4,33]
program = [1101,100,-1,4,0]
program = reset

def run(program, inptiter):
  inpt = iter(inptiter)
  pc = 1
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
    
    #print("Executing op", op,  "pmodes", pmode)

    if(op == 1):
      value = oper(1) + oper(2)
      dest = program[pc+3]
      print("Executing add, program[", dest, "]=", value, "=", oper(1), "+", oper(2))
      program[dest] = value
      pc += 3
    elif(op == 2):
      value = oper(1) * oper(2)
      dest = program[pc+3]
      print("Executing mul, program[", dest, "]=", value, "=", oper(1), "*", oper(2))
      program[dest] = value
      pc += 3
    elif(op == 99):
      break
    elif(op == 3):
      i = next(inpt)
      dest = program[pc+1]
      print("Executing input, program[", dest, "]=",i)
      program[dest] = i
      pc += 1 
    elif(op == 4):
      src = program[pc+1]
      value = program[src]
      yield value
      print("Executing output, ",value,"=program[", src, "]")
      pc += 1 
    else:
      raise RuntimeError("Unknown operation", op)
    pc+=1

out = run(program, [1])
print("output", [x for x in out])
