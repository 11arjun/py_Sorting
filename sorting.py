# Write a Python function that takes a list of integers and returns the second-largest number in the list.
numbers = [100, 50, 20, 80, 80, 15,1,2,3,33434,43434,434342334,56546,56,87,8,6782,32323]
# we can use sort function for ascending order
#numbers.sort() 
#Initially lets separate the unique
# we can use sort function for descending order
# If i use sort function the it modifies the original list  but if we need to preserve the original list we have tp use sorted
highest = max(numbers)
second_highest = sorted(numbers, reverse=True)
print("The highest number is ", highest)
print("The second highest number is ", second_highest[1])
