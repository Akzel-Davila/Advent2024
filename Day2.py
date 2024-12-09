def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def day2_solution(data):
    safe_reports = 0
    for rules in data:
        rules = rules.split(" ")
        rules = helper(rules)
        if(rules == rules.sort() or rules == rules.reverse()):
            for i in range(len(rules)-1):
                difference = abs(int(rules[i])-int(rules[i+1]))
                print(difference)
                if(difference<=3 and difference>1):
                    safe_reports +=1
    print(safe_reports)

def helper(rules):
    new_list = []
    for i in range(len(rules)):
        new_list.append(int(rules[i]))
    return new_list

file_data = get_file_data("Day2Input")
# you now have a list of Strings from the input file
day2_solution(file_data)
