def wordslength(words):
    return list(map(lambda a: len(a), words))

print("Integers corresponding to words ['PHP', 'Exercises', 'Backend'] are"\
    , wordslength(words=['PHP', 'Exercises', 'Backend']))