marks = [75, 67, 56, 98, 87, 75]
#       0    1    2    3    4
print("list methods")
print("append method")
marks.append(100)
# print list without loop
print(*marks, sep="\n")
print("insert method")
marks.insert(2, 99)
print("list after insert method")
print(*marks, sep="\n")
print("list count method")
print(marks.count(75))
print("add element at the starting of the list")
marks.insert(0, 87)
print("list after insert method")
print(*marks, sep="\n")