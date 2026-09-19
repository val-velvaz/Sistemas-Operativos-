import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import Qt

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("Mi Primera Ventana en Qt")
        self.resize(400, 200)

        # Contador de clics
        self.contador = 0

        # Componentes (Widgets)
        self.etiqueta = QLabel("¡Hola! Presiona el botón:", self)
        self.etiqueta.setAlignment(Qt.AlignCenter)

        self.boton = QPushButton("Haz clic aquí", self)
        # Conectar el evento del botón con una función (Signal & Slot)
        self.boton.clicked.connect(self.al_hacer_clic)

        # Diseño (Layout vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.boton)

        # Contenedor principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def al_hacer_clic(self):
        self.contador += 1
        self.etiqueta.setText(f"¡Has hecho clic {self.contador} veces!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())