num_of_elements = int(input("enter number of elements: "))
lst = []
for i in range(num_of_elements):
    x = int(input(f"enter item {i + 1}: "))
    lst.append(x)

even_number_count = 0
odd_number_count = 0
for item in lst:
    if item % 2 == 0:
        even_number_count += 1
        # even_number_count = even_number_count + 1
    else:
        odd_number_count += 1
print(f"There are {even_number_count} even numbers")
print(f"There are {odd_number_count} odd numbers")