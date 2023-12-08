from collections import defaultdict

def day4v2(input):
  f = open(input)
  lines = f.read().splitlines()
  f.close()
  ans = 0
  G = defaultdict(int)
  for i,line in enumerate(lines):
    G[i]+=1 #conto le carte originali
    first_part, second_part = line.split("|")
    id_game, cards = first_part.split(": ")
    win_numbers = [int(c) for c in cards.split()]
    my_numbers = [int(c) for c in second_part.split()]
    val = len(set(win_numbers) & set(my_numbers)) #intersezione tra i due set
    if val>0:
      ans+=2**(val-1)
    for j in range(val):
      G[i+1+j]+=G[i] #qui aggiungo le copie
  print(sum(G.values()))
  return ans

print(day4v2("input.txt"))