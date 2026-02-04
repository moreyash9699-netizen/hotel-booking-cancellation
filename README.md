# 🏨 Hotel Booking Cancellation Prediction System

This project predicts whether a hotel booking is likely to be canceled using Machine Learning.  
It is an end-to-end Data Science project covering data preprocessing, model building, evaluation, and deployment using Streamlit.

---

## 📌 Problem Statement

Hotel booking cancellations result in significant revenue loss for hotels.  
The objective of this project is to **predict high-risk bookings in advance** so that hotel management can take preventive actions.

---

## 🚀 Key Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Selection & Scaling
- Machine Learning Models:
  - Logistic Regression
  - Random Forest (Final Selected Model)
- Overfitting Detection & Handling
- Model Evaluation:
  - Accuracy
  - Classification Report
  - Confusion Matrix
- Interactive Streamlit Dashboard
- Real-time Prediction on User Input
- Deployed using Streamlit Community Cloud

---

## 🧠 Machine Learning Approach

- **Target Variable:** `is_canceled`
  - `0` → Not Canceled
  - `1` → Canceled

- **Final Model Used:**  
  **Regularized Random Forest Classifier**

- **Why Random Forest?**
  - Handles non-linear relationships
  - Better recall for canceled bookings
  - Overfitting controlled using tree-based regularization
  - Performs well on real-world tabular data

---

## 🖥️ Streamlit Web Application

The Streamlit application is designed for **hotel staff or hotel managers** to support decision-making.

### 🔑 Inputs Used:
- Lead Time
- ADR (Average Daily Rate)
- Deposit Type
- Market Segment
- Customer Type
- Total Special Requests
- Required Car Parking Spaces

### 🎯 Output:
- **Booking is likely to be CANCELED**
- **Booking is NOT likely to be canceled**

> ⚠️ The prediction is probabilistic and intended as a decision-support tool, not a guaranteed outcome.

---

## 📂 Project Structure

hotel-booking-cancellation/
│
├── hotel_app.py
├── hotel_cancellation_model.pkl
├── model_features.pkl
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- HTML & CSS (for UI styling)

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt

streamlit run hotel_app.py

👤 Author

~ YASH MORE
Internship Project – Data Science & AI/ML

🔗 **Live Application:** [https://your-app-name.streamlit.app](https://hotel-booking-cancellation-k7spyftbxggwutgmq5rj6p.streamlit.app/)


