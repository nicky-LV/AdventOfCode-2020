with open("input.txt", "r") as f:
    arr = f.read().split("\n")
    f.close()


def part_1(arr):
    count = 0
    for entries in arr:
        password = entries.split(":")[1]
        letter = entries.split(":")[0].split("-")[1][-1]
        min_occurences = int(entries.split(":")[0].split("-")[0])
        max_occurences = int(entries.split(":")[0].split("-")[1].split(" ")[0])

        if min_occurences <= password.count(letter) <= max_occurences:
            print(f"{password} has at least {min_occurences} {letter} and at most {max_occurences} {letter}")
            count += 1

        else:
            print(print(f"{password} has DOES NOT HAVE at least {min_occurences} {letter} and at most {max_occurences} {letter}"))

        print(count)


def part_2(arr):
    count = 0
    for entries in arr:
        password = entries.split(":")[1]
        letter = entries.split(":")[0].split("-")[1][-1]
        # we would usually minus 1 from the policy as it's not zero-indexed
        # but one of the indexes is already taken by whitespace, so we do not have to. index corresponds to length.
        index_1 = int(entries.split(":")[0].split("-")[0])
        index_2 = int(entries.split(":")[0].split("-")[1].split(" ")[0])

        if password[index_1] == letter or password[index_2] == letter:
            if password[index_1] == letter and password[index_2] == letter:
                print(f"{password} index1: {index_1} index2: {index_2} both are {letter}")

            else:  # means that one of the indexes is the letter, the policy is fulfilled
                print(f"{password} index1: {index_1} index2: {index_2} are not both {letter}")
                count += 1

    print(count)

part_2(arr)