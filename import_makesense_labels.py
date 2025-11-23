import os
import shutil
import zipfile

print("🎯 Makesense.ai Etiket İçe Aktarma Scripti\n")

zip_path = input("İndirdiğin ZIP dosyasının yolunu yapıştır (sürükle-bırak yapabilirsin): ").strip().replace("'", "")

if not os.path.exists(zip_path):
    print("❌ Dosya bulunamadı!")
    exit()

extract_dir = "/Users/erenalikoca/Desktop/Uyg2/makesense_extract"
os.makedirs(extract_dir, exist_ok=True)

print("\n📦 ZIP dosyası çıkartılıyor...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

train_labels = "/Users/erenalikoca/Desktop/Uyg2/yolo_dataset/train/labels"
val_labels = "/Users/erenalikoca/Desktop/Uyg2/yolo_dataset/val/labels"

txt_files = [f for f in os.listdir(extract_dir) if f.endswith('.txt')]

if not txt_files:
    print("❌ ZIP içinde .txt dosyası bulunamadı!")
    exit()

print(f"\n✅ {len(txt_files)} etiket dosyası bulundu")

train_images = set(os.path.splitext(f)[0] for f in os.listdir("/Users/erenalikoca/Desktop/Uyg2/yolo_dataset/train/images"))
val_images = set(os.path.splitext(f)[0] for f in os.listdir("/Users/erenalikoca/Desktop/Uyg2/yolo_dataset/val/images"))

train_count = 0
val_count = 0

for txt_file in txt_files:
    basename = os.path.splitext(txt_file)[0]
    src = os.path.join(extract_dir, txt_file)
    
    if basename in train_images:
        shutil.copy(src, os.path.join(train_labels, txt_file))
        train_count += 1
    elif basename in val_images:
        shutil.copy(src, os.path.join(val_labels, txt_file))
        val_count += 1

print(f"\n📊 Sonuçlar:")
print(f"  ✅ Train etiketleri: {train_count}")
print(f"  ✅ Val etiketleri: {val_count}")
print(f"\n🎉 İşlem tamamlandı! Artık yolo_training.ipynb'yi çalıştırabilirsin.")
