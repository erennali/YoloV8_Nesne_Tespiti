# Google Colab'da Çalıştırma Rehberi

## 1. Klasör Yapısını Google Drive'a Yükle

Google Drive'ınızda şu yapıyı oluşturun:

```
MyDrive/
└── Uyg2/
    ├── data.yaml
    ├── yolo_training_colab.ipynb
    └── yolo_dataset/
        ├── train/
        │   ├── images/  (103 JPG dosyası)
        │   └── labels/  (103 txt dosyası)
        └── val/
            ├── images/  (27 JPG dosyası)
            └── labels/  (27 txt dosyası)
```

## 2. Yüklenecek Dosyalar

Şu dosyaları/klasörleri Google Drive'a yükle:
- `data.yaml`
- `yolo_training_colab.ipynb` 
- `yolo_dataset/` (tüm içeriğiyle birlikte)

## 3. Colab'da Çalıştırma

1. Google Drive'da `yolo_training_colab.ipynb` dosyasına sağ tık
2. "Birlikte Aç" → "Google Colaboratory"
3. Runtime → Change runtime type → **GPU** seç
4. Hücreleri sırayla çalıştır (Runtime → Run all)

## 4. Beklenen Süre

- GPU ile: ~15-20 dakika
- Eğitim bitince `best.pt` dosyası Drive'a kaydedilir

## 5. Sonuç

Eğitim bitince:
- `best.pt` modelini indir
- Lokal bilgisayarında `gui_app.py` ile test et
