# 🚀 EKSTRA PUAN İÇİN YAPILACAKLAR LİSTESİ

Bu dosya, projenizden ekstra puan almanız için yapmanız gereken adımları sırasıyla anlatır.

## 1. HAZIRLIK (Bilgisayarınızda)
- [x] Gereksiz dosyalar temizlendi (`augment_dataset.py` vb. silindi)
- [ ] **ADIM 1:** `Uyg2 2` klasörünü komple **Google Drive**'ınıza yükleyin.
  - Drive'da `Uyg2 2` adında bir klasör olsun.
  - İçinde `yolo_dataset`, `data.yaml` ve `yolov5_egitim_colab.ipynb` olduğundan emin olun.

## 2. EĞİTİM (Google Colab'da)
- [ ] **ADIM 2:** Google Colab'ı açın (colab.research.google.com).
- [ ] **ADIM 3:** File -> Upload Notebook diyerek `yolov5_egitim_colab.ipynb` dosyasını seçin.
- [ ] **ADIM 4:** Notebook açılınca:
  - Üst menüden **Runtime -> Change runtime type** seçin.
  - **Hardware accelerator** kısmını **GPU** yapın ve Save deyin.
- [ ] **ADIM 5:** Notebook'taki hücreleri sırayla çalıştırın (veya Runtime -> Run all).
  - Google Drive izni isteyecek, izin verin.
  - Eğitim yaklaşık 15-20 dakika sürecek.
  - En sonda "Tüm dosyalar Google Drive'a kaydedildi" yazısını görünce işlem tamamdır.

## 3. SONUÇLARI ALMA (Google Drive'dan)
- [ ] **ADIM 6:** Google Drive'ınıza gidin. `Uyg2 2` klasörüne bakın.
- [ ] **ADIM 7:** Şu yeni dosyaları bilgisayarınıza (proje klasörüne) indirin:
  - `yolov5_best.pt` (Eğitilen model)
  - `yolov5_results.png` (Başarı grafiği)
  - `yolov5_confusion_matrix.png` (Hata matrisi)

## 4. RAPORLAMA (Bilgisayarınızda)
- [ ] **ADIM 8:** Bilgisayarınızdaki `model_comparison.ipynb` dosyasını açın (Jupyter Lab veya VS Code ile).
- [ ] **ADIM 9:** "5. YOLOv5 Sonuçları" kısmına, indirdiğiniz `yolov5_results.png` içindeki değerleri veya eğitim bitince ekranda yazan değerleri girin.
  - Örnek: `mAP50: 0.65` gibi.
- [ ] **ADIM 10:** Notebook'u çalıştırıp grafikleri oluşturun ve kaydedin.

## 5. FİNAL (GitHub)
- [ ] **ADIM 11:** Artık elinizde hem YOLOv8 hem YOLOv5 sonuçları var. Tüm proje klasörünü GitHub'a yükleyin.
- [ ] **ADIM 12:** Hocaya sunarken: "Hocam, YOLOv8 zorunluydu yaptım. Ekstra olarak YOLOv5 ile de eğittim, sonuçları karşılaştırdım, raporu da burada" deyin.

BAŞARILAR! 🎓
