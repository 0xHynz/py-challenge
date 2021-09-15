def flatten(l: list[list[int]]) -> list:
    return [hasil for loop in l for hasil in loop]


print(flatten([[1], [2], [3], [4, 5]]))