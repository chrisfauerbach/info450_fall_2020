

with open("iliad.txt", 'r') as iliad, open("bigwords.txt", "w") as big_words, open("smallwords.txt", "w") as small_words:
    contents = iliad.read()
    for char in '?!-=+/\'"-.,\n':
        contents = contents.replace(char,' ')
    contents = contents.lower()
    word_list = contents.split()
    print(word_list[0:100])
    for word in word_list:
        if len(word) > 5:
            big_words.write(f"{word}\n")
        else:
            small_words.write(f"{word}\n")
    
