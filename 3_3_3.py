class Account():
    def __init__(self, initialState):
        self.state = 0
        self.initialState = initialState

    def start(self):
        self.state = self.initialState

    def step(self, inp):
        self.state = 1.05 * self.state + inp
        return self.state

    def run(self, n = 20):
        self.start()
        [self.step(0) for i in range(n)]
        return self.state

account = Account(100)
print account.run(23)