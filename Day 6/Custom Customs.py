with open('input.txt', 'r') as f:
    answered_questions = [answer.split('\n') for answer in f.read().split('\n\n')]
    f.close()


def part_two(answers: list):
    summed_count = 0

    for answer in answered_questions:

        list_of_answers = []
        people_in_group = len(answer)

        for i in range(people_in_group):
            for letter in answer[i]:
                list_of_answers.append(letter)

        list_of_unique_letters = []

        for letter in list_of_answers:
            if letter not in list_of_unique_letters:
                list_of_unique_letters.append(letter)

        for unique_letter in list_of_unique_letters:
            count_of_letter = list_of_answers.count(unique_letter)

            if count_of_letter == people_in_group:
                summed_count += 1
                for i in range(count_of_letter):
                    index_of_letter = list_of_answers.index(unique_letter)
                    del list_of_answers[index_of_letter]

    return summed_count


"""
part one (before changing the function to suit both parts due to similarity

def part_one(answers: list):
    questions_answered_per_group = []
    summed_count = 0
    for answer in answered_questions:
        list_of_answers = []
        people_in_group = len(answer)
        print(f"Answer {answer}")
        print(f"People in group {people_in_group}")

        for i in range(people_in_group):
            for letter in answer[i]:
                print(f'Letter {letter}')
                if letter not in list_of_answers:
                    list_of_answers.append(letter)

        questions_answered_per_group.append(list_of_answers)

    for answers in questions_answered_per_group:
        count = len(answers)
        summed_count += count
    return summed_count
    
"""