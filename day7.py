import itertools
i = open('day7.txt', 'r').read()

reset = [ int(v) for v in i.split(',')]

#reset = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#reset = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
#         101,5,23,23,1,24,23,23,4,23,99,0,0]
#reset = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#         1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#reset = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
#         27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#reset = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
#         -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
#         53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def run(reset, name):
  name = name if name else "Santa"
  program = reset.copy()
  pc = 0

  def oper(num):
    strop = str(program[pc])
    pmode = [int(c) for c in strop[-3::-1]]
    mode = pmode[num-1] if num-1 < len(pmode) else 0
    literal = program[pc+num] if pc+num < len(program) else 0
    if mode == 0: # position mode
      return program[literal] if literal < len(program) else 0
    elif mode == 1: # immediate mode
      return literal
    else:
      raise RuntimeError("Unknown parameter mode", mode, name)

  while pc >= 0 and pc < len(program):
    strop = str(program[pc])
    op = int(strop[-2:])


    ins = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 99:0}    

    newpc = pc + ins[op]

    p1 = oper(1)
    p2 = oper(2)
    p3 = oper(3)
    dest1 = program[pc+1] if pc+1 < len(program) else 0
    dest2 = program[pc+2] if pc+2 < len(program) else 0
    dest3 = program[pc+3] if pc+3 < len(program) else 0

    if op == 1: # add
      value = p1 + p2
      program[dest3] = value
    elif op == 2: # multiply
      value = p1 * p2
      program[dest3] = value
    elif op == 3: # input
      program[dest1] = (yield)
      if program[dest1] is None:
        raise ValueError("Received bad input", program[dest1], name)
    elif op == 4: # output
      yield p1
    elif op == 5: # jump-if-true
      if p1 != 0:
        newpc = p2 
    elif op == 6: # jump-if-false
      if p1 == 0:
        newpc = p2 
    elif op == 7: # less than
      program[dest3] = 1 if p1 < p2 else 0
    elif op == 8: # equals
      program[dest3] = 1 if p1 == p2 else 0
    elif op == 99: # HCF
      break
    else:
      raise RuntimeError("Unknown operation", op, name)
    pc = newpc

def try_perm(phase_settings):
  amplifiers = [run(reset, str(i)) for i in range(5)] 
  A,B,C,D,E = amplifiers

  # start program, give phase setting
  for p, v in zip(amplifiers, phase_settings):
    next(p)
    p.send(v)
  
  curent_value = 0
  while True:
    # give next value, get response
    curent_value = E.send(D.send(C.send(B.send(A.send(curent_value)))))

    try:
      # attempt to restart amp
      [next(a) for a in amplifiers]
    except StopIteration:
      # an amplifier has stopped, exit
      return curent_value

def solve(fn, start, end):
  for p in itertools.permutations(range(start, end)):
    yield (fn(p),p)

print(max(solve(try_perm, 0, 5)))
print(max(solve(try_perm, 5, 10)))
