# Define Python operators are as follows:

# Arithmetic operators: +, -, *, /, %, //
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Bitwise operators: &, |, ^, ~, <<, >>
# Assigmnet operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
# Identity operators: is, is not
# Membership operators: in, not in

# The operator precedence in Python is as follows:


# Arthmatic operators Example:

# + 
a=5
b=5
print(a+b)

# -

c=10
d=30
print(d-c)

# *

e=7
f=9
print(e * f)

# /

g=30
h=5
print(g/h)

# %

print(g%h)


print(g**h)

print(g//h)



# Python Assignment Operators

# =

x = 6
y = x
print(y)

# +=
x += 7

print(x)    

# -=

x -= 4

print(x)

# *=

x *= 2

print(x)

# /=

x /= 9

print(x)

# %=

x %= 2

print(x)

# //=

k=5

k //= 2

print(k)

# **=

l = 10

l **= 2

print(l)

# Python Comparison Operators

# ==

a = 10

b = 10

print(a == b)

# !=

print(a != b)

# >

c= 9
d=10

print(d > c)

# <

print(d < c)

# >=

print(d >= c)

# <=

print(d <= c)


# Python Logical Operators

# Logical operators are used to combine conditional statements:

# and 

v = 7

z= v > 6 and v <8

print(z)

# or

o = 7

q= o > 6 or o>8

print(q)


# not

j = 7

u = not(j > 6)

print(u)

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is

f = 8
g=f

print ("g is f=",g is f)

# is not
print ("g is not f=",g is not f)

# Python Membership Operators

# in

fruits =["apple", "orange", "grapes"]

print ("orange" in fruits)

# not in

print("kiwi" not in fruits)

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# &

p = 5

q = 3

print ("p & q =",p & q)

# 2. Bitwise OR (|)

print ("p | q =",p | q)

# 3. Bitwise XOR (^)

print ("p ^ q =",p ^ q)

# 4. Bitwise NOT (~)

print ("~p =",~p)

# 5. Bitwise left shift (<<)

print ("p << 2 =",p << 1)

# 6. Bitwise right shift (>>)

p=10
print ("p >> 2 =",p >> 1)


# If you remember just this, it's enough:

# ✅ 1 & 1 = 1 (For AND)
# ✅ 0 | 1 = 1 (For OR)
# ✅ 1 ^ 1 = 0 (For XOR, because same bits become 0)
# ✅ Left shift (<<) → Multiplies by 2
# ✅ Right shift (>>) → Divides by 2

# That's it! This is a small world of 1s and 0s that you can control! 😃🔥
