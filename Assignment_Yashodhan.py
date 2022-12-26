r+
Open for reading and writing. The stream is positioned at the beginning of the file.
w+
Opens a file in read and write mode. It creates a new file if it does not exist, if it exists, 
it erases the contents of the file and the file pointer starts from the beginning.
a+
Open for reading and writing. The file is created if it does not exist. The stream is positioned at the end of the file.




asdfg












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

Sets






