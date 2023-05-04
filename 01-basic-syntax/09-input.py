# get inputs

# name = input("what's your name:")
# print(f'inputted: {name}')

# the type of inputs are string
# print(type(name))

a = input('please input number a: ')
b = input('please input number b: ')

print(f'the type of a is{type(a)}')

# if we don't transfer them to number, then
print(f'before transferred: a + b = {a + b}')

# after transferred:
print(f'after transferred: a + b = {int(a) + int(b)}')
