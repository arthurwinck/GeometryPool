from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import pyqtSignal

class EscolhaMesa(QMainWindow):
    sinal_iniciar = pyqtSignal()

    def __init__(self, widget):
        super(EscolhaMesa, self).__init__()
        self.widget = widget
        loadUi("interface/gui/escolha_mesa.ui", self)
        
        self.EMbuttonVoltar.clicked.connect(self.voltar)
        self.EMbuttonComecar.clicked.connect(self.iniciar_jogo)
        self.EMbuttonAleatorio.clicked.connect(self.iniciar_aleatorio)

        self.formatoMesa = "Retangular"
        self.numeroCacapa = 4
        
        self.listaMesa = ["Retangular", "Quadrado <Não funcional>"]
        self.indexMesa = 0
        self.listaCacapas = [6]
        self.indexCacapa = 0

        self.anteriorMesa.clicked.connect(self.atualizarMesaAnterior)
        self.proximoMesa.clicked.connect(self.atualizarMesaProximo)

        self.anteriorBuraco.clicked.connect(self.atualizarBuracoAnterior)
        self.proximoBuraco.clicked.connect(self.atualizarBuracoProximo)

    def atualizarMesaAnterior(self):
        if self.indexMesa - 1 < 0:
            self.indexMesa = 0
        else:
            self.indexMesa -= 1

        self.formatoMesa = self.listaMesa[self.indexMesa]
        self.textoFormato.setText(f"{self.formatoMesa}")
        
            
    def atualizarMesaProximo(self):
        if self.indexMesa + 1 > len(self.listaMesa) - 1:
            self.indexMesa = len(self.listaMesa) - 1
        else:
            self.indexMesa += 1

        self.formatoMesa = self.listaMesa[self.indexMesa]
        self.textoFormato.setText(f"{self.formatoMesa}")

    def atualizarBuracoAnterior(self):
        if self.indexCacapa - 1 < 0:
            self.indexCacapa = 0
        else:
            self.indexCacapa -= 1

        self.numeroCacapa = self.listaCacapas[self.indexCacapa]
        self.textoCacapa.setText(f"{self.numeroCacapa}")

    def atualizarBuracoProximo(self):
        if self.indexCacapa + 1 > len(self.listaCacapas) - 1:
            self.indexCacapa = len(self.listaCacapas) - 1
        else:
            self.indexCacapa += 1

        self.numeroCacapa = self.listaCacapas[self.indexCacapa]
        self.textoCacapa.setText(f"{self.numeroCacapa}")

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def iniciar_jogo(self):
        self.sinal_iniciar.emit()

    def iniciar_aleatorio(self):
        self.formatoMesa = "Retangular"
        self.numeroCacapa = 6#self.listaCacapas[randint() % len(self.listaCacapas)]
        self.iniciar_jogo()
