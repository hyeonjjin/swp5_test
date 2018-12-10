import sys,random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSizePolicy,QMessageBox
from PyQt5.QtWidgets import  QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit,  QPushButton, QLabel, QRadioButton

from mylife import Mylife
from word import Word
from pair import Pair

#Game 시작 class
class GameWindow(object):
    def setupUI(self, MainWindow):

        self.x=0     #카드 게임의 행의 개수 변수
        self.y=0     #카드 게임의 열의 개수 변수

        name = QLabel("나의 반쪽을 찾아주세요")
        name2 = QLabel("Level")

        font = name.font()
        font.setPointSize(font.pointSize() + 45)
        name.setFont(font)

        font = name2.font()
        font.setPointSize(font.pointSize() + 15)
        name2.setFont(font)

        # 라디오 박스를 통해 난이도 선택
        self.radio1 = QRadioButton("3 X 4")
        self.radio1.setStyleSheet(
            'QRadioButton{font: 12pt Helvetica MS;} QRadioButton::indicator { width: 12px; height: 12px;};')

        self.radio2 = QRadioButton("4 X 5")
        self.radio2.setStyleSheet(
            'QRadioButton{font: 12pt Helvetica MS;} QRadioButton::indicator { width: 12px; height: 12px;};')

        self.radio3 = QRadioButton("5 X 6")
        self.radio3.setStyleSheet(
            'QRadioButton{font: 12pt Helvetica MS;} QRadioButton::indicator { width: 12px; height: 12px;};')

        self.radio1.clicked.connect(self.radiobtn)
        self.radio2.clicked.connect(self.radiobtn)
        self.radio3.clicked.connect(self.radiobtn)

        # 게임 창의 크기, 이름 설정
        MainWindow.setGeometry(800, 100, 1000, 700)
        MainWindow.setWindowTitle("카드 뒤집기 게임")
        self.centralwidget = QWidget(MainWindow)

        # 게임 시작 button
        self.startbtn = QPushButton('Start Game', self.centralwidget)
        self.startbtn.move(700,580)
        self.startbtn.setFixedWidth(100)
        self.startbtn.setFixedHeight(100)
        font = self.startbtn.font()
        font.setPointSize(font.pointSize() + 4)
        self.startbtn.setFont(font)
        self.startbtn.setEnabled(False)

        # vbox 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(name,Qt.AlignTop)
        vbox.addWidget(name2)
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)
        vbox.setAlignment(Qt.AlignCenter)

        self.centralwidget.setLayout(vbox)
        MainWindow.setCentralWidget(self.centralwidget)

    # 카드 뒤집기 게임의 행과 열의 변수 설정 함수
    def radiobtn(self):
        if self.radio1.isChecked():
            self.x=3
            self.y=4
        elif self.radio2.isChecked():
            self.x=4
            self.y=5
        elif self.radio3.isChecked():
            self.x=5
            self.y=6
        self.startbtn.setEnabled(True)
        return (self.x,self.y)


