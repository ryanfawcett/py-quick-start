# String

# Single quotes
greet = 'Hello World'

# Quotes
foo = "foo"

# Triple quotes
baz = """baz"""

# How to define a quotes in String?
name = 'ryan fawcett'
_name = "'ryan fawcett'"

# Of course, there's another way to define the quotes in a String
# we can use the escapes '\'
name_with_escapes = "\"ryan fawcett\""
print(name_with_escapes)

# Extension

# 1. String Concatenation
print(greet + " " + name)

# Generally, a variable which defined with a Number, so we can't
# concat it with a String. otherwise, an error will be encountered.

# 2. Concatenating strings by placeholders
concat_greet = "Hello World! %s" % name
print(concat_greet)

# We can concat a Number with strings using placeholders
electricity_bill = 100
message = "I charged %s of electricity bill today" % electricity_bill
print(message)

# Also, we can concat multiple strings using the placeholders,
# but we must put the variables in a '()'

threshold = 80
currentVal = 93

multiple_concat_message = "The threshold is %s, but now %s, we need do something" % (threshold, currentVal)

print(multiple_concat_message)

# 3. Precision Control
num1 = 12
num2 = 12.346

print("12宽度限制5, 结果是：%5d" % num1)
print("12宽度限制为1，结果是：%1d" % num1)

# float
print("12.346宽度限制为7，小数精度为2，结果是：%7.2f" % num2)
print("12.346不限制宽度，小数精度为2，结果是：%.2f" % num2)

