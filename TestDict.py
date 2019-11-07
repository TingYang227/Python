def square_digits(num):
    res = [str(int(i) ** 2) for i in str(num)]
    return int(''.join(res))




num = 9119
print(square_digits(num))