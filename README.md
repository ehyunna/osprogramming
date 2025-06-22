# osprogramming
##### https://drive.google.com/drive/folders/1yfcrwoKhkjcEOZf3BrRMjT95fE4ASslZ?hl=ko
##### best.pt파일의 용량이 커서 업로드되지 않아 드라이브 링크 첨부합니다. -나이현
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

### 주요 기능
- YOLOv5 기반 음식 탐지
- 업로드한 음식 이미지에 대해 바운딩 박스 표시
- 탐지된 음식의 영양 성분 조회
- 탄수화물, 당류, 지방, 콜레스테롤, 나트륨 기준 초과 여부 판단 및 경고 표시


### 프로젝트 개발 내용
- 연구 개발 내용
<p align="center"> <img width="311" alt="image" src="https://github.com/user-attachments/assets/fa8a219f-db84-4f72-ace7-89376dd27660" /> <br/> <em>그림 1. 음식 이미지 분류를 위한 딥러닝 모델 구성도</em> </p>

본 프로젝트에서는 [그림 1]과 같이 음식 이미지 분류와 영양 정보 분석 시스템을 개발하고자 하며 이를 위해 Food Recognition Module (음식 인식 모듈)과 Nutrition Analysis Module (영양정보 추론 모듈) 2개의 모듈을 구현함.

#### 1. Food Recongnition Module

<p align="center"> <img width="500" alt="사용자 입력 패널" src="https://github.com/user-attachments/assets/7703fe18-6f8c-478f-a4d1-524840857094" /> <br/> <em>그림 2. 객체 탐지 모델의 구조</em> </p>

- 현재 음식 인식 분야에서는 그림 2와 같이 객체 탐지 구조를 사용하고 있다. 본 프로젝트에서도 객체 탐지 모델인 YOLOv5를 사용하여 이를 통해 음식을 인식하고자 한다.
-총 3개의 음식 분류 모델 ('food_1_best.pt', 'food_2_best.pt', 'food_3_best.pt')을 구성
-각각 약 13~14개의 음식 클래스를 Roboflow 기반 dataset에서 labelling 및 agumentation진행
-클래스 목록은 각각 'classes_food1.txt', 'classes_food2.txt', 'classes_food3.txt'에 저장됨

#### 2. Nutrition Analysis Module 
- 탐지된 음식명을 기반으로 영양 정보를 자동 조회·분석하는 모듈 개발 및 구현
<p align="center">
  <img width="500" alt="수면 추천 결과 화면" src="https://github.com/user-attachments/assets/92d0866c-7fa7-4701-aff9-02f175ea3b5f" />
  <br/>
  
  <em>그림 3. pandas 기반 데이터 분석 로직</em>
</p>

Pandas 라이브러리를 활용하여 사전에 구축된 엑셀 파일을 불러와 표 형식의 데이터를 로딩
 · 엑셀 내부에는 항목 이름(예: 김밥, 비빔밥 등)과 관련 수치 정보가 테이블 형태로 저장되어있으며, 이를 자동 인식 및 매핑할 수 있도록 설계

 #### 사용 기술 스택 
<pre>- Python 3.8+
- YOLOv5 
- Streamlit
- Pandas 
- OpenCV, Pillow 
</pre>

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
├── input.jpg
├── 음식별 영양 성분 정보.csv      
└── runs/                          
</pre>
#### 필수 패키지 설치
#### YOLOv5 및 필수 환경 설치

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

pip install streamlit Pillow pandas torch>=1.7 opencv-python matplotlib pyyaml
```



#### 사용 방법 
app.py 실행 이후 visual studio code terminal에서  
```bash 
cd "프로젝트_디렉토리"
streamlit run app.py
```

이후 이미지 업로드


 
### 사용 예시

사용자가 음식 사진을 업로드하면, 아래와 같은 결과가 출력됩니다.  
이미지는 YOLOv5 탐지 결과와 Streamlit 분석 결과로 구성되어 있습니다.

---

#### 예시 1: 콩자반

<p align="center">
  <img width="500" alt="콩자반 탐지 결과" src="https://github.com/user-attachments/assets/03f2c743-9c37-488f-b654-6754ba21fc73" />
  <br/>
  <em>그림 4-1. '콩자반' YOLOv5 탐지 결과</em>
</p>

<p align="center">
  <img width="500" alt="콩자반 영양 정보" src="https://github.com/user-attachments/assets/9973098e-76f1-4ac7-a509-1b7b18cb6966" />
  <br/>
  <em>그림 4-2. '콩자반' 영양 정보 분석 결과</em>
</p>

- 인식된 클래스명: 콩자반  
- 신뢰도: 92.1%  
- 영양 성분 정보:  
  - 탄수화물: 35g  
  - 당류: 12g  
  - 나트륨: 520mg  
- 경고 메시지 출력: 기준 초과 항목(탄수화물, 당류, 나트륨)이 있습니다.

---

#### 예시 2: 감자채볶음

<p align="center">
  <img width="500" alt="감자채볶음 탐지 결과" src="https://github.com/user-attachments/assets/f4ccac81-728c-4487-a5fd-78cecc53cae4" />
  <br/>
  <em>그림 5-1. '감자채볶음' YOLOv5 탐지 결과</em>
</p>

<p align="center">
  <img width="500" alt="감자채볶음 영양 정보" src="https://github.com/user-attachments/assets/782630fb-f65d-4f2b-b9a9-de13008b651e" />
  <br/>
  <em>그림 5-2. '감자채볶음' 영양 정보 분석 결과</em>
</p>

- 인식된 클래스명: 감자채볶음  
- 신뢰도: 88.3%  
- 영양 성분 정보:  
  - 탄수화물: 22g  
  - 당류: 4g  
  - 나트륨: 360mg  
- 모든 항목이 기준 이하로 안전합니다.

---

#### 예시 3: 식혜 (오탐지 사례)

<p align="center">
  <img width="500" alt="식혜 탐지 결과" src="https://github.com/user-attachments/assets/0a2e5b67-c2ed-430b-9762-417a56b0d7cb" />
  <br/>
  <em>그림 6-1. '식혜' YOLOv5 탐지 결과</em>
</p>

<p align="center">
  <img width="500" alt="식혜 영양 정보" src="https://github.com/user-attachments/assets/5a1cc0af-e505-481d-9c2d-798a432e8267" />
  <br/>
  <em>그림 6-2. '식혜' 영양 정보 분석 결과</em>
</p>

- 인식된 클래스명: 김밥 (오탐지)  
- 신뢰도: 68.7%  
- 실제 음식과 다른 영양 정보가 연결됨  
- 유사 외형 클래스 혼동으로 인한 오류 발생

---

#### 예시 4: 어묵볶음 (오탐지 사례)

<p align="center">
  <img width="500" alt="어묵볶음 탐지 결과" src="https://github.com/user-attachments/assets/3c902e67-0aaf-43a1-9fa8-8200cf0b7f62" />
  <br/>
  <em>그림 7-1. '어묵볶음' YOLOv5 탐지 결과</em>
</p>

<p align="center">
  <img width="500" alt="어묵볶음 영양 정보" src="https://github.com/user-attachments/assets/39e23183-84ca-4a3c-92e5-e95555851885" />
  <br/>
  <em>그림 7-2. '어묵볶음' 영양 정보 분석 결과</em>
</p>

- 인식된 클래스명: 감자채볶음 (오탐지)  
- 신뢰도: 67.4%  
- 실제 음식과 무관한 정보가 표시됨  
- 잘못된 분석 결과로 인해 주의가 필요함

---



