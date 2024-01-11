__author__ = 'Vemund'


def fibonacci_recursive(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    else:
        return fibonacci_recursive(number-1) + fibonacci_recursive(number - 2)


def fibonacci_iterative(number):
    index = 0
    a = 0
    b = 1
    numbers =[a, b]
    while index < number:
        numbers.append(a+b)
        a, b = b, a + b
        index += 1
    return numbers

def fibonacci_iterative_up_to(number):
    a = 0
    b = 1
    numbers =[a, b]
    while a + b < number:
        numbers.append(a+b)
        print(a+b)
        a, b = b, a + b
    return numbers

def fibonacci_even_sum(number):
    result = 0
    for num in fibonacci_iterative_up_to(number):
        if num % 2 == 0:
            result += num
    return result


#print(fibonacci_recursive(10))
#print(fibonacci_iterative(10))
print(fibonacci_even_sum(4000000))

"""0,1,1,2,3,5,8,13,21,34,55,89,144"""
