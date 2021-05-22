from Match import Match


class Room(object):
    def __init__(self, queue: list, currentMatch: Match):
        self.queue = queue
        self.currentMatch = currentMatch
