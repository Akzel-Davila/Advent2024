import re
def get_file_data(file_name):
    f = open(file_name)
    data = ""
    for line in f:
        data+=(line.rstrip())
    return data


file_data = get_file_data("Day3Input.txt")
regex = "mul\\([1-9]+,[1-9]+\\)"
matches = re.findall(regex, file_data)
total = 0
for str in matches:
    open_num = str.index("(")
    close_num = str.index(")")
    comma_num = str.index(",")
    num1 = str[open_num+1 : comma_num]
    num2 = str[comma_num+1 : close_num]
    print(str + " " + num1 + " " + num2)
    sum = int(num1)*int(num2)
    total += sum
print(total)