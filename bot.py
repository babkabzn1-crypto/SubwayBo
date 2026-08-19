class SubwayBot:

    def __init__(self):
        self.lane = 1

    def decide(self, blocked):
        if not blocked[self.lane]:
            return "NOTHING"

        free = [
            i for i in range(3)
            if not blocked[i]
        ]

        if not free:
            return "JUMP"

        target = min(
            free,
            key=lambda x: abs(x - self.lane)
        )

        if target < self.lane:
            self.lane = target
            return "LEFT"

        if target > self.lane:
            self.lane = target
            return "RIGHT"

        return "NOTHING"
