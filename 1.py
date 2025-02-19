# pyramid
def print_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
print_pyramid(5)


# diamond pattern
def print_diamond(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = 5 
print_diamond(n)

# inverted triangle

def print_inverted_triangle(height):
    for i in range(height):
        print(" " * i + "*" * (height - i))
height = 5
print_inverted_triangle(height)

# hollow square pattern
def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_hollow_square(5)
# program to identify the only unique number from a list of pairs of numbers.

def find_unique_number(numbers):
    unique_number = None
    for number in numbers:
        if numbers.count(number) == 1:
            unique_number = number
            break
    return unique_number
numbers = [1,1, 2, 2, 3,3, 4, 5, 5]
unique_number = find_unique_number(numbers)
print("The unique number is:", unique_number)

# to find odd or even number
def check_odd_even():
    num = int(input("Enter a number: "))
    return ["even", "odd"][num % 2]

print(check_odd_even())

# code to find missing number in a series.

li = [1, 2, 3, 5,6,7]

def find_missing_number(nums):  
    n = len(nums)  
    total = (n + 1) * (n + 2) // 2  
    sum_of_nums = sum(nums)  
    return total - sum_of_nums

print(find_missing_number(li))

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)