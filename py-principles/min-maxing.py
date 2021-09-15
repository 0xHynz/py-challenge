
def largest_difference(numbers):
    num = list(reversed(numbers))
    if min(num) == 2:
       return 1
    return max(num)-1


print (largest_difference([1,2,3]))
