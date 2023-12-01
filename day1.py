input = """""" # Enter your input here! (https://adventofcode.com/2023/day/1/input)

def replace_words_with_numbers(given_string):
    given_string = given_string.replace("one", "o1e")
    given_string = given_string.replace("two", "t2o")
    given_string = given_string.replace("three", "t3e")
    given_string = given_string.replace("four", "f4r")
    given_string = given_string.replace("five", "f5e")
    given_string = given_string.replace("six", "s6x")
    given_string = given_string.replace("seven", "s7n")
    given_string = given_string.replace("eight", "e8t")
    given_string = given_string.replace("nine", "n9e")
    return given_string


def task1(given_input):
    string_list = given_input.split("\n")

    sum = 0

    for string in string_list:
        digits = []
        for char in string:
            if char.isdigit():
                digits.append(char)

        first_digit = digits[0]
        last_digit = digits[-1]
        digit_sum = int(f"{first_digit}{last_digit}")
        sum += digit_sum

    return sum

def task2(given_input):
    string_list = given_input.split("\n")

    sum = 0

    for string in string_list:
        digits = []
        replaced_string = replace_words_with_numbers(string)
        for char in replaced_string:
            if char.isdigit():
                digits.append(char)

        first_digit = digits[0]
        last_digit = digits[-1]
        digit_sum = int(f"{first_digit}{last_digit}")
        sum += digit_sum

    return sum

print(task1(input))
print(task2(input))
