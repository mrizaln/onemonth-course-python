def greet(name):
    return f"Hey {name}!"

def concatenate(word_1, word_2):
    return word_1 + word_2

def age_in_dog_years(age):
    result = age * 7
    return result

print(greet('Maiuna'))
print(greet('Miliana'))

print(concatenate('Maiuna','Miliana'))

print(age_in_dog_years(21))

print(concatenate(word_2='Maiuna', word_1='Miliana'))

name = 'Maiuna'

def print_different_name():
    name = 'Lhyme'
    print(name)

print(name)
print_different_name()
print(name)


# define the function

def uppercase_and_reverse(item):
    return item.upper()[::-1]

print(uppercase_and_reverse(input('silakan inputkan apapun: ')))
