def safeAdd(v1, v2):
    if v1 == 'undefined' or v2 == 'undefined':
        return 'undefined'
    else:
        return v1 + v2

def safeMul(v1, v2):
    if v1 == 'undefined' or v2 == 'undefined':
        return 'undefined'
    else:
        return v1 * v2
