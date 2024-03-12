import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RichTextBox แยก Input และ Output")
        
        # สร้างเลย์เอาท์สำหรับรับข้อมูลและผลลัพธ์
        layout = QVBoxLayout()
        
        # สร้างเลย์เอาท์สำหรับปุ่ม
        button_layout = QHBoxLayout()
        
        # สร้างปุ่มสำหรับเปลี่ยนเป็นตัวพิมพ์ใหญ่
        btn_upper = QPushButton("เปลี่ยนเป็นตัวพิมพ์ใหญ่")
        button_layout.addWidget(btn_upper)
        
        # สร้างปุ่มสำหรับเปลี่ยนเป็นตัวพิมพ์เล็ก
        btn_lower = QPushButton("เปลี่ยนเป็นตัวพิมพ์เล็ก")
        button_layout.addWidget(btn_lower)
        
        # แสดงผลเลย์เอาท์ปุ่ม
        layout.addLayout(button_layout)
        
        # สร้างกล่องข้อความสำหรับรับข้อมูล
        input_text_box = QTextEdit()
        layout.addWidget(input_text_box)
        
        # สร้างกล่องข้อความสำหรับแสดงผลลัพธ์
        output_text_box = QTextEdit()
        output_text_box.setReadOnly(True)
        layout.addWidget(output_text_box)
        
        # สร้างวิดเจ็ตสำหรับเฟรมหลักและกำหนดเลย์เอาท์
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
