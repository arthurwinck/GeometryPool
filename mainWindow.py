import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui/main.ui", self)
        self.buttonComecar.clicked.connect(self.goto_escolha_mesa)
        self.buttonRanking.clicked.connect(self.goto_ranking)
        self.buttonSair.clicked.connect(self.sair)

    def sair(self):
        self.close()
        sys.exit()

    def goto_escolha_mesa(self):
        escolha_mesa = EscolhaMesa()
        widget.addWidget(escolha_mesa)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_ranking(self):
        ranking = Ranking()
        widget.addWidget(ranking)
        widget.setCurrentIndex(widget.currentIndex()+1)

class EscolhaMesa(QMainWindow):
    def __init__(self):
        super(EscolhaMesa, self).__init__()
        loadUi("gui/escolha_mesa.ui", self)
        #self.EMbuttonComecar.clicked.connect(comecarJogo)
        self.EMbuttonVoltar.clicked.connect(self.voltar)

    # def goto_escolha_jogador(self):
    #     escolha_jogador = EscolhaJogador()
    #     widget.addWidget(escolha_jogador)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    def voltar(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


# class EscolhaJogador(QMainWindow):
#     def __init__(self):
#         super(EscolhaJogador, self).__init__()
#         loadUi("gui/escolha_jogador.ui", self)
#         self.EJbuttonVoltar.clicked.connect(self.voltar)
#         #butão para iniciar jogo

#     def voltar(self):
#         widget.setCurrentIndex(widget.currentIndex()-1)

class Ranking(QMainWindow):
    def __init__(self):
        super(Ranking, self).__init__()
        loadUi("gui/ranking.ui", self)
        self.RbuttonVoltar.clicked.connect(self.voltar)

    def voltar(self):
        main = MainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
main = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedHeight(600)
widget.setFixedWidth(815)
widget.show()
app.exec_()