
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data


file_data = get_file_data("Day5Input.txt")
# you now have a list of Strings from the input file
page_pairs = file_data[file_data.index("")+1:]
ordered= []
print(page_pairs)

def part1_solution(data):
    for pair in page_pairs:
        first = pair[:pair.index("|")]
        second = pair[pair.index("|")+1:]
        try:
            ordered.index(second)
        except:
            ordered.append(second)
        try:
            ordered.index(first)
        except:
            ordered.append(first)
    #Move the first to behind the second. Pop the occurence of first beforehand.

    #
#print(ordered)
