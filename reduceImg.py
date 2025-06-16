import zipfile
import os
from collections import defaultdict
import random

# 입력 폴더 경로
input_folder = r"C:\Users\나이현\Desktop\한국 음식 이미지\kfood"
max_images_per_class = 12

for filename in os.listdir(input_folder):
    if filename.endswith(".zip"):
        input_zip_path = os.path.join(input_folder, filename)
        output_zip_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}_reduced.zip")

        food_dict = defaultdict(list)

        with zipfile.ZipFile(input_zip_path, 'r') as zin:
            for file in zin.namelist():
                if file.endswith(('.jpg', '.jpeg', '.png')) and '/' in file:
                    try:
                        folder = file.split('/')[-2]
                        food_dict[folder].append(file)
                    except IndexError:
                        continue

            with zipfile.ZipFile(output_zip_path, 'w') as zout:
                for food, files in food_dict.items():
                    selected = random.sample(files, min(len(files), max_images_per_class))
                    for file in selected:
                        zout.writestr(file, zin.read(file))
