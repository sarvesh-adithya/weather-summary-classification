\# 🌦️ Weather Summary Classification



\## 📌 Project Overview



This project predicts weather conditions using machine learning models trained on meteorological data.



The objective is to classify weather summaries such as:



\- Clear

\- Cloudy

\- Foggy

\- Windy

\- Other



using environmental and weather-related features.



\---



\# 🚀 Features



\- Data Cleaning and Preprocessing

\- Exploratory Data Analysis (EDA)

\- Correlation Analysis

\- Class Imbalance Analysis

\- Feature Engineering

\- Rare Class Handling

\- Model Comparison

\- Hyperparameter Tuning

\- Error Analysis

\- ROC AUC Evaluation

\- Streamlit Dashboard Deployment



\---



\# 📊 Dataset Features



The model uses the following features:



\- Temperature (C)

\- Apparent Temperature (C)

\- Humidity

\- Wind Speed (km/h)

\- Wind Bearing (degrees)

\- Visibility (km)

\- Pressure (millibars)

\- Precip Type\_snow



\---



\# 🤖 Machine Learning Models Used



\- Logistic Regression

\- Decision Tree

\- Random Forest

\- XGBoost



\---



\# 🏆 Final Model



\## Random Forest Classifier



The Random Forest model achieved the best balanced performance across classes.



\### Final Metrics



| Metric | Score |

|---|---|

| Accuracy | \~75% |

| Macro F1 Score | \~70% |

| ROC AUC Score | \~0.91 |



\---



\# 📈 Evaluation Metrics



Since the dataset is imbalanced, Macro F1 Score was used as the primary evaluation metric instead of accuracy.



Other evaluation metrics used:



\- Accuracy Score

\- Classification Report

\- Confusion Matrix

\- ROC AUC Score

\- ROC Curve



\---



\# 🔬 Ablation Study



Feature engineering was evaluated using an ablation study.



The engineered features slightly reduced performance, so they were excluded from the final model.



\---



\# 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- XGBoost

\- Matplotlib

\- Seaborn

\- Streamlit

\- Joblib



\---



\# 🖥️ Streamlit Dashboard



The project includes an interactive Streamlit dashboard where users can:



\- Enter weather conditions

\- Predict weather summary

\- View prediction confidence



\---



\# ▶️ Run the Project Locally



\## 1️⃣ Install Requirements



```bash

pip install -r requirements.txt

```



\## 2️⃣ Run Streamlit App



```bash

streamlit run weather\_app.py

```



\---



\# 📂 Project Structure



```text

Weather-Classification/

│

├── Weather Summary Classification.ipynb

├── weather\_app.py

├── model.pkl

├── requirements.txt

├── README.md

```



\---



\# 📌 Future Improvements



\- Deploy application online using Streamlit Cloud

\- Add real-time weather API integration

\- Improve minority class prediction

\- Add advanced interactive visualizations



\---



\# 👨‍💻 Author



Sarvesh Adithya M

