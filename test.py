support = {}
item = "abc"
support[item] = 1
try:
    support[item] += 1
except:
    support[item] = 1
print(support[item])