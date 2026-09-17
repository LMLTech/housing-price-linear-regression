# 🏡 Dự Báo Giá Bất Động Sản

## Real Estate Price Prediction

### 📌 Giới thiệu

**Dự báo giá bất động sản (Real Estate Price Prediction)** là dự án xây dựng mô hình học máy nhằm dự đoán giá bất động sản dựa trên các đặc điểm của tài sản và thông tin vị trí.

Đề tài sử dụng **Multiple Linear Regression (Hồi quy tuyến tính đa biến)** để xây dựng mô hình dự báo. Quy trình được triển khai theo một pipeline Data Science gồm các bước: tìm hiểu dữ liệu, làm sạch dữ liệu, phân tích khám phá (EDA), xây dựng đặc trưng, huấn luyện mô hình, đánh giá kết quả và kiểm định mô hình.

Bên cạnh phần Machine Learning, dự án được phát triển thành một **Web Application** sử dụng **FastAPI** cho Backend và **Angular** cho Frontend, cho phép người dùng nhập thông tin bất động sản và thực hiện dự báo giá trực tiếp trên giao diện web.

Link kaggel: https://www.kaggle.com/datasets/cresht2606/vietnam-real-estate-datasets-catalyst
---

## 🎯 Mục tiêu dự án

Dự án được thực hiện với các mục tiêu chính:

* Khám phá và phân tích bộ dữ liệu bất động sản.
* Làm sạch dữ liệu và xử lý các giá trị không hợp lệ dựa trên kiến thức miền (domain knowledge).
* Phân tích mối quan hệ giữa đặc điểm bất động sản, vị trí và giá bán.
* Xây dựng các đặc trưng phục vụ mô hình, bao gồm thông tin khu vực và khoảng cách đến khu vực trung tâm.
* Xây dựng mô hình **Multiple Linear Regression** bằng Scikit-learn.
* Đánh giá mô hình bằng các chỉ số **MAE, RMSE, R² và MAPE**.
* Phân tích residual và các trường hợp dự báo sai lớn.
* Thực hiện kiểm định chéo (Cross-Validation) và audit mô hình.
* Tích hợp mô hình Machine Learning vào Web Application thông qua REST API.

---

# 📂 Cấu trúc dự án

Dự án được tổ chức theo cấu trúc Data Science kết hợp Machine Learning và Web Application:

```text
RealEstatePrediction/
│
├── data/
│   ├── raw/
│   │   └── house_buying_dec29th_2025.csv em đã đổi thành dataset_BDS.xlsx
│   │       # Dữ liệu bất động sản ban đầu
│   │
│   └── processed/
│       ├── housing_clean.csv
│       ├── housing_features.csv
│       └── predictions.csv
│       # Dữ liệu sau khi làm sạch, tạo đặc trưng
│       # và kết quả dự báo
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   │   # Phase 1: Tìm hiểu và thống kê dữ liệu
│   │
│   ├── 02_data_cleaning.ipynb
│   │   # Phase 2: Làm sạch dữ liệu và kiểm tra
│   │
│   ├── 03_eda.ipynb
│   │   # Phase 3: Exploratory Data Analysis
│   │
│   ├── 04_feature_engineering.ipynb
│   │   # Phase 4: Xây dựng và lựa chọn đặc trưng
│   │
│   ├── 05_model_training.ipynb
│   │   # Phase 5-6: Chia dữ liệu và huấn luyện mô hình
│   │
│   ├── 06_evaluation.ipynb
│   │   # Phase 7-8: Đánh giá và phân tích sai số
│   │
│   └── 07_model_audit_and_improvement.ipynb
│       # Audit mô hình, phân tích nguyên nhân và kiểm định
│
├── src/
│   ├── preprocessing.py
│   │   # Nạp dữ liệu và xử lý dữ liệu đầu vào
│   │
│   ├── features.py
│   │   # Xử lý thông tin vị trí và xây dựng đặc trưng
│   │
│   ├── train.py
│   │   # Xây dựng và huấn luyện Machine Learning Pipeline
│   │
│   ├── evaluate.py
│   │   # Đánh giá mô hình và phân tích sai số
│   │
│   ├── predict.py
│   │   # Dự báo giá cho dữ liệu mới
│   │
│   └── visualization.py
│       # Các hàm trực quan hóa dữ liệu và kết quả
│
├── models/
│   └── linear_regression.pkl
│       # Pipeline Linear Regression đã được huấn luyện
│
├── reports/
│   └── figures/
│       # Các biểu đồ phục vụ phân tích và đánh giá
│
├── backend/
│   └── main.py
│       # FastAPI Backend
│
├── frontend/
│       # Angular Frontend
│
├── SPECIFICATION.md
│   # Yêu cầu kỹ thuật và quy chuẩn dự án
│
├── requirements.txt
│   # Danh sách thư viện Python
│
└── README.md
    # Tài liệu hướng dẫn dự án
```

