def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day5Input.txt")
# you now have a list of Strings from the input file


def part1_solution(file_data):
    page_rules = file_data[file_data.index("") + 1:]
    page_list = file_data[:file_data.index("")]
    new_pairs = []
    for pair in page_rules:
        num_list = pair.split(",")
        for i in range(len(page_list)):
            num_elements = 0
            for num in num_list:
                if page_list[i].__contains__(num):
                    num_elements += 1
            if num_elements>1:
                new_pairs.append(page_list[i])
        for num in num_list:
            correct = num_list.copy()
            order = 0
            for pairs in new_pairs:
                if (pairs.find(num)) > 0:
                    order+=1
                if(order > num_list.index(num)):
                    print(num)
                    correct.remove(num_list)
    print(correct)

    print(new_pairs)




part1_solution(file_data)