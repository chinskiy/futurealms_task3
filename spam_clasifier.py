import string
import copy


class SpamClasifier:
    def __init__(self, p_spam=0.5, p_ham=0.5):
        self.d_spam = dict()
        self.d_ham = dict()
        self.p_spam = p_spam
        self.p_ham = p_ham

    def learn(self, file_spam, file_ham):
        table = string.maketrans("", "")
        lines_spam = [line.rstrip('\n\r') for line in open(file_spam)]
        lines_spam = [_.translate(table, string.punctuation).lower() for _ in lines_spam]

        lines_ham = [line.rstrip('\n\r') for line in open(file_ham)]
        lines_ham = [_.translate(table, string.punctuation).lower() for _ in lines_ham]

        d = dict()

        for _ in lines_spam:
            for __ in _.split(' '):
                d[__] = 0

        for _ in lines_ham:
            for __ in _.split(' '):
                d[__] = 0

        self.d_ham = copy.deepcopy(d)
        self.d_spam = copy.deepcopy(d)

        for _ in self.d_ham.keys():
            for __ in lines_ham:
                if _ in __:
                    self.d_ham[_] += 1

        for _ in self.d_spam.keys():
            for __ in lines_spam:
                if _ in __:
                    self.d_spam[_] += 1

    def predict(self, string_pr):
        table = string.maketrans("", "")
        string_pr = string_pr.translate(table, string.punctuation).lower().split(' ')
        spam, ham = 1, 1
        try:
            for _ in string_pr:
                spam *= self.d_spam[_]
        except Exception:
            spam = 0

        try:
            for _ in string_pr:
                ham *= self.d_ham[_]
        except Exception:
            ham = 0

        if spam == ham:
            return 'not sure'
        return 'spam' if spam * self.p_spam > ham * self.p_ham else 'ham'
