# python3
import sys
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

from collections import defaultdict
node_idx = 0

class SuffixTreeNode:
    def __init__(self, children, parent, string_depth, edge_start, edge_end):
        global node_idx
        # suffixTreeNode
        self.parent = parent
        self.children = children
        # int
        self.string_depth = string_depth
        # int
        self.edge_start = edge_start
        # int
        self.edge_end = edge_end
        # print("create a new node with edge {}".format(text[edge_start:edge_end+1]))
        self.node_idx = node_idx
        node_idx += 1


def create_new_leaf(node, s, suffix):
    leaf = SuffixTreeNode(children={}, parent=node, string_depth=len(s)-suffix, edge_start=suffix+node.string_depth, edge_end=len(s)-1)
    node.children[s[leaf.edge_start]] = leaf
    return leaf

def break_edge(node, s, start, offset):
    start_char = s[start]
    mid_char = s[start + offset]
    # print("add a mid node")
    mid_node = SuffixTreeNode(children={}, parent=node, string_depth=node.string_depth + offset, edge_start=start, edge_end=start+offset-1)
    mid_node.children[mid_char] = node.children[start_char]
    # print("break edge {} with depth {}, start {}, end {}"
    #       .format(text[node.children[start_char].edge_start:node.children[start_char].edge_end+1],
    #               node.children[start_char].string_depth,
    #               node.children[start_char].edge_start,
    #               node.children[start_char].edge_end))
    node.children[start_char].parent = mid_node
    # print("start", start)
    node.children[start_char].edge_start += offset
    # print("into edge {} with depth {}, start {}, end {}"
    #       .format(text[node.children[start_char].edge_start:node.children[start_char].edge_end+1],
    #               node.children[start_char].string_depth,
    #               node.children[start_char].edge_start,
    #               node.children[start_char].edge_end))
    # print("with offset {}".format(offset))
    node.children[start_char] = mid_node
    return mid_node


def st_from_sa(s, order, lcp_arr):
    root = SuffixTreeNode(children=dict(), parent=None, string_depth=0, edge_start=-1, edge_end=-1)

    lcp_pre = 0
    cur_node = root

    for i in range(len(s)):
        suffix = order[i]
        while cur_node.string_depth > lcp_pre:
            cur_node = cur_node.parent
        # now cur_node.string_depth <= lcp_pre
        if cur_node.string_depth == lcp_pre:
            cur_node = create_new_leaf(cur_node, s, suffix)
        else:
            edge_start = order[i-1] + cur_node.string_depth
            offset = lcp_pre - cur_node.string_depth
            mid_node = break_edge(cur_node, s, edge_start, offset)
            cur_node = create_new_leaf(mid_node, s, suffix)
        if i < len(s)-1:
            lcp_pre = lcp_arr[i]
    return root

def invert_suffix_array(order):
    pos = [0] * len(order)
    for i in range(len(order)):
        pos[order[i]] = i
    return pos


def lcp_of_suffix(s, i, j, equal):
    lcp = max(0, equal)
    while i + lcp < len(s) and j + lcp < len(s):
        if s[i + lcp] == s[j + lcp]:
            lcp += 1
        else:
            break
    return lcp


def compute_lcp_array(s, order):
    """
    :param s: text string
    :param order: suffix array order
    :return: lcp array -> len(text)-1
    """
    lcp_arr = [None] * (len(text) - 1)
    lcp = 0
    pos_in_order = invert_suffix_array(order)
    suffix = order[0]
    for i in range(len(order)):
        order_idx = pos_in_order[suffix]
        if order_idx == len(s) - 1:
            lcp = 0
            suffix = (suffix + 1) % len(s)
            continue
        next_suffix = order[order_idx + 1]
        lcp = lcp_of_suffix(s, suffix, next_suffix, lcp-1)
        lcp_arr[order_idx] = lcp
        # next order in <string>
        suffix = (suffix + 1) % len(s)
    return lcp_arr


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    root = st_from_sa(text, sa, lcp)

    tree = defaultdict(list)
    iter_tree(root, tree)
    # Implement this function yourself
    return tree

def iter_tree(root, tree):
    stack = [root]
    while stack:
        root = stack.pop()
        for key in ['$', 'A', 'C', 'G', 'T']:
            if key not in root.children:
                continue
            _char = key
            new_node = root.children[_char]
            stack.append(new_node)
            root_idx = root.node_idx
            new_node_idx = new_node.node_idx
            tree[root_idx].append((new_node_idx, new_node.edge_start, new_node.edge_end+1))
            # print(text[new_node.edge_start: new_node.edge_end+1])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
