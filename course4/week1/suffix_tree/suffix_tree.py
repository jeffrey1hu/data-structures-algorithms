# python3
import sys, threading
from collections import defaultdict
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


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
                    pass
                    # print("the substring is fully match in current node, no need to add new edges")
                else:
                    new_leaf = Node(text[start_idx: start_idx+len(text[start_idx:])])
                    # print("append new node edge {} to {}".format(new_leaf.upstream_edge, current_node.upstream_edge))
                    current_node.next_nodes[(start_idx, len(text[start_idx:]))] = new_leaf
                break

    return flat_suffix_tree_edges(root_node, text)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))