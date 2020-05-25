word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))

input_data = ['x','y','z']
result = [ item*num for item in input_data for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))

input_data = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_data  ]
print("['x','y','z'] => " +   str(result))

input_data = [2,3,4]
result = [ [item+num] for item in input_data for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

input_data = [2,3,4,5]
result = [ [item+num for item in input_data] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

input_data=[1,2,3]
result = [ (b,a) for a in input_data for b in input_data]
print("[1,2,3] =>" +  str(result))