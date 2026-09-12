""" A perfect number equals the sum of its positive divisors.
:param number: int a positive integer
:return: str the classification of the input integer
"""
def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    divisors_sum = sum(num for num in range(1, number) if number % num == 0)
    return "perfect" if divisors_sum == number else "deficient" if divisors_sum < number else "abundant"