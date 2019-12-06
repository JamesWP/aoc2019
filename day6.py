from collections import defaultdict

lines = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""".split('\n')

lines = open('day6.txt','r').readlines()

orbits = (line.strip().split(')') for line in lines if ')' in line)

direct_orbits = defaultdict(set)
direct_orbits_reverse = dict()

for centre, planet in orbits:
  direct_orbits[centre].add(planet)
  direct_orbits_reverse[planet] = centre

def count_orbits(centre, level):
  child_orbits = direct_orbits[centre]
  return len(child_orbits)*level + sum(( count_orbits(orbiter,level+1) for orbiter in child_orbits))

def path(dest):
  yield dest
  while dest != 'COM':
    dest = direct_orbits_reverse[dest]
    yield dest
  

print(len(direct_orbits))
print(direct_orbits['COM'])
print(count_orbits('COM', 1))  

print()
non_shared = { p for p in path('SAN')} ^ {p for p in path('YOU')}
print(non_shared)
print(len(non_shared)-2)
