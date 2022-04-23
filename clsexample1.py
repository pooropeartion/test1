
# How to remove duplicate elements in a list
# python version 3.9.2

list = [1, 2, 3, 4, 5, 5, 5]
elements_store = []
for i in list:
    if i not in elements_store:
        elements_store.append(i)
print(elements_store)