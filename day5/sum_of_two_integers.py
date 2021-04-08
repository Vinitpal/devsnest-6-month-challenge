# This is the best explanation for this problem I could find:
# Following is an excerpt form Cracking the Coding Interview book: https://www.careercup.com/book


# Our first Instinct in problems like these should be that we're going to have to work with bits.
# Why, Because when you take the + sign, what other choice do we have? Plus, that's how computers do it!
# Our next thought should be to deeply understand how addition works. 
# We can walk through an addition problem to see if we can understand something new—some pattern—and 
# then see if we can replicate that with code. So let, do just that—let, walk through an addition problem. 
# We'll work in base 10 so that it, easier to see.


# To add 759 + 674, would usually add digit [0] from each number, carry the one, add digit [1] from each number,
# carry the one, and so on. You could take the same approach in binary: add each digit, and 
# carry the one as necessary.
# Can we make this a little easier? Yes! Imagine I decided to split apart the "addition" and "carry" steps. 
# That is, I do the following:


# Add 759 + 674, but "forget" to carry. I then get 323.
# Add 759 + 674 but only do the carrying, rather than the addition of each digit. I then get 1110.
# Add the result of the first two operations 
# (recursively, using the same process described in step 1 and 2): 1110 + 323 = 1433.
# Now, how would we do this in binary?


# If I add two binary numbers together, but forget to carry, 
# the ith bit in the sum will be 0 only if a and b have the same ith bit (both 0 or both 1).
# This is essentially an XOR.


# If I add two numbers together but only carry, 
# I will have a 1 in the ith bit of the sum only if bits i - 1 of a and b are both 1s. 
# This is an AND, shifted.
# Now, recurse until there's nothing to carry.	


# ---------------------------------------------------------------------------------------------------------- #

# Why we used mask?

# In Python unlike other languages the range of bits for representing a value is not 32, 
# its much much larger than that. This is great when dealing with non negative integers, 
# however this becomes a big issue when dealing with negative numbers ( two's compliment)

# Why ?

# Lets have a look, say we are adding -2 and 3, which = 1

# In Python this would be ( showing only 3 bits for clarity )

# 1 1 0 +
# 0 1 1

# Using binary addition you would get

# 0 0 1

# That seems fine but what happended to the extra carry bit ? ( 1 0 0 0 ), 
# if you were doing this by hand you would simply ignore it, but Python does not, 
# instead it continues 'adding' that bit and continuing the sum.

# 1 1 1 1 1 1 0 +
# 0 0 0 0 0 1 1
# 0 0 0 1 0 0 0 + ( carry bit )

# so this actually continues on forever unless ...

# Mask !

# The logic behind a mask is really simple, you should know that x & 1 = x right, so using that simple principle,

# if we create a series of 4 1's and & them to any larger size series, 
# we will get just that part of the series we want, so

# 1 1 1 1 1 0 0 1
# 0 0 0 0 1 1 1 1 &

# 0 0 0 0 1 0 0 1 ( Important to note that using a mask removes the two's compliment)

a = 1
b = -5
max =  0b01111111111111111111111111111111
mask = 0b11111111111111111111111111111111

def getSum(a, b):
    if b == 0:
        if a <= max:
            return a
        else:
            return ~(mask^a)
    return getSum(mask & (a^b), mask & ((a & b)<<1))

print(getSum(a,b))