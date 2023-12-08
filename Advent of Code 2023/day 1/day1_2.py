import re

numbers = ("one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")

def day1_2(input):
  with open(input) as f:
    sum=0
    pattern = r"(\d|one|two|three|four|five|six|seven|eight|nine)(.*)(\d|one|two|three|four|five|six|seven|eight|nine)"
    for line in f:
      result = re.search(pattern,line)
      result_2 = re.search(r"\d|one|two|three|four|five|six|seven|eight|nine",line)
      first_digit = ''
      second_digit = ''
      if result != None:
        if result[1].isdigit():
          first_digit = result[1]
        else:
          first_digit = str(numbers.index(result[1])+1)
        if result[3].isdigit():
          second_digit = result[3]
        else:
          second_digit = str(numbers.index(result[3])+1)
        number = int(first_digit+second_digit)
        sum+=number
      elif result_2 != None:
        if(result_2[0].isdigit()):
          first_digit = result_2[0]
        else:
          first_digit = str(numbers.index(result_2[0])+1)
        second_digit = first_digit
        number = int(first_digit+second_digit)
        sum+=number
  return sum

print(day1_2("input.txt"))