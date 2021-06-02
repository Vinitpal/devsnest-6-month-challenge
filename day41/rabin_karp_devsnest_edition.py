s = "adcdbabc"
t = "abc"

# creating hash for the given pattern
a = l = len(t)
p = 26
hash_t = 0

# ord function gives the unicode representation
# of the given word
for c in t:
    hash_t += (ord(c)-100)*p**(l-1)
    l -= 1

# creating hash for string
# and checking if the hash of string is
# equal to the hash of pattern
l = a
i = 0
hash_s = 0

# check for len(pattern) in string
while l > 0:
    hash_s += (ord(s[i])-100)*p**(l-1)
    l -= 1
    i += 1
if hash_t == hash_s:
    print("True: Found at index=", i-a)

# if not found from above then,
# moving one index ahead for whole string
while i < len(s):
    hash_s = (hash_s - (ord(s[i-a])-100)*p**(a-1))*p + ord(s[i])-100
    i += 1
    if hash_s == hash_t:
        print("True: Found at index=", i-a)
