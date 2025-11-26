import nbformat as nbf

nb = nbf.v4.new_notebook()

text_header = """# BİLGİSAYAR MÜHENDİSLİĞİ - MAKİNE ÖĞRENMESİ PROJE ÖDEVİ
**Adınız:** Eren Ali Koca  
**Okul Numaranız:** 2212721021  
**GitHub Repo Bağlantısı:** https://github.com/erenalikoca/YoloV8_Nesne_Tespiti  

Bu projede YOLOv8 kullanarak nesne tespiti modeli eğitilecektir.
"""

text_kurulum = """## 1. Kütüphane Kurulumu

Bu bölümde YOLOv8 modelini kullanabilmek için gerekli olan Ultralytics kütüphanesini yüklüyoruz.
"""

code_install = """%pip install ultralytics

import ultralytics
from ultralytics import YOLO
from IPython.display import Image
import os
import shutil

ultralytics.checks()
"""

text_dataset = """## 2. Veri Seti Yapısı

Veri setimiz `yolo_dataset` klasöründe şu şekilde organize edilmiştir:
- **train/images**: Eğitim görselleri
- **train/labels**: Eğitim etiketleri (.txt dosyaları) 
- **val/images**: Doğrulama görselleri
- **val/labels**: Doğrulama etiketleri (.txt dosyaları)

Veri setimizde **2 sınıf** bulunmaktadır: `airpods` ve `magic_mouse`

**Etiketleme:** Roboflow veya LabelImg araçları kullanılarak etiketleme işlemi gerçekleştirilmiştir.
"""

text_train = """## 3. Model Eğitimi

Bu bölümde transfer learning yöntemiyle YOLOv8n (nano) modelini kendi veri setimiz üzerinde eğiteceğiz.

**Eğitim Parametreleri:**
- **data**: Veri seti konfigürasyon dosyası
- **epochs**: 50 (Eğitim devir sayısı)
- **imgsz**: 640 (Görüntü boyutu)
- **plots**: True (Grafik oluşturma)
"""

code_train = """model = YOLO('yolov8n.pt')

results = model.train(
    data='/Users/erenalikoca/Desktop/Uyg2/data.yaml',
    epochs=50,
    imgsz=640,
    plots=True,
    name='yolov8_custom_training'
)
"""

text_results = """## 4. Eğitim Sonuçları

Eğitim tamamlandıktan sonra loss değerleri ve mAP metriklerini gösteren grafikleri görselleştiriyoruz.
"""

code_results = """results_path = f'{results.save_dir}/results.png'
if os.path.exists(results_path):
    display(Image(filename=results_path))
else:
    print("Grafik bulunamadı.")
"""

text_val = """## 5. Model Performans Değerlendirmesi

Doğrulama seti üzerinde modelin performansını ölçüyoruz.
- **mAP50**: IoU (Intersection over Union) eşiği 0.5 için ortalama hassasiyet
- **mAP50-95**: IoU eşiği 0.5'ten 0.95'e kadar ortalama hassasiyet
"""

code_val = """metrics = model.val()
print(f"mAP50: {metrics.box.map50:.4f}")
print(f"mAP50-95: {metrics.box.map:.4f}")
"""

text_export = """## 6. Eğitilmiş Modelin Kaydedilmesi

En iyi performans gösteren model ağırlıkları `best.pt` dosyası olarak kaydedilir.
"""

code_export = """best_model_path = f'{results.save_dir}/weights/best.pt'
destination_path = '/Users/erenalikoca/Desktop/Uyg2/best.pt'

if os.path.exists(best_model_path):
    shutil.copy(best_model_path, destination_path)
    print(f"Model kaydedildi: {destination_path}")
else:
    print("Model dosyası bulunamadı.")
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text_header),
    nbf.v4.new_markdown_cell(text_kurulum),
    nbf.v4.new_code_cell(code_install),
    nbf.v4.new_markdown_cell(text_dataset),
    nbf.v4.new_markdown_cell(text_train),
    nbf.v4.new_code_cell(code_train),
    nbf.v4.new_markdown_cell(text_results),
    nbf.v4.new_code_cell(code_results),
    nbf.v4.new_markdown_cell(text_val),
    nbf.v4.new_code_cell(code_val),
    nbf.v4.new_markdown_cell(text_export),
    nbf.v4.new_code_cell(code_export)
]

with open('/Users/erenalikoca/Desktop/Uyg2/yolo_training.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Notebook oluşturuldu.")
