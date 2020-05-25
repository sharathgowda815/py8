def myfilter(func, sequence):
    result = []
    
    for item in sequence:
        if func(item):
            result.append(item)
    
    return result

def is_greater(x):
    if(x > 5):
        return True
    return False

print('Numbers greater than 5 in list[1,4,7,8,9] is '+ str(myfilter(is_greater, [1,4,7,8,9])))