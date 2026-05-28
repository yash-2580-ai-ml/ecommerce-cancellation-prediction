# ecommerce-cancellation-prediction
An end-to-end data pipeline using Pandas and Logistic Regression to predict e-commerce revenue risk.
# 🛒 NEXUS: Predictive Revenue & Risk Ingestion Engine

## 📌 Project Overview
NEXUS is an end-to-end machine learning engineering pipeline designed to predict transaction cancellation risks before order fulfillment. The system automates relational data ingestion, handles extreme dataset class imbalance, scales incoming behavioral features, and deploys a live, production-grade enterprise dashboard interface to help operations teams flag revenue leakage in real-time.

---

## 🚀 Live Production Application
* **Interactive Cloud Application:** [PASTE YOUR LIVE HUGGING FACE SPACE LINK HERE]

---

## ⚙️ Core Architecture & Data Lifecycle

### 1. Relational Data Ingestion & Preservation
* **Strategy:** Implemented a robust data ingestion workflow using Pandas **Left Joins** across separate `orders`, `items`, and `payments` transactional logs. 
* **The Engineering Choice:** Using a Left Join instead of an Inner Join preserved over **1,200 structural cancellation instances** that would have otherwise been stripped out due to missing downstream payment or logistics links.

### 2. Missing Value Imputation
* **Strategy:** Handled early-stage transaction dropouts by imputing logical `0` values for missing `price` and `freight_value` features rather than executing a generic drop. This kept over 650 high-signal cancellation instances safely within the training pool.

### 3. Feature Scaling & Standardization
* **Strategy:** Deployed Scikit-Learn's `StandardScaler` to transform `price`, `freight_value`, and `payment_installments` into normalized uniform arrays. This normalization neutralized scale magnitude differences, allowing the algorithm to assign accurate math weights.

### 4. Predictive Modeling Engine
* **Strategy:** Trained a binary **Logistic Regression** model optimized using the Sigmoid function to compress multi-feature arrays into clean fractional probability metrics scaled between `0.0` (Fulfillment Success) and `1.0` (Cancellation Risk).

---

## 📊 Business Performance & Analytical Insights

* **The Core Revenue Discovery:** During exploratory data analysis (EDA), grouping data revealed that successful conversions averaged an order price of **120.62**, whereas canceled transactions sat at a stark average of **3.08**. 
* **Strategic Takeaway:** This variance proves customers drop out on low-value items, signaling that a high shipping fee-to-product cost ratio serves as the primary transaction friction point.
* **Model Accuracy:** The final operational pipeline achieved a robust evaluation accuracy score of **94.69%** on unseen test data.

---

## 📁 Repository Contents & Directory Hygiene
* `analysis.ipynb` — Data ingestion matrix, cleaning steps, exploratory analytics, and model training script.
* `app.py` — Production-ready UI routing user-facing sliders to the scaled ML backend.
* `logistic_model.pkl` — Serialized binary predictive model weights.
* `scaler.pkl` — Serialized parameter transformation array.
* `.gitignore` — Standardized Python environment optimization tracking rule block.
* `LICENSE` — Secured under the open-source open-permissive MIT framework.

---

## 🛠️ Technical Stack Summary
* **Languages:** Python, SQL, CSS
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Logistic Regression, StandardScaler, Model Selection)
* **Production Deployment:** Streamlit Web Engine, Hugging Face Cloud Spaces Containerization
