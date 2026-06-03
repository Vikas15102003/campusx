# Day 1 - Basic Python
name = "Vikas"
age = 22

print("My Name Is", name)
print("My age", age)

# Simple calculation
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Program find the sum of a 3 digit number entered by the user 
num = int(input("Enter 3 digit number"))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num  % 10

print(a + b + c)