class Log:
    def __init__(self, week, amt):
        self.week = week
        self.amount = amt


class inLog(Log):
    def __init__(self, week, amt):
        super().__init__(week, amt)
        self.transactionType = "in"


class outLog(Log):
    def __init__(self, week, amt):
        super().__init__(week, amt)
        self.transactionType = "out"
