import os
import sys


def frequency_analysis(word_list):
    def mapper(word):
        return 1

    mapped = map(mapper, word_list)
    mapped = zip(word_list, mapped)
    output_dict = dict()
    for x in mapped:
        if x not in output_dict:
            output_dict[x] = 0
        output_dict[x] += 1
    return output_dict

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        return contents

def count_words(word_list):
    return len(word_list)

if __name__ == "__main__":

    filename = "iliad.txt"
    contents = read_file(filename)
    print(f"Content length: {len(contents)}")
    for char in '?!-=+/\'"-.,\n':
        contents = contents.replace(char,' ')
    contents = contents.lower()
    word_list = contents.split()
    word_count = count_words(word_list)
    print(f"Word count: {word_count}")
    reduced = frequency_analysis(word_list)
    sorted_reduced = {k: v for k, v in sorted(reduced.items(), key=lambda item: item[1], reverse=True)}
    for x in sorted_reduced:
        print(f"{x}: {sorted_reduced[x]}")
