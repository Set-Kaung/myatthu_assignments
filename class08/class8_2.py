nList = [[-2,5,-99,99],[-3,8,1,-2,10],[1,-7,100,-10]]

#the final list of lists
postiveList = []
negativeList = []

# the input is a list of list with mixed integers
# we need to check each element in each list in the list and
# separate into two lists for each original list
for i in nList:
    negatives = [] # negatives for the current list
    positives = [] # positives for the current list

    for j in i: # we can do j in i because i is a list in this case
        if j < 0:
            negatives.append(j)
        else:
            positives.append(j)

    negativeList.append(negatives)
    postiveList.append(positives)

print(f"Output: Positive Numbers = {postiveList}")
print(f"Output: Negative Numbers = {negativeList}")
