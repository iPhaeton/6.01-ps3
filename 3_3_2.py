def recursiveRef(l, indices):
    if len(indices) == 0:
        return l
    else:
        return recursiveRef(l[indices[0]], indices[1:])


nested = \
    [
        [
            [1, 2],
            3
        ],
        [
            4,
            [5, 6]
        ],
        7,
        [8, 9, 10]
    ]

print recursiveRef(nested, [3])