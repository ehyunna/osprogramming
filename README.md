## cv기반 음식 영양 정보 분석 서비스

###### Streamlit과 YOLOv5를 기반으로 사용자가 업로드한 음식 이미지를 자동 인식하고,  탐지된 음식에 대해 사전 구축된 데이터셋을 활용해 영양 성분 및 당뇨 위험도를 분석하는 웹 서비스



### 기술 개발 배경
- 고령화의 가속으로 인해 만성질환자, 특히 당뇨 환자의 수가 지속적으로 증가하고 있음.
- 질병관리청의 ‘2024 만성질환 현황과 이슈’에 따르면 우리나라 질병 부담에 가장 큰 영향을 미치는 위험 요인은 ‘영양’으로, 건강하지 못한 식습관은 당뇨, 암, 심혈관 질환 등 주요 만성질환의 주요 원인이 되고 있음.
- 이를 해결 또는 해소하기 위하여 만성질환 환자, 특히 당뇨 환자의 건강한 식생활 유도를 위한 정밀한 음식 영양 분석 기술이 중요한 대안으로 작용할 수 있음.

### 기술 개발 목표
- 만성질환을 가진 사람들의 식습관 개선을 위한 개인 맞춤형 음식 영양 분석 기술 개발을 목표로 함.
- 음식을 자동 인식하고 영양 정보를 분석하여, 당뇨 환자에게 적합한 식단인지 실시간 판단할 수 있는 AI 기반 분석 시스템 구축.
- 사용자 상태를 반영한 동적 피드백 기능 탑재로 식생활 관리 효율 극대화.
- 사회적 약자인 만성질환 환자의 자기관리 능력 향상을 통한 올바른 식습관 형성 및 심리적 자율감 고취.
- 공공 의료비 절감, 예방 중심 건강관리 전환 등 국가 보건 정책 방향과 부합하며, 고령사회 대응 역량 강화.

### 프로젝트 개발 내용
- 연구 개발 내용
<p align="center"> <img width="311" alt="image" src="https://github.com/user-attachments/assets/fa8a219f-db84-4f72-ace7-89376dd27660" /> <br/> <em>그림 1. 음식 이미지 분류를 위한 딥러닝 모델 구성도</em> </p>

본 프로젝트에서는 [그림 1]과 같이 음식 이미지 분류와 영양 정보 분석 시스템을 개발하고자 하며 이를 위해 Food Recognition Module (음식 인식 모듈)과 Nutrition Analysis Module (영양정보 추론 모듈) 2개의 모듈을 구현함.

#### 1. Food Recongnition Module

<p align="center"> <img width="500" alt="사용자 입력 패널" src="https://github.com/user-attachments/assets/7703fe18-6f8c-478f-a4d1-524840857094" /> <br/> <em>그림 2. 객체 탐지 모델의 구조</em> </p>

- 현재 음식 인식 분야에서는 그림 2와 같이 객체 탐지 구조를 사용하고 있다. 본 프로젝트에서도 객체 탐지 모델인 YOLOv5를 사용하여 이를 통해 음식을 인식하고자 한다. 

#### 2. Nutrition Analysis Module 
- 탐지된 음식명을 기반으로 영양 정보를 자동 조회·분석하는 모듈 개발 및 구현
<p align="center">
  <img width="500" alt="수면 추천 결과 화면" src="https://github.com/user-attachments/assets/92d0866c-7fa7-4701-aff9-02f175ea3b5f" />
  <br/>
  
  <em>그림 3. pandas 기반 데이터 분석 로직</em>
</p>

Pandas 라이브러리를 활용하여 사전에 구축된 엑셀 파일을 불러와 표 형식의 데이터를 로딩
 · 엑셀 내부에는 항목 이름(예: 김밥, 비빔밥 등)과 관련 수치 정보가 테이블 형태로 저장되어있으며, 이를 자동 인식 및 매핑할 수 있도록 설계

 #### 프로젝트 구조
<pre> project-root/  
├── app.py                        
├── yolov5/                         
├── food_1_best.pt                
├── food_2_best.pt  
├── food_3_best.pt  
├── classes_food1.txt              
├── classes_food2.txt  
├── classes_food3.txt  
├── 음식별 영양 성분 정보.csv      
└── runs/                          
</pre>
#### 필수 패키지 설치
## 🛠 YOLOv5 설치

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

pip install streamlit Pillow pandas torch>=1.7 opencv-python matplotlib pyyaml
```



#### 사용 방법 
app.py 실행 이후 terminal에서  
```bash 
cd "프로젝트_디렉토리"
streamlit run app.py
```

이후 이미지 업로드
 
