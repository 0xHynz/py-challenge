def mid(text: str) -> str:
    mid: float = len(text)/2
    if mid % 2 == 0.5:
        return ''
    else:
        return text[int(mid)-1]


if __name__ == "__main__":
    print(mid('abdefghijklmno1'))
