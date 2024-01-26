nList = [[-2,5,-99,99],[-3,8,1,-2,10],[1,-7,100,-10]]

postiveList = []
negativeList = []

for i in nList:
    negatives = []
    positives = []
    for j in i: # we can do j in i because i is a list in this case   
        if j < 0:
            negatives.append(j)
        else:
            positives.append(j)
    
    negativeList.append(negatives)
    postiveList.append(positives)

print(f"Output: Positive Numbers = {postiveList}")
print(f"Output: Negative Numbers = {negativeList}")