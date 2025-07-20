"""
Loops: are pretty much what it sounds like. There are two kinds of loops

1. While Loops - block of code that will run FOREVER, as long as the condition is true

2. For Loops - block of code that will work ONLY on an iterable object.


Iterable Objects: Strings, Lists, Tuples, Dictionaries, Sets, Zip, and Range objects
(just focus on range, strings, and lists for now)

What is an Iterable Object? An objected that can be iterated over (can be counted one by one)
"""


# While Loop Psuedo Code
"""
while(condition is true):
    do
    this
    code
    repeat line by line until the condition is broken
"""


# Example 1
# while True:
#     print("I will print forever until my program crashes, runs out of memory, or my process is killed")
# print("done")

# Example 2
# flag = True
# while flag: # while flag (which equals True)
#     print("flag is up")
#     flag = False
#     print("flag down, I will go back to reverify my condition")
# print("done")

# Example 3 - same with any object
# flag = "this is a sentence"
# while flag: # while flag (which equals True)
#     flag = "another sentence"
# print("done")

# Example 4 - same with any object
# flag = 46
# while flag: # while flag (which equals True)
#     flag = 50
#     print("running")
# print("done")



#For Loop Pseudo Code
"""
for (every value index) in the range (up to SPECIFIC VALUE starting from 0) :
    print(index)


for index in range(start,stop,step):

indexing visualized for iterable objects:

        0        1        2        3
Lists[apples, oranges, bananas, lettuce]   

        -4        -3       -2        -1
Lists[apples, oranges, bananas, lettuce]     <---using Negative Numbers

"""

# range(start,stop,step=1)
# #Example 1: 
# for i in range(10):
#     print(i)

# #Example 2:
# for i in range(0, 10):
#     print(i)

# #Example 3:
# for i in range(0, 10, 3):
#     print(i)

# #Example 4:
# for i in range(10, 0):
#     print(i)



