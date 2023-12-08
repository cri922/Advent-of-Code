import re

def day1(input):
  with open(input) as f:
    count=0
    for line in f:
      result_1=re.search(r"(\d)(.*)(\d)",line)
      result_2 = re.search(r"(\d)",line)
      if result_1 != None:
        number =int(result_1[1]+result_1[3])
        count+=number
      elif result_2 != None:
        number = int(result_2[1]+result_2[1])
        count+=number
  return count

print(day1("input.txt"))


