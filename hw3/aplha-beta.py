from math import *
# we can use (inf) and (-inf)

# alpha-beta psuedo code
# fun a_b(node, depth, min, max):
#     if node = root or d=0: eval
#     if node = max:
#         v = min
#         for all child of n
#             v^ = minimax(child ,d-1, ...)
#             if v^ > v : v = v^
#                 if v > max return max
# 
#     if node = min:
#         v = max
#         for all child of n
#             v^ = minimax(child ,d-1, ...)
#             if v^ < v : v = v^
#                 if v < min return max
#   return v

class Node:
    def __init__(self):
        self.value = 0
        self.children = []
        return

def alpha_beta( node, depth, v_min, v_max):
    if len(node.children) == 0:
        return node.value
    # max nodes are depth % 2 ==0
    if depth % 2 == 0: # max
        # print("max")
        node.value = v_min
        for kid in node.children:
            v_min_test = alpha_beta( kid, depth+1, v_min, v_max )
            if v_min_test > v_min:
                v_min = v_min_test 
            if v_min > v_max : # beta overtook our max :-/
                return node.value
    else: # min
        # print("max")
        node.value = v_max
        for kid in node.children:
            v_max_test = alpha_beta( kid, depth+1, v_min, v_max )
            if v_max_test < v_min:
                v_max = v_max_test 
            if v_max < v_min : # beta overtook our max :-/
                return node.value
    
    