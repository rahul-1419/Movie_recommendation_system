## MLops Stage

1. Update config.yaml
2. Update Schema.yaml
3. Update params.yaml
4. Update entity
5. Update the configuration.py
6. Update the components
7. Update the Pipeline
8. Update the main.py


# 🎬 Modular Movie Recommendation System 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Pipeline-orange)
![Architecture](https://img.shields.io/badge/Architecture-Modular-success)

## 📝 Project Overview
This project is an **End-to-End Machine Learning Pipeline** for a Movie Recommendation System. Instead of a single messy notebook, this project is built using production-level standards. It features a highly modular architecture, complete with custom logging, robust exception handling, and sequential pipeline execution.

The system processes raw movie data, validates it, transforms text features into vectors, and builds a recommendation model (typically using Cosine Similarity) to suggest the most relevant movies to users.

## ⚙️ Pipeline Architecture

1. **📥 Stage 1: Data Ingestion**
   - Automatically reads/downloads the raw dataset.
   - Extracts and stores the raw data into the designated artifacts folder.

2. **✅ Stage 2: Data Validation**
   - Verifies the integrity of the ingested data.
   - Checks data schemas, missing values, and ensures the dataset is ready for processing.

3. **🔄 Stage 3: Data Transformation**
   - Cleans the data and handles text preprocessing.
   - Applies feature engineering (e.g., tokenization, removing stop words, stemming).
   - Converts text data into numerical vectors using techniques like `CountVectorizer` or `TF-IDF`.

4. **🧠 Stage 4: Model Building**
   - Calculates similarities between movie vectors (e.g., Cosine Similarity).
   - Generates and saves the final model artifacts (`.pkl` files) to be used for future recommendations.

5. **Stage 5: Model Evaluation**

## 🛠️ Tech Stack & Practices
- **Language:** Python
- **Core Libraries:** Pandas, NumPy, Scikit-Learn
- **Engineering Practices:**
  - **Modular Programming:** Separation of concerns (Components, Pipelines, Entities).
  - **Custom Logging:** Tracks pipeline execution step-by-step for easy debugging.
  - **Exception Handling:** Catches and logs errors instantly across all pipeline stages.

## 🚀 How to Run Locally

Follow these steps to set up and run the pipeline on your local machine:

**1. Clone the repository:**
```bash
git clone https://github.com/rahul-1419/Movie_recommendation_system.git
cd Movie_recommendation_system
```

**2. Create a Virtual Environment:**
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Linux/Mac:
source venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**4. Execute the Training Pipeline:**
Run the main execution script to trigger the ingestion, validation, transformation, and model-building stages.
```bash
python main.py
```

## 📂 Repository Structure (Modular Setup)
```text
📦 Movie_recommendation_system
 ┣ 📂 artifacts                  # Stores data, cleaned data, and model outputs
 ┣ 📂 Movie_Recommendation_system # Main package source code
 ┃ ┣ 📂 components               # Core logic for ingestion, validation, etc.
 ┃ ┣ 📂 config                   # Configuration setup
 ┃ ┣ 📂 entity                   # Data classes and return types
 ┃ ┣ 📂 pipeline                 # Stage 01 to 04 pipeline scripts
 ┃ ┣ 📜 __init__.py              # Custom logger & exception setup
 ┣ 📜 main.py                    # Pipeline execution script
 ┣ 📜 requirements.txt           # Project dependencies
 ┗ 📜 README.md                  # Project documentation
```
