def longestWord(words):

    length_of_word = len(words[0])
    longest_Word = words[0]

    for word in words:
        if(len(word) > length_of_word):
            length_of_word = len(word)
            longest_Word = word

    return longest_Word

print('Longest Word is ' + str(longestWord(words = ['PHP', 'Exercises', 'Backend'])))