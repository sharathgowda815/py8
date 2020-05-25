subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"] 

permuted_list = [(f'{subject} {verb} {object_}') for subject in subjects for verb in verbs for object_ in objects]
for sentences in permuted_list:
    print(sentences)