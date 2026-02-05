# ⚽ Football Over 2.5 Goals Prediction

## 📌 Project Description

This project focuses on building a machine learning model to predict whether a football match will have **over 2.5 goals** based on historical data and league statistics.

The objective is to analyze past matches, extract useful patterns, and generate predictions that can support sports analytics and decision-making.

---

## 📊 Dataset

The project uses the following datasets:

* `historico_partidos.csv` → Historical match data
* `leagues.csv` → League information
* `seasons.csv` → Season data
* `partidos_en_vivo.xlsx` → Live match information

These datasets contain match results, goals, leagues, and seasonal context.

---

## 🤖 Machine Learning Model

A supervised learning model was trained to classify matches into:

* **1** → Over 2.5 goals
* **0** → Under 2.5 goals

The trained model is saved as:

* `model_over25.pkl`

This allows fast reuse without retraining.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook / Google Colab
* GitHub

---

## 📁 Project Structure

```
football-over25-prediction/
│
├── football_over25_prediction.ipynb
├── model_over25.pkl
├── historico_partidos.csv
├── leagues.csv
├── seasons.csv
├── partidos_en_vivo.xlsx
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/pipesito1/football-over25-prediction.git
```

2. Install dependencies:

```bash
pip install pandas numpy scikit-learn
```

3. Open the notebook:

```bash
jupyter notebook football_over25_prediction.ipynb
```

4. Run all cells to train and test the model.

---

## 🎯 Project Goals

* Analyze football match data
* Build a predictive ML model
* Apply data preprocessing and feature engineering
* Generate actionable predictions
* Create a professional data science portfolio project

---

## 👨‍💻 Author

**Felipe Sepúlveda**
Data Analyst | Data Scientist

---

## 📬 Contact

If you have questions or suggestions, feel free to reach out via GitHub.

---

⭐ If you like this project, consider giving it a star!
