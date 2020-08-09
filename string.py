w = "I'm Somasekhar Reddy"
x = 'hello'
y = "hello"
z = 'world'

print(w)
print(x==y)

# indexing is used to grab a single character of the string
# index starts with 0
# reverse index starts with -1
print(x[2])
print(x[-3])

# slicing is used to grab a subsection of the string
# syntax--> [start:stop:jump] where stop is not inclusive

print(x[:]) # returns complete string
print(x[::]) # returns complete string
print(x[2:]) # returns string starting with index 2 till the end
print(x[:3]) # returns string starting with index 0 till the index 2
print(x[1:3]) # returns string starting with index 1 till the index 2
print(x[::2]) # returns string skipping alternate characters
print(x[::-1])# returns reverse string

print(len(y)) # returns count of characters in a string

# strings are immutable; meaning, you can't change a character in a string by assignment. i.e. x[1]= 2 is not allowed

print(x+z) # string concatenation
print(x*5) # repeats the string 5 times