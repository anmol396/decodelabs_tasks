# AI-Recommendation-Logic-Tech-Stack-Recommender

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn\&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy\&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0)](https://seaborn.pydata.org/)

</div>

<br>

A Python-based recommendation engine that analyzes user skills and suggests suitable technology career paths using similarity-based scoring techniques.

The project combines **TF-IDF**, **Cosine Similarity**, and **Skill Coverage** to generate personalized recommendations, learning paths, and career insights.

---

# Project Overview

This project helps users:

* Discover matching technology career paths
* Understand current skill readiness
* Identify missing skills
* Receive personalized learning guidance
* Visualize recommendation results

---

# Key Highlights

✔ Skill-based recommendation engine
✔ TF-IDF vectorization
✔ Cosine similarity ranking
✔ Skill coverage scoring
✔ Career recommendation logic
✔ Graph generation and analysis
✔ Beginner-friendly implementation

---

# Recommendation Method

### Formula

```text
Final Score =
(0.7 × Cosine Similarity)
+
(0.3 × Skill Coverage)
```

| Component                  | Weight | Purpose                                 |
| -------------------------- | -----: | --------------------------------------- |
| TF-IDF + Cosine Similarity |    70% | Calculates similarity between skills    |
| Skill Coverage             |    30% | Calculates percentage of matched skills |

---

# Project Workflow

```text
User Skills
↓
Normalization
↓
TF-IDF
↓
Similarity Calculation
↓
Final Ranking
↓
Career Recommendation
↓
Visualization
```

---

# Dataset

The recommendation dataset contains **27 Technology Roles** and required skills.

| Domain                  | Example Roles                 |
| ----------------------- | ----------------------------- |
| Artificial Intelligence | AI Engineer, Prompt Engineer  |
| Data                    | Data Scientist, Data Analyst  |
| Cloud                   | Cloud Engineer, DevOps        |
| Development             | Backend, Frontend, Full Stack |
| Security                | Cyber Security Analyst        |
| Analytics               | Business Analyst              |
| Infrastructure          | MLOps, Cloud Architect        |

---

# Features

| Feature               | Description                         |
| --------------------- | ----------------------------------- |
| Skill Input           | Accept user technical skills        |
| Skill Normalization   | Convert abbreviations automatically |
| Recommendation Engine | Rank careers using scoring          |
| Learning Suggestions  | Show missing skills                 |
| Visualization         | Generate readable graphs            |

---

# Generated Outputs

| Output File         | Purpose                           |
| ------------------- | --------------------------------- |
| `career_scores.png` | Top recommendation comparison     |
| `skills_match.png`  | Skills matched vs skills to learn |
| `skills_gap.png`    | Learning gap analysis             |

---

# Tech Stack

| Category             | Technology                |
| -------------------- | ------------------------- |
| Programming Language | Python                    |
| Data Processing      | Pandas, NumPy             |
| Machine Learning     | Scikit-learn              |
| Recommendation Logic | TF-IDF, Cosine Similarity |
| Visualization        | Matplotlib, Seaborn       |

---

# Project Structure

```text
AI-Recommendation-Logic-Tech-Stack-Recommender/
│
├── recommender.py
├── raw_skills.csv
├── README.md
├── requirements.txt
│
└── graphs/
    ├── career_scores.png
    ├── skills_match.png
    └── skills_gap.png
```

---

## Installation Guide

Clone the repository:

```bash
git clone https://github.com/anmol396/Tech-Stack-Recommender.git
```

Open project folder:

```bash
cd Tech-Stack-Recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python recommender.py
```


---

# Sample Input

```text
Python, NLP, ML, LLM
```

# Sample Output

```text
Recommended Role → AI Engineer
Match Score → 62.4%
Suggested Learning →
DeepLearning
TensorFlow
PyTorch
FastAPI
Git
```

---

# Learning Outcomes

* Recommendation Systems
* TF-IDF Vectorization
* Cosine Similarity
* Composite Scoring
* Data Visualization
* Career Recommendation Logic

---

# Future Scope

* Streamlit Web Application
* Resume-Based Recommendation
* Interactive Dashboard
* Personalized Learning Roadmaps

---

Developed as part of **Project 3 – AI Recommendation Logic**
