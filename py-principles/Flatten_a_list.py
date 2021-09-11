

def flatten(l):
    finnal_list = []
    for L in l:
        if len(L) > 1:
           for _l in L:
               finnal_list.append(_l)
        if len(L) == 1:
           finnal_list.append(L[0])

    return finnal_list


print (flatten([[1],[2],[3],[4,5]]))
