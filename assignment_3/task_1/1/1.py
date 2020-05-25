def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as zde:
    print('Defaultly Generated ERROR Message =>', zde)
    print("Why on earth you are dividing a number by ZERO!!!")
except Exception as e:
    print(e)
    print("Any other exception")