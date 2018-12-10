import random

class Word:

    def __init__(self, filename):
        self.words = []
        self.check = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        #개행 문자 단위로 단어 분류하기

        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

    #단어를 무작위로 뽑기
    def randFromDB(self):
        while True:
            r = random.randrange(self.count)
            if r not in self.check:
                self.check.append(r)
                return self.words[r]

