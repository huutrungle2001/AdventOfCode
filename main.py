import re


def process_file(filename):
    word_to_num = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        "1": "1",
        "2": '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }
    words = word_to_num.keys()
    pattern = '|'.join(words)
    print(pattern)

    sum1 = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            matches = re.findall(pattern, line)
            if matches:
                num_list = [word_to_num[word] for word in matches]
                sum1 += int(num_list[0] + num_list[-1])
    return sum1


# print(process_file('input.txt'))


word_to_num = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        "1": "1",
        "2": '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }
words = word_to_num.keys()
pattern = '|'.join(words)
print(pattern)
line = "sevenine"
matches = re.findall(pattern, line)
print(matches)