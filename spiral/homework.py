def spiralize(number):
    return_value = 1
    diagonal = (number - 1) // 2
    return_value = (1 / 3) * (
        diagonal * (8 * diagonal ^ 2 + 13 + diagonal * 15) * 2 + 3
    )

    return return_value


print(spiralize(501))