---

# 🔬 Quy trình thực hiện

Dự án được triển khai theo các giai đoạn chính:

```text
Raw Data
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Model Audit & Improvement
   ↓
FastAPI Backend
   ↓
Angular Frontend
```

### 1. Data Understanding

Tìm hiểu cấu trúc bộ dữ liệu, kiểu dữ liệu, số lượng bản ghi, thống kê mô tả và phân bố của biến mục tiêu.

### 2. Data Cleaning

Thực hiện xử lý dữ liệu trước khi đưa vào mô hình, bao gồm:

* Kiểm tra dữ liệu thiếu.
* Kiểm tra kiểu dữ liệu.
* Kiểm tra các giá trị bất thường.
* Lọc các giá trị không hợp lệ dựa trên domain knowledge.
* Kiểm soát nguy cơ **data leakage**.

### 3. Exploratory Data Analysis

Phân tích mối quan hệ giữa giá bất động sản với:

* Diện tích.
* Số phòng ngủ.
* Khu vực.
* Quận/huyện.
* Khoảng cách đến trung tâm.
* Giá trên mỗi mét vuông.

Ngoài ra, dự án sử dụng các biểu đồ phân phối, scatter plot, boxplot và residual plot để hỗ trợ quá trình phân tích.

### 4. Feature Engineering

Các đặc trưng được xây dựng và xử lý trước khi huấn luyện mô hình, trong đó có:

* Province.
* District.
* Khoảng cách đến CBD.
* Diện tích.
* Số phòng ngủ.
* Các thuộc tính khác của bất động sản.

Khoảng cách từ bất động sản đến CBD được tính bằng **Haversine Distance** dựa trên tọa độ địa lý.

### 5. Model Training

Dữ liệu được chia thành:

* **80% Training Set**
* **20% Test Set**

Mô hình sử dụng:

**Multiple Linear Regression**

Pipeline được xây dựng bằng Scikit-learn với các thành phần chính:

* `ColumnTransformer`
* `StandardScaler`
* `OneHotEncoder`
* `LinearRegression`

### 6. Model Evaluation

Mô hình được đánh giá bằng các chỉ số:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² (Coefficient of Determination)**
* **MAPE (Mean Absolute Percentage Error)**

Bên cạnh các chỉ số định lượng, dự án còn phân tích residual và các trường hợp có sai số dự báo lớn.

### 7. Model Audit & Improvement

Giai đoạn cuối tập trung kiểm tra độ ổn định và các hạn chế của mô hình thông qua:

* Root Cause Analysis.
* Controlled Experiments.
* Cross-Validation.
* Phân tích các prediction errors lớn nhất.
* Kiểm tra prediction âm.
* Final Verification.

---

# 🎨 Hệ thống trực quan hóa

Dự án tích hợp lớp trực quan hóa tại:

```text
src/visualization.py
```

Hệ thống gồm **15 biểu đồ**, được chia thành 5 nhóm.

## Group A — Dataset Overview

### `01_price_distribution.png`

Phân phối giá bất động sản trong dữ liệu gốc.

Kết quả cho thấy biến giá có độ lệch phải lớn (**Skewness = 8.16**).

### `02_log_price_distribution.png`

Phân phối giá sau khi áp dụng biến đổi:

```python
log1p(price)
```

Biểu đồ được sử dụng để quan sát sự thay đổi phân phối của biến mục tiêu sau phép biến đổi log.

---

## Group B — Property Characteristics

### `03_area_vs_price.png`

Biểu đồ Scatter Plot thể hiện mối quan hệ giữa diện tích bất động sản và giá.

### `04_price_by_bedrooms.png`

Boxplot thể hiện sự phân bố giá theo số lượng phòng ngủ.

