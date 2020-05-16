from binary_search_tree import BSTNode
import time

start_time = time.time()
bstn = BSTNode('hellostring')

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

with open('names_1.txt', 'r')as fp:
    line = fp.readlines()
    names = BSTNode(fp.readlines())
    for i in fp.readlines():
        names.insert(i.strip())

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements


# insert name
for name1 in names_1:
    bstn.insert(name1)
for name2 in names_2:
    if bstn.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
