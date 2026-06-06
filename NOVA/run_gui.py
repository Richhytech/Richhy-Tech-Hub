from nova.gui import NovaGUI
from PyQt5.QtWidgets import QApplication

def run_gui():
    app = QApplication([])
    gui = NovaGUI()
    gui.show()
    app.exec_()
if __name__ == "__main__":
    run_gui()
