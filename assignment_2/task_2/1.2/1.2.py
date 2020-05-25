def filter_long_words(words, n):
    longer_words = []

    for word in words:
        if(len(word) > n):
            longer_words.append(word)
    
    return longer_words

if __name__ == "__main__":
    print('Words length longer than 3 are ', filter_long_words(words=['PHP', 'Exercises', 'Backend'], n=3))