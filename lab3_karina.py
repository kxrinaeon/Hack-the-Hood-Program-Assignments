# Karina Ferreira Gandara | Lab 3 | Intro to Python

# Ticket 1
username = "kxrinaeon"
print(len(username))
# PREDICT: 8
# len() included every character but I feel that it would do that anyways because it was all letters.

# Ticket 2
print(username[0])
print(username[8])
# PREDICT: k and n
# the last index is len(username) minus 1 because index starts at 0 meaning if the username is 9 characters long when starting at 1, you have to shift over your entire count minus 1 to start at 0.

# Ticket 3
first = "Welcome to Loop, "
last = "@kxrinaeon!"
full = first + last
print(full)
print(f"Welcome to Loop, @{username}!")
# PREDICT: I think they will look identical.
# The f-string was easier to me because it was less steps, making it less complicated.

# Ticket 4
print(username.upper())
# username [0] = "X" #TypeError: 'str' object does not support item assignment
#PREDICT: an error message will pop up because it's a string mix mixed with another command
# An immutable string means that the characters of a string cannot be modified in-place.

# Ticket 5
feed = ["Yosemite 2026", "Class of 2026 Graduation", "Gradnite!"]
print(len(feed))
print(feed[0])
# PREDICT: 3 prints for the count and "Yosemite 2026" prints first.
# I used index 0 to get the first post

# Ticket 6
feed.append("June Photo Dump")
print(feed)
# PREDICT: The index of the fourth post will be 3.
# The fourth post sits at index 3 because it gets added to the end of the list.

# Ticket 7
feed.pop(0)
feed.sort()
print(feed)
# PREDICT: The yosemite post will get removed and the class grad post will be first, gradnite, second, and june photo dump third.
# I used the position deletion method and a dot method to order the list in alphabetical order.

# Ticket 8
profile = {"username": "kxrinaeon", "followers": 315, "verified": False}
print(profile["followers"])
# profile[0] # raceback (most recent call last): File "/Users/karinaferreira/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Hack the Hood Program Assignments/Hack-the-Hood-Program-Assignments/lab3_karina.py", line 53, in <module> profile[0] KeyError: 0
# PREDICT: The followers that will print are 315. I think profile [0] will return a type error.
# Dictionaries search things up by key name rather than number index because it's designed to use labels for a quick search rather than using the order of the objects.

# Ticket 9
profile = ["followers"] += 50
profile["bio"] = "MCHS '26 || UCM '30"