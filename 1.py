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
    
####################################################################### Trie ###################################################################################
_end = '_end_'
def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root
def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict
############################################################################# Z Algo ################################################################################
def z_function(s):
    n = len(s)
    z = [0]*(n)
    l, r = 0, 0
    for i in range(n):
        if i <= r:
            z[i] = min (r - i + 1, z[i - l])
        while (i + z[i] < n and s[z[i]] == s[i + z[i]]):
            z[i] += 1;
        if (i + z[i] - 1 > r):
            l = i;
            r = i + z[i] - 1
    return z
####################################


