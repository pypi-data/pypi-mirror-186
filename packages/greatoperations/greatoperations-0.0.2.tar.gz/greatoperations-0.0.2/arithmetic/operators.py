
import functools

def myadd(numbers):
	"""This function take arbitrary number of arguments and return the sum of all"""
	list_1 = list(numbers)
	sum = functools.reduce(lambda a, b : a + b, list_1)
	return sum


def mysub(a, b):
	"""This function take two numbers and return the difference of them"""
	return a - b


def mymul(*numbers):
    """This function take arbitrary number of arguments and return the product of all"""
    list_1 = list(numbers)
    result = functools.reduce(lambda a, b : a * b, list_1)
    return result


def mydiv(a, b):
	"""This function take two numbers and return the quotient of them"""
	return a / b


def power(a, b):
    """This function is used for taking power"""
    return a ** b
