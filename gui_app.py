import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFileDialog,
                             QTextEdit, QGroupBox)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO
import cv2
import os

class YOLODetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = None
        self.current_image_path = None
        self.result_image = None
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('YOLOv8 Nesne Tespiti - Eren Ali Koca')
        self.setGeometry(100, 100, 1200, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        images_layout = QHBoxLayout()
        
        original_group = QGroupBox("Orijinal Görsel")
        original_layout = QVBoxLayout()
        self.original_label = QLabel()
        self.original_label.setFixedSize(550, 450)
        self.original_label.setAlignment(Qt.AlignCenter)
        self.original_label.setStyleSheet("border: 2px solid #555; background-color: #222;")
        original_layout.addWidget(self.original_label)
        original_group.setLayout(original_layout)
        
        tagged_group = QGroupBox("Etiketlenmiş Görsel")
        tagged_layout = QVBoxLayout()
        self.tagged_label = QLabel()
        self.tagged_label.setFixedSize(550, 450)
        self.tagged_label.setAlignment(Qt.AlignCenter)
        self.tagged_label.setStyleSheet("border: 2px solid #555; background-color: #222;")
        tagged_layout.addWidget(self.tagged_label)
        tagged_group.setLayout(tagged_layout)
        
        images_layout.addWidget(original_group)
        images_layout.addWidget(tagged_group)
        
        buttons_layout = QHBoxLayout()
        
        self.select_btn = QPushButton('Görsel Seç')
        self.select_btn.clicked.connect(self.select_image)
        self.select_btn.setStyleSheet("padding: 10px; font-size: 14px;")
        
        self.test_btn = QPushButton('Tespit Et')
        self.test_btn.clicked.connect(self.test_image)
        self.test_btn.setEnabled(False)
        self.test_btn.setStyleSheet("padding: 10px; font-size: 14px;")
        
        self.save_btn = QPushButton('Görseli Kaydet')
        self.save_btn.clicked.connect(self.save_image)
        self.save_btn.setEnabled(False)
        self.save_btn.setStyleSheet("padding: 10px; font-size: 14px;")
        
        buttons_layout.addWidget(self.select_btn)
        buttons_layout.addWidget(self.test_btn)
        buttons_layout.addWidget(self.save_btn)
        
        results_group = QGroupBox("Tespit Sonuçları")
        results_layout = QVBoxLayout()
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setMaximumHeight(120)
        self.results_text.setStyleSheet("font-size: 13px; background-color: #f5f5f5;")
        results_layout.addWidget(self.results_text)
        results_group.setLayout(results_layout)
        
        main_layout.addLayout(images_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(results_group)
        
        central_widget.setLayout(main_layout)
        
        self.load_model()
        
    def load_model(self):
        try:
            model_path = '/Users/erenalikoca/Desktop/Uyg2/best.pt'
            if os.path.exists(model_path):
                self.model = YOLO(model_path)
                self.results_text.append("Model başarıyla yüklendi.")
            else:
                self.results_text.append("UYARI: best.pt bulunamadı. Önce modeli eğitiniz.")
        except Exception as e:
            self.results_text.append(f"Model yükleme hatası: {str(e)}")
    
    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Görsel Seç", "", "Image Files (*.png *.jpg *.jpeg)")
        
        if file_path:
            self.current_image_path = file_path
            pixmap = QPixmap(file_path)
            self.original_label.setPixmap(
                pixmap.scaled(self.original_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.tagged_label.clear()
            self.results_text.clear()
            self.results_text.append(f"Görsel yüklendi: {os.path.basename(file_path)}")
            self.test_btn.setEnabled(True)
            self.save_btn.setEnabled(False)
    
    def test_image(self):
        if not self.current_image_path or not self.model:
            return
        
        try:
            self.results_text.append("\nTespit işlemi başlatıldı...")
            
            results = self.model(self.current_image_path)
            result = results[0]
            
            self.result_image = result.plot()
            
            height, width, channel = self.result_image.shape
            bytes_per_line = 3 * width
            q_image = QImage(self.result_image.data, width, height, 
                           bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            
            pixmap = QPixmap.fromImage(q_image)
            self.tagged_label.setPixmap(
                pixmap.scaled(self.tagged_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
            class_counts = {}
            for box in result.boxes:
                class_id = int(box.cls[0])
                class_name = self.model.names[class_id]
                class_counts[class_name] = class_counts.get(class_name, 0) + 1
            
            self.results_text.append("\nTespit Edilen Nesneler:")
            for class_name, count in class_counts.items():
                self.results_text.append(f"  - {class_name}: {count} adet")
            
            total = sum(class_counts.values())
            self.results_text.append(f"\nToplam tespit: {total} nesne")
            
            self.save_btn.setEnabled(True)
            
        except Exception as e:
            self.results_text.append(f"\nHata: {str(e)}")
    
    def save_image(self):
        if self.result_image is None:
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Görseli Kaydet", "", "PNG Files (*.png);;JPEG Files (*.jpg)")
        
        if file_path:
            cv2.imwrite(file_path, self.result_image)
            self.results_text.append(f"\nGörsel kaydedildi: {os.path.basename(file_path)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YOLODetectionApp()
    window.show()
    sys.exit(app.exec_())
