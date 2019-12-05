
start = 137683
end = 596253

#start = 444
#end = 460

def runs(s):
  c = 1
  for a,b in zip(s, s[1:]):
    if a == b:
      c+=1
    if a != b:
      if c == 2:
        return True
      c = 1
  if c == 2:
    return True
  return False


counter = 0
for value in range(start+1, end):
  s=str(value)
  pairs = any(( a==b for a, b in zip(s, s[1:]) ))
  pairs = runs(s)
  decrease = all(( b>=a for a, b in zip(s, s[1:])))
  #print(value, pairs, decrease)
  if pairs and decrease:
    counter+=1

print(counter)
