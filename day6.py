#TASKS
#check if list is sorted or not
def is_sorted(list):
    return list==sorted(list)
a=input("Enter a list of numbers: ")
my_list=list(map(int,a.split()))
if is_sorted(my_list):
    print("The list is sorted.")
else:
    print("The list is not sorted.")

#convert binary to decimal
def binary_to_decimal(binary_str):
    decimal=0
    for digit in binary_str:
        decimal=decimal*2+int(digit)
    return decimal
binary=input("Enter a binary number: ")
print("Decimal equivalent:", binary_to_decimal(binary))

#convert decimal to binary
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary if binary else "0"
decimal = int(input("Enter a decimal number: "))
print("Binary equivalent:", decimal_to_binary(decimal))

#Tribonacci sequence
def tribonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
   
    tribo = [0, 1, 1]
   
    for i in range(3, n):
        tribo.append(tribo[i-1] + tribo[i-2] + tribo[i-3])
    return tribo
num_terms = int(input("Enter the number of terms: "))
print("Tribonacci sequence:", tribonacci(num_terms))

#sum of numbers 
try:
    numbers = list(map(int, input("Enter numbers : ").split()))
    if numbers:
        print("Sum of the numbers:", sum(numbers))
    else:
        print("Error: Please enter at least one number.")
except ValueError:
    print("Error: Please enter only numeric values.")

#product of numbers
import math
numbers = list(map(int, input("Enter numbers: ").split()))
product = math.prod(numbers)
print("Product of the numbers:", product)

#pattern
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

n = int(input("Enter the number of rows: "))
print_pyramid(n)

#PATTERN 2
def print_square(n):
    for i in range(n):
        print("* " * n)
n = int(input("Enter the number of rows and columns: "))
print_square(n)

