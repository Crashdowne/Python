'''
More work from Udemy
'''

# Calculating acceleration

v =25   # Final velocity
u = 0   # Initial velocity
t = 10  # Time

a = (v - u)/t   # Calculate acceleration

print a

# Conditionals

if a == 2:
    print "True"
    
if not a == v:  # Equivalent to !=
    print "a /= v"

if a != 15:
    print "derp"

# <= , >=
# and instead of "&&", or instead of "||"

a,b,c = 0,1,2

if a== v:
    print "a is equivalent to v"
else:
    print "a is not equivalent to v"
    
# use elif instead of multiple if stmnts    

if a > b:
    print "a > b"
elif a < c:
    print "a < c"
else:
    print "comparisons failed, le sad"
    
# Switch stmnts

switch = dict(
              one = 'one',
              two = 'two',
              three = 'three'
              )

var = 'two'

print(switch[var])  # Key error if var is not in the dict (switch[var]), if var = 'four'

var = 'four'

print(switch.get(var, 'default'))   # Workaround for key error

# Inline if, better way to wring if / elif

var = "output" if a == b else "nope"    # variable if check else differentVariable
print var

# Don't have to use inline if, use what works best


# Loops! - Woo

# While loops
a = 0
while a < 100:
    print(a)
    a += 10

# For loops

for data in [1,2,3,4,5]:    # in is a test of membership, used to iterate through a sequence (in [sequence]
    print(data)

for key,data in enumerate("strings"):
    if key % 2 == 0:    # check to see if it is even even
        print("The letter {} is in an even location".format(data))  # {} gives data at the chosen location

# Exceptions

tuple = (1,2,3,4,5)

try:
    #tuple.append(6)    # This will throw an error if uncommented
    for each in tuple:
        print each
except AttributeError as e:
    print "Error: ", e

# Break, etc
print "\nBreaks, etc\n"


list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        #break    Will stop at 7
        continue # Will skip 7
    else:
        print int
else:               # Putting an else here makes it cleaner
    print "end" 

print "\nFib Sequence\n"

val1 = 0
val2 = 1
n = 0
print val1
print val2

while n < 101:
    n = val1 + val2
    print n
    val1 = val2
    val2 = n

print "\nLists & such\n"

list = [1,2,3,4,5,6,7,8,9,10,11]

print(list)

print(list[2])  # list[2] is the item at the key of 2, negatives go from right to left
print(list[-4])    # Right - left starts at -1 vs positive starts at 0

print(len(list))    # Prints length of the list

print(list[2:4])    # From value 2 upto, but not including value 4

print(list[2:8:2])  # Second 2 is the step. [::2], step by two through the list








