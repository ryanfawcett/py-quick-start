# Data type conversion

# Convert the type of Number to String
num_str = str(11)
float_str = str(3.14)

# Check the type of the result after converted
print(type(num_str))
print(type(float_str))


# Of course, we can convert a string to a number
num_int = int('10')
print(type(num_int))

num_float = float('3.14')
print(type(num_float))

# Notice: A non-number string cannot be converted to a Number.
# Otherwise, a ValueError will be encountered
# int('Hello World!')

# 2. An integer can be converted to a float and vice-versa
num_convert_from_float = int(num_float)
print(num_convert_from_float)  # but precision loss will be occurred. the result is 3
