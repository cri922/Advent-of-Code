def day3(input):
  with open(input) as f:
    lines = f.read().splitlines()
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])
    ans = 0
    for r in range(len(G)):
      n=0
      has_part = False
      for c in range(len(G[r])+1): #plus 1 to consider numbers at the end of line
        if c<C and G[r][c].isdigit():
          n = n*10+int(G[r][c])
          for rr in [-1,0,1]:
            for cc in [-1,0,1]:
              if 0<=r+rr<R and 0<=c+cc<C:
                ch = G[r+rr][c+cc]
                if not ch.isdigit() and ch != '.':
                  has_part = True
        elif n>0:
          if has_part:
            ans+=n
          n=0
          has_part = False
  return ans
      

print(day3("input.txt"))