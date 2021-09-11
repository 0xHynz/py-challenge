
def is_anagram(a,b):
    if len(a) != len(b):
       return False

    t1,t2 = sorted(a),sorted(b)

    if t1 != t2:
       return False
    return True

print (is_anagram('hiro','rohi'))
print (is_anagram('test','tess'))
print (is_anagram('hiro','rohis'))

