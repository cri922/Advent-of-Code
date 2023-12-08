from collections import defaultdict

def day3_2(input):
  with open(input) as f:
    lines = f.read().splitlines()
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])
    prodsum = 0
    nums = defaultdict(list)
    for r in range(len(G)):
      gears = set() # put here coordinates of '*'
      n=0
      for c in range(len(G[r])+1):
        if c<C and G[r][c].isdigit():
          n = n*10+int(G[r][c])
          for rr in [-1,0,1]:
            for cc in [-1,0,1]:
              if 0<=r+rr<R and 0<=c+cc<C:
                ch = G[r+rr][c+cc]
                if ch == '*':
                  gears.add((r+rr,c+cc))
        elif n>0:
          for gear in gears:
            nums[gear].append(n)
          n=0
          gears = set()
    for k,v in nums.items():
      if len(v) == 2:
        prodsum += v[0]*v[1]
  return prodsum

print(day3_2("input.txt"))