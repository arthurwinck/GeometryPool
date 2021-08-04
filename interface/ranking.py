from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow

class Ranking(QMainWindow):
    def __init__(self,  widget):
        super(Ranking, self).__init__()
        loadUi("interface/gui/ranking.ui", self)
        self.widget = widget

        self.RbuttonVoltar.clicked.connect(self.voltar)

    def voltar(self):
        self.widget.setCurrentIndex(0)
