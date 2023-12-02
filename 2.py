l = []
with open("inputs/2","r") as f:
  l = f.readlines()
idsum = 0
powersum = 0
limit = {"red": 12, "green": 13, "blue": 14}
for i in range(len(l)):
  d = {"red": 0, "green": 0, "blue": 0}
  s = l[i].strip().replace(","," ,").replace(";", " ;").split(" ")
  for j in range(len(s)):
    if s[j] in ["blue","green","red"]:
      d[s[j]] = max(d[s[j]], int(s[j-1]))
  valid = True
  for k,v in limit.items():
    if d[k] > v:
      valid = False
      break
  if valid:
    idsum += i + 1
  ps = 1
  for v in d.values():
    if v > 0:
      ps *= v
  powersum += ps
print(idsum)
print(powersum)


