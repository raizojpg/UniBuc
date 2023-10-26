import heapq

def encode(e):

    codes = {} 
    for x in e.keys():
        codes[x]=None
    chars = [x for x in e.keys()] 
    freq = [x for x in e.values()]
    nodes = [] 

    class node: 
        def __init__(self, freq, symbol, left=None, right=None): 
            self.freq = freq 
            self.symbol = symbol 
            self.left = left 
            self.right = right 
            # tree direction (0/1) 
            self.huff = '' 
    
        def __lt__(self, nxt): 
            return self.freq < nxt.freq 
    
    def printNodes(node, val=''): 
        newVal = val + str(node.huff) 
        if(node.left): 
            printNodes(node.left, newVal) 
        if(node.right): 
            printNodes(node.right, newVal)  
        if(not node.left and not node.right): 
            #print(f"{node.symbol} -> {newVal}")
            codes[node.symbol] = newVal 
    
    for x in range(len(chars)): 
        heapq.heappush(nodes, node(freq[x], chars[x])) 
    
    #print([n.symbol for n in nodes])

    while len(nodes) > 1: 
        left = heapq.heappop(nodes) 
        right = heapq.heappop(nodes) 
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 
        heapq.heappush(nodes, newNode) 

    printNodes(nodes[0]) 
    return codes


def decode(message):
    pass