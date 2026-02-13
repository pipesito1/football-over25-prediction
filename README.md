<p align="center">
  <img src="images/project_cover.png" width="900">
</p>

# ⚽ Football Over 2.5 Goals Prediction App

## 🔗 Live Demo
👉 (https://football-over25-prediction-f5bwhjenxgqzdhhappmqxky.streamlit.app/)



---

## 📌 Project Overview

This project is an end-to-end machine learning application that predicts whether a football match will end with **Over 2.5 Goals** using live and historical match data.

It includes data ingestion from APIs, feature engineering, model training, and deployment as an interactive web app.

---

## 💼 Business Use Case

Accurate goal prediction is valuable for:

- Sports analytics teams  
- Betting risk management  
- Performance evaluation  
- Fan engagement platforms  

This project transforms raw football data into actionable insights through machine learning.

---

## 📊 Data Sources

| Source | Description |
|--------|-------------|
| API-Football | Live and historical fixtures |
| historico_partidos.csv | Processed historical matches |
| leagues.csv | League information |
| seasons.csv | Season metadata |

Data was collected, cleaned, validated, and standardized.

---

## 🧠 Methodology

This project follows a complete data science workflow:

1️⃣ API data ingestion  
2️⃣ Data cleaning & validation  
3️⃣ Feature engineering  
4️⃣ Model training  
5️⃣ Cross-validation  
6️⃣ Performance evaluation  
7️⃣ Deployment with Streamlit  

---

## 🤖 Machine Learning Model

A Random Forest classifier was trained to predict:

- **1** → Over 2.5 goals  
- **0** → Under 2.5 goals  

### Features Used

- Match minute  
- Total goals  
- Minute ratio  
- Goals per minute ratio  

### Performance

| Metric | Value |
|--------|--------|
| Accuracy | XX% |
| Precision | XX% |
| Recall | XX% |
| F1-score | XX% |


The trained model is saved using `joblib` for fast inference.

---

## 🖥️ Web Application

The Streamlit app allows users to:

✅ Input live match data  
✅ View real-time predictions  
✅ See probability scores  
✅ Explore live fixtures  

The app is deployed and publicly accessible.

---

## 🛠️ Technologies

- Python  
- Pandas / NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- API-Football  
- Streamlit  
- Joblib  
- GitHub  

---

## 📁 Project Structure


---

## ▶️ How to Run the Project

1. Clone this repository:
bash
git clone https://github.com/pipesito1/football-over25-prediction.git
2. Install dependencies:
bash
pip install pandas numpy scikit-learn
3. Open the notebook:
bash
jupyter notebook football_over25_prediction.ipynb
4. Run all cells to train and test the model.

### 1️⃣ Clone Repository

```bash
git clone https://github.com/pipesito1/football-over25-prediction.git
cd football-over25-prediction
pip install -r requirements.txt
pip install pandas numpy scikit-learn matplotlib joblib
jupyter notebook notebooks/football_over25_prediction.ipynb

```
---

## 🎯 Project Goals

* Analyze football match data
* Build a predictive ML model
* Integrate real-time data APIs
* Apply data preprocessing and feature engineering
* Generate actionable predictions
* Deploy a scalable prediction app
* Demonstrate end-to-end data science skills

---

## 👨‍💻 Author

**Felipe Sepúlveda**
Data Analyst | Data Scientist

---

## 📬 Contact

📧 jhesuafelipe24@gmail.com
If you have questions or suggestions, feel free to reach out via GitHub.

---

⭐ If you like this project, consider giving it a star!

