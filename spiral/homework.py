def spiralize(number):
    return_value = 1
    n = (number - 1) // 2
    x = (2 * n * ((8 * n * n) + (15 * n) + 16)) / 3

    return_value = x
    return return_value


print(spiralize(501))
