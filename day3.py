lines = open('day3.txt','r').readlines()

#lines = ['R8,U5,L5,D3', 'U7,R6,D4,L4']

def get_locs(directions):
  px = 0
  py = 0
  for d in directions:
    direction = d[0]
    amount = int(d[1:])
    x,y = { 'U': (0,-1), 'D':(0,1), 'R':(1,0), 'L':(-1,0) }[direction]
    yield from ((px + d*x, py + d*y) for d in range(amount))
    px += x*amount
    py += y*amount
      

f = dict()
for i, loc in enumerate(get_locs(lines[0].split(','))):
  if not loc in f:
    f[loc] = i
  
s = dict()
for i, loc in enumerate(get_locs(lines[1].split(','))):
  if not loc in s:
    s[loc] = i

intersections = (f.keys() & s.keys()) - {(0,0)}
print(intersections)
first = min(intersections, key=lambda i: f[i] + s[i])
closest = min(intersections, key=lambda i: abs(i[0]) + abs(i[1]))

print("first", first, f[first] + s[first])
print("closest", closest, abs(closest[0]) + abs(closest[1]))
"""
intersections = f & s - frozenset([(0,0)])
closest = min([abs(x)+abs(y) for x,y in intersections])
closestintersection = [ (x,y) for x,y in intersections if abs(x)+abs(y) == closest ][0]
print(closest)
print(closestintersection)
"""






