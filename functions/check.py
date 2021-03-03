def checkdiv(a, b):
    if b == 0:
        raise ZeroDivisionError
    if a % b == 0:
        return True
    else:
        return False