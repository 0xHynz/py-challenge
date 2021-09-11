

def only_ints(a,b):
    if str in [type(a),type(b)]:
       return False
    if bool in [type(a),type(b)]:
       return False
    return True

print (only_ints(12,9))
