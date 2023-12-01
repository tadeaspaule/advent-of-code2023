s = 0
digits = ["one","two","three","four","five","six","seven","eight","nine"]

with open("inputs/1","r") as f:
  for line in f:
    og = line.strip()
    edited_line = True
    while edited_line:
      edited_line = False
      while True:
        mini = 10000
        mind = -1
        for i in range(len(digits)):
          lf = line.find(digits[i])
          if lf != -1:
            mini = min(mini, lf)
            if mini == lf:
              mind = i
        if mind == -1:
          break
        edited_line = True
        line = line.replace(digits[mind],str(mind+1)+digits[mind][1:])
    nums = [int(c) for c in line if c.isnumeric()]
    print(f"'{og.strip()}' = {nums}")
    s += nums[0] * 10 + nums[-1]
print(s)
