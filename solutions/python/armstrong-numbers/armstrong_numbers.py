def is_armstrong_number(number):
    str_num = str(number)
    power = len(str_num)
    armstrong_number = sum(int(digit) ** power for digit in str_num)
    return number == armstrong_number