class CardPair(QWidget):
    def setupUI(self, MainWindow,x,y):
        self.mylife = Mylife()
        self.word = Word('words.txt')
        self.x=x
        self.y=y
        self.timeer = QTimer()
        self.words = [x for x in range(self.x*self.y)]
        self.gameover = False
        self.corr = ""
        check=[]

        # 서로 다른 단어를 서로 다른 위치에 저장
        for i in range(self.x*self.y//2):
            n=0
            w = self.word.randFromDB()
            while n!=2:
                while True:
                    r = random.randrange(self.x*self.y)
                    if r not in check:
                        self.words[r] = w
                        n+=1
                        check.append(r)
                        break

        cardPair = QGridLayout()

        self.pair = Pair(self.x * self.y // 2, self.words)
        #뒤집기 위한 카드버튼 만들기
        self.card = []
        for i in range(self.x * self.y):
            self.card.append(QPushButton(''))
            self.card[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.card[i].setObjectName(str(i))
            font = self.card[i].font()
            font.setPointSize(font.pointSize() + 5)
            self.card[i].setFont(font)
        for i in range(self.x):
            for j in range(self.y):
                cardPair.addWidget(self.card[i * y + j], i, j)

        # 맞춘 정답을 표시해주는 Widget
        self.correct = QTextEdit()
        self.correct.setReadOnly(True)
        self.correct.setFixedWidth(700)
        self.correct.setFixedHeight(70)
        font = self.correct.font()
        font.setPointSize(font.pointSize() + 5)
        self.correct.setFont(font)

        # 목숨, 게임 제목, 메시지 label
        self.namelbl = QLabel("LIFE")
        self.name = QLabel("Flip " + "\n" + "Cards")
        self.name2 = QLabel("message")
        self.name3 = QLabel("Correct Card")

        #각각의 font 크기 지정
        font = self.namelbl.font()
        font.setPointSize(font.pointSize() + 15)
        self.namelbl.setFont(font)

        font = self.name.font()
        font.setPointSize(font.pointSize() + 30)
        self.name.setFont(font)

        font = self.name2.font()
        font.setPointSize(font.pointSize() + 3)
        self.name2.setFont(font)
        self.name3.setFont(font)

        # 현재 목숨 상황을 보여주는 Widget
        self.life = QTextEdit()
        self.life.setReadOnly(True)
        self.life.setFixedWidth(200)
        self.life.setFixedHeight(100)
        self.life.setPlaceholderText(self.mylife.currentShape())

        # 메시지 출력
        self.message = QLineEdit()
        self.message.setReadOnly(True)

        # hbox레이아웃
        hbox = QHBoxLayout()
        hbox.addWidget(self.name3)
        hbox.addWidget(self.correct)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.name2)
        hbox2.addWidget(self.message)

        # vbox레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(self.name)
        vbox.addWidget(self.namelbl, 0, Qt.AlignBottom)
        vbox.addWidget(self.life, 0, Qt.AlignTop)
        vbox.addLayout(hbox2)

        # Game 레이아웃
        gameLayout = QGridLayout()
        gameLayout.addLayout(cardPair, 0, 0)
        gameLayout.addLayout(hbox, 1, 0)
        gameLayout.addLayout(vbox, 0, 1)

        MainWindow.setGeometry(800, 100, 1000, 700)
        MainWindow.setWindowTitle("나의 반쪽은 어디에??")
        self.centralwidget = QWidget(MainWindow)

        # 새로운 게임 시작 Button
        self.newGameButton = QPushButton("New Game",self.centralwidget)
        self.newGameButton.setMaximumHeight(100)
        self.newGameButton.move(850,650)
        self.centralwidget.setLayout(gameLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        #버튼이 눌렸을 때 함수 연결
        for i in range(self.x*self.y):
            self.card[i].clicked.connect(self.guessClick)

    def guessClick(self):
        a=int(self.sender().objectName())

        #game에서 이기지 못하고 졌을경우
        if self.gameover == True:
            self.message.setText("Game over")
            QMessageBox.move(self, 900, 300)
            QMessageBox.about(self, "Game over", 'Start new game')
            return self.message

        success = self.pair.pair(self.words[a],a)

        #성공여부 2:같은 카드를 2번 눌렀을 때, True : 서로 다른 카드를 2개 뒤집었을 때, False : 카드를 한번만 뒤집었을 때
        if success == 2:
            QMessageBox.move(self, 900, 300)
            QMessageBox.about(self, "MSG", 'Click another card')

        # 서로다른 위치의 카드를 뒤집었을 때
        elif success == True:
            j,self.cc,self.cc2,pp,pp2 = self.pair.comparecard()
            self.card[a].setText(str(self.words[a]))

            # 2개의 카드가 다른 카드라면
            if j == 0:

                self.mylife.decreaseLife()
                self.message.setText("Your choice wrong!!")
                if self.mylife.getRemainingLives() != len(self.mylife.text)-1:
                    self.timeer.start(500)
                    self.timeer.timeout.connect(self.timeout)

            # 2개의 카드가 같은 카드라면
            else:
                self.card[self.cc].setEnabled(False)
                self.card[self.cc2].setEnabled(False)
                self.corr = self.corr + "  " + pp2
                self.message.setText("Good choice!!")
                self.correct.setText(self.corr)

        # 카드를 한번만 뒤집었을 때
        elif success == False:
            self.card[a].setText(str(self.words[a]))

        #게임에서 이긴 경우
        if self.pair.finished():
            self.message.setText("Success!")
            QMessageBox.move(self, 900, 300)
            QMessageBox.about(self, "Winner", 'Congratuations!!')

        # 현재 남아있느 목숨을 보여줌
        self.life.setText(self.mylife.currentShape())

        # 남아있는 목숨이 없을 경우 - Game over출력, gameover = True, 카드의 답 출력
        if self.mylife.getRemainingLives() == len(self.mylife.text)-1:
            for i in range(self.x*self.y):
                self.card[i].setText(str(self.words[i]))
            self.message.setText("Game Over")
            QMessageBox.move(self, 900, 300)
            QMessageBox.about(self, "Game over", 'Start new game')
            self.gameover = True

    # 2개의 카드가 다른 경우 정해준 시간동안 보여주고 카드를 뒤집는 함수
    def timeout(self):
        self.card[self.cc].setText(" ")
        self.card[self.cc2].setText(" ")
        self.timeer.stop()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.gameWindow = GameWindow()
        self.cardpair = CardPair()
        self.startUIgameWindow()

    def startUIcardpair(self):
        x,y=self.gameWindow.radiobtn()
        self.cardpair.setupUI(self,x,y)
        self.cardpair.newGameButton.clicked.connect(self.startUIgameWindow)
        self.show()

    def startUIgameWindow(self):
        self.gameWindow.setupUI(self)
        self.gameWindow.startbtn.clicked.connect(self.startUIcardpair)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())