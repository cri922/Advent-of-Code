import re 

def power_func(result):
  red_temp = 0
  blue_temp = 0
  green_temp = 0
  for i in result:
    if i[1]=="green" and int(i[0])>green_temp:
      green_temp = int(i[0])
    if i[1]=="red" and int(i[0])>red_temp:
      red_temp = int(i[0])
    if i[1]=="blue" and int(i[0])>blue_temp:
      blue_temp = int(i[0])
  return green_temp * red_temp * blue_temp
    

def day2_2(input):
  with open(input) as f:
    sum = 0
    pattern = r"(\d\d?) (red|green|blue)"
    for line in f:
      result = re.findall(pattern, line)
      sum += power_func(result)
    return sum


print(day2_2("input.txt"))