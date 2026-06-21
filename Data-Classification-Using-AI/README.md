# Data-Classification-Using-AI

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)](https://seaborn.pydata.org/)

</div>



<br>

A beginner-friendly machine learning classification project that predicts Iris flower species using a **Decision Tree Classifier**.

This project demonstrates a complete ML workflow including **data loading, exploratory data analysis (EDA), visualization, model training, evaluation, prediction, and performance analysis**.

---

# Project Overview

This project performs end-to-end classification using the Iris dataset and covers the complete machine learning pipeline.

The system:

* Loads and explores data
* Generates visual analysis
* Trains a classification model
* Evaluates prediction performance
* Produces graphs and insights

---

# Key Highlights

* Complete machine learning workflow
* Beginner-friendly implementation
* Uses Decision Tree Classification
* Multiple visualizations included
* Performance evaluation and reporting
* Feature importance analysis

---

# Dataset Information

| Property      | Details                                              |
| ------------- | ---------------------------------------------------- |
| Dataset       | Iris Dataset                                         |
| Source        | Scikit-learn                                         |
| Total Records | 150                                                  |
| Features      | Sepal Length, Sepal Width, Petal Length, Petal Width |
| Classes       | Setosa, Versicolor, Virginica                        |

---

# Classification Model

### Algorithm Used

**Decision Tree Classifier**

A supervised machine learning algorithm used to classify flower species based on feature values.

### Model Configuration

```text
DecisionTreeClassifier(
max_depth = 3
)
```

Model depth is restricted to reduce complexity and minimize overfitting.

---

# Project Workflow

```text
Load Dataset
↓
Data Exploration
↓
Data Visualization
↓
Train-Test Split
↓
Model Training
↓
Prediction
↓
Evaluation
↓
Performance Analysis
```

---

# Model Performance

| Metric            |   Score |
| ----------------- | ------: |
| Training Accuracy |  95.83% |
| Testing Accuracy  | 100.00% |

Additional evaluation includes:

* Classification Report
* Confusion Matrix
* Feature Importance
* Overfitting Check

---

# Generated Visualizations

| File              | Purpose                       |
| ----------------- | ----------------------------- |
| `histogram.png`   | Feature distribution          |
| `boxplot.png`     | Feature spread analysis       |
| `heatmap.png`     | Correlation analysis          |
| `pairplot.png`    | Feature relationship analysis |
| `scatterplot.png` | Petal comparison              |

All graphs are stored inside the `graphs/` folder.

---

# Project Structure

```text
Data-Classification-Using-AI/
│
├── classification.py
├── README.md
├── requirements.txt
│
└── graphs/
    ├── histogram.png
    ├── boxplot.png
    ├── heatmap.png
    ├── pairplot.png
    └── scatterplot.png
```

---

# Installation Guide

Clone repository:

```bash
git clone https://github.com/anmol396/Data-Classification-Using-AI.git
```

Move to project folder:

```bash
cd Data-Classification-Using-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python classification.py
```

---

# Technologies Used

| Category         | Technology          |
| ---------------- | ------------------- |
| Language         | Python              |
| Data Processing  | Pandas, NumPy       |
| Machine Learning | Scikit-learn        |
| Visualization    | Matplotlib, Seaborn |

---

# Learning Outcomes

After completing this project:

* Understand classification workflow
* Build Decision Tree models
* Perform exploratory data analysis
* Evaluate model performance
* Generate visual insights
* Interpret feature importance

---

# Future Improvements

* Add Random Forest comparison
* Hyperparameter tuning
* Interactive dashboard
* Model deployment
* Support additional datasets

---

Developed as part of **Project 2 – Data Classification Using AI**
