def mapList(fn, l):
    return [fn(x) for x in l]

def sq(x): return x*x
# print mapList(sq, [1,2,3,4])

def sumAbs(l):
    return sum(mapList(abs, l))

# print sumAbs([1,2,-3,-5,8]) #19

def mapSquare(fn, l):
    return [[fn(y, x) for x in l] for y in l]

def diff(x, y): return x - y
print mapSquare(diff, [1,2,3])