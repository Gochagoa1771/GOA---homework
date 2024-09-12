# Step 1: Create the list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Step 2: Print the entire list
print("Original list:", fruits)

# Step 3: Access and print the first and last items
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# Step 4: Add a new fruit "fig" to the list
fruits.append("fig")

# Step 5: Remove "banana" from the list
fruits.remove("banana")

# Step 6: Change the value of the second item to "blueberry"
fruits[1] = "blueberry"

# Step 7: Print the length of the list
print("Length of the list:", len(fruits))

# Print the modified list to see all changes

# Step 1: Create the list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Step 2: Append the number 100 to the end of the list
numbers.append(100)

# Step 3: Insert the number 5 at the beginning of the list
numbers.insert(0, 5)

# Step 4: Remove the number 30 from the list
numbers.remove(30)

# Step 5: Sort the list in ascending order
numbers.sort()

# Step 6: Reverse the order of the list
numbers.reverse()

# Step 7: Find the index of the number 50
index_of_50 = numbers.index(50)

# Step 8: Count how many times 20 appears in the list
count_of_20 = numbers.count(20)

# Print the results
print("Modified list:", numbers)
print("Index of 50:", index_of_50)
print("Count of 20:", count_of_20)
# Step 1: Create the list
numbers = list(range(1, 11))  # This creates a list with integers from 1 to 10

# Step 2: Use slicing to create the first_half list
first_half = numbers[:5]  # Slices the first five elements

# Step 3: Use slicing to create the second_half list
second_half = numbers[5:]  # Slices the last five elements

# Step 4: Use list comprehension to create the squares list
squares = [x**2 for x in numbers]  # Creates a list with squares of each number

# Step 5: Print the lists
print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)
# Step 1: Create the list
temperatures = [72, 68, 75, 70, 78, 74, 71]

# Step 2: Calculate and print the highest temperature
highest_temp = max(temperatures)
print("Highest temperature:", highest_temp)

# Step 3: Calculate and print the lowest temperature
lowest_temp = min(temperatures)
print("Lowest temperature:", lowest_temp)

# Step 4: Calculate and print the average temperature
average_temp = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temp)

# Step 5: Use list comprehension to create a new list with temperatures above 70
above_70 = [temp for temp in temperatures if temp > 70]

# Step 6: Print the above_70 list
print("Temperatures above 70:", above_70)