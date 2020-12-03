import math
import itertools

with (open("input.txt", 'r')) as f:
    arr = f.read().split('\n')
    length_of_row = len(arr[0])
    f.close()

list_of_tree_counts = []
product = 0


def traverse(x_increment, y_increment):

    x = 0
    y = 0
    tree_count = 0
    for i in range(len(arr)):  # number of rows
        if y > len(arr) - 1:  # end of the slope is reached
            break

        else:

            if x > length_of_row - 1:
                remainder = x - length_of_row
                x = remainder

            if arr[y][x] == "#":
                tree_count += 1

            x += x_increment
            y += y_increment

    print(tree_count)
    list_of_tree_counts.append(tree_count)


traverse(1, 1)
traverse(3, 1)
traverse(5, 1)
traverse(7, 1)
traverse(1, 2)

print(list_of_tree_counts)