"""
Makesense.ai Etiketleme Rehberi
================================

1. https://www.makesense.ai/ adresine git

2. "Get Started" butonuna tıkla

3. Tüm görselleri yükle:
   - yolo_dataset/train/images klasöründeki tüm görselleri sürükle
   - yolo_dataset/val/images klasöründeki tüm görselleri sürükle

4. "Object Detection" seç

5. Sol taraftan "+" butonuna tıklayarak sınıfları ekle:
   - airpods
   - magic_mouse

6. Her görselde:
   - Fareyle kutu çiz
   - Sınıf seç (airpods veya magic_mouse)
   - Sonraki görsele geç

7. Tüm görseller bitince:
   - Üst menüden "Actions" → "Export Annotations"
   - Format: "A .zip package containing files in YOLO format"
   - "Export" düğmesine bas

8. İndirilen ZIP'i bu scriptle içe aktar:
   python3 import_makesense_labels.py

Not: Yaklaşık 130 görsel var, sakin sakin 1-2 saatte bitirirsin!
"""
print(__doc__)
