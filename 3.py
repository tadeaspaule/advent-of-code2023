def issymb(c):
  return c != "." and not c.isnumeric()

lines = []
with open("inputs/3","r") as f:
  for l in f:
    lines.append(l.strip())
w = len(lines[0])
h = len(lines)
ps = 0
symb = False
n = ""
for y in range(h):
  symb = False
  n = ""
  for x in range(w):
    if lines[y][x] == ".":
      if len(n) > 0:
        symb = symb or (y > 0 and issymb(lines[y-1][x]))
        symb = symb or (y+1 < h and issymb(lines[y+1][x]))
        if symb:
          ps += int(n)
      symb = False
      n = ""
    elif lines[y][x].isnumeric():
      n += lines[y][x]
      symb = symb or (y > 0 and issymb(lines[y-1][x]))
      symb = symb or (y+1 < h and issymb(lines[y+1][x]))
      if len(n) == 1 and x > 0:
        symb = symb or (y > 0 and issymb(lines[y-1][x-1]))
        symb = symb or (y+1 < h and issymb(lines[y+1][x-1]))
        symb = symb or (issymb(lines[y][x-1]))
    else:
      symb = True
      if len(n) > 0:
        ps += int(n)
      n = ""
  if len(n) > 0 and symb:
    ps += int(n)
print(ps)