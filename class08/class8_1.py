List_1 = [3, 5, 7, 8, 9, 0]
List_2 = [5, 0]
found:list[int] = []

#first we make a copy because we want to keep the original one
List_1_copy = List_1.copy()

# we consider each element in the smaller list
for element in List_2:
    index = 0
    # we need while loop since we are going to print index
    while index < len(List_1_copy):
        if List_1_copy[index] == element:
            print(f"{element} was found at index: {index}")
            found.append(element) #we add it to found
            List_1_copy.remove(element) # we don't want to consider that found element
            break
        index += 1


#if all elements are found, the lengths will be the same - Line 18
#if length of found is not equal but also not 0, then not all elements are found - Line 20
#or at last we can say none of them are found- Line 22
if len(found) == len(List_2) :
    print(f"Yes, {List_2}appears in {List_1}.")
elif len(found) != 0:
    print(f"But not all {List_2} appears in {List_1}.")
else:
    print(f"None of them are in {List_1}.")

