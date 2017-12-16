# python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()


class Node:
    def __init__(self, upstream_edge):
        # {edge_string: node}
        # edge_string -> (start_idx, length)
        self.upstream_edge = upstream_edge
        self.next_nodes = dict()

def flat_suffix_tree_edges(tree, text):
    result = []
    if tree.next_nodes:
        result.extend([text[start_idx: start_idx + length] for start_idx, length in tree.next_nodes.keys()])
    for sub_node in tree.next_nodes.values():
        result.extend(flat_suffix_tree_edges(sub_node, text))
    return result


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    root_node = Node('root')

    # Implement this function yourself
    for i in range(len(text)):
        substring = text[i:]
        # print("substring", substring)
        current_node = root_node

        start_idx = i

        while True:
            substring = text[start_idx: ]
            is_going_down = False
            for (edge_start_idx, edge_length) in current_node.next_nodes.keys():
                edge_string = text[edge_start_idx: edge_start_idx + edge_length]

                match_num = 0
                for idx in range(1, len(edge_string)+1):
                    if edge_string[:idx] == substring[:idx]:
                        match_num = idx
                    else:
                        break

                if match_num == edge_length:
                    current_node = current_node.next_nodes[(edge_start_idx, edge_length)]
                    start_idx += match_num
                    # print("match {}, remain substring is {}".format(text[edge_start_idx: edge_start_idx+edge_length],
                    #                                                 text[start_idx: ]))
                    is_going_down = True
                    break
                elif match_num > 0:
                    # upstream edge
                    new_middle_node = Node(text[edge_start_idx: edge_start_idx+match_num])
                    current_node.next_nodes[(edge_start_idx, match_num)] = new_middle_node
                    # move original leaf or node to the children of middle_node
                    original_leaf = current_node.next_nodes.pop((edge_start_idx, edge_length))
                    original_upstream_edge = original_leaf.upstream_edge
                    original_leaf.upstream_edge = text[edge_start_idx+match_num: edge_start_idx+edge_length]
                    # print("replace node to upstream {} its edge change from {} to {}".format(new_middle_node.upstream_edge, original_upstream_edge, original_leaf.upstream_edge))
                    new_middle_node.next_nodes[(edge_start_idx+match_num, edge_length - match_num)] = original_leaf
                    current_node = new_middle_node
                    start_idx += match_num
                    # print("match {}, remain substring is {}, start_idx is {}".format(text[edge_start_idx: edge_start_idx + match_num],
                    #                                                 text[start_idx: ],
                    #                                                 start_idx))
                    is_going_down = True
                    break
                else:
                    continue
            if is_going_down:
                continue
            else:
                if start_idx >= len(text):
                    # print("the substring is fully match in current node, no need to add new edges")
                    pass
                else:
                    new_leaf = Node(text[start_idx: start_idx+len(text[start_idx:])])
                    # print("append new node edge {} to {}".format(new_leaf.upstream_edge, current_node.upstream_edge))
                    current_node.next_nodes[(start_idx, len(text[start_idx:]))] = new_leaf
                break

    return root_node






result = p + q + '#$'
def search(tree, text, upstream_edge):
    '''
    dfs
    :param tree: root node of suffix tree (# $)
    :return:
    '''
    num_p = 0
    num_q = 0
    global result
    for (start_idx, length), node in tree.next_nodes.items():
        current_edge = text[start_idx: start_idx + length]
        current_p = 0
        current_q = 0
        if '#' in current_edge:
            current_p += 1
        if '$' in current_edge:
            current_q += 1
        whole_edge = upstream_edge+current_edge
        _num_p, _num_q = search(node, text, whole_edge)
        current_p += _num_p
        current_q += _num_q

        if current_edge[0] != '#':
            candidate = upstream_edge + current_edge.split('#')[0][0]
            # print("upstream edge {}, current_edge {}".format(upstream_edge, current_edge))
            # if current_p == current_q:
                # print("stat candidate edge {}, num of # {}, num of $ is {}".format(candidate, current_p, current_q))
            if current_p == current_q and len(candidate) < len(result) and candidate:
                result = candidate

        num_p += current_p
        num_q += current_q

    return num_p, num_q



def solve (p, q):

    text = p + '#' + q + '$'
    tree = build_suffix_tree(text)
    # print(flat_suffix_tree_edges(tree, text))
    search(tree, text, '')

solve (p, q)

sys.stdout.write (result + '\n')
