numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)
# Output: [1, 2, 3, 4, 5, 6]

numbers.insert(0, -1)
print(numbers)
# Output: [-1, 1, 2, 3, 4, 5]

numbers.remove(3)
print(numbers)
# Output: [1, 2, 4, 5]

numbers.clear()
print(numbers)
# Output: []

print(1 in numbers)
# Output: True

print(len(numbers))
# Output: 5
