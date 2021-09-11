
def capital_indexes(string):
    i = []
    num = 0
    for s in string:
        if s.isupper():
           i.append(num)
        num += 1
    return print (i)

if __name__=="__main__":
   capital_indexes("HeLlO")
