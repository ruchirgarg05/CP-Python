####################################################################################### Fenwick Tree #######################################################
# Fenwick tree for zero based arrays. (add +1 to idx in ft update.)

# implement Binary Index Tree
def update(index, value, tree, size):
    index += 1  # index in BIT is 1 more than the original index
    while index < size:
        tree[index] += value
        index += index & -index

def query(index, tree):
    # return sum of [0, index)
    result = 0
    while index >= 1:
        result += tree[index]
        index -= index & -index
    return result

############################################################################ Sorted List ################################################################################

sortedList = []
for num in nums:
    position=bisect.bisect_left(sortedList, num) # Position where to insert
    bisect.insort(sortedList,num)
    
