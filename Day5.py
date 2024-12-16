def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day5Input.txt")
# you now have a list of Strings from the input file
page_rules = file_data[file_data.index("")+1:]
ordered= []
print(page_rules)

def part1_solution(file_data):
    page_rules = file_data[file_data.index("") + 1:]
    page_list = file_data[:file_data.index("")]
    print(page_list)
    for pair in page_rules:
        num_list = pair.split(",")
        print(num_list)
        for num in num_list:
            #Compare the num to the string of the page pairs



part1_solution(file_data)
