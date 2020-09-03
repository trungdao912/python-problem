def check_exist():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = (3, 4, 1, 2, 7, 6, 5, 8)
    c = {5, 6, 7, 8, 1, 2, 3, 4}

    for number in a:
        if number not in b or number not in c:
            return False
    return True
