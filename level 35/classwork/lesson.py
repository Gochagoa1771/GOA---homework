# 1. Create a list named fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 2. Print the entire list
print(fruits)

# 3. Access and print the first and last items in the list
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# 4. Add a new fruit "fig" to the list
fruits.append("fig")

# 5. Remove "banana" from the list
fruits.remove("banana")

# 6. Change the value of the second item to "blueberry"
fruits[1] = "blueberry"

# 7. Print the length of the list
print("Length of the list:", len(fruits))

# 1. Create a list named numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 2. Use the append() function to add the number 100 to the end of the list
numbers.append(100)

# 3. Use the insert() function to add the number 5 at the beginning of the list
numbers.insert(0, 5)

# 4. Use the remove() function to remove the number 30 from the list
numbers.remove(30)

# 5. Use the sort() function to sort the list in ascending order
numbers.sort()

# 6. Use the reverse() function to reverse the order of the list
numbers.reverse()

# 7. Use the index() function to find the index of the number 50
index_of_50 = numbers.index(50)
print("Index of 50:", index_of_50)

# 8. Use the count() function to count how many times 20 appears in the list
count_of_20 = numbers.count(20)
print("Count of 20:", count_of_20)