# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 1: Using map() to square each number in the list
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Example 2: Using filter() to filter out even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example 3: Using map() and filter() together to perform more complex operations
modified_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print("Modified numbers (squared odd numbers):", modified_numbers)
