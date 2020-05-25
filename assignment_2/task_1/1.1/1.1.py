
def myreduce(func, seq):
    
    result = seq[0]
    
    for item in seq[1::]:
        result = func(result, item)
      
    return result

print(myreduce(lambda x, y: x+y, [1,2,3]))