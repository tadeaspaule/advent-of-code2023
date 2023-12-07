n = []
lines = []
symbs = []
gears = []
with open("inputs/3","r") as f:
  for l in f:
    lines.append(l.strip())
w = len(lines[0])
h = len(lines)
cn = ""
for y in range(len(lines)):
  n.append([0 for _ in range(len(lines[y]))])
  for x in range(len(lines[y])):
    c = lines[y][x]
    if c != "." and not c.isnumeric():
      symbs.append((x,y))
    if c == "*":
      gears.append((x,y))
    if c.isnumeric():
      cn += c
    elif len(cn) > 0:
      cnn = int(cn)
      for x2 in range(1,(len(cn)+1)):
        n[y][x - x2] = cnn
      cn = ""
  if len(cn) > 0:
    cnn = int(cn)
    for x2 in range(1,(len(cn)+1)):
      n[y][-x2] = cnn
    cn = ""

gs = 0
for (x,y) in gears:
  lsafe, rsafe = x > 0, x + 1 < w
  adj = []
  if lsafe:
    adj.append(n[y][x-1])
  if rsafe:
    adj.append(n[y][x+1])
  if y > 0:
    if n[y-1][x] > 0:
      adj.append(n[y-1][x])
    else:
      if lsafe:
        adj.append(n[y-1][x-1])
      if rsafe:
        adj.append(n[y-1][x+1])
  if y + 1 < h:
    if n[y+1][x] > 0:
      adj.append(n[y+1][x])
    else:
      if lsafe:
        adj.append(n[y+1][x-1])
      if rsafe:
        adj.append(n[y+1][x+1])
  adj = [e for e in adj if e > 0]
  if len(adj) == 2:
    gs += adj[0] * adj[1]

print(gs)
