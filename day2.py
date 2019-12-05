i = open('day2.txt', 'r').read()

reset = [ int(v) for v in i.split(',')]

# program = [1,9,10,3, 2,3,11,0, 99, 30,40,50 ]

output = 19690720

def noun_verb(program, noun, verb):
  program[1] = noun
  program[2] = verb
  run(program)
  return program[0]
  

def run(program):

  pc = 0
  while pc >= 0 and pc < len(program):
    op = program[pc]
    if(op == 1):
      in1 = program[pc+1]
      in2 = program[pc+2]
      out = program[pc+3]
      program[out] = program[in1] + program[in2]
      #print("op", op, "in1", in1, "in2", in2, "out", out)
      pc += 4
    elif(op == 2):
      in1 = program[pc+1]
      in2 = program[pc+2]
      out = program[pc+3]
      program[out] = program[in1] * program[in2]
      #print("op", op, "in1", in1, "in2", in2, "out", out)
      pc += 4
    elif(op == 99):
      break
    else:
      raise RuntimeError


for verb in range(0, 100):
  for noun in range(0, 100):
    program = [ i for i in reset ]
    result = noun_verb(program, noun, verb)
    if result == output:
      print(noun * 100 + verb)

      break;
    
