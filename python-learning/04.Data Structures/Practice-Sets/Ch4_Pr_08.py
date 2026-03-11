# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add("18")

print(s)
print(type(s))

# Therefore, ans is yes we can both int and set value in a single set