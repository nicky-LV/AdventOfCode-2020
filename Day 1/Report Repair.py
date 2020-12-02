import itertools

f = open("array.txt", "r")
arr = list(map(int, f.read().split("\n")))  # array of input


def task_1(arr=arr):  # noqa
    for combinations in itertools.combinations(arr, 2):  # itertools.combinations gets all possible combinations
        if combinations[0] + combinations[1] == 2020:  # if a combination sums to 2020
            print(combinations[0] * combinations[1])  # return the product of the combination

def task_2(arr=arr):  # noqa
    for combinations in itertools.combinations(arr, 3):
        if combinations[0] + combinations[1] + combinations[2] == 2020:
            print(combinations[0] * combinations[1] * combinations[2])


task_2()