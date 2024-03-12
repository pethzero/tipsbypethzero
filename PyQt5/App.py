import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QDialogButtonBox
from PyQt5.uic import loadUi

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('Form.ui', self)  # แทนชื่อไฟล์ XML ที่คุณได้รับจากการสร้างด้วย Qt Designer
    #     # self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.buttonBox.accepted.connect(self.on_pushButton_clicked)
    #     self.buttonBox.rejected.connect(self.reject)

    def on_pushButton_clicked(self):
        print("Button clicked")
        
    # def on_accepted(self):
    #     print("Accepted button pressed")
      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
