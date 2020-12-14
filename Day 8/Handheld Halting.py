with open('input.txt', 'r') as f:
    arr = [line.split(' ') for line in f.read().split('\n')]
    f.close()


def part_one(arr: list) -> any:
    accumulator = 0
    used_commands = []
    pointer = 0
    terminated = True

    # todo: add check if pointer >= length of list, then terminate. ask on discord

    for i in range(len(arr)):
        if pointer < 0 or pointer >= len(arr):
            terminated = True
            break

        command, value = arr[pointer]

        if value[0] == '+':
            value = int(value.strip("+"))

        elif value[0] == '-':
            value = int(value.strip("-"))*(-1)

        if command == "acc":
            accumulator += value
            pointer += 1

        elif command == "jmp":
            pointer += value

        else:
            pointer += 1

        if pointer in used_commands:
            terminated = False
            break

        else:
            used_commands.append(pointer)

    if terminated is True:
        return [True, accumulator]

    else:
        return [False, accumulator]
    
print(part_one(arr)[1])


def check_for_termination(arr):
    if part_one(arr)[0] is True:  # program terminated successfully
        accumulator = part_one(arr)[1]
        print("Program terminated.")
        print(f"Final accumulator: {accumulator}")
        return True

    else:
        print("Program did not terminate.")
        return False


def part_two(arr: list) -> any:

    for i in range(len(arr)):
        command, value = arr[i]
        print(f"- COMMAND: {command} - VALUE: {value} -")
        if command == "jmp":
            arr[i] = "nop", value
            print(f"Switched to {arr[i]}")
            if check_for_termination(arr) is True:
                check_for_termination(arr)
                break

            else:
                arr[i] = "jmp", value

        elif command == "nop":
            arr[i] = "jmp", value
            print(f"Switched to {arr[i]}")
            if check_for_termination(arr) is True:
                check_for_termination(arr)

            else:
                arr[i] = "nop", value

part_two(arr)