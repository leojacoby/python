from itertools import permutations
one_six = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
circ_perm = list(permutations(one_six, 6))
def get_difference(x, y):
    if x > y:
        return x - y
    else:
        return y - x


def all_unequal(array):
    times_equal = 0
    for i in array:
        for x in array:
            if x == i:
                times_equal += 1
        if times_equal != 1:
            return False
        else:
            times_equal = 0
    return True



line_solution = []
solution_count = 0
for i in circ_perm:
    line_solution.append(get_difference(i[0], i[1]))
    line_solution.append(get_difference(i[1], i[2]))
    line_solution.append(get_difference(i[0], i[3]))
    line_solution.append(get_difference(i[1], i[4]))
    line_solution.append(get_difference(i[2], i[5]))
    line_solution.append(get_difference(i[3], i[4]))
    line_solution.append(get_difference(i[4], i[5]))

    def unequal_check():
        for x in line_solution:
            for y in i:
                if x == y:
                    return False
        if all_unequal(line_solution):
            return True
        else:
            return False

    if unequal_check():
        print(i)
        print(line_solution)
        solution_count += 1
        print ""

    else:
        line_solution = []
print
solution_count





