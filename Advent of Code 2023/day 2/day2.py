import re

red = 12
green = 13
blue = 14
# 12 red cubes, 13 green cubes, and 14 blue cubes


def check_func(result):
    for i in result:
        if i[1] == "green" and int(i[0]) > green:
            return False
        elif i[1] == "red" and int(i[0]) > red:
            return False
        elif i[1] == "blue" and int(i[0]) > blue:
            return False
    return True


def day2(input):
    id = 1
    sum = 0
    pattern = r"(\d\d?) (red|green|blue)"
    with open(input) as f:
        for line in f:
            result = re.findall(pattern, line)
            if check_func(result):
                sum += id
                id += 1
            else:
                id += 1
        return sum


print(day2("input.txt"))
