import os
import shutil
import zipfile

roboflow_zip = input("Roboflow'dan indirdiğin ZIP dosyasının tam yolunu yapıştır: ")

if not os.path.exists(roboflow_zip):
    print("Dosya bulunamadı!")
    exit()

extract_path = "/Users/erenalikoca/Desktop/Uyg2/roboflow_export"
os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(roboflow_zip, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

train_labels_src = os.path.join(extract_path, "train", "labels")
val_labels_src = os.path.join(extract_path, "valid", "labels")

train_labels_dest = "/Users/erenalikoca/Desktop/Uyg2/yolo_dataset/train/labels"
val_labels_dest = "/Users/erenalikoca/Desktop/Uyg2/yolo_dataset/val/labels"

if os.path.exists(train_labels_src):
    for file in os.listdir(train_labels_src):
        shutil.copy(os.path.join(train_labels_src, file), train_labels_dest)
    print(f"✅ {len(os.listdir(train_labels_src))} train etiketi kopyalandı")

if os.path.exists(val_labels_src):
    for file in os.listdir(val_labels_src):
        shutil.copy(os.path.join(val_labels_src, file), val_labels_dest)
    print(f"✅ {len(os.listdir(val_labels_src))} validation etiketi kopyalandı")

print("\n🎉 Etiketleme tamamlandı! Artık modeli eğitebilirsin.")
