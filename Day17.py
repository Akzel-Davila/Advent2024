def get_file_data(file_name):
    f = open(file_name)
    data = ""
    for line in f:
        data+=(line.rstrip())
    return data

file_data = get_file_data("Day17Input.txt")
old_data = file_data.split(" ")
data = list(map(int,old_data))
def part1_solution(data):
    for i in range(len(data)-1):
        if(data[i]==0):
            data[i] = 1

    print(data)

part1_solution(data)
