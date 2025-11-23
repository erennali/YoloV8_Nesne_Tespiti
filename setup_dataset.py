import os
import shutil
import random

# Define paths
source_dir = "/Users/erenalikoca/Desktop/Uyg2/dataset"
dest_dir = "/Users/erenalikoca/Desktop/Uyg2/yolo_dataset"
classes = ["airpods", "magic_mouse"]

# Create directories
for split in ["train", "val"]:
    for dtype in ["images", "labels"]:
        os.makedirs(os.path.join(dest_dir, split, dtype), exist_ok=True)

# Process each class
for class_name in classes:
    class_dir = os.path.join(source_dir, class_name)
    if not os.path.exists(class_dir):
        print(f"Directory not found: {class_dir}")
        continue
        
    images = [f for f in os.listdir(class_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)
    
    split_idx = int(len(images) * 0.8)
    train_images = images[:split_idx]
    val_images = images[split_idx:]
    
    for img in train_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(dest_dir, "train", "images", img))
        
    for img in val_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(dest_dir, "val", "images", img))

print("Dataset structure created at", dest_dir)
