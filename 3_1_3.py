import lib601.sm as sm


class PureFunction(sm.SM):
    def __init__(self, fn):
        self.fn = fn

    def getNextValues(self, state, inp):
        return (state, self.fn(inp))


pureFn = PureFunction(lambda x: x+1)
print(pureFn.transduce([1,4,5,2]))
