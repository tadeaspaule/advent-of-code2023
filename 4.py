cards = []
with open("inputs/4","r") as f:
  for l in f:
    sl = l.strip()[(l.find(":")+1):].split("|")
    win, have = sl[0].split(" "), sl[1].split(" ")
    cards.append([set([int(n.strip()) for n in win if len(n.strip()) > 0]), [int(n.strip()) for n in have if len(n.strip()) > 0]])

ps = 0
nc = {}
for i in range(len(cards)):
  nc[i] = nc.get(i,0) + 1
  c = cards[i]
  n = 0
  for h in c[1]:
    if h in c[0]:
      n += 1
  for j in range(i+1,min(i+n+1,len(cards))):
    nc[j] = nc.get(j,0) + nc[i]

print(sum(nc.values()))
