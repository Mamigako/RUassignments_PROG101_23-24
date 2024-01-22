# ask for input, convert to boolean value.
a = bool(int(input()))
b = bool(int(input()))
c = bool(int(input()))

# post and-gate(e) values are equal to a and not b.
e = a and not b
# post and-gate(f) values are equal to not a and c.
f = c and not a

# post or-gate value is equal to e or f.
d = e or f

#print d.
print(int(d))