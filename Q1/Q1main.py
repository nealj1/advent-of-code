import re

def file_line(Lines):
    count = 0
    # Strips the newline character
    for line in Lines:
        find_num(line.strip())

def find_num(line):
    pattern = r"[0-9]"
    num = re.search(pattern, line)
    back = re.search(pattern, line[::-1])
    num = (int num)
    print(num.group())
    print(back.group())


# Using readlines()
file = open('Q1/input.txt', 'r')
Lines = file.readlines()
file_line(Lines)

