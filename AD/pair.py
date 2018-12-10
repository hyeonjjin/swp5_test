class Pair:

    def __init__(self, length, words):
        print(words)
        self.words = words
        self.len = length
        self.count=0
        self.num=0
        self.cc=int()
        self.cc2=int()
        self.ss=""
        self.ss2=""

    # 짝 맞추기
    def pair(self, character,a):
        if self.count == 1:
            if self.cc == a:
                return 2
            else:
                self.cc2 = a
                self.ss2 = character
                self.count = 0
                return True

        elif self.count == 0:
            self.cc = a
            self.ss = character
            self.count += 1
            return False

    # 모든 카드의 짝을 맞춘 경우
    def finished(self):
        if self.len == self.num:
            return True

        else:
            return False

    # 2개의 서로다른 카드를 뽑았을 때
    def comparecard(self):
        if self.ss2 != self.ss:
            return 0,self.cc,self.cc2,self.ss,self.ss2
        else:
            self.num+=1
            return 1,self.cc,self.cc2,self.ss,self.ss2



