def square(number): 
    if 1 <= number <= 64:
        result = 2 ** (number - 1)
    else: raise ValueError("square must be between 1 and 64")
    return result
def total():
    return (2 ** 64) - 1
