import streamlit as st
from PIL import Image
import os
import subprocess
import pandas as pd

st.set_page_config(page_title="🍱 음식 탐지", layout="centered")
st.title("🍱 음식 이미지 인식")

# 클래스 이름 불러오는 함수
def load_class_names(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# 모델 - 클래스 파일 매핑
model_to_classfile = {
    "food_1_best.pt": "classes_food1.txt",
    "food_2_best.pt": "classes_food2.txt",
    "food_3_best.pt": "classes_food3.txt"
}

# 이미지 업로드
st.subheader("1️⃣ 음식 이미지 업로드")
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = "input.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(Image.open(image_path), caption="업로드한 이미지", use_column_width=True)

    best_conf = -1
    best_info = None  # (model_name, class_id, class_name, confidence)
    best_result_img_path = None  # 🔧 결과 이미지 경로 저장

    for model_name, class_file in model_to_classfile.items():
        st.info(f"🔍 {model_name} 실행 중...")
        command = [
            "python", "yolov5/detect.py",
            "--weights", model_name,
            "--img", "640",
            "--conf", "0.25",
            "--source", image_path,
            "--save-txt",
            "--save-conf",
            "--project", "runs/detect",
            "--name", f"exp_{model_name}",
            "--exist-ok"
        ]
        subprocess.run(command, capture_output=True)

        label_path = f"runs/detect/exp_{model_name}/labels/input.txt"
        result_image_path = f"runs/detect/exp_{model_name}/input.jpg"  # 🔧 결과 이미지 경로
        if os.path.exists(label_path):
            class_names = load_class_names(class_file)
            with open(label_path, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) != 6:
                        continue
                    cid, conf = int(parts[0]), float(parts[5])
                    if cid < len(class_names) and conf > best_conf:
                        best_conf = conf
                        best_info = (model_name, cid, class_names[cid], conf)
                        best_result_img_path = result_image_path  # 🔧 최고 결과 이미지도 저장

    if best_info:
        model_name, cid, class_name, conf = best_info
        st.success(f"✅ 최고 신뢰도 음식: **{class_name}** ({conf:.2f}, {model_name})")

        if best_result_img_path and os.path.exists(best_result_img_path):
            st.image(best_result_img_path, caption="🖼️ 탐지된 이미지 (바운딩 박스 포함)", use_column_width=True)


        # 영양정보 CSV 로드
        df = pd.read_csv("음식별 영양 성분 정보.csv")
        row = df[df["영문이름"] == class_name]
        if not row.empty:
            row = row.iloc[0]
            st.markdown(f"**음식명:** {row['식품명']} ({row['영문이름']})")
            st.markdown(f"""
            - 에너지: {row['에너지(kcal)']} kcal  
            - 단백질: {row['단백질(g)']} g  
            - 지방: {row['지방(g)']} g  
            - 탄수화물: {row['탄수화물(g)']} g  
            - 당류: {row['당류(g)']} g  
            - 식이섬유: {row['식이섬유(g)']} g  
            - 나트륨: {row['나트륨(mg)']} mg  
            - 콜레스테롤: {row['콜레스테롤(mg)']} mg
            """)

            # 당뇨 위험 성분 확인
            st.subheader("🚨 당뇨 기준 위험 성분 체크")
            warnings = []
            if row['탄수화물(g)'] >= 30:
                warnings.append("⚠️ 탄수화물 30g 이상")
            if row['당류(g)'] >= 10:
                warnings.append("⚠️ 당류 10g 이상")
            if row['지방(g)'] >= 15:
                warnings.append("⚠️ 지방 15g 이상")
            if row['콜레스테롤(mg)'] >= 100:
                warnings.append("⚠️ 콜레스테롤 100mg 이상")
            if row['나트륨(mg)'] >= 500:
                warnings.append("⚠️ 나트륨 500mg 이상")

            if warnings:
                st.warning("🚨 당뇨 환자가 피해야 할 성분:")
                for w in warnings:
                    st.write(w)
            else:
                st.success("✅ 당뇨 기준에 모두 적합한 음식입니다.")
        else:
            st.error(f"❌ CSV에 '{class_name}' 음식 정보가 없습니다.")
    else:
        st.error("❌ 3개 모델 모두에서 탐지된 음식이 없습니다.")