def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


def day2_solution(data):
    safe_reports = 0
    for rules in data:
        safe = False
        rules = rules.split(" ")
        if(rules == sorted(rules) or rules == rules[::-1]):
            for i in range(len(rules)-1):
                difference = abs(int(rules[i])-int(rules[i+1]))
                if (difference<=3 and difference>=1):
                    safe = True
                else:
                    safe= False
            if(safe):
                safe_reports+=1
    print(safe_reports)


file_data = get_file_data("Day2Input")
# you now have a list of Strings from the input file
day2_solution(file_data)
