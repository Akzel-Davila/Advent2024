def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def day1_part1_solution(file_data):
    total = 0
    list_one = []
    list_two = []
    for line in file_data:
        split = line.split("   ")
        list_one.append(split[0])
        list_two.append(split[1])
    list_one.sort()
    list_two.sort()
    for i in range(len(list_one)):
        total += abs(int(list_one[i]) - int(list_two[i]))
    print(total)

def day1_part2_solution(file_data):
    total = 0
    list_one = []
    list_two = []
    for line in file_data:
        split = line.split("   ")
        list_one.append(split[0])
        list_two.append(split[1])
    similarity = 0
    for i in range(len(list_one)):
        for j in range(len(list_two)):
            if(list_one[i] == list_two[j]):
                similarity += 1
                print(list_one[i] + " " + list_two[j])
                print(similarity)
        total += similarity * int(list_one[i])
        similarity = 0
    print(total)
file_data = get_file_data("Day1Input.txt")
day1_part2_solution(file_data)