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

################################################################ segment tree ########################################################
MAXN = int(1e5)
t= [0]4*MAXN
n = MAXN
def build(arr, idx, tl, tr):  
    if tl == tr:
        t[idx] = arr[tl];
    else:
        tm = (tl + tr) // 2
        build(arr,idx*2, tl, tm)
        build(arr, idx*2+1, tm+1, tr)
    t[idx] = t[idx*2] + t[idx*2+1];    
        
def query(idx, tl, tr, l, r):
    if l > r:
        return 0
    if l == tl and r == tr:
        return t[idx]
    tm = (tl + tr) // 2
    return query(idx*2, tl, tm, l, min(r, tm))
           + query(idx*2+1, tm+1, tr, max(l, tm+1), r)
        
    
def update(idx, tl, tr, pos,  new_val):
    if tl == tr: 
        t[idx] = new_val
    else:
        tm = (tl + tr) // 2;
        if pos <= tm:
            update(idx*2, tl, tm, pos, new_val)
        else
            update(idx*2+1, tm+1, tr, pos, new_val)
        t[idx] = t[idx*2] + t[idx*2+1]
###################################################################### Seg tree Lazy Prop ######################################################################
MAXN = int(1e5)
t= [0]4*MAXN
lazy = 
n = MAXN
def build(arr, idx, tl, tr):  
    if tl == tr:
        t[idx] = arr[tl];
    else:
        tm = (tl + tr) // 2
        build(arr,idx*2, tl, tm)
        build(arr, idx*2+1, tm+1, tr)
    t[idx] = t[idx*2] + t[idx*2+1]
    
    
def push(idx):
    if marked[idx]:        
        lazy[idx+idx] = lazy[idx+idx+1] = lazy[idx]
        lazy[idx+idx] = lazy[idx+idx+1] 
        lazy[idx] = 0
        marked[idx] = False    
    
def update(idx, tl, tr, l, r, add_val):
    # This is seg tree for range sum query.
    if l > r:
        return
    if l == tl and r == tr:
        t[idx] += add_val
        marekd[idx] = True
        
    else:
        push(idx)
        tm = (tl + tr) // 2;
        update(idx*2, tl, tm, l, min(r, tm), add_val);
        update(idx*2+1, tm+1, tr, max(l, tm+1), r, add_val)

int get_sum(int v, int tl, int tr, int pos) {
    if tl == tr:
        return t[v]
    tm = (tl + tr) // 2
    if pos <= tm:
        return t[v] + get(v*2, tl, tm, pos)
    else:
        return t[v] + get(v*2+1, tm+1, tr, pos)
    
    
############################################################################## Ordered Sets Like C++ #####################################################################
import collections

class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)
    
########################################################################################### UNION FIND ###############################################################
 
 class Union(object):
    """
    Usage:
    
    islands = Union()
    for p in map(tuple, positions):
          islands.add(p)
          for ne in p.neighbors:
              unit(ne, p)
              return isnlands.count
    """
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1
    
        
    
##################################################################################### Djikstras ####################################################################
import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'X'))
        
 



