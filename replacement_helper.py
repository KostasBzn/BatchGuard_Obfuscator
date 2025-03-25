class ReplacementHelper:
    def __init__(self, replace_with, every_nth):
        self.counter = 0
        self.replace_with = replace_with
        self.every_nth = every_nth

    def doit(self, match):
        self.counter += 1
        return match.group(1) if self.counter % self.every_nth else self.replace_with