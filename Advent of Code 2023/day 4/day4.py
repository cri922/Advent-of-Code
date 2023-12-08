import re

def day4(input):
  pattern = r": +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) \| +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*) +(\d*)"
  win_numbers = []
  my_numbers = []
  points_list = []
  with open(input) as f:
    lines = f.read().splitlines()
    for line in lines:
      temp_win = []
      temp_my = []
      result = re.search(pattern,line)
      for i in range(1,len(result.groups())+1):
        if i<11:
          temp_win.append(int(result[i]))
        else:
          temp_my.append(int(result[i]))
      win_numbers.append(temp_win)
      my_numbers.append(temp_my)
    for l in range(len(my_numbers)):
      points = 0
      for k in range(len(my_numbers[l])):
        if my_numbers[l][k] in win_numbers[l] and points==0:
          points+=1
        elif my_numbers[l][k] in win_numbers[l] and points>=1:
          points=points*2
      points_list.append(points)
    sum=0
    for point in points_list:
      sum+=point
    return sum

print(day4("input.txt"))