### `05_price_by_area_bucket.png`

So sánh giá trung vị và số lượng bất động sản theo từng nhóm diện tích.

---

## Group C — Location & Distance

### `06_avg_price_by_district.png`

Top 10 quận/huyện có giá bất động sản trung bình cao nhất trong bộ dữ liệu.

### `07_median_price_per_m2_by_district.png`

Top 10 quận/huyện có giá trung vị trên mỗi mét vuông cao nhất.

> Biểu đồ này được sử dụng cho mục đích **EDA**, không được sử dụng trực tiếp làm đặc trưng của mô hình nếu gây ra nguy cơ data leakage.

### `08_distance_vs_price.png`

Biểu đồ thể hiện mối quan hệ giữa khoảng cách đến CBD và giá bất động sản.

### `09_price_by_distance_bucket.png`

So sánh giá trung vị và số lượng bất động sản theo từng khoảng cách đến CBD.

---

## Group D — Model Performance

### `10_actual_vs_predicted.png`

So sánh giá thực tế và giá được mô hình dự đoán.

### `11_residual_distribution.png`

Phân phối residual được tính theo:

```text
Residual = Actual Price - Predicted Price
```

### `12_residual_vs_predicted.png`

Biểu đồ residual theo giá dự đoán, được sử dụng để kiểm tra hiện tượng **heteroscedasticity** và các dạng sai lệch của mô hình.

---

## Group E — Error Analysis

### `13_absolute_error_distribution.png`

Phân phối sai số tuyệt đối:

```text
|Actual - Predicted|
```

### `14_error_by_price_range.png`

Phân tích **MAE** và **RMSE** theo từng khoảng giá thực tế.

### `15_top_prediction_errors.png`

Hiển thị 20 trường hợp có sai số dự báo lớn nhất.

Các thông tin có khả năng nhận diện cá nhân (**PII**) được loại bỏ khỏi biểu đồ.

---

# ⚙️ Cài đặt môi trường

## Yêu cầu

Môi trường cần đáp ứng:

* Python **3.8 trở lên**
* pip
* Node.js và npm nếu chạy Frontend Angular

## Cài đặt thư viện Python

Từ thư mục gốc của dự án, chạy:

```bash
pip install -r requirements.txt
```

---

# 🚀 Thực thi dự án

## 1. Chạy các Notebook

Các Notebook cần được thực hiện theo đúng thứ tự:

```text
01_data_understanding.ipynb
        ↓
02_data_cleaning.ipynb
        ↓
03_eda.ipynb
        ↓
04_feature_engineering.ipynb
        ↓
05_model_training.ipynb
        ↓
06_evaluation.ipynb
        ↓
07_model_audit_and_improvement.ipynb
```

Có thể mở project bằng **Jupyter Notebook** hoặc **JupyterLab** và chạy lần lượt từng notebook.

---

# 📊 Kết quả đánh giá mô hình

Mô hình **Multiple Linear Regression** được đánh giá trên tập Test gồm:

**N = 9,172 mẫu**

## Raw Model Output

Kết quả trực tiếp từ phương trình hồi quy:

```text
R²   = 0.3729
MAE  = 8,417.93 triệu VNĐ
RMSE = 21,435.74 triệu VNĐ
```

So với baseline cũ có **R² = 0.3017**, mô hình đạt **R² = 0.3729**, tương ứng mức tăng khoảng **7.12% theo cách tính được sử dụng trong dự án**.

Mô hình tạo ra:

```text
Negative Predictions = 747 mẫu
Tỷ lệ                  = 8.14%
```

---

## Post-Processed Output

Để đảm bảo giá dự báo không âm, kết quả được hậu xử lý bằng:

```python
np.maximum(pred, 0)
```

Kết quả sau hậu xử lý:

```text
R²   = 0.3839
MAE  = 8,065.00 triệu VNĐ
RMSE = 21,247.69 triệu VNĐ
```

Số lượng dự báo âm trước khi hậu xử lý:

```text
747 mẫu
≈ 8.14% tập Test
```

Sau hậu xử lý, các giá trị này được đưa về 0.

---

## 5-Fold Cross-Validation

Mô hình được kiểm tra thêm bằng **5-Fold Cross-Validation** trên tập Training:

```text
CV Mean R² = 0.3665
CV Std      = 0.0387
```

