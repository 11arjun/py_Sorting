# Write a Python function that takes a list of integers and returns the second-largest number in the list.
# Lets take 5 inputs from the user
numbers = []
for i in  range(5):
    User  = input("Enter Five Numbers :")
    numbers.append(int(User))
# we can use sort function for ascending order
#numbers.sort() 
#Initially lets separate the unique
# we can use sort function for descending order
# If i use sort function the it modifies the original list  but if we need to preserve the original list we have tp use sorted
highest = max(numbers)
second_highest = sorted(numbers, reverse=True)
print("The highest number is ", highest)
print("The second highest number is ", second_highest[1])
