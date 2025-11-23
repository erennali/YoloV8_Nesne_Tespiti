# YOLOv8 Nesne Tespiti Projesi

**Öğrenci:** Eren Ali Koca  
**Öğrenci No:** 2212721021  
**Ders:** BLG-407 Makine Öğrenmesi  

## Proje Açıklaması

Bu proje, YOLOv8 kullanarak özel bir veri seti üzerinde nesne tespiti yapan bir makine öğrenmesi uygulamasıdır. Proje, model eğitimi ve PyQt5 tabanlı bir GUI uygulaması içermektedir.

## Veri Seti

Veri setimiz 2 sınıfa sahiptir:
- **airpods**: AirPods kablosuz kulaklıkları
- **magic_mouse**: Apple Magic Mouse

Toplam görsel sayısı: 130+ etiketli görüntü

## Proje Yapısı

```
Uyg2/
├── yolo_training.ipynb     # Model eğitim notebook
├── gui_app.py              # PyQt5 GUI uygulaması
├── best.pt                 # Eğitilmiş model ağırlıkları
├── data.yaml               # Veri seti konfigürasyonu
├── dataset/                # Ham veri seti
│   ├── airpods/
│   └── magic_mouse/
└── yolo_dataset/           # YOLOv8 formatında veri seti
    ├── train/
    │   ├── images/
    │   └── labels/
    └── val/
        ├── images/
        └── labels/
```

## Kurulum

### Gereksinimler

```bash
pip install ultralytics
pip install PyQt5
pip install opencv-python
```

### Model Eğitimi

1. Jupyter Notebook'u açın:
```bash
jupyter notebook yolo_training.ipynb
```

2. Tüm hücreleri sırayla çalıştırın.

3. Eğitim tamamlandığında `best.pt` dosyası oluşacaktır.

### GUI Uygulaması

Model eğitildikten sonra GUI uygulamasını çalıştırın:

```bash
python3 gui_app.py
```

## Kullanım

1. **Görsel Seç**: Tespit yapmak istediğiniz görseli seçin
2. **Tespit Et**: YOLOv8 modelini kullanarak nesne tespiti yapın
3. **Görseli Kaydet**: Tespit sonuçlarını içeren görseli kaydedin

## Performans Metrikleri

Model eğitimi sonrasında elde edilen metrikler:
- mAP50: Training sonuçlarında görülebilir
- mAP50-95: Training sonuçlarında görülebilir
- Loss grafikleri: `runs/detect/yolov8_custom_training/` klasöründe

## Özellikler

- ✅ Transfer learning ile YOLOv8n modeli eğitimi
- ✅ PyQt5 ile modern arayüz
- ✅ Gerçek zamanlı nesne tespiti
- ✅ Tespit sonuçlarını kaydetme
- ✅ Detaylı performans raporları

## Lisans

Bu proje eğitim amaçlı hazırlanmıştır.
