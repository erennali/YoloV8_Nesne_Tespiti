<div align="center">

# 🎯 YOLOv8 Nesne Tespiti Projesi

### BİLGİSAYAR MÜHENDİSLİĞİ - MAKİNE ÖĞRENMESİ PROJE ÖDEVİ

**Öğrenci:** Eren Ali Koca  
**Öğrenci No:** 2212721021  
**Ders:** BLG-407 Makine Öğrenmesi  
**GitHub:** [erennali/YoloV8_Nesne_Tespiti](https://github.com/erennali/YoloV8_Nesne_Tespiti)

---

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Dataset](https://img.shields.io/badge/Dataset-203_images-orange)

</div>

---

## 📸 Uygulama Görselleri

<div align="center">

### Orijinal Görsel ve Tespit Sonucu

<table>
<tr>
<td width="50%">
<img src="Ekran Resmi 2025-11-23 18.01.33.png" alt="Orijinal Görsel" width="100%"/>
<p align="center"><i>Orijinal Görsel - AirPods</i></p>
</td>
<td width="50%">
<img src="Ekran Resmi 2025-11-23 18.01.46.png" alt="Tespit Sonucu" width="100%"/>
<p align="center"><i>YOLOv8 Tespit Sonucu</i></p>
</td>
</tr>
</table>

</div>

---

## 📋 Proje Hakkında

Bu proje, **YOLOv8** (You Only Look Once v8) derin öğrenme modeli kullanarak özel bir veri seti üzerinde **gerçek zamanlı nesne tespiti** yapan kapsamlı bir makine öğrenmesi uygulamasıdır. 

Proje kapsamında:
- ✅ Kendi veri setimiz oluşturuldu ve etiketlendi
- ✅ YOLOv8 modeli transfer learning ile eğitildi
- ✅ PyQt5 ile kullanıcı dostu bir GUI geliştirildi
- ✅ Model performansı detaylı olarak analiz edildi

---

## 🎯 Veri Seti

### Sınıflar

Veri setimiz **2 farklı sınıf** içermektedir:

| Sınıf | Açıklama | Görüntü Sayısı |
|-------|----------|----------------|
| 🎧 **airpods** | Apple AirPods kablosuz kulaklıklar | 120 |
| 🖱️ **magic_mouse** | Apple Magic Mouse | 120 |

### Veri Seti İstatistikleri

- **Toplam Görüntü:** 240 (ham veri seti)
- **Eğitim Seti:** 158 etiketli görüntü (%78)
- **Doğrulama Seti:** 45 etiketli görüntü (%22)
- **Toplam Etiketli Veri:** 203 görüntü
- **Etiketleme Formatı:** YOLO format (txt dosyaları)
- **Görüntü Formatı:** JPG (3024x4032 piksel)

### Veri Seti Hazırlama Süreci

1. **Görüntü Toplama:** iPhone kamera ile 130+ orijinal fotoğraf çekildi
2. **Veri Artırma:** Veri çeşitliliği için görüntüler çoğaltıldı (240 görüntü)
3. **Etiketleme:** YOLO formatında bounding box etiketleri oluşturuldu
4. **Bölümleme:** %78 eğitim, %22 doğrulama olarak ayrıldı

---

## 📁 Proje Yapısı

```
YoloV8_Nesne_Tespiti/
│
├── 📓 yolo_training.ipynb          # Model eğitim notebook (Jupyter)
├── 📓 yolo_training_colab.ipynb    # Google Colab eğitim notebook
├── 🖥️  gui_app.py                   # PyQt5 GUI uygulaması
├── 🤖 best.pt                       # Eğitilmiş model ağırlıkları (6.2 MB)
├── ⚙️  data.yaml                    # Veri seti konfigürasyonu
├── 📖 README.md                     # Proje dokümantasyonu
│
├── 📂 dataset/                      # Ham veri seti (240 görüntü)
│   ├── airpods/                    # AirPods görselleri (120)
│   └── magic_mouse/                # Magic Mouse görselleri (120)
│
├── 📂 yolo_dataset/                 # YOLOv8 formatında veri seti
│   ├── train/                      # Eğitim seti
│   │   ├── images/                 # Eğitim görselleri (158)
│   │   └── labels/                 # Eğitim etiketleri (158)
│   └── val/                        # Doğrulama seti
│       ├── images/                 # Doğrulama görselleri (45)
│       └── labels/                 # Doğrulama etiketleri (45)
│
└── 📂 runs/                         # Eğitim sonuçları
    └── detect/
        └── yolov8_custom_training/
            ├── weights/            # Model ağırlıkları
            ├── results.png         # Performans grafikleri
            └── confusion_matrix.png # Confusion matrix
```

---

## 📂 Proje Yapısı

Bu proje, düzenli bir çalışma ortamı sağlamak için aşağıdaki klasör yapısına sahiptir:

*   **`models/`**: Eğitilmiş YOLO modelleri (`best.pt`, `yolov8_old.pt` vb.)
*   **`notebooks/`**: Eğitim ve test için kullanılan Jupyter Notebook dosyaları.
*   **`scripts/`**: Veri seti hazırlama ve etiketleme için yardımcı Python scriptleri.
*   **`docs/`**: Proje rehberleri ve dokümantasyon dosyaları.
*   **`results/`**: Eğitim sonuçları, grafikler ve test görselleri.
*   **`test_images/`**: Test için kullanılan ham görseller.
*   **`dataset/`**: Orijinal veri seti.
*   **`yolo_dataset/`**: YOLO formatına dönüştürülmüş veri seti.
*   **`gui_app.py`**: Projenin ana grafik arayüz uygulaması.
*   **`README.md`**: Proje dokümantasyonu.

## 🚀 Kurulum

### Sistem Gereksinimleri

- **Python:** 3.8 veya üzeri
- **İşletim Sistemi:** Windows, macOS, Linux
- **RAM:** Minimum 8 GB (eğitim için)
- **GPU:** Opsiyonel (eğitim hızlandırma için)

### Gerekli Kütüphaneler

```bash
# YOLOv8 ve bağımlılıkları
pip install ultralytics

# GUI için PyQt5
pip install PyQt5

# Görüntü işleme
pip install opencv-python
pip install Pillow

# Jupyter Notebook (opsiyonel)
pip install jupyter
```

### Hızlı Kurulum

```bash
# Repository'yi klonlayın
git clone https://github.com/erennali/YoloV8_Nesne_Tespiti.git
cd YoloV8_Nesne_Tespiti

# Gerekli paketleri yükleyin
pip install -r requirements.txt
```

---

## 🎓 Model Eğitimi

### Yerel Bilgisayarda Eğitim

1. **Jupyter Notebook'u başlatın:**
```bash
jupyter notebook yolo_training.ipynb
```

2. **Tüm hücreleri sırayla çalıştırın**

3. **Eğitim parametreleri:**
   - Model: YOLOv8n (nano)
   - Epoch: 50
   - Batch Size: 16
   - Image Size: 640x640
   - Optimizer: AdamW

### Google Colab'da Eğitim

1. `yolo_training_colab.ipynb` dosyasını Google Colab'da açın
2. Runtime → Change runtime type → GPU seçin
3. Tüm hücreleri çalıştırın

### Eğitim Süresi

- **CPU:** ~2-3 saat
- **GPU (Tesla T4):** ~10-15 dakika
- **Apple M1/M2:** ~30-45 dakika

---

## 🖥️ GUI Uygulaması

### Uygulamayı Başlatma

```bash
python3 gui_app.py
```

### Özellikler

| Özellik | Açıklama |
|---------|----------|
| 📁 **Görsel Seç** | Bilgisayardan JPG/PNG formatında görsel yükleme |
| 🔍 **Tespit Et** | YOLOv8 modeli ile nesne tespiti yapma |
| 💾 **Görseli Kaydet** | Tespit sonuçlarını PNG/JPG olarak kaydetme |
| 📊 **Sonuç Gösterimi** | Tespit edilen nesnelerin sınıf ve sayı bilgisi |
| 🎨 **Bounding Box** | Renkli kutular ile tespit edilen nesneleri gösterme |

### Kullanım Adımları

1. **Görsel Seç** butonuna tıklayın
2. Tespit yapmak istediğiniz görseli seçin
3. **Tespit Et** butonuna tıklayın
4. Sonuçları inceleyin
5. İsterseniz **Görseli Kaydet** ile sonucu kaydedin

---

## 📊 Performans Metrikleri

### Model Başarı Oranları

Eğitim tamamlandıktan sonra elde edilen metrikler:

| Metrik | Değer | Açıklama |
|--------|-------|----------|
| **mAP50** | 0.995 | IoU threshold 0.5'te ortalama hassasiyet |
| **mAP50-95** | 0.995 | IoU threshold 0.5-0.95 arası ortalama hassasiyet |
| **Precision** | 0.998 | Doğru pozitif oranı |
| **Recall** | 1.000 | Tespit edilen gerçek pozitif oranı |

### Sınıf Bazlı Performans

| Sınıf | Precision | Recall | mAP50 | mAP50-95 |
|-------|-----------|--------|-------|----------|
| 🎧 airpods | 0.998 | 1.000 | 0.995 | 0.995 |
| 🖱️ magic_mouse | 0.998 | 1.000 | 0.995 | 0.995 |

### Grafik Sonuçları

Eğitim sonuçları ve performans grafikleri:
- **Loss Grafikleri:** `runs/detect/yolov8_custom_training/results.png`
- **Confusion Matrix:** `runs/detect/yolov8_custom_training/confusion_matrix.png`
- **PR Curve:** `runs/detect/yolov8_custom_training/PR_curve.png`

---

## ✨ Özellikler

### Model Özellikleri

- ✅ **Transfer Learning:** YOLOv8n ön eğitimli modeli kullanıldı
- ✅ **Hızlı Tespit:** Gerçek zamanlı nesne tespiti (~30 FPS)
- ✅ **Yüksek Doğruluk:** %96+ recall oranı
- ✅ **Hafif Model:** 6.2 MB model boyutu

### GUI Özellikleri

- ✅ **Modern Arayüz:** PyQt5 ile kullanıcı dostu tasarım
- ✅ **Türkçe Dil Desteği:** Tüm butonlar ve mesajlar Türkçe
- ✅ **Görsel Karşılaştırma:** Orijinal ve tespit edilmiş görselleri yan yana gösterme
- ✅ **Detaylı Sonuçlar:** Tespit edilen nesne sayısı ve sınıf bilgisi
- ✅ **EXIF Oryantasyon Desteği:** iPhone fotoğrafları otomatik düzeltme

### Teknik Özellikler

- ✅ **Modüler Kod Yapısı:** Temiz ve okunabilir kod
- ✅ **Hata Yönetimi:** Kapsamlı try-except blokları
- ✅ **Bellek Optimizasyonu:** Verimli görüntü işleme
- ✅ **Cross-Platform:** Windows, macOS, Linux desteği

---

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler

| Teknoloji | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| Python | 3.8+ | Ana programlama dili |
| YOLOv8 | 8.3.230 | Nesne tespiti modeli |
| PyQt5 | 5.15+ | GUI geliştirme |
| OpenCV | 4.8+ | Görüntü işleme |
| PyTorch | 2.9+ | Derin öğrenme framework |
| Pillow | 10.0+ | Görüntü manipülasyonu |

### Model Mimarisi

- **Backbone:** CSPDarknet
- **Neck:** PANet
- **Head:** YOLOv8 Detection Head
- **Parametreler:** ~3M
- **GFLOPs:** 8.2

---

## 📈 Model Karşılaştırması (Ekstra)

Proje kapsamında **YOLOv5** modeli de eğitilerek YOLOv8 ile performans karşılaştırması yapılmıştır.

| Model | mAP50 | mAP50-95 | Eğitim Süresi |
|-------|-------|----------|---------------|
| **YOLOv8n** | 0.995 | 0.995 | ~10 dk |
| **YOLOv5s** | 0.991 | 0.627 | ~15 dk |

### 🏆 Ekstra Puan Kazanımları
Bu çalışma ile aşağıdaki ekstra hedefler tamamlanmıştır:
- ✅ **YOLOv5 Kurulumu ve Eğitimi:** Google Colab üzerinde YOLOv5 ortamı kurulup model eğitildi.
- ✅ **Karşılaştırma Raporu:** `model_comparison.ipynb` dosyasında detaylı metrik karşılaştırması yapıldı.
- ✅ **Grafiksel Analiz:** Her iki modelin Loss, mAP ve Confusion Matrix grafikleri analiz edildi.
- ✅ **Sonuç:** YOLOv8n modeli, mAP50-95 metriğinde YOLOv5s'e göre **%58 daha yüksek başarı** (0.995 vs 0.627) göstermiştir.

*Detaylı inceleme için `notebooks/model_comparison.ipynb` dosyasına bakabilirsiniz.*

---

## 📝 Lisans

Bu proje **eğitim amaçlı** hazırlanmıştır ve BLG-407 Makine Öğrenmesi dersi kapsamında geliştirilmiştir.

---

## 👨‍💻 Geliştirici

**Eren Ali Koca**  
Bilgisayar Mühendisliği Öğrencisi  
Öğrenci No: 2212721021

---

## 🙏 Teşekkürler

- **Ultralytics** - YOLOv8 framework'ü için
- **PyQt5** - GUI framework'ü için
- **BLG-407 Öğretim Görevlileri** - Proje desteği için

---

<div align="center">

### ⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

**Son Güncelleme:** 23 Kasım 2025

</div>
