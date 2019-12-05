i = open('day5.txt', 'r').read()

reset = [ int(v) for v in i.split(',')]

program = reset
program = [3,0,4,0,99]
program = [1002,4,3,4,33]
program = [1101,100,-1,4,0]
program = reset
program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
           1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
           999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
program = reset

def run(program, inptiter):
  inpt = iter(inptiter)
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
      raise RuntimeError("Unknown parameter mode", mode)

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
      program[dest1] = next(inpt)
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
      raise RuntimeError("Unknown operation", op)
    pc = newpc

def test_input():

  def generate_numbers():
    while True:
      yield int(input("input a number:"))
  print("")
  print("")
  print("")
  print("Start")
  out = run(program, generate_numbers())
  print("output", [x for x in out])


test_input()
