def longestWord(words):
    return max(words, key=len)

print('Longest Word is ' + str(longestWord(words = ['PHP', 'Exercises', 'Backend'])))