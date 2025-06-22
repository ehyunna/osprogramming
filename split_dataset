import os
import shutil
import random
from collections import defaultdict
from tqdm import tqdm

# 현재 경로
image_input_dir = "train/images"
label_input_dir = "train/labels"

# 새로운 경로
for split in ["train", "val", "test"]:
    os.makedirs(f"images/{split}", exist_ok=True)
    os.makedirs(f"labels/{split}", exist_ok=True)

# 클래스별 분류
class_to_files = defaultdict(list)

for label_file in os.listdir(label_input_dir):
    label_path = os.path.join(label_input_dir, label_file)
    with open(label_path, "r") as f:
        lines = f.readlines()
        if not lines:
            continue
        class_id = lines[0].strip().split()[0]
        image_file = label_file.replace(".txt", ".jpg")
        if os.path.exists(os.path.join(image_input_dir, image_file)):
            class_to_files[class_id].append(label_file)

# 이미지 데이터 8:1:1 분할 (train : valid : test)
for class_id, label_files in tqdm(class_to_files.items()):
    random.shuffle(label_files)
    total = len(label_files)
    n_train = int(total * 0.8)
    n_val = int(total * 0.1)

    for i, file in enumerate(label_files):
        if i < n_train:
            split = "train"
        elif i < n_train + n_val:
            split = "val"
        else:
            split = "test"

        src_img = os.path.join(image_input_dir, file.replace(".txt", ".jpg"))
        src_lbl = os.path.join(label_input_dir, file)

        dst_img = os.path.join("images", split, file.replace(".txt", ".jpg"))
        dst_lbl = os.path.join("labels", split, file)

        shutil.copy(src_img, dst_img)
        shutil.copy(src_lbl, dst_lbl)
