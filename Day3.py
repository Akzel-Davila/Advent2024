import re
def get_file_data(file_name):
    f = open(file_name)
    data = ""
    for line in f:
        data+=(line.rstrip())
    return data


file_data = get_file_data("Day3Input.txt")
regex = "mul\\([0-9]+,[0-9]+\\)"
regex2 = r"do\(\)(.*?)(?=don't\(\))"
matches = re.findall(regex, file_data)
matches2 = re.findall(regex2,file_data)
new_str = ""
text_file = open("test.txt", "w")
for match in matches2:
    text_file.write(match)
text_file.close()
file_data2 = get_file_data("test.txt")
matches3 = re.findall(regex,file_data2)
total = 0
for str in matches:
    print(str)
    open_num = str.index("(")
    close_num = str.index(")")
    comma_num = str.index(",")
    num1 = str[open_num+1 : comma_num]
    num2 = str[comma_num+1 : close_num]
    sum = int(num1)*int(num2)
    total += sum
print(total)
