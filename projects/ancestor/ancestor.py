
def earliest_ancestor(ancestors, starting_node):
    unexplored = [[starting_node],]
    while len(unexplored) > 0:
        cur =  unexplored.pop()
        for e in ancestors:
            if e[1] == cur[len(cur)-1]:
                unexplored.append([*cur,e[0]])
    if len(cur) != 1:
        return cur[len(cur)-1]
    else:
        return -1

            