Kết quả Cross-Validation được sử dụng để kiểm tra mức độ ổn định của mô hình giữa các fold và đối chiếu với kết quả trên Test Set.

---

# 🌐 Web Application

Dự án được mở rộng thành Web Application với kiến trúc:

```text
Angular Frontend
       ↓
REST API
       ↓
FastAPI Backend
       ↓
Machine Learning Pipeline
       ↓
Linear Regression Model
       ↓
Prediction
```

## Backend — FastAPI

Backend được xây dựng bằng **FastAPI**, chịu trách nhiệm:

* Cung cấp REST API.
* Nhận thông tin bất động sản từ Frontend.
* Thực hiện preprocessing.
* Chạy Machine Learning Pipeline.
* Trả về kết quả dự báo.
* Cung cấp các API phục vụ Dashboard và Visualization.

### Khởi động Backend

Từ thư mục gốc của dự án:

```bash
uvicorn backend.main:app --reload --port 8000
```

Backend mặc định chạy tại:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

Health Check:

```text
http://localhost:8000/api/health
```

---

# 🖥️ Frontend — Angular

Frontend được xây dựng bằng **Angular + TypeScript**, cung cấp giao diện để người dùng:

* Nhập thông tin bất động sản.
* Thực hiện dự báo giá.
* Xem kết quả dự báo.
* Xem Dashboard.
* Theo dõi các biểu đồ phân tích.
* Xem thông tin và chỉ số của mô hình.

## Khởi động Frontend

Di chuyển vào thư mục:

```bash
cd frontend
```

Cài đặt dependencies nếu cần:

```bash
npm install
```

Khởi chạy Angular:

```bash
npm start
```

Frontend mặc định chạy tại:

```text
http://localhost:4200
```

---

# 🧭 Các trang chính của Web Application

| Route            | Chức năng                                                 |
| ---------------- | --------------------------------------------------------- |
| `/`              | Trang chủ, giới thiệu dự án và quy trình Machine Learning |
| `/predict`       | Nhập thông tin bất động sản và thực hiện dự báo giá       |
| `/visualization` | Dashboard với 15 biểu đồ phân tích                        |
| `/model`         | Thông tin mô hình, chỉ số đánh giá và các hạn chế         |

---

# ⚠️ Hạn chế của mô hình

Mô hình hiện tại sử dụng **Multiple Linear Regression**, do đó vẫn tồn tại một số hạn chế:

* Quan hệ giữa các đặc trưng và giá bất động sản có thể không hoàn toàn tuyến tính.
* Thị trường bất động sản chịu ảnh hưởng bởi nhiều yếu tố chưa được đưa vào dữ liệu.
* Mô hình vẫn xuất hiện một số trường hợp dự báo có sai số lớn.
* Một số prediction ban đầu có giá trị âm và cần được hậu xử lý.
* Giá bất động sản có phân phối lệch phải mạnh.
* R² trên Test Set cho thấy mô hình mới giải thích được một phần biến thiên của giá, do đó không nên xem kết quả dự báo là giá thị trường chính xác tuyệt đối.

Vì vậy, kết quả của mô hình nên được sử dụng như **một công cụ hỗ trợ ước lượng**, không phải giá định giá chính thức của bất động sản.

---

# 🛠️ Công nghệ sử dụng

### Data Science & Machine Learning

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook

### Backend

* FastAPI
* Uvicorn
* Python

### Frontend

* Angular
* TypeScript
* HTML
* CSS

### Machine Learning

* Multiple Linear Regression
* Train/Test Split
* Cross-Validation
* Feature Engineering
* One-Hot Encoding
* Standardization
* Model Evaluation
* Residual Analysis

---

# 📚 Tài liệu liên quan

Các yêu cầu kỹ thuật và quy chuẩn chi tiết của dự án được trình bày trong:

```text
SPECIFICATION.md
```

Danh sách thư viện cần thiết:

```text
requirements.txt
```

---

# 👥 Đóng góp

Dự án được xây dựng nhằm phục vụ mục đích **học tập, nghiên cứu và thực hành quy trình xây dựng một hệ thống Machine Learning hoàn chỉnh**, từ xử lý dữ liệu, xây dựng mô hình đến triển khai mô hình trên Web Application.

---

# 📄 License

Dự án được sử dụng cho mục đích học tập và nghiên cứu.
