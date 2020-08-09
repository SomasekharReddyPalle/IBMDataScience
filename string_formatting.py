'''
There are three ways to perform string formatting.
    The oldest method involves placeholders using the modulo % character.
    An improved technique uses the .format() string method.
    The newest method, introduced with Python 3.6, uses formatted string literals, called f-strings.
'''

# formating with %s, %d, %x.yf, %r

print('This is %s text' %'inserted')
print('This is %r text' %'inserted')
print('This is %s text' %'\ninserted')
print('This is %r text' %'\ninserted')
print('This is %s %s text' %('some','inserted'))
x= 'more'
y = 'inserted'
print('This is %s %s text' %(x,y))
print('This is line-%s' %4.2556)
print('This is line-%d' %4.2556)
print('This is line-%1.2f' %4.2556)
print('This is line-%6.2f' %4.2556)
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))


# formating with .format method
print('This is a string with an {}'.format('insert'))
print('This is a string with an {0!r}'.format('insert'))
print('This is a string with an {0!a}'.format('insert'))
print('This is a string with a {} {}'.format('text','insert'))
print('This is a string with a {0} {1}'.format('text','insert'))
print('This is a string with a {0} {0}'.format('text','insert'))
print('This is a string with a {1} {0}'.format('text','insert'))
print('This is a string with a {x} {y}'.format(x='text',y='insert'))
print('This is a string with a {} {}'.format(x,y))
print('{2}, {1}, {0}'.format(*'abc'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
#Using the comma as a thousands separator:
print('{:,}'.format(1234567890))

# Alignment, padding and precision with .format()
# Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more

print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))# {0:8} --> 0 represents first index and 8 represents the width
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
#By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a left, center or right alignment:

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

#You can precede the aligment operator with a padding character

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

print('This is my ten-character, two-decimal number:{:10.2f}'.format(13.579,12.465))
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579,12.465))
print('This is my ten-character, two-decimal number:{1:10.2f}'.format(13.579,12.465))

# formating with f-strings (Formatted String Literals)

name = 'Fred'

print(f"He said his name is {name}.")

#Pass !r to get the string representation
print(f"He said his name is {name!r}.")

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{4}}")
print(f"My 10 character, four decimal number is:{num:10.4f}")