def capital_indexes(string:str)->list:
    return print([k for k, v in enumerate(string) if v.isupper()])


if __name__ == "__main__":
    capital_indexes("HeLlO")
