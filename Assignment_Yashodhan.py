r+
Open for reading and writing. The stream is positioned at the beginning of the file.
w+
Opens a file in read and write mode. It creates a new file if it does not exist, if it exists, 
it erases the contents of the file and the file pointer starts from the beginning.
a+
Open for reading and writing. The file is created if it does not exist. The stream is positioned at the end of the file.
















Lists
numbers = [1, 2, 5]
print(numbers)   # Output: [1, 2, 5]

Access List Elements

languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[0])   # Python
# access item at index 2
print(languages[2])   # C++

Negative Indexing in Python

languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[-1])   # C++
# access item at index 2
print(languages[-3])   # Python

Slicing of a  List

# List slicing in Python

my_list = ['y','a','s','h','o','d','h','a','n']
# items from index 2 to index 4
print(my_list[2:5])  # ['s', 'h', 'o']
# items from index 5 to end
print(my_list[5:])   # ['d', 'h', 'a', 'n']
# items beginning to end
print(my_list[:])    # ['y','a','s','h','o','d','h','a','n'] 

List Methods
append()
# Adds List Element as value of List.
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)
Output:
['Mathematics', 'chemistry', 1997, 2000, 20544]

insert()
List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2,10087)	
print(List)	
Output:
['Mathematics', 'chemistry', 10087, 1997, 2000, 20544]

extend()
List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
# Add List2 to List1
List1.extend(List2)
print(List1)
# Add List1 to List2 now
List2.extend(List1)
print(List2)
Output:
[1, 2, 3, 2, 3, 4, 5]
[2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]

length
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))
Output:
10

index()
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))
Output:
1

Tuple

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)         # (1, 2, 3)
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)         #  (1, 'Hello', 3.4)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)         #  ('mouse', [8, 4, 6], (1, 2, 3))

Tuple Methods
Index() 
# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# getting the index of 3
res = Tuple.index(3)
print('First occurrence of 3 is', res)
# getting the index of 3 after 4th
# index
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)
Output:
First occurrence of 3 is 3
First occurrence of 3 after 4th index is: 5
  
Slicing a Tuple 
percentages=(99,95,90,89,93,96)
percentages[2:4]
percentages[:4]
Output
(90, 89)
(99, 95, 90, 89)

Negative indexing
percentages[:-2]
percentages[-2:]
Output
(99, 95, 90, 89)
(93, 96)

len()
my_tuple = (1, 2, 3, [6, 5])
len(my_tuple)
Output
4

Dictionary

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Yash', 2: 'is', 3: 'Good'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Yash', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Output:
Dictionary with the use of Integer Keys: 
{1: 'Yash', 2: 'is', 3: 'Good'}
Dictionary with the use of Mixed Keys: 
{'Name': 'Yash', 1: [1, 2, 3, 4]}

Add Elements to a Dictionary
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)
Output
Initial Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London'}
Updated Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London', 'Japan': 'Tokyo'}
  
Removing elements from Dictionary

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)
Output
Initial Dictionary:  {111: 'Eric', 112: 'Kyle', 113: 'Butters'}
Updated Dictionary  {112: 'Kyle', 113: 'Butters'}

Iterating Through a Dictionary
# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
Output
1
9
25
49
81

Sets
Create a Set 
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
Output
Student ID: {112, 114, 115, 116, 118}
Vowel Letters: {'u', 'a', 'e', 'i', 'o'}
Set of mixed data types: {'Hello', 'Bye', 101, -2}

Add Items to a Set 
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers) 
Output
Initial Set: {34, 12, 21, 54}
Updated Set: {32, 34, 12, 21, 54}

Remove an Element from a Set
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)
Output
Initial Set: {'Python', 'Swift', 'Java'}
Set after remove(): {'Python', 'Swift'}

Iterate Over a Set in Python
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits: 
    print(fruit)
Output
Mango
Peach
Apple

frozenset()
Example 1: Working of frozenset()
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
# frozensets are immutable
fSet.add('v')
Output
The frozen set is: frozenset({'a', 'o', 'u', 'i', 'e'})
The empty frozen set is: frozenset()
Traceback (most recent call last):
  File "<string>, line 8, in <module>
    fSet.add('v')
AttributeError: 'frozenset' object has no attribute 'add'

Example 2: frozenset() for Dictionary
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet)
Output
The frozen set is: frozenset({'name', 'sex', 'age'})
