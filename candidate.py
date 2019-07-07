class Candidate:

    def __init__(self, word):
        self.word = word
        self.truth_list = len(word) * [0]

    def __repr__(self):
        return "\n" + self.word + "\n" + self.truth_list.__str__() + "\n"
